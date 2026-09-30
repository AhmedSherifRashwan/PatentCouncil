"""Build and install the Patent Council agents into OpenClaw.

    python3 ~/PatentCouncil/tools/build_openclaw.py            build openclaw/workspaces/* from agents/*.md
    python3 ~/PatentCouncil/tools/build_openclaw.py --install  build, copy changed files into ~/.openclaw, patch config
    python3 ~/PatentCouncil/tools/build_openclaw.py --check    report what --install would change

`agents/*.md` stay the single source of every agent's instructions. The build turns each into an OpenClaw
workspace: AGENTS.md (the role, contracts, fast flow and company rules, with the Paperclip mechanics replaced by
how a turn works on OpenClaw), SOUL.md (who the agent is), USER.md and IDENTITY.md. The front door's workspace and
skill live in `openclaw/front-door/` and are copied as they are.
"""

from __future__ import annotations

import argparse
import datetime as dt
import filecmp
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path.home() / "PatentCouncil"
OC = Path.home() / ".openclaw"
OPENCLAW = OC / "bin" / "openclaw"
OUT = ROOT / "openclaw" / "workspaces"
FRONT = ROOT / "openclaw" / "front-door"

# OpenClaw id -> (source file, display name, model, one-line identity)
AGENTS = {
    "pc-invention-analyst": ("invention-analyst", "Invention Analyst", "anthropic/claude-opus-5-5",
                             "Captures the invention exactly (Phase 1) and builds its embodiments and design-arounds (Phase 3)."),
    "pc-prior-art-analyst": ("prior-art-analyst", "Prior-Art Analyst", "anthropic/claude-opus-5-5",
                             "Finds, indexes and charts the real prior art (Phase 2) and writes the pre-drafting findings report."),
    "pc-specification-drafter": ("specification-drafter", "Specification Drafter", "anthropic/claude-fable-5-1",
                                 "Drafts the specification (Phase 4): blueprint, description parts, drawings, registry, abstract, fixes."),
    "pc-claims-architect": ("claims-architect", "Claims Architect", "anthropic/claude-fable-5-1",
                            "Builds the claim family (Phase 5) and its support map, and fixes the claims after review."),
    "pc-examiner": ("examiner", "Examiner", "anthropic/claude-opus-5-5",
                    "Blind review as a hostile patent examiner; runs the 14-question filing gate."),
    "pc-litigator": ("litigator", "Litigator", "anthropic/claude-fable-5-1",
                     "The permanent adversary: attacks the differentiation and the embodiments, then reviews blind as competitor's counsel."),
    "pc-adjudicator": ("adjudicator", "Adjudicator", "anthropic/claude-opus-5-5",
                       "Rules on every review finding against the text and writes the Prosecution Assessment."),
}
FRONT_ID, FRONT_NAME, FRONT_MODEL = "patent-council", "Patent Council", "anthropic/claude-sonnet-5"
BOOT_FILE, BOOT_TOTAL = 60000, 90000

OPENCLAW_TURN = """## How a turn works on OpenClaw

- **The runner (`council`) is the Orchestrator.** It is code, not an agent: it plans the task graph, runs the
  gates, stitches the description, builds the blind review package, merges and routes findings, applies your
  edits and delivers the two documents. It calls you once per task, many tasks in parallel.
- **Each message is the whole brief.** It names your prompts (with their full text), embeds every input you
  need (do not re-read embedded files; open a listed file only when the message says it is not embedded),
  and lists the exact files to write.
- **Write each output with your Write tool at exactly the path given, one file per call,** inside the run
  folder only. Then reply with one line per file and anything that must be routed (open questions,
  `disclosure_requests`, `open_disagreements`, `narrowing_suggested`). Nothing else: no summary of the work.
- **The runner runs the checks** (`pc contract`, the terminology lock, claims format, the registry, the
  assessment check). If one fails you get one correction message in the same session: fix the file in place
  with your Edit tool (targeted replacements, not a re-type).
- **Never wait, poll or ask.** Every input that exists is in front of you. A missing optional input is named
  as missing: work without it and say what it would have changed.
- **Time matters.** A whole matter runs in about two hours. Every task has a budget in minutes: be complete,
  write each deliverable once, no drafts or padding.

"""

