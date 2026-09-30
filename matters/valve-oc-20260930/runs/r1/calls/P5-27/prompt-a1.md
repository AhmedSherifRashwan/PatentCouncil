# Patent Council · matter `valve-oc-20260930` · run `r1` · step `P5-27` · profile full

You are the **Claims Architect**. Follow your AGENTS.md. This message is the whole brief: what to do, the prompts to execute, every input (embedded below, so do not re-read those files), and the exact files to write.

## What to do

Run Prompt 27, in parallel with its siblings. Build generously: the fallback depth of the claim family comes from here.

**Time budget:** about 10 minutes. The whole matter is planned to finish end to end in two hours. Be complete, but write each deliverable once: no drafts, no repetition, no padding.

## Prompt 27 — Omnibus fallback claim concepts  (kind `drafting`)

**Write your reply to:** `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/27.md`

*Capture sub-combinations worth preserving.*

Identify independently valuable sub-combinations disclosed in the specification that could support later amendment, continuation/divisional practice or separate inventions. Draft candidate claim concepts and identify exact supporting passages/figures needed in the initial filing.

**How to work.** The description in front of you is the only source of support. Any limitation that lacks an explicit passage in the description must NOT be drafted: leave it out, and record it in `disclosure_requests` (limitation, and the disclosure ip-spec would need to add) so the inner loop can supply the support. Use locked preferred terms verbatim and the registry's component names; where a claim term needs a reference sign, use the registry numeral. Cite the supporting paragraph for every limitation in `support_refs`. Under `### Omnibus Fallback Concepts` give a numbered list; each concept has: the sub-combination in one sentence, a candidate independent-claim concept (claim-like prose, not necessarily a finished claim), the exact description paragraphs and figures that support it today, whether it is fully supported for a future continuation/divisional or needs a passage added before filing (then also a `disclosure_requests` entry), and the white-space item from `10` it corresponds to, if any. These do not enter `claims.md`. Reply exactly in the drafting output contract: `## Deliverable` (with the H3 sections named above), `## Rationale`, `## Assumptions`, `## Open Questions`, then one final fenced `json` envelope. No preamble before `## Deliverable`; nothing after the envelope. Reuse locked preferred terms verbatim; declare any other term in `new_terms` with a reason.

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

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P2/10.md`

````markdown
## Deliverable

### White-Space Opportunities

This is a drafting and analysis aid prepared by AI. It is not legal advice and does not say that any item is patentable; qualified patent counsel signs off before anything is filed.

**How to read this list.**
- Every item points to disclosure the inventor has already given. Nothing here is a new embodiment.
- "Clear of the charted references" means clear of the 17 references in `07`, which is a thin, partly fictional pile (07 Q1, Q2). It does not mean clear of the art.
- There are no Gate 1 answers, so every item still depends on the Phase 1 questions it cites.
- Ideas that would need new inventor input are not listed here. They are in the Open Questions, marked as blocking P3.

1. **A valve core with three states, sold without the valve stem (replacement valve core).**
   - *Aspect:* The core body (20), seat ring (30), poppet (40) with sealing face (42) and purge shoulder (44), and the return spring (50) together give a closed state, a normal-open state and a purge state. The assembly screws into the stem bore of a conventional Presta-pattern valve stem.
   - *Why clear:* In `07`, rows N0b, N0c (only during over-travel) and N0d are absent or ambiguous in all 17 references. `09` rows 1 and 2 carry it. The valve cores in the art (US4462449A, EP1137892A1, ref-01) have no normal-open state that is separate from a deflection-opened purge path.
   - *Support:* §1 ("cores are sold in multipacks"); §3(1) (conventional valve stem "with a threaded bore to accept the core"); §3(2)–(6); 01 (i) state table; LOCKED `valve core`, `closed state`, `normal-open state`, `purge state`.
   - *Commercial note:* This is value map rank 1: the swappable unit and the retrofit channel. It is subject to 01 Q1/Q2 (enabling the purge gap) and 01 Q33 (intent to sell the core alone).

2. **Method of operation: the inflation-event sequence.**
   - *Aspect:* The sequence within one inflation event:
     1. couple the inflation device to the supply side;
     2. the pressure differential passes the crack pressure (normal stroke; main passage open);
     3. it then passes the over-travel threshold (over-travel; the purge shoulder deflects the ring; the purge gap opens; air purge);
     4. the inflation device is removed, the pressure differential falls, and shape recovery closes the purge gap, with the snap-back wipe.
   - *Why clear:* No `07` reference shows this sequence (rows N0b–N1). `09` rows 1–3.
   - *Support:* §2; 01 (d) steps S1–S5; §8 (inflate to 6 bar with a floor pump); bench data (audible snap on removal of the pump head).
   - *Commercial note:* Value map rank 8. It is hard to detect in infringement (02 A3), so it is better used as a dependent "configured to" limitation, or as a use claim against a competitor's valve, than as a claim asserted against riders.

3. **The two contact interfaces on one poppet, offset along its axis.**
   - *Aspect:* The sealing face (42) and the purge shoulder (44) sit on the same poppet. The purge shoulder is on the chamber side of the sealing face. The sealing face rests on the sealing edge in the closed state; the purge shoulder meets the seat ring only after the normal stroke (prototype: 0.6 mm normal stroke, then 0.5 mm over-travel).
   - *Why clear:* US4408632A has a poppet with a flange that engages a ring-carrying shroud during opening, moving it axially (07 row N0c ?), so the poppet on its own is exposed. The white space is the offset relationship between the two interfaces and the seat ring: the purge shoulder is clear of the ring throughout the normal stroke (`09` row 1).
   - *Support:* §3(4) ("a purge shoulder (44) below the sealing face that only contacts the ring during over-travel"); §4. The geometry of the purge shoulder is not stated (01 Q8).
   - *Commercial note:* This is the feature a copier must reproduce to get the purge state. Useful as a dependent claim and as a definition anchor for "normal stroke".

4. **Split architecture: a fixed seat with a separate wiper ring (Alternative B).**
   - *Aspect:* A fixed seat does the sealing. A separate thin spring wiper ring on its chamber side is deflected outward by the purge shoulder during over-travel.
   - *Why clear:* In the charted wiping art, the wiper is carried on the moving member (US4719938A, US6006954A, US11345196B2: 07 rows N1 A†). No reference has a stationary wiper ring deflected by the valve member's over-travel (`09` rows 1 and 3). `08` rates the ref-01 + US4719938A attack as moderate.
   - *Support:* §6 Alternative B (a rigid brass fixed seat "for sealing plus a separate thin stainless spring wiper ring below it that is deflected outward by the purge shoulder"); LOCKED `wiper ring`, `fixed seat`, `deflectable ring element`.
   - *Commercial note:* Value map rank 6: it blocks the obvious way round a claim to a one-piece seat ring and may be easier to make (§6). Support is one paragraph with no geometry (03 Q7), so the Description cannot go beyond §6 without inventor input.

5. **Polymer seat ring with the same convoluted wall (Alternative A).**
   - *Aspect:* A PEEK seat ring with the convoluted wall, in the same over-travel architecture.
   - *Why clear:* ref-02 discloses only elastomer rings (60–80 Shore A) and a one-sentence spring-steel lip (07 row N4 ?). No charted reference has a polymer seat ring deflected by over-travel (`09` rows 1 and 5).
   - *Support:* §6 Alternative A (with "some radial compliance", "cheaper", slower recovery and a weaker wipe).
   - *Commercial note:* Value map rank 5, for a lower-cost product line. It keeps the deflectable ring element genus from being limited to superelastic alloy. It is untested, and the inventor has not confirmed it is within the invention (03 Q5).

6. **The seat ring as a component, defined by function and by dimensions.**
   - *Aspect:* A seat ring that has:
     - a sealing edge;
     - a convoluted wall of one or two shallow convolutions that converts axial load on the sealing edge into radial deflection;
     - the inventor's believed dimensions: inner diameter 2.0–2.6 mm, wall 0.15–0.30 mm, free length 2.5–4.0 mm, convolution amplitude 0.08–0.20 mm.
   - *Why clear, and how far:* US9982818B2 discloses a wave-profile NiTi sealing ring (07 rows N3 ?, N4 E). `08` rates a ring defined only by material and wave wall as strongly exposed. What remains is the sealing edge, the axial-to-radial function and the dimensions, none of which appears in the US9982818B2 extract (07 Q3).
   - *Support:* §3(3); §4; §5; §7.
   - *Commercial note:* Value map rank 2. It reaches ring suppliers that never sell a complete valve core. It is a secondary family only, and its value depends on the full text of US9982818B2.

7. **Method of manufacturing the seat ring.**
   - *Aspect:* The §7 route:
     1. laser cutting of NiTi tube (2.7 mm OD, 0.20 mm wall) to the convoluted profile on a mandrel;
     2. shape-setting at 500 °C for 10 minutes in a fixture that holds the wave geometry;
     3. water quench;
     4. electropolishing to remove the oxide and the heat-affected edge;
     5. pressing into the core body with about 0.03 mm interference against the internal shoulder.
   - *Why clear:* No `07` reference discloses these steps (rows N6/7). ref-01 press-fits a sleeve that is not a seat ring; US6393765B1 mentions only "thermo-mechanical treatments already known in the art". `08` rates it moderate to strong once the ring is known, because the steps are routine NiTi practice (08 A5).
   - *Support:* §5; §7; LOCKED `laser cutting`, `shape-setting`, `electropolishing`, `interference fit`.
   - *Commercial note:* Value map rank 4. It reaches volume ring makers, but only one set of process values is disclosed and there are no process windows (01 Q32).

8. **Calibration relationship between the two thresholds.**
   - *Aspect:* The crack pressure is set by the first spring stage and the over-travel threshold by the second spring stage. The over-travel threshold is higher than the crack pressure and below the pressure an inflation device reaches during an inflation event. Values: 0.8–1.5 bar and 2.5–5.0 bar (believed); 1.0 and 3.5 bar (prototype); inflation to 6 bar (§8).
   - *Why clear:* EP1137892A1's threshold acts on chamber-side pressure and releases air to atmosphere (07 row N0b ?). The spring art has no sequential stages (07 rows N5 ?; `09` row 7).
   - *Support:* §2 (a threshold "which every floor pump reaches"); §3(5); §4; §8.
   - *Commercial note:* A fallback ladder for Claims Architect. The basis for "every floor pump" is unanswered (01 Q5), and `08` rates the ranges as routine optimisation unless their basis is supplied (01 Q15).

9. **Material and temperature species of the seat ring.**
   - *Aspect:* A superelastic alloy seat ring: NiTi, nominally 55.8 wt% Ni, austenite finish temperature below 5 °C, electropolished.
   - *Why clear:* This is only clear in combination with items 1–3. US6393765B1 and US9982818B2 disclose superelastic or shape-memory NiTi seals, but not as a valve seat ring deflected by a poppet (07 rows N2, N4; `09` row 4).
   - *Support:* §2; §4; §5.
   - *Commercial note:* The premium product. It is where the inventor locates the strength of the wipe (§2). Dependent only, because the inventor's own Alternatives A and B design round it.

10. **The valve core in a wheel or chamber assembly.**
    - *Aspect:* An inflation valve with the valve core fitted, in an inflatable chamber that holds liquid sealant: a bicycle inner tube or a tubeless set-up.
    - *Why clear:* Only through item 1. The chamber increment is known (US11179979B2 claim 12, US11065925B2 claim 7).
    - *Support:* §1; §8 (700×28 tubes each charged with 60 ml of sealant).
    - *Commercial note:* Value map rank 3, the OEM channel for tubes, tyres and wheels. Tubeless use is disclosed but untested (01 Q25).

11. **Corrosion-resistant core body.**
    - *Aspect:* A core body of stainless 303 for use with ammonia-bearing liquid sealant.
    - *Why clear:* Only in combination with item 1. No charted reference addresses core body material against sealant chemistry.
    - *Support:* §5 ("a stainless 303 variant was also machined for corrosion resistance with ammonia-bearing sealant").
    - *Commercial note:* Value map rank 9: a product-line dependent claim. It was not bench-tested (01 Q18).

12. **Thermally actuated purge (weak).**
    - *Aspect:* A two-way shape-memory NiTi seat ring with an austenite finish temperature of about 35–40 °C, which opens the purge gap when warmed by hand.
    - *Why clear, and how weak:* No charted reference applies heat-driven ring movement to a purge gap in a tyre valve. However, US9982818B2 claim 5 and US6393765B1 claim 1 show SMA seal elements moving in response to temperature, and `08` rates the attack moderate to strong.
    - *Support:* §6 (the inventor is "not sure this is worth pursuing and [has] no data").
    - *Commercial note:* Value map rank 10. Include it only if the inventor confirms (01 Q21).

## Rationale

**How items were chosen.** Each item passes two tests:
- it has a passage in the disclosure behind it;
- it is clear of the `07` charts, either on its own or in combination with the `09` distinctions.

**Order.** Items 1–3 are the core of the white space, because they sit on the three relationships that `08` found absent from the pile. Items 4 and 5 are the inventor's own design-arounds, and claiming them is what stops the one-piece superelastic NiTi seat ring being the only protected form. Item 6 is listed with its exposure to US9982818B2 stated, not hidden, because a component claim loses the valve context that carries novelty. Items 7–12 are product-line and fallback territory.

**What I left out.** Several tempting areas are not in the list because they would need matter the inventor has not given:
- other valve types;
- other alloys;
- straight-walled or other axial-to-radial geometries;
- other threshold-setting arrangements;
- other ways of retaining the ring;
- other forming routes;
- purging on deflation;
- a mitigation for the film found in the purge-gap region;
- a spare-ring refill consumable.

Each is an open question below, marked as blocking P3.

## Assumptions

A1. No Gate 1 answers exist. Items 1–3 depend on 01 Q1/Q2 (the purge gap) and 03 Q1 (purge against wipe) being answered in a way consistent with `03`. Blocking for P3 and P5.

A2. Items 4 and 5 (Alternatives B and A) are treated as disclosed alternatives within the locked deflectable ring element genus. The inventor has not confirmed they are within the invention (03 Q5). Blocking for P5.

A3. Retrofitting a conventional valve stem (item 1) rests on §3(1) (a conventional valve stem "with a threaded bore to accept the core") and §1 (replacement cores sold in multipacks). Whether the core is intended to be sold alone is unanswered (01 Q33). Not blocking for P3.

A4. The "clear of" statements cover only the 17 charted references. Not blocking.

## Open Questions

Q1. Has the inventor conceived use in Schrader-pattern or other valve types, or in other tyres or fluid valves prone to fouling (01 Q26)? This would widen items 1 and 10. Blocks P3.

Q2. Would a straight-walled seat ring, or any other geometry that turns axial load into radial deflection, work (01 Q12)? This would widen items 5 and 6 beyond the convoluted wall. Blocks P3.

Q3. Has any threshold-setting arrangement other than the two spring stages been conceived, for example ring stiffness, a second spring or a detent (01 Q6)? This would widen item 8. Blocks P3.

Q4. Have other superelastic alloys or other polymers been conceived for the seat ring (01 Q14; 03 Q6)? This would widen items 5 and 9. Blocks P3.

Q5. Have other ways of retaining the ring (adhesive, crimp, snap feature) or other forming routes (stamping, etching, rolling) been conceived, and what are the working windows for the shape-setting and interference-fit values (01 Q17, Q32)? This would widen item 7. Blocks P3.

Q6. Does deflation through the valve also trigger over-travel or the purge state (01 Q23)? If so, a purge on deflation could be a further use protocol. Blocks P3.

Q7. Cured film collected on the ring's outer surface in the purge-gap region by cycle 40 (§8). Has the inventor conceived a mitigation (01 Q30)? Blocks P3.

Q8. Is a spare-ring or core refill pack, or another consumable, intended (02 Q3)? Blocks P3.

Q9. Should the thermally actuated purge (item 12) be kept, given the inventor's doubt, the lack of data and the moderate-to-strong attack in `08` (01 Q21)? Blocks P3, P5.

Q10. The purge gap and air path (01 Q1, Q2) underpin items 1–3. Without them, the three-state valve core is not enabled as written. Blocks P3, P4, P5.

Q11. Coverage is thin and ref-01 and ref-02 are fictional (07 Q1, Q2). The white space is untested against a professional search. Blocks P3, PACKAGE.

```json
{
  "prompt": "10",
  "status": "partial",
  "assumptions": [
    {"id": "A1", "text": "No Gate 1 answers exist; items 1-3 depend on 01 Q1/Q2 (purge gap) and 03 Q1 (purge against wipe) being answered consistently with 03.", "blocking": true},
    {"id": "A2", "text": "Items 4 and 5 (Alternatives B and A) treated as disclosed alternatives within the locked deflectable ring element genus; not confirmed by the inventor (03 Q5).", "blocking": true},
    {"id": "A3", "text": "Retrofit into a conventional valve stem (item 1) rests on §3(1) and §1; intent to sell the core alone unanswered (01 Q33).", "blocking": false},
    {"id": "A4", "text": "'Clear of' statements cover only the 17 references charted in 07.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "Schrader-pattern or other valve types, other tyres or fouling-prone fluid valves conceived (01 Q26)? Would widen items 1 and 10.", "blocks": ["P3"]},
    {"id": "Q2", "text": "Would a straight-walled seat ring or other axial-to-radial geometry work (01 Q12)? Would widen items 5 and 6.", "blocks": ["P3"]},
    {"id": "Q3", "text": "Any threshold-setting arrangement other than the two spring stages (01 Q6)? Would widen item 8.", "blocks": ["P3"]},
    {"id": "Q4", "text": "Other superelastic alloys or other polymers for the seat ring (01 Q14; 03 Q6)? Would widen items 5 and 9.", "blocks": ["P3"]},
    {"id": "Q5", "text": "Other ring retention methods or forming routes, and working windows for shape-setting and interference fit (01 Q17, Q32)? Would widen item 7.", "blocks": ["P3"]},
    {"id": "Q6", "text": "Does deflation through the valve trigger over-travel or the purge state (01 Q23)? Possible further use protocol.", "blocks": ["P3"]},
    {"id": "Q7", "text": "Mitigation conceived for cured film collecting on the ring outer surface in the purge-gap region (01 Q30)?", "blocks": ["P3"]},
    {"id": "Q8", "text": "Is a spare-ring or core refill pack or other consumable intended (02 Q3)?", "blocks": ["P3"]},
    {"id": "Q9", "text": "Keep the thermally actuated purge (item 12) given inventor doubt, no data and a moderate-to-strong attack in 08 (01 Q21)?", "blocks": ["P3", "P5"]},
    {"id": "Q10", "text": "Purge gap and air path (01 Q1, Q2) underpin items 1-3; the three-state valve core is not enabled as written without them.", "blocks": ["P3", "P4", "P5"]},
    {"id": "Q11", "text": "Coverage thin and ref-01/ref-02 fictional (07 Q1, Q2); white space untested against a professional search.", "blocks": ["P3", "PACKAGE"]}
  ],
  "new_terms": [
    {"term": "threshold-setting arrangement", "maps_to": "second spring stage", "reason": "Locked genus of the second spring stage; used in Q3 so alternatives to the return spring can be asked about."}
  ],
  "support_refs": [
    {"item": "Item 1 three-state valve core; replacement core", "support": "intake/disclosure.md §1, §3(1)-(6); runs/r1/P1/01.md (i); runs/r1/P2/07.md rows N0b-N0d; runs/r1/P2/09.md rows 1-2"},
    {"item": "Item 2 inflation-event sequence", "support": "intake/disclosure.md §2, §8; runs/r1/P1/01.md (d) S1-S5; intake/data/bench-test.md"},
    {"item": "Item 3 sealing face and purge shoulder interfaces", "support": "intake/disclosure.md §3(4), §4; runs/r1/P2/07.md US4408632A row N0c"},
    {"item": "Item 4 Alternative B fixed seat and wiper ring", "support": "intake/disclosure.md §6; runs/r1/P2/07.md rows N1 (US4719938A, US6006954A, US11345196B2)"},
    {"item": "Item 5 Alternative A PEEK seat ring", "support": "intake/disclosure.md §6; runs/r1/P2/07.md ref-02 row N4"},
    {"item": "Item 6 seat ring component and dimensions", "support": "intake/disclosure.md §3(3), §4, §5, §7; runs/r1/P2/07.md US9982818B2 rows N3, N4"},
    {"item": "Item 7 seat ring manufacturing method", "support": "intake/disclosure.md §5, §7"},
    {"item": "Item 8 crack pressure and over-travel threshold calibration", "support": "intake/disclosure.md §2, §3(5), §4, §8"},
    {"item": "Item 9 superelastic NiTi, Af below 5 °C, 55.8 wt% Ni, electropolished", "support": "intake/disclosure.md §2, §4, §5"},
    {"item": "Item 10 inflatable chamber assembly", "support": "intake/disclosure.md §1, §8"},
    {"item": "Item 11 stainless 303 core body", "support": "intake/disclosure.md §5"},
    {"item": "Item 12 thermally actuated purge", "support": "intake/disclosure.md §6"}
  ],
  "disclosure_requests": [
    {"limitation": "Item 4 wiper ring (Alternative B)", "needed_disclosure": "Form, thickness and retention of the wiper ring, and whether it wipes the poppet on recovery (03 Q7)."},
    {"limitation": "Items 1-3 purge gap", "needed_disclosure": "Written description of the purge gap boundaries, opening mechanism and air path (01 Q1, Q2)."}
  ],
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

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P4/16.md`

````markdown
## Deliverable

### Specification Blueprint

This blueprint is a drafting and analysis aid prepared by AI. It is not legal advice and says nothing about patentability; qualified patent counsel signs off before anything is filed.

**Sources and scope.** Structure and prose are to be drafted only from `CONFIRMED.md` (Prompts 11–15 as confirmed at Gate 2), the Phase 1 outputs (`01`, `02`, `03`), `terminology/LOCKED.md`, `intake/data/bench-test.md` and `intake/drawings/README.md`. `intake/disclosure.md` is cited §1–§9 through `01`. Prompts 09 and 10 and the pre-drafting findings do not exist yet (A1). No Gate 1 answers were embedded, so every Phase 1 open question is treated as unanswered (A2). Design-around routes DA-7, DA-23 and DA-24 are marked in `CONFIRMED.md` as closable only with matter the inventor has not conceived; they are excluded from the description (A3, Q1). Every section id below is stable and is to be reused by Prompts 17–20a and the compose step. Each node gives: what the section contains | the dossier material that feeds it.

- **S1 Title.** "Inflation valve with a deflectable ring element for purging sealant film", or a variant that names the valve core and the purge state without material or valve-standard limitations | `03` N0; LOCKED (terms to avoid). Drafted at compose.
- **S2 Technical field.** Inflation valves and valve cores for inflatable chambers that hold liquid sealant; the deflectable ring element as a component; methods of making and using them | §1; `03` C31; `02` ranks 1–4. Drafted at compose.
- **S3 Background.** Liquid sealant in inner tubes and tubeless set-ups; capillary ingress along the poppet stem and pressure-surge ingress on each inflation event; drying to sealant film; the two failure modes (leak-down, blockage) after 10–20 inflation cycles; the tool-based remedy and multipack sale; existing attempts (low-adhesion coating, enlarged bore, removable insert) that only slow build-up. No named prior-art documents until `09`/`10` exist (A1) | §1; `01` (a); bench data (conventional valve core failures). Drafted at compose.
- **S4 Problem.** A valve core that keeps sealing and keeps opening over many sealant-loaded inflation cycles without a tool or user action, by removing sealant film rather than slowing its formation | §1, §2; `01` (c). Drafted at compose.
- **S5 Summary (statements of invention).** One general statement per claim family CF-A to CF-M of the support map, in functional genus language, each followed by its preferred species; the relationships that make the mechanism work (over-travel threshold above the crack pressure and reachable by the inflation device; purge gap closed in the closed state and the normal-open state; cleaning action by the air purge, the snap-back wipe, or both) | `03` N0–N7; `CONFIRMED.md` 11 findings 1–4; `02`. Drafted at compose from the parts.
- **S6 Brief description of drawings.** One line per figure of the figure plan (Prompt 20): Fig. 1 axial section, closed state (from inventor FIG-1); Fig. 2 axial section, purge state (from inventor FIG-2); Fig. 3 axial section, normal-open state; Fig. 4 enlarged detail of the sealing edge, sealing face and purge shoulder during shape recovery (snap-back wipe); Fig. 5 the seat ring alone, with the convoluted wall and dimension call-outs; Fig. 6 diagram of poppet displacement against pressure differential showing crack pressure, normal stroke, over-travel threshold and over-travel distance; Fig. 7 axial section of the fixed seat and wiper ring embodiment; Fig. 8 alternative forms of the deflectable ring element (slotted, frustoconical, cellular, conical annular disc, plain wall with tapered purge shoulder); Fig. 9 alternative threshold-setting arrangements; Fig. 10 alternative purge gap locations and purge flow paths; Fig. 11 alternative ring retention; Fig. 12 the mechanism in a non-removable inflation valve and in a larger-bore valve core; Fig. 13 flow chart of the seat ring manufacturing method; Fig. 14 chart of inflation time against inflation cycle for the prototype and conventional valve core from the bench data | drawings README; `CONFIRMED.md` 12; bench data. The inventor's images are absent (Q2); Figs. 1 and 2 are re-drawn from the README descriptions and §3.
- **S7 Definitions and conventions** (opens the detailed description; content from Prompt 19).
  - S7.1 Comprising, "in some embodiments", "optionally", singular and plural, direct and indirect coupling, order of steps | Prompt 19.
  - S7.2 Orientation: supply side and chamber side replace orientation words; "axial" and "radial" relative to the poppet axis | LOCKED (supply side, chamber side); `01` A4, A5.
  - S7.3 Pressure differential, crack pressure, over-travel threshold, normal stroke, over-travel, over-travel distance; static or transient reading stated as an assumption | LOCKED; `01` A3; `13` Table 1.
  - S7.4 Deflectable ring element and seat ring defined by function (seats, is deflected radially during over-travel, undergoes shape recovery), not by material or wall form; wiper ring and fixed seat | LOCKED; `03` A1; `12` §4.
  - S7.5 Purge gap, purge flow path, purge gap opening, radial deflection defined by function: a purge passage bounded at least in part by a surface of the deflectable ring element, closed in the closed state and the normal-open state, opened by the radial deflection, in either radial sense | `12` §7 genus; `11` DA-2, DA-3; LOCKED.
  - S7.6 Purge shoulder defined by function (deflecting formation that contacts the deflectable ring element only during over-travel) | LOCKED; `11` DA-4; `12` §3.
  - S7.7 Second spring stage and threshold-setting arrangement defined by function | LOCKED; `11` DA-11; `12` §2.
  - S7.8 Air purge (any inflation gas), snap-back wipe, cleaning action, sealant film, liquid sealant (not limited to latex), inflatable chamber (inner tube and tubeless), inflation device, inflation event | LOCKED; `12` E8.5.
  - S7.9 Superelastic alloy, austenite finish temperature, martensite start temperature and their measurement; resilient metal; resilient polymer | LOCKED; `12` §12, §13.
  - S7.10 Dimensional conventions: how seat ring inner diameter, seat ring outer diameter, seat ring wall thickness, seat ring free length, convolution amplitude and purge gap opening are measured | LOCKED (needs definition); `13` Tables 1–2.
  - S7.11 Test definitions for the examples: inflation cycle, leak-down, blockage, inflation time, conventional valve core | §8; bench data; LOCKED.
- **S8 Structure of the valve core (closed state)** (Fig. 1, Fig. 5).
  - S8.1 The inflation valve, valve stem and stem bore; the valve core threaded into the stem bore; Presta-pattern as the worked example, not a limitation | §3(1), §3(2); LOCKED; `11` DA-6.
  - S8.2 What the valve core comprises; that it is a unit separable from the valve stem; the replacement valve core | §3; `02` rank 1; LOCKED (valve core needs definition); `11` DA-19.
  - S8.3 Core body: internal shoulder, core body bore, poppet guidance; brass CW614N and stainless 303 as materials; in some embodiments a polymer core body | §3(2), §5; `11` DA-5; `12` E4.5.
  - S8.4 Seat ring in the closed state: annular, sealing edge, convoluted wall, seated against the internal shoulder; the interference fit and, in some embodiments, an interference fit confined to an axial band at the internal shoulder leaving the remainder of the wall free of the core body bore | §3(3), §7; `12` E14.1–E14.3; `11` DA-22.
  - S8.5 Poppet: poppet stem, sealing face (conical in the example, metal to metal), purge shoulder on the chamber side of the sealing face, axial clearance between purge shoulder and seat ring at rest | §3(4); `12` E3.1, E11.1; `01` Q8, Q9 flagged.
  - S8.6 Return spring: first spring stage, second spring stage; the two-stage spring as one species of threshold-setting arrangement; spring material immaterial | §3(5), §5; `12` E2.1; `03` C17.
  - S8.7 Purge gap in the closed state, as the locked species (annular radial clearance between the seat ring outer surface and the core body bore) and as the S7.5 genus; whether the closed purge gap is itself airtight stated as an open point with the sealing edge as the primary seal | §3(6); `01` Q1, Q31; `15` FM-22.
  - S8.8 Lock nut and its storage function | §3(7); `15` FM-12.
- **S9 Operation** (Fig. 2, Fig. 3, Fig. 4, Fig. 6).
  - S9.1 Pressure differential and the state table: closed state, normal-open state, purge state, recovery, locked | `01` (i); LOCKED.
  - S9.2 Crack pressure and the normal stroke against the first spring stage; flow through the main passage; purge gap remains closed | §2, §3(5), §4.
  - S9.3 Over-travel threshold and over-travel against the second spring stage; over-travel distance; what limits over-travel (in some embodiments an over-travel stop in the core body, coil-bind of the second spring stage, or the seat ring itself); in some embodiments the over-travel threshold equals or barely exceeds the crack pressure so the purge state is reached on every opening | §2, §4; `01` Q36; `15` FM-9; `11` DA-1.
  - S9.4 Purge state: purge shoulder bears on the seat ring; radial deflection; purge gap opening; species of direction (radially outward, radially inward at the bounding surface, ovalising) described as alternatives with no one named as the prototype mechanism | §2, §3(6); `12` §6, §7; `01` Q1, Q2 flagged for Prompt 17.
  - S9.5 Purge flow path and air purge: inflation gas from the supply side through the purge gap across the surfaces where sealant film accumulates into the inflatable chamber, alongside the main passage; any inflation gas | §2; drawings README FIG-2; `12` E8.1, E8.5.
  - S9.6 Removal of the inflation device: collapse of the pressure differential, return of the poppet, shape recovery, closing of the purge gap, snap-back wipe across the sealing face or an adjacent poppet surface; superelastic recovery contrasted with elastomer behaviour without turning §2 into a disclaimer | §2; bench data (audible snap); `11` DA-15 drafting point.
  - S9.7 The two cleaning actions: air purge and snap-back wipe; embodiments using both, the air purge alone and the snap-back wipe alone (wipe-only embodiment) | §2; `11` DA-10; `03` A2, Q1.
  - S9.8 Over-travel by other means: pressure differential, a poppet-depressing actuator on the inflation device or an adaptor, pressing by hand; purge during deflation with flow in either direction | `12` E1.4, E1.5; `11` DA-9, DA-20.
  - S9.9 Inflation event, inflation cycle, once-per-event reading; behaviour when topping up stated as open | `01` A8, Q4.
- **S10 The deflectable ring element** (Fig. 5, Fig. 7, Fig. 8).
  - S10.1 Materials: superelastic alloy (NiTi, nickel content nominally 55.8 wt%, austenite finish temperature below 5 °C, martensite start temperature open); ternary NiTi; resilient metal (stainless spring steel, beta-titanium, precipitation-hardened stainless); resilient polymer (PEEK preferred; PPS, PEI); copper-based superelastic alloys with ammonia-free liquid sealant only; effect of material on shape recovery and snap-back wipe strength | §2, §4, §5, §6; `12` §12, §13, §9; `14` sentences 1, 2, 6.
  - S10.2 Wall geometry as axial-to-radial conversion geometry: convoluted wall (one, two, three or more convolutions, any profile), frustoconical wall, slotted wall, cellular wall, conical annular disc, plain wall driven by a tapered purge shoulder | §3(3); `12` §4, §5; `11` DA-12, DA-18.
  - S10.3 Continuous, split and segmented forms; purge opening as an annular gap, slits or apertures in the wall, or gaps between fingers | `11` DA-3; `12` E4.3, E4.6, E5.4.
  - S10.4 Dimensions and parameter ladders: seat ring inner diameter, seat ring outer diameter, seat ring wall thickness, seat ring free length, convolution amplitude, purge gap opening, over-travel distance, crack pressure, over-travel threshold; broad, intermediate and preferred ranges with the prototype value; the intermediate and preferred rungs labelled as proposed; no value outside §4; relationships stated before numbers; ranges tied to the superelastic seat ring and adapted for other materials | §4; `13` Table 1; `14` sentence 7; `11` DA-16.
  - S10.5 One-piece seat ring versus fixed seat with wiper ring: the wiper ring on the chamber side of the fixed seat, deflected by the purge shoulder; its form, thickness and retention as open points; whether it wipes as open; split wiper ring | §6 Alternative B; `12` E4.2, E4.6, E10.2; `14` E-III; `01` Q20; `03` Q7.
  - S10.6 Separate from or integral with the core body (moulded, machined or pressed flexure section); carried by the valve stem instead of the core body | `11` DA-5; `12` E4.5, E14.5, E14.6.
  - S10.7 Shape recovery species: superelastic, elastic (polymer, spring metal), positively driven by a second formation on the poppet; recovery by warming above the austenite finish temperature after chilling | `12` §9.
- **S11 Alternatives for the other parts, valve formats and combinations** (Fig. 9, Fig. 10, Fig. 11, Fig. 12).
  - S11.1 Purge gap species: seat ring outer surface to core body bore; to stem bore through windows in the core body; seat ring inner surface to poppet on the chamber side of the sealing edge; through-wall openings; each with the direction of radial deflection it needs | `12` §7; `11` DA-2.
  - S11.2 Purge flow path species: alongside the main passage; purge ports in the core body; flutes in the core body bore; through the wall of the seat ring | `12` §8.
  - S11.3 Deflecting formation species: annular purge shoulder; tapered purge shoulder; discrete lugs; separate collar on the poppet stem; return-spring retainer; purge sleeve; the sealing face itself or a continuation of it; kinematic inversion with the ring element on the poppet and the formation on the core body | `12` §3, E1.3; `11` DA-4, DA-8.
  - S11.4 Threshold-setting arrangement species: two-stage return spring (variable pitch); auxiliary compression spring with lost motion; disc spring stack; detent (ball, radially sprung, magnetic); polymer compression bush; seat ring stiffness alone with a single-rate return spring; separate purge actuator | `12` §2, E1.2; `11` DA-11.
  - S11.5 Snap-back wipe and mechanical wipe species: recovering seat ring across the sealing face; wiper ring; fixed wiping land; defined wiping edge; rotational wipe | `12` §10.
  - S11.6 Sealing face species: conical; part-spherical; flat on the axial end of the seat ring; hard-anodised aluminium; polymer facing; hard low-adhesion coating used together with the purge | §5; `12` §11.
  - S11.7 Core body material and corrosion resistance: brass CW614N, stainless 303, polymer; ammonia-bearing liquid sealant | §5; `14` CB2; `15` FM-18.
  - S11.8 Ring retention species: interference fit (about 0.03 mm on diameter), interference confined to a band, crimped lip, retaining sleeve, adhesive, staking, laser welding, over-moulding, clamping, integral, supplementary retention | §7; `12` §14; `11` DA-22; `15` FM-6.
  - S11.9 Valve formats: Presta-pattern valve core; Schrader-pattern and Dunlop-pattern valve cores; non-removable inflation valve with the parts carried by the valve stem; inner tube, tubeless tyre, wheel and bicycle incorporating the inflation valve; other fluid valves prone to fouling as candidates | §1, §3(1); `12` §16; `11` DA-6; `02` rank 3.
  - S11.10 Component and kit supply: the seat ring alone; the seat ring with the poppet and return spring; the replacement valve core | `11` DA-19; `14` CB5; `02` ranks 1, 2.
  - S11.11 Thermally actuated purge as a separate concept (two-way shape-memory ring, austenite finish temperature about 35–40 °C), stated as conceived and untested; included only if kept at Gate 3 (Q4) | §6; `12` E9.5; `03` C32.
  - S11.12 Combinations: express statement that every feature of S10 and S11 combines with each of the three core embodiments (superelastic seat ring, polymer seat ring, fixed seat with wiper ring) except the incompatibilities in `14` (electropolishing and austenite finish temperature with a polymer ring; austenite finish temperature with a non-superelastic wiper ring); the seven candidate sentences of `14` | `14` matrix and sentences 1–7.
- **S12 Manufacture and assembly** (Fig. 13).
  - S12.1 Seat ring by laser cutting from NiTi tube stock (2.7 mm outer diameter, 0.20 mm wall) on a mandrel; the step that forms the convolution stated as laser cut, mandrel forming or shape-setting fixture, without asserting which the prototype used | §7; `01` Q11.
  - S12.2 Shape-setting at 500 °C for 10 minutes in a fixture holding the wave geometry, water quench; process window open | §7; `01` Q32; `15` FM-14.
  - S12.3 Electropolishing to remove oxide and heat-affected edge; depth open; mechanical or chemical polishing; limited electropolishing to preserve a defined wiping edge | §7; `12` E15.7, E10.4; `15` FM-17.
  - S12.4 Alternative forming routes: roll-forming, hydroforming, injection moulding (polymer), stamping or deep drawing (wiper ring, conical disc), photochemical etching and rolling | `12` §15; `11` DA-21.
  - S12.5 Assembly: pressing the seat ring into the core body against the internal shoulder with about 0.03 mm interference; alternative retention steps; assembly force or travel check; turning of core body and poppet with no special process | §7; `12` §14; `15` FM-7.
- **S13 Examples.**
  - S13.1 Example 1 (actual): prototype build with the §4 and §7 values; bench test protocol (700×28 inner tube, 60 ml liquid sealant, inflate to 6 bar with a floor pump, hold 24 h at 22 °C, deflate through the valve; failure criteria); per-unit results P-1 to P-3 and C-1 to C-3; audible snap as the over-travel indicator; stereo microscope inspection at cycle 40; what was not measured or tested | §8; bench data; `01` (l).
  - S13.2 Comparative Example 1 (actual): the conventional valve core results | §8; bench data.
  - S13.3 Prophetic example: polymer (PEEK) seat ring with the same convoluted wall, slower shape recovery and weaker snap-back wipe; present or conditional tense | §6 Alternative A; `14` CB3.
  - S13.4 Prophetic example: fixed seat with stainless wiper ring | §6 Alternative B; `14` CB4.
  - S13.5 Prophetic example: stainless 303 core body (machined, not tested) and hard-anodised aluminium sealing face (considered, not built) | §5; `01` F1, F2.
- **S14 Data and results** (Fig. 14).
  - S14.1 Table of per-unit cycles to failure, failure mode, inflation time at cycle 1 and last cycle, leak-down at last cycle; statement that n = 3, 40 cycles censored, over-travel distance and purge gap opening not measured, one liquid sealant, one temperature, one inflation device | bench data; `13` Table 3.
  - S14.2 Interpretation limited to what was observed: sealing edge and poppet face clean, film on the seat ring outer surface in the purge-gap region; no attribution between air purge and snap-back wipe | bench data; `03` A2.
- **S15 Robustness, failure modes and mitigations.** Purge-gap region fouling and larger purge gap opening; over-travel stop; supplementary ring retention; interference tolerance; wear-resistant sealing face; cold behaviour, martensite start temperature and margin for CO2 inflation devices; process windows and verification; ammonia-free liquid sealant untested; long flat storage untested; lock nut for storage; caution against tool insertion. Each mitigation labelled as disclosed, disclosed alternative, or candidate mitigation with no test | `15` FM-1 to FM-22; §9.
- **S16 Industrial applicability and use.** Inner tubes and tubeless set-ups with liquid sealant; floor pump, hand pump, compressor and CO2 inflation devices (reach of the over-travel threshold stated as device-dependent); replacement valve core; original-equipment supply; component supply | §1, §2, §6; `02`; `12` E8.5.
- **S17 Claim-support paragraphs.** For each claim family in the map, one paragraph in genus language with the species listed, placed at the end of the detailed description, cross-referring to S8–S15 by paragraph anchor; drafted after the parts are stitched so anchors are known | this map; `03` ladder; `02`.
- **S18 Abstract.** Placeholder only; drafted by Prompt 39a from the final description and claims | Prompt 39a.

#### Parts for parallel drafting

Each part drafts only its sections under one `### Description` wrapper with `####` section titles, no paragraph numbers, registry numerals and locked terms verbatim. Target 24–30 paragraphs per part.

- **Part 1 — Definitions and structure.** Sections S7.1–S7.11, S8.1–S8.8. Figures: Fig. 1, Fig. 5 (structural call-outs only). Claim families: CF-A, CF-B, CF-C, CF-J (structure), CF-K. Answers: `11` DA-2, DA-4, DA-5, DA-6, DA-11 by functional definitions; `15` FM-12, FM-22.
- **Part 2 — Operation and cleaning actions.** Sections S9.1–S9.9. Figures: Fig. 2, Fig. 3, Fig. 4, Fig. 6. Claim families: CF-A (functional limitations), CF-D, CF-J (behaviour). Answers: `11` DA-1, DA-9, DA-10, DA-20; `15` FM-9, FM-19, FM-21 (stated as open). Carries the enablement flag on the purge gap mechanism for Prompt 17.
- **Part 3 — The deflectable ring element.** Sections S10.1–S10.7. Figures: Fig. 5 (dimensions), Fig. 7, Fig. 8. Claim families: CF-B, CF-H, CF-I, CF-G, ranges of CF-A. Answers: `11` DA-3, DA-5, DA-12 to DA-18; `15` FM-3, FM-4, FM-5.
- **Part 4 — Alternatives, valve formats and combinations.** Sections S11.1–S11.12. Figures: Fig. 9, Fig. 10, Fig. 11, Fig. 12. Claim families: CF-A dependents, CF-C, CF-H, CF-J, CF-K, CF-L, CF-M. Answers: `11` DA-2, DA-4, DA-6, DA-8, DA-11, DA-19, DA-22, DA-25; `14` matrix; `15` FM-6, FM-8, FM-18.
- **Part 5 — Manufacture, examples, data, robustness and use.** Sections S12.1–S12.5, S13.1–S13.5, S14.1–S14.2, S15, S16. Figures: Fig. 13, Fig. 14. Claim families: CF-E, CF-F, CF-G, CF-L, evidence for CF-A and CF-D. Answers: `11` DA-21; `15` FM-1, FM-2, FM-7, FM-10, FM-11, FM-13 to FM-17, FM-20. Actual and prophetic examples kept apart and labelled.

Compose step: S1–S6, S17 and the joins; S18 by Prompt 39a.

### Claim-Family Support Map

| Claim family | Sections that must support it | Confirmed embodiments relied on | Gaps |
|---|---|---|---|
| CF-A Valve core (apparatus, independent; valve stem not a required element): core body, deflectable ring element, poppet with sealing face and deflecting formation, threshold-setting arrangement, purge gap closed except in the purge state | S7.3–S7.7, S8.1–S8.8, S9.1–S9.7, S11.1–S11.4, S13.1, S17 | Prototype (`03` N0–N7; `12` E1.1, E2.1, E3.1, E4.1, E5.1, E6.1, E7.1, E8.1, E9.1, E10.1); `14` CB1; `11` findings 1–3 for the functional definitions | Purge gap location and opening mechanism unresolved (`01` Q1, Q2): S9.4 and S11.1 can describe species but cannot state the prototype mechanism. Purge shoulder geometry and axial clearance (`01` Q8). What limits over-travel (`01` Q36). Whether the closed purge gap is airtight (`01` Q31). Pressure differential definition (`01` Q4). |
| CF-B Deflectable ring element / seat ring (component, independent) with dependents for material, wall geometry, dimensions | S7.4, S7.9, S7.10, S8.4, S10.1–S10.7, S12.1–S12.4, S13.1, S17 | `12` §4, §5, §9, §12, §13; `13` Table 1; `14` sentences 1, 2, 6, 7; `02` rank 2 | Measurement conventions for the ring dimensions not disclosed (S7.10 must state them as conventions). Convolution count of the prototype (`01` Q11). Austenite finish temperature measurement and lower bound (`01` Q13). Intermediate and preferred rungs are proposals, not data (`13`). Component sale intent (`02` Q1). |
| CF-C Inflation valve and system (valve stem with valve core; inner tube, tubeless tyre, wheel, bicycle; non-removable inflation valve; other valve formats) | S8.1, S8.2, S11.9, S16, S17 | `12` §16, E14.6; `11` DA-6; `02` rank 3 | Only inner tubes tested (`01` Q25). Schrader-pattern, Dunlop-pattern and non-removable formats are engineering candidates confirmed by an unattended gate, not inventor statements (A4). |
| CF-D Method of use (inflating an inflatable chamber holding liquid sealant; the apparatus configured to perform the sequence) | S9.1–S9.9, S13.1, S14.1, S17 | `01` (d) S1–S5; `12` E1.1, E8.1, E9.1, E10.1; bench data | Over-travel and purge gap opening inferred from an audible snap, never measured (`01` Q23). Attribution between air purge and snap-back wipe unevidenced (`03` Q1). Detectability weakness noted by `02` rank 8 for Claims Architect. |
| CF-E Method of manufacturing the seat ring (laser cutting, shape-setting, quench, electropolishing) with alternative routes as dependents | S12.1–S12.4, S13.1, S17 | §7 via `01` (j); `12` §15; `11` DA-21; `02` rank 4 | No process windows (`01` Q32). Which step forms the convolution (`01` Q11). Function of electropolishing (`03` Q15). |
| CF-F Method of assembling the valve core (pressing the seat ring against the internal shoulder; alternative retention) | S12.5, S11.8, S17 | §7; `12` §14; `15` FM-6, FM-7 | Working interference range (`01` Q17). Interaction of the interference fit with the purge gap (`01` Q2). |
| CF-G Product-by-process (seat ring obtainable by the method of CF-E) | S12.1–S12.3, S10.1, S17 | §7; `12` E15.1 | Justified only if the shape-set convoluted wall and austenite finish temperature cannot be fully defined structurally; EPO and UK treat product-by-process as the product as such, US as the product regardless of process for infringement: flag for Claims Architect. |
| CF-H Split architecture (fixed seat with a separate wiper ring) | S7.4, S10.5, S11.3, S11.5, S13.4, S17 | §6 Alternative B via `01` F4; `12` E4.2, E4.6, E10.2; `14` E-III, CB4 | Wiper ring form, thickness and retention (`01` Q20). Whether it wipes (`03` Q7). Whether the ranges of S10.4 apply (`14` [d]). Not built. |
| CF-I Material genus dependents (resilient polymer; resilient metal; superelastic alloy species; austenite finish temperature conditioned on the alloy species) | S7.9, S10.1, S10.7, S13.3, S17 | §6 Alternative A; `12` §12, §13; `14` sentences 1, 2, 6; `11` DA-13, DA-14 | PEEK not built. PPS, PEI, ternary NiTi and non-superelastic metals are engineering candidates (A4). No elastomer embodiment (`11` DA-15): S9.6 avoids a disclaimer but describes no elastomer. |
| CF-J Threshold-setting arrangement dependents (two-stage return spring and the species of S11.4; threshold equal to crack pressure) | S7.7, S8.6, S9.2, S9.3, S11.4, S17 | §3(5); `12` §2; `11` DA-1, DA-11 | Spring rates and engagement stroke (`01` Q7). Prototype spring construction (`01` Q6). Whether purge on every opening works (`03` Q3). |
| CF-K Kit and replacement valve core (seat ring alone; seat ring with poppet and return spring; valve core for fitting to an existing valve stem) | S8.2, S11.10, S16, S17 | `11` DA-19; `14` CB5; §1 (multipack sale) | Commercial intent (`02` Q1; `01` Q33). |
| CF-L Corrosion-resistant variant (stainless 303 core body; polymer core body) | S8.3, S11.7, S13.5, S17 | §5 F1; `14` CB2; `15` FM-18 | Stainless body machined but not tested (`01` Q18). Polymer core body is a candidate (A4). |
| CF-M Thermally actuated purge (two-way shape-memory ring) | S11.11, S17 | §6 F5; `12` E9.5; `03` C32 | No data; inventor doubtful; keep or drop (`03` Q12). Recommended for a dependent claim or continuation only (`02` rank 10). |
| Composition | none | none | Not justified: the superelastic alloy is a purchased material with no compositional novelty disclosed. |
| Consumable | none | none | Not justified: the liquid sealant is a third-party product (`02` A4). |
| Controller or software | none | none | Not applicable: the mechanism is wholly mechanical (`01` (i)). |

## Rationale

The description is built as a reservoir around a functional nucleus, because `CONFIRMED.md` shows that every locked species (annular purge gap at the outer surface, purge shoulder as a separate face, separate seat ring, two-stage return spring, convoluted wall, superelastic alloy) has a cheap escape route. S7 therefore defines the deflectable ring element, purge gap, purge shoulder and threshold-setting arrangement by function, and S10–S11 list the species so the genus is supported and any single species can be claimed as a fallback. The five parts are cut along those lines so that no two parts describe the same species: Part 1 defines and shows structure, Part 2 describes behaviour, Part 3 owns the ring element, Part 4 owns everything else that varies, Part 5 owns process and evidence.

The purge gap inconsistency (`01` Q1, Q2) is the largest risk to the whole application. I did not resolve it by choosing a mechanism. S9.4 and S11.1 describe the direction of radial deflection and the location of the purge gap as alternative species, and S8.4 discloses the interference fit confined to a band so that at least one described species is mechanically coherent. Prompt 17 must record that the prototype's own mechanism is unstated, and the compose step must not present any species as the prototype's.

Gate 2 was recorded as auto-unattended. I treated the confirmation as lifting candidate status for drafting, since the operating contract allows nothing else, but the description will mark inventor-disclosed material (§1–§9) and engineering alternatives differently in tense and hedging, and A4 asks the human at Gate 3 to review every alternative that the inventor did not state. DA-7, DA-23 and DA-24 are excluded because `CONFIRMED.md` itself says they cannot be closed without matter the inventor has not conceived.

The intermediate and preferred rungs of `13` are included in S10.4 but are to be written as ranges the specification discloses, without any claim that they were derived from data; the compose step must keep the `13` labelling out of the prose while preserving the honest statement in S14.1 that only the prototype value was built.

Composition, consumable and controller families are listed with reasons for exclusion so that Claims Architect does not re-open them. Product-by-process is retained as a narrow fallback with a jurisdiction flag.

## Assumptions

A1. Prompts 09 and 10 and the pre-drafting findings do not exist; the background (S3) names no prior-art documents and the alternatives are not weighted against the art. Not blocking for Prompt 16; the compose step must revisit S3 when `09`/`10` exist.

A2. No Gate 1 answers were embedded, so every open question in `01` and `03` is treated as unanswered. Blocking for P4 compose (S9.4, S11.1) and REVIEW.

A3. DA-7, DA-23 and DA-24 (porting, rigid wiping edge, pressure-only deflection) are excluded from the description because `CONFIRMED.md` records them as not conceived. Not blocking.

A4. The unattended Gate 2 confirmation is treated as permission to describe the `12` engineering alternatives as embodiments, with hedged language, but a human must review them at Gate 3 because they are not the inventor's stated conception. Blocking for PACKAGE.

A5. Figures 1 and 2 will be re-drawn from the README descriptions and §3, since the inventor's images are absent. Blocking for P4 (Prompt 20) only in that the drawings cannot be checked against the sketches.

A6. `01` A3–A5 (pressure differential is supply side minus chamber side; the poppet opens towards the chamber side) carry forward. Blocking for P4 until `01` Q3, Q4 are answered.

## Open Questions

Q1. Should the inventor be asked at Gate 3 whether porting (DA-7), a rigid wiping edge (DA-23) or pressure-only deflection (DA-24) were conceived, so that S9 and S11 can add them? Blocks P4 revisions, P5.

Q2. The FIG-1 and FIG-2 images are absent; can they be supplied before Prompt 20 so the re-drawn figures can be checked? Blocks P4, PACKAGE.

Q3. Where is the purge gap and how does it open in the prototype (`01` Q1, Q2)? Without the answer, S9.4 describes species only and Prompt 17 must record the nucleus as not enabled for the prototype mechanism. Blocks P4, P5, REVIEW.

Q4. Is the thermally actuated purge (S11.11, CF-M) to be kept or dropped (`03` Q12)? Blocks P4, P5.

Q5. Which parts of the valve core does the inventor intend to sell separately (`02` Q1; `01` Q33)? Decides how much of S11.10 and CF-K is drafted. Blocks P5.

```json
{
  "prompt": "16",
  "status": "complete",
  "assumptions": [
    {"id": "A1", "text": "Prompts 09/10 and the pre-drafting findings do not exist; S3 names no prior-art documents and alternatives are not weighted against the art.", "blocking": false},
    {"id": "A2", "text": "No Gate 1 answers embedded; every open question in 01 and 03 treated as unanswered.", "blocking": true},
    {"id": "A3", "text": "DA-7, DA-23 and DA-24 excluded from the description as not conceived per CONFIRMED.md.", "blocking": false},
    {"id": "A4", "text": "Unattended Gate 2 confirmation treated as permission to describe the 12 engineering alternatives with hedged language; human review needed at Gate 3.", "blocking": true},
    {"id": "A5", "text": "Figs. 1 and 2 re-drawn from the README descriptions and §3 because the inventor's images are absent.", "blocking": true},
    {"id": "A6", "text": "01 A3–A5 (pressure differential direction, poppet opening towards the chamber side) carry forward.", "blocking": true}
  ],
  "open_questions": [
    {"id": "Q1", "text": "Ask the inventor at Gate 3 whether porting (DA-7), a rigid wiping edge (DA-23) or pressure-only deflection (DA-24) were conceived, so S9/S11 can add them?", "blocks": ["P4", "P5"]},
    {"id": "Q2", "text": "Can the FIG-1 and FIG-2 images be supplied before Prompt 20 so the re-drawn figures can be checked?", "blocks": ["P4", "PACKAGE"]},
    {"id": "Q3", "text": "Where is the purge gap and how does it open in the prototype (01 Q1, Q2)? S9.4 describes species only until answered.", "blocks": ["P4", "P5", "REVIEW"]},
    {"id": "Q4", "text": "Keep or drop the thermally actuated purge (S11.11, CF-M; 03 Q12)?", "blocks": ["P4", "P5"]},
    {"id": "Q5", "text": "Which parts of the valve core are to be sold separately (02 Q1; 01 Q33)? Decides the depth of S11.10 and CF-K.", "blocks": ["P5"]}
  ],
  "new_terms": [
    {"term": "deflecting formation", "maps_to": "purge shoulder", "reason": "Genus listed in LOCKED for the purge shoulder; used in S7.6 and S11.3 to cover the tapered, lug, collar, retainer and sleeve species."},
    {"term": "threshold-setting arrangement", "maps_to": "second spring stage", "reason": "Genus listed in LOCKED; used in S7.7, S11.4 and CF-J to cover non-spring species."},
    {"term": "axial-to-radial conversion geometry", "maps_to": "convoluted wall", "reason": "Genus listed in LOCKED; used in S10.2 to cover frustoconical, slotted, cellular and disc forms."},
    {"term": "purge passage", "maps_to": "purge gap", "reason": "Genus listed in LOCKED; used in S7.5 for the functional definition covering all purge gap locations."},
    {"term": "purge opening", "maps_to": "purge gap", "reason": "Covers slits, apertures and finger gaps in the wall of the deflectable ring element (DA-3) as well as the annular gap."},
    {"term": "purge port", "maps_to": "purge flow path", "reason": "Species of purge flow path through the core body wall (12 E8.2), needed in S11.2."},
    {"term": "ring retention", "maps_to": "interference fit", "reason": "Genus listed in LOCKED; used in S11.8 and CF-F for crimp, sleeve, adhesive and integral species."},
    {"term": "resilient metal", "maps_to": "superelastic alloy", "reason": "Genus listed in LOCKED; used in S10.1 for non-superelastic spring metals."},
    {"term": "resilient polymer", "maps_to": null, "reason": "Material genus for the PEEK seat ring (Alternative A) and the PPS/PEI candidates; no locked term exists for the polymer genus."},
    {"term": "over-travel stop", "maps_to": null, "reason": "Structural formation limiting over-travel (15 FM-9); the disclosure does not name what limits over-travel."},
    {"term": "replacement valve core", "maps_to": "valve core", "reason": "Species listed in LOCKED; used in S8.2, S11.10 and CF-K for the retrofit product."},
    {"term": "kit", "maps_to": null, "reason": "Names the separately supplied seat ring, poppet and return spring of DA-19 for claim family CF-K."},
    {"term": "wiping edge", "maps_to": "snap-back wipe", "reason": "Species of 12 E10.4 (sharp-cornered edge on the ring inner surface) used in S11.5 and S12.3."}
  ],
  "support_refs": [
    {"item": "S3 background: ingress, sealant film, two failure modes, tool-based remedy, existing attempts", "support": "intake/disclosure.md §1 via 01 (a); intake/data/bench-test.md"},
    {"item": "S7.4–S7.7 functional definitions of deflectable ring element, purge gap, purge shoulder, threshold-setting arrangement", "support": "CONFIRMED.md 11 findings 1–3, DA-2, DA-3, DA-4, DA-11; 12 §2, §3, §4, §7 genus statements; terminology/LOCKED.md"},
    {"item": "S8 structure and numerals 10–70", "support": "intake/disclosure.md §3 via 01 (d); intake/drawings/README.md FIG-1"},
    {"item": "S8.4 interference fit confined to a band", "support": "CONFIRMED.md 12 E14.2, E14.3; 11 DA-22"},
    {"item": "S9 state table and operating sequence", "support": "01 (i), (d) steps S1–S5; intake/disclosure.md §2, §4"},
    {"item": "S9.3 over-travel threshold equal to crack pressure; over-travel stop", "support": "CONFIRMED.md 11 DA-1; 15 FM-9"},
    {"item": "S9.4, S11.1 purge gap species and directions of radial deflection", "support": "CONFIRMED.md 12 §6, §7; 11 DA-2"},
    {"item": "S9.7 wipe-only and purge-only embodiments", "support": "CONFIRMED.md 11 DA-10; 03 A2"},
    {"item": "S9.8 mechanical and user over-travel; purge on deflation", "support": "CONFIRMED.md 12 E1.4, E1.5; 11 DA-9, DA-20"},
    {"item": "S10.1 materials", "support": "intake/disclosure.md §2, §4, §5, §6; CONFIRMED.md 12 §12, §13; 14 sentences 1, 2, 6"},
    {"item": "S10.2, S10.3 wall geometry and split/segmented forms", "support": "intake/disclosure.md §3(3); CONFIRMED.md 12 §4, §5; 11 DA-3, DA-12, DA-18"},
    {"item": "S10.4 parameter ladders", "support": "intake/disclosure.md §4; CONFIRMED.md 13 Table 1; 14 sentence 7"},
    {"item": "S10.5 fixed seat and wiper ring", "support": "intake/disclosure.md §6 Alternative B via 01 F4; CONFIRMED.md 12 E4.2, E4.6, E10.2; 14 E-III"},
    {"item": "S10.6 integral ring element; ring carried by the valve stem", "support": "CONFIRMED.md 11 DA-5; 12 E4.5, E14.5, E14.6"},
    {"item": "S11.2–S11.6 purge flow path, deflecting formation, threshold-setting, wipe and sealing face species", "support": "CONFIRMED.md 12 §2, §3, §8, §10, §11; 11 DA-4, DA-8, DA-11"},
    {"item": "S11.7 core body materials", "support": "intake/disclosure.md §5; CONFIRMED.md 14 CB2; 15 FM-18"},
    {"item": "S11.9 valve formats and system", "support": "CONFIRMED.md 12 §16; 11 DA-6; 02 rank 3"},
    {"item": "S11.10 kit and component supply", "support": "CONFIRMED.md 11 DA-19; 14 CB5; intake/disclosure.md §1"},
    {"item": "S11.11 thermally actuated purge", "support": "intake/disclosure.md §6 via 01 F5; CONFIRMED.md 12 E9.5"},
    {"item": "S11.12 combinations and incompatibilities", "support": "CONFIRMED.md 14 matrix, footnotes [e]–[h], sentences 1–7"},
    {"item": "S12 manufacture and assembly", "support": "intake/disclosure.md §7 via 01 (j); CONFIRMED.md 12 §14, §15; 11 DA-21"},
    {"item": "S13.1, S13.2, S14 actual example and comparative data", "support": "intake/disclosure.md §8; intake/data/bench-test.md; 01 (l); CONFIRMED.md 13 Table 3"},
    {"item": "S13.3–S13.5 prophetic examples", "support": "intake/disclosure.md §5, §6 via 01 F1–F4; CONFIRMED.md 14 CB2–CB4"},
    {"item": "S15 failure modes and mitigations", "support": "CONFIRMED.md 15 FM-1 to FM-22; intake/disclosure.md §9"},
    {"item": "Claim families CF-A to CF-M", "support": "02 ranks 1–10; 03 N0–N7; CONFIRMED.md 11 findings 1–5, 12 findings for Claims Architect"}
  ],
  "disclosure_requests": [
    {"limitation": "CF-A purge gap and purge flow path (S9.4, S11.1)", "needed_disclosure": "Inventor's statement of which surfaces bound the purge gap in the prototype, the direction of radial deflection and the complete purge flow path; until given, the description can offer species only."},
    {"limitation": "CF-A over-travel limit (S9.3)", "needed_disclosure": "What limits over-travel in the prototype: over-travel stop, coil-bind of the second spring stage or the seat ring."},
    {"limitation": "CF-H wiper ring (S10.5)", "needed_disclosure": "Form, thickness, retention and wiping behaviour of the wiper ring in Alternative B."},
    {"limitation": "CF-E process windows (S12.2, S12.3)", "needed_disclosure": "Shape-setting temperature and time window, electropolishing depth, laser-cutting parameters and which step forms the convolution."},
    {"limitation": "CF-B dimensional conventions (S7.10)", "needed_disclosure": "How the inventor measures seat ring free length, convolution amplitude and purge gap opening."}
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
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/25.md`

## Files to write

Write each of these with your Write tool, at exactly this path, one file per call (the folders exist). Write nothing outside the run folder `{R}`. Do not run the checks yourself: the runner runs them and will tell you if anything fails.

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/27.md`

When every file is written, reply with one line per file (path and a few words on what it holds) and anything the runner must route: open questions, disclosure requests, open disagreements, narrowing suggested. Nothing else.
