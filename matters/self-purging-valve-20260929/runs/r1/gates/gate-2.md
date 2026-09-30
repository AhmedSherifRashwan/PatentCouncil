# Gate 2 — Confirm embodiments

**Matter:** self-purging-valve-20260929 · run r1 · mode: unattended (auto-unattended) · profile: full · flow: fast

**Decision:** Phase 3 outputs (design-around register, equivalent architectures, parameter/range ladder,
combination/permutation map, failure-mode embodiments) aggregated into `runs/r1/CONFIRMED.md`.

**Command:**
`pc confirm --replies runs/r1/P3/11.r1.md runs/r1/P3/12.r1.md runs/r1/P3/13.md runs/r1/P3/14.md runs/r1/P3/15.md --out runs/r1/CONFIRMED.md`
**Result:** `{"sources": 5, "written": "runs/r1/CONFIRMED.md", "ok": true}`

**Disposition:** auto-unattended — `matter.json` sets `"mode": "unattended"`, and the matter issue states
explicitly that Gates 1 and 2 auto-accept and are logged; only Gate 3 waits. No human confirmation was
sought at this gate.

## Which files were used, and why

The task text named the base files (`11.md`…`15.md`). I used the corrected `.r1` version for 11 and 12
instead, because:
- `pc terms` fails on `P3/11.md` (2 undeclared-synonym violations: bare "film", table header "ID") and
  passes on `P3/11.r1.md` (0 violations). The Invention Analyst's own comment on that task names
  `11.r1.md` as "the file to use."
- `pc terms` fails on `P3/12.md` (1 violation: bare "tube" read as a synonym of "tyre chamber") and passes
  on `P3/12.r1.md`. Same "use this one" note from the Analyst.
- `P3/13.md` and `P3/14.md` pass `pc terms` as first drafts; no `.r1` exists or is needed.
- `P3/15.md` has no `.r1` despite failing `pc terms` (3 residual flags: "core", "differential", "purge").
  The Invention Analyst's task comment documents this as a pre-existing tool limitation — each flagged
  word is a bare-word collision with a *different* locked compound term ("valve core", "pressure
  differential", "air purge") while the text itself correctly uses the mandatory locked terms "core body
  bore", "over-travel differential" and "purge gap". They verified the same collision class reproduces
  against `P1/01.md`, the source document the terminology table was built from, and reported it per the
  standing instruction to report both when a check and judgement disagree, rather than loop further
  correction turns against an unfixable false positive. I accept that reasoning: rewording to dodge these
  three would itself violate the terminology lock. Using `P3/15.md` as-is.

Using the base (failed) `11.md`/`12.md` would have carried logged terminology violations into the
confirmed-embodiments record; the corrected, passing versions are the ones this gate confirms.

## What this gate does and does not resolve

`CONFIRMED.md`'s own header states that candidate status is lifted by this gate. That is true only in the
procedural sense: these five documents are now the fixed input to Phase 4/5 drafting, and nothing outside
them is specification content. It is **not** true that the individual rows have been technically vetted —
most rows still carry their own `candidate` / `needs inventor confirmation` tag, and that tag is preserved
verbatim in the file. In particular:

- `intake/answers.md` does not exist. No inventor answer has been received on any open question.
- 11.r1 alone raises 16 Gate-2 questions (Q1–Q16) against the design-around register, including three
  (DA-2, DA-10, DA-14) that the Analyst flags as escaping the inventive nucleus N0 entirely unless the
  inventor confirms air purge alone gives the effect.
- 12.r1 raises 9 further Gate-2 questions (Q1–Q9) against the equivalent-architectures map, including a
  credibility finding (Q5) that a 0.15 mm radial purge gap on a 1.35 mm outer radius implies about 11%
  hoop strain — above the recoverable strain usually cited for superelastic NiTi — unless the figure is
  diametral or the opening comes from wall bending.
- 15 raises further open questions on storage-only sealant build-up and whether the failure-mode scope
  extends to Alt-A/Alt-B.
- Both 11.r1 and 12.r1 note they were written before `P2/09` and `P2/10` (differentiation, white space)
  existed, so none of the design-arounds or alternatives were ranked against the actual prior art. Both
  09 and 10 now exist in this run; that re-ranking has not happened and is not part of this gate.

None of this blocks the mechanical step this task asks for — profile is full, flow is fast, and the matter
is explicitly configured to auto-accept Gates 1–2 (this is also a stated FICTIONAL timing-run matter per
PAT-49). But because so much of what is now "confirmed" for drafting purposes is internally marked as
unconfirmed by its own authors, I am carrying the open items forward rather than treating this gate as
having resolved them. Downstream drafting (Specification Drafter, Claims Architect) must still write
"candidate" language exactly as the Phase 3 documents do for every row tagged `needs inventor
confirmation`; Human Gate 3 is where a qualified patent attorney or agent has final visibility on all of
this before anything is filed.

**Time:** 2026-09-29 (gate recorded immediately following `pc confirm`)