TOOLS_NOTE = """## Your tools

Your tools are Claude Code's: Read, Write, Edit, Bash, and web search and fetch. The company checks
(`~/PatentCouncil/tools/pc <command>`) are run for you by the runner; you do not need to run them. Before
drafting, the lessons in `~/PatentCouncil/lessons.md` apply (they are embedded in drafting tasks).

"""


def section_bounds(lines: list[str], start_pat: str, level: int) -> tuple[int, int] | None:
    """(start, end) of the first heading matching start_pat, up to the next heading of level <= `level`."""
    start = next((i for i, l in enumerate(lines) if re.match(start_pat, l)), None)
    if start is None:
        return None
    end = next((j for j in range(start + 1, len(lines))
                if re.match(r"^#{1,%d}\s" % level, lines[j]) and not _in_fence(lines, j)), len(lines))
    return start, end


def _in_fence(lines: list[str], idx: int) -> bool:
    return sum(1 for l in lines[:idx] if l.startswith("```")) % 2 == 1


def transform(src: str, name: str) -> tuple[str, str, str]:
    """-> (AGENTS.md, SOUL.md, USER.md)"""
    lines = src.splitlines()
    # Paperclip execution contract: everything from the H1 to the end.
    b = section_bounds(lines, r"^# Execution Contract", 1)
    if b:
        lines = lines[:b[0]]
    # USER.md out into its own file.
    user = ""
    b = section_bounds(lines, r"^# USER\.md", 1)
    if b:
        user = "\n".join(lines[b[0]:b[1]]).strip() + "\n"
        lines = lines[:b[0]] + lines[b[1]:]
    for pat in (r"^## How a task works in Paperclip", r"^## Your tools"):
        b = section_bounds(lines, pat, 2)
        if b:
            lines = lines[:b[0]] + lines[b[1]:]
    text = "\n".join(lines)
    # The Orchestrator is now the runner.
    text = text.replace("You report to the **Orchestrator**.",
                        "You report to the **runner** (`council`: the Orchestrator's job, done by code).")
    text = re.sub(r'mean the \*\*Orchestrator\*\*', "mean the **runner** (`council`)", text)
    text = text.replace("| Orchestrator | Plans and runs each matter: the task graph, gates, debates, loop-backs, the two deliverables |",
                        "| Runner (`council`, code) | Plans and runs each matter: the task graph, gates, checks, stitching, routing, the two deliverables |")
    text = re.sub(r"\bthe Orchestrator\b", "the runner", text)
    text = re.sub(r"\bOrchestrator\b", "runner", text)
    text = re.sub(r"\bthe orchestrator\b", "the runner", text)
    text = re.sub(r"\bin your comment\b", "in your final reply", text)
    text = re.sub(r"\byour comment\b", "your final reply", text)
    text = text.replace("Paste disclosure content anywhere outside Paperclip and the dossier",
                        "Paste disclosure content anywhere outside the dossier")
    # Insert the OpenClaw turn rules before the debates section (or at the end).
    marker = "## Debates (how we attack each other's work)"
    add = OPENCLAW_TURN + TOOLS_NOTE
    text = text.replace(marker, add + marker, 1) if marker in text else text.rstrip() + "\n\n" + add
    # SOUL: the first 'Who you are' (or 'Role') subsection, as the agent's character.
    lines = text.splitlines()
    soul_b = section_bounds(lines, r"^## Who you are", 2) or section_bounds(lines, r"^# Role\b", 1)
    soul = "\n".join(lines[soul_b[0]:soul_b[1]]).strip() if soul_b else ""
    soul = f"# SOUL — {name}\n\n{soul}\n\nEverything you do is governed by AGENTS.md.\n"
    return text.strip() + "\n", soul, user


