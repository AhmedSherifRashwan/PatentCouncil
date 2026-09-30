### Figure Instructions

**Numbering convention.** Numerals 10, 20, 30, 40, 42, 44, 50, 60, 70 are fixed by the inventor's own disclosure (`intake/disclosure.md` §3) and `terminology/LOCKED.md`; they are not changed. Decades 11–79 extend them by component family (1x valve stem, 2x core body, 3x seat ring, 4x poppet, 5x return spring, 6x purge gap/flow, 7x lock nut) for the preferred embodiment (FIG. 1 onward). Where a later figure shows an alternative species of a baseline component, the new numeral keeps the baseline's last two digits and changes the leading digit(s) to identify the alternative group: **1xx** = Alternative B (fixed seat/wiper) new components; **2xx** = first alternative species of a baseline component; **3xx** = second alternative species; **4xx** = third alternative species; **6xx/7xx** = alternative valve-architecture components, mirroring the core-body/seat-ring family. Repeated instances of one component within a figure (a second convolution, a second lug, a second finger) are labelled with a letter suffix on the same base numeral (e.g. 32a/32b) rather than given a new numeral. No numeral is reused for two different components.

**Deferred cross-checks.** `description.md`, `claims.md` and `registry.json` (an earlier registry) do not yet exist for this run (Prompt 16 has not produced a blueprint, and Prompts 18–19 have not run). The cross-check of this registry against description and claims text, required before Prompt 38, is therefore **deferred** and is flagged again below.

#### FIG. 1 — Axial section, closed state

- View: full axial section on the plane containing the poppet axis. Projection: orthographic, front elevation section.
- Elements: valve stem (10), with stem bore (12) shown threaded; core body (20) threaded into the stem bore, with core body bore (22) and internal shoulder (24); seat ring (30) seated against the internal shoulder (24), with convoluted wall (32) — label each convolution 32a, 32b if two are shown — and sealing edge (34); poppet (40) with poppet stem (41), sealing face (42) resting on the sealing edge (34), and purge shoulder (44) shown clear of the seat ring (30) by a lead-line dimension; return spring (50), shown as first spring stage (52) and second spring stage (54) (a single two-rate spring, or two springs, per the manufacturing note under FIG. 5); purge gap (60), shown as a closed (zero-width) annular line between the seat ring (30) outer surface and the core body bore (22); lock nut (70) at the outer end of the valve stem (10).
- Callout notes: mark the interference-fit region between the seat ring (30) and the internal shoulder (24) with hatching or a bracket distinct from the remainder of the seat ring's outer surface, which is drawn with a small clearance to the core body bore (22) even in the closed state, to support the FIG. 6 detail. Indicate "closed state" beneath the figure.
- Draftsperson/CAD notes: dimensions are not to be shown numerically on this general-arrangement view (they belong on FIG. 6); show proportionate wall thickness for the seat ring (30) relative to the 6 mm valve stem (10) outer diameter, consistent with the believed range of §4.

#### FIG. 2 — Axial section, normal-open state

- View/projection: as FIG. 1, same section plane.
- Elements: poppet (40) displaced from FIG. 1 by the normal stroke; sealing face (42) lifted clear of the sealing edge (34); first spring stage (52) shown compressed; main passage (64), shown with flow arrows from the supply side, past the sealing face (42), to the chamber side; purge shoulder (44) shown still clear of the seat ring (30), with a residual clearance dimension line to distinguish this state from FIG. 3.
- Callout notes: "normal-open state" beneath the figure; second spring stage (54) shown not yet engaged.
- Draftsperson/CAD notes: keep the seat ring (30) undeformed, identical in outline to FIG. 1.

#### FIG. 3 — Axial section, purge state

- View/projection: as FIG. 1, same section plane. Corresponds to the inventor's FIG-2.png.
- Elements: poppet (40) in over-travel; purge shoulder (44) in contact with the seat ring (30); seat ring (30) shown deflected radially outward, its at-rest outline (from FIG. 1) repeated in dashed line for comparison; purge gap (60) shown open, with a radial dimension line; purge flow path (62), shown with flow arrows distinct from the main-passage (64) arrows, running from the supply side through the purge gap (60) into the region on the chamber side; second spring stage (54) shown fully engaged/compressed.
- Callout notes: "purge state" beneath the figure; arrows for the purge flow path (62) should visibly cross the outer surface of the seat ring (30) and the adjoining region of the core body bore (22), i.e. the surfaces the bench data identifies as the fouling location.
- Draftsperson/CAD notes: the outward deflection of the seat ring (30) should be exaggerated for clarity (not to the true ~0.15 mm scale) with a note "deflection exaggerated for clarity."

#### FIG. 4 — Axial section, recovery state

