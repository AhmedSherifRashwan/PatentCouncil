"""Patent Council run planner: creates a run's Paperclip tasks, with dependencies, in one call.

    ~/PatentCouncil/tools/pc-plan init       --slug S --matter-issue ID --profile full|quick [--run r1]
                                             [--from P1|P2|P3|P4|P5|REVIEW --base-run r1] [--dry-run]
    ~/PatentCouncil/tools/pc-plan review     --slug S --run r1 --round 1 [--dry-run]
    ~/PatentCouncil/tools/pc-plan adjudicate --slug S --run r1 --round 1 [--dry-run]
    ~/PatentCouncil/tools/pc-plan loopback   --slug S --run r1 --round 1 [--dry-run]
    ~/PatentCouncil/tools/pc-plan package    --slug S --run r1 [--dry-run]

Every task is a child of the matter issue, assigned to its owner, and blocked by the tasks whose
outputs it reads, so Paperclip starts each one the moment its inputs exist. Nothing polls. Each
stage ends in an Orchestrator checkpoint task that runs the next stage.

Run by the Orchestrator inside its own Paperclip run (it uses PAPERCLIP_API_URL, PAPERCLIP_API_KEY,
PAPERCLIP_RUN_ID and PAPERCLIP_COMPANY_ID from that run). Prints one JSON object.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

HOME = Path.home()
MATTERS = HOME / "PatentCouncil" / "matters"
PROMPTS = HOME / "IP-Filing-Ecosystem" / "prompts"
PC = "~/PatentCouncil/tools/pc"
PHASE_ORDER = ["P1", "P2", "P3", "P4", "P5", "REVIEW"]
REVIEW_GROUPS = {
    "G1 support, amendment basis and priority": ["28", "29", "31"],
    "G2 jurisdictions and examiner red-team": ["30", "32"],
    "G3 enforcement, freedom to operate, moat and gaps": ["33", "34", "35", "36"],
    "G4 claims, specification and formal audits": ["37", "38", "40a"],
}
ROUND2_GROUPS = ["G1 support, amendment basis and priority", "G2 jurisdictions and examiner red-team",
                 "G4 claims, specification and formal audits"]


# -- Paperclip -------------------------------------------------------------------------------


class Api:
    def __init__(self, dry: bool):
        self.dry = dry
        self.base = os.environ.get("PAPERCLIP_API_URL", "http://127.0.0.1:3100").rstrip("/") + "/api"
        self.company = os.environ.get("PAPERCLIP_COMPANY_ID", "")
        self.created: list[dict] = []
        self._agents: dict[str, str] | None = None

    def call(self, method: str, path: str, body: dict | None = None):
        headers = {"Content-Type": "application/json"}
        if os.environ.get("PAPERCLIP_API_KEY"):
            headers["Authorization"] = "Bearer " + os.environ["PAPERCLIP_API_KEY"]
        if os.environ.get("PAPERCLIP_RUN_ID"):
            headers["X-Paperclip-Run-Id"] = os.environ["PAPERCLIP_RUN_ID"]
        req = urllib.request.Request(self.base + path, data=json.dumps(body).encode() if body is not None else None,
                                     headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                raw = resp.read()
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as exc:
            raise SystemExit(json.dumps({"ok": False, "error": f"{method} {path} -> {exc.code}",
                                         "body": exc.read()[:500].decode(errors="replace")}))

    def agent(self, name: str) -> str:
        if self._agents is None:
            self._agents = {a["name"]: a["id"] for a in self.call("GET", f"/companies/{self.company}/agents")}
        if name not in self._agents:
            raise SystemExit(json.dumps({"ok": False, "error": f"no agent named {name!r} in this company"}))
        return self._agents[name]

    def issue(self, matter_issue: dict, key: str, title: str, agent: str, description: str,
              blocked_by: list[str], priority: str = "medium") -> str:
        body = {"title": title, "description": description, "parentId": matter_issue["id"],
                "projectId": matter_issue.get("projectId"), "projectWorkspaceId": matter_issue.get("projectWorkspaceId"),
                "status": "todo", "priority": priority, "blockedByIssueIds": [b for b in blocked_by if b]}
        if self.dry:
            fake = f"dry-{len(self.created) + 1}"
            self.created.append({"key": key, "id": fake, "agent": agent, "title": title, "blocked_by": body["blockedByIssueIds"]})
            return fake
        body["assigneeAgentId"] = self.agent(agent)
        issue = self.call("POST", f"/companies/{self.company}/issues", body)
        self.created.append({"key": key, "id": issue["id"], "identifier": issue.get("identifier"), "agent": agent,
                             "title": title, "blocked_by": body["blockedByIssueIds"]})
        return issue["id"]

    def matter_issue(self, issue_id: str) -> dict:
        if self.dry:
            return {"id": issue_id, "projectId": None, "projectWorkspaceId": None}
        return self.call("GET", f"/issues/{issue_id}")


# -- prompts and paths -----------------------------------------------------------------------


def prompt(pid: str) -> dict:
    path = next(PROMPTS.glob(f"{pid}-*.md"), None) if pid[0].isdigit() or pid == "gate14" else PROMPTS / f"{pid}.md"
    if path is None or not path.exists():
        raise SystemExit(json.dumps({"ok": False, "error": f"prompt {pid} not found"}))
    fm = path.read_text().split("---")[1]

    def field(key):
        m = re.search(rf"^{key}:\s*(.*)$", fm, re.M)
        return m.group(1).strip().strip('"') if m else ""

    def listed(key):
        return [x.strip() for x in field(key).strip("[]").split(",") if x.strip()]

    return {"id": pid, "path": path, "kind": field("kind"), "title": field("title"),
            "inputs": listed("inputs"), "optional": listed("optional_inputs")}


class Paths:
    def __init__(self, slug: str, run: str, base_run: str | None, restart_from: str):
        self.m = MATTERS / slug
        self.r = self.m / "runs" / run
        self.base = self.m / "runs" / base_run if base_run else None
        self.restart = restart_from

    def phase_root(self, phase: str) -> Path:
        """Earlier phases than the restart point are read from the base run."""
        if self.base and PHASE_ORDER.index(phase) < PHASE_ORDER.index(self.restart):
            return self.base
        return self.r

    def out(self, phase: str, pid: str) -> Path:
        return self.phase_root(phase) / phase / f"{pid}.md"

    def spec(self, spec: str, full: bool) -> str:
        s = spec
        if s == "intake:disclosure":
            return str(self.m / "intake" / "disclosure.md")
        if s == "intake:data/*":
            return str(self.m / "intake" / "data") + "/ (if present)"
        if s == "intake:drawings":
            return str(self.m / "intake" / "drawings") + "/ (file names only, if present)"
        if s == "intake:prior-art/*":
            return (f"{self.phase_root('P2') / 'prior-art' / 'INDEX.md'} and the full texts it lists under "
                    f"{self.phase_root('P2') / 'prior-art' / 'refs'}/, plus anything the requester supplied in "
                    f"{self.m / 'intake' / 'prior-art'}/")
        if s == "intake:priority/*":
            return str(self.m / "intake" / "priority") + "/ (if present)"
        if s == "intake:gate-1-answers":
            return str(self.m / "intake" / "answers.md") + " (the inventor's answers, if any have arrived)"
        if s == "terminology":
            return str(self.phase_root("P2") / "terminology" / "LOCKED.md")
        if s == "confirmed_embodiments":
            return str(self.phase_root("P4") / "CONFIRMED.md")
        if s == "registry":
            return str(self.phase_root("P5") / "registry.json")
        if s == "out:P4/description":
            return str(self.phase_root("P5") / "description.md") + " (latest version: description.md, or the newest description.vN.md)"
        if s == "out:P5/claims":
            return str(self.phase_root("REVIEW") / "claims.md") + " (latest version: claims.md, or the newest claims.vN.md)"
        if s.startswith("out:"):
            phase, pid = s[4:].split("/")
            if full and phase == "P2" and pid == "09":
                return str(self.phase_root("P3") / "P2" / "09r.md") + " (09 as revised after the prior-art debate)"
            return str(self.out(phase, pid))
        return s  # findings/corrections/disclosure requests: named explicitly in the task body


# -- task text -------------------------------------------------------------------------------


def body(p: Paths, step: str, agent: str, profile: str, what: str, prompts: list[dict], extra_inputs: list[str],
         done: list[str], full: bool) -> str:
    lines = [f"**Patent Council · matter `{p.m.name}` · run `{p.r.name}` · step `{step}` · profile {profile}**", "",
             f"Owner: **{agent}**. Follow your AGENTS.md; this task tells you what, where and in what order.", "",
             "## What to do", "", what.strip(), ""]
    if prompts:
        lines += ["## Prompts (execute in this order; one reply file per prompt)", ""]
        for pr in prompts:
            reply = p.r / pr["phase_dir"] / f"{pr['id']}.md"
            inputs = [p.spec(s, full) for s in pr["inputs"]]
            optional = [p.spec(s, full) for s in pr["optional"] if not s.startswith(("findings:", "corrections",
                                                                                          "disclosure_requests", "open_disagreements"))]
            lines += [f"### {pr['id']} — {pr['title']}  (kind `{pr['kind']}`)",
                      f"- Prompt file: `{pr['path']}`",
                      f"- Reply file: `{reply}`",
                      "- Required inputs:", *[f"  - `{i}`" for i in inputs]]
            if optional:
                lines += ["- Optional inputs (use when present):", *[f"  - `{i}`" for i in optional]]
            lines.append("")
    if extra_inputs:
        lines += ["## Also read", "", *[f"- `{i}`" for i in extra_inputs], ""]
    lines += ["## Before you mark this done", "", *[f"- {d}" for d in done], "",
              f"Dossier: `{p.m}` · this run: `{p.r}` · tools: `{PC}` · planner: `~/PatentCouncil/tools/pc-plan`."]
    return "\n".join(lines)


CHECKS = (f"Validate every reply: `{PC} contract --kind <kind> --reply <file>`; once the lock exists also "
          f"`{PC} terms --locked <run>/terminology/LOCKED.md --reply <file> --kind <kind>`. One correction turn "
          "per failure (save the fix as `<id>.r1.md`); if it still fails, say so and mark the task blocked.")


def pr(pid: str, phase_dir: str) -> dict:
    d = prompt(pid)
    d["phase_dir"] = phase_dir
    return d


# -- stages ----------------------------------------------------------------------------------


def stage_init(args, api: Api) -> dict:
    full = args.profile == "full"
    p = Paths(args.slug, args.run, args.base_run, args.restart_from)
    if not api.dry:
        for sub in ("P1", "P2", "P3", "P4", "P5", "prior-art/refs", "terminology", "debate", "risk", "review", "loop",
                    "package", "gates"):
            (p.r / sub).mkdir(parents=True, exist_ok=True)
        (p.m / "intake").mkdir(parents=True, exist_ok=True)
    mi = api.matter_issue(args.matter_issue)
    run_meta = {"slug": args.slug, "run": args.run, "profile": args.profile, "from": args.restart_from,
                "base_run": args.base_run, "matter_issue": args.matter_issue}
    if not api.dry:
        (p.r / "run.json").write_text(json.dumps(run_meta, indent=2) + "\n")
    start = PHASE_ORDER.index(args.restart_from)
    ids: dict[str, str] = {}
    T = lambda key, title, agent, what, blocked, prompts=(), extra=(), done=(CHECKS,), prio="medium": ids.__setitem__(
        key, api.issue(mi, key, f"{args.slug} · {args.run} · {title}", agent,
                       body(p, key, agent, args.profile, what, list(prompts), list(extra), list(done), full),
                       [ids.get(b) for b in blocked], prio))

    if start <= 0:  # ---------------------------------------------------------------- P1
        T("P1a", "P1 · 01–04 invention, value map, nucleus, terminology", "Disclosure Analyst",
          "Run Prompts 01, 02, 03 and 04 in order, each reading the previous replies. Prompt 04's Terminology "
          "Table becomes the locked vocabulary at Gate 1, so make it complete.", [],
          [pr("01", "P1"), pr("02", "P1"), pr("03", "P1"), pr("04", "P1")])
        T("G1", "Gate 1 · lock terminology", "Orchestrator",
          f"Gate 1. Run `{PC} lock-terms --reply {p.r}/P1/04.md --out {p.r}/terminology/LOCKED.md`, record the "
          f"decision in `{p.r}/gates/gate-1.md` (auto-unattended unless the matter is attended; if attended, put the "
          "terminology and the reading of the disclosure to the board with request_confirmation and wait).",
          ["P1a"], done=["LOCKED.md exists and `lock-terms` reported ok.", "gate-1.md records who decided and when."])
        T("P1b", "P1 · 05 inventor interrogation and top-10 questions", "Disclosure Analyst",
          f"Run Prompt 05. Then write `{p.r}/P1/top10-questions.md`: the ten questions whose answers would change the "
          "claims most, each with 2–4 multiple-choice answers where possible plus 'other', and what each answer "
          "would change.", ["P1a"], [pr("05", "P1")])
        T("QF", "Inventor question form", "Orchestrator",
          f"Put `{p.r}/P1/top10-questions.md` to the board on the matter issue with ask_user_questions "
          f"(supersedeOnUserComment false). Do not wait for answers. When they arrive (on any later wake-up), write "
          f"them to `{p.m}/intake/answers.md` and note it in the matter issue.", ["P1b"],
          done=["The question card exists on the matter issue."], prio="low")
        T("RES1", "Prior-art search · landscape pass", "Prior-Art Researcher",
          "Landscape pass, in parallel with Phase 1. From your own reading of the disclosure, formulate GENERIC "
          "technical search queries (never disclosure text) and search patent databases and the literature. Fetch "
          f"the full text and claims of the strongest candidates into `{p.r}/prior-art/refs/` and log every query "
          f"in `{p.r}/prior-art/search-log.md`.", [],
          extra=[str(p.m / "intake" / "disclosure.md")], done=["search-log.md lists every query run and every result kept or dropped."]) if full else None
    if start <= 1:  # ---------------------------------------------------------------- P2
        T("P2a", "P2 · 06 search concept decomposition", "Prior-Art Strategist",
          "Run Prompt 06: the searchable concepts, keyword families, CPC/IPC themes and search strings the "
          "Researcher will use.", ["G1"], [pr("06", "P2")])
        T("RES2", "Prior-art search · targeted pass and index", "Prior-Art Researcher",
          "Targeted pass using Prompt 06's strings and classes. Finalise the reference set: the "
          f"{'10–20' if full else '5–8'} closest references, each saved with full text and claims in "
          f"`{p.r}/prior-art/refs/<publication-number>.md`, and `{p.r}/prior-art/INDEX.md` listing them with "
          "publication number, title, assignee, dates, URL, why it matters, and the concepts it hits.",
          ["P2a", "RES1"], extra=[str(p.r / "P2" / "06.md")],
          done=["INDEX.md lists every reference with a source URL and access date.", "Every listed reference has its full text saved."])
        T("P2b", "P2 · 07–09 charts, novelty attack, differentiation", "Prior-Art Strategist",
          "Run Prompts 07, 08 and 09 in order against the references in INDEX.md.", ["RES2"],
          [pr("07", "P2"), pr("08", "P2"), pr("09", "P2")])
        if full:
            T("D1a", "Debate 1 · attack the differentiation", "Prior-Art Researcher",
              f"Attack Prompt 09's differentiation matrix: for each claimed distinction, find the closest disclosure "
              f"(in the reference set or by new generic searches) that erodes it. Write `{p.r}/debate/d1-attack.md`: "
              "per distinction, the reference, the exact passage, and how strong the attack is. Add any newly found "
              "references to refs/ and INDEX.md.", ["P2b"], extra=[str(p.r / "P2" / "09.md"), str(p.r / "prior-art" / "INDEX.md")],
              done=["Every distinction in 09 has an attack or an explicit 'no credible attack found, searched: …'."])
            T("D1b", "Debate 1 · defend, revise 09, then 10", "Prior-Art Strategist",
              f"Answer every attack in `{p.r}/debate/d1-attack.md` in `{p.r}/debate/d1-response.md` (concede, narrow the "
              f"distinction, or rebut with the passage that proves it). Save the revised matrix as `{p.r}/P2/09r.md` "
              "(same output contract as Prompt 09). Then run Prompt 10 against 09r.", ["D1a"], [pr("10", "P2")])
        else:
            T("P2c", "P2 · 10 white space", "Prior-Art Strategist", "Run Prompt 10.", ["P2b"], [pr("10", "P2")])
    last_p2 = "D1b" if full else "P2c"
    if start <= 2:  # ---------------------------------------------------------------- P3
        dep = [last_p2] if start <= 1 else []
        for pid in ("11", "12", "13", "15"):
            T(f"P3-{pid}", f"P3 · {pid} {prompt(pid)['title'].lower()}", "Embodiment Architect",
              f"Run Prompt {pid}. Everything you produce is a candidate until Gate 2.", dep, [pr(pid, "P3")])
        T("P3-14", "P3 · 14 combination map", "Embodiment Architect", "Run Prompt 14.", ["P3-12"], [pr("14", "P3")])
        p3_all = ["P3-11", "P3-13", "P3-14", "P3-15"]
        if full:
            T("D2a", "Debate 2 · competitor escape routes", "Litigator",
              f"As a well-funded competitor, attack the Phase 3 candidate set: for each core embodiment, the cheapest "
              f"credible way to get the same commercial result outside it. Write `{p.r}/debate/d2-attack.md`.", p3_all,
              extra=[str(p.r / "P3" / f"{x}.md") for x in ("11", "12", "13", "14", "15")] + [str(p.r / "P2" / "09r.md")],
              done=["Each escape route names the embodiment it avoids and why it works commercially."])
            T("D2b", "Debate 2 · close the escape routes", "Embodiment Architect",
              f"Answer `{p.r}/debate/d2-attack.md` in `{p.r}/P3/p3-defence.md` (drafting output contract): close every "
              "escape route you legitimately can with additional candidate embodiments or broader genus language, and "
              "say plainly which ones cannot be closed without matter the inventor has not conceived.", ["D2a"])
            p3_all = ["D2b"]
        T("G2", "Gate 2 · confirm embodiments", "Orchestrator",
          f"Gate 2. Run `{PC} confirm --replies {' '.join(str(p.r / 'P3' / f'{x}.md') for x in ('11', '12', '13', '14', '15'))}"
          f"{' ' + str(p.r / 'P3' / 'p3-defence.md') if full else ''} --out {p.r}/CONFIRMED.md` (auto-unattended unless "
          "the matter is attended; if attended, put the candidates to the board and confirm only what they accept).",
          p3_all, done=["CONFIRMED.md exists; gate-2 decision recorded in gates/gate-2.md."])
        T("RISK", "Pre-drafting findings report", "Risk Analyst",
          f"Write `{p.r}/risk/pre-drafting-findings.md` from Phases 1–3 and the lessons file.", ["G2"],
          extra=[str(p.r / x) for x in ("P1/01.md", "P1/03.md", "P2/08.md", "P2/09r.md" if full else "P2/09.md", "P2/10.md",
                                         "CONFIRMED.md", "terminology/LOCKED.md")] + ["~/PatentCouncil/lessons.md"],
          done=["Every critical and high risk names its owner (P4, P5 or both) and the drafting response required."])
    if start <= 3:  # ---------------------------------------------------------------- P4
        T("P4a", "P4 · 16 specification blueprint", "Specification Drafter", "Run Prompt 16.",
          ["RISK"] if start <= 2 else [], [pr("16", "P4")], extra=[str(p.phase_root("P4") / "risk" / "pre-drafting-findings.md")])
        T("P4b", "P4 · 17 enablement audit", "Specification Drafter", "Run Prompt 17.", ["P4a"], [pr("17", "P4")])
        T("P4c", "P4 · 19 definitions", "Specification Drafter", "Run Prompt 19.", ["P4a"], [pr("19", "P4")])
        T("P4d", "P4 · 18, 20, 20a and the composed description", "Specification Drafter",
          f"Run 18, 20 and 20a in order, then `{PC} registry --reply {p.r}/P4/20a.md --out {p.r}/registry.json`, then "
          f"x-p4-compose-description → write the finished description to `{p.r}/description.md` with stable [0001]-style "
          f"paragraph numbers. Then write `{p.r}/P4/pre-drafting-response-P4.md`.", ["P4b", "P4c"],
          [pr("18", "P4"), pr("20", "P4"), pr("20a", "P4"), pr("x-p4-compose-description", "P4")],
          done=[CHECKS, f"`{PC} numerals --registry {p.r}/registry.json --description {p.r}/description.md --claims /dev/null` "
                "reports no numeral missing from the registry."])
    if start <= 4:  # ---------------------------------------------------------------- P5
        T("P5a", "P5 · 21–22 claim strategy and independent claims", "Claims Architect", "Run Prompts 21 and 22 in order.",
          ["P4d"] if start <= 3 else [], [pr("21", "P5"), pr("22", "P5")])
        T("P5b", "P5 · 23 dependent ladder", "Claims Architect", "Run Prompt 23.", ["P5a"], [pr("23", "P5")])
        T("P5c", "P5 · 24 alternative formulations", "Claims Architect", "Run Prompt 24.", ["P5a"], [pr("24", "P5")])
        T("P5d", "P5 · 25 final claim set and support map", "Claims Architect",
          f"Run Prompt 25. Write its Final Claim Set to `{p.r}/claims.md` (plain numbered claims) and build "
          f"`{p.r}/support-map.json` for every claim. Then write `{p.r}/P5/pre-drafting-response-P5.md`.", ["P5b", "P5c"],
          [pr("25", "P5")],
          done=[CHECKS, f"`{PC} support-map --description {p.r}/description.md --claims {p.r}/claims.md --map {p.r}/support-map.json`, "
                f"`{PC} claims-format --claims {p.r}/claims.md` and `{PC} antecedent --claims {p.r}/claims.md` run, results pasted into your comment."])
        T("P5e", "P5 · 26–27 functional-language audit and fallback concepts", "Claims Architect",
          "Run Prompts 26 and 27.", ["P5d"], [pr("26", "P5"), pr("27", "P5")])
        T("IL1a", "Inner loop 1 · description answers the claims", "Specification Drafter",
          f"Debate 3, round 1. Answer every `disclosure_requests` item in the envelopes of `{p.r}/P5/25.md` and "
          f"`{p.r}/P5/26.md` (x-p4-revise): add the disclosure, or answer `cannot support without new matter`. Save the "
          f"reply as `{p.r}/loop/inner-1/x-p4-revise.md` and the revised description as `{p.r}/description.v2.md` (never "
          "overwrite description.md).", ["P5d"], [pr("x-p4-revise", "loop/inner-1")])
        T("IL1b", "Inner loop 1 · claims answer the description", "Claims Architect",
          f"Debate 3, round 1. x-p5-revise against `{p.r}/description.v2.md`: tighten claims to what is now supported, "
          f"push back in `open_disagreements` where the drafter refused support you need. Save the reply as "
          f"`{p.r}/loop/inner-1/x-p5-revise.md`, the claims as `{p.r}/claims.v2.md`, and update support-map.json.",
          ["IL1a", "P5e"], [pr("x-p5-revise", "loop/inner-1")],
          done=[CHECKS, f"support-map, claims-format and antecedent re-run on claims.v2.md and description.v2.md; results in your comment."])
    T("CP-REVIEW", "Checkpoint · end of drafting", "Orchestrator",
      "Decide the second inner-loop round, then launch the review. See 'Checkpoint: end of drafting' in your AGENTS.md.",
      ["IL1b"] if start <= 4 else [], done=["The next stage's tasks exist, or the reason they do not is on the matter issue."],
      prio="high")
    return {"stage": "init", "tasks": len(api.created)}


def stage_review(args, api: Api) -> dict:
    p = Paths(args.slug, args.run, None, "P1")
    run_meta = json.loads((p.r / "run.json").read_text())
    full = run_meta["profile"] == "full"
    mi = api.matter_issue(run_meta["matter_issue"])
    rdir = p.r / "review" / f"r{args.round}"
    package = rdir / "package"
    if not (package / "claims.md").exists() and not api.dry:
        raise SystemExit(json.dumps({"ok": False, "error": f"build the review package first: {package}"}))
    reviewers = ["Examiner", "Litigator"] if full else ["Examiner"]
    groups = list(REVIEW_GROUPS) if args.round == 1 else ROUND2_GROUPS
    keys = []
    for reviewer in reviewers:
        suffix = "" if reviewer == "Examiner" else "b"
        for g in groups:
            key = f"R{args.round}-{reviewer[:3]}-{g.split()[0]}"
            prompts = [pr(x, f"review/r{args.round}") for x in REVIEW_GROUPS[g]]
            what = (f"Review round {args.round}, group {g}, as the **{reviewer}**. Read ONLY `{package}/` and the prompt "
                    f"files. Write each reply to `{rdir}/<id>{suffix}.md` and its envelope with "
                    f"`{PC} contract --kind review --reply {rdir}/<id>{suffix}.md --write-envelope {rdir}/<id>{suffix}.envelope.json`.")
            if args.round > 1:
                what += (f" This is a re-review after loop-back: `{rdir}/CHANGED.md` lists what changed. Review the whole "
                         "package, but look hardest at the changed passages and at whether earlier upheld findings are resolved.")
            body_text = body(p, key, reviewer, run_meta["profile"], what, [], [str(package)] +
                             [f"{x['path']} (reply: {rdir}/{x['id']}{suffix}.md)" for x in prompts],
                             [f"Every reply validated and its envelope written ({suffix or 'no'} suffix)."], full)
            api.issue(mi, key, f"{args.slug} · {args.run} · review r{args.round} · {reviewer} · {g}", reviewer, body_text, [])
            keys.append(api.created[-1]["id"])
    api.issue(mi, f"CP-ADJ-{args.round}", f"{args.slug} · {args.run} · Checkpoint · review r{args.round} done", "Orchestrator",
              body(p, f"CP-ADJ-{args.round}", "Orchestrator", run_meta["profile"],
                   "Merge the review and launch adjudication. See 'Checkpoint: review done' in your AGENTS.md.", [], [str(rdir)],
                   ["findings.json and findings-report.md written; adjudication tasks exist."], full),
              keys, "high")
    return {"stage": "review", "round": args.round, "tasks": len(api.created)}


OWNER_CATEGORIES = {
    "Embodiment Architect": {"novelty", "design-around"},
    "Specification Drafter": {"enablement", "support", "formal"},
    "Claims Architect": {"novelty", "design-around", "enablement", "formal"},
}


def stage_adjudicate(args, api: Api) -> dict:
    p = Paths(args.slug, args.run, None, "P1")
    run_meta = json.loads((p.r / "run.json").read_text())
    full = run_meta["profile"] == "full"
    mi = api.matter_issue(run_meta["matter_issue"])
    rdir = p.r / "review" / f"r{args.round}"
    items = json.loads((rdir / "findings.json").read_text())["findings"] if (rdir / "findings.json").exists() else []
    severe = [f for f in items if f["severity"] in ("critical", "high")]
    rebuttal_ids = []
    if full:
        for owner, cats in OWNER_CATEGORIES.items():
            mine = [f["id"] for f in severe if f["category"] in cats and
                    (owner != "Claims Architect" or f.get("claim_refs") or f["category"] != "enablement")]
            if not mine and not api.dry:
                continue
            api.issue(mi, f"RB-{args.round}-{owner.split()[0]}", f"{args.slug} · {args.run} · rebuttal r{args.round} · {owner}", owner,
                      body(p, f"RB-{args.round}", owner, run_meta["profile"],
                           f"Debate 4. For each finding id below (in `{rdir}/findings.json`), either ACCEPT it or REBUT it "
                           "with the exact paragraph or claim text that already answers it. No new drafting here. Write "
                           f"`{rdir}/rebuttals/{owner.split()[0].lower()}.json` as "
                           '`{"responses": [{"id": "F-32-1", "position": "accept|rebut", "argument": "...", "citations": ["[0042]"]}]}`.'
                           f"\n\nFindings: {', '.join(mine) or '(dry run)'}", [],
                           [str(rdir / "findings.json"), str(rdir / "package")], ["Every listed id has exactly one response."], full),
                      [])
            rebuttal_ids.append(api.created[-1]["id"])
    to_rule = items if full else severe
    batch = 40
    adj_ids = []
    for n in range(max(1, (len(to_rule) + batch - 1) // batch)):
        chunk = [f["id"] for f in to_rule[n * batch:(n + 1) * batch]]
        api.issue(mi, f"AJ-{args.round}-{n + 1}", f"{args.slug} · {args.run} · adjudication r{args.round} · batch {n + 1}", "Adjudicator",
                  body(p, f"AJ-{args.round}-{n + 1}", "Adjudicator", run_meta["profile"],
                       f"Rule on each finding id below against the actual text in `{rdir}/package/`, weighing the owner's "
                       f"rebuttal in `{rdir}/rebuttals/` where one exists. Write `{rdir}/rulings-{n + 1}.json` as "
                       '`{"rulings": [{"id": "...", "ruling": "upheld|rejected|unclear", "reason": "...", "severity": "optional corrected severity"}]}`.'
                       + (f" For round {args.round} also rule whether each finding upheld in round {args.round - 1} is now resolved "
                          f"(`{rdir}/resolution-{n + 1}.json`)." if args.round > 1 and n == 0 else "")
                       + f"\n\nFindings: {', '.join(chunk) or '(dry run)'}", [],
                       [str(rdir / "findings.json"), str(rdir / "package"), str(rdir / "rebuttals")],
                       ["Every listed id has exactly one ruling with a reason that cites the text."], full),
                  rebuttal_ids)
        adj_ids.append(api.created[-1]["id"])
    api.issue(mi, f"CP-ROUTE-{args.round}", f"{args.slug} · {args.run} · Checkpoint · rulings r{args.round} done", "Orchestrator",
              body(p, f"CP-ROUTE-{args.round}", "Orchestrator", run_meta["profile"],
                   "Apply the rulings, route, and launch the loop-back or the package. See 'Checkpoint: rulings done' in your AGENTS.md.",
                   [], [str(rdir)], ["findings.adjudicated.json, the report and the route plan written; next stage launched."], full),
              adj_ids, "high")
    return {"stage": "adjudicate", "round": args.round, "findings": len(items), "ruled": len(to_rule), "tasks": len(api.created)}


def stage_loopback(args, api: Api) -> dict:
    p = Paths(args.slug, args.run, None, "P1")
    run_meta = json.loads((p.r / "run.json").read_text())
    full = run_meta["profile"] == "full"
    mi = api.matter_issue(run_meta["matter_issue"])
    rdir = p.r / "review" / f"r{args.round}"
    state = json.loads((p.r / "loop" / "loopback.json").read_text()) if (p.r / "loop" / "loopback.json").exists() else {"history": [{"steps": []}]}
    plan = state["history"][-1]
    cdir = p.r / "loop" / f"c{args.round}"
    prev = None
    ids = []
    for s in plan["steps"]:
        step, owner, fids = s["step"], s["owner"], s["finding_ids"]
        if step == "x-formal-fix":
            continue  # formal corrections run last, after the substantive revisions
        what = (f"Loop-back cycle {args.round}, step {step}. Fix ONLY these upheld findings (full text in "
                f"`{rdir}/findings.adjudicated.json`): {', '.join(fids)}. Prefer added disclosure to narrowing; any narrowing "
                f"goes in `narrowing_suggested` for the human. Save your reply as `{cdir}/{step}.md` and the new full text as "
                f"the next version (`description.vN.md` / `claims.vN.md`, never overwriting), and append the ids you "
                f"addressed with the paragraphs or claims changed to `{cdir}/CHANGED.md`.")
        api.issue(mi, f"LB-{args.round}-{step}", f"{args.slug} · {args.run} · loop-back c{args.round} · {step}", owner,
                  body(p, f"LB-{args.round}-{step}", owner, run_meta["profile"], what, [pr(step, f"loop/c{args.round}")], [],
                       [CHECKS, "support-map, claims-format, antecedent and numerals re-run on the new versions; results in your comment."], full),
                  [prev] if prev else [])
        prev = api.created[-1]["id"]
        ids.append(prev)
    formal = next((s for s in plan["steps"] if s["step"] == "x-formal-fix"), None)
    if formal:
        api.issue(mi, f"LB-{args.round}-formal", f"{args.slug} · {args.run} · loop-back c{args.round} · formal fix", "Specification Drafter",
                  body(p, f"LB-{args.round}-formal", "Specification Drafter", run_meta["profile"],
                       f"Apply the reviewers' mechanical corrections (`corrections[]` in the review envelopes in `{rdir}`) and "
                       f"formal findings {', '.join(formal['finding_ids'])} to the latest description and claims (claims corrections "
                       "go in the claims file too; you own formal fixes to both). New versions, never overwrite.",
                       [pr("x-formal-fix", f"loop/c{args.round}")], [], [CHECKS], full), [prev] if prev else [])
        prev = api.created[-1]["id"]
        ids.append(prev)
    api.issue(mi, f"CP-RR-{args.round + 1}", f"{args.slug} · {args.run} · Checkpoint · loop-back c{args.round} done", "Orchestrator",
              body(p, f"CP-RR-{args.round + 1}", "Orchestrator", run_meta["profile"],
                   f"Loop-back cycle {args.round} is complete. Build review package r{args.round + 1} from the newest versions, copy "
                   f"`{cdir}/CHANGED.md` into it, and launch review round {args.round + 1}. See 'Checkpoint: loop-back done'.",
                   [], [str(cdir)], ["Review round tasks exist."], full), [prev] if prev else [], "high")
    return {"stage": "loopback", "round": args.round, "steps": [s["step"] for s in plan["steps"]], "tasks": len(api.created)}


def stage_package(args, api: Api) -> dict:
    p = Paths(args.slug, args.run, None, "P1")
    run_meta = json.loads((p.r / "run.json").read_text())
    full = run_meta["profile"] == "full"
    mi = api.matter_issue(run_meta["matter_issue"])
    pkg = p.r / "package"
    ids = []
    api.issue(mi, "PK-39a", f"{args.slug} · {args.run} · package · abstract", "Specification Drafter",
              body(p, "PK-39a", "Specification Drafter", run_meta["profile"],
                   f"Draft the Abstract from the FINAL description and claims only. Reply `{pkg}/39a.md`; abstract text to `{pkg}/abstract.md`.",
                   [pr("39a", "package")], [str(pkg / "description.md"), str(pkg / "claims.md")], [CHECKS], full), [])
    ids.append(api.created[-1]["id"])
    for pid in ("39", "gate14", "40"):
        api.issue(mi, f"PK-{pid}", f"{args.slug} · {args.run} · package · {prompt(pid)['title'].lower()}", "Examiner",
                  body(p, f"PK-{pid}", "Examiner", run_meta["profile"],
                       f"Run Prompt {pid} on the final package in `{pkg}/` only. Reply `{pkg}/{pid}.md`, envelope via "
                       f"`{PC} contract --kind review --reply {pkg}/{pid}.md --write-envelope {pkg}/{pid}.envelope.json`.",
                       [pr(pid, "package")], [str(pkg)], ["Reply validated; envelope written."], full), [])
        ids.append(api.created[-1]["id"])
    api.issue(mi, "CP-FINAL", f"{args.slug} · {args.run} · Checkpoint · assemble the package", "Orchestrator",
              body(p, "CP-FINAL", "Orchestrator", run_meta["profile"],
                   "Write the cover memo, assemble and export the package, attach it, write the scorecard, and put Gate 3 to "
                   "the board. See 'Checkpoint: package' in your AGENTS.md.", [], [str(pkg)],
                   ["Word and PDF attached to the matter issue; Gate 3 requested."], full), ids, "high")
    return {"stage": "package", "tasks": len(api.created)}


def main() -> int:
    parser = argparse.ArgumentParser(prog="pc-plan", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="stage", required=True)
    i = sub.add_parser("init")
    i.add_argument("--slug", required=True); i.add_argument("--matter-issue", required=True)
    i.add_argument("--profile", choices=["full", "quick"], default="full"); i.add_argument("--run", default="r1")
    i.add_argument("--from", dest="restart_from", choices=PHASE_ORDER, default="P1"); i.add_argument("--base-run")
    i.add_argument("--dry-run", action="store_true")
    for name in ("review", "adjudicate", "loopback"):
        s = sub.add_parser(name)
        s.add_argument("--slug", required=True); s.add_argument("--run", default="r1")
        s.add_argument("--round", type=int, required=True); s.add_argument("--dry-run", action="store_true")
    k = sub.add_parser("package")
    k.add_argument("--slug", required=True); k.add_argument("--run", default="r1"); k.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if getattr(args, "restart_from", "P1") != "P1" and not getattr(args, "base_run", None):
        print(json.dumps({"ok": False, "error": "--from needs --base-run (the run whose earlier phases are reused)"}))
        return 2
    api = Api(args.dry_run)
    result = {"init": stage_init, "review": stage_review, "adjudicate": stage_adjudicate,
              "loopback": stage_loopback, "package": stage_package}[args.stage](args, api)
    print(json.dumps({"ok": True, "dry_run": args.dry_run, **result, "created": api.created}, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