def build() -> dict[str, dict[str, str]]:
    built = {}
    for aid, (src, name, _, ident) in AGENTS.items():
        agents_md, soul, user = transform((ROOT / "agents" / f"{src}.md").read_text(encoding="utf-8"), name)
        files = {"AGENTS.md": agents_md, "SOUL.md": soul, "USER.md": user,
                 "IDENTITY.md": f"# IDENTITY\n\n- **Name:** {name}\n- **Company:** Patent Council\n- **Role:** {ident}\n"}
        d = OUT / aid
        d.mkdir(parents=True, exist_ok=True)
        for fn, body in files.items():
            if len(body) > BOOT_FILE:
                sys.exit(f"{aid}/{fn} is {len(body)} chars, over the {BOOT_FILE} bootstrap cap")
            (d / fn).write_text(body, encoding="utf-8")
        total = sum(len(b) for b in files.values())
        if total > BOOT_TOTAL:
            sys.exit(f"{aid} workspace is {total} chars, over the {BOOT_TOTAL} total cap")
        leftovers = [w for w in ("Paperclip", "heartbeat", "matter issue", "ask_user_questions") if w in agents_md]
        built[aid] = {"chars": total, "leftover_platform_words": leftovers}
    return built


def patch() -> dict:
    entries = {}
    for aid, (_, name, model, _) in AGENTS.items():
        entries[aid] = {"name": aid, "workspace": str(OC / "workspaces" / aid), "agentDir": str(OC / "agents" / aid / "agent"),
                        "identity": {"name": name}, "model": model, "tools": {"profile": "minimal"},
                        "bootstrapMaxChars": BOOT_FILE, "bootstrapTotalMaxChars": BOOT_TOTAL}
    entries[FRONT_ID] = {"name": FRONT_NAME, "workspace": str(OC / "workspaces" / FRONT_ID),
                         "agentDir": str(OC / "agents" / FRONT_ID / "agent"), "identity": {"name": FRONT_NAME},
                         "model": FRONT_MODEL, "tools": {"profile": "coding"},
                         "bootstrapMaxChars": BOOT_FILE, "bootstrapTotalMaxChars": BOOT_TOTAL}
    return {"agents": {"defaults": {"models": {m: {"agentRuntime": {"id": "claude-cli"}} for m in
                                               {"anthropic/claude-opus-5-5", "anthropic/claude-fable-5-1", "anthropic/claude-sonnet-5"}}},
                       "entries": entries}}


def install(check: bool) -> list[str]:
    changes = []
    for aid in list(AGENTS) + [FRONT_ID]:
        src_dir = OUT / aid if aid != FRONT_ID else FRONT / "workspace"
        dst_dir = OC / "workspaces" / aid
        for src in sorted(p for p in src_dir.rglob("*") if p.is_file()):
            dst = dst_dir / src.relative_to(src_dir)
            if dst.exists() and filecmp.cmp(src, dst, shallow=False):
                continue
            changes.append(f"copy {src.relative_to(ROOT)} -> {dst}")
            if not check:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dst)
        if not check:
            (OC / "agents" / aid / "agent").mkdir(parents=True, exist_ok=True)
    pfile = ROOT / "openclaw" / "openclaw.patch.json"
    pfile.write_text(json.dumps(patch(), indent=1) + "\n")
    current = json.loads((OC / "openclaw.json").read_text())
    missing = [a for a in list(AGENTS) + [FRONT_ID] if a not in current.get("agents", {}).get("entries", {})]
    changes.append(f"config patch ({len(missing)} new agent entries: {', '.join(missing) or 'none'}; others refreshed)")
    if not check:
        backup = OC / f"openclaw.json.bak.pc.{dt.datetime.now():%Y%m%d-%H%M%S}"
        shutil.copyfile(OC / "openclaw.json", backup)
        res = subprocess.run([str(OPENCLAW), "config", "patch", "--file", str(pfile)], capture_output=True, text=True)
        changes.append((res.stdout + res.stderr).strip()[-400:])
        if res.returncode != 0:
            sys.exit("config patch failed; config left as it was. Backup: " + str(backup))
    return changes


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--install", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    built = build()
    print(json.dumps({"built": built}, indent=1))
    if a.install or a.check:
        for line in install(check=a.check):
            print(("would: " if a.check else "") + line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
