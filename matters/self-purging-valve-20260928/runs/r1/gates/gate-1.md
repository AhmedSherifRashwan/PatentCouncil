# Gate 1 — terminology lock and reading of the disclosure

- Matter: `self-purging-valve-20260928` · run `r1` · profile quick
- Decision: **auto-unattended** (`intake/matter.json` mode `unattended`)
- Decided by: Orchestrator (mechanical step only; no human reviewed this gate)
- Time: 2026-09-28T11:52:14Z
- Command: `pc lock-terms --reply runs/r1/P1/04.md --out runs/r1/terminology/LOCKED.md`
- Result: `{"locked_terms": 49, "ok": true}`

## What this gate did and did not do

The preferred terms in `runs/r1/P1/04.md` are now the terminology lock for this run (`runs/r1/terminology/LOCKED.md`, 49 terms). Every later drafting output must use them verbatim or declare a `new_terms` entry with a reason.

No human confirmed the Phase 1 reading of the disclosure. Nothing generated in Phase 1 is confirmed by this gate; it stays `candidate`. `intake/answers.md` does not exist at the time of this gate, so the inventor's answers to the top-10 questions are not reflected in the lock.
