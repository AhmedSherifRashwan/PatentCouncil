"""The fast flow: the Patent Council task graph, built for a two-hour end-to-end run.

Everything that can run in parallel does. Prior art starts at minute zero; Phase 3 starts at Gate 1; the
description is drafted in parallel parts and stitched by `pc`; claims start from Gate 2; the Litigator's attacks
feed the drafting directly; the 14-question gate runs alongside the review; the fix pass returns paragraph edits
instead of re-typing the description; the Prosecution Assessment is written while the fixes are made.

The runner steps here are what the Orchestrator did in Paperclip: gates, stitching, the blind review package,
merging and routing findings, and delivering the two documents.
"""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from council import edits
from council.engine import Ctx, PromptRef, Task
from council.paths import newest

IA, PA, SD, CA = "pc-invention-analyst", "pc-prior-art-analyst", "pc-specification-drafter", "pc-claims-architect"
EX, LI, AJ = "pc-examiner", "pc-litigator", "pc-adjudicator"
SONNET = "claude-sonnet-5"
REVIEW_GROUPS = {"G1": ["28", "29", "31"], "G2": ["30", "32"], "G3": ["33", "34", "35", "36"], "G4": ["37", "38", "40a"]}
REVIEW_GROUP_NAMES = {"G1": "support, amendment basis and priority", "G2": "jurisdictions and examiner red-team",
                      "G3": "enforcement, freedom to operate, moat and gaps", "G4": "claims, specification and formal audits"}
BATCH = 35
PUB_RE = re.compile(r"\b((?:US|EP|GB|WO|CN|JP|DE|KR|FR|CA|AU|TW|RU|ES|IT|NL|SE|CH|AT|DK|FI|IN|BR)\s?[-/]?\s?"
                    r"(?:\d[\d,\s/]{4,14}\d)\s?(?:[A-Z]\d?)?)\b")
LOOP = "loop/c1"


def P(pid: str, folder: str, relax: tuple[str, ...] = ()) -> PromptRef:
    return PromptRef(pid, f"{folder}/{pid}.md", relax)


# -- runner steps ---------------------------------------------------------------------------------------------------


def step_gate1(ctx: Ctx) -> dict:
    R = ctx.R
    res = ctx.pc("lock-terms", "--reply", str(R / "P1/04.md"), "--out", str(R / "terminology/LOCKED.md"), allow_fail=False)
    (R / "gates").mkdir(exist_ok=True)
    (R / "gates/gate-1.md").write_text(f"# Gate 1 — terminology lock\n\nDecision: accepted (auto-unattended), "
                                       f"{ctx.engine.state.get('started', '')}.\n\n```json\n{json.dumps(res, indent=1)[:2000]}\n```\n")
    ctx.say(f"GATE 1 terminology locked ({res.get('locked_terms', '?')} terms, auto-unattended)")
    return {"lock": {k: v for k, v in res.items() if k != "table"}}


def step_questions(ctx: Ctx) -> dict:
    src = ctx.R / "P1/top10-questions.md"
    dst = ctx.run.intake / "questions-for-inventor.md"
    shutil.copyfile(src, dst)
    ctx.say(f"QUESTIONS for the inventor are ready: {dst}. The run does not wait for them; answers go in "
            f"{ctx.run.intake / 'answers.md'} for a second pass.", urgent=True)
    return {"questions": str(dst)}


def _norm(raw: str) -> str | None:
    m = PUB_RE.search(raw)
    if not m:
        return None
    n = re.sub(r"[\s,/-]", "", m.group(1)).upper()
    return n if len(re.sub(r"\D", "", n)) >= 5 else None


def _numbers(index_text: str) -> list[str]:
    """Publication numbers from the index table's number column. Rows for requester-supplied or fictional
    references are skipped: they are read from intake, never looked up."""
    seen, out, col = set(), [], None
    for line in index_text.splitlines():
        if not line.startswith("|"):
            col = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if col is None:
            col = next((i for i, c in enumerate(cells) if re.search(r"number|publication", c, re.I)), -1)
            continue
        if re.match(r"^:?-", cells[0]) or col < 0 or col >= len(cells):
            continue
        if re.search(r"fictional|intake/", line, re.I):
            continue
        n = _norm(cells[col].strip("`*"))
        if n and n not in seen:
            seen.add(n)
            out.append(n)
    if not out:  # no table with a number column: fall back to every number in the text
        for line in index_text.splitlines():
            if not re.search(r"fictional|intake/", line, re.I):
                for m in PUB_RE.finditer(line):
                    n = _norm(m.group(1))
                    if n and n not in seen:
                        seen.add(n)
                        out.append(n)
    return out


def step_fetch_refs(ctx: Ctx) -> dict:
    """Only publication numbers leave the machine. Full texts are saved beside the analyst's index."""
    from ecosystem import search  # IP-Filing-Ecosystem's Google Patents client

    refs = ctx.R / "prior-art/refs"
    refs.mkdir(parents=True, exist_ok=True)
    index = (ctx.R / "prior-art/INDEX.md").read_text(encoding="utf-8")
    fetched, kept, failed = [], [], []
    for n in _numbers(index):
        path = refs / f"{n}.md"
        if path.exists() and path.stat().st_size > 3000:
            kept.append(n)
            continue
        try:
            rec = search.fetch_patent(n)
        except Exception as exc:  # noqa: BLE001 - one missing page never stops the run
            failed.append(f"{n}: {str(exc)[:120]}")
            continue
        claims = "\n".join(f"{i}. {c}" for i, c in enumerate(rec.claims, 1))
        path.write_text(
            f"<!-- MACHINE-RETRIEVED from {rec.url} at {rec.retrieved_at}; sha256 {rec.sha256} -->\n"
            f"# {rec.number} — {rec.title}\n\n- URL: {rec.url}\n- Accessed: {rec.retrieved_at}\n"
            f"- Dates: {json.dumps(rec.dates)}\n- CPC: {', '.join(rec.cpc[:12])}\n\n## Abstract\n\n{rec.abstract}\n\n"
            f"## Claims\n\n{claims}\n\n## Description (extract)\n\n{rec.description_excerpt}\n", encoding="utf-8")
        fetched.append(n)
    total = len(list(refs.glob("*.md")))
    ctx.say(f"PRIOR ART indexed: {total} references saved ({len(fetched)} full texts fetched by number"
            f"{', ' + str(len(failed)) + ' not retrievable' if failed else ''})")
    return {"fetched": fetched, "already_saved": kept, "failed": failed, "refs": total}


