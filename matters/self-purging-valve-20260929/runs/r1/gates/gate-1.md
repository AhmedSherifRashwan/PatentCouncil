# Gate 1 — Lock terminology

**Matter:** self-purging-valve-20260929 · run r1 · mode: unattended (auto-unattended)

**Decision:** Terminology lock generated from `runs/r1/P1/04.md` and written to `runs/r1/terminology/LOCKED.md`.

**Command:** `pc lock-terms --reply runs/r1/P1/04.md --out runs/r1/terminology/LOCKED.md`
**Result:** `{"locked_terms": 56, "ok": true}`

**Disposition:** auto-unattended — matter.json mode is "unattended", so no human confirmation is required at this gate. 56 preferred terms locked (with synonyms, genus/species, functional description, avoid-list and needs-definition flags). This file becomes law for all downstream drafting (Phases 3–5); any new synonym introduced later must carry a logged `new_terms` reason.

**Time:** 2026-09-29 (gate recorded immediately following lock-terms run)