- View/projection: as FIG. 1, same section plane.
- Elements: seat ring (30) shown mid-recovery, with a curved motion arrow indicating its surface moving across the sealing face (42) (the snap-back wipe); purge gap (60) shown partially closed (narrower than FIG. 3, wider than FIG. 1).
- Callout notes: "recovery state — snap-back wipe in progress" beneath the figure.
- Draftsperson/CAD notes: show the motion arrow originating at the seat ring's sealing edge (34) region and crossing the sealing face (42), consistent with the wipe described in §2.

#### FIG. 5 — Exploded perspective view

- View: isometric exploded perspective, parts separated along the poppet axis in assembly order.
- Elements, listed top to bottom in assembly order: lock nut (70); valve stem (10); core body (20); seat ring (30); poppet (40) (with sealing face (42) and purge shoulder (44) called out); return spring (50) (first spring stage (52) and second spring stage (54) called out on the same part, or as two parts if separately embodied).
- Callout notes: a bracket note beside the seat ring (30), poppet (40) and return spring (50) reading "may be supplied as a separate component or kit (see description)."
- Draftsperson/CAD notes: no new numerals; reuse FIG. 1's numerals throughout.

#### FIG. 6 — Enlarged cross-section detail, two sub-views

- **FIG. 6A** (at rest): enlarged partial section of the region bounded by the internal shoulder (24), core body bore (22), seat ring (30) and purge shoulder (44), at a larger scale than FIG. 1.
  - Elements: internal shoulder (24); core body bore (22); seat ring (30) with convoluted wall (32a, 32b) and sealing edge (34); purge shoulder (44), with an axial clearance dimension line to the seat ring (30); purge gap (60), shown closed, with a bracket distinguishing the interference-fit region (against the internal shoulder (24)) from the free region (where the purge gap (60) opens).
- **FIG. 6B** (over-travel): the same region, seat ring (30) deflected, purge gap (60) shown open with a radial dimension line labelled to match Table 1 of `13.md` ("purge gap opening").
- Callout notes: label the interference-fit region explicitly as "interference fit, seat ring (30) to internal shoulder (24)" and the free region as "purge gap (60), radial clearance"; this is the drawing convention recorded as Assumption A2 in Prompt 20, not an asserted inventor fact — mark with a footnote symbol on the sheet referencing the description's treatment of this point.
- Draftsperson/CAD notes: show both convolutions (32a, 32b) if the description confirms two; if only one is confirmed, show 32a alone and omit 32b.

#### FIG. 7 — Mechanical control-logic / operating-sequence diagram

- View: schematic state diagram, not a section. Five state boxes: "closed," "normal-open," "purge," "recovery," "locked," connected by labelled transition arrows.
- Elements: no reference numerals (schematic); each transition arrow is labelled with its governing condition in words, e.g. "pressure differential ≥ crack pressure," "pressure differential ≥ over-travel threshold," "pump head removed," "lock nut engaged," matching `01.md` (d) steps S1–S5 and (i).
- Callout notes: a note beneath the diagram: "control is entirely mechanical, actuated by the pressure differential across the poppet; no electronic or software control is present."
- Draftsperson/CAD notes: flowchart style, rectangular state boxes, arrows in sequence; no numerals to register.

#### FIG. 8 — Manufacturing/assembly sequence, five sub-views

- **FIG. 8A**: seat ring (30) shown as cut tube stock, laser-cut to profile.
- **FIG. 8B**: seat ring (30) shown in a shape-setting fixture holding the convoluted wall (32) geometry.
- **FIG. 8C**: seat ring (30) shown pressed into the core body (20) against the internal shoulder (24), interference fit.
- **FIG. 8D**: alternative to 8C — seat ring (30) retained by a crimped lip (224) rolled or swaged over its end by the core body (20).
- **FIG. 8E**: alternative to 8C — seat ring (30) retained by a separate retaining sleeve (324) clamping it against the internal shoulder (24).
- Callout notes: process arrows between 8A→8B→8C; 8D and 8E each labelled "alternative to FIG. 8C."
- Draftsperson/CAD notes: schematic process-flow style; no dimensions required on this sheet.

#### FIG. 9 — Axial section, PEEK seat ring embodiment

- View/projection: as FIG. 1 (rest) with a purge-state inset as FIG. 3, or a single view with a state note; same section plane.
- Elements: identical numerals to FIG. 1/FIG. 3 throughout; the seat ring (30) callout adds "(PEEK)".
- Callout notes: "Alternative embodiment: seat ring (30) formed from PEEK. Recovery is slower and the resulting snap-back wipe is weaker than the superelastic embodiment of FIG. 1–4; the purge gap and air purge provide cleaning independently of the wipe."
- Draftsperson/CAD notes: do not add an electropolish callout or an austenite-finish-temperature callout to this figure (footnotes [e], [g] of the combination matrix; not technically applicable to a polymer part).

#### FIG. 10 — Axial section, fixed seat + wiper ring embodiment, two sub-views