def step_gate2(ctx: Ctx) -> dict:
    R = ctx.R
    replies = [str(R / f"P3/{x}.md") for x in ("11", "12", "13", "14", "15")]
    res = ctx.pc("confirm", "--replies", *replies, "--out", str(R / "CONFIRMED.md"), allow_fail=False)
    (R / "gates/gate-2.md").write_text("# Gate 2 — confirm embodiments\n\nDecision: candidates confirmed "
                                       "(auto-unattended). Nothing auto-confirmed is treated as human-confirmed.\n")
    ctx.say(f"GATE 2 candidate embodiments from {res.get('sources', '?')} Phase 3 outputs confirmed (auto-unattended)")
    return {"confirm": {k: v for k, v in res.items() if isinstance(v, (int, str))}}


def step_stitch(ctx: Ctx) -> dict:
    R = ctx.R
    n = int(ctx.settings.get("parts", 5))
    parts = [str(R / f"P4/parts/part{k}.md") for k in range(1, n + 1)]
    res = ctx.pc("assemble-description", "--parts", *parts, "--out", str(R / "description.md"), allow_fail=False)
    num = ctx.pc("numerals", "--registry", str(R / "registry.json"), "--description", str(R / "description.md"),
                 "--claims", "/dev/null")
    (R / "P4/stitch-checks.json").write_text(json.dumps({"assemble": res, "numerals": num}, indent=1))
    ctx.say(f"DESCRIPTION stitched: {res.get('paragraphs')} paragraphs from {n} parts"
            f"{'' if num.get('ok') else ' (numeral warnings logged)'}")
    return {"paragraphs": res.get("paragraphs"), "numerals_ok": num.get("ok")}


def step_review_package(ctx: Ctx) -> dict:
    R, run = ctx.R, ctx.run
    rdir = R / "review/r1"
    ctx.mark("drafting", "end")
    ctx.mark("review", "start")
    res = ctx.pc("review-package", "--description", str(run.description()), "--claims", str(run.claims()),
                 "--figures", str(R / "P4/20.md"), "--registry-reply", str(R / "P4/20a.md"), "--out", str(rdir / "package"),
                 allow_fail=False)
    checks = {
        "support_map": ctx.pc("support-map", "--description", str(run.description()), "--claims", str(run.claims()),
                              "--map", str(R / "support-map.json")),
        "claims_format": ctx.pc("claims-format", "--claims", str(run.claims())),
        "antecedent": ctx.pc("antecedent", "--claims", str(run.claims())),
    }
    (rdir / "pre-review-checks.json").write_text(json.dumps(checks, indent=1))
    claims = len(re.findall(r"^\s*\d+\.\s", run.claims().read_text(encoding="utf-8"), re.M))
    ctx.say(f"DRAFTING done: {claims} claims · blind review starting ({'two reviewers' if ctx.full else 'one reviewer'})",
            urgent=True)
    return {"package": res.get("written"), "claims": claims,
            "checks": {k: v.get("ok") for k, v in checks.items()}}


def expand_review(ctx: Ctx) -> list[Task]:
    rdir = "review/r1"
    pkg = [f"{rdir}/package/{f}" for f in ("description.md", "claims.md", "figures.md", "registry.md")]
    reviewers = [(EX, "", "Examiner")] + ([(LI, "b", "Litigator")] if ctx.full else [])
    tasks, keys = [], []
    for agent, suffix, name in reviewers:
        for g, pids in REVIEW_GROUPS.items():
            key = f"R1-{name[:3]}-{g}"
            keys.append(key)
            tasks.append(Task(
                key, f"review · {name} · {g} {REVIEW_GROUP_NAMES[g]}", agent, deps=["PKG-REVIEW"], review=True,
                prompts=[PromptRef(p, f"{rdir}/{p}{suffix}.md") for p in pids], embed=pkg + ["prior-art/INDEX.md"],
                refer=["prior-art/refs"], model=SONNET if g == "G4" else None, budget=10, stage="",
                what=(f"Blind review, group {g} ({REVIEW_GROUP_NAMES[g]}), as the **{name}**. You see only the finished "
                      "text (the review package, embedded below) and the saved prior art: no drafting rationale, no earlier "
                      "phases, no risk report, no other reviewer. Run each prompt below against the package and write each "
                      "reply in the review output contract, with every finding anchored to a claim, paragraph or reference "
                      "passage. Findings are how this company improves the application: raise every real one, all severities.")))
    tasks.append(Task("PK-gate14", "14-question filing gate", EX, deps=["PKG-REVIEW"], review=True,
                      prompts=[PromptRef("gate14", f"{rdir}/gate14.md")], embed=pkg + ["prior-art/INDEX.md"],
                      refer=["prior-art/refs"], budget=9,
                      what="Run the 14-question filing gate on the review package and the saved prior art. It feeds the "
                           "grant-likelihood score in the Prosecution Assessment."))
    # The gate's findings are merged with the reviews', so the Adjudicator rules on them too.
    tasks.append(Task("MERGE", "merge the two reviews", deps=keys + ["PK-gate14"], run=step_merge, expand=expand_adjudicate))
    return tasks


