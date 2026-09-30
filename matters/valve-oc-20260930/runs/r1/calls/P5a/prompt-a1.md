# Patent Council · matter `valve-oc-20260930` · run `r1` · step `P5a` · profile full

You are the **Claims Architect**. Follow your AGENTS.md. This message is the whole brief: what to do, the prompts to execute, every input (embedded below, so do not re-read those files), and the exact files to write.

## What to do

Run Prompts 21 and 22 from the confirmed embodiments, the differentiation and white space, and (if embedded) the blueprint, the risk report and the attacks. The description is being drafted in parallel: claim what CONFIRMED.md supports; every limitation is mapped to the finished description in P5d.

**Time budget:** about 14 minutes. The whole matter is planned to finish end to end in two hours. Be complete, but write each deliverable once: no drafts, no repetition, no padding.

## Prompt 21 — Claim-family strategy  (kind `drafting`)

**Write your reply to:** `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/21.md`

*Protect the invention from multiple infringement angles.*

Propose a claim-family architecture covering, where appropriate: apparatus/device, system, method of operation/use, method of manufacture, composition/material, kit, consumable, controller/software/computer-implemented method, data-processing method and product-by-process. State which families are justified by the disclosure and commercial model; do not add claim categories merely for volume.

**How to work.** The description in front of you is the only source of support. Any limitation that lacks an explicit passage in the description must NOT be drafted: leave it out, and record it in `disclosure_requests` (limitation, and the disclosure ip-spec would need to add) so the inner loop can supply the support. Use locked preferred terms verbatim and the registry's component names; where a claim term needs a reference sign, use the registry numeral. Cite the supporting paragraph for every limitation in `support_refs`. Under `### Claim-Family Architecture` give a table: family | justified (yes / no) | commercial basis (cite the value-map rank) | disclosure basis (description paragraphs) | intended independent claim concept | notes on jurisdiction (e.g. unity, category mixing). A family with a commercial case but no disclosure basis is not justified; put it in `disclosure_requests` instead. Reply exactly in the drafting output contract: `## Deliverable` (with the H3 sections named above), `## Rationale`, `## Assumptions`, `## Open Questions`, then one final fenced `json` envelope. No preamble before `## Deliverable`; nothing after the envelope. Reuse locked preferred terms verbatim; declare any other term in `new_terms` with a reason.

## Prompt 22 — Broad independent claims  (kind `drafting`)

**Write your reply to:** `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/22.md`

*Draft the commercial perimeter.*

Draft alternative independent claims directed to the core commercial architectures. Use the fewest limitations reasonably necessary to distinguish the known art while maintaining clarity, support and enablement. For each limitation provide: reason included, specification support, likely prior-art vulnerability and likely design-around route.

