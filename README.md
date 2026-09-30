# Patent Council

Workspace for the **Patent Council** company in Paperclip: an AI patent-drafting team that runs the
Patent Drafting Prompt Playbook (prompts in `~/IP-Filing-Ecosystem/prompts/`) end to end, with real
prior-art research, structured debates between agents, adjudicated review findings, and a Word/PDF
filing package for qualified patent counsel.

- `tools/pc` — deterministic checks and bookkeeping (`pc --help`): output contracts, terminology lock,
  support map, antecedent basis, claim format, numerals, review package, finding merge, rulings,
  owner-only loop-back routing, scorecard, Word/PDF export. Built on the IP Filing Ecosystem's own code.
- `tools/pc-plan` — creates a run's Paperclip tasks with their dependencies (`pc-plan --help`).
- `lessons.md` — recurring failures and the rules that prevent them. Read before every matter.
- `matters/<slug>/` — one dossier per matter: `intake/` (disclosure verbatim, supplied prior art,
  answers), `runs/<rN>/` (every phase output, versioned, never overwritten), `timeline.jsonl`.
  **Git-ignored and confidential: never committed, never uploaded.**

**Two deliverables per matter** (Word and PDF each): the **Patent Application** (Abstract, Detailed
Description, List of Figures, Claims) and the **Prosecution Assessment** (likelihood of grant out of 10, and a
table of every deficiency and prior-art reference the application will face). Everything else stays in the dossier.
- `agents/` — every agent's AGENTS.md, under version control; the source of truth for their instructions.

AI drafting is a drafting and analysis aid, not a substitute for a qualified patent attorney or agent.

## Running on OpenClaw (default since 2026-09-30)

Patent Council runs on OpenClaw. The Orchestrator is now code: `council` (in `council/`) plans the fast-flow
task graph, runs everything that can run in parallel, embeds each agent's inputs in its prompt, runs the `pc`
checks itself (one correction turn in the same session when one fails), pauses on a Claude usage limit and
resumes by itself, and delivers the two documents. Seven OpenClaw agents do the judgement work
(`pc-invention-analyst`, `pc-prior-art-analyst`, `pc-specification-drafter`, `pc-claims-architect`,
`pc-examiner`, `pc-litigator`, `pc-adjudicator`); `patent-council` is the chat front door (Chief of Staff).

```bash
tools/council new-matter --slug demo-20261001 --title "Self-purging valve" --from-example
tools/council run --slug demo-20261001 --background
tools/council status --slug demo-20261001
```

- `council run` resumes a stopped, failed or paused run; `council stop` stops launching new steps.
- `council run --simulate-from <old run folder>` replays an earlier run's outputs through every runner step
  and check with no model calls (the end-to-end test).
- Timing per step: `matters/<slug>/runs/<run>/council-timing.md`; ticker: `progress.md`.
- Agents: `python3 tools/build_openclaw.py --install` rebuilds the OpenClaw workspaces from `agents/*.md`
  (the single source) and the front door from `openclaw/front-door/`, then patches `~/.openclaw/openclaw.json`.

What changed against the Paperclip flow, for speed: no heartbeat scheduling between steps; gates, stitching,
the review package, merging, routing and delivery are code, not agent turns; inputs are embedded rather than
read file by file; the description fix returns paragraph edits (`@@ REPLACE/AFTER/DELETE [nnnn]`) instead of
re-typing the description; the 14-question gate runs alongside the review; the terminology lock is enforced
only on text that goes into the application (advisory on analysis outputs).