- **FIG. 10A** (closed state) and **FIG. 10B** (purge state), same section plane as FIG. 1/3.
- Elements: valve stem (10); core body (20) with core body bore (22); fixed seat (130), rigid, on which the sealing face (42) of the poppet (40) rests in the closed state; wiper ring (132), on the chamber side of the fixed seat (130), deflected outward by the purge shoulder (44) in 10B; purge gap (60), shown between the wiper ring (132) outer surface and the core body bore (22), closed in 10A and open in 10B; return spring (50).
- Callout notes: "Alternative embodiment: sealing performed by a fixed seat (130); purging and wiping performed by a separate wiper ring (132)."
- Draftsperson/CAD notes: the fixed seat (130) and wiper ring (132) are new components; do not reuse the seat ring (30) numeral for either.

#### FIG. 11 — Alternative deflecting-formation geometries, three sub-views

- **FIG. 11A**: partial section, poppet (40) with tapered purge shoulder (244), frustoconical, entering the seat ring (30) and deflecting it by direct radial contact.
- **FIG. 11B**: partial section, poppet (40) with discrete lugs (344a, 344b, ...), two to four shown, in place of a continuous annular purge shoulder.
- **FIG. 11C**: partial section, poppet (40) with a separate collar (444) fixed onto the poppet stem (41) (pressed, crimped or threaded), performing the purge-shoulder function.
- Callout notes: each sub-view labelled "alternative to purge shoulder (44), FIG. 1–4."
- Draftsperson/CAD notes: show 11B in a transverse (radial) partial view inset to make the discrete-lug arrangement clear.

#### FIG. 12 — Alternative axial-to-radial conversion geometries, three sub-views

- **FIG. 12A**: partial section, frustoconical wall (232) in place of the convoluted wall (32).
- **FIG. 12B**: partial section and end view, slotted wall (332) with axial slots forming fingers (332a, 332b, ...) that splay radially under the purge shoulder (44).
- **FIG. 12C**: partial section and end view, cellular wall (432), a laser-cut lattice pattern between two continuous end bands.
- Callout notes: each sub-view labelled "alternative to convoluted wall (32), FIG. 1, 6."
- Draftsperson/CAD notes: 12B and 12C each need an end-on view (looking along the poppet axis) in addition to the axial partial section, to show the slot/cell pattern.

#### FIG. 13 — Alternative purge-flow-path geometries, two sub-views

- **FIG. 13A**: partial section, purge ports (262a, 262b, ...) through the wall of the core body (20), on the chamber side of the purge gap (60), with flow arrows.
- **FIG. 13B**: partial section, flutes (362a, 362b, ...) in the core body bore (22), behind the seat ring (30), with flow arrows shown connecting to the supply side when the ring surface moves inward.
- Callout notes: each sub-view labelled "alternative to purge flow path (62), FIG. 3."
- Draftsperson/CAD notes: 13A needs a transverse partial view showing port placement around the circumference; 13B needs a similar view showing flute placement.

#### FIG. 14 — Alternative threshold-setting arrangements, two sub-views

- **FIG. 14A**: partial section, auxiliary spring (254) shown engaged only after a lost-motion clearance closes at the end of the normal stroke, acting in parallel with the first spring stage (52).
- **FIG. 14B**: partial section, detent (354) — a spring-loaded ball or a magnet — engaging a groove or target on the poppet stem (41), releasing at a breakaway force.
- Callout notes: each sub-view labelled "alternative to second spring stage (54), FIG. 1."
- Draftsperson/CAD notes: 14B may show either the ball-detent or the magnetic species with a bracket note "(ball detent shown; magnetic detent is an alternative using a ferritic target)."

#### FIG. 15 — Alternative valve architectures, two sub-views (schematic)

- **FIG. 15A**: schematic axial section, Schrader-pattern valve core: Schrader-pattern core body (620) and Schrader-pattern poppet (630), carrying the same seat ring (30)/purge shoulder (44)/purge gap (60) mechanism at larger bore.
- **FIG. 15B**: schematic axial section, non-removable inflation valve: valve stem (10) carrying a seat ring (730) directly, with no separate core body (20).
- Callout notes: each sub-view labelled "schematic only; not to Presta-pattern scale of FIG. 1–4."
- Draftsperson/CAD notes: reuse the seat ring (30)/purge shoulder (44)/purge gap (60) numerals inside 15A where the same structure is retained; use the new numeral 730 in 15B only for the stem-integrated seat ring, since it is carried by a different part (the valve stem (10), not a core body).

### Reference-Numeral Registry