def step_merge(ctx: Ctx) -> dict:
    rdir = ctx.R / "review/r1"
    res = ctx.pc("merge-findings", "--review-dir", str(rdir), allow_fail=False)
    ctx.pc("findings-report", "--findings", str(rdir / "findings.json"), "--title",
           f"{ctx.run.slug} — review round 1 (before rulings)", "--out", str(rdir / "findings-report.pre.md"))
    ctx.mark("review", "end")
    ctx.mark("adjudication", "start")
    ctx.say(f"REVIEW done: {res.get('findings')} findings ({res.get('consensus')} raised by both reviewers) · rulings starting",
            urgent=True)
    return {"findings": res.get("findings"), "consensus": res.get("consensus")}


def _findings(path: Path) -> list[dict]:
    raw = json.loads(path.read_text()) if path.exists() else {"findings": []}
    return raw.get("findings", raw) if isinstance(raw, dict) else raw


def expand_adjudicate(ctx: Ctx) -> list[Task]:
    rdir = ctx.R / "review/r1"
    items = _findings(rdir / "findings.json")
    to_rule = items if ctx.full else [f for f in items if f.get("severity") in ("critical", "high")]
    bdir = rdir / "batches"
    bdir.mkdir(exist_ok=True)
    pkg = [f"review/r1/package/{f}" for f in ("description.md", "claims.md", "figures.md")]
    tasks, keys = [], []
    for n in range(max(1, (len(to_rule) + BATCH - 1) // BATCH)):
        chunk = to_rule[n * BATCH:(n + 1) * BATCH]
        bfile = bdir / f"batch-{n + 1}.json"
        if not bfile.exists():
            bfile.write_text(json.dumps({"findings": chunk}, indent=1))
        key = f"AJ-{n + 1}"
        keys.append(key)
        ids = [f["id"] for f in chunk]
        tasks.append(Task(
            key, f"rulings · batch {n + 1} ({len(ids)} findings)", AJ, deps=["MERGE"], budget=8,
            embed=[bfile] + pkg + ["prior-art/INDEX.md"], refer=["prior-art/refs"],
            outputs=[f"review/r1/rulings-{n + 1}.json"],
            checks=lambda c, f=f"review/r1/rulings-{n + 1}.json", ids=tuple(ids): _check_rulings(c, f, ids),
            what=("Rule on every finding in the embedded batch file against the actual text of the review package. There "
                  "is no rebuttal round: before ruling, make the drafter's best defence yourself (find the paragraph or "
                  "claim that would answer the finding) and rule on the stronger case. Correct a severity only with a "
                  f"reason. Write `rulings-{n + 1}.json` as "
                  '`{"rulings": [{"id": "F-..", "ruling": "upheld|rejected|unclear", "reason": "<cites the text>", '
                  '"severity": "<only if corrected>"}]}` with exactly one ruling per id: ' + ", ".join(ids))))
    tasks.append(Task("ROUTE", "apply rulings and route the fix pass", deps=keys, run=step_route, expand=expand_fix))
    return tasks


def _check_rulings(ctx: Ctx, rel: str, ids: tuple[str, ...]) -> list[tuple[str, str]]:
    path = ctx.R / rel
    try:
        data = json.loads(path.read_text())
        ruled = {r["id"] for r in (data.get("rulings", data) if isinstance(data, dict) else data)}
    except Exception as exc:  # noqa: BLE001
        return [(str(path), f"not valid rulings JSON: {exc}")]
    missing = [i for i in ids if i not in ruled]
    return [(str(path), f"no ruling for: {', '.join(missing)}")] if missing else []


def step_route(ctx: Ctx) -> dict:
    R = ctx.R
    rdir = R / "review/r1"
    rulings = []
    for f in sorted(rdir.glob("rulings-*.json")):
        try:
            data = json.loads(f.read_text())
            rulings += data.get("rulings", data) if isinstance(data, dict) else data
        except Exception:  # noqa: BLE001 - reported below as unruled
            pass
    ruled = {r["id"] for r in rulings}
    # A severe finding nobody ruled on stays open in the assessment; it is never waved through.
    for f in _findings(rdir / "findings.json"):
        if f["id"] not in ruled and f.get("severity") in ("critical", "high"):
            rulings.append({"id": f["id"], "ruling": "unclear", "reason": "not ruled in adjudication; left open"})
    (rdir / "rulings.json").write_text(json.dumps({"rulings": rulings}, indent=1))
    applied = ctx.pc("apply-rulings", "--findings", str(rdir / "findings.json"), "--rulings", str(rdir / "rulings.json"),
                     "--out", str(rdir / "findings.adjudicated.json"))
    ctx.pc("findings-report", "--findings", str(rdir / "findings.adjudicated.json"), "--title",
           f"{ctx.run.slug} — review round 1", "--out", str(rdir / "findings-report.md"))
    route = ctx.pc("route", "--findings", str(rdir / "findings.adjudicated.json"), "--state", str(R / "loop/loopback.json"),
                   "--cap", "1", "--commit")
    (rdir / "route.json").write_text(json.dumps(route, indent=1))
    steps = route.get("steps", [])
    spec = sorted({i for s in steps if s["step"] in ("x-loopback-p3", "x-p4-revise") for i in s["finding_ids"]})
    claims = sorted({i for s in steps if s["step"] == "x-p5-revise" for i in s["finding_ids"]})
    formal = sorted({i for s in steps if s["step"] == "x-formal-fix" for i in s["finding_ids"]})
    items = {f["id"]: f for f in _findings(rdir / "findings.adjudicated.json")}
    loop = R / LOOP
    loop.mkdir(parents=True, exist_ok=True)
    (loop / "findings-desc.json").write_text(json.dumps({"findings": [items[i] for i in spec + formal if i in items]}, indent=1))
    (loop / "findings-claims.json").write_text(json.dumps({"findings": [items[i] for i in claims + formal if i in items]}, indent=1))
    corr_d, corr_c = [], []
    for env in sorted(rdir.glob("*.envelope.json")):
        try:
            for c in json.loads(env.read_text()).get("corrections") or []:
                where = json.dumps(c).lower()
                (corr_c if "claim" in where and "paragraph" not in where else corr_d).append({**c, "source": env.stem})
        except Exception:  # noqa: BLE001
            continue
    (loop / "corrections-desc.json").write_text(json.dumps(corr_d, indent=1))
    (loop / "corrections-claims.json").write_text(json.dumps(corr_c, indent=1))
    plan = {"description": spec, "claims": claims, "formal": formal,
            "corrections": {"description": len(corr_d), "claims": len(corr_c)}}
    (loop / "plan.json").write_text(json.dumps(plan, indent=1))
    tally = applied.get("rulings", {})
    ctx.mark("adjudication", "end")
    ctx.mark("fix-and-assess", "start")
    ctx.say(f"RULINGS: {tally.get('upheld', 0)} upheld · {tally.get('rejected', 0)} rejected · {tally.get('unclear', 0)} "
            f"unclear · fix pass on {len(spec)} description and {len(claims)} claims findings (+{len(formal)} formal) · "
            "assessment in parallel", urgent=True)
    return {"rulings": tally, "plan": plan}


def expand_fix(ctx: Ctx) -> list[Task]:
    R = ctx.R
    plan = json.loads((R / LOOP / "plan.json").read_text())
    common = ("Fix ONLY the upheld findings in the embedded findings file, plus the reviewers' mechanical corrections "
              "(embedded). Prefer added disclosure to narrowing; a narrowing you consider necessary goes in "
              "`narrowing_suggested` for the human, never applied. ")
    tasks = [Task(
        "LB-desc", "fix pass · description (paragraph edits)", SD, deps=["ROUTE"], budget=15,
        prompts=[PromptRef("x-p4-revise", f"{LOOP}/x-p4-revise.md")],
        embed=[f"{LOOP}/findings-desc.json", f"{LOOP}/corrections-desc.json", "P5/unsupported.md", "P4/enablement-gaps.md",
               "debate"],
        outputs=[f"{LOOP}/CHANGED-desc.md"], checks=_check_edits, post=step_apply_edits,
        what=(common + "Novelty and design-around findings are answered by adding disclosure drawn from CONFIRMED.md and the "
              "attacks' closed escape routes, never by inventing embodiments. Also answer every item in "
              "`P5/unsupported.md` and `P4/enablement-gaps.md` (embedded if they exist).\n\n"
              "**Do not re-type the description.** Under `### Description` in your Deliverable, give ONLY edit blocks against "
              "the numbered paragraphs of the description embedded below, each starting on its own line:\n\n"
              "```\n@@ REPLACE [0042]\n<the full new text of paragraph 0042; more paragraphs may follow>\n"
              "@@ AFTER [0042]\n<one or more new paragraphs (or #### headings) to insert after 0042>\n@@ DELETE [0042]\n```\n\n"
              "No paragraph numbers inside the new text (the runner numbers inserted paragraphs 0042a, 0042b ...). Use "
              "reference numerals exactly as in the registry and locked terms verbatim. Under `### Change Log` list each "
              "edit with the finding ids it answers. Then write `CHANGED-desc.md`: one line per finding id addressed, with "
              f"the paragraphs changed.\n\nFindings routed to you: {', '.join(plan['description'] + plan['formal']) or '(none: corrections and the gap lists only)'}."))]
    tasks.append(Task(
        "LB-abstract", "abstract and list of figures", SD, deps=["LB-desc"], budget=5,
        prompts=[PromptRef("39a", f"{LOOP}/39a.md")], embed=["P4/20.md"], outputs=[f"{LOOP}/abstract.md", f"{LOOP}/list-of-figures.md"],
        what=("From the FINAL description and claims (embedded): the Abstract (Prompt 39a) as the reply, the abstract text "
              "alone in `abstract.md` (no heading), and `list-of-figures.md`: one line per figure, `Fig. N — what it shows`, "
              "matching the figures and reference numerals the description uses.")))
    if plan["claims"] or plan["formal"] or plan["corrections"]["claims"]:
        tasks.append(Task(
            "LB-claims", "fix pass · claims", CA, deps=["ROUTE"], budget=15,
            prompts=[PromptRef("x-p5-revise", f"{LOOP}/x-p5-revise.md")],
            embed=[f"{LOOP}/findings-claims.json", f"{LOOP}/corrections-claims.json"],
            outputs=["claims.v2.md", f"{LOOP}/claims-needs.md", f"{LOOP}/CHANGED-claims.md"],
            checks=lambda c: _check_claims(c, c.R / "claims.v2.md"),
            what=(common + "You work in parallel with the description fix: amend only to what the description embedded below "
                  "already supports, and list anything that needs new disclosure in `claims-needs.md` (one line each: claim, "
                  "limitation, disclosure needed); it becomes a deficiency in the assessment. Keep the claim family broad "
                  "and deep: fix, do not prune. Write the complete amended claim set, plain numbered claims only, to "
                  "`claims.v2.md`, and `CHANGED-claims.md`: one line per finding id addressed, with the claims changed.\n\n"
                  f"Findings routed to you: {', '.join(plan['claims'] + plan['formal']) or '(none: corrections only)'}.")))
    rdir = "review/r1"
    tasks.append(Task(
        "PK-GRANT", "Prosecution Assessment (grant likelihood)", AJ, deps=["ROUTE", "PK-gate14"], budget=13,
        embed=[f"{rdir}/findings-report.md", f"{rdir}/gate14.md", "prior-art/INDEX.md", "loop/loopback.json", f"{LOOP}/plan.json",
               f"{rdir}/package/claims.md"],
        refer=[f"{rdir}/findings.adjudicated.json", f"{rdir}/package", "prior-art/refs"],
        outputs=["package/prosecution-assessment.md"], checks=_check_assessment,
        what=("Write the **Prosecution Assessment** exactly as 'The prosecution assessment' in your AGENTS.md defines, in "
              "parallel with the fix pass, from the review package, your rulings (`findings.adjudicated.json`, and the "
              "report embedded below), the 14-question gate and the saved prior art. The table lists EVERY finding ruled "
              "upheld or unclear (all severities) and EVERY reference in the index. Add a **Status** column: `open, routed "
              "to fix pass` for the upheld findings routed in `plan.json`, `open` for every other upheld or unclear "
              "finding, `prior art` for references. Score the application as reviewed; say in the score line that fixes "
              "made after review are not re-scored. Cite paragraphs as `[0042]`.")))
    tasks.append(Task("FINAL", "deliver the two documents",
                      deps=["LB-abstract", "PK-GRANT"] + (["LB-claims"] if any(t.key == "LB-claims" for t in tasks) else []),
                      run=step_final, stage=""))
    return tasks


def _check_edits(ctx: Ctx) -> list[tuple[str, str]]:
    from ecosystem.contracts import split_sections

    path = ctx.R / LOOP / "x-p4-revise.md"
    text = path.read_text(encoding="utf-8")
    ops = edits.parse_edits(text)
    plan = json.loads((ctx.R / LOOP / "plan.json").read_text())
    if not ops and (plan["description"] or plan["formal"]):
        return [(str(path), "no `@@ REPLACE|AFTER|DELETE [nnnn]` edit blocks found under ### Description")]
    base = (ctx.R / "review/r1/package/description.md").read_text(encoding="utf-8")
    _, report = edits.apply_edits(base, ops)
    if report["missing_anchor"]:
        return [(str(path), "edit anchors that are not paragraphs of the description: " + ", ".join(report["missing_anchor"]))]
    return []


def step_apply_edits(ctx: Ctx) -> dict:
    R = ctx.R
    ops = edits.parse_edits((R / LOOP / "x-p4-revise.md").read_text(encoding="utf-8"))
    base = (R / "review/r1/package/description.md").read_text(encoding="utf-8")
    new, report = edits.apply_edits(base, ops)
    (R / "description.v2.md").write_text(new, encoding="utf-8")
    (R / LOOP / "edits-applied.json").write_text(json.dumps(report, indent=1))
    ctx.say(f"DESCRIPTION fixed: {report['applied']} paragraph edits applied"
            f"{', ' + str(len(report['missing_anchor'])) + ' skipped' if report['missing_anchor'] else ''}")
    return report


def _check_registry(ctx: Ctx) -> list[tuple[str, str]]:
    res = ctx.pc("registry", "--reply", str(ctx.R / "P4/20a.md"), "--out", str(ctx.R / "registry.json"))
    return [] if res.get("ok") else [(str(ctx.R / "P4/20a.md"), f"numeral registry could not be built: {json.dumps(res)[:600]}")]


def _check_claims(ctx: Ctx, path: Path) -> list[tuple[str, str]]:
    res = ctx.pc("claims-format", "--claims", str(path))
    return [] if res.get("ok") else [(str(path), f"claims format: {json.dumps(res)[:600]}")]


def _check_assessment(ctx: Ctx) -> list[tuple[str, str]]:
    R = ctx.R
    res = ctx.pc("assessment-check", "--assessment", str(R / "package/prosecution-assessment.md"), "--findings",
                 str(R / "review/r1/findings.adjudicated.json"), "--index", str(R / "prior-art/INDEX.md"))
    return [] if res.get("ok") else [(str(R / "package/prosecution-assessment.md"), f"assessment-check: {json.dumps(res)[:900]}")]


def _append_claims_needs(assessment: str, needs: list[str]) -> tuple[str, int]:
    """Add a row per claims-needs item to the deficiency table (the one with a Status column)."""
    lines = assessment.split("\n")
    header_at = next((i for i, l in enumerate(lines) if l.startswith("|") and "status" in l.lower()), None)
    if header_at is None or not needs:
        return assessment, 0
    cols = [c.strip().lower() for c in lines[header_at].strip().strip("|").split("|")]
    end = header_at + 1
    while end < len(lines) and lines[end].startswith("|"):
        end += 1
    rows = []
    for k, item in enumerate(needs, 1):
        cells = []
        for c in cols:
            if c in ("#", "no", "no."):
                cells.append(f"CN-{k}")
            elif "deficiency" in c or "reference" in c:
                cells.append(item.replace("|", "/"))
            elif c == "type":
                cells.append("support (claims need disclosure)")
            elif "claim" in c:
                cells.append(", ".join(re.findall(r"\b[Cc]laims?\s+(\d+)", item)) or "see item")
            elif "severity" in c:
                cells.append("medium")
            elif "source" in c:
                cells.append("claims fix pass")
            elif "respond" in c:
                cells.append("add supporting disclosure before filing, or amend the claim")
            elif "status" in c:
                cells.append("open")
            else:
                cells.append("")
        rows.append("| " + " | ".join(cells) + " |")
    lines[end:end] = rows
    return "\n".join(lines), len(rows)


def _table_counts(text: str) -> tuple[dict[str, int], int]:
    """Deficiencies by severity and prior-art rows, read from the table's Severity and Type/Status columns."""
    sev = {k: 0 for k in ("critical", "high", "medium", "low")}
    refs, cols = 0, None
    for line in text.splitlines():
        if not line.startswith("|"):
            cols = None
            continue
        cells = [c.strip().lower() for c in line.strip().strip("|").split("|")]
        if cols is None:
            cols = cells if "severity" in cells else None
            continue
        if re.match(r"^:?-", cells[0]):
            continue
        row = dict(zip(cols, cells))
        if "prior art" in row.get("type", "") or row.get("status", "") == "prior art":
            refs += 1
        elif row.get("severity") in sev:
            sev[row["severity"]] += 1
    return sev, refs


def step_final(ctx: Ctx) -> dict:
    R, run = ctx.R, ctx.run
    pkg, loop = R / "package", R / LOOP
    pkg.mkdir(exist_ok=True)
    matter = json.loads((run.intake / "matter.json").read_text()) if (run.intake / "matter.json").exists() else {}
    title = matter.get("title") or run.slug
    desc_final, mapping = edits.renumber(newest(R, "description").read_text(encoding="utf-8"))
    (pkg / "description.md").write_text(desc_final, encoding="utf-8")
    (pkg / "paragraph-map.json").write_text(json.dumps(mapping, indent=1))
    shutil.copyfile(newest(R, "claims"), pkg / "claims.md")
    shutil.copyfile(loop / "abstract.md", pkg / "abstract.md")
    shutil.copyfile(loop / "list-of-figures.md", pkg / "list-of-figures.md")
    changed = "\n".join(p.read_text(encoding="utf-8") for p in (loop / "CHANGED-desc.md", loop / "CHANGED-claims.md") if p.exists())
    (loop / "CHANGED.md").write_text(changed, encoding="utf-8")
    assess = pkg / "prosecution-assessment.md"
    status = ctx.pc("assessment-status", "--assessment", str(assess), "--changed", str(loop / "CHANGED.md"), "--out", str(assess))
    text = assess.read_text(encoding="utf-8")
    needs_file = loop / "claims-needs.md"
    needs = [re.sub(r"^\s*[-*\d.]+\s*", "", l).strip() for l in needs_file.read_text(encoding="utf-8").splitlines()
             if l.strip() and not l.startswith("#")] if needs_file.exists() else []
    needs = [n for n in needs if n and n[:60] not in text]
    text, added = _append_claims_needs(text, needs)
    text = edits.remap_refs(text, mapping)
    assess.write_text(text, encoding="utf-8")
    app = pkg / f"{run.slug}-patent-application.md"
    assembled = ctx.pc("assemble", "--title", title, "--abstract", str(pkg / "abstract.md"), "--description",
                       str(pkg / "description.md"), "--figures-list", str(pkg / "list-of-figures.md"), "--claims",
                       str(pkg / "claims.md"), "--out", str(app), allow_fail=False)
    check = ctx.pc("assessment-check", "--assessment", str(assess), "--findings", str(R / "review/r1/findings.adjudicated.json"),
                   "--index", str(R / "prior-art/INDEX.md"))
    readable = pkg / "readable"
    ex1 = ctx.pc("export", "--source", str(app), "--out", str(readable), "--title", f"{title} — Patent Application")
    ex2 = ctx.pc("export", "--source", str(assess), "--out", str(readable), "--title", f"{title} — Prosecution Assessment")
    ctx.mark("fix-and-assess", "end")
    ctx.mark("run", "end")
    ctx.pc("scorecard", "--matter", str(run.m), "--run", run.run)
    score = re.search(r"(\d+(?:\.\d+)?)\s*/\s*10", text)
    sev, refs = _table_counts(text)
    files = ex1.get("written", []) + ex2.get("written", [])
    summary = {"score": score.group(0) if score else None, "claims": assembled.get("claims"), "severity_rows": sev,
               "prior_art_rows": refs, "fix_pass_rows_marked": status.get("rows_marked"), "claims_needs_rows": added,
               "assessment_check_ok": check.get("ok"), "files": files}
    (pkg / "delivery.json").write_text(json.dumps(summary, indent=1))
    timing = write_timing(ctx)
    ctx.say(f"DELIVERED: grant likelihood {summary['score'] or '?'} · {summary['claims']} claims · deficiencies "
            f"critical {sev['critical']} / high {sev['high']} / medium {sev['medium']} / low {sev['low']} · {refs} prior-art "
            f"references · {timing} · files: {', '.join(files)} · details {pkg / 'delivery.json'}", urgent=True)
    return summary


def write_timing(ctx: Ctx) -> str:
    import datetime as dt

    st = ctx.engine.state
    rows = []
    for key, s in st["tasks"].items():
        if s.get("started") and s.get("finished"):
            rows.append((s["started"], s["finished"], key, s.get("minutes")))
    if not rows:
        return "no timing"
    start = min(dt.datetime.fromisoformat(r[0]) for r in rows)
    end = max(dt.datetime.fromisoformat(r[1]) for r in rows)
    wall = (end - start).total_seconds() / 60
    md = [f"# Timing — {ctx.run.slug} / {ctx.run.run}", "", f"Wall clock: **{wall:.0f} min** "
          f"({start:%H:%M} → {end:%H:%M}, including any usage-limit pause)", "", "| Step | Start | End | Minutes |", "|---|---|---|---|"]
    for a, b, key, mins in sorted(rows):
        md.append(f"| {key} | {a[11:16]} | {b[11:16]} | {mins} |")
    (ctx.R / "council-timing.md").write_text("\n".join(md) + "\n")
    return f"{wall:.0f} min end to end"


# -- the graph ------------------------------------------------------------------------------------------------------


def build(ctx: Ctx) -> list[Task]:
    full, n_parts = ctx.full, int(ctx.settings.get("parts", 5))
    R = ctx.R
    for sub in ("P1", "P2", "P3", "P4/parts", "P5", "prior-art/refs", "terminology", "debate", "risk", "review/r1",
                LOOP, "package", "gates", "calls"):
        (R / sub).mkdir(parents=True, exist_ok=True)
    disclosure = ctx.run.intake / "disclosure.md"
    T: list[Task] = []

    # -- invention capture ∥ prior-art search (both from minute zero)
    T.append(Task("P1a", "P1 · 01 invention extraction", IA, prompts=[P("01", "P1")], budget=6, stage="",
                  what="Run Prompt 01. Every later step reads it, so it goes first and alone."))
    for pid, relax, model in (("02", (), SONNET), ("03", ("out:P1/02",), None), ("04", ("out:P1/03",), None)):
        T.append(Task(f"P1-{pid}", f"P1 · {pid}", IA, deps=["P1a"], prompts=[P(pid, "P1", relax)], model=model, budget=6,
                      what=f"Run Prompt {pid}. It runs in parallel with its siblings: use their outputs if they are embedded."))
    T.append(Task("G1", "Gate 1 · lock terminology", deps=["P1-04"], run=step_gate1))
    T.append(Task("P1b", "P1 · 05 inventor questions", IA, deps=["P1-03", "P1-04"], prompts=[P("05", "P1")], model=SONNET,
                  outputs=["P1/top10-questions.md"], budget=8,
                  what="Run Prompt 05, then write `P1/top10-questions.md`: the ten questions whose answers would change the "
                       "claims most, each multiple-choice (2–4 options plus 'other') where possible, and what each answer would change."))
    T.append(Task("QF", "questions to the inventor", deps=["P1b"], run=step_questions, optional=True))
    T.append(Task(
        "RES", "prior art · search strategy (06), search and index", PA,
        prompts=[P("06", "P2", ("out:P1/01", "out:P1/03", "out:P1/04", "terminology", "intake:gate-1-answers"))],
        embed=[disclosure], outputs=["prior-art/INDEX.md", "prior-art/search-log.md"], budget=18,
        what=("Starts at minute zero, alongside Phase 1. (1) Run Prompt 06 from the disclosure itself (Phase 1 outputs are "
              "optional: use any that are embedded). (2) Search with your web tools: patent databases (Google Patents, "
              "Espacenet, Lens) and the technical literature, using its strings and classes. **Generic technical queries "
              "only: never disclosure text, never the invention's own phrasing.** Read the strongest candidates' claims. "
              f"(3) Choose the {'10–20' if full else '5–8'} closest references and write `prior-art/INDEX.md`: one row per "
              "reference with the publication number written in full (e.g. `US 10,123,456 B2`, `EP 3456789 A1`), title, "
              "assignee, priority and publication dates, URL, the concepts it hits and closeness 1–5. The runner fetches "
              "every numbered patent's full text into `prior-art/refs/<number>.md` from the number alone. For a non-patent "
              "reference, save its relevant text yourself as `prior-art/refs/NPL-<n>.md` with URL and access date. "
              "(4) `prior-art/search-log.md`: every query run, where, and what was kept or dropped.")))
    T.append(Task("FETCH", "prior art · fetch full texts by number", deps=["RES"], run=step_fetch_refs))
    T.append(Task("P2b", "P2 · 07–10 charts, novelty attack, differentiation, white space", PA, deps=["FETCH", "G1"],
                  prompts=[P("07", "P2"), P("08", "P2"), P("09", "P2"), P("10", "P2")], refer=["prior-art/refs"], budget=16,
                  what="Run Prompts 07, 08, 09 and 10 in order against the references in INDEX.md (full texts under "
                       "`prior-art/refs/`: read the ones you chart). Write each reply as soon as it is done."))

    # -- embodiments ∥ attack on the differentiation
    relax = ("out:P2/09", "out:P2/10", "out:P2/08", "intake:gate-1-answers")
    for pid in ("11", "12", "13", "14", "15"):
        T.append(Task(f"P3-{pid}", f"P3 · {pid}", IA, deps=["G1"], budget=10,
                      prompts=[P(pid, "P3", relax + (("out:P3/12", "out:P3/13") if pid == "14" else ()))],
                      model=SONNET if pid in ("13", "14", "15") else None,
                      what=f"Run Prompt {pid}. Everything is a candidate until Gate 2. It runs in parallel with the other "
                           "Phase 3 prompts and with the prior-art charts: use the differentiation (09) and white space (10) "
                           "if they are embedded."))
    T.append(Task("G2", "Gate 2 · confirm embodiments", deps=[f"P3-{x}" for x in ("11", "12", "13", "14", "15")], run=step_gate2))
    if full:
        T.append(Task("D1a", "attack · the differentiation", LI, deps=["P2b"], embed=["P2/09.md", "prior-art/INDEX.md"],
                      refer=["prior-art/refs"], outputs=["debate/d1-attack.md"], budget=10,
                      what="Attack Prompt 09's differentiation with the closest disclosures: the saved references, or new "
                           "generic web searches (never the invention's wording). Write `debate/d1-attack.md`: per distinction, "
                           "the reference, the exact passage, and how strong the attack is; or 'survives: searched …'. The "
                           "drafters and the risk report answer it; there is no defence round. Any new reference you rely on "
                           "gets a row appended to INDEX.md with its full publication number."))
        T.append(Task("D2a", "attack · competitor escape routes", LI, deps=["G2"], embed=["CONFIRMED.md", "P2/09.md"],
                      outputs=["debate/d2-attack.md"], budget=8,
                      what="As a well-funded competitor, find the cheapest credible escape from each confirmed embodiment. "
                           "Write `debate/d2-attack.md`: each escape route names the embodiment it avoids and why it works "
                           "commercially. The drafters must close these routes in the description and the claims."))
    T.append(Task("RISK", "pre-drafting findings report", PA, deps=["G2", "P2b"], outputs=["risk/pre-drafting-findings.md"],
                  embed=["P1/01.md", "P1/03.md", "P2/08.md", "P2/09.md", "P2/10.md", "CONFIRMED.md", "debate"], budget=8,
                  what="Write `risk/pre-drafting-findings.md` from Phases 1–3, the attacks (whatever is embedded) and the "
                       "lessons file. Every critical and high risk names its owner (P4, P5 or both) and the drafting response."))

    # -- description in parallel parts ∥ claims from the blueprint
    T.append(Task("P4a", "P4 · 16 specification blueprint", SD, deps=["G2"], prompts=[P("16", "P4")],
                  embed=["risk/pre-drafting-findings.md"], budget=10,
                  what=f"Run Prompt 16. Its section plan must split the detailed description into **{n_parts} parts** of "
                       f"similar size that can be drafted independently: list them as `Part 1` … `Part {n_parts}`, each with "
                       "its sections, figures and claim families. The risk report may still be in progress: use it if embedded."))
    for pid in ("18", "19"):
        T.append(Task(f"P4-{pid}", f"P4 · {pid}", SD, deps=["G2"], prompts=[P(pid, "P4", ("out:P4/16", "out:P4/17", "out:P4/18"))],
                      model=SONNET, budget=8,
                      what=f"Run Prompt {pid} from the confirmed embodiments and the locked terms, alongside the blueprint "
                           "(use it if embedded)."))
    T.append(Task("P4-20", "P4 · 20 and 20a drawings and numeral registry", SD, deps=["G2"], model=SONNET, budget=10,
                  prompts=[P("20", "P4", ("out:P4/18", "out:P4/16")), P("20a", "P4", ("out:P4/18", "out:P4/16", "out:P4/20"))],
                  checks=_check_registry,
                  what="Run Prompts 20 and 20a from the confirmed embodiments, alongside the blueprint (use it if embedded). "
                       "20a must register every reference numeral the drawings use."))
    parts = []
    for k in range(1, n_parts + 1):
        parts.append(f"P4-part{k}")
        T.append(Task(
            f"P4-part{k}", f"P4 · description part {k} of {n_parts}", SD,
            deps=["P4a", "P4-18", "P4-19", "P4-20", "RISK"] + (["D2a"] if full else []),
            prompts=[PromptRef("x-p4-compose-description", f"P4/parts/part{k}.md", ("out:P4/17",))],
            embed=["risk/pre-drafting-findings.md", "debate"], budget=12,
            what=(f"Draft **Part {k} of {n_parts}** of the detailed description: exactly the sections Prompt 16's blueprint "
                  f"assigns to Part {k}. Rules: one `### Description` wrapper; section titles as `####` headings (never `##` "
                  "or `###` inside); no paragraph numbers (the stitcher numbers them); reference numerals exactly as in the "
                  "registry; locked terms verbatim. Answer the risks and attacks that fall in your sections. Do not repeat "
                  "material that belongs to another part. Depth matters: every claim family must find its support here.")))
    T.append(Task("P4-stitch", "stitch the description", deps=parts, run=step_stitch))
    T.append(Task("P4-17", "P4 · 17 enablement audit of the finished description", SD, deps=["P4-stitch"],
                  prompts=[P("17", "P4", ("out:P4/16",))], outputs=["P4/enablement-gaps.md"], budget=9, optional=True,
                  what="Run Prompt 17 against the stitched description. Also write every enablement or sufficiency gap to "
                       "`P4/enablement-gaps.md`, one line each with the paragraph and the disclosure needed: the fix pass answers them."))
    claims_relax = ("out:P4/description", "registry", "out:P4/19", "out:P4/16", "out:P5/23", "out:P5/25", "out:P5/21")
    T.append(Task("P5a", "P5 · 21–22 claim strategy and independent claims", CA, deps=["G2", "P2b"], budget=14,
                  prompts=[P("21", "P5", claims_relax), P("22", "P5", claims_relax)],
                  embed=["P4/16.md", "CONFIRMED.md", "risk/pre-drafting-findings.md", "debate"],
                  what="Run Prompts 21 and 22 from the confirmed embodiments, the differentiation and white space, and (if "
                       "embedded) the blueprint, the risk report and the attacks. The description is being drafted in "
                       "parallel: claim what CONFIRMED.md supports; every limitation is mapped to the finished description in P5d."))
    for pid in ("23", "24", "27"):
        T.append(Task(f"P5-{pid}", f"P5 · {pid}", CA, deps=["P5a"], prompts=[P(pid, "P5", claims_relax)], budget=10,
                      what=f"Run Prompt {pid}, in parallel with its siblings. Build generously: the fallback depth of the "
                           "claim family comes from here."))
    T.append(Task("P5d", "P5 · 25 final claim set and support map", CA, deps=["P5-23", "P5-24", "P5-27", "P4-stitch"],
                  prompts=[P("25", "P5")], outputs=["claims.md", "support-map.json", "P5/unsupported.md"], budget=12,
                  checks=lambda c: _check_claims(c, c.R / "claims.md"),
                  what="Run Prompt 25 against the stitched description (embedded). Write the Final Claim Set, plain numbered "
                       "claims only, to `claims.md`, and `support-map.json` as "
                       '`{"claims": {"1": [{"element": "<exact claim words>", "paragraphs": ["[0012]"]}]}}` for every '
                       "element of every claim. A limitation you cannot map to a paragraph is re-worded to what the text "
                       "supports, or listed in `P5/unsupported.md` (one line each) for the fix pass. Keep the family broad "
                       "and deep: independent claims in every justified category, full dependent ladders."))
    T.append(Task("PKG-REVIEW", "blind review package", deps=["P5d"], run=step_review_package, expand=expand_review))
    return T
