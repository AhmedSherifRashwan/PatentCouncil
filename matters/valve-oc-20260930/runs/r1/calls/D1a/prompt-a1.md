# Patent Council · matter `valve-oc-20260930` · run `r1` · step `D1a` · profile full

You are the **Litigator**. Follow your AGENTS.md. This message is the whole brief: what to do, the prompts to execute, every input (embedded below, so do not re-read those files), and the exact files to write.

## What to do

Attack Prompt 09's differentiation with the closest disclosures: the saved references, or new generic web searches (never the invention's wording). Write `debate/d1-attack.md`: per distinction, the reference, the exact passage, and how strong the attack is; or 'survives: searched …'. The drafters and the risk report answer it; there is no defence round. Any new reference you rely on gets a row appended to INDEX.md with its full publication number.

**Time budget:** about 10 minutes. The whole matter is planned to finish end to end in two hours. Be complete, but write each deliverable once: no drafts, no repetition, no padding.

## Inputs (embedded)

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P2/09.md`

````markdown
## Deliverable

### Differentiation Matrix

This is a drafting and analysis aid prepared by AI. It is not legal advice and does not say the invention is patentable; qualified patent counsel signs off before anything is filed. The distinctions below are tested only against the 17 references charted in `07`. That pile is thin (07 Q1), and ref-01 and ref-02 are fictional (07 Q2). The rows are ordered by how much of the `08` attack each one answers. The possible claim language gives phrases in locked terms, not claims.

| Prior-art feature | Our differentiating feature | Technical effect | Evidence / support | Possible claim language | Design-around risk |
|---|---|---|---|---|---|
| **1. The poppet deflects the seat on every opening, or a resilient member is deformed as the only way to open.**<br>ref-02 claim 4: "lip seal deflectable by the poppet during opening"; [0019] (07 ref-02 row N0c ?).<br>US4462449A claim 1: the closure member is "not contacting said elastomeric member unless moved toward" it, but no flow reaches the chamber until that member is penetrated (07 row N0c ?).<br>EP1137892A1 claims 1(e) and 8: a gap opens above a threshold on **chamber-side** pressure, in a member separate from the inflation valve (07 row N0b ?) | **Two sequential poppet ranges on one poppet.**<br>Over the normal stroke (from the crack pressure) the main passage is open and the purge shoulder is clear of the deflectable ring element.<br>Only when the pressure differential exceeds a higher over-travel threshold does over-travel bring the purge shoulder to bear on the deflectable ring element and deflect it. The result is three states: closed state, normal-open state, purge state | **Purging is added on top of normal inflation, not a condition of it.** Inflation and sealing work as in a conventional valve core up to the threshold. In the same inflation event, once the inflation device pushes the differential above the threshold, the purge state follows automatically, with no tool and no user action.<br>Prototype values: crack pressure 1.0 bar, threshold 3.5 bar, normal stroke 0.6 mm, over-travel 0.5 mm. A threshold "which every floor pump reaches" (§2; basis open, 01 Q5) | §2 (normal stroke; over-travel "above a threshold"); §3(4) (purge shoulder "only contacts the ring during over-travel"); §3(5); §4.<br>01 (i) state table; 03 C1–C4, C18; LOCKED `normal-open state`, `purge state`.<br>Bench data: an audible snap on every prototype inflation (indirect evidence only; 01 A9).<br>Not in any `07` reference (row N0b A or ? throughout) | "the poppet being movable through a normal stroke, in which the main passage is open and the purge shoulder is spaced from the deflectable ring element, and into over-travel beyond the normal stroke when the pressure differential exceeds an over-travel threshold higher than the crack pressure, the purge shoulder bearing on and deflecting the deflectable ring element in over-travel" | **Moderate.**<br>(a) A competitor lets the purge shoulder touch the ring on every opening, with no threshold. That escapes the claim only if purging on every opening does not work, which is unanswered (03 Q3), and it would then read on ref-02.<br>(b) The threshold is set by ring stiffness rather than by the return spring: keep the threshold functional (threshold-setting arrangement) and describe more than one structure, because of 35 U.S.C. §112(f).<br>(c) Positive "spaced from" wording avoids a negative limitation (lessons L1) |
| **2. Deflection only enlarges the main passage; other extra openings discharge outward or are permanently open.**<br>ref-02 [0019]: the lip "deflects outward to enlarge the flow passage" (07 row N0d ?).<br>EP1137892A1: bleed apertures "allow air to exit" the valve; claim 8, a gap between the reference's sealing ring and "the second solid support" (07 row N0d ?).<br>US11065925B2: a permanently open supplemental air hole (07 row N0d A).<br>CN215861914U: air flow cleans a filter on exhaust (07 row N0d A†) | **A purge gap separate from the main passage.** It is closed in the closed state and the normal-open state and is opened only by radial deflection of the deflectable ring element in the purge state. Through it, a purge flow path runs from the supply side into the inflatable chamber | **Air purge at inflation-device pressure** over the surfaces where sealant film collects, blowing it into the inflatable chamber (§2).<br>At cycle 40 the cured film was confined to the outside of the ring "in the purge gap region", while the sealing edge and poppet face were clean. All three conventional valve cores failed at cycles 12–18; the prototypes ran 40 cycles without failure (§8; bench data) | §2; §3(6); §8; bench data (film location); drawings README FIG-2 (air "through the main passage and through the purge gap into the tube"); 03 C6, C7; LOCKED `purge gap`, `purge flow path`.<br>**Support is conditional.** The location of the purge gap is stated two ways (§2 "stem bore" against §3(6) "core body bore"), and its opening is hard to reconcile with the 0.03 mm interference fit (§7) (01 Q1, Q2) | "a purge gap, separate from the main passage, that is closed in the closed state and the normal-open state and is opened by radial deflection of the deflectable ring element in the purge state, to form a purge flow path from the supply side into the inflatable chamber" | **Moderate on the art; critical on support.** A competitor using a different purge route (for example through the ring wall) escapes a claim that fixes the bounding surfaces, so define the purge gap by function and state, not by bore. If the gap cannot be enabled as disclosed, this row cannot be relied on, and row 1 plus row 3 must carry N0 |
| **3. Deposits are removed by a wiper carried on the moving member, by grinding, or by maintenance.**<br>US4719938A: a wiper ring on the valve member wipes the fixed bore on closing (abstract, claims 1 and 5; 07 row N1 A†).<br>US6006954A: a wiper on the valve stem removes deposits from the fixed wall (claims 1 and 6).<br>US11345196B2: a sealing ring on a moving rod squeezes sealant from the bore on reinstallation (abstract).<br>US4627461A: rotation of the closure member grinds the seat (state of the art).<br>ref-02: an elastomer that seals *around* particles | **Snap-back wipe driven by shape recovery.** The deflectable ring element is fixed in the core body (interference fit against the internal shoulder). When the pressure differential falls, its own shape recovery moves it across the poppet and shears off sealant film. The relative movement comes from the ring's recovery, not from the stroke of the valve member | A mechanical cleaning action on the **moving** part (the poppet face) at the end of every inflation event, with no tool and no user action. Partially cured sealant film is sheared off rather than embedded, in contrast to a rubber seat (§2).<br>Bench: the poppet face was clean at cycle 40. The wipe's share of the effect is **not isolated** from the air purge (01 Q24) | §2 ("wipes across the poppet face with a snap"); §6 (PEEK wipe weaker); §7 (ring pressed in against the internal shoulder); §8; bench data (audible snap on removal of the pump head; clean poppet face); 03 C9; LOCKED `snap-back wipe`, `shape recovery` | "the deflectable ring element being held in the core body and, on shape recovery when the pressure differential falls, moving across the poppet so as to wipe it" | **Moderate.**<br>(a) A competitor omits the wipe and relies on the air purge. Keep the wipe out of the independent claim unless 03 Q1 shows it is needed.<br>(b) A wiper carried on the poppet (as in US4719938A) avoids the claim, but it is then closer to the art and harder to defend.<br>(c) Which ring surface wipes which poppet surface is unknown (01 Q10), so the language must stay general |
| **4. Elastomer seat ring, or a single-sentence spring-steel lip; superelastic NiTi known only as static or hatch seals.**<br>ref-02 [0015]–[0021] (60–80 Shore A nitrile or fluoroelastomer) and [0024] (07 row N4 ?).<br>US6393765B1: superelastic NiTi seal element on hatches (07 row N4 E).<br>US9982818B2: NiTi sealing ring, actuated thermally (07 row N4 E) | **Superelastic seat ring in the valve core.** A superelastic alloy seat ring with an austenite finish temperature below 5 °C, so that it is superelastic at riding temperatures. It is deflected repeatedly by the poppet's purge shoulder and recovers on each inflation event | "Fast and stiff" recovery, not a slow elastomer creep, gives the snap-back wipe its force (§2). Latex does not embed in it as it would in a rubber seat (§2). The PEEK alternative gives a weaker wipe (§6), which shows the effect depends on the material.<br>**Not isolated experimentally** (08 Q6) | §2; §4 (Af below 5 °C); §5 (NiTi, nominally 55.8 wt% Ni); §6; §9 item 2 (CO2 cold-shock margin unknown); 03 C14–C16; bench data | "the seat ring being of a superelastic alloy having an austenite finish temperature below 5 °C" | **High** for an independent claim: PEEK (Alternative A) and stainless spring (Alternative B) are the inventor's own design-arounds. Use it as a dependent claim or fallback only. Rated a *strong* increment in `08` |
| **5. Wave-profile ring whose radial movement is thermally driven, in a static seal between two members.**<br>US9982818B2 abstract and claims 3–5: "at least one peak and at least one trough"; heating moves the inner portion inward and the outer portion outward (07 row N3 ?) | **Convoluted wall under axial load.** The seat ring's convoluted wall (one or two shallow convolutions) converts the **axial** load that the purge shoulder applies during over-travel into radial deflection, and the wall recovers elastically | It turns axial poppet over-travel (prototype 0.5 mm; believed 0.4–0.9 mm) into radial opening of the purge gap (prototype 0.15 mm; believed 0.10–0.25 mm). A mechanical conversion, repeated every inflation event, at service temperature, with no heating | §3(3) (axial load on the sealing edge "translates into radial expansion", in the inventor's words); §4 (convolution amplitude 0.12 mm, 0.08–0.20 mm; wall 0.15–0.30 mm); §6 (Alternative A has "the same convoluted wall"); §7; 03 C12, C13 | "the seat ring having a convoluted wall that converts axial load applied by the purge shoulder into radial deflection of the seat ring" | **Moderate to high.** A straight wall, or any other geometry that turns axial load into radial movement, would avoid the claim. Whether such geometries work is unanswered (01 Q12). Keep it dependent. Rated *moderate* as an increment in `08` |
| **6. The seat ring seals and deflects, but only to enlarge the main passage; other sealing and cleaning parts are separate.**<br>ref-02 claim 1 (07 row N2 E).<br>US11179979B2: a separate elastic one-way valve (07 row N0e ?).<br>ref-01: rigid seat (07 row N2 A) | **One seat ring, two jobs.** The same seat ring carries the sealing edge on which the sealing face rests in the closed state and, in the purge state, is deflected by the purge shoulder to open the purge gap | One part seals, purges and wipes. The sealing edge is cleaned by the same cycle that opens the purge gap; the sealing edge was clean at cycle 40 (§8). No additional part or axial length is needed, whereas Alternative B needs "one more part and more axial length" (§6) | §3(3), §3(4); §6 (Alternative B trade-off); §8; 03 C10, C11; LOCKED `sealing edge` | "the sealing face resting on a sealing edge of the seat ring in the closed state" | **High.** Alternative B separates sealing from purging. Keep this dependent and cover Alternative B through the deflectable ring element genus (03 Q5). On its own it is known from ref-02 claim 1 (a *strong* increment in `08`) |
| **7. Rising-rate or dual springs used for other purposes.**<br>US9297373B2 claim 1: parallel progressive springs, for surge suppression.<br>EP1137892A1 claim 28: springs on opposite sides of a disk.<br>US4627461A claim 3: progressive cushioning spring (07 rows N5 ?) | **Two spring stages that set two thresholds.** The return spring has a first spring stage setting the crack pressure and a second spring stage, engaged at the end of the normal stroke, setting the over-travel threshold | It separates the crack pressure (0.8–1.5 bar believed; 1.0 bar prototype) from the over-travel threshold (2.5–5.0 bar believed; 3.5 bar prototype), so the purge state is a distinct, higher-differential state | §3(5); §4; 03 C17; LOCKED `first spring stage`, `second spring stage` | "a return spring having a first spring stage that sets the crack pressure and a second spring stage that sets the over-travel threshold" | **High.** It is one species of the threshold-setting arrangement; other means are unanswered (01 Q6). Dependent only. Rated a *strong* increment in `08` |

**Not distinctions: the drafting must not rely on these (each is in the `07` charts):**
- A tyre valve for sealant-filled chambers, or the sealant blockage problem (US11904644B2, US11065925B2, US11345196B2, ref-01, EP4735276A1: rows F0/F1 E).
- A cleaning action stated only as a result (CN215861914U, US4719938A, US4627461A). This is result-only language and needs the structure of rows 1–3.
- Superelastic NiTi as a deformable seal material in itself (US6393765B1), or a wave-profile NiTi sealing ring in itself (US9982818B2).
- A resilient seat that the poppet deflects, or that recovers when the pump is removed, in itself (ref-02 claim 4, [0020]).
- A moving member that deforms a resilient member after its initial travel, in itself (US4462449A claim 1).
- Two springs, or rising-rate springs, in themselves (US9297373B2, EP1137892A1).
- The §4 ranges and §7 process steps in themselves (08: routine optimisation / CGK).

## Rationale

**Order of the rows.** The ordering follows `08`. Row 1 comes first because the normal-stroke/over-travel sequence is the relationship absent from every reference and because it answers the ref-02 claim 4 and US4462449A attack directly. Row 2 comes next because it answers ref-02 [0019] and EP1137892A1 claim 8. It is honest to put it second rather than first, because its support is conditional on 01 Q1/Q2. Row 3 is the only distinction that answers the wiping art, and its strength lies in the kinematics (the recovery drives the movement, not the stroke).

**The lower rows.** Rows 4–7 are real, supported features. `08` rates them as known or obvious increments, so their design-around risk column says plainly that they are fallbacks. Every "possible claim language" entry is positive and structural, to follow lessons L1. Results such as "removes sealant film" appear only in the effect column.

**What I left out.** I did not use the swelling of nitrile in ammonia-bearing sealant against ref-02. The ref-02 file itself notes that the disclosure does not support it, and neither the inventor's disclosure nor the bench data mentions it. The same applies to fatigue benefits of purging only above a threshold: nothing in the dossier states it.

## Assumptions

A1. No Gate 1 answers exist, so rows 1–3 follow `03` (air purge essential, wipe advantageous). If 03 Q1 shows that the wipe alone suffices, row 3 moves up and row 2 becomes a dependent claim. Blocking for P3 and P5.

A2. The deflectable ring element genus covers the seat ring (including Alternative A) and the Alternative B wiper ring, as locked. The inventor has not confirmed that Alternatives A and B are within the invention (03 Q5). Blocking for P5.

A3. "Held in the core body" in row 3 rests on §3(3) and §7 (pressed in against the internal shoulder). Other retention methods are unanswered (01 Q17). Not blocking.

A4. The technical effects are stated as the inventor states them (§2) and as the bench data corroborates them. No effect is attributed to an individual feature beyond what the dossier says. Not blocking.

## Open Questions

Q1. Row 2 depends on 01 Q1/Q2: which surfaces bound the purge gap, how it opens against the 0.03 mm interference fit, and the full air path into the inflatable chamber. Until these are answered, the separate-purge-gap distinction is unsupported as written. Blocks P3, P4, P5.

Q2. Must the purge shoulder be clear of the deflectable ring element throughout the normal stroke, or would contact on every opening still work (03 Q3)? Row 1 depends on the threshold being necessary. Blocks P3, P5.

Q3. Which ring surface wipes which poppet surface, in what direction and over what distance (01 Q10)? Row 3's claim language cannot be made more specific without it. Blocks P4, P5.

Q4. Does the air purge alone, the snap-back wipe alone, or both produce the effect (03 Q1)? This decides whether row 2 or row 3 goes in the independent claim. Blocks P3, P5.

Q5. Is the convoluted wall essential, and has any other geometry that turns axial load into radial deflection been conceived (01 Q12)? This decides row 5's design-around cover. Blocks P3, P5.

Q6. Has any threshold-setting arrangement other than the two spring stages been conceived (01 Q6)? This decides how many structures the Description must give for row 1 under §112(f). Blocks P4, P5.

Q7. Coverage is thin, and ref-01 and ref-02 are fictional (07 Q1, Q2). The matrix is untested against a professional search. Blocks P3, PACKAGE.

```json
{
  "prompt": "09",
  "status": "partial",
  "assumptions": [
    {"id": "A1", "text": "No Gate 1 answers exist; rows 1-3 follow 03 (air purge essential, wipe advantageous); if the wipe alone suffices, row 3 moves up and row 2 becomes dependent.", "blocking": true},
    {"id": "A2", "text": "Deflectable ring element genus covers the seat ring (incl. Alternative A) and the Alternative B wiper ring, as locked; inventor has not confirmed (03 Q5).", "blocking": true},
    {"id": "A3", "text": "'Held in the core body' (row 3) rests on §3(3) and §7 (pressed against the internal shoulder); other retention methods unanswered (01 Q17).", "blocking": false},
    {"id": "A4", "text": "Technical effects stated as the inventor states them (§2) and as the bench data corroborates; no effect attributed to an individual feature beyond the dossier.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "Row 2 depends on 01 Q1/Q2 (purge gap boundaries, opening against the interference fit, full air path); unsupported as written until answered.", "blocks": ["P3", "P4", "P5"]},
    {"id": "Q2", "text": "Must the purge shoulder be clear of the ring element throughout the normal stroke, or would contact on every opening work (03 Q3)?", "blocks": ["P3", "P5"]},
    {"id": "Q3", "text": "Which ring surface wipes which poppet surface, direction and distance (01 Q10)?", "blocks": ["P4", "P5"]},
    {"id": "Q4", "text": "Air purge alone, snap-back wipe alone, or both (03 Q1)? Decides whether row 2 or row 3 goes in the independent claim.", "blocks": ["P3", "P5"]},
    {"id": "Q5", "text": "Is the convoluted wall essential; any other axial-to-radial geometry conceived (01 Q12)?", "blocks": ["P3", "P5"]},
    {"id": "Q6", "text": "Any threshold-setting arrangement other than the two spring stages (01 Q6)? Sets the structures needed under §112(f).", "blocks": ["P4", "P5"]},
    {"id": "Q7", "text": "Coverage thin and ref-01/ref-02 fictional (07 Q1, Q2); matrix untested against a professional search.", "blocks": ["P3", "PACKAGE"]}
  ],
  "new_terms": [
    {"term": "threshold-setting arrangement", "maps_to": "second spring stage", "reason": "Locked genus of the second spring stage; used in row 1 design-around note so the threshold is not tied to the return spring."}
  ],
  "support_refs": [
    {"item": "Row 1 normal stroke then over-travel; purge shoulder contacts only in over-travel", "support": "intake/disclosure.md §2, §3(4), §3(5), §4; runs/r1/P1/01.md (i); runs/r1/P1/03.md C1-C4, C18; intake/data/bench-test.md (audible snap)"},
    {"item": "Row 2 separate purge gap and purge flow path", "support": "intake/disclosure.md §2, §3(6), §8; intake/drawings/README.md FIG-2; runs/r1/P1/03.md C6, C7; conditional on 01 Q1, Q2"},
    {"item": "Row 3 snap-back wipe by shape recovery of ring held in core body", "support": "intake/disclosure.md §2, §6, §7, §8; intake/data/bench-test.md; runs/r1/P1/03.md C9"},
    {"item": "Row 4 superelastic alloy, Af below 5 °C", "support": "intake/disclosure.md §2, §4, §5, §6, §9; runs/r1/P1/03.md C14-C16"},
    {"item": "Row 5 convoluted wall axial-to-radial; over-travel 0.4-0.9 mm; purge gap opening 0.10-0.25 mm", "support": "intake/disclosure.md §3(3), §4, §6, §7; runs/r1/P1/03.md C12, C13"},
    {"item": "Row 6 seat ring carries sealing edge and is deflected", "support": "intake/disclosure.md §3(3), §3(4), §6, §8; runs/r1/P1/03.md C10, C11"},
    {"item": "Row 7 first and second spring stages; crack pressure and over-travel threshold ranges", "support": "intake/disclosure.md §3(5), §4; runs/r1/P1/03.md C17"},
    {"item": "Prior-art features in every row", "support": "runs/r1/P2/07.md chart rows as cited; runs/r1/P2/08.md ratings"}
  ],
  "disclosure_requests": [
    {"limitation": "Row 2 purge gap separate from the main passage, closed in closed and normal-open states", "needed_disclosure": "Written description of the purge gap boundaries, how radial deflection opens it despite the interference fit, and the full air path into the inflatable chamber (01 Q1, Q2)."},
    {"limitation": "Row 1 threshold-setting arrangement", "needed_disclosure": "Any structure other than the two spring stages that sets the over-travel threshold, and the stroke at which the second spring stage engages (01 Q6, Q7)."},
    {"limitation": "Row 3 snap-back wipe", "needed_disclosure": "Which ring surface moves across which poppet surface, direction and distance (01 Q10)."}
  ],
  "open_disagreements": [],
  "narrowing_suggested": []
}
```
````

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/prior-art/INDEX.md`

```markdown
# Prior-art index — matter valve-oc-20260930, run r1

Compiled by the Prior-Art Analyst, 2026-09-30 (search step RES). Access date for every URL: 2026-09-30.
This index is a drafting and analysis aid, not a professional search or a patentability opinion; qualified patent counsel signs off.

**Nucleus concepts (from P2/06):** N1 superelastic NiTi seat ring contacted by the poppet · N2 thin convoluted (wave) wall turning axial load into radial expansion · N3 poppet over-travel above a pressure threshold (two-rate return spring) · N4 over-travel loads the seat ring and opens a purge gap closed at rest · N5 purge air across the sealant-accumulation surfaces · N6 snap-back recovery of the seat wipes the poppet face · N7 Presta/tubeless valve used with liquid sealant.

**Closeness scale:** 5 reads on the nucleus as a whole · 4 reads on most nucleus concepts · 3 discloses one nucleus concept closely, or the problem plus a related mechanism · 2 same problem or an analogous mechanism, weakly · 1 background.

**Reading status.** The references below were read through the Google Patents page (abstract, description and claim 1) by a page-summarising fetch. Claim wording in the reference files must be taken from the full text the runner saves in `refs/`; charts in Prompt 07 must quote those files, not this index. Where claim 1 was not seen, the row says so.

## Patent references (fetchable by number)

| # | Publication number | Title | Assignee | Priority date | Publication date | URL | Concepts hit | Why it matters | Closeness |
|---|---|---|---|---|---|---|---|---|---|
| 1 | US 9,982,818 B2 | Shape memory alloy sealing ring and assembly | UTC Aerospace Systems Wroclaw Sp. z o.o. (orig. HS Wroclaw) | 2015-11-23 | 2018-05-29 | https://patents.google.com/patent/US9982818B2/en | N1 (NiTi, thermally actuated), N2 | NiTi ring with a wave-like section (S, sinusoidal, W, zigzag) whose peaks and troughs give radial displacement of its inner and outer sealing portions. Closest found for the ring geometry and material. It is a static seal between a tube and a housing, not a seat for a moving valve member, and it is thermally actuated, not superelastic. Likely secondary reference for N1+N2. | 3 |
| 2 | US 11,904,644 B2 | Inflation system for tubeless tires | Santa Cruz Bicycles LLC | 2019-04-17 | 2024-02-20 | https://patents.google.com/patent/US11904644B2/en | N7, N5 (in part) | Bicycle tubeless valve built because Presta/Schrader cores clog with sealant. A resilient seating surface on the valve stem closes on a beveled external seat, and opening gives an annular air flow around the seat. Closest tyre-valve art for the problem and for flow across the seat. No deforming seat, no over-travel, no wipe. Likely primary reference. | 3 |
| 3 | US 4,719,938 A | Self-cleaning valve and cryopump utilizing the same | Helix Technology Corp. | 1985-01-22 | 1988-01-19 | https://patents.google.com/patent/US4719938A/en | N6 (functional) | Wiper rings, pressed outward by a spring-steel expansion ring, move ahead of the seal ring as the valve member closes and wipe debris from the sealing surface. Closing-stroke wiping by a resiliently loaded element: a combination partner against N6. | 3 |
| 4 | US 11,345,196 B2 | Tire valve assembly | Kunshan Fuluo Auto Parts Co., Ltd. | 2020-04-14 | 2022-05-31 | https://patents.google.com/patent/US11345196B2/en | N7, N6 (manual) | Tyre valve built for tyre repair liquid blockage. A seal ring on a movable rod squeezes residual liquid off the air-pipe wall when the rod is reinserted. A wiping action in a tyre valve against sealant, but performed by a maintenance movement, not by recovery of the seat. | 3 |
| 5 | US 6,393,765 B1 | Superelastic sealing closures | United States of America, Secretary of the Navy | 2000-08-24 | 2002-05-28 | https://patents.google.com/patent/US6393765B1/en | N1 | Superelastic NiTi sheet-metal seal elements that deform on closure and recover elastically when the closure opens (hatches, doors). Evidence that superelastic NiTi was known as a repeatedly deforming seal element. | 3 |
| 6 | US 4,462,449 A | Valve core for pneumatic tires | John H. Zabel, Jr. (individual) | 1982-02-02 | 1984-07-31 | https://patents.google.com/patent/US4462449A/en | N7, N5 | Tyre valve core with a collapsed elastomer tubular member. States that soil entering is "swept through" on inflation and that the core is "self cleaning". Early statement of inflation-flow self-cleaning in a tyre valve core; no seat ring or wipe. | 3 |
| 7 | US 6,006,954 A | Metering valve | Bespak plc (now Consort Medical) | 1997-06-10 | 1999-12-28 | https://patents.google.com/patent/US6006954A/en | N6 (functional) | Acetal or polyester wiper on the valve stem scrapes deposited solids from the chamber wall on both strokes (claim 1 recites the wiper scraping to remove deposited matter). Deposit-removing wiper driven by valve movement. | 2 |
| 8 | US 11,179,979 B2 | Valve for tubeless tires | Sport Components AG | 2016-08-18 | 2021-11-23 | https://patents.google.com/patent/US11179979B2/en | N7 | Elastic duckbill first valve at the stem base stops sealant entering the valve stem, and tyre pressure increases lip contact. Prevention by exclusion, not removal. Claim 1 was not seen in the fetched page; read it from the saved full text. | 2 |
| 9 | US 11,065,925 B2 | Valve stem apparatus, assemblies and methods for use | Liquitube Industries LLC | 2017-12-15 | 2021-07-20 | https://patents.google.com/patent/US11065925B2/en | N7 | Clog-resistant tyre valve stem using an extension tube with radial supplemental air holes and a deflecting surface. Same problem, flow-path solution; no seat or core change. | 2 |
| 10 | EP 4735276 A1 | Inflation valve comprising a ball valve for tubeless tyre | Not identified on the page read | 2023-08-18 | 2026-05-06 | https://www.goveda.com/patent/EP-4735276-A1 | N7 | Replaces the Presta core with a ball valve to cure restricted flow and sealant clogging. Recent (published 2026) evidence of the problem and of a different solution. Applicant to be taken from the saved full text. | 2 |
| 11 | CN 215861914 U | Central tire inflation and deflation system tire valve with self-cleaning function | Jinan Weidisi Transmission Technology Co., Ltd. | 2021-09-29 | 2022-02-18 | https://patents.google.com/patent/CN215861914U/en | N5 (functional) | Tyre valve in which exhaust air flow at pressure blows debris off a filter element beside an annular sealing gasket. Air-flow self-cleaning in a tyre valve; read in machine translation. | 2 |
| 12 | US 4,627,461 A | Self cleaning valve | K.J. Baillie Pty. Ltd. | 1985-10-03 | 1986-12-09 | https://patents.google.com/patent/US4627461A/en | N6 (functional) | The closure member is rotated against the seat during closing to grind away deposits. Seat cleaning driven by the closing movement: an alternative mechanism to N6. | 2 |
| 13 | US 4,408,632 A | High flow shroud check valve | Brunswick Corp. (later Circle Seal Controls) | 1981-04-23 | 1983-10-11 | https://patents.google.com/patent/US4408632A/en | N3, N4 (partial) | Poppet with concentric primary and secondary seats and a resilient seal ring; the flow paths open in sequence as the poppet travels. Background for a poppet that opens a second path at a later stage of its stroke. | 2 |
| 14 | EP 1137892 A1 | Pressure regulating tire valve and core | Sumnett Inc. | 1998-10-23 | 2001-10-04 | https://patents.google.com/patent/EP1137892A1/en | N3 (partial), N7 | Tyre valve core with a calibrated spring. Above a set pressure the disk moves and exposes bleed apertures: a second flow path opened above a pressure threshold, in a tyre valve core. Claim 1 was not seen; read it from the saved full text. | 2 |
| 15 | US 9,297,373 B2 | Differential pressure valve with parallel biasing springs and method for reducing spring surge | Nuovo Pignone S.r.l. | 2011-07-19 | 2016-03-29 | https://patents.google.com/patent/US9297373B2/en | N3 (spring only) | Poppet valve biased by two parallel, progressive (non-linear) compression springs. Background for a non-linear valve return spring. The springs act together, not as sequential stages. | 1 |

## Requester-supplied references (intake; not fetchable by number)

| Intake file | Description | Concepts hit | Note |
|---|---|---|---|
| `intake/prior-art/ref-01-sealant-resistant-core.md` | Test document: sealant-resistant valve core with removable insert, low-adhesion coated poppet, rigid seat, enlarged bore | N7; N5 ambiguous ([0022]) | The file states that the document and its publication number are **fictional**. Do not fetch by number: the stated number may belong to an unrelated real document. Chart from the intake file only (see P2/06 Q3). |
| `intake/prior-art/ref-02-elastomer-seat-valve.md` | Test document: tyre valve with an elastomer lip seat that deflects outward under inflation pressure; a spring-steel lip alternative is mentioned | N7; seat deflection (main path only); N1 ambiguous ([0024] spring-steel lip) | The file states that the document and its number are **fictional**. Do not fetch by number, for the same reason. Chart from the intake file only. |

## Coverage statement

**Coverage is thin.** A professional search is warranted before Phase 3 relies on this picture.

- Nothing found discloses a superelastic or shape-memory seat against which a moving valve member seals (N1 in its valve role), the combination N3+N4 in any valve, or seat-recovery wiping (N6 as claimed). The nearest material art is static seals (#1, #5); the nearest wiping art is separate wipers (#3, #7) or a maintenance movement (#4).
- The search was web-only, English-language and single-engine (Google Patents through web search). There was no Espacenet or CNIPA classification browsing, no CPC-group walk of F16K 15/20 or B60C 29/00, and no citation chasing beyond reading the documents.
- Chinese, Taiwanese and Japanese bicycle-valve utility models are under-represented (one CN document).
- No non-patent literature was saved: no product documentation for the commercial clog-resistant tubeless valves (the page-level marketing claims are not citable), and no NiTi superelastic fatigue or low-temperature literature.
- Commercial valves described as "patent-pending" or "patented" (see search-log) could not be linked to a publication number and are not indexed.
```

## Files you may read (not embedded: open only what you need)

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/prior-art/refs`/

## Files to write

Write each of these with your Write tool, at exactly this path, one file per call (the folders exist). Write nothing outside the run folder `{R}`. Do not run the checks yourself: the runner runs them and will tell you if anything fails.

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/debate/d1-attack.md`

When every file is written, reply with one line per file (path and a few words on what it holds) and anything the runner must route: open questions, disclosure requests, open disagreements, narrowing suggested. Nothing else.
