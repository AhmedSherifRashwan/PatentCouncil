# Patent Council · matter `valve-oc-20260930` · run `r1` · step `P5-23` · profile full

You are the **Claims Architect**. Follow your AGENTS.md. This message is the whole brief: what to do, the prompts to execute, every input (embedded below, so do not re-read those files), and the exact files to write.

## What to do

Run Prompt 23, in parallel with its siblings. Build generously: the fallback depth of the claim family comes from here.

**Time budget:** about 10 minutes. The whole matter is planned to finish end to end in two hours. Be complete, but write each deliverable once: no drafts, no repetition, no padding.

## Prompt 23 — Dependent-claim ladder  (kind `drafting`)

**Write your reply to:** `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/23.md`

*Build fallback positions deliberately.*

For each independent claim create a dependent-claim ladder from broad to narrow. Cover structural relationships, materials, geometry, ranges, operating modes, control logic, manufacturing features and use conditions. Each dependent claim should add a meaningful fallback rather than cosmetic detail. Identify the technical effect associated with each added limitation.

**How to work.** The description in front of you is the only source of support. Any limitation that lacks an explicit passage in the description must NOT be drafted: leave it out, and record it in `disclosure_requests` (limitation, and the disclosure ip-spec would need to add) so the inner loop can supply the support. Use locked preferred terms verbatim and the registry's component names; where a claim term needs a reference sign, use the registry numeral. Cite the supporting paragraph for every limitation in `support_refs`. Under `### Dependent Claim Ladders` use one H4 per independent claim, then the dependent claims in full, numbered continuously after the independent claims of `22`, each followed by a one-line note: added limitation | technical effect | support paragraph | the prior-art or design-around risk it answers. Ranges come only from the description's stated ranges; do not create intermediate values the description does not recite. Reply exactly in the drafting output contract: `## Deliverable` (with the H3 sections named above), `## Rationale`, `## Assumptions`, `## Open Questions`, then one final fenced `json` envelope. No preamble before `## Deliverable`; nothing after the envelope. Reuse locked preferred terms verbatim; declare any other term in `new_terms` with a reason.

## Output contract (drafting)

Your reply MUST be markdown with exactly these H2 headings, in this order, and nothing before the first one:

## Deliverable

One H3 heading per deliverable section named in the task, in the order named, each containing the finished content for that section. Only the text under `## Deliverable` is carried forward to later prompts, to the package and to the human; anything you want them to see goes here.

## Rationale

Why you drafted or analysed it this way: trade-offs, alternatives considered, how conflicts between inputs were resolved. This section is stripped before the package reaches the independent reviewer.

## Assumptions

Every assumption you made, numbered A1, A2 ..., each saying whether it blocks a later phase.

## Open Questions

Every question the dossier does not answer, numbered Q1, Q2 ..., each naming the phase(s) it blocks.