**How to work.** The description in front of you is the only source of support. Any limitation that lacks an explicit passage in the description must NOT be drafted: leave it out, and record it in `disclosure_requests` (limitation, and the disclosure ip-spec would need to add) so the inner loop can supply the support. Use locked preferred terms verbatim and the registry's component names; where a claim term needs a reference sign, use the registry numeral. Cite the supporting paragraph for every limitation in `support_refs`. Under `### Independent Claims` write each claim in full, numbered, in plain text (no markdown inside the claim), one claim per justified family from `21`. Under `### Limitation Table` give, for every limitation of every independent claim: claim | limitation (quoted) | reason included | specification support (paragraph numbers) | prior-art vulnerability (cite the `09` row or `07` chart) | design-around route. Test each limitation against 'is this needed to distinguish the charted art?'; if not, remove it and note the removal in `## Rationale`. Reply exactly in the drafting output contract: `## Deliverable` (with the H3 sections named above), `## Rationale`, `## Assumptions`, `## Open Questions`, then one final fenced `json` envelope. No preamble before `## Deliverable`; nothing after the envelope. Reuse locked preferred terms verbatim; declare any other term in `new_terms` with a reason.

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

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P2/07.md`

````markdown
## Deliverable

### Prior-Art Claim Charts

This is a drafting and analysis aid prepared by AI. It is not legal advice and gives no view on validity; qualified patent counsel signs off before anything is filed.

**What was charted.** Every reference in `prior-art/INDEX.md` (15 files under `prior-art/refs/`) and both requester-supplied files under `intake/prior-art/`: 17 references in all. Each chart quotes only the saved file.

- The 15 `refs/` files are **machine-retrieved extracts**: the abstract, the claims and a description cut off after a few thousand characters. When a row is marked *absent* for one of these, it means the saved extract does not contain the feature. The full document must be read before anyone relies on that absence.
- Several statements in INDEX.md are **not in the saved text**. These are US4462449A's "swept through"/cleaning statement, US11904644B2's annular air flow around the seat, and EP4735276A1's clogging passage. The charts below do not rely on them (Q3).
- `ref-01` and `ref-02` are marked **FICTIONAL** by the requester. Each is a summary, not a document, with fictional numbers and dates. They are charted as supplied, and their paragraph numbers are the ones the summaries give (Q2).
- There is **no Gate 1 answers file**. Gate 1 locked the terminology unattended, so every Phase 1 open question is still open (A1).

**Rows.** The rows are taken from `03` and use locked terms:

| Row | Feature (03 item) |
|---|---|
| F0 | Valve core of an inflation valve for a tyre (C26, C29 context) |
| F1 | Liquid sealant in the inflatable chamber, with sealant film on valve surfaces as the problem (C31) |
| N0a | The poppet opens the main passage by a normal stroke at the crack pressure (C1) |
| N0b | A threshold-setting arrangement: the poppet over-travels beyond the normal stroke only above an over-travel threshold that is higher than the crack pressure (C2, C3, C18) |
| N0c | The purge shoulder bears on a deflectable ring element **only during over-travel** and deflects it (C4, C5) |
| N0d | That deflection opens a purge gap, closed at rest and separate from the main passage. The air purge flows through it across the sealant-bearing surfaces into the inflatable chamber (C6, C7) |
| N0e | When the pressure differential falls, shape recovery of the deflectable ring element closes the purge gap (C8) |
| N1 | Snap-back wipe: the recovering ring element moves across the poppet and shears off sealant film (C9) |
| N2 | The deflectable ring element is the seat ring: the sealing face rests on its sealing edge (C10, C11) |
| N3 | A convoluted wall converts axial load into radial deflection (C12, C13) |
| N4 | The seat ring is a superelastic alloy (NiTi; austenite finish temperature below 5 °C) (C14–C16) |
| N5 | The return spring has a first spring stage and a second spring stage (C17) |
| N6/7 | The inventor's believed ranges, prototype values and process (C19–C28) |

**Status key:**
- **E**: explicit.
- **I**: implicit or inherent.
- **?**: ambiguous.
- **A**: absent from the saved text.
- **A†**: absent as defined, but a functional analogue is present. The analogue matters for inventive step, not for novelty.

#### Overview grid (single-reference; one row per reference)

| Reference (INDEX #) | Type | Priority | F0 | F1 | N0a | N0b | N0c | N0d | N0e | N1 | N2 | N3 | N4 | N5 | N6/7 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ref-02-elastomer-seat-valve.md | fictional summary | 2018 (fict.) | E | ? | E | A | ? | ? | E | A | E | A | ? | A | A |
| US4462449A.md (#6) | extract | 1982 | E | A | E | A | ? | A | I | ? | A | A | A | A | A |
| EP1137892A1.md (#14) | extract | 1998 | E | A | E | ? | A | ? | ? | A | A | A | A | ? | A |
| US4719938A.md (#3) | extract | 1985 | A | A | E | A | A | A | A | A† | A | A | A | A | A |
| US9982818B2.md (#1) | extract | 2015 | A | A | A | A | A | A | A | A | A | ? | E | A | A |
| US6393765B1.md (#5) | extract | 2000 | A | A | A | A | A | A | A | A | ? | A | E | A | ? |
| US11904644B2.md (#2) | extract | 2019 | E | E | ? | A | A | A | A | A | A | A | A | A | A |
| ref-01-sealant-resistant-core.md | fictional summary | 2017 (fict.) | E | E | I | A | A | ? | A | A | A | A | A | A | ? |
| US11345196B2.md (#4) | extract | 2020 | E | E | ? | A | A | A | A | A† | A | A | A | A | A |
| US4408632A.md (#13) | extract | 1981 | A | A | E | ? | ? | A | A | A | ? | A | A | A | A |
| US6006954A.md (#7) | extract | 1997 | A | A | A | A | A | A | A | A† | A | A | A | A | A |
| CN215861914U.md (#11) | extract (machine translation) | 2021 | E | A | E | A | A | A† | A | A | A | A | A | A | A |
| US4627461A.md (#12) | extract | 1985 | A | A | A | A† | A | A | A | A† | A | A | A | ? | A |
| US9297373B2.md (#15) | extract | 2011 | A | A | E | A | A | A | A | A | A | A | A | ? | A |
| US11179979B2.md (#8) | extract | 2016 | E | E | I | A | A | A | ? | A | A | A | A | A | A |
| US11065925B2.md (#9) | extract | 2017 | E | E | I | A | A | A | A | A | A | A | A | A | A |
| EP4735276A1.md (#10) | extract | 2023 (pub. 2026-05-06) | E | E | A | A | A | A | A | A | A | A | A | A | A |

**What the grid shows, stated as fact and not as a conclusion:**
- None of the 17 references discloses N0b, N0c as defined ("only during over-travel") or N0d as defined (a separate purge gap) explicitly or implicitly, and none discloses N1.
- The rows that come closest are ambiguous: ref-02 claim 4 and US4462449A claim 1 for N0c; EP1137892A1 for N0b and N0d.
- Each of the following is disclosed somewhere, but in a different reference, and none of them in a tyre valve that holds liquid sealant:
  - the material (US9982818B2, US6393765B1);
  - the wave geometry (US9982818B2);
  - wiping on closing (US4719938A, US6006954A);
  - a threshold-opened second opening in a tyre valve core (EP1137892A1).
- All references predate the 2026-08-30 disclosure date. EP4735276A1, published 2026-05-06, is the most recent.

#### ref-02-elastomer-seat-valve.md

Requester-supplied (`intake/prior-art/`). The file states it is **fictional**: "EP 3 456 789 B1", proprietor Vellmar Reifentechnik GmbH (fictional), priority 9 June 2018. It is a summary with paragraph citations and has no full text. It is the closest reference to N0 in the pile.

| Row | Status | Passage (location) | Note |
|---|---|---|---|
| F0 | E | "a tyre valve — for bicycles and light vehicles — in which the seat against which the poppet seals is an elastomeric ring (element 12)" (Summary, first paragraph) | Tyre inflation valve with a poppet. The summary does not say whether it is a removable valve core |
| F1 | ? | "so that the seal is maintained despite particulate contamination of the sealing surfaces" ([0008]); stated problem "sealing against dust and sealant particles" (Summary) | Sealant is present only as particulate contamination to be sealed around. Removal of sealant film is not described |
| N0a | E | Claim 1: "a body, a poppet, and a seat formed by an elastomeric ring retained in the body" | Poppet valve opened by inflation. Crack pressure is not quantified |
| N0b | A | — | The summary's own note: "no over-travel distinct from normal opening, and no two-stage spring" |
| N0c | ? | Claim 4: "the seat being a lip seal deflectable by the poppet during opening" | The poppet deflects the ring element, but **on every opening**. There is no separate purge shoulder and no over-travel. The closest disclosure of N0c in the pile |
| N0d | ? | [0019]: the lip "deflects outward to enlarge the flow passage and reduce the pressure drop across the valve" | The deflection enlarges the **main passage**. No separate purge gap is closed at rest, and air flow across sealant deposits is not described |
| N0e | E | [0020]: on removal of the pump the lip "returns under its own elasticity" to seal | Recovery on removal of the inflation device is disclosed. It closes the main passage, not a purge gap |
| N1 | A | — | No wipe. The elastomer is chosen to seal around particles (reviewer's note) |
| N2 | E | Claim 1 (seat formed by the elastomeric ring); Summary | The ring element is the seat. Its material is 60–80 Shore A nitrile or fluoroelastomer ([0015]–[0021]) |
| N3 | A | — | An elastomeric ring or moulded lip ([0015]–[0021]). No convoluted wall |
| N4 | ? | [0024]: "the seat ring may alternatively be formed of a resilient thermoplastic elastomer or a spring steel lip seal" | A metallic resilient seat is named in a single sentence, with no geometry. There is no superelastic alloy and no Af |
| N5 | A | — | — |
| N6/7 | A | 60–80 Shore A; retained "in a groove" ([0015]–[0021]) | None of our ranges or process. Retention is by a groove, not by an interference fit |

#### US4462449A.md

INDEX #6. Machine-retrieved extract: Zabel, "Valve core for pneumatic tires", priority 1982-02-02. It is the closest **real** reference on the N0 row set, because a moving closure member deforms a resilient member only after an initial part of its travel.

| Row | Status | Passage (location) | Note |
|---|---|---|---|
| F0 | E | Title; claim 6 "A core for a valve stem"; field "automobile and truck tires" (Background) | Tyre valve core |
| F1 | A | "road soil enters the conventional cores ... to impair the normal operation thereof" (Background) | The contaminant is road soil, not liquid sealant. The INDEX's "swept through" statement is not in the saved text |
| N0a | E | Claim 1: "means for resiliently urging said [closure member] toward said distal end whereby said head portion normally blocks fluid ... communication", allowing it "to be moved towards said high pressure area" | A spring-biased closure member (the reference's hollow member with a head portion maps to the poppet). The saved text does not say whether pressure differential or a pump pin moves it |
| N0b | A | — | No threshold separates two flow states. No flow reaches the chamber until the resilient member is penetrated, so there is no normal-open state with main-passage flow |
| N0c | ? | Claim 1: the hollow closure member is "not contacting said elastomeric member unless moved toward said elastomeric member to penetrate and move through said elastomeric member" | The resilient member is deformed only after an initial part of the stroke, which is structurally analogous to N0c. It is the only flow path, however, so the deformation is required on every inflation. It is not a purge added on top of normal opening |
| N0d | A | Claim 1: flow "through the hollow of said [closure member]" | Flow runs through the bore of the moving member, not through a gap opened by deflection |
| N0e | I | Claim 1: a "flexible tubular elastomeric member" that normally prevents fluid communication and is penetrable | Because the member is normally closed, it must re-close on withdrawal. That is elastic recovery closing a path, but of an elastomer |
| N1 | ? | — | Withdrawal through a re-closing elastomer involves sliding contact, but the extract says nothing about removing deposits. An examiner could argue inherency. The full text must be read (Q3) |
| N2 | A | — | The head portion seals the distal end opening. The elastomeric member is a second closure in series, not the seat |
| N3 | A | — | Elastomeric tube |
| N4 | A | — | — |
| N5 | A | Claims 4, 9: "a spring for biasing" | A single spring |
| N6/7 | A | — | — |

#### EP1137892A1.md

INDEX #14. Machine-retrieved extract: Sumnett Inc., "Pressure regulating tire valve and core", priority 1998-10-23. It is a tyre valve core in which a calibrated spring lets a moving member open a second opening above a pressure threshold.

| Row | Status | Passage (location) | Note |
|---|---|---|---|
| F0 | E | Abstract "tire stem valve (1) possessing a built-in calibrated air pressure regulator"; last claim (printed "3."): "a modified valve stem core" | Tyre valve core |
| F1 | A | — | No sealant |
| N0a | E | Claim 1(b) "a one-way valve for inflating the tire"; claims 16–17 (ball valve with "a ball, a cylindrical housing having apertures, and a spring") | The inflation check valve is a **separate** member from the pressure-regulating disk |
| N0b | ? | Claim 1(c)–(e): the movable disk moves "in response to an increase or decrease in the internal pressure of the tire" and bleed apertures "allow air to exit ... when air pressure inside the tire exceeds a desired value" | A second opening appears above a pressure threshold. The threshold is on **chamber-side** pressure, the member is not the inflation poppet, and the flow is **out** of the tyre. It is not over-travel of the inflation poppet |
| N0c | A | — | Nothing on the inflation member deflects a ring element |
| N0d | ? | Claim 8: the aperture "comprises a gap between" the reference's elastomeric sealing ring "and the second solid support"; last claim: the sealing ring "moves ... when the internal pressure of the tire exceeds a desired value creating an aperture through which excess air escapes" | A gap bounded by a moving sealing ring opens above a threshold. The ring moves bodily and is not deflected, and the air goes to atmosphere, not across sealant surfaces into the chamber |
| N0e | ? | Claim 1(c): the disk effects "a substantially air-tight seal when the tire pressure is at or below the desired value" | The gap is closed again by spring return of the disk, not by shape recovery of a ring |
| N1 | A | — | — |
| N2 | A | Claim 25: "rubbery or coating" on disk and support | — |
| N3 | A | — | — |
| N4 | A | — | — |
| N5 | ? | Claim 28(d)–(e): "a spring" and "a second spring ... positioned between the movable disk and a second solid support ... on the tire-side"; claim 10: a support "to limit the linear travel of the movable disk" | Two springs act on one moving member, from opposite sides. They are not sequential first and second spring stages. A travel stop is disclosed |
| N6/7 | A | — | Claims 21–23 describe an audible whistle, which is unrelated to our audible snap |

#### US4719938A.md

INDEX #3. Machine-retrieved extract: Helix Technology, cryopump pressure relief valve, priority 1985-01-22. Its function is closest to N1.

| Row | Status | Passage (location) | Note |
|---|---|---|---|
| F0 | A | "pressure relief valves on cryopumps" (Technical Field) | Not a tyre valve |
| F1 | A | "debris" (Abstract) | Contamination, but not sealant film |
| N0a | E | Abstract: "In opening, the valve member moves away from an end port to open [side] ports in the side of the valve cylinder" | A pressure-actuated valve member opening a flow path |
| N0b | A | — | Single stage |
| N0c | A | Abstract: "A taper is provided on the inner surface of the cylinder to release compression on the vacuum sealing [elastomeric ring] upon opening and to compress [it] as the valve member moves to the closed position" | The seal is compressed or released by the taper as the valve moves. There is no purge shoulder and no over-travel |
| N0d | A | — | — |
| N0e | A | — | — |
| N1 | A† | Abstract: "As the valve member is moved into the closed position in response to an atmospherical pressure differential, a wiper ring cleans debris from the inner surface of the valve cylinder"; "The wiper ring is expansible in order to provide a wiping action along the entire taper"; claim 5: "a z-cut to allow for expansion and ... a spring ring pressing outward against the wiper ring"; claim 1: the wiper "preceding the seal ring ... as the valve member is moved to the closed position" | A radially resilient ring wipes on the closing stroke, which is driven by the pressure differential. The kinematics differ from ours: the wiper is **carried by the moving member** and wipes the **fixed bore**, and the motion comes from the valve member's stroke, not from recovery of the ring |
| N2 | A | — | The seal ring is on the valve member |
| N3 | A | — | A z-cut split ring, not a convoluted wall |
| N4 | A | — | — |
| N5 | A | "the pressure relief valve is a springloaded valve which opens when the pressure ... exceeds about 3 pounds per square inch gauge" (Background) | A single spring, and this is background art |
| N6/7 | A | — | — |

#### US9982818B2.md

INDEX #1. Machine-retrieved extract: UTC Aerospace Systems, "Shape memory alloy sealing ring and assembly", priority 2015-11-23. It is the closest reference for material plus geometry.

| Row | Status | Passage (location) | Note |
|---|---|---|---|
| F0 | A | "sealing an inlet tube within the housing of a differential pressure flow meter/sensor" (Background) | A static seal between two members |
| F1 | A | — | — |
| N0a–N0e | A | — | No moving closure member, no purge gap and no pressure-actuated recovery (each row is absent; they are grouped for brevity) |
| N1 | A | — | — |
| N2 | A | Claim 1: the ring sits "between the first and second member ... the radially inner sealing portion faces the first member and the radially outer sealing portion faces the second member" | Nothing seats on it |
| N3 | ? | Abstract: a shape "between a radially inner sealing portion and radially outer sealing portion ... which has at least one peak and at least one trough"; claims 3–4 ("S-shaped", "sinusoidal"); claim 5: heating "causes the radially inner sealing portion to move radially inwardly and the radially outer sealing portion to move radially outwardly" | A wave-profile ring with radial movement is explicit. The radial movement is produced by **heating** (shape recovery), not by conversion of axial load. The extract gives no dimensions or wall-profile orientation |
| N4 | E (material) / ? (superelastic in service) | Claims 9, 11: "the SMA comprises an NiTi alloy"; Background: "when above the transformation temperature, the SMA may exhibit pseudoelastic behaviour ... absorb high strains whilst maintaining a certain stress or sealing force, which gives such sealing members a high fatigue resistance" | NiTi is explicit. Pseudoelasticity is mentioned as a possible property, and the claimed action is thermal (claim 10). No Af value is given |
| N5 | A | — | — |
| N6/7 | A | Claim 10: deforming "below the martensitic phase transformation temperature" then "heating ... above the austenitic phase transformation temperature" | A different process: deformation followed by thermal recovery. No laser cutting, shape-setting fixture or electropolishing |

#### US6393765B1.md

INDEX #5. Machine-retrieved extract: US Navy, "Superelastic sealing closures", priority 2000-08-24.

| Row | Status | Passage (location) | Note |
|---|---|---|---|
| F0 | A | "sealing closures such as those associated with hangar doors and hatches onboard marine vessels" | — |
| F1 | A | — | — |
| N0a–N0e | A | — | No valve (each row is absent; they are grouped for brevity) |
| N1 | A | — | — |
| N2 | ? | Summary: sheet metal positioned on the edge surfaces of rigid structural parts "as seal elements to be deformed by engagement in response to closure displacement" | A superelastic seal element deformed by a moving closure part. It is not a valve seat, and nothing is said about the contact being repeated in service |
| N3 | A | Claims 3, 6–8: "arcuate contact portion", "loop-shaped ends", "gutter shaped intermediate portions", "cross-sectionally oval shape" | Loop-shaped and oval sections, not a convoluted wall that converts axial load into radial deflection |
| N4 | E | Claim 1: the sheet metal element is a shape memory alloy "selected for endowment thereof with superelastic properties"; Abstract: the element is formed as a NiTi alloy | Superelastic NiTi used as a repeatedly deformed seal element. No Af value is given |
| N5 | A | — | — |
| N6/7 | ? | Summary: NiTi alloying "by undergoing thermo-mechanical treatments already known in the art" | A generic reference to known treatment. No specific process |

#### US11904644B2.md

INDEX #2. Machine-retrieved extract: Santa Cruz Bicycles, "Inflation system for tubeless tires", priority 2019-04-17. It is the closest real reference for field and problem.

| Row | Status | Passage (location) | Note |
|---|---|---|---|
| F0 | E | Abstract: "An inflation valve for a tubeless tire ... A valve stem extends through the cavity and includes a plug" | The reference's "valve stem" with its plug maps to our **poppet**, and its "valve body" to our core body or valve stem |
| F1 | E | Introduction: existing valves "are often clogged by sealant due to their small diameter"; "sealant must be present in the air mixture filling the tires" | Same problem. Its answer is a larger flow path |
| N0a | ? | Abstract: the valve moves between "a closed position, where a resilient surface of the plug engages the beveled surface" and "an open position, where the resilient surface ... is spaced from the beveled surface"; claim 1(c): open when "the cap is axially transitioned toward the proximal end" | Opening is by moving the cap, not stated to be by pressure differential. Claim 4: the seat is held closed "by force exerted by air pressure within the tubeless tire" |
| N0b | A | Claim 1(a)–(c): cap positions (screwed fully on / partially unscrewed / open) | Positions set by hand, not a pressure threshold |
| N0c | A | — | — |
| N0d | A | Claim 1: a cap channel "configured to direct a flow of air to exit the valve" | This path carries air out of the valve. The INDEX's "annular air flow around the seat" is not in the saved text |
| N0e | A | — | — |
| N1 | A | — | — |
| N2 | A | Claim 1: "a resilient seating surface" on the plug, seating on a rigid "valve seat" | The resilient part is on the **moving** member (claim 2 names an elastomeric sealing ring). The fixed seat is rigid |
| N3–N5 | A | — | Each row is absent; they are grouped for brevity |
| N6/7 | A | — | — |

#### ref-01-sealant-resistant-core.md

Requester-supplied and **fictional**: "US 2019/0123456 A1", Northbridge Cycle Components (fictional), filed 18 October 2017. It is a summary only.

| Row | Status | Passage (location) | Note |
|---|---|---|---|
| F0 | E | Brass body, poppet (24), seat (30) ([0012]–[0028], Figs. 1–3) | Presta-pattern valve core |
| F1 | E | "latex tyre sealant drawn into a … valve core during inflation, drying on the seat and poppet, and causing leak or blockage" (Summary) | The same problem as §1 |
| N0a | I | Poppet (24) with conical sealing face and seat (30) ([0012]–[0028]) | A conventional pressure-opened valve core, by implication |
| N0b | A | Reviewer's note: "No over-travel of the poppet, no secondary spring stage" | — |
| N0c | A | — | — |
| N0d | ? | [0022]: the enlarged bore "allows the inflation air stream to carry loose sealant back into the tyre" | The air carries sealant through the **main passage** (a 2.8 mm bore). There is no gap opened by deflection. Marked ambiguous as the file directs |
| N0e | A | — | — |
| N1 | A | Fluoropolymer layer (26), 10–25 μm, "reducing adhesion of cured latex" | Reduces adhesion; does not remove a formed sealant film |
| N2 | A | "The seat (element 30) is a rigid brass shoulder machined in the body" | A rigid seat |
| N3 | A | [0036]: the sleeve "may be provided with a slight flare at its lower edge" | A flare on the sleeve, not a convoluted wall |
| N4 | A | — | — |
| N5 | A | — | — |
| N6/7 | ? | Sleeve (40) "press-fitted into the lower bore" ([0030]–[0041]) | A press fit of an annular part in the core body is disclosed, but for a sleeve described as removable, not a seat ring. None of our ranges |

#### US11345196B2.md

INDEX #4. Machine-retrieved extract: Kunshan Fuluo, "Tire valve assembly", priority 2020-04-14.

| Row | Status | Passage (location) | Note |
|---|---|---|---|
| F0 | E | Field: "a tire valve assembly which is used on the wheel frame of the bicycle" | — |
| F1 | E | Background: repeated inflation means "the end of the valve is often affected by the tire repair liquid ... reduced air intake, and even obstruction" | Same problem as F1 (blockage) |
| N0a | ? | Claim 2: the second seal ring "is pushed by the movable screw to move out of the smooth section", after which inflator air flows into the tyre | The saved text does not say whether the screw is moved by the pressure differential or by hand. Claim 3: a limiting nut sets "a displaceable length" |
| N0b | A | Claim 1: limiting nut "to limit a displaceable length of the movable screw" | A travel limit, not a pressure threshold |
| N0c–N0e | A | — | Each row is absent; they are grouped for brevity |
| N1 | A† | Abstract: "When the movable rod is reinstalled in the air pipe, the tire repair liquid remaining on the inner wall of the air pipe will also be squeezed out"; claim 1: "friction exists between the second seal ring and the smooth section" as the rod "is pushed and pulled" | Sealant is removed by a sealing ring on a **moving** rod sliding over a fixed wall. The stated occasion is maintenance (reinstallation). Claim 1's friction on every push and pull could be argued as a wipe on each opening. It is not recovery of a ring |
| N2 | A | — | The seal ring is on the moving rod |
| N3–N6/7 | A | — | Each row is absent; they are grouped for brevity |

#### US4408632A.md

INDEX #13. Machine-retrieved extract: Brunswick Corp., "High flow shroud check valve", priority 1981-04-23.

| Row | Status | Passage (location) | Note |
|---|---|---|---|
| F0 | A | "a check or relief valve" (Technical Field) | — |
| F1 | A | Background: "foreign bodies on one or the other of the mating elements ... caused leaks" | Contamination in general only |
| N0a | E | Claims 5–6: a spring moves the poppet valve to the closed position | Spring-biased check-valve poppet |
| N0b | ? | Claim 7: the flow ports "move between a closed position within said inlet fitting to a position partially or wholly open into said valve chamber" | Opening progresses with travel. No second pressure threshold is disclosed |
| N0c | ? | Claim 3: "a flange on said poppet valve ... engaging with said lip to move said shroud means and seal ring in an axial direction with said poppet valve during opening" | A formation on the poppet engages a ring-carrying part during opening. It moves the part axially and does not deflect it radially, and the contact is not limited to over-travel |
| N0d | A | Claim 4: apertures in the lip where "high flow ... reduces pressure in said apertures to seat the seal ring" | The flow holds the ring in place. It is not a purge |
| N0e | A | — | — |
| N1 | A | — | — |
| N2 | ? | Claim 1: "an annular resilient seal ring encircling said poppet valve ... to seal said seal ring between said two second sealing surfaces" | A resilient ring forms part of the seal but is carried with the poppet. Claim 8 names an elastomeric sealing ring |
| N3–N6/7 | A | — | Each row is absent; they are grouped for brevity |

#### US6006954A.md

INDEX #7. Machine-retrieved extract: Bespak, "Metering valve", priority 1997-06-10.

| Row | Status | Passage (location) | Note |
|---|---|---|---|
| F0 | A | "metering valves for pressurised dispensing containers" | — |
| F1 | A | "deposition of the solid product on the inner surfaces of the metering chamber" | Deposits analogous to sealant film, but in an aerosol valve |
| N0a | A | — | The valve stem is displaced by the user, not by a pressure differential |
| N0b–N0e | A | — | Each row is absent; they are grouped for brevity |
| N1 | A† | Claim 1: "the wiper means scrapes the inner surface to thereby remove solid matter deposited thereon" as the stem slides; claim 6: "at least the perimeter of the wiper means is flexible and is deformed against the inner surface" | A flexible wiper **on the moving member** removes deposits from a fixed wall on each stroke. It is not a ring recovering across the closure member |
| N2 | A | — | — |
| N3 | A | — | — |
| N4 | A | Claims 11–12: plastics; acetal or polyester | — |
| N5 | A | Claim 13: "a helical spring biasing the valve stem to its rest position" | A single spring |
| N6/7 | A | — | — |

#### CN215861914U.md

INDEX #11. Machine-retrieved extract, read in **machine translation**: Jinan Weidisi, central tyre inflation and deflation system valve, priority 2021-09-29.

| Row | Status | Passage (location) | Note |
|---|---|---|---|
| F0 | E | Claim 1: "a valve body, a control valve and a one-way locking valve" | Tyre valve for a vehicle central inflation system |
| F1 | A | Abstract: "sand, water and the like" | No sealant |
| N0a | E | Claim 1: "the one-way locking valve comprises a valve core seat and a guide rod ... a second spring ... abutted to the valve core seat", with "a conical valve seat" | Spring-biased check valve |
| N0b | A | — | The control valve is operated by the system's air-pressure control unit. The saved text gives no pressure stages for this device |
| N0c | A | — | — |
| N0d | A† | Abstract: "in the exhaust process, dust and silt attached to the outer surface of the filter element are blown off by airflow with certain air pressure" | Pressurised air flow removes deposits inside a tyre valve. This happens on exhaust (deflation), at a filter element, and not through a gap opened by deflection |
| N0e | A | — | — |
| N1 | A | — | — |
| N2 | A | Claim 1: an annular sealing element "arranged inside the exhaust port"; claim 9: first sealing member "forms a lip seal" | — |
| N3–N6/7 | A | Claim 8: conical surface at "15 to 20 degrees" | Each row is absent; they are grouped for brevity |

#### US4627461A.md

INDEX #12. Machine-retrieved extract: K.J. Baillie, rotating-closure valve for caustic service, priority 1985-10-03.

| Row | Status | Passage (location) | Note |
|---|---|---|---|
| F0 | A | "a circular valve seat on which deposits can build up to impair effective closing" (Field) | Process valve |
| F1 | A | "caustic build up on the valve seat" | Deposit analogue only |
| N0a | A | — | Driven by an actuator |
| N0b | A† | Abstract: "When the member engages the valve seat further rotation of the spindle causes the collar to ride up the spindle against the spring bias which maintains the closing force on the member while allowing it to rotate to clean the closing surfaces" | Driven movement continues beyond seat contact, against a spring, to perform cleaning. It is actuator-driven and on closing, not over-travel above a pressure threshold on opening |
| N0c–N0e | A | — | Each row is absent; they are grouped for brevity |
| N1 | A† | State of the Art: "the rotation of the closure member grinds away any sediment which has built up on the seat" | Seat cleaning by movement of the closure member during closing. It is not recovery of a ring element |
| N2 | A | — | — |
| N3 | A | — | — |
| N4 | A | — | — |
| N5 | ? | Claim 3: "said spring offers a progressively increasing resistance to compression" | A rising-rate spring, but in a cushioning role. It is not first and second spring stages biasing a poppet |
| N6/7 | A | — | — |

#### US9297373B2.md

INDEX #15. Machine-retrieved extract: Nuovo Pignone, differential pressure poppet valve, priority 2011-07-19.

| Row | Status | Passage (location) | Note |
|---|---|---|---|
| F0 | A | "reciprocating compressor valves, such as ... poppet valves of hyper compressors" | — |
| F1 | A | — | — |
| N0a | E | Claim 1: "the shutter being movable between an open position and a closed position under a differential pressure across the valve"; claim 6: "poppet shutter" | — |
| N0b | A | — | Progressive rate, but no defined second threshold |
| N0c–N4 | A | — | Each row is absent; they are grouped for brevity |
| N5 | ? | Claim 1: "at least two pre-loaded compression springs arranged in parallel ... both the two springs are non-linear, and ... progressive springs" | A rising-rate biasing member on a poppet. It is not a soft first spring stage followed by a stiff second spring stage, and the stated purpose is suppressing spring surge |
| N6/7 | A | — | — |

#### US11179979B2.md

INDEX #8. Machine-retrieved extract: Sport Components AG, "Valve for tubeless tires", priority 2016-08-18. Claim 1 is in the saved text.

| Row | Status | Passage (location) | Note |
|---|---|---|---|
| F0 | E | Claim 8: "a Presta-type valve core or a Schrader-type valve core inserted in the valve stem body" | — |
| F1 | E | Abstract: "a method to test the amount of sealant in a wheel and a refilling assembly" | The sealant context is explicit. That the duckbill stops sealant entering is **not** stated in the saved text |
| N0a | I | Claim 8 (a conventional valve core as the second valve) | — |
| N0b–N0d | A | — | Each row is absent; they are grouped for brevity |
| N0e | ? | Claims 1–5: "a self-sealing one-way valve" (duckbill, "sealing lip", "slit", "rubber and silicone") | The elastic lips re-close after flow. That is elastic recovery closing a path, but in a separate valve and not a purge gap |
| N1 | A | — | — |
| N2 | A | — | — |
| N3–N6/7 | A | — | Each row is absent; they are grouped for brevity |

#### US11065925B2.md

INDEX #9. Machine-retrieved extract: Liquitube, "Valve stem apparatus", priority 2017-12-15.

| Row | Status | Passage (location) | Note |
|---|---|---|---|
| F0 | E | Background: "depressing the valve core to let air out"; claim 3: "a valve disposed in the first tubular body" | — |
| F1 | E | "valve stems that resist clogging when a sealing material is introduced" (Field); claim 13: "natural rubber latex" | Same problem. Background: clogging can leave "the inner valve getting stuck open" |
| N0a | I | Background: a valve "seated by a compression spring within the axial airway" | Conventional valve |
| N0b–N0c | A | — | Each row is absent; they are grouped for brevity |
| N0d | A | Claim 1: "a supplemental air hole ... extending radially through the second tubular body" | A permanently open extra hole downstream of the valve. It is not opened by deflection |
| N0e–N6/7 | A | — | Each row is absent; they are grouped for brevity |

#### EP4735276A1.md

INDEX #10. Machine-retrieved extract, published 2026-05-06 (priority 2023-08-18). The applicant is not given in the saved text.

| Row | Status | Passage (location) | Note |
|---|---|---|---|
| F0 | E | Claim 1: "An inflation valve for use with a tubeless tyre, the inflation valve comprising a ball valve"; [007] names the valve core | It replaces the poppet valve core |
| F1 | E | Claim 2: "air and/or sealant is allowed to flow through the through-hole"; [007](a): "narrow or restrictive valve core design. This can impede the airflow through the valve" | Restricted flow is explicit. A statement about sealant clogging is not in the saved text |
| N0a–N6/7 | A | — | Rotary ball valve. No poppet, seat ring or spring stages (all rows absent) |

#### Combination analysis (inventive step only; not used for novelty)

The novelty charts above are single-reference. The following are only the combinations that the rows make available to an examiner; Prompt 08 builds and rates them.

1. **N0 (threshold-opened purge through a deflected seat):**
   - ref-02 supplies: a seat ring deflected by the poppet on opening (claim 4), enlargement of the main passage by that deflection ([0019]), and recovery on removal of the pump ([0020]).
   - EP1137892A1 supplies: a tyre valve core in which a calibrated spring lets a gap open above a pressure threshold (claims 1(e), 8).
   - CN215861914U supplies: removal of deposits in a tyre valve by pressurised air flow.
   - US4462449A (real art) can stand in for ref-02 on "the moving member deforms a resilient member only after initial travel" (claim 1).
2. **N1 (wipe on closing):** ref-02 or US4462449A combined with US4719938A (wiping on the closing stroke by a radially resilient ring, driven by the pressure differential) or US6006954A (a flexible wiper removing deposits on each stroke). US11345196B2 is the tyre-valve analogue (a sealing ring on a moving rod removing sealant from the bore).
3. **N3/N4 (convoluted superelastic seat ring):** ref-02 [0024] (a resilient metal seat as an alternative) combined with US9982818B2 (wave-profile NiTi sealing ring with radial movement; pseudoelastic "high fatigue resistance") and/or US6393765B1 (superelastic NiTi seal element deformed by the closing part).
4. **N5 (two-stage return spring):** any of the above combined with US9297373B2 (progressive springs on a poppet), EP1137892A1 claim 28 (two springs on one moving member) or US4627461A claim 3 (progressive spring).

**Coverage.** The coverage is **thin**:
- 15 web-retrieved extracts plus 2 fictional summaries;
- English-language, from a single search engine;
- one Chinese utility model;
- no non-patent literature;
- no classification walk of the F16K 15/20 and B60C 29/00 groups (INDEX, "Coverage statement").

These charts cannot show that the art is clear. A professional search is warranted before Phase 3 relies on them (Q1).

## Rationale

**How the rows were built.** They follow `03`: N0 is split into its five elements (a)–(e), then the ladder N1–N7. The context is split into F0 (tyre valve core) and F1 (sealant). The split matters because several references are close on context and nowhere on mechanism (US11904644B2, US11065925B2, EP4735276A1, ref-01), and others are the reverse (US9982818B2, US4719938A). N6 and N7 share a row because no reference comes near any value or process step.

**Order of the charts.** They are ordered by how dangerous the reference is to N0 on a hostile reading, not by INDEX number:
- ref-02 comes first even though it is fictional, because claim 4 plus [0019]–[0020] give a seat ring that the poppet deflects and that recovers on removal of the pump. This is the nearest thing in the pile to N0c–N0e.
- US4462449A is the real-art counterpart. Its closure member deforms a resilient member only after initial travel, which an examiner will read against a loosely worded N0c. I charted that as ambiguous rather than absent.
- EP1137892A1 is the only tyre-valve reference with a threshold-opened second opening.

**Where I held back.** Some statements in INDEX.md are not in the saved text, so I charted from the saved text and not from those statements. The functional analogues of N1 (US4719938A, US6006954A, US11345196B2, US4627461A) are marked A†, not ambiguous. They wipe or grind by movement of the valve member, not by recovery of a ring element, so on a strict single-reference reading N1 is absent from each. The marker keeps them visible for the inventive-step analysis.

**How I handled the gaps.** For machine-retrieved extracts, *absent* means absent from the extract; this is said in the preamble and repeated in Q3, not buried in the notes. The two fictional intake documents are charted as the brief directs. Their fictional status is carried into every downstream use through Q2.

## Assumptions

A1. No Gate 1 answers exist. `runs/r1/gates/gate-1.md` records only an unattended terminology lock, and `intake/answers.md` does not exist. The Phase 1 open questions are therefore treated as unanswered: in particular 01 Q1/Q2 (location and opening of the purge gap), 03 Q1 (purge against wipe) and 03 Q5 (Alternatives A and B within the invention). The N0 rows use `03` as written. Blocking for P3 and P5 until those questions are answered.

A2. The effective date is taken as no earlier than the disclosure date of 2026-08-30 (06 A3). Every charted reference predates it, EP4735276A1 included (published 2026-05-06). Not blocking.

A3. The two fictional intake documents are charted as supplied references for this test matter, with the paragraph numbers their summaries give. Not blocking for P2; blocking for PACKAGE if they are to appear in the Prosecution Assessment as real art.

A4. The reference's own component names are mapped to locked terms in the notes. For example: US11904644B2's "valve stem" with its plug maps to the poppet; US4462449A's hollow closure member maps to the poppet. The mapping is for charting only. Not blocking.

A5. The machine translation of CN215861914U is taken as accurate enough for triage-level charting. Not blocking.

## Open Questions

Q1. Coverage is thin: web-only, English-language, one engine, one Chinese utility model, no non-patent literature and no classification walk. Nothing charted discloses N0b, N0c, N0d or N1. That is a finding about this pile, not evidence that the art is clear. Should a professional search, including a CPC walk of F16K 15/20 and B60C 29/00, CN/TW/JP utility models and superelastic-seat non-patent literature, be commissioned before Phase 3 relies on these charts? Blocks P3, P5, PACKAGE.

Q2. ref-01 and ref-02 are fictional test documents. ref-02 is the closest reference to N0 in the pile. Should the Prosecution Assessment list them as prior art, or should the analysis be rebased on the real references (US4462449A, EP1137892A1) as the closest art? Blocks PACKAGE.

Q3. The charted texts are extracts. Full texts are needed before any *absent* row is relied on. The priorities are:
- US4462449A: the full description, including the inflation-flow statement the INDEX mentions and whether withdrawal of the closure member wipes it;
- US9982818B2: the ring profile, its orientation and its dimensions;
- US4719938A: the wiper geometry;
- EP1137892A1: the description of the travel stop and the second spring;
- US11904644B2: the air flow around the seat;
- EP4735276A1: the clogging passage and the applicant.

Blocks P3, PACKAGE.

Q4. 01 Q1/Q2 are unanswered: where the purge gap is and how it opens against a 0.03 mm interference fit. Every N0d distinction over ref-02 [0019] and EP1137892A1 claim 8 depends on the purge gap being a separate path, closed at rest. Can the inventor describe the air path in words? Blocks P3, P4, P5.

Q5. Have the inventor's prototypes, concept or bench results been shown, used or published before filing (01 Q34)? A disclosure by the inventor would be prior art that is not in this pile. Blocks P2, PACKAGE.

```json
{
  "prompt": "07",
  "status": "partial",
  "assumptions": [
    {"id": "A1", "text": "No Gate 1 answers exist (gate-1.md records only an unattended terminology lock; intake/answers.md absent); Phase 1 open questions treated as unanswered and N0 rows use 03 as written.", "blocking": true},
    {"id": "A2", "text": "Effective date taken as no earlier than the 2026-08-30 disclosure date; all charted references, including EP4735276A1 (published 2026-05-06), predate it.", "blocking": false},
    {"id": "A3", "text": "ref-01 and ref-02 (fictional intake summaries) are charted as supplied references using the paragraph numbers their summaries give.", "blocking": false},
    {"id": "A4", "text": "Reference component names are mapped to locked terms for charting only (e.g. US11904644B2 'valve stem' with plug and US4462449A hollow closure member both map to the poppet).", "blocking": false},
    {"id": "A5", "text": "The machine translation of CN215861914U is taken as adequate for charting.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "Coverage is thin (web-only, English, one engine, one CN utility model, no NPL, no CPC walk); nothing charted discloses N0b, N0c, N0d or N1. Commission a professional search before Phase 3 relies on the charts?", "blocks": ["P3", "P5", "PACKAGE"]},
    {"id": "Q2", "text": "ref-01 and ref-02 are fictional; ref-02 is the closest reference to N0. List them in the Prosecution Assessment, or rebase on the real references (US4462449A, EP1137892A1) as closest art?", "blocks": ["PACKAGE"]},
    {"id": "Q3", "text": "Charted texts are extracts; full texts needed before any 'absent' row is relied on, priority US4462449A, US9982818B2, US4719938A, EP1137892A1, US11904644B2, EP4735276A1.", "blocks": ["P3", "PACKAGE"]},
    {"id": "Q4", "text": "01 Q1/Q2 unanswered: every N0d distinction over ref-02 [0019] and EP1137892A1 claim 8 depends on the purge gap being a separate path closed at rest. Inventor to describe the air path in words.", "blocks": ["P3", "P4", "P5"]},
    {"id": "Q5", "text": "Any public showing, use or publication of the prototypes, concept or bench results before filing (01 Q34)?", "blocks": ["P2", "PACKAGE"]}
  ],
  "new_terms": [
    {"term": "threshold-setting arrangement", "maps_to": "second spring stage", "reason": "Locked genus of the second spring stage; used for row N0b so that the row is not limited to the two-rate return spring (03 C3)."}
  ],
  "support_refs": [
    {"item": "Row definitions F0-N6/7", "support": "runs/r1/P1/03.md N0 (a)-(e), ladder N1-N7, feature classification C1-C31"},
    {"item": "ref-02 N0c/N0d/N0e/N2/N4", "support": "intake/prior-art/ref-02-elastomer-seat-valve.md claim 1, claim 4, [0008], [0019], [0020], [0024]"},
    {"item": "US4462449A N0a/N0c/N0e", "support": "runs/r1/prior-art/refs/US4462449A.md claims 1, 6"},
    {"item": "EP1137892A1 N0b/N0d/N0e/N5", "support": "runs/r1/prior-art/refs/EP1137892A1.md claims 1, 8, 10, 28 and final claim"},
    {"item": "US4719938A N1 analogue", "support": "runs/r1/prior-art/refs/US4719938A.md abstract, claims 1, 5"},
    {"item": "US9982818B2 N3/N4", "support": "runs/r1/prior-art/refs/US9982818B2.md abstract, claims 3-5, 9, 10, background"},
    {"item": "US6393765B1 N2/N4", "support": "runs/r1/prior-art/refs/US6393765B1.md abstract, claim 1, summary"},
    {"item": "US11904644B2 F0/F1/N2", "support": "runs/r1/prior-art/refs/US11904644B2.md abstract, claims 1-4, introduction"},
    {"item": "ref-01 F1/N0d/N1/N2", "support": "intake/prior-art/ref-01-sealant-resistant-core.md [0012]-[0041], [0022], [0036]"},
    {"item": "US11345196B2 N1 analogue", "support": "runs/r1/prior-art/refs/US11345196B2.md abstract, claims 1-3"},
    {"item": "US4408632A N0b/N0c/N2", "support": "runs/r1/prior-art/refs/US4408632A.md claims 1, 3, 4, 7"},
    {"item": "US6006954A N1 analogue", "support": "runs/r1/prior-art/refs/US6006954A.md claims 1, 6, 13"},
    {"item": "CN215861914U N0d analogue", "support": "runs/r1/prior-art/refs/CN215861914U.md abstract, claim 1"},
    {"item": "US4627461A N0b/N1 analogues, N5", "support": "runs/r1/prior-art/refs/US4627461A.md abstract, state of the art, claim 3"},
    {"item": "US9297373B2 N5", "support": "runs/r1/prior-art/refs/US9297373B2.md claims 1, 6"},
    {"item": "US11179979B2, US11065925B2, EP4735276A1 context rows", "support": "runs/r1/prior-art/refs/ files, claims and background as cited in each chart"},
    {"item": "Coverage statement", "support": "runs/r1/prior-art/INDEX.md 'Coverage statement'; runs/r1/P2/06.md Q2"}
  ],
  "disclosure_requests": [
    {"limitation": "N0d purge gap separate from the main passage, closed at rest", "needed_disclosure": "Written description of the surfaces bounding the purge gap, how deflection opens it despite the interference fit, and the full air path into the inflatable chamber (01 Q1, Q2); needed to distinguish ref-02 [0019] and EP1137892A1 claim 8."}
  ],
  "open_disagreements": [],
  "narrowing_suggested": []
}
```
````

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P1/03.md`

````markdown
## Deliverable

### Inventive Nucleus

This analysis was drafted by AI to help with drafting. It is not legal advice and says nothing about whether the invention is patentable. Qualified patent counsel must sign off before anything is filed.

**Sources.** `intake/disclosure.md` is cited as §1–§9, `runs/r1/P1/01.md` as "01 (x)", and `intake/data/bench-test.md` as "bench data". Terms are those used in 01. Three new terms are declared in the envelope:
- **ring element**: the genus covering the seat ring (30) and the inventor's alternative ring parts;
- **threshold arrangement**: the genus covering the two-rate return spring (50) as the thing that sets the over-travel threshold;
- **main passage**: the name the drawings README uses for the normal air path.

Where a classification below is provisional, it is labelled so and tied to an assumption and a Gate 1 question.

**N0 — nucleus (minimum combination, provisional).** A valve core for a tyre that holds liquid sealant, in which:
- (a) the poppet (40) opens the main passage by a normal stroke at the crack pressure;
- (b) a threshold arrangement holds the poppet at its normal stroke until the pressure differential exceeds a higher over-travel threshold, above which the poppet moves beyond its normal stroke (over-travel);
- (c) during over-travel only, the purge shoulder (44) of the poppet bears on a resiliently deflectable ring element and deflects it;
- (d) that deflection opens a purge gap (60), closed at rest, through which inflation air flows across the surfaces on which sealant accumulates and into the tyre (air purge);
- (e) when the pressure differential collapses, the ring element recovers its shape and the purge gap closes.

Why this is the minimum:
- (a)–(e) is the combination common to the §2 concept and to both of the inventor's considered alternatives in §6: Alternative A, a PEEK ring with the same convoluted wall, and Alternative B, a brass seat plus a stainless spring wiper ring "deflected outward by the purge shoulder".
- Nothing narrower is shared by all three.
- The thermal two-way variant (§6) replaces over-travel with warming by hand. It therefore sits outside N0. It is a separate candidate concept pending Q12, and it is not a rung on this ladder.

**N0 enablement caution.** Element (d) is essential, but as the disclosure stands it is not enabled. The location of the purge gap is stated two ways (§2 says the "stem bore"; §3(6) says the "core body bore"). An outward-flexing ring that is interference-fitted in the core body (§7) would ordinarily close a gap at its outer surface rather than open one (01 (m); 01 Q1, Q2). Until the inventor describes the air path in words, the nucleus cannot be written up as enabled (Q2).

**Alternative nucleus reading, pending Q1.** The inventor describes two cleaning actions, and the bench test does not separate them (01 (c), (l); A6 of 01):
- If the inventor confirms that the air purge alone produces the effect, N0 stands as written.
- If the snap-back wipe alone suffices, the minimum would instead be (a)–(c) + (e) + the wipe, and (d) would become advantageous.
- If both are needed, N1 becomes the nucleus.

This is recorded as a question (Q1), not as an embodiment.

**The ladder.** Each rung adds features to the one before.

1. **N1 = N0 + snap-back wipe.** On recovery, the ring element moves across the poppet face and shears off the sealant film (§2). This is still common to the NiTi ring and to Alternative A (§6, with a weaker wipe). Whether it holds for Alternative B's wiper ring is unstated (Q7).
2. **N2 = N1 + the ring element is also the seat.** The sealing face (42) of the poppet seats on the upper edge of the ring element, so a single part both seals and purges (§3(3), §3(4)). This rung covers the prototype and Alternative A. It excludes Alternative B (§6).
3. **N3 = N2 + convoluted wall.** The ring element is a short tube whose wall has one or two shallow convolutions. These convert axial load from the purge shoulder into radial outward expansion (§3(3)). This rung still covers Alternative A, which has "the same convoluted wall" (§6).
4. **N4 = N3 + superelastic alloy.** The ring element is a superelastic alloy, specifically superelastic NiTi, with Af below 5 °C so that it is superelastic at all riding temperatures (§2, §4, §5). This gives the "fast and stiff" recovery that the inventor credits for the strength of the wipe (§2). It excludes Alternative A.
5. **N5 = N4 + two-rate return spring (50).** A soft first stage sets the crack pressure and a stiffer second stage sets the over-travel threshold (§3(5)).
6. **N6 = N5 + the inventor's believed ranges (§4; none evidenced beyond the prototype value, 01 (h), Q13):**
   - crack pressure 0.8–1.5 bar;
   - over-travel threshold 2.5–5.0 bar;
   - over-travel 0.4–0.9 mm;
   - purge gap fully open 0.10–0.25 mm radial;
   - ring element inner diameter 2.0–2.6 mm, wall 0.15–0.30 mm, free length 2.5–4.0 mm;
   - convolution amplitude 0.08–0.20 mm.
7. **N7 = N6 + the prototype values and process:**
   - crack pressure 1.0 bar; threshold 3.5 bar; normal stroke 0.6 mm; over-travel 0.5 mm; purge gap 0.15 mm;
   - ring inner diameter 2.3 mm, wall 0.20 mm, free length 3.0 mm, convolution amplitude 0.12 mm;
   - NiTi nominally 55.8 wt% Ni, laser-cut from 2.7 mm OD tube, shape-set at 500 °C for 10 minutes, water-quenched and electropolished;
   - ring pressed in with about 0.03 mm interference against an internal shoulder of the core body (20);
   - core body in brass CW614N; valve stem (10) Presta-pattern, 6 mm; lock nut (70) (§3–§5, §7).

This order puts the rungs that keep the inventor's own alternatives in scope ahead of the rungs that exclude them. As a result, each exclusion (Alternative B at N2, Alternative A at N4) happens as late as the disclosure allows.

### Feature Classification

"Provisional" means the disclosure does not say whether the feature is essential. Each provisional entry is tied to an assumption (A) and a Gate 1 question (Q).

| # | Feature | Rung | Classification | Why (support) | Omission risk |
|---|---|---|---|---|---|
| C1 | Poppet (40) opens the main passage by a normal stroke at the crack pressure | N0 | Conventional (necessary context) | This is how any valve core works (§1: the "standard remedy" and "conventional core" context; §3(4); 01 (d) D4) | Technical effect: without it there is no valve |
| C2 | Over-travel: the poppet moves beyond its normal stroke above the over-travel threshold | N0 | Essential | §2 defines the concept by over-travel. The same actuation appears in Alternatives A and B (§6). Bench data: an audible snap on every prototype inflation | Technical effect |
| C3 | Threshold arrangement separating the normal stroke from over-travel (generic) | N0 | Essential, provisional (A3) | §2 ("above a threshold"); §3(5). The disclosure does not say whether a poppet that over-travels on every opening would work (Q3) | Technical effect: unknown, pending Q3 |
| C4 | Purge shoulder (44) on the poppet, bearing on the ring element only during over-travel | N0 | Essential | §2; §3(4). Alternative B keeps it (§6). Its geometry is unstated (01 Q8) | Technical effect |
| C5 | Resiliently deflectable ring element, deflected by the purge shoulder | N0 | Essential (genus provisional, A1) | §2; §3(3). §6 extends the genus to PEEK and to a stainless spring wiper ring. Elastomers are not conceived and are disparaged for the wipe (§2) (Q6) | Technical effect |
| C6 | Purge gap (60), closed at rest and opened by the deflection | N0 | Essential (provisional against the wipe-only reading, A2) | §2; §3(6). Bench data: film found "in the purge-gap region". **Its location and opening mechanism are inconsistent in the disclosure** (01 Q1, Q2) | **Enablement** and technical effect |
| C7 | Air purge: inflation air flows through the purge gap across the surfaces on which sealant accumulates, into the tyre | N0 | Essential, provisional (A2) | §2; the drawings README (FIG-2) via 01 (b)5. Its share of the effect is unevidenced (01 Q24) | Technical effect; **enablement** until the air path is described (Q2) |
| C8 | Recovery of the ring element when the differential collapses, closing the purge gap | N0 | Essential | §2. Bench data: snap on pump-head removal; leak-down ≤ 0.2 bar at cycle 40. Whether the closed gap must be airtight is unstated (Q11) | Technical effect (possible leak-down, or no further cycles) |
| C9 | Snap-back wipe: the recovering ring element moves across the poppet face | N1 | Advantageous, provisional (A2) | §2 (cleaning "twice"). §6: the PEEK wipe is weaker, yet PEEK is still offered for a product line. Bench data: the poppet face was clean at cycle 40 | Technical effect: unknown, pending Q1 |
| C10 | Ring element also forms the seat for the sealing face (42) | N2 | Advantageous | §3(3), §3(4). Alternative B separates sealing from purging, at the cost of one more part and more axial length (§6) | None: Alternative B shows another route |
| C11 | Conical sealing face (42) | N2 | Conventional / exemplary | §3(4). Cone angle unstated (01 Q9) | None |
| C12 | Convoluted wall with one or two shallow convolutions, converting axial load into radial expansion | N3 | Advantageous, provisional (A4) | §3(3) states it as the expansion mechanism. No other geometry is disclosed (01 Q12) | **Enablement**: if it is omitted and no other axial-to-radial geometry is disclosed, the deflection is not enabled (Q4) |
| C13 | Deflection is radially outward | N3 | Advantageous, provisional (A4) | §2 ("flexes radially outward"); §6 (Alternative B "deflected outward") | Enablement is tied to C6 (Q2) |
| C14 | Superelastic alloy ring element | N4 | Advantageous | §2 credits it with the "fast and stiff" recovery that makes the wipe work. §6 shows PEEK is an option with a weaker wipe | Technical effect: the wipe is degraded, not lost (§6) |
| C15 | NiTi, nominally 55.8 wt% Ni | N4 / N7 | Exemplary | §5. No tolerance and no other alloys are stated (01 Q14) | None beyond C14 |
| C16 | Af below 5 °C | N4 | Advantageous; essential **if** a shape-memory alloy is used (A5) | §4 ("superelastic at all riding temperatures"). §9 (item 2) raises the CO₂ cold-shock doubt (Q10) | **Technical effect**: a martensitic ring would not recover, so the purge gap would stay open or the wipe would be lost |
| C17 | Two-rate return spring (50) | N5 | Advantageous, provisional (A3) | §3(5). The disclosure does not say whether it is the only threshold arrangement (01 Q6, Q7) | None if another threshold arrangement is disclosed. Otherwise **enablement** of C3 |
| C18 | Over-travel threshold above the crack pressure and reachable by the inflation device | N0 (relationship) / N6 (values) | Relationship essential; values advantageous | §2 ("which every floor pump reaches"); §4. The basis for "every" is unstated (01 Q5) | **Technical effect**: a threshold that the pump cannot reach gives no purge (Q9) |
| C19 | Pressure ranges: crack pressure 0.8–1.5 bar; over-travel threshold 2.5–5.0 bar | N6 | Advantageous (believed, not evidenced) | §4. Only the prototype values were built (01 (h)) | None (Q13) |
| C20 | Over-travel 0.4–0.9 mm; purge gap 0.10–0.25 mm radial | N6 | Advantageous (believed) | §4. Neither was measured in the test (bench data) | None (Q13) |
| C21 | Ring element dimensions: inner diameter 2.0–2.6 mm, wall 0.15–0.30 mm, free length 2.5–4.0 mm, convolution amplitude 0.08–0.20 mm | N6 | Advantageous (believed); a "thin" wall is part of the concept | §2 ("thin, sinuous wall"); §4 | Enablement: at least one working set of dimensions must be disclosed, and the prototype values provide it |
| C22 | What limits over-travel (stop, coil-bind of the spring, or the ring) | Not placed | Unknown | Not stated (01 Q36) | Enablement is possible if the ring itself is the stop (fatigue) |
| C23 | Ring retained by about 0.03 mm interference against an internal shoulder | N7 | Exemplary, provisional | §7. Other retention methods are unstated (01 Q17). **Interacts with C6** | **Enablement**, through the purge-gap inconsistency (Q2) |
| C24 | Laser cut, shape-set at 500 °C for 10 minutes, water quench | N7 | Exemplary | §7 | Enablement: for a NiTi ring, some shape-setting route must be disclosed, and this one suffices |
| C25 | Electropolished ring surface | N7 | Exemplary (its function is unstated) | §5, §7 | None known (Q15) |
| C26 | Core body (20): threaded to the stem, carries the ring element, guides the poppet; brass CW614N or stainless 303 | N0 (carrier) / N7 (material) | Carrier conventional; material exemplary | §3(2), §5 | None |
| C27 | Poppet material: brass, or an anodised aluminium face | N7 | Exemplary | §5 | None |
| C28 | Spring material | N7 | Exemplary | §5 ("nothing in the concept depends on the spring material") | None |
| C29 | Presta-pattern valve stem (10), 6 mm | N7 | Conventional | §3(1). Whether the core alone is a product is open (01 Q33) | None (Q14) |
| C30 | Lock nut (70) | N7 | Conventional | §3(7) | None |
| C31 | Field of use: a tyre (inner tube or tubeless) holding liquid sealant | Context | Conventional context (A5) | §1. Only inner tubes were tested (§8) | Technical effect: the effect is defined against sealant |
| C32 | Thermal two-way shape-memory purge (Af about 35–40 °C) | Outside N0 | Exemplary, separate candidate concept | §6 (inventor doubtful; no data) | Not applicable (Q12) |

**Features whose omission may undermine enablement or technical effect:**
- **Enablement:**
  - C6/C7: the purge gap and air path are inconsistent (§2 against §3(6) and §7);
  - C12: the convolution is the only disclosed means of axial-to-radial conversion;
  - C17: the two-rate spring is the only disclosed threshold arrangement;
  - C23: the interference fit interacts with the purge-gap mechanism.
- **Technical effect:**
  - C2–C8: the nucleus;
  - C16: Af, where NiTi is used;
  - C18: the threshold must be reachable.

The most urgent Gate 1 items are Q1 and Q2 (01 Q1, Q2 and Q24). Without them the nucleus cannot be stated as enabled, and it cannot be fixed as purge-based, wipe-based or both.

## Rationale

**Why N0 is built from §2 and §6.** The nucleus is the intersection of the §2 concept with the inventor's own considered alternatives in §6, rather than a description of the prototype. §6 is the inventor's own statement that NiTi is not essential (Alternative A) and that sealing and purging can be split between separate parts (Alternative B). Using §6 as the boundary gives the broadest N0 the inventor's conception supports, without adding matter. I did not widen the ring element to elastomers: the inventor disparages rubber for the wipe (§2), and nothing suggests an elastomer ring element was conceived. That is asked as Q6, not included.

**Why the air purge is essential and the wipe advantageous.** The bench test does not separate the two actions. I made the air purge essential (provisionally) and the snap-back wipe advantageous for three reasons:
- §2 builds the concept around the purge gap.
- The film found in the purge-gap region shows that air flows there.
- The inventor accepts a weaker wipe in Alternative A for a product line.

The contrary reading is stated in full next to the ladder so that Gate 1 can reverse it cheaply.

**Rung order.** The ladder order keeps each of the inventor's alternatives in scope for as many rungs as the disclosure allows:
- The wipe (N1) comes before the one-piece seat (N2), because both A and the prototype wipe.
- The seat comes before the convolution (N3), because Alternative B's wiper-ring form is unknown.
- The convolution comes before the alloy (N4), because Alternative A shares the convolution.
- The two-rate spring comes late (N5), because §3(5) presents it as the means, not as the concept.

**Missing input.** Prompt 02 (commercial value map) was not available, so the rung order is not weighted by commercial value. Claims Architect should reconcile the two once 02 exists.

**Thermal variant.** This is kept off the ladder because it removes over-travel, which is the one feature common to everything else.

## Assumptions

A1. The ring element genus covers the NiTi seat ring (30), a PEEK ring of the same form (§6 Alternative A) and a stainless spring wiper ring (§6 Alternative B). This rests on §6 describing them as considered alternatives. The inventor has not confirmed they fall within the invention (01 Q20). **Blocking** for P3 and P5 until Q5.

A2. The air purge (C6, C7) is treated as essential and the snap-back wipe (C9) as advantageous. This rests on §2 (the purge gap as the core of the concept), §6 (a weaker wipe accepted in Alternative A) and the bench data (film in the purge-gap region). The test does not separate the two actions. **Blocking** for P3 and P5 until Q1.

A3. Some threshold arrangement distinguishing the normal stroke from over-travel is treated as essential, and the two-rate return spring as one species of it. This rests on §2 ("above a threshold") and §3(5). **Blocking** for P5 until Q3.

A4. The convoluted wall and radially outward deflection are treated as advantageous rather than essential. This rests on §3(3) presenting the convolution as the means of radial expansion, and on §6 Alternative B's wiper ring being "deflected outward" with no stated form. Not blocking for P3; **blocking** for P5 until Q4.

A5. Two contextual assumptions:
- Af below 5 °C is classified as essential only for a shape-memory-alloy ring element. This rests on §4 and §9 (item 2).
- Sealant use is treated as the field of use rather than as a structural feature of the combination (§1).

Not blocking.

A6. 01's assumptions A3–A5 carry forward unchanged: the pressure differential is pump side minus tube side; "upper" is the pump side; the poppet opens towards the tube. **Blocking** for P4, as in 01.

A7. Prompt 02 was not available, so the ladder is ordered by fallback logic and not by commercial value. Not blocking.

## Open Questions

Q1. Is the air purge alone, the snap-back wipe alone, or both needed to keep the valve sealing and opening over many sealant-loaded cycles (01 Q24)? The answer decides whether the nucleus is N0, the wipe-based reading or N1. Blocks P3, P5.

Q2. Where is the purge gap (60), how does it open when the ring is interference-fitted and flexes outward, and what is the full air path from the pump side into the tyre (01 Q1, Q2)? The nucleus is not enabled without this. Blocks P3, P4, P5.

Q3. Must the over-travel threshold be distinct from the crack pressure? Would a poppet that deflects the ring element on every opening still work? Is the two-rate spring the only threshold arrangement conceived (01 Q6)? Blocks P3, P5.

Q4. Is the convoluted wall essential, or has the inventor conceived any other geometry that turns axial load from the purge shoulder into radial deflection (01 Q12)? Blocks P3, P5.

Q5. Does the inventor regard the PEEK ring (Alternative A) and the brass seat with a stainless wiper ring (Alternative B) as within the invention, so that the ring element need not be NiTi or a one-piece seat (01 Q20)? Blocks P3, P5.

Q6. Has the inventor conceived any other resilient material for the ring element, such as other polymers, spring metals or elastomers? §2 contrasts rubber unfavourably for the wipe only. Blocks P3.

Q7. In Alternative B, does the wiper ring wipe the poppet face on recovery, and if so which surface does it wipe (01 Q10)? Blocks P3, P4.

Q8. Must the purge shoulder (44) be a separate surface below the sealing face (42), or could another part of the poppet bear on the ring element during over-travel? Blocks P3, P5.

Q9. Which inflation devices must reach the over-travel threshold (floor pump, hand pump, CO₂ inflator, compressor), and what upper limit on the threshold follows (01 Q4, Q5)? Blocks P3, P5.

Q10. Is Af below 5 °C a requirement for the effect, and is there a lower bound or a margin needed for CO₂ inflation (01 Q13, Q28)? Blocks P3, P4.

Q11. At rest, must the closed purge gap be airtight? That is, is recovery essential to sealing, or only to cleaning (01 Q31)? Blocks P4, P5.

Q12. Should the thermal two-way variant be kept as a separate candidate concept or dropped (01 Q21)? Blocks P3, P5.

Q13. What is the basis for each §4 range beyond the prototype value (01 Q15)? Blocks P3, P4, P5.

Q14. Is the core without the valve stem (10) a product in its own right, and are other valve types conceived (01 Q26, Q33)? The answer decides whether the stem belongs in the nucleus context. Blocks P3, P5.

Q15. Does the electropolished surface do anything functionally, for example for the wipe, for sealant release or for fatigue life (01 Q32)? Blocks P4.

```json
{
  "prompt": "03",
  "status": "complete",
  "assumptions": [
    {"id": "A1", "text": "Ring element genus covers the NiTi seat ring (30), a PEEK ring (§6 Alt A) and a stainless spring wiper ring (§6 Alt B); inventor has not confirmed these are within the invention.", "blocking": true},
    {"id": "A2", "text": "Air purge (purge gap) treated as essential and snap-back wipe as advantageous, on §2, §6 and bench-data film location; the test does not separate them.", "blocking": true},
    {"id": "A3", "text": "A threshold arrangement distinguishing normal stroke from over-travel is essential; the two-rate return spring is one species (§2, §3(5)).", "blocking": true},
    {"id": "A4", "text": "Convoluted wall and radially outward deflection classified advantageous, not essential (§3(3), §6 Alt B).", "blocking": true},
    {"id": "A5", "text": "Af below 5 °C essential only for a shape-memory-alloy ring element; sealant use treated as field of use, not a structural feature.", "blocking": false},
    {"id": "A6", "text": "01 assumptions A3–A5 (pressure differential, orientation, opening direction) carried forward.", "blocking": true},
    {"id": "A7", "text": "Prompt 02 unavailable; ladder ordered by fallback logic, not commercial weight.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "Is the air purge alone, the snap-back wipe alone, or both needed for the effect (01 Q24)? Decides whether nucleus is N0, the wipe-based reading or N1.", "blocks": ["P3", "P5"]},
    {"id": "Q2", "text": "Purge gap location, opening mechanism with interference fit and outward flex, and full air path (01 Q1, Q2); nucleus not enabled without it.", "blocks": ["P3", "P4", "P5"]},
    {"id": "Q3", "text": "Must the over-travel threshold be distinct from crack pressure; would purge on every opening work; any threshold arrangement other than the two-rate spring (01 Q6)?", "blocks": ["P3", "P5"]},
    {"id": "Q4", "text": "Is the convoluted wall essential; any other axial-to-radial geometry conceived (01 Q12)?", "blocks": ["P3", "P5"]},
    {"id": "Q5", "text": "Are Alternatives A (PEEK) and B (brass seat plus stainless wiper ring) within the invention (01 Q20)?", "blocks": ["P3", "P5"]},
    {"id": "Q6", "text": "Other resilient ring-element materials conceived (polymers, spring metals, elastomers)?", "blocks": ["P3"]},
    {"id": "Q7", "text": "In Alternative B, does the wiper ring wipe the poppet face on recovery, and which surface (01 Q10)?", "blocks": ["P3", "P4"]},
    {"id": "Q8", "text": "Must the purge shoulder be distinct from and below the sealing face, or could another poppet part deflect the ring element?", "blocks": ["P3", "P5"]},
    {"id": "Q9", "text": "Which inflation devices must reach the over-travel threshold, and the resulting upper limit (01 Q4, Q5)?", "blocks": ["P3", "P5"]},
    {"id": "Q10", "text": "Is Af below 5 °C required for the effect; lower bound; margin for CO2 inflation (01 Q13, Q28)?", "blocks": ["P3", "P4"]},
    {"id": "Q11", "text": "Must the closed purge gap be airtight at rest (01 Q31)?", "blocks": ["P4", "P5"]},
    {"id": "Q12", "text": "Keep the thermal two-way variant as a separate candidate concept or drop it (01 Q21)?", "blocks": ["P3", "P5"]},
    {"id": "Q13", "text": "Basis for each §4 believed range (01 Q15).", "blocks": ["P3", "P4", "P5"]},
    {"id": "Q14", "text": "Is the core without the valve stem a product; other valve types conceived (01 Q26, Q33)?", "blocks": ["P3", "P5"]},
    {"id": "Q15", "text": "Functional role of the electropolished surface (01 Q32)?", "blocks": ["P4"]}
  ],
  "new_terms": [
    {"term": "ring element", "maps_to": "seat ring (30)", "reason": "Genus covering the NiTi seat ring and the inventor's §6 alternatives (PEEK ring, stainless spring wiper ring), so the nucleus is not limited to a one-piece NiTi seat."},
    {"term": "wiper ring", "maps_to": "ring element", "reason": "Inventor's own term for the §6 Alternative B species of the ring element."},
    {"term": "threshold arrangement", "maps_to": "return spring (50)", "reason": "Genus for whatever sets the over-travel threshold; the two-rate return spring is the only disclosed species."},
    {"term": "main passage", "maps_to": null, "reason": "Normal inflation air path past the sealing face, named as in the drawings README (FIG-2) via 01 (b)5; needed to distinguish it from the purge gap."},
    {"term": "superelastic alloy", "maps_to": null, "reason": "Material genus of which the prototype NiTi is the species (§2, §5); used for rung N4."}
  ],
  "support_refs": [
    {"item": "N0 over-travel beyond normal stroke above a threshold", "support": "intake/disclosure.md §2, §3(5), §4; bench data (audible snap)"},
    {"item": "N0 purge shoulder bears on ring element only in over-travel", "support": "intake/disclosure.md §2, §3(4); §6 Alternative B"},
    {"item": "N0 purge gap and air purge", "support": "intake/disclosure.md §2, §3(6); bench data (film in purge-gap region); 01 (b)5 (drawings README FIG-2); inconsistency per 01 (m)"},
    {"item": "N0 recovery closes purge gap", "support": "intake/disclosure.md §2; bench data (leak-down ≤ 0.2 bar at cycle 40)"},
    {"item": "Ring element genus (NiTi, PEEK, stainless wiper ring)", "support": "intake/disclosure.md §3(3), §5, §6"},
    {"item": "N1 snap-back wipe", "support": "intake/disclosure.md §2, §6 (weaker for PEEK); bench data (poppet face clean at cycle 40)"},
    {"item": "N2 ring element forms the seat", "support": "intake/disclosure.md §3(3), §3(4); §6 Alternative B trade-off"},
    {"item": "N3 convoluted wall", "support": "intake/disclosure.md §3(3); §6 Alternative A 'same convoluted wall'"},
    {"item": "N4 superelastic NiTi, Af below 5 °C", "support": "intake/disclosure.md §2, §4, §5; §9 item 2"},
    {"item": "N5 two-rate return spring", "support": "intake/disclosure.md §3(5)"},
    {"item": "N6 believed ranges", "support": "intake/disclosure.md §4; 01 (h)"},
    {"item": "N7 prototype values and process", "support": "intake/disclosure.md §3–§5, §7; 01 (h), (j)"},
    {"item": "Thermal variant outside nucleus", "support": "intake/disclosure.md §6"}
  ],
  "disclosure_requests": [
    {"limitation": "N0 purge gap and air purge (C6, C7)", "needed_disclosure": "Consistent written description of the surfaces bounding the purge gap, how deflection of the ring element opens it given the interference fit, and the full air path into the tyre."},
    {"limitation": "Threshold arrangement (C3, C17)", "needed_disclosure": "Whether means other than a two-rate return spring set the over-travel threshold, and spring stage forces/engagement stroke."},
    {"limitation": "Axial-to-radial conversion (C12)", "needed_disclosure": "Whether ring-element geometries other than the convoluted wall are conceived, and the form of the Alternative B wiper ring."},
    {"limitation": "Relative contribution of air purge and snap-back wipe (C7, C9)", "needed_disclosure": "Any test or inventor explanation separating the two cleaning actions."}
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

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/CONFIRMED.md`

```markdown
# Confirmed embodiments

Confirmed at Gate 2 by **Orchestrator (auto-unattended)**, 2026-09-30 10:18 UTC. Only what is below goes into the specification. Candidate status is lifted by this gate and by nothing else.


---

## From `11.md`

### Design-Around Risk Register

**Status: candidate.** Nothing below is specification content until the human confirms it at Gate 2. None of the alternatives has been built or tested; the only built embodiment is the prototype of §3–§8. This register was prepared by AI as a drafting and analysis aid. It is not legal advice, and qualified patent counsel signs off before anything is filed.

**Sources and references.** The proposed claim limitations are the nucleus N0(a)–(e), the ladder rungs N1–N7 and the feature codes C1–C32 of `03`, together with the claim-type ranks of `02`. `09` and `10` do not exist yet, so no "possible claim language" column was available (A1). `intake/disclosure.md` is cited as §1–§9. The "Support" column reads either **Dossier** (the alternative is disclosed in some form, with the passage cited) or **Needs inventor confirmation**, with the open question below that Gate 2 must answer. Three rows are marked **Cannot be closed without new matter**: they become inventor questions, not embodiments. Rows are ranked by risk, highest first. Risk combines three things: technical plausibility, commercial attractiveness, and whether the route escapes the nucleus N0 or only a ladder rung.

| ID | Design-around (what the competitor builds) | Limitation avoided | Technical plausibility | Commercial attractiveness | Broader genus or alternative embodiment the specification could describe | Support | Status |
|---|---|---|---|---|---|---|---|
| DA-1 | **Purge on every opening.** A single-rate return spring is used, and the poppet's deflecting surface reaches the seat ring at or just after the crack pressure. The purge gap then opens on every opening and there is no separate over-travel threshold. | N0(b): the threshold-setting arrangement, and over-travel beyond the normal stroke (C2, C3). N0(c): "only during over-travel" (C4). | **Medium.** Mechanically simpler. Unknown whether leak-down and seat-ring fatigue hold if the ring deflects on every opening, possibly on every piston cycle of a floor pump (01 Q4, Q27). | **High.** Removes the second spring stage and the threshold tuning. | Describe an over-travel threshold that may equal or barely exceed the crack pressure, including an embodiment with a negligible normal stroke in which the purge state is reached on every opening. Define the purge state by deflection of the deflectable ring element, not by a second threshold. | Needs inventor confirmation (Q1; 03 Q3) | candidate |
| DA-2 | **Deflection in another direction.** The deflectable ring element is deflected radially inward, tilted, or lifted axially off the internal shoulder. The purge gap then forms at its inner surface, at an end face or against the poppet, not between its outer surface and the core body bore. | N0(d): the purge gap as locked (an annular radial clearance between the seat ring outer surface and the core body bore, §3(6)). C13: radially outward radial deflection. | **High.** Each is an ordinary elastic deformation of a thin-walled ring. The base embodiment's own direction is unresolved (01 Q1, Q2), so a competitor can pick whichever reading the claims leave out. | **High.** No cost penalty. A competitor can copy the prototype and argue that the gap is elsewhere. | Define the purge gap by function: any clearance bounded partly by the deflectable ring element, closed in the closed state and opened by the deflection. Describe outward, inward, axial and tilting deflection, with the gap at the outer surface, the inner surface or an end face. | Needs inventor confirmation (Q2; 01 Q1, Q2). The base embodiment must be resolved first. | candidate |
| DA-3 | **Slotted or segmented purge opening.** The seat ring wall carries laser-cut slits or apertures that are closed at rest and open when the purge shoulder strains the wall. Alternatively, the ring is split into fingers whose gaps open. Air flows through the wall, not around it. | N0(d): the "annular" purge gap. The implied continuity of the seat ring (C5, C6). | **High.** The prototype is already laser-cut (§7), and strain-opened slits in a thin wall are an ordinary structure. Whether closed slits seal at rest needs inventor comment (01 Q31). | **High.** Same tooling. The ring can be press-fitted with no clearance at its outer surface. | Describe a purge opening genus: an annular gap, one or more slits or apertures in the wall, or gaps between the fingers of a segmented ring element. Describe the deflectable ring element as continuous, split or segmented. | Needs inventor confirmation (Q3) | candidate |
| DA-4 | **No distinct purge shoulder.** One conical sealing face seals on the sealing edge at rest and, pushed further in over-travel, forces the sealing edge to deflect radially. Alternatively, a taper on the poppet stem entering the seat ring does the deflecting. | N0(c): the purge shoulder as a surface separate from the sealing face and on its chamber side (C4; the locked species of purge shoulder). | **Medium–high.** Depends on the poppet's direction of travel (01 Q3), but either a sealing face or a taper on the poppet stem can put a radial load on a thin ring. | **High.** One fewer turned feature and a simpler poppet. | Define the purge shoulder by function: the formation of the poppet that contacts the deflectable ring element during over-travel. State that it may be the sealing face, a continuation of it, a taper on the poppet stem, or a separate formation. | Needs inventor confirmation (Q4; 03 Q8) | candidate |
| DA-5 | **Integral lip.** The core body is injection-moulded polymer, or a spring-metal pressing, with an integral thin annular lip. The lip seals against the sealing face and is deflected during over-travel. There is no separate seat ring and no interference fit. | The seat ring as a separate part carried by the core body (C5, C26). N7: interference fit (C23). | **Medium–high.** Moulded lips are a known polymer feature. Recovery and the snap-back wipe would probably be weaker, as §6 says of PEEK. A brass lip is unlikely to recover. | **High.** Removes the NiTi part, laser cutting, shape-setting and press-fitting: a volume cost-down. | Describe the deflectable ring element as either separate from the core body or integral with it (moulded, machined or pressed). Describe a polymer core body as well as a metal one. | Needs inventor confirmation (Q5). PEEK as a ring material: Dossier §6. | candidate |
| DA-6 | **Different valve format.** The mechanism is built directly into the valve stem of an integrated tubeless inflation valve with no removable valve core. Alternatively, it is built into a Schrader-pattern or Dunlop-pattern valve core. | The valve core as a core body threaded into the stem bore (C26). Any Presta-pattern limitation (C29). | **High.** The mechanism does not depend on the thread or on the Presta pattern. | **High.** Reaches OEM tubeless valves (02 rank 3) and Schrader-pattern markets. | Describe the mechanism in any inflation valve, with its parts carried either by a removable core body or directly by the valve stem. Name the other valve standards as candidates and keep Presta-pattern as the worked example. | Needs inventor confirmation (Q6; 01 Q26, Q33; 03 Q14) | candidate |
| DA-7 | **Over-travel uncovers a port.** In over-travel the poppet uncovers a purge port in the core body bore (spool-type porting) that directs air across the sealing edge into the inflatable chamber. Nothing deflects and nothing recovers. | N0(c)–(e): the deflectable ring element, its deflection and its shape recovery (C5, C6, C8). | **Medium.** Porting by poppet travel is ordinary. Unevidenced whether directed air alone removes cured sealant film (01 Q24). | **High.** No special alloy and no ring. | Only a genus such as "a purge flow path opened by over-travel, whether by deflecting an element or by uncovering a port" would close this route. Nothing in the dossier suggests the inventor conceived porting. | **Cannot be closed without new matter** unless the inventor confirms conception (Q7) | candidate |
| DA-8 | **Kinematic inversion.** The deflectable ring element is a thin skirt carried by the poppet. In over-travel a fixed formation in the core body deflects it, and on recovery it wipes the core body bore. | N0(c): a purge shoulder on the poppet bearing on a ring element carried by the core body (C4, C5). | **Medium.** Mechanically symmetric, but the wipe then acts on the core body bore rather than the sealing face (01 Q10). | **Medium.** A moving ring adds mass and fatigue risk. | Describe the deflecting formation and the deflectable ring element as each carried by either the poppet or the core body, with the counterpart on the other. | Needs inventor confirmation (Q8) | candidate |
| DA-9 | **Mechanical over-travel.** An adaptor or actuator on the inflation device pushes the poppet into over-travel whatever the pressure differential, or the user pushes it by hand. The valve has only a single-rate return spring. | N0(b): over-travel caused by the pressure differential exceeding the over-travel threshold (C2, C18). | **High** mechanically. It depends on an adaptor or a user step. | **Medium.** An adaptor can be bundled with the valve. The adaptor maker, not the valve vendor, may then be the only party practising the full combination. | Describe over-travel produced by the pressure differential, by a poppet-depressing actuator on the inflation device or an adaptor, or by pressing the poppet by hand. | Needs inventor confirmation (Q9) | candidate |
| DA-10 | **Wipe only.** The deflectable ring element is sealed at its periphery, so no air flows through the purge gap. Over-travel and shape recovery produce only the snap-back wipe. | N0(d): the air purge (C6, C7). | **Medium.** Depends on whether the snap-back wipe alone keeps the valve sealing and opening. The bench test does not separate the two cleaning actions (01 Q24; 03 Q1). | **Medium.** Same parts, and it avoids a limitation requiring the air purge. | Describe the cleaning action as the air purge, the snap-back wipe, or both. Include a wipe-only embodiment and describe the snap-back wipe independently of any flow. | Needs inventor confirmation (Q10; 03 Q1, A2) | candidate |
| DA-11 | **Other threshold-setting arrangement.** Examples: two compression springs (a second one engaged at the end of the normal stroke); a magnetic or ball detent; an elastomer stop; or a single-rate return spring with the seat ring's own stiffness supplying the step. | N5: the two-stage return spring, i.e. the first spring stage plus the second spring stage (C17). | **High.** All are conventional ways to get a stepped force–stroke characteristic. | **Medium.** Escapes only N5, but a competitor tuning its own threshold will choose one of these. | Describe a threshold-setting arrangement genus with these species. State that the return spring and the deflectable ring element may each contribute. Keep the two-stage return spring as the example. | Needs inventor confirmation (Q11; 01 Q6, Q7) | candidate |
| DA-12 | **Straight-walled seat ring.** A tapered interface (a tapered purge shoulder, a chamfered sealing edge, or a conical inner surface of the seat ring) converts axial load into radial deflection without a convoluted wall. | N3: the convoluted wall (C12). | **Medium.** Works geometrically. Recoverable strain limits the purge gap opening, and the convolution may be there to keep strain low (01 Q12). | **Medium–high.** A simpler ring with no wave fixture. | Describe an axial-to-radial conversion geometry genus: a convoluted wall, a tapered or chamfered interface on either part, or a slotted wall. Keep the convoluted wall as the preferred species. | Needs inventor confirmation (Q12; 03 Q4) | candidate |
| DA-13 | **Polymer ring element:** PEEK as in §6, or another engineering polymer, moulded rather than cut. | N4: superelastic alloy (C14, C15) and the austenite finish temperature (C16). | **High.** The inventor proposes PEEK for a lower-cost line, accepting a weaker snap-back wipe (§6). | **High.** A budget line (02 rank 5). | Describe the deflectable ring element in polymer, with PEEK as the disclosed species. Add other polymers and moulding only if the inventor conceived them. | PEEK: Dossier §6. Other polymers and moulding: needs inventor confirmation (Q13; 03 Q6) | candidate |
| DA-14 | **Other resilient metal.** A spring metal that is not superelastic (stainless spring steel, beryllium copper), or another superelastic alloy (ternary NiTi, copper-based). | N4: superelastic alloy; nickel content (C15). | **Medium.** Conventional spring metals recover far less strain than superelastic alloys, so the wall geometry or the purge gap opening would change. §6 Alternative B already uses a stainless spring wiper ring. | **Medium.** Cheaper stock and no NiTi supply chain. | Describe the deflectable ring element in a resilient metal, superelastic or not, with NiTi as the preferred species. Stainless steel for the wiper ring is already disclosed. | Stainless wiper ring: Dossier §6. Other metals and alloys: needs inventor confirmation (Q14; 01 Q14) | candidate |
| DA-15 | **Elastomeric ring element**, for example a high-hardness thermoplastic elastomer. | N4, and any wording that defines the ring element by fast, stiff shape recovery (C9, C14). | **Low–medium.** The inventor states that latex would embed itself in rubber (§2). | **High.** The cheapest material. | An elastomer embodiment cannot be added unless the inventor conceived it. The specification can still avoid turning §2 into a disclaimer: present superelastic shape recovery as preferred, not as the definition of the deflectable ring element. | Drafting point: reading of §2. Elastomer embodiment: needs inventor confirmation (Q15; 03 Q6) | candidate |
| DA-16 | **Values outside the believed ranges.** For example: over-travel threshold below 2.5 bar or above 5.0 bar; seat ring wall thickness outside 0.15–0.30 mm; over-travel distance outside 0.4–0.9 mm. | N6: the ranges (C19–C21). | **High.** Nothing in the mechanism fixes these endpoints, and the inventor says they are believed, not evidenced (§4). | **Medium.** Tuning only. | Lead with the relationships that make the mechanism work: the over-travel threshold is above the crack pressure and within what the inflation device reaches, and the purge gap is closed at rest. Give the ranges as a ladder (Prompt 13), with no new endpoints without data. | Needs inventor confirmation (Q16; 01 Q15) | candidate |
| DA-17 | **Split sealing and purge** (§6 Alternative B). A fixed seat seals, and a separate wiper ring is deflected by the purge shoulder. | N2: the seat ring also forms the seat (C10). | **Medium–high.** The inventor proposes it, at the cost of one more part and more axial length (§6). | **Medium.** "Possibly easier to make" (§6). | Describe Alternative B as a species of the deflectable ring element used with a fixed seat. Include the wiper ring's form, thickness and retention, and whether it wipes the sealing face. | Existence: Dossier §6. Details: needs inventor confirmation (Q17; 01 Q20; 03 Q7) | candidate |
| DA-18 | **More or different convolutions.** Three or more convolutions, or another profile (circumferential rather than axial wave, helical, saw-tooth). | N3: "one or two" convolutions (C12). | **High.** An obvious variation once the convolution is known. | **Low–medium.** | Describe the convoluted wall as having at least one convolution of any profile, with one and two as the disclosed species. | Needs inventor confirmation (Q18; 01 Q11) | candidate |
| DA-19 | **Component or kit sale.** The seat ring, or the seat ring with the poppet and return spring, sold as a kit to fit into a core body the customer supplies. | Any claim that requires the assembled valve core including the core body (02 rank 1). | **Low–medium.** Conventional core bodies are not designed to be taken apart. | **Low–medium.** | Describe the seat ring and the poppet as separately supplied components, and describe the kit. Component claims are for Claims Architect (02 rank 2). | Needs inventor confirmation (Q19; 02 Q1; 01 Q33) | candidate |
| DA-20 | **Purge on deflation.** The user presses the poppet into over-travel while deflating, so chamber air leaves through the purge gap. Inflation uses the normal stroke only. | N0(d): inflation gas flowing through the purge gap into the inflatable chamber during an inflation event. | **Medium.** Over-travel by hand is plausible, but the outward flow carries liquid sealant towards the user. | **Low.** | Describe the purge state reached during deflation, with flow through the purge gap in either direction. | Needs inventor confirmation (Q20; 01 Q23) | candidate |
| DA-21 | **Different ring manufacture.** Pressing from strip and rolling; photo-chemical etching; drawing tube stock with a formed wave; machining from bar; or moulding (polymer). | The manufacturing method (02 rank 4): laser cutting, shape-setting in a fixture, water quench, electropolishing (C24, C25). | **High.** | **Medium.** These are volume routes. | Describe the alternative forming routes and process windows as candidates, keeping the §7 route as the example. | Needs inventor confirmation (Q21; 01 Q32) | candidate |
| DA-22 | **Other retention.** Adhesive, crimping, staking, laser welding, over-moulding, or clamping between two core body parts, with no interference fit. | N7: interference fit against the internal shoulder (C23). | **High.** | **Low.** | Describe a retention genus with the interference fit as the example. | Needs inventor confirmation (Q22; 01 Q17). Resolve the interaction with the purge gap (01 Q2) first. | candidate |
| DA-23 | **Rigid wiping edge.** A fixed edge in the core body over which the poppet slides during over-travel, shearing sealant film off the poppet. Nothing deflects. | N0(c)–(e): the deflectable ring element and its shape recovery (C5, C8). N1: the snap-back wipe (C9). | **Medium.** Sliding wipers are known, but cured sealant film may jam a rigid close fit. | **Medium.** | Cannot be closed from the dossier: the inventor's concept is the recovery of a deflected element. | **Cannot be closed without new matter** unless the inventor confirms conception (Q23) | candidate |
| DA-24 | **Ring deflected by pressure, without contact.** A thin polymer ring element is deflected by the pressure differential alone, opening the purge gap; the poppet never touches it. | N0(c): contact by the purge shoulder (C4). Over-travel (C2). | **Low for metal.** At the disclosed pressures the hoop load on a 0.20 mm NiTi wall gives negligible deflection. **Medium for a thin polymer ring.** | **Low–medium.** | Only a genus such as "deflected by the purge shoulder or by the pressure differential" would close this route, and it is not in the dossier. | **Cannot be closed without new matter** unless the inventor confirms conception (Q24) | candidate |
| DA-25 | **Thermally actuated purge** (§6). A two-way shape-memory ring element opens the purge gap when warmed; there is no over-travel. | N0(b)–(c): over-travel and the purge shoulder. | **Low.** The inventor doubts it and there is no data (§6). | **Low.** | Describe the thermally actuated purge as a separate candidate concept, and only if the inventor keeps it. | Concept only, no data: Dossier §6. Keep or drop: needs inventor confirmation (Q25; 01 Q21) | candidate |

**Findings for Claims Architect and Specification Drafter** (candidate; for Gate 2):

1. **DA-1 is the cheapest escape from N0.** If the inventor confirms that purging on every opening works (Q1), then the threshold-setting arrangement (C3) is not essential and should not appear in the broadest claim.
2. **The purge gap needs a functional definition (DA-2, DA-3).** The locked species, "annular radial clearance between the seat ring outer surface and the core body bore", can be avoided without cost. This holds even before 01 Q1/Q2 are answered, and those answers are needed before any of this can be enabled.
3. **Three more features should be described by function or as a genus:**
   - the purge shoulder (DA-4);
   - the deflectable ring element, as separate from or integral with the core body (DA-5);
   - the mechanism, as usable in any inflation valve (DA-6).
4. **Four ladder features are already shown to be non-essential by the inventor's own §6 alternatives or by ordinary engineering:**
   - the convoluted wall (DA-12, DA-18);
   - the superelastic alloy (DA-13, DA-14);
   - the one-piece seat (DA-17);
   - the two-stage return spring (DA-11).
5. **DA-7, DA-23 and DA-24 cannot be closed without matter the inventor has not conceived.** They are recorded as inventor questions only.
6. **Detectability.**
   - A teardown and section of a competitor's valve core shows the routes in DA-2 to DA-6 and DA-11 to DA-18.
   - DA-1, DA-9 and DA-10 turn on behaviour (when deflection occurs, and whether air flows through the purge gap), which needs a bench test on the product.


---

## From `12.md`

### Equivalent Architecture Library

**Status: candidate.** Every entry below is a candidate for Human Gate 2. Entries marked *disclosed* restate what the inventor's disclosure already contains. Every other entry comes from engineering analysis. None of them has been built or tested, and none of them may enter the Description until the inventor confirms at Gate 2 that it is technically real and within their conception. This library is a drafting and analysis aid prepared by AI. It is not legal advice, and qualified patent counsel signs off before anything is filed.

**Sources.** §1–§9 refer to `intake/disclosure.md`, read through `01`. `01 (x)` is the structured disclosure, `03 Cn` the feature classification, `02 rank n` the commercial value map, and LOCKED is `terminology/LOCKED.md`.

**Inputs not available.** `11`, `09`, `10` and `intake/answers.md` did not exist when this was written. That has three consequences:
- **No design-around cross-references.** Instead, each entry's "Changes" line names the escape route it would cover, so it can be re-mapped to `11` ids at Gate 2.
- **No weighting against the prior art.**
- **Every open question in `01` and `03` is treated as unanswered.** This matters most for the location of the purge gap (01 Q1, Q2).

**Coverage.** The library covers every feature that `03` classifies as essential or advantageous: C2, C3, C4, C5, C6, C7, C8, C9, C10, C12, C13, C14, C16, C17, and the C18 relationship. It also covers four features classified conventional or exemplary, because each is a likely design-around route: the ring retention (C23), the seat ring manufacture (C24, C25), the sealing face (C11) and the valve core type (C29). The ranges (C19–C21) are left to Prompt 13 and are not laddered here.

| Section | Locked term | 03 feature |
|---|---|---|
| 1 | over-travel | C2, C18 |
| 2 | second spring stage (threshold-setting arrangement) | C3, C17 |
| 3 | purge shoulder | C4 |
| 4 | deflectable ring element | C5, C10 |
| 5 | convoluted wall | C12 |
| 6 | radial deflection | C13 |
| 7 | purge gap | C6 |
| 8 | purge flow path | C7 |
| 9 | shape recovery | C8 |
| 10 | snap-back wipe | C9 |
| 11 | sealing face | C10, C11 |
| 12 | superelastic alloy | C14, C15 |
| 13 | austenite finish temperature | C16 |
| 14 | interference fit | C23, C26 |
| 15 | shape-setting (seat ring manufacture) | C24, C25 |
| 16 | valve core | C29 |

**How to read an entry.** Each entry gives:
- **Structure:** the concrete structure or mechanism.
- **Same purpose:** how it achieves the same technical purpose.
- **Changes:** what changes (interfaces, ordering, materials), and the escape route the entry would cover.
- **Genus:** the term that would cover both the disclosed form and the alternative.
- **Credibility:** an engineering judgement, not test data.

"Basis" reads either *disclosed (§n)* or *not conceived in the dossier — inventor to confirm (Qn)*.

#### 1. over-travel

1. **E1.1 Axial over-travel of the poppet against the second spring stage.** *Disclosed (§2, §3(5)).* Status: candidate (baseline).
2. **E1.2 Separate purge actuator.** *Not conceived — Q9.* Status: candidate.
   - Structure: an annular piston or flexible diaphragm is housed in the core body, with its supply side open to supply-side pressure and its own compression spring as bias. It advances only when the pressure differential exceeds the over-travel threshold, and it carries the deflecting formation onto the seat ring. The poppet performs only its normal stroke.
   - Same purpose: the seat ring is deflected, and the purge gap opened, only above the over-travel threshold, while inflation gas is flowing.
   - Changes: purge actuation is decoupled from the poppet, and the poppet needs no purge shoulder. It adds a part and a sliding seal exposed to liquid sealant. Covers the route "the part that deflects the ring is not the poppet".
   - Genus: a member moved, above the over-travel threshold, beyond the position it occupies in the normal-open state, so as to deflect the deflectable ring element.
   - Credibility: mechanically sound. Space is tight in a 6 mm Presta-pattern valve stem, where the annulus around a seat ring of 2.3 mm inner diameter leaves little piston area. It is more plausible in larger-bore valve cores (see E16.2).
3. **E1.3 Two-part poppet with a purge sleeve.** *Not conceived — Q4.* Status: candidate.
   - Structure: the sealing face is on the poppet. The purge shoulder is on a sleeve that slides on the poppet stem. The sleeve travels with the poppet during the normal stroke and is pushed onto the seat ring only in over-travel.
   - Same purpose: as E1.1.
   - Changes: the poppet is split into two parts. Covers the route "the purge shoulder is not part of the poppet".
   - Genus: a deflecting formation that moves with the poppet.
   - Credibility: credible. The sleeve clearance on the poppet stem is a new place for sealant film to form.
4. **E1.4 Over-travel produced mechanically by the inflation device.** *Not conceived — Q9.* Status: candidate.
   - Structure: a fixed depressor in the inflation-device head drives the poppet into over-travel on coupling, whatever the pressure differential.
   - Same purpose: the seat ring deflects and the purge gap opens while inflation gas flows, so the air purge runs.
   - Changes: the threshold is set by the geometry of the head, not by a pressure differential, and the purge lasts for the whole coupling. The valve core could omit the second spring stage altogether. Covers the route "a head plus a core with no pressure threshold".
   - Genus: over-travel produced by the pressure differential or by mechanical actuation.
   - Credibility: credible. Depressor heads exist for Schrader-pattern valves; for Presta-pattern valves this needs a matching head.
5. **E1.5 User-actuated over-travel.** *Not conceived — Q9.* Status: candidate.
   - Structure: with the lock nut released, the user presses the poppet beyond its normal stroke with the chamber pressurised.
   - Same purpose: the seat ring deflects and the purge gap opens.
   - Changes: the purge flow runs from the chamber side to the supply side, carrying sealant film out of the valve rather than into the inflatable chamber. It needs user action. Covers the route "the purge is a user operation, not part of inflation".
   - Genus: over-travel produced by the pressure differential or by mechanical actuation.
   - Credibility: physically credible. It conflicts with the §2 statement of effect ("no tool and no rider action"), so it may lie outside the conception. The inventor must decide.

#### 2. second spring stage (threshold-setting arrangement)

1. **E2.1 Two-rate compression spring.** *Disclosed (§3(5)); construction unknown (01 Q6).* Status: candidate.
   - Structure: one candidate construction is a variable-pitch compression spring whose close-pitched section becomes solid at the end of the normal stroke, leaving fewer active turns and a higher rate.
   - Genus: threshold-setting arrangement.
   - Credibility: standard spring practice. That this is the prototype's construction is **not** asserted.
2. **E2.2 Auxiliary compression spring with lost motion.** *Not conceived — Q2.* Status: candidate.
   - Structure: the return spring acts alone over the normal stroke as the first spring stage. A second compression spring is engaged only when a lost-motion clearance closes at the end of the normal stroke, and then acts in parallel.
   - Same purpose: the force rises in a step at the end of the normal stroke, so over-travel needs a higher pressure differential.
   - Changes: two parts instead of one, and each stage can be tuned independently. Covers the route "two springs, not a two-rate spring".
   - Genus: threshold-setting arrangement.
   - Credibility: high; common practice for springs.
3. **E2.3 Seat ring stiffness as the threshold.** *Not conceived; raised as a question in 01 Q6 — Q3.* Status: candidate.
   - Structure: a single-rate return spring. The over-travel threshold is set by the force the purge shoulder needs to deflect the deflectable ring element. In a superelastic alloy, the loading follows a stress plateau after the initial elastic rise, so the force–deflection curve behaves like a threshold.
   - Same purpose: the poppet stops at the end of its normal stroke until the pressure differential can overcome the ring's resistance.
   - Changes: one part fewer. The threshold is coupled to the ring's dimensions and to temperature, because the plateau stress of a superelastic alloy rises with temperature. A PEEK or spring-metal ring has no plateau, so its threshold is less distinct. Covers the route "no dedicated second spring stage".
   - Genus: threshold-setting arrangement.
   - Credibility: credible in principle. How much the ring contributes in the prototype is unknown.
4. **E2.4 Disc spring stack engaged after lost motion.** *Not conceived — Q2.* Status: candidate.
   - Structure: one or more conical disc springs of stainless steel, stacked, are engaged when a lost-motion clearance closes.
   - Same purpose: as E2.2, with high force in a short axial length.
   - Changes: more axial compactness, at the cost of more parts. Covers the same route as E2.2.
   - Genus: threshold-setting arrangement.
   - Credibility: high as a spring. Stack friction adds hysteresis.
5. **E2.5 Detent.** *Not conceived — Q2.* Status: candidate.
   - Structure: either a spring-loaded ball, or a radially sprung element, in the core body engages a circumferential groove on the poppet stem at the end of the normal stroke; or a permanent magnet in the core body attracts a ferritic stainless target on the poppet.
   - Same purpose: the poppet is held at the end of its normal stroke until the force exceeds a breakaway value.
   - Changes: the force falls after breakaway, so the poppet crosses over-travel quickly. The detent must release on the return. A brass poppet needs a ferritic target for the magnetic version. A sliding detent exposed to sealant is a failure mode for Prompt 15. Covers the route "no spring sets the threshold".
   - Genus: threshold-setting arrangement.
   - Credibility: moderate. The magnetic version avoids sliding contacts exposed to sealant.
6. **E2.6 Polymer compression bush as the second spring stage.** *Not conceived — Q2.* Status: candidate.
   - Structure: an annular bush of engineering polymer is engaged after lost motion.
   - Same purpose: as E2.2.
   - Changes: the material. Covers the route "a non-metallic second spring stage".
   - Genus: threshold-setting arrangement.
   - Credibility: moderate. Compression set and swelling in ammonia-bearing sealant are the risks. The §2 criticism of rubber concerns the seat, not the threshold.

#### 3. purge shoulder

1. **E3.1 Annular shoulder integral with the poppet, on the chamber side of the sealing face.** *Disclosed (§3(4)); geometry unknown (01 Q8).* Status: candidate (baseline).
2. **E3.2 Tapered purge shoulder.** *Not conceived — Q4.* Status: candidate.
   - Structure: a frustoconical flank on the poppet enters the seat ring during over-travel and deflects the seat ring radially outward by direct radial contact, in the way a mandrel expands a ring.
   - Same purpose: the seat ring is deflected only during over-travel.
   - Changes: the load on the ring is radial, not axial, so no axial-to-radial conversion geometry is needed (E5.5). The flank slides on the ring's inner surface: more friction and wear, but it also wipes that surface on the return. Covers the route "a straight-walled ring driven by a tapered poppet".
   - Genus: deflecting formation.
   - Credibility: high; this is a standard way of expanding a ring.
3. **E3.3 Discrete lugs.** *Not conceived — Q4.* Status: candidate.
   - Structure: two to four radial lugs on the poppet in place of a continuous annulus.
   - Same purpose: the seat ring is deflected locally during over-travel.
   - Changes: the ring ovalises (E6.3), the purge gap opens over arcs rather than all round, and less force is needed. Covers the route "no annular shoulder".
   - Genus: a deflecting formation that contacts the deflectable ring element at one or more places around its circumference.
   - Credibility: credible. The purge flow is non-uniform.
4. **E3.4 Separate collar fixed on the poppet stem.** *Not conceived — Q4.* Status: candidate.
   - Structure: a collar, for example of stainless steel on a brass poppet, is pressed, crimped or threaded onto the poppet stem.
   - Same purpose: as E3.1.
   - Changes: an assembly step, and a free choice of material for wear against the ring. Covers the route "the purge shoulder is not integral".
   - Genus: deflecting formation.
   - Credibility: high.
5. **E3.5 Return-spring retainer as the deflecting formation.** *Not conceived — Q4.* Status: candidate.
   - Structure: the retainer that seats the return spring on the poppet bears on the chamber-side end of the seat ring during over-travel.
   - Same purpose: as E3.1.
   - Changes: the contact moves to the other end of the ring, and one part does two jobs. Covers the route "the deflecting surface is a spring retainer, not a shoulder on the poppet".
   - Genus: deflecting formation.
   - Credibility: credible, if the stroke geometry allows it (01 Q8, Q36).

#### 4. deflectable ring element

1. **E4.1 One-piece seat ring that both seals and deflects.** *Disclosed (§3(3)): NiTi; PEEK in Alternative A (§6).* Status: candidate (baseline).
2. **E4.2 Fixed seat plus wiper ring.** *Disclosed as Alternative B (§6); details unknown (01 Q20, 03 Q7).* Status: candidate (baseline).
3. **E4.3 Slotted seat ring.** *Not conceived — Q5.* Status: candidate.
   - Structure: a short tubular ring with a continuous band at the sealing-edge end, and axial slots cut from the other end that form fingers. The fingers splay radially under the purge shoulder.
   - Same purpose: large radial deflection at low force and low strain. The continuous band keeps the sealing edge intact.
   - Changes: the purge gas can flow through the slots (E8.4). The slots can hold sealant (a failure mode for Prompt 15). It can be laser-cut from the same NiTi tube stock (§7). Covers the route "no convoluted wall".
   - Genus: deflectable ring element.
   - Credibility: high; this is the form of a collet.
4. **E4.4 Conical annular disc.** *Not conceived — Q5.* Status: candidate.
   - Structure: a thin frustoconical annulus held at one rim. Axial load from the purge shoulder flattens the cone, moving the free rim radially. With the inner rim held, the outer rim moves outward; with the outer rim held, the inner rim moves inward.
   - Same purpose: axial over-travel load becomes radial deflection of a ring edge.
   - Changes: short axial length, and a separate fixed seat is probably needed for sealing (as E4.2). Covers the route "a disc instead of a ring".
   - Genus: deflectable ring element.
   - Credibility: moderate. Radial movement per unit of axial stroke is small at shallow cone angles. Reaching a purge gap of the order disclosed (§4) needs design work, which only the inventor can confirm.
5. **E4.5 Integral flexure section.** *Not conceived — Q5.* Status: candidate.
   - Structure: a thin-walled convoluted or slotted section turned or moulded as part of the core body itself, for example in PEEK or in stainless steel.
   - Same purpose: as E4.1.
   - Changes: no separate ring and no interference fit, so the core body material must be resilient. Covers the route "no separate seat ring".
   - Genus: deflectable ring element.
   - Credibility: credible for PEEK and for spring-temper stainless steel. **Not credible for brass CW614N**, whose elastic strain limit is too low for the deflections of §4.
6. **E4.6 Split wiper ring.** *Not conceived — Q5; wiper-ring form only.* Status: candidate.
   - Structure: a ring with one axial split that opens circumferentially under a tapered purge shoulder (E3.2). It is used only as the wiper ring behind a fixed seat.
   - Same purpose: as E4.2.
   - Changes: the split is the purge opening. Covers a variant of Alternative B.
   - Genus: deflectable ring element.
   - Credibility: credible only where sealing is done by a fixed seat. **Not credible as a one-piece seat ring**, because the split breaks the sealing edge.

#### 5. convoluted wall

1. **E5.1 Wall with one or two convolutions.** *Disclosed (§3(3)); count and profile unknown (01 Q11).* Status: candidate (baseline).
2. **E5.2 Wall with three or more convolutions.** *Not conceived — Q5.* Status: candidate.
   - Structure: the same wall, with more convolutions.
   - Same purpose: axial load becomes radial deflection.
   - Changes: more axial compliance, and less radial deflection per convolution for a given load. Covers the route "just outside a one-or-two count".
   - Genus: axial-to-radial conversion geometry.
   - Credibility: credible up to the point where the wall mainly shortens axially. Beyond that point it no longer serves the purpose.
3. **E5.3 Frustoconical wall.** *Not conceived — Q5.* Status: candidate.
   - Structure: a plain wall with a conical flare. Axial load at the narrow end increases the flare and moves the free end outward.
   - Same purpose: as E5.1.
   - Changes: no convolution to form, which may be simpler to make. Covers the route "no convolution".
   - Genus: axial-to-radial conversion geometry.
   - Credibility: credible.
4. **E5.4 Cellular wall.** *Not conceived — Q5.* Status: candidate.
   - Structure: a laser-cut pattern of diamond or chevron cells between two continuous end bands. Under axial compression the cell struts rotate and the wall enlarges radially.
   - Same purpose: as E5.1.
   - Changes: the cells pass through the wall, so they can carry the purge flow (E8.4), and the sealing edge sits on the continuous end band. It fits the inventor's laser-cutting route (§7). The cells can trap sealant. Covers the route "no convolution".
   - Genus: axial-to-radial conversion geometry.
   - Credibility: credible. Laser-cut superelastic cell structures are an established class of product. The coupling between axial shortening and radial enlargement depends on the cell geometry and would need design.
5. **E5.5 Plain wall deflected directly by a tapered purge shoulder (E3.2).** *Not conceived — Q4.* Status: candidate.
   - Structure: a straight-walled ring.
   - Same purpose: radial deflection without any conversion geometry.
   - Changes: the convoluted wall is not needed. Covers the route "a straight wall".
   - Genus: deflectable ring element (no wall-profile limitation).
   - Credibility: high.

**Finding for Claims Architect (subject to Gate 2).** E3.2 with E5.5 would show that the convoluted wall is a means, not an essential feature. If the inventor confirms either, the enablement risk recorded against C12 in `03` is reduced.

#### 6. radial deflection

1. **E6.1 Radially outward.** *Disclosed (§2; Alternative B, §6).* Status: candidate (baseline).
2. **E6.2 Radially inward at the surface that bounds the purge gap.** *Not conceived — Q1, Q7.* Status: candidate.
   - Structure: the part of the seat ring's outer surface that touches the core body bore at rest moves inward, away from that bore. Two mechanisms would do this: axial tension on an outward convolution, which flattens its crest, or axial compression of an inward convolution, which deepens it.
   - Same purpose: it opens a purge gap at the seat ring's outer surface. That is the location given in §3(6) and the location of the film found in the bench data.
   - Changes: the sense of deflection, and the way the purge shoulder is coupled to the ring.
   - Genus: radial deflection (the direction is neutral in LOCKED).
   - Credibility: credible mechanics. **This is offered as a candidate only. It does not resolve 01 Q1 and Q2 and must not be written into the Description as the inventor's mechanism unless the inventor confirms it.**
3. **E6.3 Ovalising deflection.** *Not conceived — Q4.* Status: candidate.
   - Structure: loading at discrete points (E3.3) moves the ring outward at the load points and inward about 90° away.
   - Same purpose: it opens gaps on both the ring's inner and outer surfaces, on different arcs.
   - Changes: a non-axisymmetric purge gap.
   - Genus: radial deflection.
   - Credibility: credible; this is standard ring mechanics.

#### 7. purge gap

No surface pair is assumed here to be the inventor's. Each entry states the direction of deflection it needs, so that the inventor can pick the true one at Gate 2 (01 Q1, Q2).

1. **E7.1 Between the seat ring's outer surface and the core body bore.** *Disclosed location (§3(6)); opening mechanism unresolved.* Status: candidate.
   - Opens only by inward movement of that surface (E6.2 or E6.3). This is consistent with the film found on the ring's outer surface (bench data), and in tension with "flexes radially outward" (§2) and with the interference fit (§7) unless the fit is confined to one band (E14.2, E14.3).
2. **E7.2 Between the seat ring's outer surface and the stem bore, through windows in the core body.** *Wording of §2 ("stem bore"); not otherwise conceived — Q1.* Status: candidate.
   - Needs openings through the wall of the core body at the ring, and inward movement as in E7.1.
   - Credibility: moderate; it weakens the core body.
3. **E7.3 Between the seat ring's inner surface and the poppet, on the chamber side of the sealing edge.** *Not conceived — Q1.* Status: candidate.
   - Opens by outward deflection, as in §2. The purge flow passes along the poppet stem, which is the capillary path named in §1.
   - Credibility: moderate. The gap is distinct from the main passage only if the clearance between the ring's inner surface and the poppet is closed or very small at rest, and the disclosure does not say so.
4. **E7.4 Through-wall openings in the seat ring (E4.3, E5.4), closed at rest by contact with the core body bore and uncovered by deflection.** *Not conceived — Q14.* Status: candidate.
   - Credibility: credible if the openings sit where the wall moves away from its contact surface.

Genus for all four: a purge passage, bounded at least in part by a surface of the deflectable ring element, which is closed in the closed state and in the normal-open state and is opened by radial deflection.

#### 8. purge flow path

1. **E8.1 From the supply side through the purge gap into the inflatable chamber, alongside the main passage.** *Disclosed (§2; drawings README, FIG-2).* Status: candidate (baseline).
2. **E8.2 Purge ports.** *Not conceived — Q14.* Status: candidate.
   - Structure: radial holes or slots through the wall of the core body, on the chamber side of the purge gap, lead to the clearance between the core body and the stem bore and on to the inflatable chamber.
   - Same purpose: they carry the air purge and the dislodged sealant film into the inflatable chamber.
   - Changes: they fix where the purged sealant film leaves the valve core, and they need machining of the core body. The ports can themselves foul. Covers the route "the purge exits sideways, not axially".
   - Genus: purge flow path.
   - Credibility: high.
3. **E8.3 Flutes in the core body bore.** *Not conceived — Q14.* Status: candidate.
   - Structure: axial grooves in the core body bore behind the seat ring. At rest the ring's outer surface lies on the lands between them; when that surface moves inward (E6.2), the flutes connect to the supply side.
   - Same purpose: as E8.1.
   - Changes: the flutes set the purge flow area independently of the size of the purge gap opening.
   - Genus: purge flow path.
   - Credibility: credible.
4. **E8.4 Through the wall of the seat ring (slots or cells, E4.3, E5.4).** *Not conceived — Q14.* Status: candidate.
   - Credibility: credible.
5. **E8.5 Purge gas.** *Genus note, not a structure.* Status: candidate.
   - Any inflation gas: air from a floor pump, hand pump or compressor, or gas from a compressed-CO2 inflation device. Whether a CO2 inflation device reaches the over-travel threshold is unknown, and the risk of cold to the ring is open (01 Q5, Q28). E1.5 reverses the direction of flow.

#### 9. shape recovery

1. **E9.1 Superelastic recovery of NiTi.** *Disclosed (§2).* Status: candidate (baseline).
2. **E9.2 Elastic recovery of PEEK, slower and with less force.** *Disclosed (§6, Alternative A).* Status: candidate (baseline).
3. **E9.3 Elastic recovery of a spring metal.** *Disclosed for the stainless wiper ring (§6, Alternative B); other spring metals in E12.4.* Status: candidate.
4. **E9.4 Positively driven recovery.** *Not conceived — Q8.* Status: candidate.
   - Structure: a second formation on the poppet, on the opposite side of the ring from the deflecting formation, meets the ring on the return and pushes it back to its at-rest shape.
   - Same purpose: the purge gap closes when the pressure differential falls.
   - Changes: closing no longer depends only on the material's recovery, which guards against residual set (01 Q27) and against cold below the martensite start temperature (01 Q28). Covers the route "a ring that does not recover by itself".
   - Genus: elastic return, or return driven by the poppet.
   - Credibility: credible. It adds contact and friction on the return.
5. **E9.5 Recovery by warming above the austenite finish temperature.** *Related to the thermally actuated purge (§6); separate concept (03 C32) — Q12 of 03.* Status: candidate.
   - Listed only as a recovery mechanism if a ring left martensitic by chilling from a CO2 inflation device is warmed. It is not a rung of the nucleus.

#### 10. snap-back wipe

1. **E10.1 The recovering seat ring moves across the sealing face or an adjacent poppet surface.** *Disclosed (§2); geometry unknown (01 Q10).* Status: candidate (baseline).
2. **E10.2 Wipe by the wiper ring on recovery.** *Alternative B (§6); whether it wipes is unknown (03 Q7).* Status: candidate.
3. **E10.3 Fixed wiping land.** *Not conceived — Q8.* Status: candidate.
   - Structure: a close-clearance land in the core body bore, or on the fixed seat, through which the poppet passes on every stroke. Relative axial movement shears the sealant film. The seat ring deflection only opens the purge gap.
   - Same purpose: mechanical removal of sealant film from the poppet.
   - Changes: the wipe no longer depends on ring recovery. Covers the route "a wipe without a recovering ring".
   - Genus: mechanical wipe.
   - Credibility: credible. The close clearance is itself a place for sealant film to collect (a failure mode for Prompt 15).
4. **E10.4 Defined wiping edge.** *Not conceived — Q8.* Status: candidate.
   - Structure: a sharp-cornered edge on the ring's inner surface, set by the laser-cut profile and a limited depth of electropolishing, presented to the poppet as the ring recovers.
   - Same purpose: it concentrates contact pressure, so the ring shears the sealant film rather than riding over it.
   - Changes: a trade-off against electropolishing, which rounds edges (§7).
   - Genus: snap-back wipe.
   - Credibility: credible. The purpose of electropolishing is unknown (03 Q15).
5. **E10.5 Rotational wipe.** *Not conceived — Q8.* Status: candidate.
   - Structure: a helical guide between the poppet stem and the core body turns the poppet a few degrees during over-travel and back again on the return, so that the sealing face rubs the sealing edge circumferentially.
   - Same purpose: mechanical removal of sealant film.
   - Changes: more friction, and wear of the sealing surfaces that may raise leak-down.
   - Genus: mechanical wipe.
   - Credibility: moderate.

#### 11. sealing face

1. **E11.1 Conical sealing face on the sealing edge, metal to metal.** *Disclosed (§3(4)); cone angle, and whether any elastomer is present, unknown (01 Q9).* Status: candidate (baseline).
2. **E11.2 Hard-anodised aluminium sealing face.** *Disclosed (§5); not built.* Status: candidate (baseline).
3. **E11.3 Part-spherical sealing face.** *Not conceived — Q13.* Status: candidate.
   - Line contact on the sealing edge that tolerates misalignment of the poppet. Genus: sealing surface. Credibility: high.
4. **E11.4 Flat sealing face bearing on the axial end of the seat ring.** *Not conceived — Q13.* Status: candidate.
   - Genus: sealing surface. Credibility: credible. It is less self-centring, and film on the sealing surfaces has more effect on it.
5. **E11.5 Polymer sealing face, for example a PEEK facing on the poppet.** *Not conceived — Q13.* Status: candidate.
   - Lower leak-down against a metal sealing edge. Genus: sealing surface. Credibility: credible. §2's argument that latex embeds in rubber may extend to soft polymers, so the inventor must confirm.
6. **E11.6 Hard low-adhesion coating on the sealing face (for example electroless nickel or diamond-like carbon), used together with the purge.** *Not conceived — Q13.* Status: candidate.
   - §1 says that coatings used alone only slow build-up, so this is useful only in combination with the purge. Genus: sealing surface. Credibility: credible.

#### 12. superelastic alloy

1. **E12.1 Binary NiTi, nominally 55.8 wt% nickel content.** *Disclosed (§5).* Status: candidate (baseline).
2. **E12.2 Ternary NiTi: NiTiCu for narrower hysteresis and more stable cycling; NiTiFe or NiTiCr for a lower austenite finish temperature.** *Not conceived — Q6.* Status: candidate.
   - Changes: the transformation temperatures and the plateau stress, which interact with E2.3 and section 13.
   - Genus: superelastic alloy.
   - Credibility: established alloy families. Availability as tube stock at 2.7 mm outer diameter is not verified.
3. **E12.3 Copper-based superelastic alloys (Cu-Al-Mn, Cu-Al-Ni).** *Not conceived — Q6.* Status: candidate.
   - Genus: superelastic alloy.
   - Credibility: **low with ammonia-bearing liquid sealant**, because copper alloys are attacked by ammonia. Credible only with ammonia-free liquid sealant (01 Q29).
4. **E12.4 Spring metals without a phase transformation: beta-titanium alloys, precipitation-hardened stainless steel (17-7PH), cold-worked austenitic stainless steel.** *Stainless is disclosed only for the wiper ring (§6); otherwise not conceived — Q6.* Status: candidate.
   - Changes: recoverable strain is about an order of magnitude below that of NiTi, so a thinner wall, smaller deflection or slotted form is needed (E4.3). There is no dependence on the austenite finish temperature, which avoids the cold risk of 01 Q28.
   - Genus: resilient metal.
   - Credibility: credible with a redesigned geometry.
5. **E12.5 Resilient engineering polymers: PEEK (disclosed, §6); PPS or PEI as chemically resistant alternatives.** *PPS and PEI not conceived — Q6.* Status: candidate.
   - Changes: creep under a sustained interference fit, and weaker recovery (§6).
   - Genus: resilient polymer.
   - Credibility: moderate for PPS and PEI. Resistance to ammonia-bearing liquid sealant must be checked.

#### 13. austenite finish temperature

1. **E13.1 Austenite finish temperature below 5 °C.** *Disclosed (§4).* Status: candidate (baseline).
2. **E13.2 Lower austenite finish temperature, set by nickel content or by shape-setting time and temperature.** *Not conceived — Q6.* Status: candidate.
   - Changes: more margin against chilling by a CO2 inflation device (01 Q28). A higher plateau stress at service temperature raises the ring's contribution to the over-travel threshold (E2.3).
   - Genus: superelastic at the service temperature of the inflation valve.
   - Credibility: credible. Values are left to Prompt 13; none is asserted.
3. **E13.3 No dependence on transformation temperature: materials from E12.4 or E12.5.** Status: candidate.

#### 14. interference fit

1. **E14.1 Interference fit of about 0.03 mm on diameter, against the internal shoulder.** *Disclosed (§7).* Status: candidate (baseline).
2. **E14.2 Crimped lip.** *Not conceived — Q10.* Status: candidate.
   - Structure: a lip on the core body is rolled or swaged over the end of the seat ring.
   - Same purpose: it retains the ring axially.
   - Changes: the ring's outer surface is freed from radial interference, which removes the conflict with a purge gap at the outer surface (E7.1).
   - Genus: ring retention.
   - Credibility: high; brass swages readily.
3. **E14.3 Retaining sleeve.** *Not conceived — Q10.* Status: candidate.
   - Structure: a sleeve pressed or threaded into the core body clamps the ring against the internal shoulder.
   - Same purpose and changes: as E14.2, with one more part.
   - Genus: ring retention.
   - Credibility: high.
4. **E14.4 Adhesive bond with an ammonia-resistant adhesive.** *Not conceived — Q10.* Status: candidate.
   - Genus: ring retention.
   - Credibility: moderate. Adhesion to the oxide surface of NiTi, and exposure to liquid sealant, are the risks.
5. **E14.5 Seat ring integral with the core body (E4.5).** Status: candidate.
6. **E14.6 Seat ring carried by the valve stem instead of the core body.** *Not conceived — Q12.* Status: candidate.
   - Changes: the ring becomes part of the valve stem assembly. Covers the route "a valve core without the ring" against core-level claims (02 rank 1).
   - Genus: ring retention.
   - Credibility: credible, particularly in non-removable valves (E16.3).

#### 15. shape-setting (seat ring manufacture)

1. **E15.1 Laser cutting from NiTi tube stock, shape-setting at 500 °C for 10 minutes in a fixture, water quench, then electropolishing.** *Disclosed (§7).* Status: candidate (baseline).
2. **E15.2 Convolution formed by roll-forming with profiled rollers, in stages, with shape-setting between stages.** *Not conceived — Q11.* Status: candidate.
   - Credibility: credible. Staged forming with intermediate shape-setting is normal NiTi practice.
3. **E15.3 Convolution formed by internal pressure in a split die (hydroforming).** *Not conceived — Q11.* Status: candidate.
   - Credibility: credible for stainless steel; difficult for NiTi at room temperature.
4. **E15.4 Injection moulding of a PEEK seat ring.** *Alternative A material (§6); process not conceived — Q11.* Status: candidate.
   - Credibility: moderate. A 0.20 mm wall over a free length of 3.0 mm is micro-moulding territory.
5. **E15.5 Stamping or deep drawing from strip.** *Not conceived — Q11.* Status: candidate.
   - For a stainless wiper ring (E4.2) or a conical annular disc (E4.4). Credibility: high.
6. **E15.6 Photochemical etching of flat sheet for slotted or cellular patterns, then rolling and joining.** *Not conceived — Q11.* Status: candidate.
   - Credibility: high for stainless steel. Moderate for NiTi, because of the fatigue life of the seam weld.
7. **E15.7 Mechanical or chemical polishing in place of electropolishing.** *Not conceived — Q11.* Status: candidate.
   - The function of electropolishing is unknown (03 Q15). Credibility: credible.

#### 16. valve core

1. **E16.1 Presta-pattern valve core that can be removed from the valve stem.** *Disclosed (§3).* Status: candidate (baseline).
2. **E16.2 Schrader-pattern valve core.** *Not conceived — Q12 (01 Q26).* Status: candidate.
   - Changes: a larger bore, which gives room for E1.2. The core pin is depressed by the head (E1.4).
   - Genus: valve mechanism.
   - Credibility: credible.
3. **E16.3 Non-removable inflation valve.** *Not conceived — Q12 (01 Q33).* Status: candidate.
   - Structure: the seat ring, poppet and return spring are carried directly in the valve stem, with no separate core body.
   - Changes: covers the route "no valve core" against core-level claims.
   - Genus: valve mechanism.
   - Credibility: high.

**Findings for Claims Architect (each only if confirmed at Gate 2).**
- E2.3: the second spring stage may not be needed as a separate part, which supports functional language for the threshold (02 rank 7; 03 C3).
- E3.2 and E5.5: the convoluted wall is a means, not an essential feature.
- E1.2 and E1.3: the deflecting formation need not be on the poppet.
- E10.3: a mechanical wipe is possible without ring recovery.
- E1.4: the pressure threshold can be avoided by mechanical actuation.
- E14.6 and E16.3: core-level claims can be avoided by moving the ring into the valve stem.


---

## From `13.md`

### Parameter Ladders

Status: candidate. This is a drafting and analysis aid prepared by AI. It says nothing about patentability and is not legal advice; qualified patent counsel signs off before anything is filed. Nothing in this deliverable is confirmed: every proposed rung is a candidate until Human Gate 2 decides it is technically real and within what the inventor has conceived.

**Sources.** `intake/disclosure.md` is cited §1–§9; `intake/data/bench-test.md` as "bench data"; `runs/r1/P1/01.md` and `03.md` as "01 (x)" / "03 (x)"; `terminology/LOCKED.md` as "locked". Prompts 02 (commercial value), 09 and 10 (prior-art differentiation, white space) were not available and are not used. Only §4's parameters carry an inventor-stated broad range ("the ranges we believe would work"); every other numeric parameter in the disclosure is a single prototype or test value with no stated range.

**Method for proposed rungs.** Where §4 gives a broad range [L, U] and a prototype (representative) value R, this analysis proposes: intermediate range = the middle band spanning 60% of (U − L), centred on R and clipped to [L, U]; preferred range = the middle band spanning 25% of (U − L), centred on R and clipped to [L, U]. This is a drafting convention for generating nested fallback positions from a single disclosed range and a single worked example; it is not itself data, is not derived from any calculation or test, and every cell built this way is marked "needs confirmation" below. No value outside the inventor's stated broad range is proposed for any parameter, and no range is proposed at all for a parameter that has no stated range to interpolate from.

#### Table 1 — Parameters with an inventor-stated broad range (§4), proposed ladder

| Parameter (locked term) | Unit | Broad range | Intermediate range | Preferred range | Endpoints | Representative value | Source | Confirmation needed |
|---|---|---|---|---|---|---|---|---|
| seat ring inner diameter | mm | 2.0–2.6 | 2.1–2.5 (proposed) | 2.2–2.4 (proposed) | 2.0 / 2.6 | 2.3 | §4 (broad, endpoints, representative); this analysis (intermediate, preferred) | Yes — broad is the inventor's belief, not evidenced; intermediate/preferred are this analysis's proposal; only the representative value (2.3 mm) is a built prototype figure (§7) |
| seat ring wall thickness | mm | 0.15–0.30 | 0.16–0.24 (proposed) | 0.18–0.22 (proposed) | 0.15 / 0.30 | 0.20 | §4, §7; this analysis | Yes — as above |
| seat ring free length | mm | 2.5–4.0 | 2.6–3.5 (proposed) | 2.8–3.2 (proposed) | 2.5 / 4.0 | 3.0 | §4; this analysis | Yes — as above |
| convolution amplitude | mm | 0.08–0.20 | 0.08–0.16 (proposed) | 0.11–0.14 (proposed) | 0.08 / 0.20 | 0.12 | §4; this analysis | Yes — as above |
| over-travel distance | mm | 0.4–0.9 | 0.4–0.65 (proposed) | 0.44–0.56 (proposed) | 0.4 / 0.9 | 0.5 | §4 (broad, endpoints, representative — representative **not independently measured in the test**, only inferred from an audible snap on pump-head removal, 01 (h), A9); this analysis (intermediate, preferred) | Yes — as above, plus the representative value itself is an indirect inference, not a measurement (01 Q23) |
| purge gap opening | mm, radial | 0.10–0.25 | 0.11–0.20 (proposed) | 0.13–0.17 (proposed) | 0.10 / 0.25 | 0.15 | §4 (representative not independently measured in the test); this analysis | Yes — as the over-travel distance row, **and** the purge gap's location and opening mechanism are internally inconsistent between §2 and §3(6)/§7 (01 Q1, Q2; 03 Q2); no value in this row can be treated as enabled until that is resolved |
| crack pressure | bar | 0.8–1.5 | 0.8–1.2 (proposed) | 0.91–1.09 (proposed) | 0.8 / 1.5 | 1.0 | §4; this analysis | Yes — as the first four rows |
| over-travel threshold | bar | 2.5–5.0 | 2.75–4.25 (proposed) | 3.2–3.8 (proposed) | 2.5 / 5.0 | 3.5 | §4; this analysis | Yes — as above, and additionally tied to which inflation devices must reach it (03 Q9; §2's unsupported "every floor pump reaches") |

#### Table 2 — Single prototype/spec value, no range disclosed (ladder cannot be proposed without data)

| Parameter (locked term) | Unit | Broad range | Intermediate range | Preferred range | Endpoints | Representative value | Source | Confirmation needed |
|---|---|---|---|---|---|---|---|---|
| normal stroke | mm | not disclosed | not disclosed | not disclosed | not disclosed | 0.6 | §4 | Yes — no range given; no basis to propose one |
| seat ring outer diameter | mm | not disclosed | not disclosed | not disclosed | not disclosed | 2.7 (inferred) | §7, *inferred* from tube stock (01 A2); not asserted by the inventor as a ring dimension | Yes — the value itself is inferred, not stated |
| number of convolutions | count | not disclosed | not disclosed | not disclosed | 1 / 2 | not stated which the prototype used | §3(3) ("one or two") | Yes — prototype count unstated (01 Q11); whether the convolution is essential at all is separately open (03 Q4) |
| nickel content | wt% Ni | not disclosed | not disclosed | not disclosed | not disclosed | 55.8 (nominal) | §5 | Yes — no tolerance stated (01 Q14) |
| austenite finish temperature (Af), seat ring | °C | < 5 (upper bound only) | not disclosed | not disclosed | upper 5; lower none | "specified below 5 °C" | §4 | Yes — no lower bound; As, Ms, Mf not given (01 Q13, Q28) |
| interference fit (seat ring in core body) | mm on diameter | not disclosed | not disclosed | not disclosed | not disclosed | approx. 0.03 | §7 | Yes — single approximate value; working range not given (01 Q17) |
| shape-setting temperature | °C | not disclosed | not disclosed | not disclosed | not disclosed | 500 | §7 | Yes — no process window given (01 Q32) |
| shape-setting duration | min | not disclosed | not disclosed | not disclosed | not disclosed | 10 | §7 | Yes — no process window given (01 Q32) |
| valve stem outer diameter | mm | not proposed (conventional Presta dimension) | — | — | — | 6 | §3(1) | No — conventional, industry-standard dimension; not a proposed fallback range |
| thermal variant austenite finish temperature (Af), two-way alloy (§6, F5) | °C | approx. 35–40 | not disclosed | not disclosed | approx. 35 / 40 | none — not built or tested | §6 | Yes — no prototype and no data; inventor states doubt about pursuing this variant at all (03 Q12) |

#### Table 3 — Test-derived / measured values (bench data, n = 3 per group)

| Parameter (locked term) | Unit | Broad range | Intermediate range | Preferred range | Endpoints | Representative value | Source | Confirmation needed |
|---|---|---|---|---|---|---|---|---|
| test inflation pressure | bar | — | — | — | — | 6 | §8, bench data (test protocol, as used) | No — as-used test condition; effect at other pressures untested |
| test hold duration | h | — | — | — | — | 24 | §8, bench data | No — as-used test condition |
| test hold temperature | °C | — | — | — | — | 22 | §8, bench data | No — as-used test condition; "all riding temperatures" (§4) is otherwise unquantified |
| sealant charge volume | ml | — | — | — | — | 60 | §8, bench data | No — as-used test condition; sealant product and ammonia content unstated (01 Q23) |
| leak-down failure threshold | bar/24h | — | — | — | — | > 0.5 (failure criterion) | §8 | No — as defined in the test protocol |
| blockage response threshold | s | — | — | — | — | 5 (failure criterion) | §8 | No — as defined in the test protocol |
| leak-down, prototype at cycle 40 | bar/24h | — | — | — | 0.1 / 0.2 | 0.1–0.2 (P-1: 0.1; P-2: 0.1; P-3: 0.2) | bench data | Yes — measured, but n = 3; behaviour beyond cycle 40 unknown (01 Q27, Q30) |
| inflation time, prototype at cycle 1 | s | — | — | — | 41 / 44 | 41–44 (P-2: 41; P-1: 43; P-3: 44) | bench data | Yes — measured, n = 3 |
| inflation time, prototype at cycle 40 | s | — | — | — | 46 / 50 | 46–50 (P-2: 46; P-1: 47; P-3: 50) | bench data | Yes — measured, n = 3 |
| inflation time, conventional valve core at cycle 1 | s | — | — | — | 40 / 42 | 40–42 (C-2: 40; C-1: 41; C-3: 42) | bench data | Yes — measured, n = 3, comparator only |
| cycles completed without failure, prototype | count | — | — | — | — | 40 (all 3 units; censored — no failure observed, so true fatigue life not established) | §8, bench data | Yes — censored data; fatigue life beyond 40 cycles is an unresolved known unknown (§9; 01 Q27) |
| cycles to failure, conventional valve core | count | — | — | — | 12 / 18 | 12–18 (C-2: 12; C-1: 14; C-3: 18) | §8, bench data | No, as measured comparator data — though n = 3 |

#### Table 4 — Parameters named in the disclosure with no value at all (ladder cannot be started)

| Parameter (locked term) | Unit | Broad range | Intermediate range | Preferred range | Endpoints | Representative value | Source | Confirmation needed |
|---|---|---|---|---|---|---|---|---|
| sealant ammonia concentration | — | not disclosed | not disclosed | not disclosed | not disclosed | none | §1, §5 (ammonia-bearing latex sealant, unquantified) | Yes (01 Q23) |
| first spring stage rate/force | N or N/mm | not disclosed | not disclosed | not disclosed | not disclosed | none | §3(5) | Yes (01 Q7) |
| second spring stage rate/force | N or N/mm | not disclosed | not disclosed | not disclosed | not disclosed | none | §3(5) | Yes (01 Q7) |
| sealing face cone angle | ° | not disclosed | not disclosed | not disclosed | not disclosed | none | §3(4) | Yes (01 Q9) |
| purge shoulder axial clearance | mm | not disclosed | not disclosed | not disclosed | not disclosed | none | §2, §3(4) | Yes (01 Q8) |
| core body bore diameter at seat ring | mm | not disclosed | not disclosed | not disclosed | not disclosed | none | — | Yes (01 Q16) |
| NiTi austenite start temperature (As) | °C | not disclosed | not disclosed | not disclosed | not disclosed | none | — | Yes (01 Q13, Q28) |
| NiTi martensite start temperature (Ms) | °C | not disclosed | not disclosed | not disclosed | not disclosed | none | — | Yes (01 Q13, Q28) |
| NiTi martensite finish temperature (Mf) | °C | not disclosed | not disclosed | not disclosed | not disclosed | none | — | Yes (01 Q13, Q28) |
| NiTi composition tolerance | wt% | not disclosed | not disclosed | not disclosed | not disclosed | none | §5 | Yes (01 Q14) |


---

## From `14.md`

### Combination Matrix

Status: candidate. Nothing in this section is confirmed; every combination and every draft sentence below is a candidate pending Human Gate 2, and pending the inventor's answers to the questions cited. This is a drafting and analysis aid prepared by AI. It is not legal advice and makes no statement about patentability; qualified patent counsel signs off before anything is filed.

**Inputs used.** `runs/r1/P3/12.md` (equivalent architecture library) and `runs/r1/P2/10.md` (prior-art white space) do not yet exist, so the core-embodiment columns below are built only from the nucleus ladder in `03` and the inventor's own §6 alternatives, not from a fuller equivalents library or a white-space-driven set of design-around embodiments. See Assumption A1 and Open Question Q7. This map should be revisited once `12` and `10` exist.

**Core embodiments (columns).** Three structurally distinct embodiments are read from `01`/`03`, all sharing the essential nucleus (N0: over-travel, purge shoulder, deflectable ring element, purge gap, air purge, recovery):

- **E-I — superelastic seat ring embodiment.** The seat ring is a single part that both seats the poppet and is deflected during over-travel (nucleus rung N2 onward, materialised in NiTi at N4–N7; §2, §3(3)–(4), §4, §5, §7).
- **E-II — PEEK seat ring embodiment.** Same one-piece seat-ring structure as E-I (nucleus through N3, "the same convoluted wall"), with the seat ring formed from PEEK instead of a superelastic alloy (§6, Alternative A).
- **E-III — fixed seat and wiper ring embodiment.** Sealing is performed by a rigid fixed seat; a separate wiper ring, deflected outward by the purge shoulder, opens the purge gap (nucleus through N1 only; excluded from N2 onward). One more part and more axial length than E-I/E-II (§6, Alternative B).

**Optional features (rows).** Drawn from `03`'s advantageous/exemplary classification (C9–C30) and from the optional components in `01`(e), limited to features that are not already part of a core embodiment's own structural definition.

| # | Optional feature (source) | E-I: superelastic seat ring | E-II: PEEK seat ring | E-III: fixed seat + wiper ring | Status |
|---|---|---|---|---|---|
| 1 | Snap-back wipe as a claimed effect (C9; §2) | Compatible | Conditional [a] | Conditional [b] | candidate |
| 2 | Convoluted wall geometry on the deflectable ring element (C12/C13; §3(3)) | Compatible | Compatible | Conditional [c] | candidate |
| 3 | Two-rate return spring / threshold arrangement (C17; §3(5)) | Compatible | Compatible | Compatible | candidate |
| 4 | Prototype-derived pressure and dimensional ranges, N6 (C19–C21; §4) | Compatible (basis of the ranges) | Conditional [d] | Conditional [d] | candidate |
| 5 | Stainless 303 core body (F1; §5) | Compatible | Compatible | Compatible | candidate |
| 6 | Hard-anodised aluminium sealing face on the poppet (F2; §5) | Compatible | Compatible | Compatible | candidate |
| 7 | Electropolished surface finish on the deflectable ring element (C25; §7) | Compatible | **Incompatible** [e] | Conditional [f] | candidate |
| 8 | Lock nut (C30; §3(7)) | Compatible | Compatible | Compatible | candidate |
| 9 | Austenite finish temperature (Af) below 5 °C specification (C16; §4) | Compatible (essential if a shape-memory alloy is used) | **Incompatible** [g] | **Incompatible** [h] | candidate |

**Footnotes (conditional and incompatible cells).**

- **[a]** §6 states the PEEK seat ring gives "some radial compliance, but recovery is slower and snap-back force lower, so the wipe is weaker." The wipe is not excluded, but it is degraded, and no lower bound on wipe force is disclosed. A sentence claiming the wipe for E-II must not assert it is as effective as in E-I. See Q1.
- **[b]** Whether the wiper ring of E-III wipes the poppet face on recovery, and if so which surface moves across which, is not stated in the disclosure (`03` Q7). Marked conditional rather than compatible until the inventor confirms. See Q1 below.
- **[c]** §6 says the wiper ring is "deflected outward" but does not state its wall form. A convoluted wall is a candidate way to achieve that deflection by analogy with E-I/E-II, but it is not disclosed for the wiper ring. See Q2.
- **[d]** The N6 ranges (crack pressure, over-travel threshold, over-travel distance, purge gap opening, ring dimensions) were derived against the NiTi seat ring's stiffness and recovery behaviour. PEEK's lower stiffness and slower recovery (§6), and the extra part and axial length of E-III (§6), make it technically uncertain whether the same numeric ranges hold. Flagged for inventor confirmation, not asserted. See Q3.
- **[e]** Electropolishing is an electrochemical metal-finishing process that removes surface oxide by anodic dissolution; it has no counterpart process for a polymer such as PEEK. Marking this cell compatible would assert a technically incoherent permutation. This is a general materials-science fact about the named process, not an invented fact about the invention.
- **[f]** The disclosed E-III wiper ring is "stainless" (§6), i.e. a metal, so electropolishing is technically feasible on it, but the disclosure does not describe this step for the wiper ring. Marked conditional, not compatible, until confirmed. See Q5.
- **[g]** Af is a transformation temperature of a shape-memory/superelastic alloy. PEEK is a thermoplastic polymer with a glass transition temperature, not an alloy transformation temperature; it does not have an Af. Asserting an Af specification for the PEEK ring would be technically incoherent.
- **[h]** The wiper ring of E-III is disclosed only as "stainless spring" (§6), read as conventional spring steel, not a superelastic alloy. As disclosed, no Af applies. A superelastic wiper-ring species is conceptually possible but is not in the disclosure. See Q4.

#### Commercially important or patentably distinct combinations

Ranking basis: `02`'s commercial value map and `03`'s rung ordering (which shows E-II and E-III are the inventor's own named design-arounds).

| # | Combination | Core embodiment | Optional features | Why important / distinct | Rests on | Status |
|---|---|---|---|---|---|---|
| CB1 | Full nucleus product | E-I | Rows 3, 4, 8, 9 (two-rate spring, N6 ranges, lock nut, Af < 5 °C) | This is the tested, evidenced embodiment and the main commercial product (`02` rank 1–2; bench data, 40-cycle result) | §2–§5, §7, §4; bench data | candidate |
| CB2 | Corrosion-resistant line | E-I | Row 5 (stainless 303 core body) | Named premium variant for ammonia-bearing sealant (`02` rank 9); independent of ring material, so also combinable with E-II/E-III | §5 (F1) | candidate |
| CB3 | Lower-cost line | E-II | Rows 2, 3, 8 (convoluted wall, two-rate spring, lock nut); **not** row 9 (Af) | Inventor's own named cost-reduction design-around (`02` rank 5, `03` N4 exclusion); closes a design-around a competitor could otherwise use to avoid a superelastic-alloy limitation | §6 (Alternative A) | candidate |
| CB4 | Design-around-closing split architecture | E-III | Rows 3, 5, 8 (two-rate spring, stainless body, lock nut); rows 1, 2, 7 only as conditional/candidate pending Q1–Q2, Q5 | Inventor's own named structural design-around separating sealing from purge/wipe (`02` rank 6, `03` N2 exclusion); the claim family most likely to catch a competitor who splits the seat and wiper into two parts specifically to avoid a one-piece-ring claim | §6 (Alternative B) | candidate |
| CB5 | Retrofit core, ring-material-agnostic | E-I or E-II or E-III | Row 8 (lock nut) only, core sold without the valve stem | Independent replacement-core product line (`02` rank 1); demonstrates that ring-material and architecture choice are orthogonal to the stem-inclusion claim strategy question raised in `02` Q1 | §1 ("cores are sold in multipacks"); `01` Q33 | candidate |

#### Draft specification language

Each sentence is a candidate for the Description, written in locked terms, and is expressly scoped so that it does not assert an incompatible permutation (rows 7 and 9, footnotes [e]–[h]).

1. "In some embodiments, the deflectable ring element is a seat ring formed from a superelastic alloy, such as NiTi, having an austenite finish temperature below 5 °C; in other embodiments, the deflectable ring element is a seat ring formed from a polymer, such as PEEK, or is a wiper ring separate from a fixed seat." — supports CB1/CB3/CB4 as alternative species of the same genus, without tying the polymer or wiper-ring species to the Af limitation. (Rows 1, 9)

2. "Where the deflectable ring element is formed from a superelastic alloy, the alloy is selected to have an austenite finish temperature below a threshold, such as 5 °C, so that the ring element remains superelastic across the intended range of ambient temperatures." — conditions the Af limitation expressly on the superelastic-alloy species, consistent with footnotes [g]/[h]. (Row 9)

3. "The core body may be formed from a corrosion-resistant material, such as stainless steel, independently of whether the deflectable ring element is a superelastic seat ring, a polymer seat ring, or a wiper ring used together with a separate fixed seat." — supports CB2 as combinable across all three core embodiments. (Row 5)

4. "The convoluted wall geometry described herein for converting axial load into radial deflection may be applied to a seat ring that also performs a sealing function, or, in embodiments having a separate fixed seat, to a wiper ring that performs the purging and wiping function without also sealing." — supports extending row 2 to E-III as a candidate, expressly flagged in the Description as a candidate application rather than a confirmed one, pending Q2. (Row 2)

5. "A lock nut for manually holding the poppet closed may be combined with any of the seat ring, PEEK seat ring, or fixed-seat-and-wiper-ring embodiments described herein." — supports CB5 and row 8 generally. (Row 8)

6. "In embodiments in which the deflectable ring element is a polymer, such as PEEK, the recovery on release of the pressure differential may be slower and the resulting wipe weaker than in embodiments using a superelastic alloy; the purge gap and air purge nonetheless provide cleaning independently of the wipe." — supports CB3 while expressly avoiding an assertion that the PEEK embodiment wipes as effectively as the superelastic embodiment, consistent with footnote [a]. (Row 1)

7. "The dimensions and pressure thresholds given in the examples herein correspond to the superelastic seat ring embodiment; a person skilled in the art will adapt them to the stiffness and recovery characteristics of a polymer seat ring or of a separate wiper ring." — avoids asserting the N6 ranges apply unmodified to E-II/E-III, consistent with footnote [d]. (Row 4)


---

## From `15.md`

**Status: candidate.** This is a drafting and analysis aid prepared by AI. Nothing below is confirmed, tested or asserted as fact about the invention; it is a competitor/engineer stress-test of the nucleus and confirmed vocabulary. Every row is a candidate until Human Gate 2 confirms it is technically real and within what the inventor has conceived. Qualified patent counsel signs off before anything is filed.

**Sources.** `runs/r1/P1/01.md` (cited as 01), `runs/r1/P1/03.md` (cited as 03), `runs/r1/terminology/LOCKED.md` (locked terms used verbatim), `intake/data/bench-test.md` (cited as bench data). `runs/r1/P3/12.md` and `13.md` (equivalent architectures, parameter ladders) and `runs/r1/P2/09.md`/`10.md` (differentiation, white space) do not exist yet; this analysis proceeds without them, from the nucleus (03) and the disclosure (01) alone. Gate 1 answers (`intake/answers.md`) also do not exist yet, so every open question from 01 and 03 that this list touches is still open.

### Failure-Mode Embodiments

| ID | Failure mode / abuse case | Cause | Technical mitigation | Disclose as | Support |
|---|---|---|---|---|---|
| FM-1 | Purge gap region progressively fouls despite the cleaning actions: cured sealant film accumulates on the seat ring outer surface in the purge-gap region over many inflation events | The air purge and snap-back wipe act mainly at the sealing edge and across the purge flow path; sealant may re-deposit in the purge-gap region faster than it is cleared there, even while the sealing edge and poppet face stay clean | Enlarge the purge gap opening toward the higher end of the disclosed range (0.10–0.25 mm) to raise clearance and purge-flow velocity in that region; extend the disclosed electropolish (§7) to the adjoining core body bore surface to reduce adhesion where the film was found | Alternative embodiment (larger purge gap; treated bore surface) and dependent-claim fallback (purge gap size toward the upper end of §4's range) | Bench data (film found on the ring outer surface in the purge-gap region at cycle 40, sealing edge and poppet face clean); §4 range; §7 electropolish. Extension of electropolish to the core body bore is candidate – needs confirmation |
| FM-2 | Purge gap fails to open at all: cured sealant bridges the closed gap before over-travel is reached, resisting or blocking radial deflection | If the closed-gap region is not itself kept clear by either cleaning action, a hardened bridge could form there specifically, since it is closed (and therefore not purged) whenever the valve is not over-travelling | Not established in the disclosure; candidate only: the repeated snap-back wipe already occurring on every recovery (§2) may itself prevent hardening from setting in the closed gap, but this is not tested at cycle counts beyond 40 | Dependent-claim fallback reciting a purge-gap geometry or finish that resists sealant ingress at rest, once the inventor confirms whether this occurs | Candidate – needs confirmation; relates to 01 Q30 (long-term effect of the observed film) |
| FM-3 | Seat ring fatigue crack in the convoluted wall after cycling beyond the 40 cycles tested, causing loss of sealing or a ring fragment entering the sealant/tube | Repeated radial flexing concentrates strain at the convolution root; §9 names fatigue life as an unresolved question and the bench data confirms no fatigue testing was done | Not disclosed; candidate: a fillet radius at the convolution root, or distributing strain across two convolutions rather than one (§3(3) leaves the count unstated) | Dependent-claim fallback (convolution root geometry; convolution count) once the inventor supplies a mechanism; flag actual fatigue life as an open question rather than asserting a mitigation works | §9 item 1 (fatigue life open); bench data (no fatigue testing); §3(3) (count unstated, 01 Q11). Mitigation is candidate – needs confirmation |
| FM-4 | Seat ring chilled below its martensite start temperature by CO2 inflation while over-travelled, so it does not fully recover shape (superelastic recovery lost) | §9 item 2 raises CO2 cold-shock as untested; adiabatic expansion from a CO2 cartridge can cool the valve significantly | Not disclosed; candidate only: specifying an Af/Ms margin below the coldest expected CO2-inflation temperature (no such data exists in the dossier) | Dependent-claim fallback (Af with a stated cold-inflation margin) once the inventor supplies the transformation temperatures; not an embodiment without that data | §9 item 2; §4 (Af "below 5 °C", no lower bound). Mitigation is candidate – needs confirmation (relates to 01 Q13, Q28) |
| FM-5 | Ring loses shape recovery from ordinary cold-climate storage or riding, by the same mechanism as FM-4 but without CO2 | §4 gives only an upper bound on Af ("below 5 °C"); no As, Ms or Mf value is given, so the margin against ordinary cold weather is unknown | Same candidate mitigation as FM-4 | Same as FM-4 | §4; candidate – needs confirmation (01 Q13) |
| FM-6 | Seat ring loosens, rotates or migrates axially in the core body bore after repeated thermal cycling or vibration, drifting the purge-gap geometry or, in the worst case, coming free into the sealant/tube | Retention relies solely on an interference fit of about 0.03 mm (§7) with no process range or supplementary retention given (01 Q15, Q16) | Not disclosed; candidate: a supplementary ring retention feature in addition to the interference fit — for example adhesive bonding, a crimped lip on the core body, or a snap-fit groove | Dependent-claim fallback (interference fit is one species of a broader ring retention genus) and alternative embodiment for the supplementary feature | §7 (interference fit only); 01 Q17 (already raises alternative retention methods). Mitigation is candidate – needs confirmation |
| FM-7 | Interference fit manufactured at the tight end of an unstated tolerance over-constrains the ring, suppressing radial deflection (reduced or absent purge gap opening), or cracks the ring during press-fit assembly | No tolerance band is given for the ~0.03 mm interference (01 Q15) | Not disclosed; candidate: a specified interference tolerance band and an assembly force/travel check | Dependent-claim fallback specifying an interference range, once supplied; not worth disclosing as an embodiment without the range | §7; candidate – needs confirmation (01 Q15, Q17) |
| FM-8 | Sealing-edge wear or galling from repeated metal-to-metal contact between the brass sealing face and the seat ring sealing edge over the product's service life, degrading the at-rest seal independent of sealant fouling | At-rest sealing is direct metal-to-metal contact with no elastomer (§3(4)); the commercial target is "several thousand" cycles (§9) against only 40 tested | A hard-anodised aluminium sealing face (already disclosed, §5, Alternative F2) or a wear-resistant finish on the poppet sealing face | Alternative embodiment (F2 already in the dossier; confirm whether it was built, per 01 Q19) and dependent-claim fallback (wear-resistant sealing-face material) | §5 (Alternative F2, not confirmed tested per 01 Q19); §9 (cycle target) |
| FM-9 | Over-pressurisation beyond the believed over-travel threshold range (for example rapid inflation from a shop compressor) strains the seat ring beyond its superelastic limit if nothing else limits poppet travel | 01 Q36 and 03 note that what limits over-travel — a mechanical stop, spring coil-bind, or the ring itself — is not stated | A positive over-travel stop (a stop shoulder in the core body bore, or designed coil-bind of the second spring stage) limiting poppet travel independently of the seat ring | Alternative embodiment (structural over-travel stop) and dependent-claim fallback | Candidate – needs confirmation; directly answers the unresolved 01 Q36 / 03 (what limits over-travel) |
| FM-10 | Rapid, repeated pump-head engagement and disengagement drives many over-travel cycles in a short period, a duty cycle not represented by the tested protocol | The bench test ran one inflation event per 24-hour hold (§8); higher-frequency actuation is not addressed | None disclosed beyond the ring's inherent design | Not worth disclosing as a structural embodiment; dependent-claim fallback limiting claimed cycle life to what was tested (40 cycles), if broader endurance claims are challenged | §8 (protocol); candidate |
| FM-11 | Cross-threading or over-torquing the valve core into the stem bore during installation or removal distorts the core body bore, shifting the interference fit or the purge-gap geometry | No installation torque specification is given; metal-on-metal threading into the valve stem is common practice but easy to over-tighten | Not disclosed; candidate: a torque-limiting feature such as a shoulder that bottoms out at a defined torque | Not worth disclosing without inventor confirmation; raise as an open question rather than an embodiment | Candidate – needs confirmation; no support in the dossier |
| FM-12 | A valve cap or accessory with an internal pin holds the poppet in a partially or fully over-travelled state during storage or transport, subjecting the ring to sustained (non-transient) deflection | Not addressed by the disclosure; ordinary caps can contact the poppet tip | The lock nut (70), already disclosed for storage and transport (§3(7)), holds the poppet fully closed rather than over-travelled | Alternative embodiment note (recommended use of the existing lock nut for storage); not worth a separate dependent claim | §3(7) (lock nut function) |
| FM-13 | A higher-viscosity or particulate-laden sealant, or a non-latex formulation with abrasive fillers, abrades the sealing edge or lodges in the purge gap and prevents full closure | Only one unnamed latex sealant was tested (01 Q23); §9 raises ammonia-free sealants as untested and does not address particulate size at all | Not disclosed; no dimensional adjustment is asserted without data | Not worth disclosing as an embodiment; raise as an open question for Gate 2 | §9; candidate – needs confirmation |
| FM-14 | Manufacturing variability in shape-setting temperature, time or quench rate shifts a production unit's austenite finish temperature (Af) above the "below 5 °C" specification, so that unit is not superelastic at ordinary riding temperatures | §7 gives only the prototype's single process point (500 °C, 10 min, water quench); no process window or tolerance is given (01 Q32) | Not disclosed; candidate: a specified process window validated to hold Af below a target, with sampled or full Af verification during manufacture | Dependent-claim fallback (Af tolerance/verification) once a process window is supplied; not a structural embodiment | §7; candidate – needs confirmation (01 Q32) |
| FM-15 | Manufacturing variability in the convolution profile (laser-cut kerf width, mandrel-forming inconsistency) produces convolution amplitude outside the believed 0.08–0.20 mm range, so units purge at the wrong pressure or open the wrong gap size | 01 Q11 notes the process step that actually forms the convolution (laser cut, mandrel, or shape-set fixture) is ambiguous in §7 | Not disclosed; candidate: a tighter manufacturing tolerance on convolution amplitude, or a post-forming dimensional check before shape-setting | Dependent-claim fallback (narrower convolution-amplitude tolerance); not an alternative embodiment | §4 (range); §7 (ambiguous process); candidate |
| FM-16 | Second spring stage manufacturing variability shifts the over-travel threshold outside the believed 2.5–5.0 bar range, so some units purge too early (reduced normal-stroke range) or too late (some pumps never reach the threshold, per 01 Q5) | No manufacturing tolerance is given for the return spring's second stage (01 Q7) | Not disclosed; candidate: spring-rate sorting or verification during assembly | Dependent-claim fallback narrowing the over-travel threshold range; not an embodiment without further data | §4; candidate – needs confirmation |
| FM-17 | Electropolishing removes more material than intended, locally thinning the convoluted wall — especially at the convolution root — below the believed 0.15–0.30 mm range, lowering fatigue margin exactly where FM-3 concentrates strain | §7 states electropolishing removes oxide and the heat-affected edge but gives no depth, time or tolerance (01 Q32) | Not disclosed; candidate: a specified electropolish depth/time window verified by post-process wall-thickness sampling | Dependent-claim fallback (wall thickness within §4's range, measured post-electropolish); not an embodiment | §7; §4 (range); candidate |
| FM-18 | Stress-corrosion attack on brass components (core body, poppet) from prolonged exposure to ammonia-bearing sealant | Brass alloys are generally known to be susceptible to stress-corrosion (season) cracking in ammoniacal environments — background engineering knowledge, not an inventor-supplied fact. The disclosure itself is consistent with this concern: Alternative F1 (stainless 303 core body) is offered "for corrosion resistance with ammonia-bearing sealant" (§5), and the sealant contains ammonia (§1) | The stainless 303 core body, already disclosed as Alternative F1 (§5) | Alternative embodiment (F1 is already in the dossier); also a dependent-claim fallback (stainless core body material). Recommend confirming whether F1 was ever built into a working, tested core (01 Q18) | §5 (F1); §1 (ammonia sealant). The stress-corrosion mechanism itself is general materials-science background, not from the dossier, and is flagged as such — not asserted to occur in this product without inventor confirmation |
| FM-19 | First inflation after long-term flat storage meets a harder-than-normal sealant plug near the valve, needing more force to open than a routine ride-to-ride inflation | §1 describes capillary ingress and drying generally; only 24-hour hold cycles were tested (§8), not extended flat storage | None disclosed beyond the air purge and snap-back wipe already claimed for routine fouling; not tested at this extreme | Not worth a separate embodiment; a description-level note on the operating condition, and an open question for Gate 2 on whether long-term flat storage was ever tested | §1; §8 (only 24 h holds tested); candidate |
| FM-20 | A user inserts a sharp tool into the valve core bore out of habit from servicing conventional cores, scratching, denting or puncturing the thin convoluted wall | The invention's purpose is removing tool-based servicing (§1, §2), but a user unaware of that, or troubleshooting something else, might still probe the core | None structural; a description-level caution against tool insertion is not a technical mitigation | Not worth disclosing as an embodiment or claim; at most a cautionary note in the description | §2 (thin wall, §4: 0.15–0.30 mm); not a claim-worthy mitigation |
| FM-21 | The poppet itself sticks in its fit within the core body from sealant that migrated along the poppet by capillary action, independent of the seat-ring cleaning mechanism | §1 states sealant is drawn in "by the pressure surge and by capillary action along the poppet stem"; the disclosed air purge and snap-back wipe act at the seat ring and purge gap, and no cleaning action along the poppet's fit within the core body is described | Not disclosed; candidate: extending a wiping or clearance feature to the poppet's fit within the core body, or additional running clearance there | Not worth disclosing as an embodiment without inventor input; raise as an open question, since this could be a gap in the invention's coverage of the very problem §1 describes | §1 (capillary ingress along the poppet); candidate – needs confirmation |
| FM-22 | If the closed purge gap is not itself airtight, it becomes a route for pressure loss distinct from the sealing edge, in any embodiment where sealing does not depend solely on the sealing edge | 01 Q31 and 03 Q11 leave open whether the closed purge gap must itself be airtight, or whether sealing depends solely on the sealing edge | None needed under the working assumption (03 A5, this analysis) that the sealing edge is the sole seal and the closed purge gap is a secondary flow path only when open; recommend the specification state this explicitly | Not an embodiment; a drafting/disclosure note to avoid an enablement gap | Candidate – needs confirmation (01 Q31, 03 Q11) |
```

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/debate/d2-attack.md`

```markdown
# Debate 2 — Competitor attack on the confirmed embodiments (D2a)

**Status: attack, one-way.** Prepared by the Litigator as a well-funded competitor's engineering and litigation team. It is a drafting and analysis aid prepared by AI, not legal advice; qualified patent counsel signs off before anything is filed.

**Inputs.** `CONFIRMED.md` only (the confirmed content of 11–15). `P2/09.md` does not exist, so no prior-art reference is cited and nothing below is a novelty attack. No web research was performed inside the time budget; every route rests on the confirmed package and on common general knowledge, which is named as such where used. Locked terms are used verbatim.

**Two facts shape every route below.**

1. Gate 2 was confirmed by the orchestrator unattended. None of the inventor questions Q1–Q25 of `11` or the "not conceived — Qn" markers of `12` has an answer. So the "confirmed" set is, for a competitor, a list of what the inventor has *not* yet said they conceived. A competitor reads that list as the safe ground.
2. The purge gap's location and the direction of deflection are still contradictory in the inventor's own material (§2 "flexes radially outward" against §3(6) "clearance between the seat ring outer surface and the core body bore" with an interference fit at §7; 01 Q1, Q2; 12 §7). That contradiction is the cheapest attack of all, because it costs the competitor nothing: it builds the prototype and litigates the words.

Core embodiments attacked: **E-I** superelastic seat ring, **E-II** PEEK seat ring, **E-III** fixed seat and wiper ring (14), and the shared nucleus N0 (over-travel, purge shoulder, deflectable ring element, purge gap, air purge, shape recovery).

---

## 1. Routes that escape all three embodiments (the nucleus)

### R1 — Copy the prototype, litigate the gap (E-I, E-II, E-III)

- **What we build.** The prototype of §3–§7 exactly: NiTi seat ring, interference fit, two-rate spring.
- **What it avoids.** Whichever construction of "purge gap" and "radial deflection" the claim adopts. If the claim says the gap opens between the seat ring outer surface and the core body bore, we say the ring flexes outward (§2), so that surface presses harder on the bore and the gap in our product forms at the inner surface or an end face. If the claim says outward deflection, we say the clearance at §3(6) can only open by inward movement (12 E7.1), so the claimed gap never forms. Either way the description contradicts itself, which is an insufficiency and clarity attack on the nucleus under all three jurisdictions.
- **Why it works commercially.** Zero engineering cost and the strongest invalidity position in the file. The patentee cannot prove where the gap forms without sectioning a live, over-travelled valve.
- **Close it by.** Resolving 01 Q1/Q2 with the inventor before drafting, then defining the purge gap by function only (a passage bounded at least in part by a surface of the deflectable ring element, closed in the closed state and in the normal-open state, opened by the deflection, whichever direction), with outward, inward, tilting and end-face species each described (12 §6, §7). Claims must not recite the surface pair or the direction in the independent claim. **Requires the inventor's answer; not closable by drafting alone.**

### R2 — Purge through a port, nothing deflects (E-I, E-II, E-III)

- **What we build.** A brass poppet whose over-travel uncovers a radial port or a spool land in the core body bore, directing supply-side gas across the sealing edge into the inflatable chamber (11 DA-7; 12 E8.2 without a ring). A single-rate spring or a two-rate spring, as we choose.
- **What it avoids.** Deflectable ring element, radial deflection, shape recovery, snap-back wipe: N0(c)–(e) in every embodiment.
- **Why it works commercially.** Turned brass only, made by the existing valve-core supply base, no NiTi, no laser cutting, no shape-setting, no press fit. It is the cheapest plausible product that can be marketed as a "self-purging" valve core. Whether directed air alone clears cured film is untested (01 Q24) but a competitor only needs a marketing claim, not the inventor's 40-cycle result.
- **Close it by.** Nothing in the package. `11` records DA-7 as "cannot be closed without new matter". Only the inventor can say whether a purge flow path opened by over-travel *without* a deflecting element was within their conception. **Inventor question; do not write it in.**

### R3 — Fixed wiping land plus ordinary flow (E-I, E-II, E-III)

- **What we build.** A close-clearance land in the core body or on a fixed seat through which the poppet passes on every stroke, shearing film (12 E10.3, now confirmed as candidate; 11 DA-23). No recovering element.
- **What it avoids.** Shape recovery and the snap-back wipe (N0(e), N1), and, if paired with R2, the whole ring.
- **Why it works commercially.** Scraper lands on reciprocating parts are common general knowledge (A1). One extra turned diameter.
- **Close it by.** E10.3 is now in the confirmed set, so the drafters may describe a fixed wiping land as an *additional* species of mechanical wipe. That does not close R3 as a stand-alone product, and the drafters must not write a rigid-land-only embodiment as the invention: the inventor's concept is recovery of a deflected element. **Partly closable (as an add-on); the stand-alone escape is an inventor question (11 Q23).**

### R4 — Purge on every opening; threshold by the ring, not a spring (E-I, E-II, E-III)

- **What we build.** A single-rate return spring. The poppet's deflecting surface reaches the ring at or just past the crack pressure (11 DA-1), or the ring's own stiffness provides the step (12 E2.3).
- **What it avoids.** The threshold-setting arrangement, the second spring stage, "over-travel beyond the normal stroke", and "only when the pressure differential exceeds the over-travel threshold" (N0(b), N5, C2–C4, C17).
- **Why it works commercially.** One spring, no tuning, no lost-motion clearance. And it is **undetectable by teardown**: whether our product has a distinct threshold is a bench measurement of force against stroke, and a claim that recites a threshold above the crack pressure is one the patentee must prove on our part with a test rig, at their cost, under a protective order.
- **Close it by.** Describing an embodiment in which the over-travel threshold equals or barely exceeds the crack pressure and the purge state is reached on every opening (11 DA-1 genus), and defining the purge state by deflection of the deflectable ring element, not by a second threshold. A dependent rung keeps the two-stage spring. **Closable in P4/P5 only if the inventor confirms that purging on every opening works (11 Q1); the 40-cycle data does not cover it.**

### R5 — The pump head does the over-travel (E-I, E-II, E-III)

- **What we build.** A valve core with a single-rate spring and no threshold, sold together with, or separately from, an inflation head whose depressor pushes the poppet into over-travel on coupling (12 E1.4; 11 DA-9). For Presta-pattern valves a matching head is needed; for Schrader-pattern cores depressor heads already exist (common general knowledge, A2).
- **What it avoids.** Over-travel "caused by the pressure differential" (C2, C18) and the threshold-setting arrangement.
- **Why it works commercially.** A pump maker sells the head and a valve maker sells the core. No single party makes, sells or uses a valve in which the pressure differential causes over-travel. Any claim that needs both the core geometry and the pressure-driven behaviour is split across two suppliers and a rider. That is the divided-infringement escape, and the pump makers are the ones with the distribution.
- **Close it by.** A genus "over-travel produced by the pressure differential or by mechanical actuation of the poppet" (12 E1.4 genus), an apparatus claim on the valve core that does not recite what causes over-travel, and a separate claim on the core in combination with an inflation head. **Closable by drafting if the inventor confirms mechanical actuation was within the conception (11 Q9); E1.5 conflicts with §2's "no rider action" and the inventor must decide.**

### R6 — Move the mechanism into the stem (E-I, E-II, E-III)

- **What we build.** An integrated tubeless valve with the ring, poppet and spring carried directly in the valve stem, no removable core body (12 E16.3, E14.6; 11 DA-6). Or a Schrader-pattern core (E16.2).
- **What it avoids.** "Valve core", "core body threaded into the stem bore", "seat ring carried by the core body" (C26, C29), and the interference fit against an internal shoulder of the core body.
- **Why it works commercially.** This is the OEM channel (02 rank 3): wheel and rim makers specify the stem, not the core, and an integrated stem is a higher-margin part than a multipack core. It also takes the aftermarket by making the retrofit core irrelevant on new wheels.
- **Close it by.** Describing the mechanism in "an inflation valve" with the deflectable ring element carried by "a valve body, which may be a removable core body or the valve stem", and an independent claim to the inflation valve as well as to the core. Name Schrader-pattern and Dunlop-pattern as alternatives. **Closable by drafting, but only as far as the inventor conceived other formats (11 Q6).**

### R7 — Seal the periphery: wipe only, no air purge (E-I, E-II, E-III)

- **What we build.** The same ring, but its outer surface is bonded or crimped so no gas passes it; over-travel and recovery give only the wipe (11 DA-10).
- **What it avoids.** "Inflation gas flows through the purge gap into the inflatable chamber" (N0(d), C6, C7).
- **Why it works commercially.** Same parts as the prototype. And again undetectable without a flow test: the patentee cannot prove that gas passes our ring from a section.
- **Close it by.** Describing the cleaning action as "the air purge, the snap-back wipe, or both", with a wipe-only embodiment, and an independent claim that recites deflection and recovery without flow. **Closable if the inventor confirms the wipe alone is enough (11 Q10; 03 Q1); the bench test does not separate the two actions.**

---

## 2. Routes aimed at E-I (superelastic seat ring)

### R8 — Stainless slotted collet, no superelastic alloy

- **What we build.** A short tube of 17-7PH or cold-worked 301 stainless with axial slots forming fingers behind a continuous sealing band (12 E4.3 with E12.4), photo-etched from strip and rolled, or laser-cut from tube (E15.6).
- **What it avoids.** Superelastic alloy, nickel content, austenite finish temperature (N4, C14–C16), the convoluted wall (N3), "annular" purge gap (gas passes the slots, E8.4), electropolishing and shape-setting (C24, C25).
- **Why it works commercially.** Spring stainless strip is a commodity; NiTi tube at 2.7 mm outer diameter is a specialist purchase. Recoverable strain is an order of magnitude lower (12 E12.4), so the geometry must be redesigned, but the confirmed library itself says that is credible.
- **Close it by.** "Resilient metal, superelastic or not" as the genus, with NiTi preferred; the deflectable ring element "continuous, slotted or segmented"; the purge opening genus "an annular gap, one or more slits or apertures through the wall, or gaps between fingers" (11 DA-3, DA-14). **Closable by drafting subject to 11 Q3, Q14.**

### R9 — Tapered poppet and a plain ring

- **What we build.** A frustoconical flank on the poppet enters a straight-walled ring during over-travel and expands it like a mandrel (12 E3.2 with E5.5; 11 DA-4, DA-12).
- **What it avoids.** The convoluted wall (N3, C12); the purge shoulder as a distinct annular surface on the chamber side of the sealing face (C4); the axial-to-radial conversion.
- **Why it works commercially.** One fewer forming operation on the ring and one fewer turned feature on the poppet. The library rates it "high" credibility.
- **Close it by.** Defining the purge shoulder as "a deflecting formation of the poppet that contacts the deflectable ring element during over-travel, which may be a separate shoulder, the sealing face or a continuation of it, a taper on the stem, a collar or lugs" (12 §3), and the wall as "an axial-to-radial conversion geometry" with the convoluted wall as the preferred species. **Closable by drafting subject to 11 Q4, Q12.**

### R10 — Integral moulded lip

- **What we build.** An injection-moulded PEEK or PPS core body with an integral thin flexure section that seals on the poppet and deflects in over-travel (12 E4.5; 11 DA-5). No separate ring, no interference fit.
- **What it avoids.** "Seat ring carried by the core body", the separate part, the interference fit against an internal shoulder (C5, C23, C26).
- **Why it works commercially.** One moulding replaces ring manufacture, shape-setting, electropolishing and press-fitting. This is the route a volume manufacturer takes for a budget line, and the library rates it credible for PEEK and spring stainless.
- **Close it by.** "The deflectable ring element may be separate from, or integral with, the body that carries it", with a polymer body described. **Closable by drafting subject to 11 Q5.**

### R11 — Step outside the ranges

- **What we build.** Threshold at 2.3 bar or 5.3 bar; wall 0.13 mm or 0.33 mm; over-travel 0.35 mm or 1.0 mm.
- **What it avoids.** Every N6 rung (C19–C21). The ranges are "believed", not evidenced (§4), and nothing in the mechanism fixes the endpoints (11 DA-16; 13 Table 1).
- **Why it works commercially.** Tuning only. It matters because, if the independent claim survives only with a range, the whole patent is avoided by a tolerance.
- **Close it by.** Never carrying a numeric range into the independent claim; leading with the relationships (over-travel threshold above the crack pressure and within what the inflation device reaches; purge gap closed at rest). **Closable in P5; no new matter.**

### R12 — Other threshold-setting arrangements

- **What we build.** Two springs with lost motion, a disc-spring stack, a detent, or a polymer bush (12 E2.2–E2.6).
- **What it avoids.** "Two-stage return spring" and "second spring stage" (N5, C17).
- **Why it works commercially.** Any competitor tuning its own threshold picks one of these; all are standard spring practice.
- **Close it by.** "Threshold-setting arrangement" as the genus with the species listed. **Closable by drafting subject to 11 Q11.**

---

## 3. Routes aimed at E-II (PEEK seat ring)

### R13 — A polymer that is not PEEK, moulded

- **What we build.** A PPS, PEI or glass-filled polyamide ring, micro-moulded (12 E12.5, E15.4).
- **What it avoids.** Any claim or species naming PEEK; every Af limitation, because a polymer has no austenite finish temperature (14 footnote [g]); electropolishing (14 [e]).
- **Why it works commercially.** Same tooling logic as R10. The lowest-cost line in the file.
- **Close it by.** "Resilient polymer" genus with PEEK as the disclosed species; the Af limitation conditioned expressly on the superelastic species (14 sentence 2). **Closable by drafting subject to 11 Q13; PPS and PEI are not conceived.**

### R14 — Sell PEEK and deny the wipe

- **What we build.** The inventor's own Alternative A.
- **What it avoids.** Any claim reciting the snap-back wipe. §6 says the PEEK ring's "recovery is slower and snap-back force lower, so the wipe is weaker". We say our ring does not "snap back" at all; there is no disclosed lower bound on wipe force or speed (14 [a]), so the term is indefinite against us and, in any event, not met.
- **Why it works commercially.** No design cost. The patentee's own text supplies the argument.
- **Close it by.** Keeping the wipe out of the independent claim; where a wipe is claimed, defining it as "movement of the recovering ring element across a surface of the poppet" without a speed or force qualifier, and describing the polymer wipe expressly as within that definition (14 sentence 6). **Closable in P4/P5; no new matter.**

### R15 — High-hardness thermoplastic elastomer

- **What we build.** A TPE ring, 90 Shore A or harder (11 DA-15).
- **What it avoids.** N4 and any definition of the ring element by fast, stiff recovery. Then we turn §2 against the patentee: §2 says latex embeds itself in rubber, so the patentee has told the world a rubber-like ring is *not* the invention. Prosecution-history and specification disclaimer arguments follow in all three jurisdictions.
- **Why it works commercially.** The cheapest material there is.
- **Close it by.** Writing §2's criticism as a criticism of *soft* seats that deform under the sealing face, not of elastomers as a class, and presenting superelastic recovery as preferred rather than as the definition of the deflectable ring element. An elastomer embodiment itself cannot be added without the inventor (11 Q15). **Drafting point closable in P4; the embodiment is an inventor question.**

---

## 4. Routes aimed at E-III (fixed seat and wiper ring)

### R16 — Split-ring or poppet-carried wiper

- **What we build.** Behind a conventional fixed seat, a stainless split ring opened by a tapered flank (12 E4.6), or a thin skirt on the poppet that a fixed formation in the body deflects and that wipes the bore on recovery (11 DA-8).
- **What it avoids.** A continuous "annular" ring; a ring "carried by the core body"; a purge shoulder "on the poppet" (C4, C5). The split ring's gap is the purge opening.
- **Why it works commercially.** The fixed seat is the conventional core. The wiper is a stamped part. And here the litigator's point: a wiper or scraper ring behind a seat on a reciprocating part is common general knowledge (A1), so any claim to E-III whose only contribution over a conventional core is "a resilient wiper ring deflected by the poppet" will meet an inventive-step attack, whichever direction the ring moves. E-III is the weakest embodiment to claim on its own.
- **Close it by.** "The deflecting formation and the deflectable ring element are each carried by one of the poppet and the body, the counterpart by the other" (11 DA-8 genus), the ring "continuous, split or segmented", and E-III claimed only with what distinguishes it (the purge gap that opens *only* in over-travel and closes at rest; the two-stage return). **Closable by drafting subject to 11 Q8, Q17; the inventive-step exposure is for P5 to weigh.**

### R17 — E-III without a purge flow

- **What we build.** A wiper ring that scrapes but never opens a gas path (R7 applied to E-III).
- **What it avoids.** Everything in E-III beyond a scraper. Combined with R16 this is a conventional core plus a scraper.
- **Close it by.** As R7. The drafters should recognise that if E-III is claimed without the air purge, it is a scraper and will be read as one.

---

## 5. Business-model escapes (against CB1–CB5)

### R18 — Kit and component sale

- **What we build.** The ring alone, or ring plus poppet and spring, sold to be fitted into a core body of the buyer's choosing (11 DA-19). Also the core sold without the two-stage spring, the threshold being "user-selectable" by a separately sold spring.
- **What it avoids.** Any claim to the assembled valve core (02 rank 1) and to the assembled combination of ring and spring.
- **Why it works commercially.** Conventional cores are not designed to come apart (11 rates plausibility low–medium), but a competitor can design a two-part core body for exactly this purpose, and a component sale in one jurisdiction for assembly in another puts direct infringement in nobody's hands.
- **Close it by.** Component claims to the deflectable ring element as such (defined by its geometry and by its function when fitted), to the poppet as such, and to the kit. **Closable in P5 if the inventor confirms the component form (11 Q19).**

### R19 — Retrofit core sold "for tubes only"

- **What we build.** The exact core, labelled for inner-tube use with no sealant.
- **What it avoids.** Any claim that recites liquid sealant, an inflatable chamber "containing sealant", a tubeless tyre, or the purpose of removing sealant film. Riders will use it with sealant anyway; the seller has not.
- **Close it by.** Apparatus claims reciting no sealant, no tubeless tyre and no purpose; sealant only in dependent claims and in use claims. **Closable in P5; no new matter.**

---

## 6. Ranking

| Route | Embodiments escaped | Technical credibility | Commercial pull | Detectable by teardown? | Closable without new matter? | Target |
|---|---|---|---|---|---|---|
| R1 gap contradiction | all | certain (it is the prototype) | highest: costs nothing, wins twice | irrelevant | **No: inventor must resolve 01 Q1/Q2** | inventor, then P4, P5 |
| R2 port purge | all | medium | high | yes | **No (11 Q7)** | inventor |
| R4 purge every opening | all | medium | high | **no: bench test** | only if 11 Q1 confirmed | P4, P5 |
| R5 head does over-travel | all | high | high (pump makers; divided infringement) | **no** | if 11 Q9 confirmed | P4, P5 |
| R6 into the stem | all | high | high (OEM channel) | yes | if 11 Q6 confirmed | P4, P5 |
| R10 integral lip | E-I, E-II | medium–high | high (volume cost-down) | yes | if 11 Q5 confirmed | P4, P5 |
| R8 stainless collet | E-I | medium–high | high | yes | if 11 Q3, Q14 confirmed | P4, P5 |
| R9 taper and plain ring | E-I | high | high | yes | if 11 Q4, Q12 confirmed | P4, P5 |
| R13 non-PEEK polymer | E-II | moderate | high | yes | if 11 Q13 confirmed | P4, P5 |
| R7 wipe only | all | medium | medium | **no: flow test** | if 11 Q10 confirmed | P4, P5 |
| R14 deny the wipe | E-II | certain | medium | **no** | yes | P5 |
| R11 outside the ranges | E-I | high | medium | yes, by measurement | yes | P5 |
| R16 split or poppet wiper | E-III | high | medium | yes | if 11 Q8, Q17 confirmed | P4, P5 |
| R12 other threshold | E-I, E-II | high | medium | yes | if 11 Q11 confirmed | P4, P5 |
| R3 fixed land | all | medium | medium | yes | add-on only; stand-alone is 11 Q23 | inventor |
| R15 elastomer | E-II | low–medium | high | yes | drafting point yes; embodiment no | P4 |
| R18 kit sale | all | low–medium | medium | yes | if 11 Q19 confirmed | P5 |
| R19 "tubes only" label | all | certain | medium | n/a | yes | P5 |
| R17 E-III scraper | E-III | high | medium | no | as R7 | P5 |

---

## 7. What the drafters must do

1. **Get 01 Q1/Q2 answered before a word of the Description is written.** R1 is a fatal attack on the nucleus and no genus wording hides a contradiction; the examiner and the opponent will both find it.
2. **Claim the nucleus as function, not as the prototype.** Purge gap: a passage bounded in part by the deflectable ring element, closed at rest and in the normal-open state, opened by its deflection. Purge shoulder: a deflecting formation of the poppet. Threshold: a threshold-setting arrangement, which may be the ring itself. Deflectable ring element: separate or integral, continuous, slotted or segmented, resilient metal or resilient polymer. Body: removable core body or valve stem. Over-travel: by pressure differential or mechanical actuation.
3. **Put behaviour into claims that can be proven.** R4, R5, R7 and R14 win because a section of the product proves nothing about thresholds, flows or wipes. Provide structural rungs that are visible in a teardown (a second spring stage; a lost-motion clearance; a ring free of the bore over a band on the chamber side of the sealing edge; through-wall openings) alongside the functional independent claim, and use claims (inflating a tubeless tyre with the valve) for the behaviour.
4. **Keep numbers, materials, PEEK, Af, sealant and tubeless out of the independent claims** (R11, R13, R19).
5. **Do not let §2 become a disclaimer** (R15) and do not let §6's "weaker wipe" become an admission (R14).
6. **Record R2, R3 (stand-alone) and R1 as inventor questions**, not as drafted embodiments. Everything marked "not conceived — Qn" in `12` has been confirmed by code, not by the inventor; if the drafters write those entries as the inventor's own embodiments without an answer, the competitor's next attack is added matter and lack of possession, and it will be a good one.

## Assumptions

- **A1.** Common general knowledge: scraper or wiper rings on reciprocating rods and pistons, and close-clearance wiping lands, are known mechanical elements. No reference is cited.
- **A2.** Common general knowledge: inflation heads for Schrader-pattern valves carry a fixed pin that depresses the core pin on coupling. No reference is cited.
- **A3.** All confirmation questions of `11` and `12` are treated as unanswered, because `CONFIRMED.md` was confirmed unattended.
- **A4.** No prior-art reference exists in the run at the time of writing; nothing here is a novelty attack.
```

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
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/registry.json`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/21.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/risk/pre-drafting-findings.md`

## Files to write

Write each of these with your Write tool, at exactly this path, one file per call (the folders exist). Write nothing outside the run folder `{R}`. Do not run the checks yourself: the runner runs them and will tell you if anything fails.

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/21.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/22.md`

When every file is written, reply with one line per file (path and a few words on what it holds) and anything the runner must route: open questions, disclosure requests, open disagreements, narrowing suggested. Nothing else.
