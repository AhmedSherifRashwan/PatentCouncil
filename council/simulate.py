"""Replay a finished run through the runner without calling a model.

`council run --simulate-from <old run folder>` stands in a fake agent that copies each task's outputs from the
old run (same relative paths) and synthesises the few the old run never produced. Every runner step and every
deterministic check runs for real, so the whole graph, the gates, stitching, merging, routing, the edits and
the delivery are exercised end to end at zero model cost.
"""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

from council.engine import Ctx, Task


def _drafting_reply(prompt_id: str, deliverable: str) -> str:
    env = {"prompt": prompt_id, "status": "complete", "assumptions": [], "open_questions": [], "new_terms": [],
           "support_refs": [], "disclosure_requests": [], "open_disagreements": [], "narrowing_suggested": []}
    return (f"## Deliverable\n\n{deliverable.strip()}\n\n## Rationale\n\nSimulated.\n\n## Assumptions\n\nNone.\n\n"
            f"## Open Questions\n\nNone.\n\n```json\n{json.dumps(env, indent=2)}\n```\n")


def make_fake(source: Path):
    source = Path(source).expanduser()

    def fake(ctx: Ctx, task: Task) -> dict:
        R = ctx.R
        wanted = [pr.reply for pr in task.prompts] + task.outputs
        for rel in wanted:
            dst = R / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            src = source / rel
            if src.exists():
                shutil.copyfile(src, dst)
                continue
            dst.write_text(_synth(ctx, task, rel, source), encoding="utf-8")
        return {"simulated": True}

    return fake


def _synth(ctx: Ctx, task: Task, rel: str, source: Path) -> str:
    R = ctx.R
    plan = json.loads((R / "loop/c1/plan.json").read_text()) if (R / "loop/c1/plan.json").exists() else {}
    if rel.endswith("x-p4-revise.md"):
        desc = (R / "review/r1/package/description.md").read_text(encoding="utf-8")
        ids = re.findall(r"^\[(\d{4})\]", desc, re.M)
        body = (f"### Description\n\n@@ REPLACE [{ids[2]}]\nA simulated replacement paragraph.\n\n"
                f"@@ AFTER [{ids[5]}]\nA simulated inserted paragraph answering an enablement gap.\n\nA second one.\n\n"
                f"### Change Log\n\n- {', '.join(plan.get('description', [])[:3]) or 'none'}: simulated edits")
        return _drafting_reply("x-p4-revise", body)
    if rel.endswith("x-p5-revise.md"):
        return _drafting_reply("x-p5-revise", "### Final Claim Set\n\n" + (R / "claims.md").read_text() +
                               "\n\n### Change Log\n\n- simulated")
    if rel == "claims.v2.md":
        return (R / "claims.md").read_text()
    if rel.endswith("CHANGED-desc.md"):
        return "\n".join(f"- {i}: simulated edit" for i in plan.get("description", [])[:5]) + "\n"
    if rel.endswith("CHANGED-claims.md"):
        return "\n".join(f"- {i}: simulated amendment" for i in plan.get("claims", [])[:5]) + "\n"
    if rel.endswith("claims-needs.md"):
        return "- Claim 3: the purge interval limitation needs a disclosed range.\n"
    if rel.endswith("39a.md"):
        return _drafting_reply("39a", "### Abstract\n\nA simulated abstract.")
    if rel.endswith("abstract.md"):
        return "A self-purging valve (simulated abstract for the replay test).\n"
    if rel.endswith("list-of-figures.md"):
        return "Fig. 1 — simulated figure.\n"
    if rel.endswith("enablement-gaps.md"):
        return "- [0010]: simulated gap.\n"
    if rel.startswith("P4/parts/part"):
        # the old run had fewer parts: give the extra ones one small section
        k = re.search(r"part(\d+)", rel).group(1)
        return _drafting_reply("x-p4-compose-description", f"### Description\n\n#### Simulated part {k}\n\nSimulated paragraph.")
    return f"Simulated output for {rel} ({task.key}).\n"