Then ONE final fenced ```json block, and nothing after it, with exactly this shape:

```json
{
  "prompt": "<id>",
  "status": "complete|partial",
  "assumptions": [{"id": "A1", "text": "...", "blocking": false}],
  "open_questions": [{"id": "Q1", "text": "...", "blocks": ["P4"]}],
  "new_terms": [{"term": "...", "maps_to": "<locked preferred term or null>", "reason": "..."}],
  "support_refs": [{"item": "...", "support": "..."}],
  "disclosure_requests": [{"limitation": "...", "needed_disclosure": "..."}],
  "open_disagreements": [{"topic": "...", "position": "..."}],
  "narrowing_suggested": []
}
```

Rules:

- `prompt` is the id of the task you were given. `status` is `partial` whenever a required input was missing or an open question stopped you finishing a section.
- The lists in the envelope must mirror the prose sections (`## Assumptions` ↔ `assumptions`, `## Open Questions` ↔ `open_questions`). Empty lists are `[]`, never omitted.
- `blocks` values are phase ids: `P1`, `P2`, `P3`, `P4`, `P5`, `REVIEW`, `PACKAGE`.
- `support_refs` records, for every drafted item that relies on the dossier (a limitation, a range, an example, a definition), where it is supported: a paragraph number, section id, figure, intake file or earlier output.
- `disclosure_requests` is used by the claims drafter for limitations it could not support, and by the specification drafter for disclosure it needs but the confirmed embodiments do not contain. Each entry names the limitation or passage and the disclosure that would be needed.
- `open_disagreements` records a position you hold that conflicts with another agent's output in the inner loop (Phase 4 ↔ Phase 5). `narrowing_suggested` lists claim narrowings you consider necessary but did not apply; both are surfaced to the human.
- Terminology rule: reuse the locked preferred terms verbatim (once the terminology lock exists; before it, the terms used in the Phase 1 outputs). Any other term for a locked concept must be declared in `new_terms` with the locked term it maps to and a reason; an undeclared synonym or a term from the avoid list is a contract violation. `maps_to` is `null` only for a genuinely new concept.
- Write the deliverable in British spelling. No preamble, no closing remarks, no offers of further help.

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

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P1/02.md`

````markdown
## Deliverable

### Commercial Value Map

This is a drafting and analysis aid prepared by AI. It is not legal advice and makes no statement about patentability; qualified patent counsel signs off before anything is filed.

Ranking basis: which subject matter a competitor would have to practise to sell a comparable product or capture the same effect, read from `01` (Structured Invention Disclosure), the raw disclosure and the bench-test data. Component names and reference numerals are those locked in `01`.

| Rank | Subject matter | Who would practise it | Why it matters commercially | Recommended protection |
|---|---|---|---|---|
| 1 | **Valve core assembly** — core body (20) + seat ring (30) + poppet (40, with sealing face (42) and purge shoulder (44)) + threshold-setting return spring (50) (+ optional lock nut (70)) — drafted so the claim does **not** require the valve stem (10) as an element | Any manufacturer or aftermarket brand selling a compatible replacement valve core | This is the sellable, swappable unit itself. §1 records that conventional cores are already "sold in multipacks" for replacement after fouling, and the bench data quantifies exactly the advantage a buyer is paying for: conventional cores failed at cycle 12–18 (leak or block), while all three prototypes ran the full 40-cycle test with inflation time rising only 8–14% and leak-down staying at 0.1–0.2 bar/24 h. That measured durability gap is the product's whole commercial pitch, and the retrofit channel exists independently of any OEM stem sale. Claiming the core without the stem as a required element catches a competitor who sells only a compatible core (the far more likely infringer than one who also makes a matching stem) | **Independent claim** |
| 2 | **Resiliently deflectable seat/purge ring** (30) — the ring element whose wall geometry converts axial over-travel load into radial expansion, opens the purge gap (60), and elastically recovers to produce the snap-back wipe | Any component supplier selling a compatible ring or insert to third-party core assemblers, or a core maker sourcing the ring separately | This is the narrowest and most defensible point of novelty — no version of the self-purge effect exists without some form of this element, and the bench data's post-test inspection (clean sealing edge and clean poppet face at cycle 40, film only on the ring's outer surface) shows the ring is where the measured effect actually resides. A component-level claim catches suppliers who never sell a complete core, and anchors the dependent ladder for material and geometry species | **Independent claim** (component), with dependents for NiTi species, convolution form, and the broader genus at rank 5 |
| 3 | **Complete valve stem (10) + core, or a tube/tyre/wheel assembly incorporating it** | Tube and tyre manufacturers, complete-wheel and complete-bicycle OEMs | A separate, high-volume channel from the aftermarket core (rank 1): every new tube, tubeless tyre or wheel sold with the valve pre-fitted. Catches an OEM who integrates the valve without ever selling the core as a spare part | **Separate claim family** (system claim reciting the tube/tyre/wheel with the valve core of the independent apparatus claim) |
| 4 | **Method of manufacturing the seat ring** — laser-cutting the convoluted profile from NiTi tube stock on a mandrel, shape-setting in a fixture holding the wave geometry, water-quenching, electropolishing, and press-fitting into the core body with a controlled interference | A component manufacturer producing the ring at volume; likely a specialised NiTi subcontractor given the process described in §7 | Even if a competitor designs around the apparatus claims with a different ring geometry, a process claim can still catch anyone using this manufacturing route, and is a useful fallback where the finished ring geometry is hard to reverse-engineer or is made abroad | **Separate claim family** (process claims) |
| 5 | **Genus of resiliently deflectable ring material** (not limited to NiTi) — covers Alternative A, a PEEK ring with the same convoluted wall, proposed by the inventor for a lower-cost line | A competitor building a cheaper, non-metallic version of the same ring geometry — exactly the route the inventor itself has already identified | This is the inventor's own named design-around (§6, Alternative A). Claiming NiTi specifically and nothing broader hands a competitor an easy non-infringing substitute for a budget product | **Dependent claim** broadening the rank-2 ring claim to a material genus, with NiTi as a preferred dependent species |
| 6 | **Split sealing/purge architecture** — a rigid sealing seat plus a separate, thin resiliently deflectable wiper ring below it, deflected outward by the purge shoulder (Alternative B) | A competitor who separates the sealing and purge/wipe functions into two parts specifically to avoid a single-ring claim | Also the inventor's own named design-around (§6, Alternative B). A claim requiring one ring that both seals and wipes would not reach this two-part structure | **Dependent claim / separate claim family** reciting a sealing member and a separate resiliently deflectable wiping member as an alternative structure |
| 7 | **Threshold-setting mechanism** — currently embodied as the two-rate return spring (50), but claimed as any arrangement requiring a higher pressure differential to reach over-travel than to reach normal opening | Any core manufacturer, since some threshold behaviour is necessary to make the purge event a distinct, higher-pressure action rather than something that happens on every normal inflation | `01`'s Q6 leaves open whether the two-rate spring is the only way to set the threshold — the ring's own stiffness may contribute. Claiming the independent apparatus around "a two-rate spring" specifically would let a competitor substitute a different threshold means for a literal design-around | **Dependent claim** (independent claim should use functional language for the threshold, per `01`'s open question on essentiality) |
| 8 | **Self-purging method of operation** — moving the poppet through its normal stroke and into over-travel so the purge shoulder deflects the ring and opens the purge gap for air purge, then removing the pump head to allow recovery and snap-back wipe | Technically, every rider using the valve, and any competitor's valve exhibiting the same operating sequence | A freestanding method claim is commercially weak here: the event is internal, momentary (confirmed in the bench data only indirectly, by an audible snap on pump-head removal) and hidden inside the valve during ordinary pump use, so infringement by a rider is essentially undetectable and undesirable to assert. Its value is as a fallback against a competitor's differently-built valve that performs the same steps | **Dependent claim** on the apparatus (claimed as the apparatus "configured to" perform the steps), not a standalone method claim asserted against end users — flagged to Claims Architect (P5) for a final call on detectability |
| 9 | **Corrosion-resistant body variant** — stainless steel 303 core body/stem, machined and mentioned by the inventor for compatibility with ammonia-bearing sealant | A premium product line, or markets/sealant chemistries where brass corrosion is a known issue | Real but modest differentiator; the inventor has already machined this variant (though the bench data lists brass-body prototypes only, so it was not run through the durability test), so it is cheap to claim, but it protects a product line rather than the core inventive effect | **Dependent claim** |
| 10 | **Thermal two-way shape-memory manual-purge variant** (Af about 35–40 °C, warmed by hand to open the purge gap without a pump) | No current practitioner; a possible future pump-free-purge product | The inventor is explicitly unsure this is worth pursuing and has no data on it (§6). Ranking it for completeness only | **Not recommended for the main claim set now**; candidate for a dependent claim or a later continuation if the inventor confirms intent and supplies data |

No separate **consumable** was identified: the sealant itself is a third-party product used with the valve, not part of the invention, and is not addressed here.

## Rationale

I ranked by what a competitor must copy to obtain the same commercial outcome, in the order the AGENTS.md standing instruction asks for, not by inventive cleverness — the two-rate spring (rank 7) is a good example of something structurally necessary but commercially secondary to the ring itself. The most consequential judgement call is splitting rank 1 (core sold independently of the stem) from rank 3 (the same core integrated by an OEM into a tube, tyre or wheel): §1 describes an existing replacement-core market ("cores are sold in multipacks"), and drafting the primary independent claim so the stem is not a required element is what lets that claim reach a competitor who only ever sells a core. This is a claim-strategy consequence of the commercial analysis, not a technical fact, so I flagged it in Assumptions rather than asserting it as inventor-confirmed business intent.

With `intake/data/bench-test.md` now in the dossier, I strengthened ranks 1 and 2 with the actual per-core figures (cycles to failure, inflation-time drift, leak-down) rather than only the disclosure's summary statement, since a ranked commercial map is more useful to the drafters with the quantified advantage attached to the component that carries it. I did not use the bench data to change the ranking order itself — the durability data corroborates rank 1 and 2's position rather than establishing it, since the underlying commercial logic (an existing replacement-part market, and the ring being the narrowest point of novelty) already placed them there from the disclosure alone.

Ranks 5 and 6 track the inventor's own §6 alternatives directly, because a design-around the inventor has already named is the clearest evidence of where competitors will go; the disclosure_requests carried forward from `01` (support for Alternatives A and B) apply equally here — this map ranks them for commercial importance but does not assert they are supported for claiming yet. I ranked the method claim (rank 8) low relative to its structural counterpart because method claims requiring proof of a rider's internal, momentary valve action are a recognised enforcement weakness, and the bench data itself only detects that action indirectly (an audible snap), which reinforces the detectability concern rather than resolving it. I left the thermal variant (rank 10) at the bottom and recommended against building the main claim set around it, mirroring the inventor's own stated doubt (§6) and the absence of any data.

I did not invent a licensing, OEM-supply or consumer-retail business model beyond what §1's "sold in multipacks" already implies about the existing product category this invention competes in; where the map's ranking depends on a channel the disclosure does not confirm (standalone core sale vs OEM integration vs component licensing), I marked it as an assumption or open question rather than a stated fact.

## Assumptions

A1. A retrofit/replacement-core aftermarket channel exists for this invention, analogous to the conventional valve-core market described in §1 ("cores are sold in multipacks"). This underlies the rank-1 recommendation to claim the core independent of the stem. *Inferred from §1's description of existing industry practice, not a stated business model.* Not blocking, but ties to `01` Q33 (is the core intended to be sold alone).

A2. OEM/bulk supply to tube, tyre and wheel manufacturers is a plausible separate channel (rank 3), given the tube and tubeless use cases in §1 and §6. *Market-based inference.* Not blocking.

A3. A freestanding method-of-operation claim (rank 8) asserted against end users is commercially weak because the operating event is internal, momentary and not readily observable during ordinary use — the bench data's own reliance on an audible snap as the only indicator supports this reading but does not itself establish it as a commercial/legal conclusion. *Legal/commercial judgement, not drawn from the disclosure.* Not blocking; feeds the recommendation at rank 8, flagged to P5 for a final call.

A4. No consumable distinct from the (third-party) sealant was identified in the disclosure, so no consumable row is included in the map. Not blocking.

A5. Component-level licensing of the ring (rank 2) and the manufacturing process (rank 4) to third-party core or valve manufacturers is a plausible channel, given the specialised NiTi processing in §7. *Inferred, not stated.* Not blocking.

## Open Questions

Q1. Does the inventor intend to sell the valve core assembly as a standalone replacement product (as with conventional cores), supply or license the ring and/or manufacturing process to other core or valve manufacturers, supply complete valves to tube/tyre/wheel OEMs, or some combination? This determines which of ranks 1, 2, 3 and 4 should receive the primary independent claim and which should be secondary claim families. Related to `01` Q33. Blocks P5.

Q2. Does the inventor regard Alternative B's split sealing/purge architecture (rank 6) as commercially worth pursuing as its own product line, or only as a design-around blocker to be claimed but not built? This affects how much specification detail (P4) is worth investing in that variant beyond what closes the design-around. Blocks P4, P5.

Q3. Is there any intended consumable, kit or subscription-style product (e.g. a purge-verified sealant sold alongside the valve, or a spare-ring refill pack) that the disclosure does not mention? If none, the map's "no consumable identified" conclusion stands. Blocks P2 (confidence of this map only; not otherwise blocking).

```json
{
  "prompt": "02",
  "status": "complete",
  "assumptions": [
    {"id": "A1", "text": "A retrofit/replacement-core aftermarket channel exists, analogous to the conventional valve-core market described in §1; underlies claiming the core independent of the stem.", "blocking": false},
    {"id": "A2", "text": "OEM/bulk supply to tube, tyre and wheel manufacturers is a plausible separate channel, given the tube and tubeless use cases in §1 and §6.", "blocking": false},
    {"id": "A3", "text": "A freestanding method-of-operation claim asserted against end users is commercially weak because the event is internal, momentary and not readily observable during ordinary use.", "blocking": false},
    {"id": "A4", "text": "No consumable distinct from the third-party sealant was identified, so no consumable row is included.", "blocking": false},
    {"id": "A5", "text": "Component-level licensing of the ring and the manufacturing process to third-party manufacturers is a plausible channel, given the specialised NiTi processing in §7.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "Does the inventor intend to sell the core standalone, license the ring/process, supply OEMs, or a combination? Determines primary vs secondary claim families among ranks 1-4.", "blocks": ["P5"]},
    {"id": "Q2", "text": "Is Alternative B (split sealing/purge architecture) worth pursuing as a product line, or only as a design-around blocker? Affects specification depth for that variant.", "blocks": ["P4", "P5"]},
    {"id": "Q3", "text": "Is there any intended consumable, kit or refill product not mentioned in the disclosure?", "blocks": ["P2"]}
  ],
  "new_terms": [
    {"term": "valve core assembly", "maps_to": null, "reason": "Groups core body (20), seat ring (30), poppet (40), return spring (50) and optionally lock nut (70) as the commercially sold/replaced unit implied by §1's 'the core'; no single reference numeral covers this grouping in the disclosure."},
    {"term": "resiliently deflectable ring/element", "maps_to": "seat ring (30)", "reason": "Broader genus term needed to discuss claim scope beyond the NiTi species, given §6 Alternatives A (PEEK) and B (stainless wiper ring) show the inventor conceives non-NiTi ring materials."},
    {"term": "threshold-setting mechanism", "maps_to": "return spring (50)", "reason": "Functional genus term for whatever sets the over-travel threshold, needed because `01` Q6 leaves open whether the two-rate spring is the only means."},
    {"term": "sealing member", "maps_to": null, "reason": "Names the rigid sealing part of Alternative B's split architecture (§6) for claim-strategy discussion; the disclosure does not give it a reference numeral."},
    {"term": "wiping member", "maps_to": null, "reason": "Names the separate deflectable wiper part of Alternative B's split architecture (§6) for claim-strategy discussion; the disclosure does not give it a reference numeral."}
  ],
  "support_refs": [
    {"item": "Rank 1: valve core assembly, retrofit market", "support": "intake/disclosure.md §1 ('cores are sold in multipacks'); 01.md (d), (e)"},
    {"item": "Rank 1: quantified durability advantage (cycles to failure, inflation time, leak-down)", "support": "intake/data/bench-test.md (C-1 to C-3, P-1 to P-3); intake/disclosure.md §8"},
    {"item": "Rank 2: seat ring as narrowest novelty", "support": "01.md (b), (d) item D2-D3; intake/disclosure.md §2, §3(3)"},
    {"item": "Rank 2: clean sealing edge/poppet face vs film on ring outer surface at cycle 40", "support": "intake/data/bench-test.md; intake/disclosure.md §8"},
    {"item": "Rank 3: OEM tube/tyre/wheel integration", "support": "intake/disclosure.md §1, §6 (tubeless, lower-cost line); 01.md (k)"},
    {"item": "Rank 4: seat ring manufacturing method", "support": "intake/disclosure.md §7; 01.md (j)"},
    {"item": "Rank 5: PEEK ring genus (Alternative A)", "support": "intake/disclosure.md §6; 01.md (f) item F3"},
    {"item": "Rank 6: split sealing/purge architecture (Alternative B)", "support": "intake/disclosure.md §6; 01.md (f) item F4"},
    {"item": "Rank 7: threshold-setting mechanism, essentiality open", "support": "01.md (d) item D6, (m) Q6, Q7; intake/disclosure.md §3(5)"},
    {"item": "Rank 8: self-purging method, enforceability judgement", "support": "intake/disclosure.md §2 (operating sequence); 01.md (d) steps S1-S5; intake/data/bench-test.md (audible snap as only indicator)"},
    {"item": "Rank 9: stainless 303 body variant", "support": "intake/disclosure.md §5; 01.md (f) item F1; intake/data/bench-test.md (brass-body prototypes only)"},
    {"item": "Rank 10: thermal two-way SMA variant", "support": "intake/disclosure.md §6; 01.md (f) item F5, (m) Q21"}
  ],
  "disclosure_requests": [],
  "open_disagreements": [],
  "narrowing_suggested": []
}
```
````

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/terminology/LOCKED.md`

```markdown
# Locked terminology

Locked at Gate 1, 2026-09-30 10:10 UTC, from `04.md`. Every later drafting output must use these preferred terms verbatim or declare a new term in `new_terms`.

### Terminology Table

| Preferred term | Synonyms | Broader (genus) | Narrower (species) | Functional description | Terms to avoid | Needs definition |
|---|---|---|---|---|---|---|
| inflation valve | tyre valve | fluid valve; pressure-actuated check valve | Presta-pattern inflation valve | admits inflation gas into the inflatable chamber and retains it; receives the valve core | bicycle valve; Presta valve; tube valve | no |
| valve stem | none | valve body; valve housing | Presta-pattern valve stem of brass, 6 mm outer diameter | tubular body fixed to the inflatable chamber that receives the valve core in its stem bore | Presta stem; brass stem | no |
| stem bore | threaded stem bore | receiving bore | threaded bore of the Presta-pattern valve stem | receives and retains the core body | none | no |
| valve core | core assembly | valve mechanism | Presta-pattern valve core; replacement valve core (subject to Q10) | assembly of the core body and the parts it carries (seat ring, poppet, return spring) that opens, closes and purges the inflation valve | valve insert; removable insert; cartridge | yes |
| core body | core housing; core carrier | valve core housing; carrier | turned core body of brass CW614N; turned core body of stainless 303 | threaded into the stem bore; carries the seat ring against the internal shoulder and guides the poppet | brass core | no |
| internal shoulder | locating shoulder | axial stop; locating formation | internal shoulder of the core body against which the seat ring is pressed | locates the seat ring axially in the core body | none | no |
| core body bore | core bore | receiving bore | bore of the core body at the seat ring | receives the seat ring; bounds the purge gap on its outer side according to §3(6) (subject to Q1) | none | no |
| seat ring | valve seat ring; sinuous ring; superelastic seat | deflectable ring element; valve seat member | superelastic NiTi seat ring with convoluted wall; PEEK seat ring (Alternative A) | annular element whose sealing edge seats the poppet in the closed state, which the purge shoulder deflects radially during over-travel to open the purge gap, and which undergoes shape recovery when the pressure differential falls | NiTi ring; nitinol seat; shape-memory seat; grommet; O-ring; gasket; washer | yes |
| deflectable ring element | resilient ring element | resilient member; annular element | seat ring; wiper ring (Alternative B) | any annular element that the purge shoulder deflects radially during over-travel so as to open a purge flow path, and that recovers when the pressure differential falls | ring spring; snap ring | yes |
| convoluted wall | sinuous wall; wavy wall; wave profile | compliant wall profile; axial-to-radial conversion geometry | wall with one convolution; wall with two convolutions | wall profile of the seat ring that converts axial load on the sealing edge into radial deflection | bellows; corrugated tube; pleated wall | yes |
| sealing edge | seat edge | seat surface | sealing edge of the convoluted seat ring | edge of the seat ring on which the sealing face rests in the closed state | upper edge; seat lip | no |
| poppet | moving valve member | movable closure member | brass poppet with conical sealing face and purge shoulder | moves with the pressure differential between the closed state, the normal-open state and the purge state, carrying the sealing face and the purge shoulder | plunger; valve pin; needle | no |
| poppet stem | poppet shank | valve-member shank | none disclosed | elongate part of the poppet along which sealant is drawn by capillary action (§1) | valve pin | no |
| sealing face | poppet face (subject to Q5); conical face | sealing surface | conical sealing face of brass; hard-anodised aluminium sealing face | surface of the poppet that rests on the sealing edge in the closed state | valve cone | no |
| purge shoulder | actuating shoulder; purge collar | deflecting formation; actuating surface | shoulder on the poppet on the chamber side of the sealing face | contacts the seat ring only during over-travel and deflects it radially to open the purge gap | cam; wedge | yes |
| return spring | valve spring; poppet spring | biasing member; resilient return element | two-rate compression spring; compression spring of stainless music wire | biases the poppet towards the closed state; through its two stages sets the crack pressure and the over-travel threshold | coil spring; two-rate spring | no |
| first spring stage | soft stage; first stage | first biasing stage | first stage of the prototype return spring | lower-rate stage resisting the normal stroke; sets the crack pressure | soft spring | no |
| second spring stage | stiff stage; second stage | threshold-setting arrangement; over-travel resistance | second stage of the prototype return spring | higher-rate stage that the pressure differential must overcome to produce over-travel; sets the over-travel threshold | stiff spring | yes |
| purge gap | secondary annular gap; annular clearance; purge clearance | purge passage; secondary flow passage | annular radial clearance between the seat ring outer surface and the core body bore (§3(6); location subject to Q1) | clearance closed in the closed state and the normal-open state, opened by radial deflection of the seat ring in the purge state, through which the air purge flows | bypass; vent; leak path | yes |
| purge flow path | secondary flow path | flow path | path from the supply side through the purge gap into the inflatable chamber (FIG-2, per drawings README) | carries inflation gas across the surfaces on which sealant film accumulates during the purge state | bypass channel | yes |
| main passage | main flow path | flow path | passage past the sealing face | carries inflation gas into the inflatable chamber in the normal-open state and the purge state | none | no |
| lock nut | locking nut; valve nut | manual closing member | conventional Presta-pattern lock nut | holds the poppet in the closed state manually for storage and transport | none | no |
| supply side | pump side; outer side; inlet side | upstream side | side coupled to the inflation device | side of the poppet exposed to inflation-device pressure | upper side | yes |
| chamber side | tube side; inner side | downstream side | side open to an inner tube or a tubeless tyre | side of the poppet exposed to the pressure of the inflatable chamber | lower side; underside | yes |
| inflatable chamber | tyre cavity; tube interior | pressurised volume | bicycle inner tube; tubeless bicycle tyre set-up | volume inflated through the inflation valve and holding liquid sealant | none | yes |
| inflation device | inflator; pumping device | pressure source | floor pump with pump head; CO2 cartridge inflator | source of inflation gas coupled to the supply side | none | no |
| pressure differential | differential pressure; pressure difference | pressure condition | supply-side pressure minus chamber-side pressure (inferred; 01 A3) | quantity whose value determines the state of the poppet | pump pressure | yes |
| crack pressure | cracking pressure; opening pressure | opening threshold | 1.0 bar (prototype); 0.8–1.5 bar (inventor's believed range) | pressure differential at which the poppet begins its normal stroke | none | yes |
| over-travel threshold | over-travel pressure; purge threshold; second-stage pressure | actuation threshold | 3.5 bar (prototype); 2.5–5.0 bar (inventor's believed range) | pressure differential above which the poppet moves beyond the normal stroke into over-travel | floor-pump pressure | yes |
| normal stroke | normal poppet stroke; opening stroke | opening displacement | 0.6 mm (prototype) | displacement of the poppet from the closed state over which the purge shoulder does not contact the seat ring | full stroke | yes |
| over-travel | overtravel; over-stroke; extended stroke | further displacement of the valve member | over-travel beyond the normal stroke against the second spring stage | movement of the poppet beyond the normal stroke when the pressure differential exceeds the over-travel threshold, bringing the purge shoulder against the seat ring | overshoot | yes |
| over-travel distance | over-travel length | displacement | 0.5 mm (prototype); 0.4–0.9 mm (inventor's believed range) | axial distance the poppet moves beyond the end of the normal stroke | none | yes |
| radial deflection | radial expansion; radial flexing | elastic deformation | radially outward deflection of the convoluted wall (§2; direction subject to Q1) | deformation of the seat ring produced by the purge shoulder that opens the purge gap | buckling; collapse | yes |
| purge gap opening | purge gap width | clearance dimension | 0.15 mm radial (prototype); 0.10–0.25 mm (inventor's believed range) | radial size of the purge gap when fully open | none | yes |
| shape recovery | spring-back; return to shape | elastic return | superelastic recovery of the NiTi seat ring; slower recovery of the PEEK seat ring | return of the seat ring to its at-rest shape when the pressure differential falls, closing the purge gap | memory effect; creep recovery | no |
| cleaning action | purging action | deposit removal | air purge; snap-back wipe | action by which the valve removes sealant film from its sealing surfaces without a tool or user action | self-cleaning; anti-clogging; clog-proof | no |
| air purge | blow-through | gas purge | flow of air at inflation-device pressure through the purge gap | flow of inflation gas along the purge flow path that carries sealant film into the inflatable chamber | air blast | yes |
| snap-back wipe | wiping action; recovery snap | recovery wipe; mechanical wipe | wipe produced by superelastic shape recovery of the seat ring across the poppet face | movement of the recovering seat ring across the poppet that shears off partially cured sealant film | scraping; snap-through; snap-action | yes |
| sealant film | cured latex; sealant deposit | deposit; fouling | partially cured latex deposit; cured latex deposit | layer of liquid sealant dried or cured on valve surfaces that causes leakage or blockage | latex film; crust | yes |
| liquid sealant | tyre sealant; sealant fluid | sealing fluid | latex emulsion with ammonia and suspended particles; ammonia-free sealant (untested) | fluid carried in the inflatable chamber that is drawn into the valve on inflation | latex sealant | yes |
| blockage | clogging | valve failure | failure of the inflation device to open the valve within 5 s of engagement (§8 criterion) | failure mode in which sealant film prevents the poppet from opening | none | yes |
| inflation event | inflation session | pressurisation | inflation from fully deflated to 6 bar with a floor pump (§8) | period from coupling the inflation device to the supply side until its removal | pump stroke | yes |
| deflation | letting down | depressurisation | full deflation through the valve (§8 test protocol) | release of gas from the inflatable chamber through the inflation valve | none | no |
| closed state | closed position | valve state | closed state held by the lock nut | sealing face on the sealing edge; purge gap closed | none | yes |
| normal-open state | open position | valve state | none disclosed | poppet displaced within the normal stroke; flow through the main passage; purge gap closed | none | no |
| purge state | purge position | valve state | none disclosed | poppet in over-travel; seat ring in radial deflection; purge gap open | none | yes |
| superelastic alloy | pseudoelastic alloy; superelastic metal | shape-memory alloy; resilient metal | NiTi, nominally 55.8 wt% Ni, from drawn tube | alloy that recovers large strains on unloading at service temperature by a reversible phase transformation | nitinol; memory metal | yes |
| austenite finish temperature | Af; Af temperature | transformation temperature | below 5 °C (seat ring, specified); about 35–40 °C (thermal variant) | temperature above which the alloy is fully austenitic and behaves superelastically | transition temperature | yes |
| martensite start temperature | Ms | transformation temperature | none disclosed | temperature on cooling below which martensite forms and shape recovery may be lost (§9) | transition temperature | yes |
| nickel content | Ni content; nickel fraction | alloy composition | nominally 55.8 wt% Ni | composition of the NiTi seat ring | none | no |
| seat ring inner diameter | ring bore; ring ID | ring dimension | 2.3 mm (prototype); 2.0–2.6 mm (inventor's believed range) | inner diameter of the seat ring | none | no |
| seat ring outer diameter | ring OD | ring dimension | 2.7 mm (inferred from tube stock; 01 A2) | outer diameter of the seat ring | none | no |
| seat ring wall thickness | wall gauge | ring dimension | 0.20 mm (prototype); 0.15–0.30 mm (inventor's believed range) | thickness of the convoluted wall | none | yes |
| seat ring free length | unloaded length | ring dimension | 3.0 mm (prototype); 2.5–4.0 mm (inventor's believed range) | axial length of the seat ring unloaded | none | yes |
| convolution amplitude | wave amplitude; wave height | ring dimension | 0.12 mm (prototype); 0.08–0.20 mm (inventor's believed range) | radial excursion of the convoluted wall | none | yes |
| number of convolutions | convolution count | ring geometry | one convolution; two convolutions | count of convolutions in the convoluted wall | none | no |
| interference fit | press fit | ring retention | interference of approximately 0.03 mm on diameter | retains the seat ring in the core body against the internal shoulder | none | no |
| laser cutting | laser profiling | profile cutting | laser cutting of NiTi tube (2.7 mm OD, 0.20 mm wall) on a mandrel | forms the seat ring profile from tube stock | none | no |
| shape-setting | shape-set; heat-setting | thermomechanical treatment | 500 °C for 10 min in a fixture holding the wave geometry, then water quench | fixes the convoluted wall geometry of the seat ring | annealing | no |
| electropolishing | electropolish | surface finishing | electropolishing to remove oxide and the heat-affected edge | finishes the seat ring surface | none | no |
| wiper ring | none | deflectable ring element | thin stainless spring wiper ring (Alternative B) | separate ring on the chamber side of the fixed seat that the purge shoulder deflects outward, separating purge and wipe from sealing | scraper ring | yes |
| fixed seat | rigid seat | valve seat member | brass fixed seat (Alternative B) | non-deflecting seat that performs sealing when sealing is separated from purge and wipe | brass seat | no |
| thermally actuated purge | manual purge; hand-warming purge | non-pressure-actuated purge | two-way shape-memory NiTi ring with an austenite finish temperature of about 35–40 °C, warmed by hand | opening of the purge gap by warming the ring instead of by over-travel | heat-activated valve | yes |
| inflation cycle | sealant-loaded cycle; test cycle | service cycle | inflate to 6 bar, hold 24 h at 22 °C, deflate fully (§8) | one repetition of inflation, hold and deflation | none | yes |
| leak-down | pressure loss; leak rate | leakage | more than 0.5 bar in 24 h (failure criterion); 0.1–0.2 bar in 24 h at cycle 40 (prototypes) | loss of chamber pressure through the valve over a hold period | slow leak | yes |
| inflation time | fill time | inflation performance measure | time from coupling the inflation device to reaching 6 bar (bench data) | measure of how freely the valve opens | none | yes |
| conventional valve core | standard Presta core; conventional core | reference valve core | commercial Presta core used as comparator (§8) | comparator in the bench test | none | yes |

This table is a drafting and analysis aid prepared by AI, not legal advice; qualified patent counsel signs off before anything is filed.

#### Reasons for the terms to avoid

- `bicycle valve`, `Presta valve`, `tube valve`, `Presta stem`: tie the invention to one vehicle, one valve standard or inner tubes only. Tubeless use is disclosed (§1); other valve types are open (01 Q26).
- `brass stem`, `brass core`, `brass seat`: material limitations. Stainless 303 is disclosed for the core body (§5).
- `valve insert`, `removable insert`: the removable insert is one of the existing remedies the inventor distinguishes (§1). `cartridge` collides with the CO2 cartridge inflator (§9).
- `NiTi ring`, `nitinol seat`, `nitinol`, `memory metal`: material-limit the seat ring although Alternative A (PEEK) is disclosed (§6); the last two are informal and imprecise.
- `shape-memory seat`, `memory effect`: imply thermally triggered shape memory. The seat ring works by superelastic recovery (§2, §4); the thermal route is a separate variant (§6).
- `grommet`, `O-ring`, `gasket`, `washer`: imply an elastomeric or flat sealing element, which is what the seat ring replaces (§2).
- `ring spring`, `snap ring`: names of known standard parts (friction ring spring, circlip) that would import their structure.
- `bellows`, `corrugated tube`, `pleated wall`: imply many convolutions and axial compliance; the disclosure has one or two convolutions that convert axial load into radial deflection (§3(3)).
- `upper edge`, `upper side`, `lower side`, `underside`: depend on orientation, which changes as the wheel turns and is not confirmed (01 Q3).
- `seat lip`: implies an elastomeric lip seal.
- `plunger`, `valve pin`, `needle`: imply a solid pin or needle-valve closure member.
- `valve cone`: fixes the geometry of the sealing face.
- `cam`, `wedge`: fix the profile of the purge shoulder (01 Q8).
- `coil spring`: fixes spring form. `two-rate spring` as a component name ties the over-travel threshold to the spring; whether other means can set it is open (01 Q6).
- `soft spring`, `stiff spring`: relative terms, and imply two separate springs.
- `bypass`, `bypass channel`: evoke the known bypass-valve category. `vent`: implies discharge to atmosphere; the purge flows into the inflatable chamber. `leak path`: implies a defect.
- `pump pressure`, `floor-pump pressure`: ambiguous between absolute and differential pressure, and tie the threshold to one pump type (01 Q5).
- `full stroke`: implies the end of poppet travel, which conflicts with over-travel beyond it.
- `overshoot`: implies an uncontrolled transient; over-travel is a pressure-set displacement (subject to 01 Q4).
- `buckling`, `collapse`: imply instability or failure; the radial deflection is elastic and recovered.
- `creep recovery`: §2 contrasts superelastic recovery with elastomer creep.
- `self-cleaning`, `anti-clogging`, `clog-proof`: overstate the effect. Film remained on the ring outer surface after 40 cycles (§8); a promissory result invites a clarity or utility objection.
- `air blast`: implies a discrete high-velocity event.
- `scraping`: implies a rigid scraper. `snap-through`, `snap-action`: denote bistable mechanisms the disclosure does not describe.
- `latex film`, `latex sealant`, `crust`: limit to latex chemistry, although ammonia-free sealants are in issue (§9); `crust` is informal.
- `pump stroke`: a different unit from the inflation event (01 A8).
- `transition temperature`: ambiguous (for PEEK it suggests glass transition); name the specific transformation temperature.
- `annealing`: a different heat treatment from shape-setting.
- `heat-activated valve`: evokes thermal valves generally.
- `scraper ring`: implies a rigid scraper; Alternative B describes a spring wiper deflected outward (§6).
- `slow leak`: informal; use leak-down with a stated threshold.

#### Terms that need an express definition in the specification

- **valve core**: which parts it comprises and whether it is claimed alone as a replacement part (Q10).
- **seat ring** and **deflectable ring element**: the functional definition (seats, deflects radially during over-travel, recovers), so that material and wall form are not implied; and whether the genus covers the Alternative B wiper ring (Q11).
- **convoluted wall**, **convolution amplitude**, **seat ring wall thickness**, **seat ring free length**: how each is measured (Q2, Q3).
- **purge gap**, **purge flow path**, **radial deflection**, **purge gap opening**: which surfaces bound the gap, the direction of deflection and how the opening is measured. Cannot be finalised until 01 Q1–Q2 are answered (Q1, Q4).
- **purge shoulder**: defined by its function, contact with the seat ring only during over-travel (§3(4)).
- **supply side**, **chamber side**: replace orientation words (Q13; 01 Q3).
- **pressure differential**, **crack pressure**, **over-travel threshold**: how the differential is taken and whether static or transient (Q13; 01 Q4).
- **normal stroke**, **over-travel**, **over-travel distance**: where the normal stroke ends and over-travel begins (Q6).
- **second spring stage**: defined by function (sets the over-travel threshold) so that the threshold is not tied to one spring construction (01 Q6).
- **air purge**: whether "air" means any inflation gas (Q8).
- **snap-back wipe**: which surface moves across which (Q5; 01 Q10).
- **sealant film**, **liquid sealant**: not limited to latex; cured and partially cured states.
- **inflatable chamber**: covers inner tubes and tubeless set-ups (Q9).
- **superelastic alloy**, **austenite finish temperature**, **martensite start temperature**: the property and measurement method (Q7).
- **closed state**, **purge state**: whether the closed purge gap must itself be airtight (01 Q31).
- **thermally actuated purge**, **wiper ring**: only if the inventor keeps these alternatives (01 Q20, Q21).
- **blockage**, **leak-down**, **inflation time**, **inflation cycle**, **inflation event**, **conventional valve core**: the test definitions for the worked example (§8, bench data).

#### Drafting notes on the table

- Bare words that collide with locked terms are not locked on their own and must not be used as component names: "tube" (inner tube, NiTi tube stock, tubeless), "stem" (valve stem, poppet stem), "seat" (seat ring, fixed seat), "spring", "shoulder", "core", "film". Always use the full preferred term.
- The core body bore and the stem bore are different features. The "valve core bore" of §1 is not mapped to either until 01 Q1 is answered.
- The inventor's relative words "thin", "light", "shallow", "fast", "stiff" and "slow" (§2, §3, §6) should be replaced in claims by the §4 values or by a relation between parts. Under EPO practice such relative terms draw clarity objections; in the US and UK they need an objective standard in the description.
- Several genus terms (deflectable ring element, biasing member, threshold-setting arrangement) pair a generic noun with a function. In the US that pattern can be read as means-plus-function under 35 U.S.C. §112(f) and limited to the disclosed structures and their equivalents. The Description should therefore describe each corresponding structure. EPO and UK practice does not apply this construction.
- Reference numerals follow §3: valve stem (10), core body (20), seat ring (30), poppet (40), sealing face (42), purge shoulder (44), return spring (50), purge gap (60), lock nut (70).
```

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/22.md`

````markdown
## Deliverable

### Independent Claims

This is a drafting and analysis aid prepared by AI. It is not legal advice and says nothing about validity; qualified patent counsel signs off before anything is filed.

One independent claim per justified family of `21` (A valve core, C inflation valve, B seat ring, D method of use, E method of manufacture). The description does not yet exist: every limitation is supported by the inventor's disclosure (§1–§9 via `01`, `03`), by `CONFIRMED.md` and by the blueprint section ids of `16`; paragraph anchors are mapped in P5d. Dependent ladders follow in Prompt 23; Prompt 25 fixes the final numbering. Reference signs are those of the disclosure (§3): core body (20), seat ring (30), poppet (40), sealing face (42), purge shoulder (44), return spring (50), purge gap (60), valve stem (10). No independent claim recites a material, a number other than in claim 3, liquid sealant, a tubeless tyre, the snap-back wipe, the convoluted wall (except claim 3), the purge shoulder, or the second spring stage.

1. A valve core for an inflation valve, the valve core comprising:
a core body (20);
a deflectable ring element (30) carried by the core body;
a poppet (40) guided by the core body and having a supply side, a chamber side, a sealing face (42) and a deflecting formation (44), the poppet being movable in response to a pressure differential between the supply side and the chamber side;
a main passage past the sealing face, the main passage being closed by the sealing face in a closed state of the valve core; and
a return spring (50) biasing the poppet towards the closed state;
wherein the poppet is movable from the closed state, at a pressure differential at or above a crack pressure, through a normal stroke into a normal-open state in which the main passage is open, the deflecting formation being spaced from the deflectable ring element throughout the normal stroke;
wherein the poppet is movable into over-travel beyond the normal stroke when the pressure differential exceeds an over-travel threshold higher than the crack pressure, the deflecting formation bearing on the deflectable ring element in the over-travel and producing radial deflection of the deflectable ring element; and
wherein a purge gap (60), bounded at least in part by a surface of the deflectable ring element, is closed in the closed state and in the normal-open state and is opened by the radial deflection in a purge state of the valve core so as to open a purge flow path, separate from the main passage, from the supply side to the chamber side, the deflectable ring element undergoing shape recovery to close the purge gap when the pressure differential falls.

2. An inflation valve for an inflatable chamber, the inflation valve comprising:
a valve stem (10) having a stem bore; and
carried by the valve stem, a deflectable ring element (30), a poppet (40) and a return spring (50),
the poppet having a supply side, a chamber side, a sealing face (42) and a deflecting formation (44), the poppet being movable in response to a pressure differential between the supply side and the chamber side,
a main passage past the sealing face being closed by the sealing face in a closed state of the inflation valve, and the return spring biasing the poppet towards the closed state;
wherein the poppet is movable from the closed state, at a pressure differential at or above a crack pressure, through a normal stroke into a normal-open state in which the main passage is open, the deflecting formation being spaced from the deflectable ring element throughout the normal stroke;
wherein the poppet is movable into over-travel beyond the normal stroke when the pressure differential exceeds an over-travel threshold higher than the crack pressure, the deflecting formation bearing on the deflectable ring element in the over-travel and producing radial deflection of the deflectable ring element; and
wherein a purge gap (60), bounded at least in part by a surface of the deflectable ring element, is closed in the closed state and in the normal-open state and is opened by the radial deflection in a purge state of the inflation valve so as to open a purge flow path, separate from the main passage, from the supply side to the chamber side, the deflectable ring element undergoing shape recovery to close the purge gap when the pressure differential falls.

3. A seat ring (30) for a valve core of an inflation valve, the seat ring being an annular element having a wall extending between a first axial end and a second axial end, the first axial end forming a sealing edge on which a sealing face of a poppet is seatable, the wall comprising a convoluted wall having at least one convolution, the convoluted wall being arranged such that an axial load applied to the seat ring produces radial deflection of the convoluted wall and such that the convoluted wall recovers elastically on removal of the axial load, the seat ring having a seat ring inner diameter of from 2.0 mm to 2.6 mm and a seat ring wall thickness of from 0.15 mm to 0.30 mm.

4. A method of inflating an inflatable chamber that holds liquid sealant through an inflation valve, the inflation valve comprising a deflectable ring element, a poppet having a supply side, a chamber side, a sealing face and a deflecting formation, a main passage past the sealing face, and a return spring biasing the poppet towards a closed state in which the main passage is closed by the sealing face, the method comprising:
coupling an inflation device to the supply side;
raising a pressure differential between the supply side and the chamber side to at or above a crack pressure so that the poppet moves through a normal stroke into a normal-open state in which inflation gas flows through the main passage into the inflatable chamber, the deflecting formation remaining spaced from the deflectable ring element throughout the normal stroke;
raising the pressure differential above an over-travel threshold higher than the crack pressure so that the poppet moves into over-travel beyond the normal stroke, the deflecting formation bears on the deflectable ring element and produces radial deflection of the deflectable ring element, and the radial deflection opens a purge gap, bounded at least in part by a surface of the deflectable ring element and closed in the closed state and in the normal-open state, so that inflation gas flows as an air purge along a purge flow path, separate from the main passage, through the purge gap into the inflatable chamber; and
removing the inflation device from the supply side so that the pressure differential falls and the deflectable ring element undergoes shape recovery to close the purge gap.

5. A method of manufacturing a seat ring (30) for a valve core of an inflation valve, the method comprising:
providing tube stock of a superelastic alloy;
laser cutting the tube stock to form a seat ring blank having a first axial end forming a sealing edge and a second axial end;
forming, in a wall of the seat ring blank between the first axial end and the second axial end, a convoluted wall having at least one convolution; and
shape-setting the seat ring by heating the seat ring blank in a fixture holding the geometry of the convoluted wall and then quenching, so that the convoluted wall is arranged such that an axial load applied to the seat ring produces radial deflection of the convoluted wall and the convoluted wall recovers elastically on removal of the axial load.

### Limitation Table

Support is cited to the disclosure (§), the Phase 1 outputs, `CONFIRMED.md` (11, 12, 13, 14) and the `16` blueprint section ids; paragraph anchors are mapped in P5d. Vulnerability cites the `09` row or the `07` chart. "Charted art" means the 17 references of `07`.

| Claim | Limitation (quoted) | Reason included | Specification support | Prior-art vulnerability | Design-around route |
|---|---|---|---|---|---|
| 1 | "A valve core for an inflation valve" | Names the sellable unit (02 rank 1) without the valve stem; preamble only | §3 via 01 (d); 19 "valve core"; 16 S8.2 | None; F0 is explicit in ref-02, US4462449A, EP1137892A1 (07 grid) | Mechanism carried by the valve stem with no core body (d2 R6): met by claim 2 |
| 1 | "a core body (20)" | The carrier of the ring element and guide of the poppet; the part threaded into the stem bore in the replacement product | §3(2); 03 C26; 16 S8.3 | None; ref-02 claim 1 "a body" (07 ref-02 N0a) | As above (R6); polymer core body is a dependent (S11.7) |
| 1 | "a deflectable ring element (30) carried by the core body" | The genus of seat ring and wiper ring (LOCKED); "carried by" covers direct and indirect carriage and, on the 19 construction paragraph, an integral flexure (12 E4.5; 11 DA-5). Needed: the element that is deflected and recovers is what distinguishes EP1137892A1's bodily moving ring (07 EP1137892A1 N0d) | §2, §3(3), §6; 03 C5; 19 "deflectable ring element"; 16 S7.4, S8.4, S10.6 | 09 row 6: a resilient seat ring per se is ref-02 claim 1 (07 N2 E); US4462449A's elastomeric member (07 N0c ?). Carried by the genus, not by this limitation alone | Ring element on the poppet, formation on the core body (11 DA-8; d2 R16): not covered; Prompt 24 tests a carrier-neutral formulation. Port purge with nothing deflecting (DA-7, R2): cannot be closed without new matter |
| 1 | "a poppet (40) guided by the core body and having a supply side, a chamber side, a sealing face (42) and a deflecting formation (44), the poppet being movable in response to a pressure differential between the supply side and the chamber side" | The moving member and its two functional surfaces; "deflecting formation" (genus of purge shoulder) so that a sealing face, taper, collar or lugs are covered (11 DA-4; 12 §3). Pressure actuation distinguishes hand-operated valves (07 US11904644B2 N0a ?, US11345196B2 N0a ?) | §3(4), §2; 01 A3 (differential); 03 C1, C4; 19 "purge shoulder", "supply side", "chamber side", "pressure differential"; 16 S7.2, S7.3, S7.6, S8.5, S11.3 | 09 row 1: ref-02 claim 4 (poppet deflects the lip "during opening"); US4462449A claim 1 (07 N0c ?). Met by the normal-stroke clause below, not here | Over-travel by a depressor head or by hand (12 E1.4, E1.5; d2 R5): "movable in response to a pressure differential" is satisfied by any pressure-opened valve; the threshold clause is the exposure, see below |
| 1 | "a main passage past the sealing face, the main passage being closed by the sealing face in a closed state of the valve core" | Defines the closed state and gives the antecedent for "separate from the main passage" (08 item 1(iii)); avoids naming the seat so that the fixed seat of Alternative B is covered | §3(4), §3(6); 01 (i); 03 C1, C10; 19 "closed state"; 16 S8.5, S9.1 | None; conventional (07 all N0a E) | None; every valve has it |
| 1 | "a return spring (50) biasing the poppet towards the closed state" | Conventional; gives the structural basis of the crack pressure and the antecedent for the spring-stage dependents. Not needed to distinguish; costs no scope because every product has one | §3(5); 03 C1, C17; 19 "second spring stage"; 16 S8.6 | None (07 ref-02, US4462449A claim 4, EP1137892A1 claim 28) | None |
| 1 | "the poppet is movable from the closed state, at a pressure differential at or above a crack pressure, through a normal stroke into a normal-open state in which the main passage is open, the deflecting formation being spaced from the deflectable ring element throughout the normal stroke" | 08 item 1(i): a normal-open state with main-passage flow and no contact between the formation and the ring element is what ref-02 claim 4 and US4462449A claim 1 lack. Positive "spaced from" wording, not a negative limitation (lessons L1; 09 row 1 note (c)) | §2 ("normal stroke"), §3(4) ("only contacts the ring during over-travel"), §4 (0.6 mm); 01 (i); 03 C1, C4, C18; 19 "normal stroke", "crack pressure"; 16 S7.3, S8.5, S9.2 | 09 row 1: ref-02 claim 4 deflects on every opening (07 N0c ?); US4462449A claim 1 contacts only after initial travel but has no main-passage flow before contact (07 N0b A, N0d A). Distinguished as drafted | Purge on every opening with no normal stroke (11 DA-1; d2 R4): escapes claim 1; whether it works is unanswered (03 Q3) and it reads on ref-02. Undetectable by teardown; the method claim and a second-spring-stage dependent give provable structure |
| 1 | "the poppet is movable into over-travel beyond the normal stroke when the pressure differential exceeds an over-travel threshold higher than the crack pressure, the deflecting formation bearing on the deflectable ring element in the over-travel and producing radial deflection of the deflectable ring element" | 08 item 1(ii): the second poppet range, above a higher threshold, is absent from every reference (07 grid N0b). Stated as a relationship, not as a spring, so the threshold-setting arrangement is a dependent genus (09 row 1 note (b); 02 rank 7). "Radial deflection" is direction-neutral (LOCKED; 19) | §2 ("above a threshold"), §3(4), §3(5), §4 (3.5 bar); 03 C2, C3, C13, C18; 19 "over-travel", "over-travel threshold", "radial deflection"; 16 S7.3, S9.3, S9.4, S11.4 | 09 row 1: EP1137892A1 claims 1(e), 8 (threshold on chamber-side pressure, separate member, flow out of the tyre; 07 N0b ?); US4408632A claim 7 (07 N0b ?). None has over-travel of the inflation poppet | Threshold set by the ring's own stiffness with a single-rate spring (12 E2.3): still within the claim (the relationship holds). Mechanical over-travel by a head or by hand (R5): the claim requires over-travel "when the pressure differential exceeds" the threshold; a core with no pressure threshold escapes. Closable only if the inventor confirms mechanical actuation (11 Q9); recorded in disclosure_requests. US §112(f) risk for the functional relationship: the description must give more than one threshold-setting structure (S11.4) |
| 1 | "a purge gap (60), bounded at least in part by a surface of the deflectable ring element, is closed in the closed state and in the normal-open state and is opened by the radial deflection in a purge state of the valve core so as to open a purge flow path, separate from the main passage, from the supply side to the chamber side" | 08 item 1(iii): a separate path, closed in both lower states, is what ref-02 [0019] (enlargement of the main passage) and EP1137892A1 claim 8 lack. Defined by function and state, not by bounding surfaces or direction (11 DA-2, DA-3, finding 2; d2 R1). "To the chamber side" avoids reciting the inflatable chamber | §2, §3(6); drawings README FIG-2 via 01 (b)5; 03 C6, C7; 19 "purge gap", "purge flow path", "purge state"; 16 S7.5, S8.7, S9.4, S9.5, S11.1, S11.2 | 09 row 2: ref-02 [0019] (07 N0d ?); EP1137892A1 claim 8 (07 N0d ?); US11065925B2 permanently open hole (07 N0d A); ref-01 [0022] main-passage flow (07 N0d ?). **Support is conditional**: location and opening against the interference fit are unresolved (01 Q1, Q2); an insufficiency attack on this element is the strongest attack in the file (08 item 3; d2 R1) | Wipe only, periphery sealed (11 DA-10; d2 R7): escapes; closable only if the inventor confirms the wipe alone suffices (03 Q1). Port purge (DA-7, R2): escapes; new matter. Any purge gap location is covered by the functional wording |
| 1 | "the deflectable ring element undergoing shape recovery to close the purge gap when the pressure differential falls" | Makes the three-state cycle repeatable and explicit; every viable product re-closes, so it gives away no scope. Kept short; the snap-back wipe is not recited (09 row 3 (a); 03 A2) | §2; 03 C8; bench data (snap on removal; leak-down at cycle 40); 19 "deflectable ring element", "purge state"; 16 S9.6, S10.7 | Not a distinction on its own: ref-02 [0020] (07 N0e E); US4462449A (07 N0e I) | Positively driven recovery by a second formation on the poppet (12 E9.4) is still "shape recovery" on the 19 construction if the ring returns to its at-rest form; the description should say so (S10.7) |
| 2 | "An inflation valve for an inflatable chamber ... a valve stem (10) having a stem bore" | The OEM unit (02 rank 3); the valve stem as the carrier defeats the mechanism-in-the-stem route (d2 R6) | §3(1); 19 "valve stem", "stem bore"; 16 S8.1, S11.9 | None; F0 explicit (07 grid) | None within the inflation valve; a competitor selling only a core is met by claim 1 |
| 2 | "carried by the valve stem, a deflectable ring element (30), a poppet (40) and a return spring (50)" | "Carried by" covers indirect carriage by a removable core body in the stem bore and direct carriage in a non-removable inflation valve (12 E16.3, E14.6; 19 coupling paragraph) | CONFIRMED 12 E16.3, E14.6; 11 DA-6; 16 S11.9, S7.1 | As claim 1 | Direct-carriage limb is an unattended-gate candidate (11 Q6); if the inventor did not conceive it, claim 2 must recite "a core body received in the stem bore" and R6 stays open |
| 2 | Remaining clauses (poppet surfaces, main passage, return spring, normal stroke, over-travel, purge gap, shape recovery) | Identical to claim 1, with "inflation valve" in place of "valve core" | As claim 1 | As claim 1 | As claim 1 |
| 3 | "A seat ring (30) for a valve core of an inflation valve" | Component family (02 rank 2); preamble read as "suitable for" (EPO) or intended use (US), so it does not limit | §3(3); 19 "seat ring"; 16 S11.10, S17 CF-B | None | None; the limitations below must carry the claim |
| 3 | "an annular element having a wall extending between a first axial end and a second axial end, the first axial end forming a sealing edge on which a sealing face of a poppet is seatable" | The valve-seat function is what a static sealing ring lacks (07 US9982818B2 N2 A; US6393765B1 N2 ?). "Seatable" keeps the poppet out of the claim | §3(3), §3(4); 03 C10; 19 "sealing edge"; 16 S8.4, S10.2 | 09 row 6: ref-02 claim 1 has a ring that is the seat, but of elastomer with no convoluted wall (07 N3 A) | A sealing edge at neither axial end (mid-wall seat): not covered; not disclosed |
| 3 | "the wall comprising a convoluted wall having at least one convolution, the convoluted wall being arranged such that an axial load applied to the seat ring produces radial deflection of the convoluted wall and such that the convoluted wall recovers elastically on removal of the axial load" | 09 row 5: axial-to-radial conversion at service temperature distinguishes US9982818B2's thermally driven radial movement (07 N3 ?). "At least one" covers one, two or more (12 E5.2; 11 DA-18); "elastically" is material-neutral so the PEEK species (§6 Alternative A) is covered | §3(3) ("translates into radial expansion"), §6 ("same convoluted wall"); 03 C12, C13; 19 "convoluted wall"; 16 S10.2, S7.4 | 09 row 5; 08 N3 increment rated *moderate*: ref-02 [0024] + US9982818B2 (07 N3 ?, N4 E). The extract gives no dimensions, so the dimensional limitations below matter (07 Q3) | Straight wall driven by a tapered formation (12 E3.2, E5.5; d2 R9), slotted collet (E4.3; R8), conical disc (E4.4): escape claim 3 but stay within claim 1. Claim 3 cannot be widened to "axial-to-radial conversion geometry" without losing the distinction over US9982818B2; accepted |
| 3 | "a seat ring inner diameter of from 2.0 mm to 2.6 mm and a seat ring wall thickness of from 0.15 mm to 0.30 mm" | Only these two ranges are needed to place the ring in a valve core of this size and out of an aerospace flow-meter seal (08 rank-2 row: *moderate* with dimensions). Free length, convolution amplitude and material are left to dependents | §4 (believed ranges), §7 (2.3 mm, 0.20 mm prototype); 03 C21; 13 Table 1; 19 "seat ring wall thickness"; 16 S7.10, S10.4 | 08 N6: ranges are inventor belief, no criticality evidenced (08 A6); US9982818B2 dimensions unknown (07 Q3) | Outside the range by tolerance (d2 R11): escapes claim 3 only; claim 1 has no numbers. Measurement conventions must be in the description (S7.10; 19 A5) |
| 4 | "A method of inflating an inflatable chamber that holds liquid sealant through an inflation valve, the inflation valve comprising [the claim 1 parts]" | The sealant context, omitted from claims 1–3, is placed here where it is the use (d2 R19); the parts are recited so the claim is self-contained in the US | §1, §2; 03 C31; 19 "inflatable chamber", "liquid sealant"; 16 S9.1, S16 | F1 explicit in US11904644B2, US11345196B2, US11065925B2, ref-01 (07 grid) | A seller who labels "tubes only" is outside direct infringement; inducement needs instructions for sealant use |
| 4 | "coupling an inflation device to the supply side" | The start of the inflation event (LOCKED) | §2, §8; 01 (d) S1; 19 "inflation event"; 16 S9.9 | None | None |
| 4 | "raising a pressure differential ... to at or above a crack pressure so that the poppet moves through a normal stroke into a normal-open state in which inflation gas flows through the main passage into the inflatable chamber, the deflecting formation remaining spaced from the deflectable ring element throughout the normal stroke" | Claim 1's first range as a step; "inflation gas" so that CO2 inflation devices are covered (12 E8.5; 16 S7.8) | §2, §4; 01 (d) S2, (i); 16 S9.2 | As claim 1 (09 row 1) | As claim 1 (R4) |
| 4 | "raising the pressure differential above an over-travel threshold higher than the crack pressure so that the poppet moves into over-travel ... the radial deflection opens a purge gap ... so that inflation gas flows as an air purge along a purge flow path, separate from the main passage, through the purge gap into the inflatable chamber" | Claim 1's second range and the air purge as the act; the air purge is essential on 03 A2 | §2, §3(6), §4; 01 (d) S3, S4; 03 C2, C6, C7; 19 "air purge"; 16 S9.3–S9.5 | As claim 1 (09 rows 1, 2); support conditional on 01 Q1/Q2 | Wipe-only product (R7): escapes; the over-travel by head (R5) is within the method if the differential exceeds the threshold, which a depressor head does not require |
| 4 | "removing the inflation device from the supply side so that the pressure differential falls and the deflectable ring element undergoes shape recovery to close the purge gap" | The end of the inflation event; the snap-back wipe is a dependent step | §2; 01 (d) S5; bench data (snap on removal); 16 S9.6 | ref-02 [0020] (07 N0e E), not a distinction alone | None |
| 5 | "A method of manufacturing a seat ring (30) for a valve core of an inflation valve" | Process family (02 rank 4) | §7; 16 S12 | None | None |
| 5 | "providing tube stock of a superelastic alloy" | The §7 starting material; "superelastic alloy" (genus) rather than NiTi | §5, §7; 03 C15, C24; 19 "superelastic alloy"; 16 S12.1, S10.1 | 08 N7: CGK of NiTi processing (08 A5); US6393765B1 generic treatment (07 N6/7 ?) | Strip, sheet or bar routes (12 E15.2, E15.5, E15.6; 11 DA-21): escape; they are dependents of family B, not of claim 5 |
| 5 | "laser cutting the tube stock to form a seat ring blank having a first axial end forming a sealing edge and a second axial end" | The §7 cutting step; the sealing edge ties the process to the family B product | §7 ("laser-cutting ... on a mandrel"); 03 C24; 16 S12.1 | As above; US9982818B2 claim 10 is a different process (07 N6/7) | Photochemical etching (E15.6): escapes |
| 5 | "forming, in a wall of the seat ring blank ..., a convoluted wall having at least one convolution" | Which step forms the convolution is unstated (01 Q11), so the step is claimed generically | §7 (mandrel; fixture "holding the wave geometry"); 03 C12; 16 S12.1 | As above | Roll-forming or hydroforming (E15.2, E15.3): still "forming"; covered |
| 5 | "shape-setting the seat ring by heating the seat ring blank in a fixture holding the geometry of the convoluted wall and then quenching, so that the convoluted wall is arranged such that an axial load ... produces radial deflection ... and ... recovers elastically" | The step that fixes the geometry and gives the superelastic behaviour; 500 °C, 10 min and water quench are dependents (only the prototype point is disclosed, 01 Q32) | §7; 03 C24; 19 "shape-setting" (LOCKED, not "annealing"); 16 S12.2 | 08 N7 *moderate*: no supplied reference has it, but a handbook would be cited | A polymer ring by moulding (E15.4): outside claim 5 (no superelastic alloy); covered by claim 1 and claim 3 |

## Rationale

**How each claim was built.** Each independent claim starts from the smallest combination that `09` rows 1 and 2 say distinguishes the charted art: two sequential poppet ranges on one poppet, with the ring element clear of the formation in the first and deflected in the second, and a purge gap that is closed in both lower states. Every other feature was tested against "is this needed to distinguish the charted art?" and moved to the ladder if not.

**Limitations removed after that test.** (a) "Seat ring" and "sealing edge" in claims 1, 2 and 4: replaced by the deflectable ring element genus and by "main passage closed by the sealing face", so that Alternative B and an integral flexure are covered; the one-piece seat is ref-02 claim 1 anyway (09 row 6). (b) "Purge shoulder ... on the chamber side of the sealing face": replaced by "deflecting formation" so that DA-4 is covered; the 19 definition of purge shoulder fixes its position. (c) "Second spring stage" and "threshold-setting arrangement": replaced by the relationship "over-travel threshold higher than the crack pressure"; the structure is a dependent genus. (d) "Radially outward": removed; direction-neutral. (e) "Annular radial clearance between the seat ring outer surface and the core body bore": removed; the purge gap is defined by function and state, which is the only definition that survives 01 Q1/Q2 (d2 R1). (f) Snap-back wipe: removed from all independent claims; a dependent of claims 1, 2 and 4. (g) Superelastic alloy, austenite finish temperature, convoluted wall (in claims 1, 2 and 4), all numbers, liquid sealant, tubeless tyre: removed from the apparatus claims (d2 R11, R13, R19). (h) Interference fit, internal shoulder, "threaded into the stem bore": removed; a competitor omits each at no cost (11 DA-22, DA-6).

**Limitations kept although not distinguishing.** The return spring (structural basis of the crack pressure; every product has one) and the shape recovery clause (every product re-closes). Both cost nothing and make the state cycle explicit for the Examiner who cannot see this rationale.

**Claim 1 and the threshold.** I tested the broader relationship (purge state defined by deflection alone, DA-1 genus) and rejected it for claim 1: without the normal-stroke/over-travel sequence the claim reads on ref-02 claim 4 with [0019] (08 item 2). If the inventor confirms that purging on every opening works (03 Q3), a broader claim exists and should be added at the fix pass; I have not drafted it because it is unsupported by the bench data and unconfirmed.

**Claim 1 and the carrier.** A carrier-neutral formulation (ring element and formation each on one of the poppet and the core body, DA-8) was considered and left for Prompt 24, where it is one of the three formulations to be compared. It costs clarity, the wipe then acts on the bore, and DA-8 is rated medium on both plausibility and pull.

**Claim 2 in full rather than "the valve core of claim 1 in a valve stem".** Written out so that the direct-carriage species (no core body) is claimed; a claim referring back to claim 1 would import the core body. The direct-carriage limb rests on an unattended-gate candidate (12 E16.3) and is flagged in A2 and Q4.

**Claim 3's numbers.** The only independent claim with numbers. Without them, 08 rates the component claim *strong* for anticipation by US9982818B2; with the sealing edge, the axial-load conversion and the two ranges, *moderate*. The trade-off against d2 R11 is accepted and stated in the table so counsel can drop the family if the search widens.

**Claim 4 self-contained.** Referring to "the valve core of claim 1" is acceptable at the EPO but is treated as a dependent claim, or an improper one, in the US; the parts are therefore recited. The sealant context sits here, not in the apparatus claims.

**Claim 5.** Kept to four steps. Electropolishing is a dependent because its function is unknown (03 Q15); the 500 °C / 10 min point and the austenite finish temperature are dependents because only the prototype point is disclosed; pressing into the core body is a dependent because it is a separate act and target (family F folded in).

**Support caution repeated for the record.** The purge gap clause of claims 1, 2 and 4 is supported by §2 and §3(6) only conditionally (01 Q1, Q2). It is drafted functionally because that is the only wording under which the description, as blueprinted (16 S7.5, S11.1), can be consistent. If the inventor's answer shows no separate purge gap can be enabled, claims 1, 2 and 4 fall back to the wipe-based nucleus of `03`, and 25 must be re-run.

## Assumptions

A1. No Gate 1 answers exist: 01 Q1/Q2, 03 Q1, Q3, Q5 and 11 Q1–Q25 are unanswered. The purge gap is claimed by function and state; the air purge is essential and the snap-back wipe advantageous (03 A2). Blocking for P5 (25, 28) and REVIEW.

A2. Gate 2 was confirmed unattended. The deflecting formation genus (11 DA-4), the functional purge gap genus (11 DA-2) and the direct-carriage limb of claim 2 (12 E16.3) are engineering candidates; they are used as `CONFIRMED.md` permits and must be reviewed by a human at Gate 3 (16 A4). Blocking for PACKAGE.

A3. The description will contain the genus statements listed in `disclosure_requests` at the blueprint sections cited (16 S7.4–S7.7, S9.2–S9.6, S10.2, S11.9, S12.1–S12.2); paragraph anchors are mapped in P5d. Blocking for P5 (25).

A4. The pressure differential is the supply-side pressure less the chamber-side pressure, and the poppet opens towards the chamber side (01 A3–A5; 19 A4). Blocking for P5 only if 01 Q3/Q4 reverse it.

A5. "Carried by" is construed as in the 19 general-construction paragraph (direct or indirect, including an integral formation on the 16 S10.6 statement), so that claim 1 covers an integral flexure and claim 2 covers both valve formats. Not blocking.

A6. ref-01 and ref-02 (fictional) are treated as charted art; every distinction also holds over US4462449A and EP1137892A1 (08 A2). Blocking for PACKAGE (07 Q2).

## Open Questions

Q1. Where is the purge gap and how does it open against the interference fit (01 Q1, Q2)? The purge gap clause of claims 1, 2 and 4 is unsupported as a specific mechanism until answered; the fallback is the wipe-based nucleus. Blocks P5, REVIEW.

Q2. Does the air purge alone, the snap-back wipe alone, or both produce the effect (03 Q1)? If the wipe alone suffices, a wipe-only independent claim (d2 R7) must be added. Blocks P5.

Q3. Would purging on every opening work (03 Q3; 11 Q1)? If yes, a broader claim without the over-travel threshold above the crack pressure should be added at the fix pass. Blocks P5.

Q4. Did the inventor conceive mechanical over-travel by a depressor head or by hand (11 Q9; 12 E1.4, E1.5)? Decides whether claims 1 and 2 may recite "over-travel produced by the pressure differential or by mechanical actuation" to close d2 R5. Blocks P5.

Q5. Did the inventor conceive the mechanism carried directly by the valve stem and other valve formats (11 Q6; 01 Q26, Q33)? Decides claim 2's direct-carriage limb. Blocks P5, PACKAGE.

Q6. May the deflecting formation be the sealing face or a continuation of it (11 Q4; 03 Q8)? Decides whether "deflecting formation" survives in claims 1, 2 and 4 or reverts to "purge shoulder". Blocks P5.

Q7. Are the §4 ranges of claim 3 the inventor's believed ranges with no evidenced criticality (01 Q15; 03 Q13), and how are seat ring inner diameter and seat ring wall thickness measured (19 Q5)? Blocks P5 (25, 26).

Q8. Full texts of US4462449A, US9982818B2 and EP1137892A1 (07 Q3), and a professional search (07 Q1): the vulnerability column is tested against extracts only. Blocks P5, PACKAGE.

```json
{
  "prompt": "22",
  "status": "complete",
  "assumptions": [
    {"id": "A1", "text": "No Gate 1 answers; purge gap claimed by function and state; air purge essential and snap-back wipe advantageous (03 A2).", "blocking": true},
    {"id": "A2", "text": "Gate 2 confirmed unattended; deflecting formation genus (11 DA-4), functional purge gap genus (11 DA-2) and claim 2 direct-carriage limb (12 E16.3) are candidates used as CONFIRMED.md permits, subject to Gate 3 review.", "blocking": true},
    {"id": "A3", "text": "The description will contain the genus statements listed in disclosure_requests at the cited 16 sections; paragraph anchors mapped in P5d.", "blocking": true},
    {"id": "A4", "text": "Pressure differential is supply-side less chamber-side pressure and the poppet opens towards the chamber side (01 A3-A5; 19 A4).", "blocking": false},
    {"id": "A5", "text": "'Carried by' is construed per the 19 general-construction paragraph (direct or indirect, including integral per 16 S10.6).", "blocking": false},
    {"id": "A6", "text": "Fictional ref-01/ref-02 treated as charted art; distinctions also hold over US4462449A and EP1137892A1.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "Purge gap location and opening against the interference fit (01 Q1, Q2); purge gap clause of claims 1, 2, 4 unsupported as a specific mechanism until answered; fallback is the wipe-based nucleus.", "blocks": ["P5", "REVIEW"]},
    {"id": "Q2", "text": "Air purge alone, snap-back wipe alone, or both (03 Q1)? If wipe alone suffices, a wipe-only independent claim must be added.", "blocks": ["P5"]},
    {"id": "Q3", "text": "Would purging on every opening work (03 Q3; 11 Q1)? If yes, a broader claim without the threshold relationship should be added at the fix pass.", "blocks": ["P5"]},
    {"id": "Q4", "text": "Mechanical over-travel by a depressor head or by hand conceived (11 Q9)? Decides whether claims 1 and 2 may recite mechanical actuation to close d2 R5.", "blocks": ["P5"]},
    {"id": "Q5", "text": "Mechanism carried directly by the valve stem and other formats conceived (11 Q6; 01 Q26, Q33)? Decides claim 2's direct-carriage limb.", "blocks": ["P5", "PACKAGE"]},
    {"id": "Q6", "text": "May the deflecting formation be the sealing face or a continuation (11 Q4; 03 Q8)? Decides 'deflecting formation' versus 'purge shoulder'.", "blocks": ["P5"]},
    {"id": "Q7", "text": "Basis of the claim 3 ranges (01 Q15; 03 Q13) and measurement conventions for seat ring inner diameter and wall thickness (19 Q5).", "blocks": ["P5"]},
    {"id": "Q8", "text": "Full texts of US4462449A, US9982818B2, EP1137892A1 (07 Q3) and a professional search (07 Q1); vulnerability column tested against extracts only.", "blocks": ["P5", "PACKAGE"]}
  ],
  "new_terms": [
    {"term": "deflecting formation", "maps_to": "purge shoulder", "reason": "Locked genus of the purge shoulder (LOCKED Broader column; 16 S7.6, S11.3); used in claims 1, 2 and 4 so that the sealing face, a taper, a collar or lugs are covered (11 DA-4)."},
    {"term": "threshold-setting arrangement", "maps_to": "second spring stage", "reason": "Locked genus of the second spring stage (LOCKED Broader column); named in the table as the dependent genus that the claim 1 threshold relationship leaves open."},
    {"term": "tube stock", "maps_to": null, "reason": "The §7 starting material (drawn NiTi tube) for claim 5; 'tube' alone is barred by the LOCKED drafting notes."},
    {"term": "seat ring blank", "maps_to": "seat ring", "reason": "The laser-cut part before shape-setting, needed to sequence the claim 5 steps (§7)."},
    {"term": "inflation gas", "maps_to": null, "reason": "Any gas from the inflation device (12 E8.5; 16 S7.8), used in claim 4 so that CO2 inflation devices are covered; 'air' alone would limit."},
    {"term": "annular element", "maps_to": "seat ring", "reason": "The LOCKED functional description of the seat ring ('annular element'); used as the structural noun of claim 3."},
    {"term": "first axial end / second axial end", "maps_to": null, "reason": "Orientation-neutral names for the two ends of the seat ring in claims 3 and 5, replacing 'upper edge' (barred) and 'chamber-side end'."}
  ],
  "support_refs": [
    {"item": "Claims 1, 2, 4: core body, deflectable ring element carried by the core body or valve stem", "support": "intake/disclosure.md §3(2), §3(3), §6; runs/r1/P1/03.md C5, C26; CONFIRMED.md 12 E4.5, E16.3, E14.6; 11 DA-5, DA-6; runs/r1/P4/19.md 'deflectable ring element', coupling paragraph; runs/r1/P4/16.md S7.4, S8.3, S8.4, S10.6, S11.9"},
    {"item": "Claims 1, 2, 4: poppet with supply side, chamber side, sealing face, deflecting formation; pressure differential", "support": "intake/disclosure.md §2, §3(4); runs/r1/P1/01.md A3-A5; runs/r1/P1/03.md C1, C4; CONFIRMED.md 12 §3; 11 DA-4; runs/r1/P4/19.md 'purge shoulder', 'supply side', 'chamber side', 'pressure differential'; runs/r1/P4/16.md S7.2, S7.3, S7.6, S8.5, S11.3"},
    {"item": "Claims 1, 2, 4: main passage closed by the sealing face in the closed state; return spring", "support": "intake/disclosure.md §3(4), §3(5), §3(6); runs/r1/P1/01.md (i); runs/r1/P1/03.md C1, C10, C17; runs/r1/P4/19.md 'closed state'; runs/r1/P4/16.md S8.5, S8.6, S9.1"},
    {"item": "Claims 1, 2, 4: normal stroke at the crack pressure, normal-open state, deflecting formation spaced from the ring element throughout the normal stroke", "support": "intake/disclosure.md §2, §3(4), §4; runs/r1/P1/03.md C1, C4, C18; runs/r1/P4/19.md 'normal stroke', 'crack pressure'; runs/r1/P4/16.md S7.3, S8.5, S9.2"},
    {"item": "Claims 1, 2, 4: over-travel above an over-travel threshold higher than the crack pressure; deflecting formation bears on and radially deflects the ring element", "support": "intake/disclosure.md §2, §3(4), §3(5), §4; runs/r1/P1/03.md C2, C3, C13, C18; CONFIRMED.md 12 §2, §6; 11 DA-11; runs/r1/P4/19.md 'over-travel', 'over-travel threshold', 'radial deflection'; runs/r1/P4/16.md S7.3, S9.3, S9.4, S11.4"},
    {"item": "Claims 1, 2, 4: purge gap bounded partly by the ring element, closed in closed and normal-open states, opened by radial deflection; purge flow path separate from the main passage, supply side to chamber side", "support": "intake/disclosure.md §2, §3(6); intake/drawings/README.md FIG-2 via runs/r1/P1/01.md (b)5; runs/r1/P1/03.md C6, C7; CONFIRMED.md 12 §7 genus, §8; 11 DA-2, DA-3; runs/r1/P4/19.md 'purge gap', 'purge flow path', 'purge state'; runs/r1/P4/16.md S7.5, S8.7, S9.4, S9.5, S11.1, S11.2; conditional on 01 Q1, Q2"},
    {"item": "Claims 1, 2, 4: shape recovery closes the purge gap when the pressure differential falls", "support": "intake/disclosure.md §2; runs/r1/P1/03.md C8; intake/data/bench-test.md (audible snap; leak-down at cycle 40); CONFIRMED.md 12 §9; runs/r1/P4/16.md S9.6, S10.7"},
    {"item": "Claim 2: valve stem with stem bore; inflation valve for an inflatable chamber", "support": "intake/disclosure.md §1, §3(1); runs/r1/P4/19.md 'valve stem', 'inflatable chamber'; runs/r1/P4/16.md S8.1, S11.9"},
    {"item": "Claim 3: annular seat ring with sealing edge at a first axial end; convoluted wall with at least one convolution; axial load produces radial deflection; elastic recovery", "support": "intake/disclosure.md §3(3), §3(4), §6; runs/r1/P1/03.md C10, C12, C13; CONFIRMED.md 12 E5.1, E5.2, §9; 11 DA-18; runs/r1/P4/19.md 'seat ring', 'sealing edge', 'convoluted wall'; runs/r1/P4/16.md S8.4, S10.2, S10.7"},
    {"item": "Claim 3: seat ring inner diameter 2.0-2.6 mm; seat ring wall thickness 0.15-0.30 mm", "support": "intake/disclosure.md §4, §7; runs/r1/P1/03.md C21; CONFIRMED.md 13 Table 1; runs/r1/P4/19.md 'seat ring wall thickness'; runs/r1/P4/16.md S7.10, S10.4"},
    {"item": "Claim 4: inflatable chamber holding liquid sealant; coupling and removing the inflation device; inflation gas; air purge", "support": "intake/disclosure.md §1, §2, §8; runs/r1/P1/01.md (d) S1-S5; runs/r1/P1/03.md C7, C31; CONFIRMED.md 12 E1.1, E8.1, E8.5, E9.1; runs/r1/P4/19.md 'inflation event', 'air purge', 'liquid sealant'; runs/r1/P4/16.md S7.8, S9.1-S9.9, S16"},
    {"item": "Claim 5: tube stock of a superelastic alloy; laser cutting; forming the convoluted wall; shape-setting in a fixture and quenching", "support": "intake/disclosure.md §5, §7; runs/r1/P1/01.md (j), Q11; runs/r1/P1/03.md C12, C15, C24; CONFIRMED.md 12 §15; 11 DA-21; runs/r1/P4/19.md 'superelastic alloy'; runs/r1/P4/16.md S10.1, S12.1, S12.2"},
    {"item": "Prior-art vulnerability column", "support": "runs/r1/P2/07.md charts (ref-02, US4462449A, EP1137892A1, US9982818B2, US6393765B1, US4408632A, US11065925B2, ref-01, F0/F1 grid); runs/r1/P2/09.md rows 1-7; runs/r1/P2/08.md items 1-4, A5, A6"},
    {"item": "Design-around column", "support": "CONFIRMED.md 11 DA-1 to DA-22; 12 E1.4, E1.5, E2.3, E3.2, E4.3, E4.4, E5.5, E9.4, E15.2-E15.6; runs/r1/debate/d2-attack.md R1-R19, §7"}
  ],
  "disclosure_requests": [
    {"limitation": "Claims 1, 2, 4: 'a purge gap, bounded at least in part by a surface of the deflectable ring element, ... closed in the closed state and in the normal-open state and ... opened by the radial deflection in a purge state ... so as to open a purge flow path, separate from the main passage, from the supply side to the chamber side'", "needed_disclosure": "An express statement in those words in the definitions (16 S7.5) and in operation (S9.4, S9.5), with the outer-surface, inner-surface, end-face and through-wall species (12 §7) each described and none named as the prototype mechanism until 01 Q1/Q2 are answered."},
    {"limitation": "Claims 1, 2, 4: 'a deflecting formation' of the poppet, 'spaced from the deflectable ring element throughout the normal stroke' and 'bearing on the deflectable ring element in the over-travel'", "needed_disclosure": "An express genus statement (16 S7.6, S11.3) that the deflecting formation is the purge shoulder in the illustrated embodiment and may be the sealing face or a continuation of it, a taper on the poppet stem, a collar, lugs or the return-spring retainer; and an express statement of the axial clearance between it and the deflectable ring element in the closed state and the normal-open state (S8.5, S9.2)."},
    {"limitation": "Claims 1, 2, 4: 'an over-travel threshold higher than the crack pressure' with no threshold-setting structure recited", "needed_disclosure": "More than one corresponding structure described (16 S8.6, S11.4): the second spring stage, an auxiliary spring with lost motion, a disc spring stack, a detent, a polymer bush, and the deflectable ring element's own stiffness with a single-rate return spring, so that the functional relationship is not limited to the two-stage return spring under 35 U.S.C. §112(f)."},
    {"limitation": "Claims 1, 2, 4: 'the deflectable ring element undergoing shape recovery to close the purge gap when the pressure differential falls'", "needed_disclosure": "An express statement (16 S9.6, S10.7) that shape recovery may be superelastic, elastic (polymer or spring metal) or assisted by a second formation on the poppet, and that in each case the purge gap is closed in the closed state."},
    {"limitation": "Claim 2: deflectable ring element, poppet and return spring 'carried by the valve stem'", "needed_disclosure": "An express statement (16 S11.9) that the parts are carried by the valve stem either through a removable core body received in the stem bore or directly in a non-removable inflation valve, labelled as a candidate pending 11 Q6; and that 'carried by' includes both (S7.1)."},
    {"limitation": "Claim 3: 'an annular element having a wall extending between a first axial end and a second axial end, the first axial end forming a sealing edge', 'an axial load applied to the seat ring produces radial deflection of the convoluted wall', 'recovers elastically on removal of the axial load'", "needed_disclosure": "An express description of the seat ring as a component (16 S11.10, S17 CF-B) using 'first axial end' and 'second axial end', the axial-load statement in genus form for any material (S10.2), and the measurement conventions for seat ring inner diameter and seat ring wall thickness (S7.10)."},
    {"limitation": "Claim 4: 'inflation gas flows as an air purge along a purge flow path ... into the inflatable chamber'", "needed_disclosure": "An express statement (16 S7.8, S9.5) that the air purge is a flow of any inflation gas, including gas from a CO2 inflation device, and that the purge flow path discharges into the inflatable chamber."},
    {"limitation": "Claim 5: 'forming ... a convoluted wall' and 'shape-setting ... by heating the seat ring blank in a fixture holding the geometry of the convoluted wall and then quenching'", "needed_disclosure": "An express statement (16 S12.1, S12.2) that the convolution may be formed by the laser cut, by a mandrel or by the shape-setting fixture, that 500 °C for 10 minutes followed by a water quench is one example of the shape-setting step, and that the cut part before shape-setting is the seat ring blank."},
    {"limitation": "Claims 1, 2 (to close d2 R5): 'over-travel produced by the pressure differential or by mechanical actuation of the poppet'", "needed_disclosure": "Not drafted. Needed only if the inventor confirms mechanical over-travel by a depressor head or by hand was conceived (11 Q9; 12 E1.4, E1.5); if confirmed, an express statement at 16 S9.8 and a revised claim 1 wherein clause."}
  ],
  "open_disagreements": [],
  "narrowing_suggested": []
}
```
````

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P2/08.md`

````markdown
## Deliverable

### Novelty and Inventive-Step Attack

This is a preliminary, diagnostic pass prepared by AI as a drafting and analysis aid. It is not legal advice, it is not a validity opinion, and it is not the final examiner review (Prompt 32). Qualified patent counsel signs off before anything is filed.

**Basis.**
- **Concepts attacked:** the proposed independent claim concepts are N0 and the ladder N1–N7 from `03`, the wipe-based alternative nucleus that `03` records, and the items ranked 1–6 and 10 in the value map `02`. There are no drafted claims.
- **References:** only the 17 references charted in `07` are used, and every objection cites a `07` chart row. Fifteen are machine-retrieved extracts and two (ref-01, ref-02) are fictional requester summaries (07 Q2).
- **Unresolved inputs:** there are no Gate 1 answers, so 03 Q1 (purge against wipe), 03 Q5 (Alternatives A and B) and 01 Q1/Q2 (the purge gap) remain open.
- **Coverage:** coverage is thin (07 Q1). An objection rated *weak* here means weak against **this pile**. It does not mean the art is clear.

#### How a hostile examiner would lead

1. **Closest single reference: ref-02 (fictional).** Of the real references, the closest is **US4462449A**. The examiner would read the essential elements onto them as follows:
   - ref-02 has a tyre valve whose seat ring the poppet deflects on opening (claim 4), which enlarges the flow passage ([0019]) and recovers when the pump is removed ([0020]) (07 ref-02 rows N0c, N0d, N0e, N2).
   - US4462449A has a tyre valve core whose closure member deforms a resilient member only after an initial part of its travel (claim 1; 07 US4462449A row N0c).
   - The examiner's argument would be that "purge gap" reads on the enlarged passage and "over-travel" reads on the later part of a single opening stroke.
   - This fails **only if** N0 is drafted so that three things are unmistakable: (i) a normal-open state exists, with main-passage flow and no contact between the purge shoulder and the deflectable ring element; (ii) the contact that deflects the ring happens only beyond the normal stroke, above a higher over-travel threshold; (iii) the purge gap is a separate path, closed in both the closed state and the normal-open state.
2. **Strongest combination: ref-02 + EP1137892A1 + CN215861914U.**
   - EP1137892A1 contributes a tyre valve core in which a calibrated spring lets a gap open above a pressure threshold (07 EP1137892A1 rows N0b, N0d).
   - CN215861914U contributes pressurised air flow removing deposits inside a tyre valve (07 CN215861914U row N0d, A†).
   - The same mosaic can be built from real art by using US4462449A in place of ref-02.
3. **Common general knowledge and routine design.** These cover the add-on features:
   - superelastic NiTi as a repeatedly deformed seal (07 US6393765B1 row N4; US9982818B2 row N4);
   - a wave-profile NiTi sealing ring with radial movement (07 US9982818B2 row N3);
   - rising-rate or two-spring biasing (07 US9297373B2, EP1137892A1 and US4627461A, row N5);
   - optimisation of numerical ranges;
   - the NiTi tube process.

   Any CGK statement that no supplied reference supports is labelled as an assumption (A3–A6).

#### Attack by claim concept

| Concept | Strongest novelty objection (single reference; `07` row) | Rating and reason | Strongest inventive-step objection | Rating and reason |
|---|---|---|---|---|
| **N0**: normal stroke, then over-travel above a threshold; the purge shoulder deflects the deflectable ring element only in over-travel; a separate purge gap is closed at rest; shape recovery closes it. Same as value map rank 1, the valve core claimed without the valve stem | ref-02: poppet-deflected seat ring (claim 4, row N0c ?), enlargement of the flow passage by the deflection ([0019], row N0d ?), recovery on removal of the pump ([0020], row N0e E). Real-art version: US4462449A claim 1 (row N0c ?) | **Weak** against N0 as `03` states it: rows N0b are absent from ref-02 and from US4462449A, and neither has a normal-open state separate from the deflection. **Strong** against any claim that lets the purge gap read on the main passage, or that omits the normal-stroke/over-travel sequence | ref-02 (closest) + EP1137892A1 (a calibrated spring opens a gap above a threshold in a tyre valve core: claims 1(e), 8; rows N0b ?, N0d ?) + CN215861914U (pressurised air flow cleans a tyre valve: row N0d A†). Motivation: ref-02 [0008] names contamination of the sealing surfaces; CN215861914U shows that air flow can clean. US examiners may present this as a combination of known elements with predictable results | **Moderate.** Three documents, and none teaches that the inflation poppet's own extra travel deflects the seat. EP1137892A1's threshold acts on chamber-side pressure and releases air **out** of the tyre, the opposite of an inflation-direction purge. Under the EPO problem-solution approach and UK practice there is no pointer from EP1137892A1 (pressure regulation) to the objective problem (removing sealant film during inflation), so the objection is weaker there than in the US. It becomes strong if N0d is not enabled and the claim has to fall back to "any gap" (Q4) |
| **Wipe-based alternative nucleus** (03, pending 03 Q1): N0a–N0c + N0e + snap-back wipe, without a purge gap | ref-02 again (rows N0c ?, N0e E); ref-02 has no wipe (row N1 A) | **Weak.** N1 is absent from every reference | ref-02 + US4719938A: an expansible wiper ring wipes on the closing stroke, which the pressure differential drives (abstract, claims 1 and 5; row N1 A†). Motivation: both concern contamination of the sealing surfaces. The examiner would argue that moving the wiping element from the moving part to the fixed part is a routine kinematic inversion (A5) | **Moderate.** Two documents, with a shared problem. Counter-points: ref-02 chooses an elastomer to *seal around* particles, the opposite mechanism; US4719938A's wiper is carried by the valve member and wipes the bore; no reference teaches that recovery of the seat ring **itself** produces the relative movement |
| **N1**: N0 + snap-back wipe | None. Row N1 is absent (A or A†) in all 17 references | **Weak** | The N0 combination + US4719938A or US6006954A (a flexible wiper removes deposits on each stroke: claims 1, 6; row N1 A†); tyre-valve analogue US11345196B2 (a sealing ring on a moving rod removes sealant: abstract, claim 1; row N1 A†) | **Weak.** Four documents, two of them from unrelated fields (cryopumps, aerosol metering), and the wiping art uses a different kinematic arrangement (wiper on the moving member). This relies on hindsight. The effect evidence helps: the conventional cores failed at cycles 12–18 while the prototypes ran 40 (bench data). But that comparison is against a conventional core, not against the closest art (Q6) |
| **N2**: N1 + the deflectable ring element is the seat ring | As for N1. The **increment** itself is disclosed by ref-02 claim 1 (row N2 E) | The concept: **weak**, carried by N0/N1. The increment alone: **strong**, as it adds nothing new over ref-02 | The increment is known from ref-02 | The concept: **weak** (as N1). N2 adds no inventive-step weight |
| **N3**: N2 + convoluted wall converting axial load into radial deflection | As for N1. The increment is closest to US9982818B2: a wave-profile ring whose inner and outer portions move radially (abstract, claims 3–5; row N3 ?) | The concept: **weak**. The increment is not anticipated: the radial movement in US9982818B2 comes from heating, not from axial load | Increment: ref-02 [0024] (a resilient metal seat as an alternative; row N4 ?) + US9982818B2 (wave profile; pseudoelastic "high fatigue resistance", background; rows N3 ?, N4 E) | The increment: **moderate.** There is a motivation (fatigue resistance under repeated strain), but US9982818B2 is a static seal between two members, actuated thermally, and teaches nothing about turning a poppet's axial load into radial opening. The concept overall stays **weak** (as N1) |
| **N4**: N3 + superelastic alloy seat ring, NiTi, Af below 5 °C | As for N1. Increment: US6393765B1 (a superelastic NiTi seal element deformed by the closing part: claim 1, summary; rows N2 ?, N4 E); US9982818B2 (NiTi, claims 9 and 11) | The concept: **weak**. The increment is known as a material choice for a deformable seal | Increment: ref-02 [0024] + US6393765B1 or US9982818B2. Af below 5 °C: the examiner would say that superelastic behaviour needs a service temperature above the transformation temperature (tied to the US9982818B2 background, "when above the transformation temperature, the SMA may exhibit pseudoelastic behaviour"), so the choice of Af follows from the service temperatures (A3) | The increment: **strong.** It is a known material for a known purpose, and the Af value is chosen from the operating temperature. The inventor's stated effect, "fast and stiff" recovery driving the wipe (§2), is not isolated by the test: no seat ring of elastomer, PEEK or spring steel in the same geometry was tested (Q5, Q6). The concept overall stays **weak** (as N1) |
| **N5**: N4 + return spring with a first spring stage and a second spring stage | As for N1. Increment: EP1137892A1 claim 28 (two springs on one moving member; row N5 ?); US9297373B2 claim 1 (progressive springs on a poppet; row N5 ?); US4627461A claim 3 (row N5 ?) | The concept: **weak**. The increment is ambiguous in every reference: none has sequential stages | Increment: once an over-travel threshold is claimed, a stiffer second spring stage is an obvious way to set it (US9297373B2; A4) | The increment: **strong.** It is a standard means for a claimed function. It adds nothing to the inventive step |
| **N6**: N5 + the inventor's believed ranges (§4) | None of the ranges appears in any reference (rows N6/7 A) | **Weak** (novelty is carried by N0) | Routine optimisation. Only the prototype values were built; over-travel and purge-gap opening were not measured (bench data); nothing is shown about the range endpoints (01 (h)) (A6) | **Strong.** The ranges would be treated as arbitrary selections within a design the examiner regards as known. They are useful only as fallbacks once N0/N1 are accepted |
| **N7**: N6 + prototype values and process (laser cutting, shape-setting at 500 °C for 10 min, water quench, electropolishing, interference fit of about 0.03 mm) | None. Rows N6/7: US6393765B1 has a generic "thermo-mechanical treatments already known in the art" (?); ref-01 has a sleeve press-fitted into the core body (?) | **Weak** | CGK of NiTi tube processing, which no supplied reference supports (A5); US6393765B1 summary; ref-01 press fit | **Moderate.** It cannot be tied to a supplied reference, but an examiner would cite a handbook. It adds little |
| **Value map rank 2**: the seat ring as a component (material + convoluted wall, "for" a valve core) | US9982818B2: a NiTi sealing ring with a wave profile between radially inner and outer portions (abstract, claims 3, 4, 9; rows N3 ?, N4 E). "For a valve core" is read as "suitable for" at the EPO, and preamble intended use usually does not limit in the US | **Strong** against a ring defined only by material and wave wall. **Moderate** if the ring is defined by a sealing edge, by ring dimensions (§4) and by superelasticity at service temperature. The extract gives no dimensions (07 Q3) | ref-02 [0024] + US9982818B2 | **Moderate.** A component claim does not inherit the N0 distinctions |
| **Value map rank 3**: inflatable chamber, tyre or wheel with the valve core | As for N0. The increment is known: US11179979B2 claim 12 (a tubeless wheel with a valve stem system); US11065925B2 claim 7 (tyre and rim assembly) | Same as N0 (**weak**) | Same as N0 | Same as N0 (**moderate**). The system adds nothing |
| **Value map rank 4**: method of manufacturing the seat ring (§7) | None (rows N6/7 A). US9982818B2 claim 10 is a different process: deform below the martensitic temperature, then heat | **Weak** | CGK of NiTi processing (A5) | **Moderate to strong** once the ring itself is known. The claim survives only through the product it makes (the N3/N4 ring with a sealing edge) or through a demonstrated process effect, and the disclosure states none: the function of electropolishing is not given (03 Q15) |
| **Value map rank 6**: Alternative B, a fixed seat plus a separate wiper ring deflected outward by the purge shoulder | ref-01: rigid seat, sealant problem (rows F1 E, N2 A). No reference has a stationary wiper ring deflected by the valve member | **Weak** | ref-01 + US4719938A (a radially expansible wiper whose radial state changes with valve travel along a taper; abstract, claim 5) | **Moderate.** Kinematic inversion again (A5). Support is also thin: §6 is one paragraph with no geometry (03 Q7) |
| **Thermal two-way variant** (outside N0; value map rank 10) | None anticipates it in a valve. US9982818B2 claim 5: heating causes radial movement of an SMA wave ring (row N3 ?) | **Weak** | Any tyre-valve reference + US9982818B2 claim 5 / US6393765B1 claim 1 (deformation "in response to a change in temperature") | **Moderate to strong.** Heat-driven radial movement of an SMA ring is known. The inventor has no data and doubts the variant (§6) |

#### What the attack shows (diagnostic, not claim wording)

1. **Novelty and inventive step both rest on three N0 relationships:**
   - the purge shoulder is clear of the deflectable ring element through the normal stroke and bears on it only in over-travel (N0b + N0c);
   - the purge gap is separate from the main passage and closed in the closed and normal-open states (N0d);
   - for N1, the relative movement of the wipe comes from **shape recovery** of a ring element that is fixed in the core body.

   None of these is in the pile. Every other feature on the ladder is either known on its own (N2, N4, N5) or routine (N6, N7).
2. **Where a naive claim falls.** A claim reciting "a resiliently deflectable seat that the poppet deflects to open an additional flow path" reads on ref-02 claim 4 with [0019]. That is the critical risk for the drafters.
3. **N0d is attackable twice.** It is attackable on the art and on sufficiency or written description (EPC Art. 83; 35 U.S.C. §112(a); UK s.14(3)): as disclosed, the location and opening of the purge gap are inconsistent (01 Q1, Q2). If N0d cannot be enabled, N0 falls back towards ref-02 and the wipe-based alternative carries the case (Q4).
4. **The effect evidence is real but does not isolate anything.** The prototypes survived 40 cycles against 12–18 for the conventional cores, which supports a technical effect over a conventional core. It does not attribute the effect to over-travel, to the purge gap or to the wipe, and it does not compare against a deflecting-seat valve of the ref-02 type. That is the comparison an EPO examiner will ask for under the problem-solution approach (Q5, Q6).

## Rationale

**Order of the attack.** It follows how an examiner actually leads: the closest single document, then the best combination, then CGK. ref-02 leads even though it is fictional, because it is the only document in which the poppet itself deflects the seat ring and the ring recovers when the pump is removed. I paired it with US4462449A so that the attack survives if the fictional documents are dropped (07 Q2).

**Novelty ratings.** Every N0 novelty rating is *weak* only on condition that the drafting keeps the normal-stroke/over-travel sequence and a separate purge gap. I gave the opposite rating (*strong*) for a claim that loses them, because that is where the attack will land.

**Inventive-step ratings.**
- The main N0 combination is rated *moderate* rather than *weak* for two reasons: US practice allows three-document mosaics of known elements, and the sufficiency problem with N0d could force a broader reading of "gap".
- The add-on features N4, N5 and N6 are rated *strong* as increments on purpose. They are real features and commercially useful fallbacks, but the drafters should not expect them to carry inventive step.

**Value-map items.** They are attacked where the value map would change the claim structure:
- The component claim (rank 2) is the most exposed item after a naive N0, because US9982818B2 is a NiTi wave-profile ring and a component claim loses the valve context.
- Alternative B and the thermal variant are rated so that Phase 3 knows how much weight they can carry.

**Kinematic inversion.** I did not treat moving the wiper from the moving part to the fixed part as automatically obvious. It is labelled as a CGK assumption (A5), because the references show wiping driven by the valve member's stroke and none shows wiping driven by recovery of the ring. That difference is where the defence will be won or lost.

## Assumptions

A1. No Gate 1 answers exist. The concepts are attacked as `03` states them, with the air purge essential and the wipe advantageous. The wipe-based alternative nucleus is attacked separately. Blocking for P3 and P5 until 03 Q1 and 01 Q1/Q2 are answered.

A2. ref-01 and ref-02 are treated as prior art for this test matter, as supplied. Every conclusion that depends on ref-02 also has a real-art counterpart (US4462449A) so that it can be rebased. Not blocking for P2; blocking for PACKAGE (07 Q2).

A3. CGK assertion: a superelastic alloy seat ring behaves superelastically only above its austenite finish temperature, so choosing an Af below the lowest service temperature is routine. This is partly tied to the US9982818B2 background; the numerical choice (below 5 °C) is not tied to any supplied reference. Not blocking.

A4. CGK assertion: two-stage or rising-rate biasing of a poppet is a standard design means. This is tied to US9297373B2 claim 1, EP1137892A1 claim 28 and US4627461A claim 3, none of which shows sequential first and second spring stages. Not blocking.

A5. CGK assertions not tied to any supplied reference:
- laser cutting, shape-setting and electropolishing NiTi tube are standard NiTi manufacturing practice;
- moving a wiping element from the moving member to the fixed member (kinematic inversion) is within the skilled person's routine;
- a tyre-valve designer would consult relief-valve, cryopump and aerosol metering-valve art as reasonably pertinent to deposits on sealing surfaces (US analogous-art test; EPO neighbouring fields).

Not blocking; each should be checked by counsel against real CGK evidence.

A6. The §4 ranges are the inventor's belief ("ranges we believe would work"), with only the prototype values built. They are treated as having no evidenced criticality. Not blocking.

## Open Questions

Q1. Coverage is thin: 15 web extracts and 2 fictional summaries, English-language, one engine, no non-patent literature and no CPC walk (07 Q1). The *weak* ratings for N0/N1 are weak against this pile only. Commission a professional search before Phase 3 relies on them? Blocks P3, P5, PACKAGE.

Q2. Should ref-01 and ref-02 (fictional) stay in the attack and the Prosecution Assessment, or should the closest art be rebased on US4462449A and EP1137892A1 (07 Q2)? Blocks PACKAGE.

Q3. The full texts of US4462449A (does withdrawal of the closure member wipe it; inflation-flow statement), US9982818B2 (profile and dimensions), US4719938A and EP1137892A1 are needed before the ambiguous rows can be settled (07 Q3). Blocks P3, PACKAGE.

Q4. Where is the purge gap, and how does it open against the 0.03 mm interference fit (01 Q1, Q2; 03 Q2)? Without an enabled, separate purge gap, N0 falls back towards ref-02 claim 4 with [0019]. Blocks P3, P4, P5.

Q5. Does the air purge alone, the snap-back wipe alone, or both produce the effect (03 Q1; 01 Q24)? The answer decides which of the three relationships the independent claims must carry. Blocks P3, P5.

Q6. Can the inventor supply any comparison against a deflecting elastomer seat of the ref-02 type, or against a seat ring of the same geometry in a non-superelastic material? Without it, the bench data shows an effect only over a conventional valve core, not over the closest art. Blocks P3, P4.

Q7. Has the inventor shown, used or published the prototypes, the concept or the results before filing (01 Q34)? Blocks P2, PACKAGE.

Q8. Are Alternatives A (PEEK) and B (fixed seat plus wiper ring) within the invention (03 Q5)? Alternative B is attackable by ref-01 + US4719938A, and §6 gives it one paragraph. Blocks P3, P5.

```json
{
  "prompt": "08",
  "status": "partial",
  "assumptions": [
    {"id": "A1", "text": "No Gate 1 answers exist; concepts attacked as 03 states them (air purge essential, wipe advantageous), with the wipe-based alternative nucleus attacked separately.", "blocking": true},
    {"id": "A2", "text": "ref-01 and ref-02 (fictional) treated as prior art for this test matter; each ref-02-based conclusion has a real-art counterpart (US4462449A) so it can be rebased.", "blocking": false},
    {"id": "A3", "text": "CGK: a superelastic alloy seat ring is superelastic only above its Af, so choosing Af below the lowest service temperature is routine; partly tied to US9982818B2 background, the numerical choice is not.", "blocking": false},
    {"id": "A4", "text": "CGK: two-stage or rising-rate biasing of a poppet is a standard means; tied to US9297373B2 claim 1, EP1137892A1 claim 28, US4627461A claim 3, none showing sequential stages.", "blocking": false},
    {"id": "A5", "text": "CGK not tied to any supplied reference: NiTi tube laser cutting, shape-setting and electropolishing are standard; kinematic inversion of a wiping element is routine; tyre-valve designers would consult relief, cryopump and aerosol valve art.", "blocking": false},
    {"id": "A6", "text": "The §4 ranges are inventor belief with only prototype values built; treated as having no evidenced criticality.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "Coverage thin (07 Q1); 'weak' ratings for N0/N1 are weak against this pile only. Commission a professional search before Phase 3?", "blocks": ["P3", "P5", "PACKAGE"]},
    {"id": "Q2", "text": "Keep fictional ref-01/ref-02 in the attack and Prosecution Assessment, or rebase closest art on US4462449A and EP1137892A1?", "blocks": ["PACKAGE"]},
    {"id": "Q3", "text": "Full texts of US4462449A, US9982818B2, US4719938A and EP1137892A1 needed to settle ambiguous rows.", "blocks": ["P3", "PACKAGE"]},
    {"id": "Q4", "text": "Purge gap location and opening against the 0.03 mm interference fit (01 Q1, Q2); without an enabled separate purge gap N0 falls back towards ref-02 claim 4 with [0019].", "blocks": ["P3", "P4", "P5"]},
    {"id": "Q5", "text": "Air purge alone, snap-back wipe alone, or both (03 Q1; 01 Q24)? Decides which relationship the independent claims must carry.", "blocks": ["P3", "P5"]},
    {"id": "Q6", "text": "Any comparison against a ref-02-type deflecting elastomer seat, or against the same geometry in a non-superelastic material? Bench data shows effect only over a conventional valve core.", "blocks": ["P3", "P4"]},
    {"id": "Q7", "text": "Any public showing, use or publication by the inventor before filing (01 Q34)?", "blocks": ["P2", "PACKAGE"]},
    {"id": "Q8", "text": "Are Alternatives A (PEEK) and B (fixed seat plus wiper ring) within the invention (03 Q5)? Alternative B is attackable by ref-01 + US4719938A and §6 gives one paragraph.", "blocks": ["P3", "P5"]}
  ],
  "new_terms": [
    {"term": "threshold-setting arrangement", "maps_to": "second spring stage", "reason": "Locked genus of the second spring stage; used so the attack on N0b is not limited to the two-rate return spring."}
  ],
  "support_refs": [
    {"item": "Concepts attacked (N0, ladder N1-N7, wipe-based alternative)", "support": "runs/r1/P1/03.md Inventive Nucleus and ladder"},
    {"item": "Value-map concepts (ranks 1-4, 6, 10)", "support": "runs/r1/P1/02.md Commercial Value Map"},
    {"item": "Closest single reference ref-02", "support": "runs/r1/P2/07.md ref-02 rows N0c, N0d, N0e, N2, N4; intake/prior-art/ref-02-elastomer-seat-valve.md claims 1, 4, [0008], [0019], [0020], [0024]"},
    {"item": "Real-art closest US4462449A", "support": "runs/r1/P2/07.md US4462449A row N0c; refs/US4462449A.md claim 1"},
    {"item": "Threshold-opened gap in tyre valve core", "support": "runs/r1/P2/07.md EP1137892A1 rows N0b, N0d, N5; refs/EP1137892A1.md claims 1, 8, 28"},
    {"item": "Air-flow cleaning in tyre valve", "support": "runs/r1/P2/07.md CN215861914U row N0d; refs/CN215861914U.md abstract"},
    {"item": "Wiping on closing", "support": "runs/r1/P2/07.md US4719938A, US6006954A, US11345196B2 rows N1; refs files abstracts and claims cited"},
    {"item": "Material and wave geometry", "support": "runs/r1/P2/07.md US9982818B2 rows N3, N4; US6393765B1 rows N2, N4"},
    {"item": "Spring increment", "support": "runs/r1/P2/07.md US9297373B2, EP1137892A1, US4627461A rows N5"},
    {"item": "Effect evidence", "support": "intake/disclosure.md §8; intake/data/bench-test.md via runs/r1/P1/01.md (l)"},
    {"item": "Purge gap inconsistency", "support": "runs/r1/P1/01.md (m), Q1, Q2; runs/r1/P1/03.md N0 enablement caution"}
  ],
  "disclosure_requests": [
    {"limitation": "N0d separate purge gap, closed in closed and normal-open states", "needed_disclosure": "Consistent written description of the purge gap boundaries, opening mechanism against the interference fit, and air path into the inflatable chamber (01 Q1, Q2)."},
    {"limitation": "Technical effect attributable to the distinguishing features", "needed_disclosure": "Any test separating air purge from snap-back wipe, and any comparison against a deflecting elastomer seat or a non-superelastic seat ring of the same geometry."}
  ],
  "open_disagreements": [],
  "narrowing_suggested": []
}
```
````

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/registry.json`

```json
{
  "entries": [
    {
      "numeral": "10",
      "component": "valve stem",
      "first_figure": "1",
      "figures": [
        "1"
      ]
    },
    {
      "numeral": "12",
      "component": "stem bore",
      "first_figure": "1",
      "figures": [
        "1"
      ]
    },
    {
      "numeral": "20",
      "component": "core body",
      "first_figure": "1",
      "figures": [
        "1"
      ]
    },
    {
      "numeral": "22",
      "component": "core body bore",
      "first_figure": "1",
      "figures": [
        "1"
      ]
    },
    {
      "numeral": "24",
      "component": "internal shoulder",
      "first_figure": "1",
      "figures": [
        "1"
      ]
    },
    {
      "numeral": "30",
      "component": "seat ring",
      "first_figure": "1",
      "figures": [
        "1"
      ]
    },
    {
      "numeral": "32",
      "component": "convoluted wall",
      "first_figure": "1",
      "figures": [
        "1"
      ]
    },
    {
      "numeral": "34",
      "component": "sealing edge",
      "first_figure": "1",
      "figures": [
        "1"
      ]
    },
    {
      "numeral": "40",
      "component": "poppet",
      "first_figure": "1",
      "figures": [
        "1"
      ]
    },
    {
      "numeral": "41",
      "component": "poppet stem",
      "first_figure": "1",
      "figures": [
        "1"
      ]
    },
    {
      "numeral": "42",
      "component": "sealing face",
      "first_figure": "1",
      "figures": [
        "1"
      ]
    },
    {
      "numeral": "44",
      "component": "purge shoulder",
      "first_figure": "1",
      "figures": [
        "1"
      ]
    },
    {
      "numeral": "50",
      "component": "return spring",
      "first_figure": "1",
      "figures": [
        "1"
      ]
    },
    {
      "numeral": "52",
      "component": "first spring stage",
      "first_figure": "1",
      "figures": [
        "1"
      ]
    },
    {
      "numeral": "54",
      "component": "second spring stage",
      "first_figure": "1",
      "figures": [
        "1"
      ]
    },
    {
      "numeral": "60",
      "component": "purge gap",
      "first_figure": "1",
      "figures": [
        "1"
      ]
    },
    {
      "numeral": "62",
      "component": "purge flow path",
      "first_figure": "3",
      "figures": [
        "3"
      ]
    },
    {
      "numeral": "64",
      "component": "main passage",
      "first_figure": "2",
      "figures": [
        "2"
      ]
    },
    {
      "numeral": "70",
      "component": "lock nut",
      "first_figure": "1",
      "figures": [
        "1"
      ]
    },
    {
      "numeral": "130",
      "component": "fixed seat",
      "first_figure": "10",
      "figures": [
        "10"
      ]
    },
    {
      "numeral": "132",
      "component": "wiper ring",
      "first_figure": "10",
      "figures": [
        "10"
      ]
    },
    {
      "numeral": "224",
      "component": "crimped lip",
      "first_figure": "8",
      "figures": [
        "8"
      ]
    },
    {
      "numeral": "232",
      "component": "frustoconical wall",
      "first_figure": "12",
      "figures": [
        "12"
      ]
    },
    {
      "numeral": "244",
      "component": "tapered purge shoulder",
      "first_figure": "11",
      "figures": [
        "11"
      ]
    },
    {
      "numeral": "254",
      "component": "auxiliary spring",
      "first_figure": "14",
      "figures": [
        "14"
      ]
    },
    {
      "numeral": "262",
      "component": "purge port",
      "first_figure": "13",
      "figures": [
        "13"
      ]
    },
    {
      "numeral": "324",
      "component": "retaining sleeve",
      "first_figure": "8",
      "figures": [
        "8"
      ]
    },
    {
      "numeral": "332",
      "component": "slotted wall",
      "first_figure": "12",
      "figures": [
        "12"
      ]
    },
    {
      "numeral": "344",
      "component": "discrete lugs",
      "first_figure": "11",
      "figures": [
        "11"
      ]
    },
    {
      "numeral": "354",
      "component": "detent",
      "first_figure": "14",
      "figures": [
        "14"
      ]
    },
    {
      "numeral": "362",
      "component": "flute",
      "first_figure": "13",
      "figures": [
        "13"
      ]
    },
    {
      "numeral": "432",
      "component": "cellular wall",
      "first_figure": "12",
      "figures": [
        "12"
      ]
    },
    {
      "numeral": "444",
      "component": "separate collar",
      "first_figure": "11",
      "figures": [
        "11"
      ]
    },
    {
      "numeral": "620",
      "component": "Schrader-pattern core body",
      "first_figure": "15",
      "figures": [
        "15"
      ]
    },
    {
      "numeral": "630",
      "component": "Schrader-pattern poppet",
      "first_figure": "15",
      "figures": [
        "15"
      ]
    },
    {
      "numeral": "730",
      "component": "seat ring (stem-integrated)",
      "first_figure": "15",
      "figures": [
        "15"
      ]
    }
  ],
  "source": "/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P4/20a.md"
}
```

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P4/19.md`

````markdown
## Deliverable

### Definitions

This drafting and analysis aid was prepared by AI. It is not legal advice, and qualified patent counsel signs off before anything is filed. Every definition below is drafted from the locked terminology table (`terminology/LOCKED.md`), the Phase 1 structured disclosure (`P1/01.md`) and nucleus analysis (`P1/03.md`), and the confirmed Phase 3 material (`CONFIRMED.md`). Where a locked term's own genus/species columns already commit to functional, direction-neutral or material-neutral language, that breadth is carried into the definition below. Breadth proposed only in the Phase 3 design-around register or equivalent architecture library, and still marked "needs inventor confirmation" there, is **not** imported into these definitions; see `## Rationale` and `## Open Questions`.

Definitions are given in drafting order (mechanism and structure, then operating states and parameters, then materials and the worked-example vocabulary), not alphabetically, so that later definitions can build on earlier ones.

**"valve core"** As used herein, a "valve core" means the assembly, received in the stem bore of a valve stem, comprising a core body, a poppet, a return spring and a deflectable ring element, which together open and close an inflation valve at a pressure differential and purge accumulated sealant film from the valve's sealing surfaces during use. In the illustrated embodiment the valve core is a Presta-pattern valve core.

**"core body"** As used herein, the "core body" is the component of the valve core, threaded into the stem bore, that carries the deflectable ring element against an internal shoulder and guides the poppet.

**"seat ring"** As used herein, a "seat ring" means a deflectable ring element that both provides a sealing edge on which the sealing face of the poppet seats in the closed state, and is deflected by the purge shoulder during over-travel to open the purge gap. In the illustrated embodiment the seat ring is formed from a superelastic alloy with a convoluted wall; in other embodiments it is formed from a resilient polymer.

**"deflectable ring element"** As used herein, a "deflectable ring element" means any annular element, carried by the valve core, that the purge shoulder deflects radially during over-travel so as to open a purge flow path, and that undergoes shape recovery toward its at-rest form when the pressure differential falls. A deflectable ring element is a seat ring, where the same element also provides the sealing edge, or, in embodiments having a separate fixed seat, a wiper ring.

**"wiper ring"** As used herein, a "wiper ring" means a deflectable ring element, separate from a fixed seat, positioned so that the purge shoulder deflects it outward during over-travel to open the purge gap, while the fixed seat performs the sealing function of the valve core.

**"fixed seat"** As used herein, a "fixed seat" means a valve seat member of the valve core that does not deflect during over-travel and that provides the sealing edge on which the sealing face of the poppet seats, used together with a wiper ring.

**"convoluted wall"** As used herein, a "convoluted wall" means a wall of the seat ring formed with one or more shallow convolutions, which converts axial load applied by the purge shoulder into radial deflection of the seat ring.

**"purge shoulder"** As used herein, a "purge shoulder" means the formation of the poppet, on the chamber side of the sealing face, that contacts the deflectable ring element only during over-travel and thereby deflects it radially to open the purge gap.

**"second spring stage"** As used herein, the "second spring stage" means the stage of the return spring having a higher rate than the first spring stage, which the pressure differential must overcome, once the normal stroke is complete, to produce over-travel, and which thereby sets the over-travel threshold.

**"supply side"** As used herein, the "supply side" of the poppet means the side coupled to the inflation device, replacing orientation-dependent description.

**"chamber side"** As used herein, the "chamber side" of the poppet means the side open to the inflatable chamber, replacing orientation-dependent description.

**"inflatable chamber"** As used herein, an "inflatable chamber" means the volume, inflated through the inflation valve and holding liquid sealant, of a bicycle inner tube or of a tubeless bicycle tyre set-up.

**"pressure differential"** As used herein, the "pressure differential" means the supply-side pressure less the chamber-side pressure across the poppet.

**"crack pressure"** As used herein, the "crack pressure" means the pressure differential at which the poppet begins its normal stroke, overcoming the first spring stage.

**"over-travel threshold"** As used herein, the "over-travel threshold" means the pressure differential above which the poppet moves beyond the normal stroke into over-travel, overcoming the second spring stage.

**"normal stroke"** As used herein, the "normal stroke" means the displacement of the poppet from the closed state, at and above the crack pressure and below the over-travel threshold, over which the purge shoulder does not contact the deflectable ring element.

**"over-travel"** As used herein, "over-travel" means movement of the poppet beyond the normal stroke, occurring when the pressure differential exceeds the over-travel threshold, during which the purge shoulder bears on the deflectable ring element.

**"over-travel distance"** As used herein, the "over-travel distance" means the axial distance the poppet moves beyond the end of the normal stroke during over-travel.

**"radial deflection"** As used herein, "radial deflection" means elastic deformation of the deflectable ring element, produced by the purge shoulder during over-travel, that opens the purge gap. In the illustrated embodiment the radial deflection is outward.

**"purge gap"** As used herein, the "purge gap" means a clearance, associated with the deflectable ring element, that is closed in the closed state and in the normal-open state and that is opened by radial deflection of the deflectable ring element in the purge state, through which the air purge flows. In the illustrated embodiment the purge gap is an annular radial clearance between the outer surface of the seat ring and the core body bore.

**"purge flow path"** As used herein, the "purge flow path" means the path, distinct from the main passage, from the supply side through the purge gap to the inflatable chamber, along which the air purge travels.

**"purge gap opening"** As used herein, the "purge gap opening" means the radial size of the purge gap when the deflectable ring element is fully deflected in the purge state.

**"closed state"** As used herein, the "closed state" means the condition of the valve core, below the crack pressure or with the lock nut engaged, in which the sealing face of the poppet rests on the sealing edge of the deflectable ring element and the purge gap is closed.

**"purge state"** As used herein, the "purge state" means the condition of the valve core, occurring when the pressure differential exceeds the over-travel threshold, in which the poppet is in over-travel, the deflectable ring element is in radial deflection, the purge gap is open, and the air purge occurs.

**"air purge"** As used herein, the "air purge" means the flow of inflation gas, at the pressure of the inflation device, along the purge flow path during the purge state, across the surfaces of the valve core on which sealant film accumulates and into the inflatable chamber.

**"snap-back wipe"** As used herein, the "snap-back wipe" means the movement of the deflectable ring element across a surface of the poppet as the ring element undergoes shape recovery when the pressure differential falls below the over-travel threshold, by which movement partially cured sealant film is sheared from that surface.

**"sealant film"** As used herein, "sealant film" means liquid sealant that has dried or cured, in whole or in part, on a surface of the valve core.

**"liquid sealant"** As used herein, "liquid sealant" means a fluid, carried in the inflatable chamber, that is drawn into the valve core on inflation and that is capable of drying or curing on the surfaces of the valve core; in the tested embodiment the liquid sealant is a latex emulsion containing ammonia and suspended particles.

**"blockage"** As used herein, "blockage" means a failure mode of the valve core in which sealant film prevents the poppet from opening within a defined response time of actuation by the inflation device.

**"inflation event"** As used herein, an "inflation event" means the period from coupling of an inflation device to the supply side until the inflation device is removed.

**"inflation cycle"** As used herein, an "inflation cycle" means one repetition of an inflation event, a hold period at the resulting chamber pressure, and deflation of the inflatable chamber.

**"superelastic alloy"** As used herein, a "superelastic alloy" means an alloy that recovers large elastic strains on unloading, at the service temperature of the inflation valve, by a reversible phase transformation between martensite and austenite; in the illustrated embodiment the superelastic alloy is nickel-titanium of nominally 55.8 wt% nickel content.

**"austenite finish temperature"** As used herein, the "austenite finish temperature" means the temperature above which the superelastic alloy of the deflectable ring element is fully austenitic and exhibits superelastic behaviour.

**"martensite start temperature"** As used herein, the "martensite start temperature" means the temperature, on cooling the superelastic alloy of the deflectable ring element, below which martensite begins to form and superelastic recovery may be impaired.

**"seat ring wall thickness"** As used herein, the "seat ring wall thickness" means the radial thickness of the material forming the convoluted wall of the seat ring.

**"seat ring free length"** As used herein, the "seat ring free length" means the axial length of the seat ring in its unloaded, at-rest condition.

**"convolution amplitude"** As used herein, the "convolution amplitude" means the radial excursion of a convolution of the convoluted wall, measured from the mean radius of the wall to the peak or trough of the convolution.

**"thermally actuated purge"** As used herein, a "thermally actuated purge" means opening of the purge gap by warming the deflectable ring element above an austenite finish temperature selected for manual actuation, rather than by over-travel; this is described herein as a separate, considered concept, not as a species of the over-travel-actuated purge state.

**"leak-down"** As used herein, "leak-down" means the loss of pressure from the inflatable chamber, through the valve core, over a hold period.

**"inflation time"** As used herein, "inflation time" means the elapsed time, using a given inflation device, from coupling to the supply side until the inflatable chamber reaches a stated pressure.

**"conventional valve core"** As used herein, a "conventional valve core" means a valve core lacking a deflectable ring element and a purge gap as defined herein, used as a comparator in the working examples.

#### General construction

**Comprising.** As used herein, "comprising" and "comprises" are open transitional terms: a valve core, seat ring, or other element or combination that "comprises" a set of recited components or steps may include additional, unrecited components or steps, and is not limited to those recited.

**Optionality.** Language such as "in some embodiments," "in other embodiments," "optionally," and "may" identifies a feature as preferred rather than essential to every embodiment described herein. The absence of such language for a given feature does not, by itself, make that feature essential; essentiality is determined from the description as a whole and, for a claimed combination, from the claim.

**Singular and plural.** As used herein, "a" and "an" mean "one or more" unless the context clearly requires otherwise. For example, "a convolution" of the convoluted wall encompasses an embodiment having a single convolution and an embodiment having two or more convolutions, and "a purge shoulder" encompasses a purge shoulder that contacts the deflectable ring element at a single location or at two or more locations around its circumference.

**Direct and indirect coupling.** Unless expressly qualified as "directly," terms describing the relationship between components — including "carried by," "coupled to," "on," "against," and "bears on" — encompass both a direct connection or contact and an indirect connection or contact through one or more intervening components. For example, a purge shoulder "on the poppet" encompasses a purge shoulder integral with the poppet and a purge shoulder formed on a separate collar fixed to the poppet.

**Ranges and endpoints.** Unless stated otherwise, a numerical range disclosed herein is inclusive of its stated endpoints, and disclosure of a range constitutes disclosure of every value and every narrower sub-range falling within it. A range described as "believed" reflects the inventor's estimate at the time of this application and is not represented as having been tested outside the specific value or values reported in the working examples.

**About/approximately.** As used herein, "about" or "approximately," applied to a stated value, accounts for ordinary variation arising from manufacturing tolerance and measurement, consistent with the level of precision of the surrounding disclosure; it does not itself define a specific numerical tolerance unless one is separately stated. For example, "approximately 0.03 mm" describes the interference fit of the working example without asserting a measured tolerance band, and "nominally 55.8 wt%" describes the alloy composition of the working example without asserting a measured compositional tolerance.

**Order of steps.** Where this specification describes a sequence of states or events — for example, the closed state, the normal stroke, over-travel and the purge state, and recovery — that description identifies the pressure differential at which each state or event occurs and does not require that the states or events be discrete, mutually exclusive, or performed only in the order presented, except where the description or the context makes a particular order necessary (for example, over-travel necessarily follows completion of the normal stroke as the pressure differential rises).

**Functional terminology.** Certain terms used herein combine a generic structural term with a statement of function — for example, "deflectable ring element," "threshold-setting arrangement" (of which the second spring stage is the disclosed species), and "biasing member" (of which the return spring is the disclosed species). Each such term refers to any structure capable of performing the recited function, consistent with the corresponding structures described in this specification and their equivalents; this specification describes at least one corresponding structure for each such term so used.

## Rationale

**Ceiling on genus breadth.** Several locked terms (deflectable ring element, purge gap, radial deflection, purge shoulder, second spring stage) already carry direction-neutral or material-neutral functional descriptions in `terminology/LOCKED.md`, produced at Gate 1. I drafted each definition to the breadth already committed to there — no further, no less. The Phase 3 design-around register (`CONFIRMED.md`, from `11.md`) and equivalent architecture library (from `12.md`) propose materially broader genus language for several of these terms (for example, DA-2's proposal to define the purge gap purely by function so as to cover inward, axial and tilting deflection at any bounding surface, or DA-6's proposal to extend "valve core" to Schrader- and Dunlop-pattern valves). I did not import that broader language into these definitions, because in every such instance the register itself records the point as "needs inventor confirmation" against a still-open Gate 1 question (01 Q1, Q2, Q6, Q7, Q12, Q20, Q26), and `03.md`'s own enablement caution says the nucleus "cannot be written up as enabled" until the purge-gap mechanism is resolved. Widening these definitions now would draft breadth into the reservoir that the dossier has not yet shown is enabled, contrary to the audit discipline this role owns (Prompt 17 gate). The genus/species architecture the register recommends is recorded as unfinished business for Claims Architect and for Prompt 17, not silently pre-empted here.

**"deflectable ring element" and "wiper ring" are Phase 1 material, not Phase 3 candidates.** Both the seat ring and the wiper ring species trace to the inventor's own §6 alternatives (Alternative A, Alternative B), captured in `01.md` (f) and locked in Gate 1's own species column. They are used here on that basis, not on the strength of the Phase 3 equivalent-architecture library.

**Purge gap and radial deflection kept direction- and location-neutral at the genus level.** `01.md`/`03.md` record an unresolved inconsistency between §2 ("stem bore," "flexes radially outward") and §3(6) ("core body bore"), which the interference fit of §7 does not obviously reconcile. Rather than pick a reading, I defined both terms functionally (closed at rest, opened by deflection during over-travel) and gave the §3(6) reading only as "the illustrated embodiment." This is consistent with `03.md`'s own treatment and avoids asserting a resolved mechanism the dossier does not support.

**"closed state" left silent on purge-gap airtightness.** Whether the closed purge gap must itself be airtight, or whether the sealing face is the sole seal, is open (01 Q31; `CONFIRMED.md` FM-22 records only a working assumption, not an inventor confirmation). The definition attributes sealing in the closed state to the sealing face and says nothing about the purge gap's own tightness, so the definition does not foreclose either reading.

**"second spring stage" not widened to a threshold-setting genus.** The equivalent architecture library (`12.md`, section 2) and the design-around register (DA-11) both propose a broader "threshold-setting arrangement" genus covering detents, auxiliary springs and ring-stiffness thresholds. I named that genus in the functional-terminology paragraph, because it is already present in `terminology/LOCKED.md`'s own "Broader" column for this term, but I did not define "second spring stage" itself as anything other than the disclosed two-rate-spring species, because whether any other threshold-setting means was conceived is still open (01 Q6, Q7).

**Measurement conventions supplied for undefined dimensional terms.** "Seat ring wall thickness," "seat ring free length" and "convolution amplitude" are flagged in `terminology/LOCKED.md` as needing definition, but no measurement method is given in the disclosure. I supplied the ordinary mechanical meaning of each (radial material thickness; unloaded axial length; peak-to-trough radial excursion from the mean wall radius) rather than leaving the term undefined, since this is consistent with ordinary technical usage and does not narrow or contradict any embodiment.

**Genus terms used without a `new_terms` entry.** "Threshold-setting arrangement," "deflecting formation," "resilient member" and "biasing member" appear only in the "Broader" column of `terminology/LOCKED.md` against their respective preferred terms; they are used above solely to state the genus-species relationship required by the functional-terminology construction paragraph, and are declared in `new_terms` below out of caution even though they originate in the locked table itself.

**Terms not defined.** I did not add definitions beyond the rows marked "Needs definition: yes." "Number of convolutions," "interference fit," "nickel content" and similar rows are marked "no" in the locked table and are adequately conveyed by their ordinary meaning together with the values given in the working example.

## Assumptions

A1. Genus-level definitions (deflectable ring element, purge gap, radial deflection, purge shoulder, second spring stage) are capped at the breadth already committed to in `terminology/LOCKED.md`'s genus/species/functional-description columns; broader candidate genus language proposed only in the Phase 3 design-around register and equivalent architecture library is not imported here because it remains tied to unresolved Gate 1 questions. Blocking: P4 (Prompt 16/18 and the Prompt 17 enablement audit must decide, with the inventor's answers, whether any of this definition set should be widened before the Description issues).

A2. "Closed state" is defined without taking a position on whether the closed purge gap must itself be airtight (01 Q31 open); sealing in the closed state is attributed to the sealing face only. Not blocking for this deliverable; blocks P4 (Prompt 17) if the enablement audit needs a settled position.

A3. "Radial deflection" and the illustrated species for "purge gap" follow the outward-deflection, outer-surface reading, as the reading best consistent with the bench-test finding of film on the ring's outer surface (per `01.md`/`03.md`), while the primary (genus) definitions remain direction- and location-neutral. Not blocking.

A4. "Pressure differential" is defined as supply-side pressure less chamber-side pressure, carrying forward `01.md` assumption A3 (inferred, not stated in the disclosure). Blocking: P4, P5 (carried forward from Phase 1, unchanged).

A5. Measurement conventions for seat ring wall thickness, seat ring free length and convolution amplitude are given their ordinary mechanical meaning because the dossier specifies none. Not blocking for this deliverable; relevant to Prompt 20/20a figure instructions, which should show the measurement basis.

## Open Questions

Q1. The purge gap's location and opening mechanism remain unresolved (01 Q1, Q2): §2 places it at the stem bore and describes outward flexing, §3(6) places it at the core body bore, and the §7 interference fit is not obviously reconcilable with either. The definitions of "purge gap" and "radial deflection" are kept functional and direction-neutral pending this answer. Blocks P4 (the Prompt 17 enablement audit cannot confirm this element is enabled without it).

Q2. Whether the closed purge gap must itself be airtight, or whether the sealing face is the sole seal in the closed state (01 Q31), is unanswered. The "closed state" definition is deliberately silent on this point. Blocks P4.

Q3. Whether the second spring stage is the only threshold-setting means the inventor conceived, or whether another arrangement (an auxiliary spring, a detent, or the seat ring's own stiffness, per `CONFIRMED.md` DA-11 and the equivalent-architecture library) is also within the invention (01 Q6, Q7), is unanswered. This determines whether "threshold-setting arrangement" should become a defined genus term of its own, rather than only a cross-reference, in a later revision. Blocks P4, P5.

Q4. Whether the inventor confirms the PEEK seat ring and the fixed-seat-and-wiper-ring architecture (§6 Alternatives A and B) as within the invention (01 Q20) affects how far the "seat ring"/"wiper ring" species pairing drafted here can be relied on for claim support. Blocks P4, P5.

Q5. No measurement method is specified in the disclosure for seat ring wall thickness, seat ring free length or convolution amplitude (01 Q32 is adjacent but does not resolve this). The ordinary mechanical meaning used here should be confirmed, or a measurement method supplied, before the figures (Prompt 20/20a) are finalised. Blocks P4.

```json
{
  "prompt": "19",
  "status": "complete",
  "assumptions": [
    {"id": "A1", "text": "Genus-level definitions are capped at the breadth already committed to in terminology/LOCKED.md; broader Phase 3 candidate genus language tied to unresolved Gate 1 questions is not imported.", "blocking": true},
    {"id": "A2", "text": "\"Closed state\" is defined without taking a position on whether the closed purge gap must itself be airtight (01 Q31 open).", "blocking": false},
    {"id": "A3", "text": "\"Radial deflection\" and the illustrated purge-gap species follow the outward-deflection, outer-surface reading, while the genus definitions remain direction- and location-neutral.", "blocking": false},
    {"id": "A4", "text": "\"Pressure differential\" is defined as supply-side pressure less chamber-side pressure, carrying forward 01.md assumption A3.", "blocking": true},
    {"id": "A5", "text": "Measurement conventions for seat ring wall thickness, free length and convolution amplitude are given their ordinary mechanical meaning because the dossier specifies none.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "Purge gap location and opening mechanism unresolved (01 Q1, Q2); definitions kept functional and direction-neutral pending the answer.", "blocks": ["P4"]},
    {"id": "Q2", "text": "Whether the closed purge gap must itself be airtight, or the sealing face is the sole seal (01 Q31), is unanswered.", "blocks": ["P4"]},
    {"id": "Q3", "text": "Whether the second spring stage is the only threshold-setting means conceived, or a broader genus should be defined (01 Q6, Q7).", "blocks": ["P4", "P5"]},
    {"id": "Q4", "text": "Whether Alternatives A (PEEK seat ring) and B (fixed seat plus wiper ring) are confirmed within the invention (01 Q20).", "blocks": ["P4", "P5"]},
    {"id": "Q5", "text": "No measurement method is given for seat ring wall thickness, free length or convolution amplitude; ordinary mechanical meaning is assumed pending confirmation.", "blocks": ["P4"]}
  ],
  "new_terms": [
    {"term": "threshold-setting arrangement", "maps_to": "second spring stage", "reason": "Genus term already recorded in terminology/LOCKED.md's Broader column for \"second spring stage\"; used here only in the functional-terminology construction paragraph to state the genus-species relationship."},
    {"term": "deflecting formation", "maps_to": "purge shoulder", "reason": "Genus term already recorded in terminology/LOCKED.md's Broader column for \"purge shoulder\"; used only for the direct/indirect coupling example."},
    {"term": "resilient member", "maps_to": "deflectable ring element", "reason": "Genus term already recorded in terminology/LOCKED.md's Broader column for \"deflectable ring element\"; not used as a headword, cited only in Rationale."},
    {"term": "biasing member", "maps_to": "return spring", "reason": "Genus term already recorded in terminology/LOCKED.md's Broader column for \"return spring\"; used in the functional-terminology construction paragraph as a second example."}
  ],
  "support_refs": [
    {"item": "valve core definition", "support": "terminology/LOCKED.md row \"valve core\"; intake/disclosure.md §3(1)-(7)"},
    {"item": "core body definition", "support": "terminology/LOCKED.md row \"core body\"; intake/disclosure.md §3(2)"},
    {"item": "seat ring definition", "support": "terminology/LOCKED.md row \"seat ring\"; intake/disclosure.md §2, §3(3)-(4)"},
    {"item": "deflectable ring element definition", "support": "terminology/LOCKED.md row \"deflectable ring element\"; intake/disclosure.md §2, §6 (Alternatives A, B)"},
    {"item": "wiper ring definition", "support": "terminology/LOCKED.md row \"wiper ring\"; intake/disclosure.md §6 Alternative B"},
    {"item": "fixed seat definition", "support": "terminology/LOCKED.md row \"fixed seat\"; intake/disclosure.md §6 Alternative B"},
    {"item": "convoluted wall definition", "support": "terminology/LOCKED.md row \"convoluted wall\"; intake/disclosure.md §3(3)"},
    {"item": "purge shoulder definition", "support": "terminology/LOCKED.md row \"purge shoulder\"; intake/disclosure.md §2, §3(4)"},
    {"item": "second spring stage definition", "support": "terminology/LOCKED.md row \"second spring stage\"; intake/disclosure.md §3(5)"},
    {"item": "supply side / chamber side definitions", "support": "terminology/LOCKED.md rows \"supply side\", \"chamber side\"; P1/01.md assumptions A3-A5"},
    {"item": "inflatable chamber definition", "support": "terminology/LOCKED.md row \"inflatable chamber\"; intake/disclosure.md §1"},
    {"item": "pressure differential definition", "support": "terminology/LOCKED.md row \"pressure differential\"; P1/01.md assumption A3"},
    {"item": "crack pressure / over-travel threshold definitions", "support": "terminology/LOCKED.md rows \"crack pressure\", \"over-travel threshold\"; intake/disclosure.md §2, §4"},
    {"item": "normal stroke / over-travel / over-travel distance definitions", "support": "terminology/LOCKED.md rows \"normal stroke\", \"over-travel\", \"over-travel distance\"; intake/disclosure.md §2, §4"},
    {"item": "radial deflection definition", "support": "terminology/LOCKED.md row \"radial deflection\"; intake/disclosure.md §2"},
    {"item": "purge gap / purge flow path / purge gap opening definitions", "support": "terminology/LOCKED.md rows \"purge gap\", \"purge flow path\", \"purge gap opening\"; intake/disclosure.md §2, §3(6); intake/drawings/README.md FIG-2"},
    {"item": "closed state / purge state definitions", "support": "terminology/LOCKED.md rows \"closed state\", \"purge state\"; P1/01.md (i) state table"},
    {"item": "air purge / snap-back wipe definitions", "support": "terminology/LOCKED.md rows \"air purge\", \"snap-back wipe\"; intake/disclosure.md §2"},
    {"item": "sealant film / liquid sealant definitions", "support": "terminology/LOCKED.md rows \"sealant film\", \"liquid sealant\"; intake/disclosure.md §1, §5"},
    {"item": "blockage / inflation event / inflation cycle / leak-down / inflation time / conventional valve core definitions", "support": "terminology/LOCKED.md corresponding rows; intake/disclosure.md §8; intake/data/bench-test.md"},
    {"item": "superelastic alloy / austenite finish temperature / martensite start temperature definitions", "support": "terminology/LOCKED.md corresponding rows; intake/disclosure.md §2, §4, §5"},
    {"item": "seat ring wall thickness / free length / convolution amplitude definitions", "support": "terminology/LOCKED.md corresponding rows; intake/disclosure.md §4; ordinary mechanical meaning (A5)"},
    {"item": "thermally actuated purge definition", "support": "terminology/LOCKED.md row \"thermally actuated purge\"; intake/disclosure.md §6; P1/03.md (kept outside N0 nucleus)"},
    {"item": "general construction paragraphs (comprising, optionality, singular/plural, coupling, ranges, about, order of steps, functional terminology)", "support": "terminology/LOCKED.md drafting notes (relative-term and §112(f) notes); AGENTS.md Prompt 19 instructions"}
  ],
  "disclosure_requests": [],
  "open_disagreements": [],
  "narrowing_suggested": []
}
```
````

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/21.md`

````markdown
## Deliverable

### Claim-Family Architecture

This is a drafting and analysis aid prepared by AI. It is not legal advice and says nothing about patentability; qualified patent counsel signs off before anything is filed.

**Basis.** The description does not yet exist. Every disclosure basis below is cited to the inventor's disclosure (§1–§9 via `01` and `03`), to `CONFIRMED.md` (11–15, confirmed unattended at Gate 2) and to the blueprint section ids of `16` that the description is being drafted to. Paragraph anchors are mapped in P5d against the stitched description. Commercial basis is cited to the ranks of `02`. The distinctions relied on are rows 1–3 of `09`, tested only against the 17 references charted in `07`, a thin pile containing two fictional documents (07 Q1, Q2).

**The one relationship every product-facing family carries.** A deflectable ring element that is clear of the poppet's deflecting formation throughout the normal stroke, is deflected only in over-travel above an over-travel threshold higher than the crack pressure, and thereby opens a purge gap that is closed in the closed state and the normal-open state (09 rows 1 and 2; 08 "What the attack shows" item 1). Families A, C and D are different perimeters around that relationship. Families B and E protect the seat ring as a part and its manufacture, which do not inherit that relationship and are the most exposed (08, value-map rank 2 row).

| Family | Justified | Commercial basis (02 rank) | Disclosure basis | Intended independent claim concept | Jurisdiction notes |
|---|---|---|---|---|---|
| **A. Valve core (apparatus)** | **Yes** | Rank 1: the sellable, swappable unit; conventional cores already sold in multipacks (§1); bench data 40 cycles against 12–18 | §2, §3(2)–(6), §4 via 01 (d), (i); 03 N0 (a)–(e), C2–C8, C18; CONFIRMED 11 findings 1–3, DA-2, DA-4, DA-5; 12 §2–§4, §7, §9; 16 S7.3–S7.7, S8.1–S8.8, S9.1–S9.7, S17 CF-A | A valve core whose deflectable ring element is carried by the core body and whose poppet carries a deflecting formation; normal stroke with the formation spaced from the ring element; over-travel above a higher over-travel threshold deflects the ring element; a purge gap bounded partly by the ring element, closed in the closed state and the normal-open state, opened by the radial deflection to give a purge flow path separate from the main passage; shape recovery closes it. The valve stem is not an element; no material, no numbers, no sealant, no wipe | Lead claim in all three jurisdictions. US: "deflectable ring element" and "deflecting formation" pair a generic noun with a function and may be read under 35 U.S.C. §112(f); the description must give the corresponding structures (16 S7.4, S7.6, S10, S11.3). EPO/UK: functional definition of the purge gap is acceptable if the state definitions are clear (16 S7.3, S7.5); relative terms avoided |
| **B. Deflectable ring element / seat ring (component)** | **Yes, with the exposure stated** | Rank 2: catches a component supplier who never sells a complete core; rank 5 genus for the polymer line | §3(3), §4, §5, §7 via 01; 03 N2–N4, C10, C12, C14, C21; CONFIRMED 12 §4, §5, §12, §13; 13 Table 1; 16 S7.4, S7.9, S7.10, S10.1–S10.7, S17 CF-B | A seat ring having a sealing edge at one axial end and a convoluted wall that converts axial load into radial deflection and recovers elastically, within the §4 dimensional envelope. Material and austenite finish temperature in dependents | Does not inherit the family A distinctions. US9982818B2 (wave-profile NiTi sealing ring) is the closest art: 08 rates the claim *strong* if defined by material and wave wall only, *moderate* with the sealing edge, dimensions and axial-load conversion. "For a valve core" is read as "suitable for" at the EPO and as intended use in the US, so the sealing edge and dimensions must do the work. Numbers in the independent claim are avoidable by tolerance (d2 R11); accepted here because the family cannot otherwise be distinguished. Unity with A at the EPO rests on the seat ring being a special technical feature of both; an a-posteriori unity objection is possible |
| **C. Inflation valve (valve stem carrying the mechanism), with inner tube, tubeless tyre and wheel dependents** | **Yes** | Rank 3: OEM channel (tube, tyre, wheel makers integrating the valve without selling a spare core); d2 R6 (mechanism moved into the stem) | §1, §3(1) via 01; CONFIRMED 12 E16.3, E14.6, E16.2; 11 DA-6; 16 S8.1, S8.2, S11.9, S16, S17 CF-C | An inflation valve in which the deflectable ring element and the poppet are carried by the valve stem, directly or by a core body received in the stem bore, with the family A relationship; dependents for the removable valve core of family A, Schrader-pattern and Dunlop-pattern formats, and the inner tube, tubeless tyre and wheel incorporating the valve | The direct-carriage species (no core body) is an engineering candidate confirmed unattended (16 A4); the inventor has not stated it (11 Q6). Human review at Gate 3 decides whether claim 2 keeps the direct-carriage limb. Same §112(f) note as A. EPO unity with A is clear (same special technical feature) |
| **D. Method of use (inflating an inflatable chamber holding liquid sealant)** | **Yes, as a supporting family** | Rank 8: weak against riders, but it is where the behaviour that a teardown cannot show is proven (d2 §7 item 3; R4, R5, R7), and it recites the sealant context that the apparatus claims deliberately omit (d2 R19) | §2, §8 via 01 (d) S1–S5, (i); bench data; CONFIRMED 12 E1.1, E8.1, E8.5, E9.1; 16 S9.1–S9.9, S13.1, S17 CF-D | Coupling an inflation device; raising the pressure differential to the crack pressure (normal-open state, flow through the main passage); raising it above the over-travel threshold (purge state, air purge into the inflatable chamber); removing the inflation device (shape recovery closes the purge gap). Snap-back wipe in a dependent | Direct infringers are end users; the commercial value is inducement or contributory liability against a seller who instructs use with sealant (US), and the EPO/UK equivalents. Over-travel and purge gap opening were inferred from an audible snap, never measured (01 Q23): evidence of the method is indirect. Counsel to decide whether to assert |
| **E. Method of manufacturing the seat ring (with assembly into the core body as a dependent step)** | **Yes, as a fallback family** | Rank 4: catches a NiTi subcontractor using this route; useful where the finished ring is made abroad or is hard to reverse-engineer | §7 via 01 (j); 03 C23–C25; CONFIRMED 12 §14, §15; 11 DA-21; 16 S12.1–S12.5, S17 CF-E, CF-F | Providing tube stock of a superelastic alloy; laser cutting the seat ring blank with a sealing edge; forming the convoluted wall; shape-setting in a fixture holding the convoluted wall geometry and quenching. Electropolishing, the 500 °C / 10 min point, the austenite finish temperature and pressing into the core body against the internal shoulder in dependents | 08 rates inventive step *moderate to strong* once the ring is known: the claim survives through the product it makes. Which step forms the convolution is unstated (01 Q11), so the forming step is claimed generically. US restriction between A, B, D and E is likely; EPO unity between E and B is clear, between E and A only via the seat ring |
| F. Method of assembling the valve core | No, as a separate family | Rank 4 (same channel as E) | §7; CONFIRMED 12 §14; 15 FM-6, FM-7 | Folded into E as a dependent step (pressing the seat ring into the core body against the internal shoulder with an interference fit) and into the A ladder (ring retention species) | A separate independent claim would add volume without a second commercial target |
| G. Product-by-process (seat ring obtainable by E) | No, for the first filing | Rank 2 (same product as B) | §7; 16 CF-G | The seat ring is definable structurally (family B), so product-by-process adds nothing now. Kept as an omnibus candidate for Prompt 27 | EPO/UK: product-by-process is the product as such and allowed only where structural definition is impossible. US: the product regardless of process for infringement |
| H. Split architecture (fixed seat plus wiper ring) | No, as a family; yes, as dependents | Rank 6: the inventor's own design-around | §6 Alternative B via 01 F4; CONFIRMED 12 E4.2, E4.6, E10.2; 14 E-III; 16 S10.5, S17 CF-H | Covered by the deflectable ring element genus in A and C; a dependent claim recites the fixed seat and the wiper ring | Claimed alone it is a scraper behind a seat and meets d2 R16/R17 and 08 (ref-01 + US4719938A). Form, thickness and retention of the wiper ring are unstated (01 Q20) |
| I. Materials genus and species (superelastic alloy, resilient metal, resilient polymer, austenite finish temperature) | No, as a family; yes, as dependents of A, B and C | Rank 5 (polymer line); rank 2 | §2, §4, §5, §6; CONFIRMED 12 §12, §13; 14 sentences 1, 2, 6; 16 S10.1, S10.7 | Ladder rungs, with the austenite finish temperature conditioned on the superelastic species (14 footnotes [g], [h]) | 08 rates the superelastic increment *strong* for obviousness; 09 row 4 rates it *high* design-around. Never in an independent claim |
| J. Threshold-setting arrangement (second spring stage and the S11.4 species; threshold equal to crack pressure) | No, as a family; yes, as dependents | Rank 7 | §3(5); CONFIRMED 12 §2; 11 DA-1, DA-11; 16 S7.7, S8.6, S9.3, S11.4 | The independent claims state the threshold as a relationship (over-travel threshold higher than the crack pressure); the structure that sets it is a dependent genus with the second spring stage as a species | Whether the two-stage return spring is the only arrangement conceived is open (01 Q6); the description must give more than one structure for §112(f) |
| K. Kit and replacement valve core (seat ring alone; seat ring with poppet and return spring) | No, for the first filing | Rank 1 (replacement valve core is family A itself); DA-19 rated low–medium plausibility | §1 ("multipack"); CONFIRMED 11 DA-19; 14 CB5; 16 S11.10 | The replacement valve core is family A without the valve stem. A kit of separately supplied parts is deferred to Prompt 27 as a sub-combination candidate; the seat ring alone is family B | Commercial intent unknown (02 Q1; 01 Q33). Conventional core bodies are not designed to come apart (11 DA-19) |
| L. Corrosion-resistant body (stainless 303; polymer core body) | No, as a family; yes, as dependents | Rank 9 | §5 F1; CONFIRMED 14 CB2; 15 FM-18; 16 S8.3, S11.7 | Dependent of A and C | Stainless body machined but not tested (01 Q18) |
| M. Thermally actuated purge (two-way shape-memory ring) | No | Rank 10: inventor doubtful, no data | §6 F5; CONFIRMED 12 E9.5; 03 C32; 16 S11.11 | Outside the nucleus (it removes over-travel). Continuation candidate at most (Prompt 27), if the inventor keeps it (03 Q12) | Heat-driven radial movement of a shape-memory ring is known (US9982818B2 claim 5; 08) |
| Composition / material | No | None | None | The superelastic alloy is a purchased material; no compositional novelty is disclosed (16) | — |
| Consumable | No | None (02 A4) | None | The liquid sealant is a third-party product | — |
| Controller, software, computer-implemented or data-processing method | No | None | None | The mechanism is wholly mechanical (01 (i)) | — |
| System (inner tube, tubeless tyre, wheel, bicycle incorporating the inflation valve) | Yes, as dependents of C, not a separate family | Rank 3 | §1, §6; CONFIRMED 12 §16; 16 S11.9 | "An inner tube / a tubeless tyre / a wheel comprising the inflation valve of claim 2" | The increment is known (US11179979B2 claim 12; US11065925B2 claim 7; 08); the claims inherit the C distinctions and add no inventive weight, which is their purpose |

**Claim count.** Five independent claims (A, B, C, D, E) in Prompt 22. US excess-claim fees apply above three independent claims and twenty claims in total; counsel may prune B or E for the US filing, or keep them for the EPO/UK filing where the fee structure differs. Restriction in the US between the apparatus (A, C), the component (B), the method of use (D) and the method of manufacture (E) is likely; the family structure is drafted so that each restricted group stands on its own.

## Rationale

**Why A leads and why the valve stem is not in it.** Rank 1 of `02` and the §1 multipack market make the replacement valve core the product a competitor would sell first. Claiming the core without the stem reaches that competitor; claim C reaches the OEM who never sells a core (d2 R6). Neither is achieved by a single claim, so both are drafted.

**Why B is justified despite its exposure.** A component supplier who sells only the seat ring practises none of the family A relationships, and the ring is where the measured effect resides (02 rank 2). The exposure to US9982818B2 is real; it is met by the sealing edge, the axial-load conversion and the §4 envelope, and stated plainly so that counsel can drop the family if the search widens.

**Why D is kept at all.** Litigator's point in d2 §7 item 3 outweighs the rank-8 detectability concern: a section of a competitor's product proves nothing about thresholds, flow or recovery, and the method claim is the only claim in which that behaviour is the infringing act. It also carries the sealant context that the apparatus claims omit to defeat the "tubes only" label (R19).

**Why E survives and F, G, K do not.** E has one commercial target (the NiTi subcontractor) that no other family reaches. F, G and K each duplicate a target already reached by A, B or E, and DA-19 rates the kit route low–medium. They are recorded as Prompt 27 candidates rather than drafted.

**Why H, I, J and L are dependents.** Each is either the inventor's own named design-around (H, I), a known or obvious increment (I, J per 08), or a product-line variant (L). They belong on the ladder, where each is a meaningful fallback, not in an independent claim, where each would be a limitation a competitor omits at no cost.

**Conflict resolved.** `02` rank 8 recommends the method of use as an apparatus "configured to" dependent only; d2 recommends use claims for behaviour. I followed d2 because the "configured to" form already sits in claim 1 as the state relationships, and the method claim adds the sealant context and a provable act.

## Assumptions

A1. No Gate 1 answers exist. 01 Q1/Q2 (purge gap location and opening), 03 Q1 (air purge against snap-back wipe), 03 Q3 (purge on every opening) and 03 Q5 (Alternatives A and B) are treated as unanswered; the families follow `03` (air purge essential, wipe advantageous) and `09` rows 1–2. Blocking for P5 (25, 28) and REVIEW.

A2. Gate 2 was confirmed unattended. Family C's direct-carriage limb (12 E16.3), the deflecting formation genus (11 DA-4) and the functional purge gap genus (11 DA-2) are engineering candidates confirmed by code, not inventor statements; the families use them as `CONFIRMED.md` permits, subject to human review at Gate 3 (16 A4). Blocking for PACKAGE.

A3. The description will follow the section ids of `16`; disclosure bases are cited to those ids and the paragraph anchors are mapped in P5d. Not blocking.

A4. The pressure differential is the supply-side pressure less the chamber-side pressure (01 A3; 19 A4). Not blocking for 21.

A5. ref-01 and ref-02 (fictional) are treated as prior art for the distinction test, with the real-art counterparts (US4462449A, EP1137892A1) carrying the same conclusions (08 A2). Not blocking for P5; blocking for PACKAGE (07 Q2).

## Open Questions

Q1. Where is the purge gap and how does it open against the interference fit (01 Q1, Q2)? Families A, C and D define the purge gap by function pending the answer; if no separate purge gap can be enabled, A and C must fall back to the wipe-based nucleus of `03` and the family map changes. Blocks P5, REVIEW.

Q2. Does the air purge alone, the snap-back wipe alone, or both produce the effect (03 Q1)? Decides whether the purge gap (family A as drafted) or the wipe carries the independent claims. Blocks P5.

Q3. Would purging on every opening work (03 Q3; 11 Q1)? If yes, the over-travel threshold above the crack pressure is not essential and a broader claim 1 exists; as it stands, that relationship is what distinguishes ref-02 claim 4 and US4462449A. Blocks P5.

Q4. Did the inventor conceive the mechanism carried directly by the valve stem, and Schrader-pattern or Dunlop-pattern formats (11 Q6; 01 Q26, Q33)? Decides whether claim 2 keeps its direct-carriage limb. Blocks P5, PACKAGE.

Q5. Which parts are to be sold separately (02 Q1; 01 Q33)? Decides whether family B is filed and whether a kit claim is added at Prompt 27. Blocks P5.

Q6. May the deflecting formation be the sealing face or a continuation of it (11 Q4; 03 Q8)? Decides whether "deflecting formation" is used in the independent claims or "purge shoulder" with its narrower locked definition. Blocks P5.

Q7. Should a professional search be commissioned before the families are relied on (07 Q1)? Blocks P5, PACKAGE.

```json
{
  "prompt": "21",
  "status": "complete",
  "assumptions": [
    {"id": "A1", "text": "No Gate 1 answers; 01 Q1/Q2, 03 Q1, Q3, Q5 treated as unanswered; families follow 03 (air purge essential, wipe advantageous) and 09 rows 1-2.", "blocking": true},
    {"id": "A2", "text": "Gate 2 confirmed unattended; family C direct-carriage limb (12 E16.3), deflecting formation genus (11 DA-4) and functional purge gap genus (11 DA-2) are candidates confirmed by code, used subject to Gate 3 review.", "blocking": true},
    {"id": "A3", "text": "The description will follow the section ids of 16; disclosure bases cite those ids; paragraph anchors mapped in P5d.", "blocking": false},
    {"id": "A4", "text": "Pressure differential is supply-side pressure less chamber-side pressure (01 A3; 19 A4).", "blocking": false},
    {"id": "A5", "text": "Fictional ref-01/ref-02 treated as prior art for the distinction test, with US4462449A and EP1137892A1 as real-art counterparts.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "Purge gap location and opening against the interference fit (01 Q1, Q2); families A, C, D define it functionally pending the answer; fallback is the wipe-based nucleus.", "blocks": ["P5", "REVIEW"]},
    {"id": "Q2", "text": "Air purge alone, snap-back wipe alone, or both (03 Q1)? Decides which carries the independent claims.", "blocks": ["P5"]},
    {"id": "Q3", "text": "Would purging on every opening work (03 Q3; 11 Q1)? Decides whether the over-travel threshold above the crack pressure is essential in claim 1.", "blocks": ["P5"]},
    {"id": "Q4", "text": "Mechanism carried directly by the valve stem and other valve formats conceived (11 Q6; 01 Q26, Q33)? Decides claim 2's direct-carriage limb.", "blocks": ["P5", "PACKAGE"]},
    {"id": "Q5", "text": "Which parts are sold separately (02 Q1; 01 Q33)? Decides family B filing and a Prompt 27 kit claim.", "blocks": ["P5"]},
    {"id": "Q6", "text": "May the deflecting formation be the sealing face or a continuation (11 Q4; 03 Q8)? Decides 'deflecting formation' versus 'purge shoulder' in the independent claims.", "blocks": ["P5"]},
    {"id": "Q7", "text": "Professional search before the families are relied on (07 Q1)?", "blocks": ["P5", "PACKAGE"]}
  ],
  "new_terms": [
    {"term": "deflecting formation", "maps_to": "purge shoulder", "reason": "Locked genus of the purge shoulder (LOCKED Broader column; 16 S7.6, S11.3); used for the independent claim concept so that the sealing face, a taper or lugs are covered (11 DA-4)."},
    {"term": "threshold-setting arrangement", "maps_to": "second spring stage", "reason": "Locked genus of the second spring stage (LOCKED Broader column; 16 S7.7, S11.4); names family J."},
    {"term": "resilient metal", "maps_to": "superelastic alloy", "reason": "Locked genus (LOCKED Broader column); names the non-superelastic metal species of family I (12 E12.4)."},
    {"term": "resilient polymer", "maps_to": null, "reason": "Material genus for the PEEK seat ring (§6 Alternative A) and the PPS/PEI candidates (12 E12.5); declared in 16."},
    {"term": "kit", "maps_to": null, "reason": "Names the separately supplied seat ring, poppet and return spring of 11 DA-19 for family K."},
    {"term": "wheel", "maps_to": null, "reason": "Names the system dependent of family C (02 rank 3; 12 §16); no locked term exists for the wheel incorporating the inflation valve."},
    {"term": "tube stock", "maps_to": null, "reason": "The §7 starting material for the seat ring (drawn NiTi tube), named for family E; 'tube' alone is barred by the LOCKED drafting notes."},
    {"term": "seat ring blank", "maps_to": "seat ring", "reason": "The laser-cut part before shape-setting, needed to sequence the family E steps (§7)."}
  ],
  "support_refs": [
    {"item": "Family A valve core concept: normal stroke, over-travel above a higher threshold, deflecting formation spaced then bearing, purge gap closed in closed and normal-open states, purge flow path separate from main passage, shape recovery", "support": "intake/disclosure.md §2, §3(2)-(6), §4 via runs/r1/P1/01.md (d), (i); runs/r1/P1/03.md N0 (a)-(e), C2-C8, C18; CONFIRMED.md 11 findings 1-3, DA-2, DA-4, DA-5; 12 §2-§4, §7, §9; runs/r1/P4/16.md S7.3-S7.7, S8.1-S8.8, S9.1-S9.7, CF-A"},
    {"item": "Family B seat ring component: sealing edge, convoluted wall, axial-to-radial conversion, elastic recovery, dimensional envelope", "support": "intake/disclosure.md §3(3), §4, §5, §7; runs/r1/P1/03.md N2-N4, C10, C12, C14, C21; CONFIRMED.md 12 §4, §5, §12, §13; 13 Table 1; runs/r1/P4/16.md S7.4, S7.9, S7.10, S10.1-S10.7, CF-B"},
    {"item": "Family C inflation valve carried by the valve stem directly or by a core body; system dependents", "support": "intake/disclosure.md §1, §3(1); CONFIRMED.md 12 E16.2, E16.3, E14.6; 11 DA-6; runs/r1/P4/16.md S8.1, S8.2, S11.9, S16, CF-C; runs/r1/P1/02.md rank 3"},
    {"item": "Family D method of use steps", "support": "intake/disclosure.md §2, §8 via runs/r1/P1/01.md (d) S1-S5, (i); intake/data/bench-test.md; CONFIRMED.md 12 E1.1, E8.1, E8.5, E9.1; runs/r1/P4/16.md S9.1-S9.9, S13.1, CF-D"},
    {"item": "Family E manufacture: tube stock, laser cutting, forming the convoluted wall, shape-setting in a fixture, quench; dependents electropolishing, 500 °C/10 min, Af below 5 °C, press-fit against the internal shoulder", "support": "intake/disclosure.md §4, §7 via runs/r1/P1/01.md (j); runs/r1/P1/03.md C23-C25; CONFIRMED.md 12 §14, §15; 11 DA-21; runs/r1/P4/16.md S12.1-S12.5, CF-E, CF-F"},
    {"item": "Dependent families H, I, J, L", "support": "intake/disclosure.md §3(5), §5, §6; CONFIRMED.md 12 §2, §12, §13, E4.2, E4.6; 14 sentences 1, 2, 6, footnotes [g], [h]; 11 DA-1, DA-11, DA-13, DA-14, DA-17; runs/r1/P4/16.md S10.1, S10.5, S11.4, S11.7"},
    {"item": "Families declined (F, G, K, M, composition, consumable, software)", "support": "runs/r1/P4/16.md Claim-Family Support Map; runs/r1/P1/02.md ranks 4, 8, 10, A4; runs/r1/P1/03.md C32; CONFIRMED.md 11 DA-19"},
    {"item": "Prior-art exposure per family", "support": "runs/r1/P2/08.md Attack by claim concept (N0, N1, value-map ranks 2, 3, 4, 6, thermal variant); runs/r1/P2/09.md rows 1-7; runs/r1/debate/d2-attack.md R6, R11, R16, R17, R19, §7"}
  ],
  "disclosure_requests": [
    {"limitation": "Family A/C/D purge gap genus: 'a purge gap bounded at least in part by a surface of the deflectable ring element, closed in the closed state and in the normal-open state, opened by the radial deflection in the purge state, giving a purge flow path separate from the main passage from the supply side to the chamber side'", "needed_disclosure": "An express statement in those words in the definitions (16 S7.5) and in the operation section (S9.4, S9.5), with the outer-surface, inner-surface, end-face and through-wall species each described (12 §7)."},
    {"limitation": "Family A/C/D 'deflecting formation of the poppet' spaced from the deflectable ring element throughout the normal stroke and bearing on it only in over-travel", "needed_disclosure": "An express genus statement (16 S7.6, S11.3) that the deflecting formation may be the purge shoulder, the sealing face or a continuation of it, a taper on the poppet stem, a collar or lugs; and an express statement of the axial clearance between the deflecting formation and the deflectable ring element in the closed state and the normal-open state (S8.5, S9.2)."},
    {"limitation": "Family C: deflectable ring element and poppet 'carried by the valve stem, directly or by a core body received in the stem bore'", "needed_disclosure": "An express statement (16 S11.9) that the parts may be carried directly by the valve stem in a non-removable inflation valve, and of Schrader-pattern and Dunlop-pattern formats, labelled as candidates pending 11 Q6."},
    {"limitation": "Family B: seat ring as a separately supplied component; axial load applied at either axial end produces radial deflection of the convoluted wall; measurement of seat ring inner diameter and seat ring wall thickness", "needed_disclosure": "An express component statement (16 S11.10, S17 CF-B), the axial-load statement in genus form (S10.2), and the measurement conventions (S7.10)."},
    {"limitation": "Family E: 'forming the convoluted wall' and 'shape-setting by heating in a fixture holding the convoluted wall geometry and quenching' as generic steps", "needed_disclosure": "An express statement (16 S12.1, S12.2) that the convolution may be formed by laser cutting, mandrel forming or the shape-setting fixture, and that the 500 °C / 10 min / water quench point is one example of the shape-setting step."}
  ],
  "open_disagreements": [],
  "narrowing_suggested": []
}
```
````

### `/Users/ahmed/PatentCouncil/lessons.md`

```markdown
# Patent Council — lessons learned

Read by the Risk Analyst before every pre-drafting report, and by the Specification Drafter and the
Claims Architect before drafting. Each lesson is a recurring failure seen in real runs, the rule that
prevents it, and the evidence. Keep entries general: **never copy confidential invention content here.**
The Orchestrator appends new lessons after each matter (see its AGENTS.md, "Checkpoint: package").

## L1 — Negative limitations in independent claims are a gift to competitors
**Rule:** Do not put "without doing X" / "not X" limitations about an internal component in an
independent claim. If the distinction matters, claim what the component *does*, and move the negative
feature to a dependent claim with its own support paragraph.
**Why:** A competitor adds one cheap extra step and is literally outside the claim, and a negative
limitation about internal behaviour is usually provable only through source-code discovery.
**Seen:** PayAxle Guard (2026-09), the top critical finding: four independent claims fell to one
avoidable negative gate limitation.

## L2 — Support gaps are the largest category of findings
**Rule:** Every claim element must be mapped in `support-map.json` to paragraphs that exist and use its
words, and `pc support-map` must pass, before the review starts. Add disclosure; do not narrow to fit.
**Why:** 93 of 209 findings (44%) in one run were support, priority or amendment-basis gaps, found only
at the end, which forced whole loop-back cycles.

## L3 — Definite articles need an antecedent
**Rule:** Run `pc antecedent` on every claim set. "The content", "the values", "the verification",
"the time" with no earlier "a/an …" is an antecedent-basis objection waiting to happen.
**Seen:** 34 flags on one shipped claim set.

## L4 — Register every reference numeral
**Rule:** Run `pc numerals` after every description revision. Numerals added in a revision (for example
a new figure's 2202–2212 series) are the ones most often missing from the registry.
**Seen:** Six unregistered numerals in a package that reached counsel.

## L5 — Hold the locked terms, especially in revisions
**Rule:** Revisions and loop-backs drift most. A bare "stage" where the locked term is "transaction
stage" is a violation. Run `pc terms` on every revision, not only on first drafts.
**Seen:** Terminology drift in the claims revision and the abstract of the same run.

## L6 — Novelty argued against nothing is worthless
**Rule:** Phase 2 needs real references with full text. If the reference set is thin, say so in every
Phase 2 output and in the cover memo; do not let a confident novelty position rest on zero documents.
**Seen:** Two consecutive runs of the same matter had no prior art at all.

## L7 — Most single-reviewer findings are opinions, not defects
**Rule:** Adjudicate before routing. Only upheld findings (and unclear critical ones) go back for
revision; every finding is still reported with its ruling.
**Seen:** Two reviewers agreed on 2 of 209 and on 0 of 130 findings in two runs of one matter.

## L8 — Inventor questions only help if they are answerable
**Rule:** Ask the ten questions that change the claims most, as a short multiple-choice form, and keep
the run moving. A list of 140 open questions was left entirely unanswered.
```

## Inputs that do not exist yet (work without them; do not wait)

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/description.md`

## Files to write

Write each of these with your Write tool, at exactly this path, one file per call (the folders exist). Write nothing outside the run folder `{R}`. Do not run the checks yourself: the runner runs them and will tell you if anything fails.

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/23.md`

When every file is written, reply with one line per file (path and a few words on what it holds) and anything the runner must route: open questions, disclosure requests, open disagreements, narrowing suggested. Nothing else.
