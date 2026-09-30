# Gate 2 — confirm embodiments

- Matter: `self-purging-valve-20260928` · run `r1` · profile quick
- Decision: **auto-unattended** (`intake/matter.json` mode `unattended`)
- Decided by: Orchestrator (mechanical step only; no human reviewed this gate)
- Time: 2026-09-28T12:42:27Z
- Command: `pc confirm --replies runs/r1/P3/11.md runs/r1/P3/12.r1.md runs/r1/P3/13.r1.md runs/r1/P3/14.r1.md runs/r1/P3/15.md --out runs/r1/CONFIRMED.md --by auto-unattended`
- Result: `{"sources": 5, "ok": true}` — `runs/r1/CONFIRMED.md`, 537 lines

## Versions used

The task named `12.md`, `13.md` and `14.md`. Each has a newer correction (`12.r1.md`, `13.r1.md`, `14.r1.md`) that changes wording only to the locked terms ("inflation cycle 40", "angle of the conical face", "rigid valve seat", "seat ring"). The newest version of each was confirmed. `pc terms` against `terminology/LOCKED.md` reports no violations for any of the five sources; every drift entry is a declared `new_terms` item.

## What this gate did and did not do

The Phase 3 outputs (11 design-around register, 12 embodiments, 13 ranges, 14 embodiment matrix, 15 failure modes) are now the embodiment set Phase 4 drafts from.

No human, and in particular not the inventor, reviewed them. Many entries say in their own text "needs inventor confirmation" or "nothing yet" and point to open questions (for example DA-1 to DA-11 in 11, the thermal variant in 14, the pulse timing in 12 E11.5). Auto-confirmation does not answer those questions: it only makes the entries eligible for the specification. `intake/answers.md` does not exist at the time of this gate, so no inventor answer to the top-10 questions is reflected. Counsel should treat every entry marked "needs inventor confirmation" as unconfirmed by the inventor and check it for new matter before filing.