| Numeral | Component | First figure | Also appears in |
|---|---|---|---|
| 10 | valve stem | FIG. 1 | FIG. 2; FIG. 3; FIG. 4; FIG. 5; FIG. 9; FIG. 10 |
| 12 | stem bore | FIG. 1 | FIG. 5 |
| 20 | core body | FIG. 1 | FIG. 2; FIG. 3; FIG. 4; FIG. 5; FIG. 6; FIG. 9; FIG. 13 |
| 22 | core body bore | FIG. 1 | FIG. 3; FIG. 4; FIG. 6; FIG. 9; FIG. 10; FIG. 13 |
| 24 | internal shoulder | FIG. 1 | FIG. 6; FIG. 8 |
| 30 | seat ring | FIG. 1 | FIG. 2; FIG. 3; FIG. 4; FIG. 5; FIG. 6; FIG. 8; FIG. 9 |
| 32 | convoluted wall | FIG. 1 | FIG. 3; FIG. 6 |
| 34 | sealing edge | FIG. 1 | FIG. 3; FIG. 4; FIG. 6; FIG. 9 |
| 40 | poppet | FIG. 1 | FIG. 2; FIG. 3; FIG. 4; FIG. 5; FIG. 9; FIG. 10; FIG. 11 |
| 41 | poppet stem | FIG. 1 | FIG. 5; FIG. 11; FIG. 14 |
| 42 | sealing face | FIG. 1 | FIG. 2; FIG. 3; FIG. 4; FIG. 5; FIG. 9; FIG. 10 |
| 44 | purge shoulder | FIG. 1 | FIG. 2; FIG. 3; FIG. 5; FIG. 6; FIG. 9; FIG. 10; FIG. 11 |
| 50 | return spring | FIG. 1 | FIG. 2; FIG. 3; FIG. 5; FIG. 9; FIG. 10 |
| 52 | first spring stage | FIG. 1 | FIG. 2; FIG. 5; FIG. 14 |
| 54 | second spring stage | FIG. 1 | FIG. 3; FIG. 5; FIG. 14 |
| 60 | purge gap | FIG. 1 | FIG. 3; FIG. 4; FIG. 6; FIG. 9; FIG. 10; FIG. 13 |
| 62 | purge flow path | FIG. 3 | FIG. 4; FIG. 10; FIG. 13 |
| 64 | main passage | FIG. 2 | FIG. 1; FIG. 3; FIG. 4; FIG. 9; FIG. 10 |
| 70 | lock nut | FIG. 1 | FIG. 5 |
| 130 | fixed seat | FIG. 10 | - |
| 132 | wiper ring | FIG. 10 | - |
| 224 | crimped lip | FIG. 8 | - |
| 232 | frustoconical wall | FIG. 12 | - |
| 244 | tapered purge shoulder | FIG. 11 | - |
| 254 | auxiliary spring | FIG. 14 | - |
| 262 | purge port | FIG. 13 | - |
| 324 | retaining sleeve | FIG. 8 | - |
| 332 | slotted wall | FIG. 12 | - |
| 344 | discrete lugs | FIG. 11 | - |
| 354 | detent | FIG. 14 | - |
| 362 | flute | FIG. 13 | - |
| 432 | cellular wall | FIG. 12 | - |
| 444 | separate collar | FIG. 11 | - |
| 620 | Schrader-pattern core body | FIG. 15 | - |
| 630 | Schrader-pattern poppet | FIG. 15 | - |
| 730 | seat ring (stem-integrated) | FIG. 15 | - |

**Inconsistency flags.**

1. **Cross-check against description and claims is deferred.** `description.md` and `claims.md` do not exist yet for this run; the check that every component named in those texts has a numeral, and that every numeral used in the description is registered here, cannot be performed now. This must be re-run at Prompt 38 once both exist.
2. **No earlier registry existed to preserve.** `registry.json` was not supplied as an input; this is a first-issue registry, so the "keep every existing numeral unchanged" rule has not yet been exercised, but must be honoured on every later revision of this run.
3. **FIG. 6's interference-fit/purge-gap convention (numeral 60, and the unlabelled interference-fit region near 24/30) rests on a drafting assumption (Prompt 20, Assumption A2), not a confirmed mechanism.** If the inventor's answer to 01 Q1/Q2 requires a different mechanism, numeral 60's callout and FIG. 6's geometry will need revision, and this is flagged rather than silently finalised.
4. **Numeral 730 (FIG. 15B) denotes the seat ring when carried directly by the valve stem (10) rather than by a core body (20).** It is deliberately not the same numeral as 30, because the component is carried by a different part in this architecture; this is a naming choice, not an inconsistency, and is recorded here so Prompt 38 does not flag it as a duplicate.
5. **No component named in `01.md` or `terminology/LOCKED.md` is left without a numeral among those actually drawn.** Locked terms not yet given a numeral (e.g. "supply side," "chamber side," "closed state," "purge state") are states/regions rather than drawn physical components and are shown as text labels only (FIG. 7), consistent with patent drafting practice; they are not treated as missing numerals.