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

AI drafting is a drafting and analysis aid, not a substitute for a qualified patent attorney or agent.
