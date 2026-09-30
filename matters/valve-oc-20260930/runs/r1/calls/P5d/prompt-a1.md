# Patent Council · matter `valve-oc-20260930` · run `r1` · step `P5d` · profile full

You are the **Claims Architect**. Follow your AGENTS.md. This message is the whole brief: what to do, the prompts to execute, every input (embedded below, so do not re-read those files), and the exact files to write.

## What to do

Run Prompt 25 against the stitched description (embedded). Write the Final Claim Set, plain numbered claims only, to `claims.md`, and `support-map.json` as `{"claims": {"1": [{"element": "<exact claim words>", "paragraphs": ["[0012]"]}]}}` for every element of every claim. A limitation you cannot map to a paragraph is re-worded to what the text supports, or listed in `P5/unsupported.md` (one line each) for the fix pass. Keep the family broad and deep: independent claims in every justified category, full dependent ladders.

**Time budget:** about 12 minutes. The whole matter is planned to finish end to end in two hours. Be complete, but write each deliverable once: no drafts, no repetition, no padding.

## Prompt 25 — Claim differentiation and dependency audit  (kind `drafting`)

**Write your reply to:** `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/25.md`

*Remove redundancy and dependency errors.*

Audit the full claim set for antecedent basis, dependency, internal consistency, duplicate scope, accidental exclusion, unnecessary limitations, unclear relative terms, unsupported terminology, mixed statutory categories and contradictions. Recommend a clean dependency tree.

**How to work.** The description in front of you is the only source of support. Any limitation that lacks an explicit passage in the description must NOT be drafted: leave it out, and record it in `disclosure_requests` (limitation, and the disclosure ip-spec would need to add) so the inner loop can supply the support. Use locked preferred terms verbatim and the registry's component names; where a claim term needs a reference sign, use the registry numeral. Cite the supporting paragraph for every limitation in `support_refs`. The runner extracts the `### Final Claim Set` section of this reply verbatim into `claims.md`, which is what the independent reviewer and, eventually, counsel will read. So: under `### Audit` give the findings as a table (claim | issue type | problem | fix applied) and the clean dependency tree; under `### Final Claim Set` write the complete, corrected claim set as numbered claims in plain text - `1. A ...`, `2. The ... of claim 1, wherein ...` - one claim per paragraph, no tables, no commentary, no bold, no notes between claims, nothing in that section that is not claim text. Claims from `22`, `23` and the formulations selected in `24` are merged here; a limitation that the audit finds unsupported is removed and recorded in `disclosure_requests`, never left in. Reply exactly in the drafting output contract: `## Deliverable` (with the H3 sections named above), `## Rationale`, `## Assumptions`, `## Open Questions`, then one final fenced `json` envelope. No preamble before `## Deliverable`; nothing after the envelope. Reuse locked preferred terms verbatim; declare any other term in `new_terms` with a reason.

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

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/description.md`

```markdown
#### Definitions and conventions

[0001] The definitions and conventions in this section apply throughout the specification and the claims. Where a defined term is also described with reference to an illustrated embodiment, the illustrated embodiment is one example of the defined term and does not limit it. The reference numerals used in this specification are those of the drawings, and the same numeral denotes the same component in every figure in which it appears.

#### General construction

[0002] As used herein, "comprising" and "comprises" are open transitional terms. A valve core, a seat ring, or any other element or combination that "comprises" a set of recited components or steps may include additional, unrecited components or steps, and is not limited to those recited.

[0003] Language such as "in some embodiments", "in other embodiments", "optionally" and "may" identifies a feature as preferred rather than essential to every embodiment described herein. The absence of such language for a given feature does not, by itself, make that feature essential; essentiality is determined from the description as a whole and, for a claimed combination, from the claim.

[0004] As used herein, "a" and "an" mean "one or more" unless the context clearly requires otherwise. For example, "a convolution" of the convoluted wall encompasses an embodiment having a single convolution and an embodiment having two or more convolutions, and "a purge shoulder" encompasses a purge shoulder that contacts the deflectable ring element at a single location or at two or more locations around its circumference.

[0005] Unless expressly qualified as "directly", terms describing the relationship between components, including "carried by", "coupled to", "on", "against" and "bears on", encompass both a direct connection or contact and an indirect connection or contact through one or more intervening components. For example, a purge shoulder "on the poppet" encompasses a purge shoulder integral with the poppet and a purge shoulder formed on a separate part fixed to the poppet.

[0006] Unless stated otherwise, a numerical range disclosed herein is inclusive of its stated endpoints, and disclosure of a range constitutes disclosure of every value and every narrower sub-range falling within it. Where a range is given herein for a parameter for which a single value is reported in the working examples, the range is the range within which the mechanism described is expected to operate, and values within the range other than the reported value are not represented as having been tested.

[0007] As used herein, "about" or "approximately", applied to a stated value, accounts for ordinary variation arising from manufacturing tolerance and measurement, consistent with the level of precision of the surrounding disclosure; it does not itself define a specific numerical tolerance unless one is separately stated. For example, "approximately 0.03 mm" describes the interference fit of the working example without asserting a measured tolerance band, and "nominally 55.8 wt%" describes the nickel content of the working example without asserting a measured compositional tolerance.

[0008] Where this specification describes a sequence of states or events, for example the closed state, the normal stroke, over-travel and the purge state, and shape recovery, that description identifies the pressure differential at which each state or event occurs and does not require that the states or events be discrete, mutually exclusive, or performed only in the order presented, except where the description or the context makes a particular order necessary; for example, over-travel necessarily follows completion of the normal stroke as the pressure differential rises.

[0009] Certain terms used herein combine a generic structural term with a statement of function, for example "deflectable ring element", "threshold-setting arrangement" (of which the second spring stage of the return spring is the species described in detail), "deflecting formation" (of which the purge shoulder is the species described in detail) and "biasing member" (of which the return spring is the species described in detail). Each such term refers to any structure capable of performing the recited function, consistent with the corresponding structures described in this specification and their equivalents; this specification describes at least one corresponding structure for each such term so used, and the term is not limited to the material, form or manner of retention of that structure.

#### Orientation and directions

[0010] As used herein, the "supply side" of the poppet means the side coupled to the inflation device, and the "chamber side" of the poppet means the side open to the inflatable chamber. These terms replace orientation-dependent words, because the orientation of the inflation valve changes as the wheel turns. "Axial" means along the axis of the poppet, referred to herein as the poppet axis, and "radial" means perpendicular to the poppet axis. "Outward" means away from the poppet axis and "inward" means towards it. Movement of the poppet from the closed state through the normal stroke and into over-travel is referred to as movement in the opening direction. The deflectable ring element is "at rest" when it is not deflected by the purge shoulder.

#### Pressure differential, crack pressure, over-travel threshold and poppet travel

[0011] As used herein, the "pressure differential" means the supply-side pressure less the chamber-side pressure across the poppet. The "crack pressure" means the pressure differential at which the poppet begins its normal stroke, overcoming the first spring stage of the return spring. The "over-travel threshold" means the pressure differential above which the poppet moves beyond the normal stroke into over-travel, overcoming the second spring stage of the return spring or other threshold-setting arrangement. The over-travel threshold is higher than the crack pressure. In the illustrated embodiment the over-travel threshold is selected so that it is exceeded during inflation of the inflatable chamber with a floor pump, as in the working example described below.

[0012] As used herein, the "normal stroke" means the displacement of the poppet from the closed state, at and above the crack pressure and below the over-travel threshold, over which the purge shoulder is spaced from the deflectable ring element. "Over-travel" means movement of the poppet beyond the normal stroke, occurring when the pressure differential exceeds the over-travel threshold, during which the purge shoulder bears on the deflectable ring element. The "over-travel distance" means the axial distance the poppet moves beyond the end of the normal stroke during over-travel.

#### Operating states

[0013] The valve core has a closed state, a normal-open state and a purge state, determined by the pressure differential. In the "closed state", which prevails when the pressure differential is below the crack pressure or when the lock nut is engaged, the sealing face of the poppet rests on the sealing edge, which is provided by the seat ring or, in embodiments having a fixed seat, by the fixed seat; the main passage is closed and the purge gap is closed. In the "normal-open state", which prevails when the pressure differential is at or above the crack pressure and does not exceed the over-travel threshold, the poppet is displaced from the closed state within the normal stroke, the sealing face is lifted from the sealing edge so that the main passage is open, the purge shoulder is spaced from the deflectable ring element, and the purge gap remains closed. In the "purge state", which prevails when the pressure differential exceeds the over-travel threshold, the poppet is in over-travel beyond the normal stroke, the purge shoulder bears on the deflectable ring element, the deflectable ring element is in radial deflection, the purge gap is open, and the air purge occurs while the main passage remains open. When the pressure differential falls below the over-travel threshold, the deflectable ring element undergoes "shape recovery", meaning its return towards its at-rest shape, the purge gap closes, and the valve core returns through the normal-open state to the closed state as the pressure differential falls below the crack pressure.

#### Deflectable ring element, seat ring, wiper ring, fixed seat and convoluted wall

[0014] As used herein, a "deflectable ring element" means any annular element, carried by the valve core, that the purge shoulder deflects radially during over-travel so as to open a purge flow path, and that undergoes shape recovery towards its at-rest form when the pressure differential falls. A deflectable ring element is a seat ring, where the same element also provides the sealing edge, or, in embodiments having a separate fixed seat, a wiper ring. The deflectable ring element is described below with reference to the seat ring of the illustrated embodiment; the term is not limited to the material, the wall form or the manner of retention of that seat ring.

[0015] As used herein, a "seat ring" means a deflectable ring element that both provides a sealing edge on which the sealing face of the poppet rests in the closed state, and is deflected by the purge shoulder during over-travel to open the purge gap. In the illustrated embodiment the seat ring is formed from a superelastic alloy and has a convoluted wall; in other embodiments it is formed from a resilient polymer. The "sealing edge" means the edge of the seat ring, or of the fixed seat, on which the sealing face rests in the closed state.

[0016] As used herein, a "wiper ring" means a deflectable ring element, separate from a fixed seat, positioned on the chamber side of the fixed seat so that the purge shoulder deflects it outward during over-travel to open the purge gap, while the fixed seat provides the sealing edge. A "fixed seat" means a component of the valve core that does not deflect during over-travel and that provides the sealing edge on which the sealing face of the poppet rests, used together with a wiper ring.

[0017] As used herein, a "convoluted wall" means a wall of the seat ring formed with one or more shallow convolutions, which converts axial load applied to the seat ring into radial deflection of the seat ring. The number of convolutions means the count of convolutions in the convoluted wall; the illustrated embodiment has one convolution or two convolutions.

#### Purge gap, purge flow path, main passage and radial deflection

[0018] As used herein, the "purge gap" means a clearance, associated with the deflectable ring element, that is closed in the closed state and in the normal-open state and that is opened by radial deflection of the deflectable ring element in the purge state, through which the air purge flows. In the illustrated embodiment the purge gap is an annular radial clearance between the outer surface of the seat ring and the core body bore; in other embodiments the purge gap is bounded by another surface of the deflectable ring element, and the term is not limited to the location of the illustrated embodiment.

[0019] As used herein, the "purge flow path" means the path, distinct from the main passage, from the supply side through the purge gap to the inflatable chamber, along which the air purge travels. The "main passage" means the passage past the sealing face that carries inflation gas into the inflatable chamber in the normal-open state and in the purge state. The main passage and the purge gap are different flow paths: the main passage is opened by lifting of the sealing face from the sealing edge at the crack pressure, whereas the purge gap is opened only by radial deflection of the deflectable ring element in the purge state. The "purge gap opening" means the radial size of the purge gap when the deflectable ring element is fully deflected in the purge state.

[0020] As used herein, "radial deflection" means elastic deformation of the wall of the deflectable ring element, produced by the purge shoulder during over-travel, that opens the purge gap. Radial deflection is a deformation of the deflectable ring element while it remains retained in the valve core; it is not a bodily displacement of the element as a whole. In the illustrated embodiment the radial deflection is outward.

#### Purge shoulder and deflecting formation

[0021] As used herein, a "purge shoulder" means the formation of the poppet, on the chamber side of the sealing face, that contacts the deflectable ring element only during over-travel and thereby deflects it radially to open the purge gap. The purge shoulder is a deflecting formation, meaning a formation that moves with the poppet and that contacts the deflectable ring element only during over-travel; the term "purge shoulder" is defined by that function and is not limited to the annular form of the purge shoulder of the illustrated embodiment.

#### Return spring, spring stages and threshold-setting arrangement

[0022] As used herein, the "return spring" means the biasing member that biases the poppet towards the closed state. The "first spring stage" means the stage of the return spring having the lower rate, which resists the normal stroke and thereby sets the crack pressure. The "second spring stage" means the stage of the return spring having a higher rate than the first spring stage, which the pressure differential must overcome, once the normal stroke is complete, to produce over-travel, and which thereby sets the over-travel threshold. A "threshold-setting arrangement" means any arrangement of the valve core that sets the over-travel threshold; the return spring having a first spring stage and a second spring stage is the threshold-setting arrangement of the illustrated embodiment.

#### Cleaning actions, sealant and inflation terms

[0023] As used herein, "cleaning action" means an action by which the valve core removes sealant film from its surfaces without a tool or user action. The cleaning actions described herein are the air purge, the snap-back wipe, or both. The "air purge" means the flow of inflation gas, at the pressure of the inflation device, along the purge flow path during the purge state, across the surfaces of the valve core on which sealant film accumulates and into the inflatable chamber. The inflation gas may be air supplied by a floor pump or another inflation device, or another gas supplied by a compressed-gas inflation device, such as a CO2 inflation device. The "snap-back wipe" means the movement of the deflectable ring element across a surface of the poppet as the deflectable ring element undergoes shape recovery when the pressure differential falls below the over-travel threshold, by which movement partially cured sealant film is sheared from that surface.

[0024] As used herein, "sealant film" means liquid sealant that has dried or cured, in whole or in part, on a surface of the valve core. "Liquid sealant" means a fluid, carried in the inflatable chamber, that is drawn into the valve core on inflation and that is capable of drying or curing on the surfaces of the valve core; in the tested embodiment the liquid sealant is an emulsion of latex containing ammonia and suspended particles, and the term is not limited to that chemistry. "Blockage" means a failure mode of the valve core in which sealant film prevents the poppet from opening within a defined response time of actuation by the inflation device.

[0025] As used herein, an "inflatable chamber" means the volume, inflated through the inflation valve and holding liquid sealant, of a bicycle inner tube or of a tubeless bicycle tyre set-up. An "inflation device" means the source of inflation gas coupled to the supply side, for example a floor pump with a pump head, or a compressed-gas inflation device. An "inflation event" means the period from coupling of an inflation device to the supply side until the inflation device is removed.

#### Materials terms

[0026] As used herein, a "superelastic alloy" means an alloy that recovers large elastic strains on unloading, at the service temperature of the inflation valve, by a reversible phase transformation between martensite and austenite; in the illustrated embodiment the superelastic alloy is a nickel-titanium alloy (NiTi) of nominally 55.8 wt% nickel content. The "austenite finish temperature" means the temperature above which the superelastic alloy of the deflectable ring element is fully austenitic and exhibits superelastic behaviour. The "martensite start temperature" means the temperature, on cooling the superelastic alloy of the deflectable ring element, below which martensite begins to form and superelastic recovery may be impaired. The austenite finish temperature and the martensite start temperature apply only to a deflectable ring element formed from a superelastic alloy.

[0027] As used herein, a "resilient metal" means a metal which, formed into the deflectable ring element, is deflected radially by the purge shoulder during over-travel and undergoes shape recovery when the pressure differential falls; a superelastic alloy is the resilient metal of the illustrated embodiment, and stainless steel is the resilient metal of the wiper ring described below. A "resilient polymer" means a polymer which, formed into the deflectable ring element, is deflected radially by the purge shoulder during over-travel and undergoes shape recovery when the pressure differential falls; polyether ether ketone (PEEK) is the resilient polymer described below.

#### Dimensional conventions

[0028] As used herein, the "seat ring inner diameter" means the inner diameter of the seat ring in its at-rest condition, measured at a portion of the wall free of convolutions, and the "seat ring outer diameter" means the outer diameter of the seat ring in its at-rest condition, measured at a portion of the wall free of convolutions. The "seat ring wall thickness" means the radial thickness of the material forming the convoluted wall of the seat ring. The "seat ring free length" means the axial length of the seat ring in its unloaded, at-rest condition. The "convolution amplitude" means the radial excursion of a convolution of the convoluted wall, measured from the mean radius of the wall to the peak or trough of the convolution. The "purge gap opening" and the "over-travel distance" are measured radially and axially respectively, as defined above, with the poppet at the end of over-travel.

#### Test definitions

[0029] As used herein, an "inflation cycle" means one repetition of an inflation event, a hold period at the resulting pressure of the inflatable chamber, and deflation of the inflatable chamber; in the working example an inflation cycle is inflation to 6 bar with a floor pump, a hold of 24 h at 22 °C, and full deflation through the inflation valve. "Leak-down" means the loss of pressure from the inflatable chamber, through the valve core, over a hold period. "Inflation time" means the elapsed time, using a given inflation device, from coupling to the supply side until the inflatable chamber reaches a stated pressure. A "conventional valve core" means a valve core lacking a deflectable ring element and a purge gap as defined herein, used as a comparator in the working example.

#### Structure of the valve core in the closed state

[0030] FIG. 1 is an axial section through the inflation valve of the illustrated embodiment on a plane containing the poppet axis, in the closed state. FIG. 5 shows the same components separated along the poppet axis in assembly order. FIG. 6A is an enlarged detail of the region of the seat ring 30, the internal shoulder 24 and the purge shoulder 44 in the closed state. The structure is described in this section in the closed state; the operation of the valve core through the normal-open state, the purge state and shape recovery is described in the following section.

#### Inflation valve and valve stem

[0031] Referring to FIG. 1, the inflation valve comprises a valve stem 10 having a stem bore 12, and a valve core received in the stem bore 12. The valve stem 10 is fixed to the inflatable chamber, which is a bicycle inner tube or a tubeless bicycle tyre set-up holding liquid sealant. In the illustrated embodiment the valve stem 10 is a conventional Presta-pattern valve stem of brass with an outer diameter of 6 mm, and the stem bore 12 is threaded. The core body 20 of the valve core is threaded into the stem bore 12, so that the valve core is retained in the valve stem 10 and can be removed from it as a unit. The Presta-pattern valve stem is described by way of example; the valve core and the inflation valve are not limited to that pattern.

#### The valve core

[0032] The valve core comprises a core body 20, a seat ring 30 carried by the core body 20, a poppet 40 guided by the core body 20, and a return spring 50 biasing the poppet 40 towards the closed state. The seat ring 30 is the deflectable ring element of the illustrated embodiment. The purge gap 60 is defined between the seat ring 30 and the core body 20, as described below. A lock nut 70 is provided on the supply side. In FIG. 5 the components are shown in assembly order: the lock nut 70, the valve stem 10, the core body 20, the seat ring 30, the poppet 40 with its sealing face 42 and purge shoulder 44, and the return spring 50 with its first spring stage 52 and second spring stage 54. The valve core is fitted to and removed from the valve stem 10 as a whole, and may be supplied separately from the valve stem 10 as a replacement valve core for fitting to an existing valve stem.

#### Core body

[0033] The core body 20 is a turned component having an external thread engaged in the stem bore 12, a core body bore 22 that receives the seat ring 30, and an internal shoulder 24 against which the seat ring 30 is seated so that the seat ring 30 is located axially in the core body 20. The core body 20 also guides the poppet 40 in its axial movement. In the illustrated embodiment the core body 20 is turned from free-machining brass CW614N. In other embodiments the core body 20 is turned from stainless steel, for example grade 303, for corrosion resistance in the presence of ammonia-bearing liquid sealant; the core body 20 is turned by ordinary machining in either material and no other special process is required. The core body 20 is not limited to those materials.

#### Seat ring

[0034] The seat ring 30 is an annular element received in the core body bore 22 and seated against the internal shoulder 24. It has a sealing edge 34 at one axial end, on which the sealing face 42 of the poppet 40 rests in the closed state, and a convoluted wall 32 between its ends. In the illustrated embodiment the convoluted wall 32 has one convolution 32a or two convolutions 32a, 32b, each convolution being a shallow radial excursion of the wall; the convoluted wall 32 converts axial load applied to the seat ring 30 into radial deflection of the seat ring 30. The seat ring 30 is thin-walled relative to the core body 20, and its dimensions and their ranges are given below with reference to FIG. 6.

[0035] In the illustrated embodiment the seat ring 30 is formed from a superelastic alloy, namely a nickel-titanium alloy of nominally 55.8 wt% nickel content, having an austenite finish temperature specified below 5 °C so that the seat ring 30 is superelastic at riding temperatures. In other embodiments the seat ring 30 is formed from a resilient polymer, such as PEEK, with the same convoluted wall 32. The materials of the deflectable ring element, and the effect of the material on shape recovery and on the snap-back wipe, are described below.

[0036] The seat ring 30 is retained in the core body 20 by an interference fit, the interference being approximately 0.03 mm on diameter, and is pressed into the core body bore 22 until it is seated against the internal shoulder 24. In some embodiments the interference fit is provided over an axial band of the seat ring 30 adjacent the internal shoulder 24, and the remainder of the outer surface of the seat ring 30, including the portion of the convoluted wall 32 that undergoes radial deflection, is not in interference with the core body bore 22, so that this portion of the wall is free to move relative to the core body bore 22 during radial deflection. FIG. 6A shows the interference fit region between the seat ring 30 and the internal shoulder 24 and, distinct from it, the region in which the purge gap 60 is located. Other ways of retaining the seat ring 30 in the core body 20 are described below.

#### Poppet

[0037] The poppet 40 has a poppet stem 41, which is guided by the core body 20 and along which liquid sealant is drawn by capillary action during inflation, a sealing face 42, and a purge shoulder 44. In the illustrated embodiment the poppet 40 is of brass and the sealing face 42 is conical. In the closed state the sealing face 42 rests on the sealing edge 34 of the seat ring 30, and the seal between the supply side and the chamber side is formed at the sealing edge 34 by the sealing face 42; the closed-state seal is formed between the sealing face 42 and the sealing edge 34 without any elastomeric element in the illustrated embodiment. Other forms and materials of the sealing face 42 are described below.

[0038] The purge shoulder 44 is a formation of the poppet 40 on the chamber side of the sealing face 42. In the illustrated embodiment the purge shoulder 44 is an annular shoulder integral with the poppet 40. In the closed state the purge shoulder 44 is spaced axially from the seat ring 30 (FIG. 1, FIG. 6A), and the axial clearance between the purge shoulder 44 and the seat ring 30 is such that the purge shoulder 44 remains spaced from the seat ring 30 throughout the normal stroke and contacts the seat ring 30 only during over-travel. The purge shoulder 44 therefore takes no part in sealing and no part in the normal stroke; its only function is to bear on the seat ring 30 during over-travel and to deflect it radially. Other forms of deflecting formation are described below.

#### Return spring

[0039] The return spring 50 biases the poppet 40 towards the closed state and has a first spring stage 52 and a second spring stage 54. The first spring stage 52 has the lower rate; it resists the normal stroke and sets the crack pressure. The second spring stage 54 has a higher rate than the first spring stage 52; it comes into action when the normal stroke is complete, it must be overcome by the pressure differential to produce over-travel, and it thereby sets the over-travel threshold. In the illustrated embodiment the first spring stage 52 and the second spring stage 54 are stages of a single return spring 50 of stainless steel music wire. The mechanism does not depend on the material of the return spring 50. The return spring 50 with its first spring stage 52 and second spring stage 54 is the threshold-setting arrangement of the illustrated embodiment; other threshold-setting arrangements are described below.

#### Purge gap in the closed state

[0040] In the illustrated embodiment the purge gap 60 is an annular radial clearance between the outer surface of the seat ring 30 and the core body bore 22 (FIG. 1, FIG. 6A). In the closed state the purge gap 60 is closed, and it remains closed in the normal-open state; it is opened only by radial deflection of the seat ring 30 when the purge shoulder 44 bears on the seat ring 30 during over-travel. In the closed state the seal between the supply side and the chamber side is formed at the sealing edge 34 by the sealing face 42. The purge gap 60 is a flow path distinct from the main passage 64: the main passage 64 is the passage past the sealing face 42, which opens at the crack pressure, whereas the purge gap 60 is closed at the crack pressure and throughout the normal stroke and opens only in the purge state. The purge gap 60 and the purge flow path 62 through it are described in the purge state, and their location in other embodiments, below.

#### Lock nut

[0041] The lock nut 70 is a conventional Presta-pattern lock nut. When engaged by hand it holds the poppet 40 in the closed state irrespective of the pressure differential, for storage and transport. While the lock nut 70 is engaged the sealing face 42 rests on the sealing edge 34, the purge shoulder 44 is spaced from the seat ring 30, and the seat ring 30 is at rest and undeflected; the lock nut 70 is therefore the preferred means of holding the inflation valve closed during storage and transport, rather than any accessory that bears on the poppet 40 in the opening direction. The lock nut 70 is a conventional component and takes no part in the cleaning actions.

#### Operation: the states of the valve core

[0042] The valve core operates in a closed state, a normal-open state and a purge state, and passes through a recovery from the purge state back to the closed state. The state that the valve core occupies is determined by the pressure differential across the poppet (40), that is by the pressure on the supply side less the pressure on the chamber side, acting against the return spring (50). FIG. 7 shows the sequence of states as a diagram, with the condition that governs each transition marked on the corresponding arrow. Control of the valve core is entirely mechanical; no electrical or electronic control is present.

[0043] In the closed state (FIG. 1) the pressure differential is below the crack pressure, the sealing face (42) of the poppet (40) rests on the sealing edge (34) of the seat ring (30), the main passage (64) is closed and the purge gap (60) is closed. In the normal-open state (FIG. 2) the pressure differential is at or above the crack pressure and below the over-travel threshold; the poppet (40) is displaced from the closed state by the normal stroke, the main passage (64) is open, the purge shoulder (44) is spaced from the seat ring (30), and the purge gap (60) remains closed. In the purge state (FIG. 3) the pressure differential exceeds the over-travel threshold, the over-travel threshold being higher than the crack pressure; the poppet (40) is in over-travel beyond the normal stroke, the purge shoulder (44) bears on the seat ring (30) and deflects it radially, and the purge gap (60), which is a flow path separate from the main passage (64), is open. The purge gap (60) is therefore closed in the closed state and in the normal-open state, and is open only in the purge state.

[0044] Recovery follows the purge state when the pressure differential falls below the over-travel threshold, as occurs when the inflation device is removed from the supply side. The return spring (50) returns the poppet (40) towards the closed state, the seat ring (30) undergoes shape recovery, the snap-back wipe occurs and the purge gap (60) closes (FIG. 4). The lock nut (70) may be tightened by hand to hold the poppet (40) in the closed state irrespective of the pressure differential, for storage and transport; FIG. 7 shows this as the locked condition. The lock nut (70) holds the poppet (40) in the closed state and not in over-travel, so that the seat ring (30) is not held in radial deflection while the inflation valve is stored.

[0045] The main passage (64) and the purge gap (60) are distinct flow paths. The main passage (64) is the passage past the sealing face (42) that carries inflation gas into the inflatable chamber whenever the sealing face (42) is lifted from the sealing edge (34), that is in the normal-open state and in the purge state. The purge gap (60) is a passage bounded at least in part by a surface of the seat ring (30); it is closed while the seat ring (30) is in its at-rest form and is opened only by the radial deflection of the seat ring (30). Inflation gas passing through the purge gap (60) follows the purge flow path (62), which is described below.

#### The crack pressure and the normal stroke

[0046] When an inflation device is coupled to the supply side and the pressure differential reaches the crack pressure, the force on the poppet (40) overcomes the first spring stage (52) of the return spring (50) and the poppet (40) moves along the poppet axis towards the chamber side, lifting the sealing face (42) from the sealing edge (34). The crack pressure is set by the first spring stage (52), which is the lower-rate stage of the return spring (50) and which alone resists the poppet (40) during the normal stroke. The normal stroke is the displacement of the poppet (40) from the closed state up to the position at which the purge shoulder (44) would first contact the seat ring (30). In the prototype the crack pressure is 1.0 bar and the normal stroke is 0.6 mm; the range of the crack pressure is given below together with the other operating parameters.

[0047] Throughout the normal stroke the purge shoulder (44) remains axially spaced from the seat ring (30) by an axial clearance, shown in FIG. 2 as the residual clearance between the purge shoulder (44) and the seat ring (30) at the end of the normal stroke. The seat ring (30) is not loaded by the poppet (40) during the normal stroke, retains its at-rest form, and the purge gap (60) remains closed. Inflation gas flows through the main passage (64) only. Until the over-travel threshold is reached, therefore, the valve core admits inflation gas and seals in the same manner as a conventional valve core, the seat ring (30) serving only to seat the sealing face (42).

#### The over-travel threshold and over-travel

[0048] When the pressure differential exceeds the over-travel threshold, the poppet (40) moves beyond the end of the normal stroke into over-travel. The over-travel threshold is set by the second spring stage (54) of the return spring (50), which has a higher rate than the first spring stage (52) and which the poppet (40) engages at the end of the normal stroke. In the prototype the over-travel threshold is 3.5 bar and the over-travel distance is 0.5 mm. The normal stroke and the over-travel are two successive ranges of movement of the one poppet (40) along the same axis, distinguished by the pressure differential at which each occurs and by whether the purge shoulder (44) bears on the seat ring (30); no second closure member and no second seating surface is involved, and the seat ring (30) remains the valve seat member throughout.

[0049] The over-travel distance is the axial distance that the poppet (40) moves beyond the end of the normal stroke. In some embodiments the over-travel distance is limited by an over-travel stop in the core body (20) that the poppet (40) meets at the end of the over-travel; in other embodiments it is limited by the second spring stage (54) reaching its solid length, or by the resistance of the seat ring (30) to further radial deflection.

[0050] The second spring stage (54) is one species of threshold-setting arrangement. In the illustrated embodiment the return spring (50) is a single compression spring having the first spring stage (52) and the second spring stage (54). Once the purge shoulder (44) bears on the seat ring (30), the resistance of the seat ring (30) to radial deflection adds to the force that the pressure differential must overcome, so that the return spring (50) and the seat ring (30) may each contribute to the over-travel threshold. Other threshold-setting arrangements, in which the step in resisting force at the end of the normal stroke is provided by a separate auxiliary spring engaged after a lost-motion clearance, by a detent, or by the seat ring (30) alone with a single-rate return spring (50), are described below with reference to FIG. 14.

[0051] The over-travel threshold is higher than the crack pressure, so that there is a normal-open state in which the valve core admits inflation gas without entering the purge state, and the seat ring (30) is deflected only when the inflation device raises the pressure differential above the over-travel threshold. In the prototype the crack pressure is 1.0 bar and the over-travel threshold is 3.5 bar. In the test described in Example 1, a floor pump inflating an inner tube from fully deflated to 6 bar produced over-travel on every inflation event. In some embodiments the over-travel threshold is set close to the crack pressure, so that the purge state is reached on substantially every opening of the valve core and the normal stroke is short; in such embodiments the second spring stage (54) may be omitted and the return spring (50) has a single rate.

#### The purge state

[0052] When the poppet (40) enters over-travel, the purge shoulder (44), which lies on the chamber side of the sealing face (42), comes into contact with the seat ring (30) and bears on it with a force that rises with the pressure differential. The seat ring (30) is retained in the core body (20) against the internal shoulder (24), and the axial load applied by the purge shoulder (44) is converted by the convoluted wall (32) of the seat ring (30) into radial deflection of the wall. In the illustrated embodiment the radial deflection is an elastic deformation of the wall of the seat ring (30) while the seat ring (30) remains retained by the core body (20) at the internal shoulder (24), rather than a bodily movement of the seat ring (30) relative to the core body (20).

[0053] The radial deflection opens the purge gap (60). The purge gap (60) is closed while the seat ring (30) is in its at-rest form, and opens when the radial deflection moves a surface of the seat ring (30) away from the surface against which it bounds the purge gap (60). FIG. 3 shows the seat ring (30) in radial deflection, its at-rest outline repeated in dashed line, with the purge gap (60) open; FIG. 6B shows the same region enlarged, with the purge gap opening marked. In the embodiment of FIGS. 1 to 4 the purge gap (60) is located at the outer surface of the seat ring (30), between that surface and the core body bore (22), and, as described above, the interference fit between the seat ring (30) and the core body (20) may be confined to an axial band at the internal shoulder (24) so that the remainder of the outer surface of the seat ring (30) is free of the core body bore (22) (FIG. 6A). The purge gap opening is the radial size of the purge gap (60) when the seat ring (30) is fully deflected in the purge state; in the prototype the purge gap opening is 0.15 mm.

[0054] The sense of the radial deflection that opens the purge gap (60) depends on which surfaces bound the purge gap (60). The radial deflection may be radially outward, as described for the embodiment of FIG. 3; it may be radially inward at the surface of the seat ring (30) that bounds the purge gap (60), for example by flattening of the crest of a convolution under axial load; or it may be an ovalising deflection, produced where the purge shoulder (44) contacts the seat ring (30) at discrete points around its circumference, that moves the wall outward at the points of contact and inward between them and so opens the purge gap (60) over arcs of the circumference. The locations at which the purge gap (60) may be formed, and the sense of radial deflection that each requires, are described below with reference to FIG. 10 and FIG. 13.

[0055] In embodiments having a fixed seat (130) and a separate wiper ring (132) (FIG. 10), the sealing face (42) seats on the fixed seat (130) in the closed state, and in the purge state the purge shoulder (44) bears on and deflects the wiper ring (132), which is the deflectable ring element of those embodiments; the purge gap (60) is then bounded by a surface of the wiper ring (132) and is opened by its radial deflection. Everything said in this section of the seat ring (30) as the element deflected by the purge shoulder (44) applies to the wiper ring (132) in those embodiments.

#### The purge flow path and the air purge

[0056] With the purge gap (60) open and inflation gas being supplied to the supply side, inflation gas flows from the supply side through the purge gap (60) along the purge flow path (62) to the chamber side of the seat ring (30) and into the inflatable chamber, at the same time as inflation gas flows through the main passage (64). FIG. 3 shows both flows with arrows. The purge flow path (62) crosses the surfaces of the valve core on which sealant film accumulates, in the illustrated embodiment the outer surface of the seat ring (30) and the adjoining region of the core body bore (22), and the inflation gas carries sealant film from those surfaces into the inflatable chamber. This flow is the air purge.

[0057] The air purge occurs at the pressure of the inflation device, in the direction of inflation, so that sealant film removed by the air purge is carried away from the valve core into the inflatable chamber and not towards the inflation device. The air purge continues for as long as the pressure differential remains above the over-travel threshold and inflation gas is supplied, and ends when the pressure differential falls and the purge gap (60) closes.

[0058] The inflation gas of the air purge is any gas supplied by the inflation device: air from a floor pump, a hand pump or a compressor, or gas from a compressed-CO2 inflation device. The air purge occurs with any inflation device that raises the pressure differential across the poppet (40) above the over-travel threshold. The over-travel threshold is accordingly chosen to lie above the crack pressure and within the pressure differential that the intended inflation device produces. In the test described in Example 1 the inflation device was a floor pump.

[0059] In the illustrated embodiment the purge flow path (62) runs alongside the main passage (64), from the supply side through the purge gap (60) to the chamber side of the seat ring (30). Other purge flow paths, through purge ports in the wall of the core body (20) or along flutes in the core body bore (22), are described below with reference to FIG. 13.

#### Removal of the inflation device: shape recovery and the snap-back wipe

[0060] When the inflation device is removed from the supply side, the pressure differential collapses. The return spring (50) returns the poppet (40) towards the closed state, the load applied by the purge shoulder (44) to the seat ring (30) is removed, and the seat ring (30) undergoes shape recovery to its at-rest form, closing the purge gap (60). As it recovers, the seat ring (30) moves across the sealing face (42) of the poppet (40), or across an adjacent surface of the poppet (40), and shears from that surface liquid sealant that has partially cured on it. This movement of the recovering seat ring (30) across a surface of the poppet (40) is the snap-back wipe. FIG. 4 shows the seat ring (30) during shape recovery, with the direction of its movement across the sealing face (42) indicated by an arrow and the purge gap (60) closing. The sealing face (42) then re-seats on the sealing edge (34) and the valve core is again in the closed state.

[0061] The relative movement that produces the snap-back wipe is driven by the shape recovery of the seat ring (30), which is held in the core body (20), and not only by the return stroke of the poppet (40): the wall of the seat ring (30) returns radially across the surface of the poppet (40) as the poppet (40) passes it. In the embodiment of FIGS. 1 to 4 the element that performs the snap-back wipe is the seat ring (30) itself, whose sealing edge (34) seats the sealing face (42) in the closed state. The snap-back wipe therefore acts on the sealing face (42), which is the surface that seals, and no separate part that could itself accumulate sealant film is needed to perform it. The sealing face (42) and the sealing edge (34) are the surfaces found clean at the end of the test described in Example 1.

[0062] In the illustrated embodiment the region of the seat ring (30) that moves across the poppet (40) during the snap-back wipe is the region of the sealing edge (34), and the surface of the poppet (40) that is wiped is the sealing face (42), as shown in FIG. 4.

[0063] The strength of the snap-back wipe depends on the speed and force of the shape recovery, which depend on the material of the seat ring (30). Where the seat ring (30) is formed from a superelastic alloy, the shape recovery is rapid and the recovery force is high, so that the recovering seat ring (30) shears partially cured sealant film from the surface of the poppet (40) rather than riding over it; in the prototype a snap is audible on removal of the inflation device. A superelastic alloy is preferred for the seat ring (30) for this reason. Where the seat ring (30) is formed from a resilient polymer such as PEEK, the shape recovery is slower and the recovery force lower, so that the snap-back wipe is weaker; the movement of the recovering polymer seat ring (30) across the surface of the poppet (40) is nonetheless a snap-back wipe as described herein, and the air purge acts independently of it. A soft sealing element that deforms under the sealing face (42) has, by contrast, the disadvantage that liquid sealant embeds itself in the deformed sealing surface as it cures instead of being sheared from the sealing face (42).

#### The two cleaning actions

[0064] The valve core thus cleans its sealing surfaces twice in each inflation event that reaches the purge state: once by the air purge while the purge gap (60) is open, and once by the snap-back wipe as the seat ring (30) recovers. Both cleaning actions are produced by the poppet (40) moving into and out of over-travel under the pressure differential applied by the inflation device; neither requires a tool, a separate actuator or any action by the user beyond inflating the inflatable chamber. The air purge acts on the surfaces along the purge flow path (62); the snap-back wipe acts on the surface of the poppet (40) that the recovering seat ring (30) crosses.

[0065] In the embodiment of FIGS. 1 to 4 the cleaning action comprises both the air purge and the snap-back wipe. The two actions are, however, independent of one another. The snap-back wipe occurs whenever a deflectable ring element held in the core body (20) is deflected by the purge shoulder (44) in over-travel and undergoes shape recovery when the pressure differential falls, whether or not inflation gas flows through the purge gap (60) while the deflectable ring element is deflected. The air purge occurs whenever the purge gap (60) is open while inflation gas is supplied, whether or not the recovering deflectable ring element wipes the poppet (40). Accordingly, in some embodiments the cleaning action is provided by the air purge and the snap-back wipe together; in some embodiments it is provided principally by the air purge, for example where the deflectable ring element is of a resilient polymer whose shape recovery produces only a weak snap-back wipe; and in some embodiments it is provided by the snap-back wipe alone, the deflectable ring element being sealed at its periphery so that no inflation gas flows past it while it is deflected, and the radial deflection in over-travel followed by the shape recovery on release producing the snap-back wipe without an air purge. The test described in Example 1 shows the combined effect of the two cleaning actions in the prototype; it does not apportion that effect between them.

#### Over-travel by other means and purge during deflation

[0066] In the embodiments described above, over-travel is produced by the pressure differential exceeding the over-travel threshold. In some embodiments over-travel is produced, in addition or instead, by mechanical depression of the poppet (40): a depressor in the head of the inflation device, or in an adaptor fitted between the inflation device and the supply side, pushes the poppet (40) beyond the normal stroke into over-travel when the inflation device is coupled, whatever the pressure differential. In such embodiments the purge state lasts for as long as the inflation device is coupled, and the second spring stage (54) may be omitted. In some embodiments the poppet (40) is pressed into over-travel by hand, with the lock nut (70) released.

[0067] The purge state may also be reached during deflation of the inflatable chamber. When the poppet (40) is pressed into over-travel while the inflatable chamber is pressurised and no inflation device is supplying gas, the purge gap (60) opens and gas from the inflatable chamber flows through the purge gap (60) in the direction from the chamber side to the supply side, carrying sealant film out of the valve core. The purge flow path (62) may therefore carry flow in either direction. In some embodiments the purge state is reached during deflation as well as during inflation; in other embodiments it is reached during deflation only, each inflation event using the normal stroke alone.

#### Inflation events and inflation cycles

[0068] An inflation event is the period from coupling of an inflation device to the supply side until its removal. Within one inflation event that reaches the purge state, the valve core passes from the closed state through the normal-open state to the purge state as the pressure differential rises past the crack pressure and then past the over-travel threshold, remains in the purge state while the pressure differential exceeds the over-travel threshold, and returns through recovery to the closed state when the inflation device is removed. The two cleaning actions therefore occur once per inflation event: the air purge during the purge state and the snap-back wipe on recovery. In the test described in Example 1, in which each inflation event inflated an inner tube from fully deflated to 6 bar with a floor pump, the purge state was reached in every inflation event, as indicated by the snap audible on removal of the inflation device.

[0069] An inflation event in which the pressure differential does not exceed the over-travel threshold, for example where the inflation device produces a lower pressure differential, is completed in the normal-open state: the valve core admits inflation gas through the main passage (64) and closes on removal of the inflation device without entering the purge state and without the seat ring (30) being deflected. Whether a given inflation event reaches the purge state depends on the pressure differential that the inflation device produces across the poppet (40) during that event.

[0070] An inflation cycle is one repetition of an inflation event, a hold period at the resulting chamber pressure and deflation of the inflatable chamber. Over repeated inflation cycles, liquid sealant drawn into the valve core during one inflation event, and dried or partially cured during the following hold period, is acted on by the air purge and the snap-back wipe of the next inflation event that reaches the purge state. The behaviour of the prototype and of a conventional valve core over forty such inflation cycles is reported in Example 1 and Comparative Example 1.

#### Materials of the deflectable ring element

[0071] The deflectable ring element is defined above by what it does: it is carried by the valve core, it is deflected radially by the purge shoulder (44) during over-travel so as to open a purge flow path, and it undergoes shape recovery towards its at-rest form when the pressure differential falls. Any material that provides a recoverable radial deflection of the size needed to open the purge gap (60), and that returns the ring element to its at-rest form when the load of the purge shoulder (44) is removed, may be used. The material chosen determines the force and speed of the shape recovery, and therefore the strength of the snap-back wipe, and it determines the wall geometry needed to keep the strain in the wall within what the material recovers. The materials are described here for the seat ring (30) of the illustrated embodiment; they apply equally to the wiper ring (132) of the fixed seat and wiper ring embodiment described below, subject to the exceptions stated.

[0072] In the preferred embodiments the seat ring (30) is formed from a superelastic alloy. The seat ring (30) of the worked example is formed from a nickel-titanium alloy (NiTi) having a nickel content of nominally 55.8 wt%, from drawn tube stock. The alloy is specified to have an austenite finish temperature below 5 °C, so that the seat ring (30) is fully austenitic, and behaves superelastically, at the temperatures at which the inflation valve is used. A superelastic alloy recovers large strains on unloading by a reversible transformation between martensite and austenite, so that a thin wall of the alloy can be deflected radially by an amount of the order of the purge gap opening and return to its at-rest form within the closing movement of the poppet (40), with a recovery that is fast and carries force. That recovery gives the seat ring (30) its strongest snap-back wipe: the recovering seat ring (30) shears partially cured sealant film from the surface of the poppet (40) it crosses rather than riding over it. A sealing element soft enough to deform under the sealing face (42), such as an elastomeric one, by contrast lets liquid sealant embed itself in the sealing surface, where neither the air purge nor a wipe reaches it; the superelastic alloy provides radial compliance without a soft sealing surface.

[0073] The austenite finish temperature of the worked example is an upper limit chosen so that the seat ring (30) is superelastic across riding temperatures. Below the martensite start temperature of the alloy, martensite forms on cooling and shape recovery may be impaired until the alloy is warmed again above its austenite finish temperature. The margin between the martensite start temperature and the lowest temperature the seat ring (30) reaches in service, including transient chilling by the expansion of gas from a compressed-gas inflation device, is therefore a design consideration. In some embodiments the alloy is selected, by its nickel content or by the shape-setting treatment described below, to have a lower austenite finish temperature and hence a wider margin. No value below 5 °C is specified herein, and the behaviour of the seat ring (30) when chilled by a compressed-gas inflation device was not tested. Where a superelastic alloy is used, the austenite finish temperature is a property of that alloy species; it has no counterpart for a resilient polymer or for a resilient metal that does not transform, and every reference herein to the austenite finish temperature is to be read as conditioned on the superelastic alloy species.

[0074] In some embodiments the superelastic alloy is a binary NiTi alloy, as in the worked example. In other embodiments it is a ternary NiTi alloy: a NiTiCu alloy, which gives a narrower transformation hysteresis and more stable behaviour over repeated cycles, or a NiTiFe or NiTiCr alloy, which gives a lower austenite finish temperature. The transformation temperatures and the plateau stress of the alloy chosen interact with the over-travel threshold in embodiments in which the stiffness of the deflectable ring element contributes to the threshold-setting arrangement, as described below. Copper-based superelastic alloys, such as Cu-Al-Mn and Cu-Al-Ni alloys, may also be used, but copper alloys are attacked by ammonia, so these alloys are contemplated only for use with an ammonia-free liquid sealant.

[0075] In other embodiments the deflectable ring element is formed from a resilient metal that recovers its shape elastically without a phase transformation. Examples are stainless steel of spring temper, cold-worked austenitic stainless steel, precipitation-hardened stainless steel such as 17-7PH, and beta-titanium alloys. Stainless steel of spring temper is the disclosed material of the wiper ring (132) of the fixed seat and wiper ring embodiment. The recoverable strain of such a metal is much lower than that of a superelastic alloy, so a deflectable ring element of resilient metal is given a thinner wall, a smaller radial deflection, or a slotted or cellular wall as described below, so that the purge gap opening is reached within the elastic range of the material. A resilient metal has no austenite finish temperature, and its recovery does not depend on temperature in the manner of a superelastic alloy.

[0076] In further embodiments the deflectable ring element is formed from a resilient polymer. The disclosed polymer is polyether ether ketone (PEEK). A seat ring (30) of PEEK having the same convoluted wall (32) as the superelastic seat ring provides radial compliance under the purge shoulder (44) at lower cost, but its shape recovery is slower and the force of the recovery lower, so that its snap-back wipe is weaker than that of the superelastic seat ring. The purge gap (60) and the air purge provide their cleaning action independently of the wipe, so the polymer seat ring retains the air purge in full. This embodiment is illustrated in FIG. 9 and is intended for a lower-cost product line. Other resilient polymers that resist the liquid sealant, such as polyphenylene sulphide (PPS) and polyetherimide (PEI), may be used; creep of the polymer under a sustained interference fit, and its resistance to an ammonia-bearing liquid sealant, are checked for the polymer chosen. Electropolishing, and the austenite finish temperature, have no application to a polymer deflectable ring element.

[0077] Whatever the material, the snap-back wipe is the movement of the recovering deflectable ring element across a surface of the poppet (40) as the pressure differential falls; the term carries no speed or force qualifier. The superelastic alloy is preferred because it gives the strongest wipe. Across the material classes described above the wipe force falls from superelastic alloy to resilient metal to resilient polymer, and the wall geometry and the over-travel distance are adapted accordingly, while the air purge is available with every material.

#### Wall geometry converting axial load into radial deflection

[0078] The purge shoulder (44) moves axially with the poppet (40). To open the purge gap (60), the deflectable ring element converts the axial load applied by the purge shoulder (44) into a radial deflection of the surface that bounds the purge gap (60). This axial-to-radial conversion geometry is the second defining feature of the deflectable ring element after its material, and the load chain is the same in every embodiment: the purge shoulder (44) bears on the deflectable ring element only in over-travel; the geometry of the ring element turns that axial load into radial deflection; the radial deflection opens the purge gap (60), which is closed in the closed state and the normal-open state; and the shape recovery of the ring element closes the purge gap (60) again when the load is removed. The wall geometry is chosen together with the material so that the purge gap opening is reached at the over-travel distance within the strain the material recovers. The geometry is loaded mechanically by the purge shoulder (44), at a defined location and at service temperature; no heating or other external actuation is involved in reaching the purge state.

[0079] In the illustrated embodiment the geometry is a convoluted wall (32). The wall of the seat ring (30) between the sealing edge (34) and the end of the seat ring (30) seated against the internal shoulder (24) is formed with one or more shallow convolutions, each a radial excursion of the wall of a convolution amplitude measured from the mean radius of the wall. Axial load applied by the purge shoulder (44) shortens the wall and changes the depth of the convolutions, moving the wall radially. The number of convolutions in the disclosed embodiments is one or two; FIG. 6A shows a first convolution (32a) and, optionally, a second convolution (32b). A wall with three or more convolutions may be used; each additional convolution adds axial compliance and reduces the radial deflection obtained per convolution for a given load, and the number is limited to that at which the wall still moves radially rather than merely shortening. The profile of a convolution is not limited to a rounded wave; it may be a saw-tooth, or a helical or circumferential wave. Optionally, the root of each convolution is provided with a fillet radius, which reduces the concentration of strain at the root under repeated radial deflection.

[0080] The convolution amplitude, together with the seat ring wall thickness and the seat ring free length, sets the relationship between the axial load applied by the purge shoulder (44), the resulting radial deflection, and the strain in the wall. A shallow convolution in a thin wall gives a radial deflection of the order of the purge gap opening at a strain the superelastic alloy recovers fully, and the convoluted wall (32) is the preferred geometry for that reason.

[0081] Other axial-to-radial conversion geometries are shown in FIG. 12. In FIG. 12A the wall is a frustoconical wall (232): a plain wall with a conical flare, in which axial load applied at the narrow end increases the flare and moves the free end radially outward, with no convolution to form. In FIG. 12B the wall is a slotted wall (332): a short tubular wall having a continuous band at the end carrying the sealing edge (34) and axial slots cut from the other end, which divide the remainder of the wall into fingers (332a, 332b) that splay radially under the load of the purge shoulder (44). The slotted wall (332) gives a large radial deflection at low force and low strain, which suits a resilient metal, and the continuous band keeps the sealing edge (34) intact. In FIG. 12C the wall is a cellular wall (432): a pattern of diamond or chevron cells cut through the wall between two continuous end bands, the struts of which rotate under axial compression so that the wall enlarges radially. The cellular wall (432) is formed by the same laser cutting as the convoluted wall (32), and the sealing edge (34) is carried on one of the continuous end bands. The coupling between axial shortening and radial enlargement of a cellular wall depends on the cell geometry chosen.

[0082] In a further embodiment, not separately illustrated, the deflectable ring element is a conical annular disc: a thin frustoconical annulus held at one rim. Axial load from the purge shoulder (44) flattens the cone and moves the free rim radially, outward where the inner rim is held and inward where the outer rim is held. The radial movement per unit of axial stroke is small at shallow cone angles, and this form is used with a separate fixed seat (130) for sealing, in the manner of the fixed seat and wiper ring embodiment described below.

[0083] In a further embodiment the wall of the deflectable ring element is plain, with no conversion geometry of its own, and the radial deflection is produced by a tapered purge shoulder (244), FIG. 11A: a frustoconical flank of the poppet (40) enters the deflectable ring element during over-travel and expands it by direct radial contact with its inner surface, as a mandrel expands a ring. The load on the ring element is then radial rather than axial. The flank slides on the inner surface of the ring element, with more friction and wear than the axial loading of the convoluted wall (32), and wipes that inner surface on the return stroke.

[0084] The frustoconical wall (232), the slotted wall (332), the cellular wall (432), the conical annular disc and the plain wall driven by a tapered purge shoulder (244) are alternatives that perform the same function as the convoluted wall (32), namely converting the movement of the poppet (40) in over-travel into radial deflection of the deflectable ring element, and any of them may be used with any of the materials described above, subject to the strain the material recovers. Each of these geometries may be applied to a seat ring (30) that also seals or, in the fixed seat and wiper ring embodiment, to a wiper ring (132) that does not seal.

#### Continuous, split and segmented forms, and the purge opening

[0085] The seat ring (30) of the illustrated embodiment is a continuous ring, and its sealing edge (34) is continuous around its circumference, so that the sealing face (42) of the poppet (40) seals on it in the closed state. Where the deflectable ring element also provides the sealing edge (34), the band of the ring that carries the sealing edge (34) remains continuous in every form described herein; the slotted wall (332) and the cellular wall (432) place their slots and cells away from that band.

[0086] The purge gap (60) of the illustrated embodiment is an annular clearance bounded at least in part by a surface of the seat ring (30), closed in the closed state and the normal-open state and opened by the radial deflection, as described above. The purge opening through which the air purge passes need not be an annular clearance at a surface of the ring element. In the slotted wall (332) and the cellular wall (432) the slots or cells pass through the wall, and in some embodiments they form the purge opening: they are closed at rest by contact of the wall with the surface of the core body bore (22) that faces them and are uncovered when the radial deflection moves the wall away from that surface, so that inflation gas passes through the wall of the deflectable ring element rather than around it. In such embodiments the ring element may be fitted in the core body bore (22) with no clearance at its outer surface at rest. A deflectable ring element that does not itself seal may also be segmented: a ring divided into fingers whose gaps open under the purge shoulder (44), or a split wiper ring having a single axial split that opens circumferentially under a tapered purge shoulder (244), the split being the purge opening. A split ring is not used as a one-piece seat ring (30), because the split would interrupt the sealing edge (34).

[0087] The purge opening is therefore, in the various embodiments, an annular gap at a surface of the deflectable ring element, one or more slits or apertures through its wall, or one or more gaps between the fingers of a segmented ring element. In each case it is closed in the closed state and the normal-open state and opened by the radial deflection in the purge state, and the deflectable ring element is continuous, slotted, cellular, split or segmented accordingly. Slots, cells and splits that pass through the wall can retain liquid sealant, which is a consideration in choosing between the forms.

#### Dimensions and parameter ranges

[0088] The dimensions and pressures given below are those of the superelastic seat ring (30) of the worked example, together with the ranges within which the mechanism is expected to operate with a seat ring (30) of that material and wall geometry. The relationships between the parameters govern, and the numbers follow from them. First, the over-travel threshold is higher than the crack pressure, so that the valve core opens and seals as a conventional valve core does until the purge state is reached, and the over-travel threshold lies within the pressure differential that the inflation device applies, so that the purge state is reached during an inflation event. Second, the purge gap (60) is closed at rest and remains closed throughout the normal stroke, the purge shoulder (44) being spaced from the deflectable ring element by at least the normal stroke at rest. Third, the radial deflection produced at the over-travel distance is at least the purge gap opening, and the strain it imposes on the wall is within what the material of the deflectable ring element recovers, so that the purge gap (60) closes again on shape recovery. Fourth, the seat ring inner diameter admits the poppet stem (41) and presents the sealing edge (34) to the sealing face (42), and the seat ring outer diameter fits the core body bore (22) with the interference fit at the internal shoulder (24). A person skilled in the art who changes one parameter adjusts the others to preserve these relationships.

[0089] The seat ring inner diameter is from 2.0 mm to 2.6 mm; in some embodiments from 2.1 mm to 2.5 mm; in some embodiments from 2.2 mm to 2.4 mm; in the worked example 2.3 mm. The seat ring wall thickness, being the radial thickness of the material of the convoluted wall (32), is from 0.15 mm to 0.30 mm; in some embodiments from 0.16 mm to 0.24 mm; in some embodiments from 0.18 mm to 0.22 mm; in the worked example 0.20 mm. The seat ring free length, being the axial length of the seat ring (30) unloaded, is from 2.5 mm to 4.0 mm; in some embodiments from 2.6 mm to 3.5 mm; in some embodiments from 2.8 mm to 3.2 mm; in the worked example 3.0 mm. The convolution amplitude is from 0.08 mm to 0.20 mm; in some embodiments from 0.08 mm to 0.16 mm; in some embodiments from 0.11 mm to 0.14 mm; in the worked example 0.12 mm. The seat ring (30) of the worked example is formed from tube stock of 2.7 mm outer diameter and 0.20 mm wall thickness, so that its seat ring outer diameter is nominally 2.7 mm. These dimensions are called out in FIG. 6A.

[0090] The purge gap opening, being the radial size of the purge gap (60) when the deflectable ring element is fully deflected in the purge state and called out in FIG. 6B, is from 0.10 mm to 0.25 mm; in some embodiments from 0.11 mm to 0.20 mm; in some embodiments from 0.13 mm to 0.17 mm; in the worked example 0.15 mm. The over-travel distance, being the axial distance the poppet (40) moves beyond the end of the normal stroke, is from 0.4 mm to 0.9 mm; in some embodiments from 0.4 mm to 0.65 mm; in some embodiments from 0.44 mm to 0.56 mm; in the worked example 0.5 mm, beyond a normal stroke of 0.6 mm. The crack pressure is from 0.8 bar to 1.5 bar; in some embodiments from 0.8 bar to 1.2 bar; in some embodiments from 0.91 bar to 1.09 bar; in the worked example 1.0 bar. The over-travel threshold is from 2.5 bar to 5.0 bar; in some embodiments from 2.75 bar to 4.25 bar; in some embodiments from 3.2 bar to 3.8 bar; in the worked example 3.5 bar. The over-travel threshold of the worked example was reached in every inflation of the bench test, in which a floor pump inflated the inflatable chamber to 6 bar; whether a given hand pump or compressed-gas inflation device reaches a given over-travel threshold depends on the pressure differential that device applies, and the over-travel threshold is chosen for the inflation devices with which the valve core is to be used.

[0091] Of these values, only those of the worked example were built and tested, and the over-travel distance and purge gap opening of the worked example are design values that were not measured directly during the bench test. The ranges correspond to the superelastic seat ring (30) with a convoluted wall (32). A person skilled in the art will adapt them to the stiffness and recovery characteristics of a resilient polymer seat ring, of a deflectable ring element of resilient metal, of a seat ring having another of the axial-to-radial conversion geometries described above, or of a separate wiper ring (132), and will scale the dimensions to the bore available in a larger valve core or in an inflation valve in which the deflectable ring element is carried directly by the valve stem (10).

#### One-piece seat ring, or fixed seat with a separate wiper ring

[0092] In the illustrated embodiment one part, the seat ring (30), performs both functions: its sealing edge (34) is the surface on which the sealing face (42) of the poppet (40) rests in the closed state, and its convoluted wall (32) is the deflectable ring element that the purge shoulder (44) deflects in over-travel. The seat ring (30) is held in the core body (20) and does not move bodily; the purge gap (60) opens by elastic deformation of its wall while the seat ring (30) remains seated against the internal shoulder (24). In this one-piece form the part that seals is also the part that wipes: the shape recovery of the seat ring (30) moves it across the sealing face (42) or an adjacent surface of the poppet (40), so that sealant film is removed from the sealing surfaces by the seat ring (30) itself, with no wiping part in addition to it. The one-piece form has the fewest parts and the shortest axial length, and the inspection of the worked example after forty inflation cycles found the sealing edge (34) and the sealing face (42) clean.

[0093] In an alternative embodiment, FIGS. 10A and 10B, sealing and deflection are performed by separate parts. A fixed seat (130), which does not deflect during over-travel, is carried by the core body (20) and provides the sealing edge (34) on which the sealing face (42) rests in the closed state; in the disclosed form the fixed seat (130) is of brass. A separate wiper ring (132), which is the deflectable ring element of this embodiment, is positioned on the chamber side of the fixed seat (130), so that the purge shoulder (44) reaches it only in over-travel. In over-travel the purge shoulder (44) deflects the wiper ring (132) radially outward, opening the purge gap (60), shown in FIG. 10B between the outer surface of the wiper ring (132) and the core body bore (22), and the air purge flows along the purge flow path (62). When the pressure differential falls the wiper ring (132) recovers its shape and the purge gap (60) closes. In the disclosed form the wiper ring (132) is a thin ring of stainless steel of spring temper. In other embodiments the wiper ring (132) is formed from any of the materials described above for the deflectable ring element, and it has a plain wall, a convoluted wall (32) or another of the axial-to-radial conversion geometries described above, or it is a split wiper ring as described above. Where the recovering wiper ring (132) moves across a surface of the poppet (40) it also provides a snap-back wipe; where it does not, this embodiment provides the air purge alone. The fixed seat and wiper ring embodiment has one more part and more axial length than the one-piece seat ring (30), and may be easier to manufacture; the form, thickness and retention of the wiper ring (132) follow from the material and geometry selected as described above.

[0094] Both forms are species of the same deflectable ring element: the seat ring (30) where the ring element also carries the sealing edge (34), and the wiper ring (132) where a fixed seat (130) carries the sealing edge (34). The description of materials, wall geometry, purge opening and dimensions above applies to both, and every reference herein to the deflectable ring element includes both unless the context excludes one. The parameter ranges given above were derived for the one-piece superelastic seat ring (30) and are adapted for the wiper ring (132) as stated.

#### Separate part, integral flexure section, or carried by the valve stem

[0095] In the illustrated embodiment the seat ring (30) is a part separate from the core body (20), received in the core body bore (22) and retained against the internal shoulder (24). The retention of a separate deflectable ring element in the core body (20), by the interference fit of the worked example or by the other forms of ring retention, is described below with the alternatives for the other parts.

[0096] In other embodiments the deflectable ring element is not a separate part but an integral flexure section of the core body (20): a thin-walled section of the core body (20), having a convoluted wall (32), a slotted wall (332) or another of the axial-to-radial conversion geometries described above, formed in one piece with the core body (20) by turning, moulding or pressing. There is then no separate seat ring (30) and no interference fit. The core body (20) is in that case formed from a material having the recoverable strain the section requires, such as a resilient polymer or stainless steel of spring temper; the free-machining brass of the illustrated core body (20) does not recover the strains involved and is not used for an integral flexure section. The functional definition of the deflectable ring element covers a ring element separate from the core body (20) and one integral with it.

[0097] In further embodiments the deflectable ring element is carried not by a removable core body (20) but directly by the valve stem (10) of the inflation valve, as the seat ring (730) of FIG. 15B, in an inflation valve having no separate valve core; the valve formats in which the mechanism may be used are described below.

#### Shape recovery

[0098] Shape recovery is the return of the deflectable ring element to its at-rest form when the pressure differential falls and the purge shoulder (44) withdraws, closing the purge gap (60); the snap-back wipe is the movement of the recovering ring element across a surface of the poppet (40) during that return. In the illustrated embodiment the shape recovery is the superelastic recovery of the NiTi seat ring (30): on unloading, the martensite formed under stress in the deflected wall reverts to austenite and the wall returns to its shape-set form, quickly and with force. In the resilient polymer seat ring (30) of FIG. 9 the shape recovery is the elastic recovery of the polymer, slower and with less force. In a deflectable ring element of resilient metal, including the stainless steel wiper ring (132), the shape recovery is the elastic recovery of the metal.

[0099] In some embodiments the shape recovery is assisted by the poppet (40) itself: a second formation of the poppet (40), on the side of the deflectable ring element opposite the purge shoulder (44), meets the ring element on the return movement of the poppet (40) and drives it back towards its at-rest form. Closing of the purge gap (60) then does not depend only on the material's own recovery, which guards against residual set of the ring element after many cycles and against loss of superelastic recovery when the ring element is chilled below its martensite start temperature, at the cost of additional contact and friction on the return.

[0100] Where a superelastic deflectable ring element has been chilled below its martensite start temperature while deflected, for example by the expansion of gas from a compressed-gas inflation device, and has not fully recovered on unloading, it recovers its shape when it is warmed again above its austenite finish temperature. This recovery on warming is a property of the alloy and is distinct from the thermally actuated purge described below, in which the purge gap (60) is deliberately opened by warming. The seat ring (30) of the illustrated embodiment is specified with an austenite finish temperature below 5 °C so that it is austenitic, and recovers superelastically, at ordinary riding temperatures without any warming. Whether chilling by a compressed-gas inflation device takes the seat ring (30) below its martensite start temperature was not tested.

[0101] The worked example completed forty inflation cycles without failure of the seat ring (30); its fatigue life beyond forty over-travel cycles was not tested. Under repeated radial deflection the strain in a convoluted wall (32) is concentrated at the roots of the convolutions. The fillet radius at the convolution root described above, and the use of two convolutions (32a, 32b) rather than one so that the radial deflection is shared between them, are design measures that may be used to reduce the strain at any one location.

#### Alternative locations of the purge gap

[0102] The purge gap (60) is defined herein by its function: it is a clearance bounded at least in part by a surface of the deflectable ring element, which is closed in the closed state and in the normal-open state, which is opened by radial deflection of the deflectable ring element in the purge state, and through which the air purge flows. The purge gap (60) is distinct from the main passage (64): the main passage (64) is opened by lifting of the sealing face (42) from the sealing edge (34) during the normal stroke, whereas the purge gap (60) remains closed throughout the normal stroke and opens only when the deflectable ring element is deflected. In the embodiment of FIG. 1 to FIG. 4 the purge gap (60) is located between the outer surface of the seat ring (30) and the core body bore (22). The surfaces that bound the purge gap (60), and the sense of the radial deflection that opens it, may however be chosen in any of the ways described in this section, each of which is a species of the same functional definition.

[0103] In a first arrangement the purge gap (60) is bounded by the outer surface of the seat ring (30) and the core body bore (22). Such a purge gap (60) opens where the bounding portion of the outer surface of the seat ring (30) moves away from the core body bore (22). That movement may be an inward movement of the bounding portion, produced for example by flattening of an outwardly convex convolution of the convoluted wall (32) under axial load from the purge shoulder (44), or by deepening of an inwardly concave convolution under the same load; or it may be the non-uniform deflection described below, in which some arcs of the seat ring (30) move outward while the intervening arcs move inward, so that the purge gap (60) opens over the inwardly moving arcs. Where the seat ring (30) is retained by an interference fit confined to an axial band at the internal shoulder (24), as described with reference to FIG. 6, the remainder of the outer surface is free of the core body bore (22) and is available to bound the purge gap (60).

[0104] In a second arrangement the purge gap (60) is bounded by the outer surface of the seat ring (30) and the stem bore (12), the wall of the core body (20) being provided with one or more windows at the axial position of the seat ring (30) through which the outer surface of the seat ring (30) is exposed to the stem bore (12). This arrangement requires the same movement of the outer surface as the first arrangement, and the windows in the core body (20) form part of the purge flow path (62).

[0105] In a third arrangement the purge gap (60) is bounded by the inner surface of the seat ring (30) and the poppet (40), on the chamber side of the sealing edge (34). Such a purge gap (60) is opened by outward radial deflection of the seat ring (30), and the air purge passes along the poppet stem (41), which is the capillary path along which liquid sealant is drawn into the valve core. In this arrangement the clearance between the inner surface of the seat ring (30) and the poppet (40) on the chamber side of the sealing edge (34) is closed, or is sufficiently small to carry no significant flow, in the closed state and the normal-open state, so that the purge gap (60) remains a flow path distinct from the main passage (64).

[0106] In a fourth arrangement the purge gap (60) is formed by one or more openings through the wall of the deflectable ring element. The openings may be slits or apertures cut through the wall of the seat ring (30), the axial slots between the fingers of a slotted wall (332), or the cells of a cellular wall (432), as described with reference to FIG. 12. The openings are closed in the closed state and the normal-open state, either because the strained wall holds them shut or because they lie against the core body bore (22), and they are opened or uncovered when the purge shoulder (44) strains the wall during over-travel. The openings are placed where the wall moves away from the surface that closes them.

[0107] Accordingly, the purge opening through which the air purge passes may be an annular gap between a surface of the deflectable ring element and an adjacent surface of the core body (20), the valve stem (10) or the poppet (40); one or more slits or apertures through the wall of the deflectable ring element; or one or more gaps between the fingers of a segmented deflectable ring element. The deflectable ring element may correspondingly be continuous around its circumference, segmented by slots that leave a continuous band at the sealing edge (34), or split by a single axial split. A split deflectable ring element, in which the split itself is the purge opening and opens circumferentially under a tapered purge shoulder (244), is used only as a wiper ring (132) together with a fixed seat (130), because a split through a seat ring (30) would interrupt the sealing edge (34).

#### Alternative purge flow paths

[0108] In the embodiment of FIG. 3 the purge flow path (62) runs from the supply side, through the purge gap (60), across the surfaces of the valve core on which sealant film accumulates, and into the inflatable chamber alongside the main passage (64). The purge flow path (62) may take any of the following alternative forms, in each of which it remains distinct from the main passage (64) and carries inflation gas in the inflation direction into the inflatable chamber.

[0109] As shown in FIG. 13A, the purge flow path (62) may include one or more purge ports (262) formed as radial holes or slots through the wall of the core body (20) on the chamber side of the purge gap (60). The purge ports (262) lead from the purge gap (60) to the clearance between the core body (20) and the stem bore (12), and thence into the inflatable chamber. The purge ports (262) fix the position at which the air purge, and the sealant film it carries, leave the valve core. Two or more purge ports (262) may be distributed around the circumference of the core body (20).

[0110] As shown in FIG. 13B, the purge flow path (62) may include one or more flutes (362) formed as axial grooves in the core body bore (22) at the axial position of the seat ring (30). In the closed state and the normal-open state the outer surface of the seat ring (30) lies on the lands between the flutes (362), closing them. When the bounding portion of the outer surface of the seat ring (30) moves away from the core body bore (22) in the purge state, the flutes (362) are placed in communication with the supply side and carry the air purge past the seat ring (30). The flutes (362) set the flow area of the purge flow path (62) independently of the size of the purge gap opening, so that the flow area can be chosen by the number, width and depth of the flutes (362) rather than by the radial deflection alone.

[0111] Where the purge gap (60) is formed by openings through the wall of the deflectable ring element, as described above with reference to the slotted wall (332) and the cellular wall (432), the purge flow path (62) passes through the wall of the deflectable ring element and then along the poppet stem (41) or the core body bore (22) into the inflatable chamber. The purge ports (262) and the flutes (362) may be combined with any of the locations of the purge gap (60) described in the preceding section, and with one another.

#### Alternative deflecting formations

[0112] The purge shoulder (44) is one species of a deflecting formation, which is any formation that moves with the poppet (40) and that contacts the deflectable ring element only during over-travel, so as to deflect it radially and open the purge gap (60). In every deflecting formation described here the same poppet (40) performs both ranges of movement: during the normal stroke the deflecting formation is spaced from the deflectable ring element and the main passage (64) is open, and during over-travel the same poppet (40) carries the deflecting formation against the deflectable ring element. There is no second valve member and no second seat to be fouled by sealant film. In the embodiment of FIG. 1 the deflecting formation is an annular purge shoulder (44) integral with the poppet (40), on the chamber side of the sealing face (42), which bears axially on the seat ring (30) during over-travel so that the convoluted wall (32) converts the axial load into radial deflection.

[0113] As shown in FIG. 11A, the deflecting formation may be a tapered purge shoulder (244) having a frustoconical flank on the poppet (40) that enters the seat ring (30) during over-travel and deflects the seat ring (30) radially outward by direct radial contact, in the manner in which a mandrel expands a ring. Because the load applied by the tapered purge shoulder (244) is radial rather than axial, the seat ring (30) need not have an axial-to-radial conversion geometry, and a seat ring (30) with a plain cylindrical wall may be used with the tapered purge shoulder (244). The flank of the tapered purge shoulder (244) slides on the inner surface of the seat ring (30) during over-travel and during the return, and thereby also wipes that inner surface. The tapered purge shoulder (244) may equally be a taper on the poppet stem (41).

[0114] As shown in FIG. 11B, the deflecting formation may be provided as two or more discrete lugs (344) on the poppet (40), for example two to four discrete lugs (344) spaced around its circumference, in place of a continuous annular shoulder. The discrete lugs (344) load the deflectable ring element at discrete points, so that the ring ovalises, moving outward at the loaded points and inward between them, and the purge gap (60) opens over arcs of the circumference rather than all round. Less force is needed to deflect the deflectable ring element by discrete lugs (344) than by a continuous annular shoulder, and the purge flow is correspondingly non-uniform around the circumference.

[0115] As shown in FIG. 11C, the deflecting formation may be a separate collar (444) fixed on the poppet stem (41), for example pressed, crimped or threaded onto it. The separate collar (444) performs the function of the purge shoulder (44) and allows the material that contacts the deflectable ring element to be chosen independently of the material of the poppet (40); for example a separate collar (444) of stainless steel may be fitted to a poppet (40) of brass.

[0116] In further embodiments the deflecting formation is a return-spring retainer that seats the return spring (50) on the poppet (40) and that bears on the chamber-side end of the seat ring (30) during over-travel, so that one part both retains the return spring (50) and deflects the seat ring (30); the contact with the seat ring (30) is then at the end of the seat ring (30) remote from the sealing edge (34). In other embodiments the deflecting formation is carried on a purge sleeve that slides on the poppet stem (41): the purge sleeve travels with the poppet (40) during the normal stroke and is driven onto the seat ring (30) only during over-travel, the sealing face (42) remaining on the poppet (40) itself. In other embodiments the deflecting formation is the sealing face (42) itself, or a continuation of the sealing face (42), which seals on the sealing edge (34) in the closed state and, when driven further during over-travel, forces the sealing edge (34) to deflect radially.

[0117] The deflectable ring element and the deflecting formation may also be exchanged between the poppet (40) and the core body (20). In such an inverted arrangement the deflectable ring element is a thin skirt carried by the poppet (40), a fixed formation in the core body (20) deflects the skirt during over-travel to open the purge gap (60), and on shape recovery the skirt moves across the core body bore (22). The arrangement of FIG. 1 to FIG. 4, in which the deflectable ring element is held in the core body (20) and the deflecting formation moves with the poppet (40), is preferred because the shape recovery of the held seat ring (30) then moves the seat ring (30) across the sealing face (42), which is the surface that seals and the surface on which sealant film matters, and because the wiping element is the seat itself, so that no separate wiping part is added that could itself be fouled.

#### Alternative threshold-setting arrangements

[0118] The second spring stage (54) of the return spring (50) is one species of a threshold-setting arrangement, which is any arrangement by which the force resisting movement of the poppet (40) rises at the end of the normal stroke, so that the pressure differential must exceed an over-travel threshold, higher than the crack pressure, before the poppet (40) enters over-travel. The over-travel threshold is what allows the valve core to inflate and to seal in the same way as a conventional valve core until the purge state is reached: below the over-travel threshold only the main passage (64) is open and the deflectable ring element is not touched. The threshold-setting arrangement may be provided in any of the following ways, and in each of them the over-travel threshold is set as a relationship to the crack pressure and to the pressure that the inflation device supplies, rather than by any one spring construction.

[0119] In the embodiment of FIG. 1 the return spring (50) is a compression spring having a first spring stage (52) of lower rate, which resists the normal stroke and sets the crack pressure, and a second spring stage (54) of higher rate, which the pressure differential must overcome to produce over-travel and which sets the over-travel threshold. In one construction of such a return spring (50) the coils are of variable pitch, and the close-pitched section becomes solid at the end of the normal stroke, leaving fewer active coils and so a higher rate for the second spring stage (54).

[0120] As shown in FIG. 14A, the threshold-setting arrangement may comprise an auxiliary spring (254) in addition to the return spring (50). The return spring (50) then acts alone over the normal stroke as the first spring stage (52), and the auxiliary spring (254) is engaged only when a lost-motion clearance between the auxiliary spring (254) and the poppet (40) closes at the end of the normal stroke, after which the auxiliary spring (254) acts in parallel with the return spring (50). The two stages can then be tuned independently, and the lost-motion clearance is a feature that can be seen and measured on the assembled valve core. The auxiliary spring (254) may be a compression spring of wire, a stack of one or more conical disc springs, which gives a high force in a short axial length, or an annular compression bush of an engineering polymer.

[0121] As shown in FIG. 14B, the threshold-setting arrangement may comprise a detent (354) that holds the poppet (40) at the end of the normal stroke until the force on the poppet (40) exceeds a breakaway value. The detent (354) may be a spring-loaded ball, or a radially sprung element, carried in the core body (20) and engaging a circumferential groove on the poppet stem (41) at the end of the normal stroke; or it may be a permanent magnet carried in the core body (20) that attracts a ferromagnetic target, for example of ferritic stainless steel, carried on the poppet (40). After breakaway the resisting force falls, so that the poppet (40) passes through over-travel quickly, and the detent (354) releases on the return so that the poppet (40) can close. The magnetic form of the detent (354) has no sliding contact exposed to liquid sealant.

[0122] The threshold-setting arrangement may also be provided by the stiffness of the deflectable ring element itself, with a return spring (50) of a single rate. The over-travel threshold is then set by the force that the deflecting formation needs to deflect the deflectable ring element. Where the deflectable ring element is formed from a superelastic alloy, its loading follows a stress plateau after an initial elastic rise, so that the force needed to deflect it behaves as a threshold; the over-travel threshold set in this way depends on the dimensions of the deflectable ring element and on temperature. A deflectable ring element of a resilient polymer or of a resilient metal without a phase transformation has no such plateau, and the over-travel threshold set by its stiffness alone is less distinct. In any of the arrangements described in this section the return spring (50) and the deflectable ring element may each contribute to the over-travel threshold.

[0123] In a further arrangement the deflecting formation is carried not by the poppet (40) but by a separate purge actuator, for example an annular piston or a flexible diaphragm housed in the core body (20), exposed on its supply side to the supply-side pressure and biased by its own compression spring. The purge actuator advances only when the pressure differential exceeds the over-travel threshold, carries the deflecting formation onto the deflectable ring element, and thereby opens the purge gap (60) while inflation gas is flowing, the poppet (40) performing only its normal stroke. The purge actuator adds a part and a sliding seal exposed to liquid sealant, and it is more readily accommodated in valve cores of larger bore, such as a Schrader-pattern valve core, than in a Presta-pattern valve core.

#### Alternative wiping arrangements

[0124] The snap-back wipe is the movement of the deflectable ring element across a surface of the poppet (40) as the deflectable ring element undergoes shape recovery when the pressure differential falls, by which movement partially cured sealant film is sheared from that surface. The snap-back wipe is defined by that movement and not by its speed or force. In the embodiment of FIG. 4 the recovering seat ring (30) moves across the sealing face (42), or across a surface of the poppet (40) adjacent to the sealing face (42). Shape recovery of a superelastic alloy is preferred because it is rapid and exerts a higher force, and so gives a stronger snap-back wipe; a seat ring (30) of a resilient polymer recovers more slowly and with less force, so that its snap-back wipe is weaker, but that movement is a snap-back wipe within the meaning used here, and the air purge provides a cleaning action independently of it.

[0125] In embodiments having a fixed seat (130) and a wiper ring (132), as shown in FIG. 10, the wiper ring (132) is deflected outward by the purge shoulder (44) during over-travel and undergoes shape recovery when the pressure differential falls. The wiper ring (132) may then perform the snap-back wipe on a surface of the poppet (40) in the same manner as the seat ring (30), while the fixed seat (130) performs the sealing function.

[0126] A mechanical wipe may additionally be provided by a structure that does not depend on shape recovery, in combination with the recovering deflectable ring element. In one such embodiment a fixed wiping land is formed as a close-clearance land in the core body bore (22), or on the fixed seat (130), through which the poppet (40) passes on every stroke, so that the relative axial movement between the poppet (40) and the fixed wiping land shears sealant film from the poppet (40); the deflection of the deflectable ring element then opens the purge gap (60) and the fixed wiping land supplements the snap-back wipe. In another embodiment a rotational wipe is provided by a helical guide between the poppet stem (41) and the core body (20), which turns the poppet (40) through a small angle during over-travel and back again on the return, so that the sealing face (42) rubs circumferentially across the sealing edge (34) in addition to the snap-back wipe.

[0127] The seat ring (30) may be provided with a defined wiping edge at its inner surface, being a sharp-cornered edge set by the cut profile of the seat ring (30) and preserved by limiting the extent of electropolishing, which is presented to the poppet (40) as the seat ring (30) recovers. The defined wiping edge concentrates the contact pressure so that the recovering seat ring (30) shears the sealant film rather than riding over it. The cleaning action of the valve core may be provided by the air purge, by the snap-back wipe, or by both, as described in relation to the operation of the valve core.

#### Alternative sealing faces

[0128] In the embodiment of FIG. 1 the sealing face (42) is a conical surface of the poppet (40) of brass, which seats on the sealing edge (34) of the seat ring (30) with metal-to-metal contact and without an elastomer. The sealing face (42) is one species of a sealing surface of the poppet (40), which may take any of the following alternative forms. The sealing face (42) may be part-spherical, giving line contact on the sealing edge (34) that tolerates misalignment of the poppet (40). The sealing face (42) may be a flat surface that bears on the axial end of the seat ring (30); such a flat sealing face (42) is less self-centring, and sealant film on the sealing surfaces has a greater effect on it.

[0129] The sealing face (42) may be of hard-anodised aluminium, the poppet (40) or a facing of the poppet (40) being of aluminium with a hard-anodised surface; a hard-anodised aluminium sealing face (42), or another wear-resistant finish of the sealing face (42), may be used where wear of the sealing face (42) from repeated metal-to-metal contact with the sealing edge (34) over the service life of the valve core is to be reduced. The sealing face (42) may be a polymer facing on the poppet (40), for example of PEEK, bearing on a metal sealing edge (34). The sealing face (42) may carry a hard low-adhesion coating, for example of electroless nickel or diamond-like carbon. A low-adhesion coating used alone only slows the build-up of sealant film and does not remove a film once formed; in the valve core described here such a coating is used together with the air purge and the snap-back wipe, which remove the film, so that the coating reduces the adhesion of what the cleaning action has to remove.

#### Materials of the core body

[0130] In the embodiment of FIG. 1 the core body (20) and the valve stem (10) are turned from free-machining brass CW614N, and the poppet (40) is of brass. The core body (20) may instead be formed from a corrosion-resistant material, and in particular from stainless steel, for example stainless steel 303, for corrosion resistance where the liquid sealant carried in the inflatable chamber contains ammonia. The choice of a stainless steel core body (20) is independent of the material and form of the deflectable ring element: a stainless steel core body (20) may be used with a seat ring (30) of a superelastic alloy, with a seat ring (30) of a resilient polymer, or with a wiper ring (132) used together with a fixed seat (130). The valve stem (10) and the poppet (40) may likewise be of stainless steel.

[0131] The core body (20) may also be formed from an engineering polymer, for example by injection moulding, in place of a metal. Where the core body (20) is of a resilient polymer or of spring-temper stainless steel, the deflectable ring element may be formed integrally with the core body (20) as a thin-walled flexure section, as described in relation to the deflectable ring element; a core body (20) of brass CW614N is not suitable for an integral deflectable ring element because the elastic strain that brass can recover is too small for the radial deflection required.

#### Retention of the deflectable ring element

[0132] In the embodiment of FIG. 1 and FIG. 8C the seat ring (30) is retained in the core body (20) by an interference fit of approximately 0.03 mm on diameter, and is seated axially against the internal shoulder (24). The interference fit is one species of ring retention, which is any means by which the deflectable ring element is held in the core body (20), or in the valve stem (10), against the internal shoulder (24) or an equivalent locating formation, so that the position of the sealing edge (34) is fixed while the portion of the deflectable ring element that undergoes radial deflection remains free to deflect. Whichever ring retention is used, it leaves that portion free.

[0133] The interference fit may be confined to an axial band of the seat ring (30) at the internal shoulder (24), the remainder of the outer surface of the seat ring (30) being free of the core body bore (22), as described with reference to FIG. 6. As shown in FIG. 8D, the seat ring (30) may instead be retained by a crimped lip (224) formed on the core body (20) and rolled or swaged over the end of the seat ring (30) remote from the internal shoulder (24); the crimped lip (224) retains the seat ring (30) axially and frees its outer surface from radial interference. As shown in FIG. 8E, the seat ring (30) may be retained by a retaining sleeve (324) pressed or threaded into the core body (20) and clamping the seat ring (30) against the internal shoulder (24), with the same freeing of the outer surface at the cost of one further part.

[0134] The deflectable ring element may also be retained by an adhesive bond, using an adhesive resistant to the liquid sealant and in particular to ammonia; by staking of the core body (20) over the deflectable ring element; by laser welding of the deflectable ring element to the core body (20); by over-moulding of a polymer core body (20) around the deflectable ring element; or by clamping of the deflectable ring element between two parts of the core body (20). The deflectable ring element may be formed integrally with the core body (20), in which case no separate ring retention is needed, or may be carried by the valve stem (10) rather than by the core body (20), as described in relation to the deflectable ring element and in the section on valve formats below.

[0135] Any of the ring retention means described here may be combined with one another. In some embodiments an interference fit is combined with a supplementary retention feature, for example an adhesive bond, a crimped lip (224) or a groove in the core body bore (22) into which the deflectable ring element snaps, so that the deflectable ring element cannot rotate or migrate axially in the core body bore (22), and cannot come free into the inflatable chamber, if the interference fit relaxes with repeated thermal cycling or vibration.

#### Valve formats and systems

[0136] The valve core is described above as a Presta-pattern valve core, whose core body (20) is threaded into the stem bore (12) of a Presta-pattern valve stem (10) of 6 mm outer diameter. The Presta-pattern valve core is the worked example and not a limitation: the operation of the deflectable ring element, the deflecting formation, the threshold-setting arrangement and the purge gap (60) does not depend on the thread by which the core body (20) is received, on the outer diameter of the valve stem (10), or on the Presta pattern. The same mechanism may be built into a valve core of another pattern, and into an inflation valve that has no removable valve core.

[0137] As shown schematically in FIG. 15A, the mechanism may be provided in a Schrader-pattern valve core, having a Schrader-pattern core body (620) and a Schrader-pattern poppet (630) which carry the seat ring (30), the purge shoulder (44) and the purge gap (60) in the same relationship as in FIG. 1 to FIG. 4. The larger bore of a Schrader-pattern valve core provides more room for the components of the mechanism, and in particular for a separate purge actuator as described above; and in a Schrader-pattern valve core the Schrader-pattern poppet (630) may be depressed by the head of the inflation device, which is one of the ways of producing over-travel described in relation to the operation of the valve core. The mechanism may likewise be provided in a Dunlop-pattern valve core.

[0138] As shown schematically in FIG. 15B, the mechanism may be provided in a non-removable inflation valve, in which the valve stem (10) directly carries a seat ring (730), together with the poppet (40) and the return spring (50), and there is no separate core body (20). The valve stem (10) then performs the functions that the core body (20) performs in the removable valve core, providing the locating formation against which the seat ring (730) is retained and the bore in which the poppet (40) is guided. Any of the ring retention means described above may be used to retain the seat ring (730) in the valve stem (10). The non-removable inflation valve is suited in particular to inflation valves fitted as original equipment to tubeless bicycle tyre set-ups.

[0139] An inflation valve according to this description comprises the valve stem (10) and, where the valve core is removable, the valve core received in the stem bore (12). The inflation valve may be fitted to a bicycle inner tube or to a tubeless bicycle tyre set-up, and the inflatable chamber so formed, holding liquid sealant, together with the inflation valve, forms a further aspect of this description; so do a wheel and a bicycle incorporating such an inflatable chamber and inflation valve. The mechanism is described with reference to inflation valves for bicycle inflatable chambers that hold liquid sealant, which is the application that has been built and tested; the same mechanism may be applied to inflation valves for other inflatable chambers that hold liquid sealant, and to other fluid valves in which a deposit forms on the sealing surfaces and is removed by a purge flow and by the recovery of a deflectable ring element.

#### Component and kit supply

[0140] The valve core is a unit that is separable from the valve stem (10), and it may be supplied as a replacement valve core for fitting into the stem bore (12) of an existing valve stem (10) in place of a conventional valve core, so that an inflatable chamber already fitted with a conventional inflation valve is given the cleaning action described here without replacement of the valve stem (10). The replacement valve core may be supplied singly or in a multipack, and may have a seat ring (30) of a superelastic alloy, a seat ring (30) of a resilient polymer, or a fixed seat (130) with a wiper ring (132).

[0141] The seat ring (30) may also be supplied as a component on its own, for fitting into a core body (20). The seat ring (30) may further be supplied as a kit together with a poppet (40) having a sealing face (42) and a purge shoulder (44), and a return spring (50) having a first spring stage (52) and a second spring stage (54), for fitting into a core body (20) supplied separately, as indicated in FIG. 5. In such a kit the seat ring (30), the poppet (40) and the return spring (50) are matched so that, when assembled into the core body (20), the purge shoulder (44) is spaced from the seat ring (30) throughout the normal stroke and bears on the seat ring (30) only in over-travel, and the purge gap (60) is closed in the closed state and the normal-open state.

#### Thermally actuated purge

[0142] As a separate concept, the purge gap (60) may be opened by warming the deflectable ring element rather than by over-travel. In such an embodiment the deflectable ring element is formed from a two-way shape-memory alloy of nickel and titanium having an austenite finish temperature of about 35 °C to 40 °C, so that the deflectable ring element changes shape and opens the purge gap (60) when it is warmed above that temperature, for example by hand, and closes the purge gap (60) when it cools again. This thermally actuated purge allows the purge gap (60) to be opened without an inflation device, for a manual purge, and is described here as a concept distinct from the over-travel-actuated purge state of the embodiments described above; it has not been built or tested.

#### Combinations of the features described

[0143] The features described in this section and in the preceding sections on the deflectable ring element may be combined with one another and with each of the three principal embodiments described in the examples, namely the embodiment in which the deflectable ring element is a seat ring (30) formed from a superelastic alloy, the embodiment in which the deflectable ring element is a seat ring (30) formed from a resilient polymer, and the embodiment in which the deflectable ring element is a wiper ring (132) used together with a fixed seat (130). Each of the alternative locations of the purge gap (60), the alternative purge flow paths (62), the alternative deflecting formations, the alternative threshold-setting arrangements, the alternative wiping arrangements, the alternative sealing faces (42), the alternative materials of the core body (20), the alternative ring retention means and the alternative valve formats described above is disclosed in combination with each of the others and with each of the three principal embodiments, except where this description states an incompatibility or a dependency.

[0144] The stated incompatibilities and dependencies are these. Electropolishing is a finishing process for a metal deflectable ring element and does not apply to a deflectable ring element of a resilient polymer. An austenite finish temperature is a property of a superelastic alloy: where the deflectable ring element is formed from a superelastic alloy, the alloy is selected to have an austenite finish temperature below a threshold, such as 5 °C, so that the deflectable ring element remains superelastic across the intended range of ambient temperatures; no austenite finish temperature applies to a deflectable ring element of a resilient polymer, or to a wiper ring (132) of a resilient metal that is not a superelastic alloy. A split deflectable ring element is used only as a wiper ring (132) with a fixed seat (130). A seat ring (30) with a plain cylindrical wall is used with a tapered purge shoulder (244) or another deflecting formation that applies a radial load. An integral deflectable ring element requires a core body (20) of a resilient polymer or of spring-temper stainless steel. A separate purge actuator is more readily accommodated in a valve core of larger bore than the Presta-pattern valve core.

[0145] In some embodiments, therefore, the deflectable ring element is a seat ring (30) formed from a superelastic alloy, such as an alloy of nickel and titanium, having an austenite finish temperature below 5 °C; in other embodiments the deflectable ring element is a seat ring (30) formed from a resilient polymer, such as PEEK; and in other embodiments the deflectable ring element is a wiper ring (132) separate from a fixed seat (130). The core body (20) may be formed from a corrosion-resistant material, such as stainless steel, independently of which of these forms the deflectable ring element takes. The convoluted wall (32) described for converting axial load into radial deflection may be applied to a seat ring (30) that also performs the sealing function or, in embodiments having a separate fixed seat (130), may be applied to a wiper ring (132) that performs the purging and wiping function without also sealing. A lock nut (70) for holding the poppet (40) in the closed state by hand may be combined with any of these embodiments.

[0146] In embodiments in which the deflectable ring element is formed from a resilient polymer, such as PEEK, the shape recovery on release of the pressure differential may be slower, and the resulting snap-back wipe weaker, than in embodiments in which the deflectable ring element is formed from a superelastic alloy; the purge gap (60) and the air purge nonetheless provide a cleaning action independently of the snap-back wipe. The dimensions and pressure values given in the examples correspond to the embodiment in which the seat ring (30) is formed from a superelastic alloy; a person skilled in the art will adapt them to the stiffness and recovery characteristics of a seat ring (30) of a resilient polymer or of a wiper ring (132) used with a fixed seat (130), and likewise to the alternative deflecting formations, threshold-setting arrangements and valve formats described in this section.

#### Manufacture of the seat ring

[0147] In the illustrated embodiment the seat ring (30) is made from tube stock of a superelastic alloy, NiTi of nominally 55.8 wt% nickel content, having an outer diameter of 2.7 mm and a wall of 0.20 mm. As shown in FIG. 8A, the tube stock is mounted on a mandrel and the profile of the seat ring is cut from it by laser cutting. The convoluted wall (32) may be defined by the laser-cut profile, by forming on the mandrel, by the shape-setting fixture described below, or by a combination of these steps; the disclosure of the convoluted wall does not depend on which of these steps imparts the convolution, provided that the finished seat ring has the convoluted wall and the sealing edge (34) described above.

[0148] As shown in FIG. 8B, the cut seat ring (30) is then subjected to shape-setting: it is held in a fixture that constrains the convoluted wall (32) to its intended wave geometry and is heated, in the illustrated embodiment at 500 °C for 10 minutes, and then water-quenched. Shape-setting fixes the at-rest geometry of the seat ring, which is the geometry to which the seat ring returns by shape recovery when the pressure differential falls. Shape-setting time and temperature, together with the nickel content, also determine the transformation temperatures of the superelastic alloy. In the illustrated embodiment the seat ring is specified to have an austenite finish temperature below 5 °C, so that it is fully austenitic and behaves superelastically at ordinary riding temperatures. The values of 500 °C and 10 minutes are those used for the prototype seat rings of Example 1; in some embodiments the shape-setting temperature and time are selected so as to hold the austenite finish temperature of production seat rings below the specified value, and in some embodiments the austenite finish temperature is verified on sampled seat rings after shape-setting.

[0149] After shape-setting, the seat ring (30) is electropolished to remove the surface oxide and the heat-affected edge left by laser cutting. The seat ring wall thickness after electropolishing lies within the range stated for the seat ring wall thickness, and in some embodiments the seat ring wall thickness is checked after electropolishing, because electropolishing removes material from the whole surface including the root of each convolution of the convoluted wall (32). In other embodiments the seat ring is finished by mechanical or chemical polishing in place of electropolishing. In some embodiments the depth of electropolishing is limited at the inner surface of the seat ring so as to preserve a defined wiping edge, formed by the laser-cut profile, that is presented to the poppet (40) during the snap-back wipe; electropolishing rounds edges, and a limited depth of electropolishing retains the sharper edge while still removing the oxide.

#### Alternative forming routes

[0150] The laser-cutting, shape-setting and electropolishing route is the route by which the seat rings (30) of Example 1 were made. The seat ring is not limited to that route, and any route that yields a deflectable ring element having the sealing edge (34), the convoluted wall (32) or another axial-to-radial conversion geometry, and the at-rest geometry described herein may be used. In some embodiments the convoluted wall of a seat ring of superelastic alloy is formed by roll-forming with profiled rollers, in stages, with shape-setting between the stages. In some embodiments the convoluted wall is formed by internal pressure in a split die; this route is more readily applied to a seat ring of stainless steel than to one of superelastic alloy at room temperature. In embodiments in which the seat ring is formed from a resilient polymer, such as PEEK, the seat ring may be injection moulded, and the shape-setting and electropolishing steps described above do not apply. In embodiments having a fixed seat (130) and a separate wiper ring (132), the wiper ring may be stamped or deep drawn from strip, as may a deflectable ring element in the form of a conical annular disc. A slotted wall (332) or a cellular wall (432) may be produced by laser cutting from tube stock as described above, or by photochemical etching of flat sheet followed by rolling and joining; the joined seam is a site of reduced fatigue life in a superelastic alloy, and for that material laser cutting from tube stock is preferred. None of the alternative forming routes of this section has been practised for the valve core described herein; they are described so that the seat ring is not limited to the route by which the prototype seat rings were made.

#### Assembly of the valve core

[0151] The core body (20) and the poppet (40) of the illustrated embodiment are turned from bar by ordinary machining, with no special process. As shown in FIG. 8C, the seat ring (30) is pressed into the core body bore (22) until it seats against the internal shoulder (24), with an interference fit of approximately 0.03 mm on diameter. The interference fit retains the seat ring axially against the internal shoulder and rotationally in the core body. As described above in connection with the closed state, in some embodiments the interference fit is confined to an axial band of the seat ring adjacent the internal shoulder, the remainder of the outer surface of the seat ring being free of the core body bore.

[0152] In other embodiments the seat ring (30) is retained in the core body (20) by ring retention other than, or in addition to, the interference fit. As shown in FIG. 8D, a crimped lip (224) of the core body may be rolled or swaged over the end of the seat ring remote from the internal shoulder (24). As shown in FIG. 8E, a retaining sleeve (324) pressed or threaded into the core body may clamp the seat ring against the internal shoulder. Each of these frees the outer surface of the seat ring from radial interference along its length. Further ring retention species, and their combination with the interference fit as supplementary retention, are described above in connection with the alternatives. In some embodiments the assembly step includes a check of the press-in force, or of the press-in travel, of the seat ring, so that a seat ring pressed with an interference at the tight end of the manufacturing tolerance is detected before it is assembled into a valve core in which the interference could suppress the radial deflection of the seat ring.

[0153] With the seat ring (30) retained, the poppet (40) is inserted so that its poppet stem (41) is guided by the core body (20) and its sealing face (42) rests on the sealing edge (34) of the seat ring, the return spring (50) is fitted so that its first spring stage (52) biases the poppet towards the closed state, and the lock nut (70) is fitted. The assembled valve core is threaded into the stem bore (12) of the valve stem (10). Where the valve core is supplied as a replacement valve core, this last step is performed by the user on an existing valve stem. Where the seat ring, or the seat ring with the poppet and the return spring, is supplied as a kit, the remaining assembly steps are performed by the recipient.

#### Examples

[0154] Example 1 and Comparative Example 1 report a bench test that was actually performed; every value in them is a measured or as-used value from that test. Examples 2, 3 and 4 are prophetic examples: they describe embodiments that have been conceived but not built or tested, they are written in the present or conditional tense, and no result is reported for them.

#### Example 1 (actual): superelastic seat ring embodiment

[0155] Three valve cores, designated P-1, P-2 and P-3, were built to the illustrated embodiment. Each comprised a core body (20) and valve stem (10) of free-machining brass CW614N, the valve stem being a Presta-pattern valve stem of 6 mm outer diameter; a seat ring (30) of superelastic alloy, NiTi of nominally 55.8 wt% nickel content, specified to have an austenite finish temperature below 5 °C, with a convoluted wall (32) and a sealing edge (34); a poppet (40) of brass with a conical sealing face (42) seating metal to metal on the sealing edge, and a purge shoulder (44) on the chamber side of the sealing face; a return spring (50) of stainless steel music wire having a first spring stage (52) and a second spring stage (54); a purge gap (60) closed in the closed state; and a lock nut (70).

[0156] The seat rings (30) of Example 1 had a seat ring inner diameter of 2.3 mm, a seat ring wall thickness of 0.20 mm, a seat ring free length of 3.0 mm and a convolution amplitude of 0.12 mm, and were made from tube stock of 2.7 mm outer diameter and 0.20 mm wall by the laser-cutting, shape-setting and electropolishing route described above, and were pressed into the core body (20) against the internal shoulder (24) with an interference fit of approximately 0.03 mm on diameter. The valve cores of Example 1 had a crack pressure of 1.0 bar, a normal stroke of 0.6 mm, an over-travel threshold of 3.5 bar, an over-travel distance of 0.5 mm and a purge gap opening of 0.15 mm radial. The crack pressure, normal stroke, over-travel threshold, over-travel distance and purge gap opening are the design values of the prototype valve cores; the over-travel distance and the purge gap opening were not measured during the bench test.

[0157] The bench test was run from 12 August 2026 to 20 August 2026. Each valve core of Example 1, and each conventional valve core of Comparative Example 1, was fitted to an identical inflatable chamber, a 700×28 bicycle inner tube, charged with 60 ml of liquid sealant, a latex emulsion containing ammonia and suspended particles. Each inflation cycle consisted of an inflation event in which the inflatable chamber was inflated from fully deflated to 6 bar with the same inflation device, a floor pump, by the same operator; a hold of 24 hours at 22 °C; and full deflation through the inflation valve. The inflation time was measured from coupling of the inflation device to the supply side until the inflatable chamber reached 6 bar. Leak-down was measured over each 24-hour hold. A valve core was recorded as failed at the first inflation cycle at which its leak-down exceeded 0.5 bar in 24 hours, or at which the inflation device failed to open the valve within 5 seconds of engagement, the latter being recorded as blockage.

[0158] Each of the valve cores P-1, P-2 and P-3 completed 40 inflation cycles without failure, at which point the test was stopped. The inflation time of P-1 was 43 s at inflation cycle 1 and 47 s at inflation cycle 40; that of P-2 was 41 s at inflation cycle 1 and 46 s at inflation cycle 40; and that of P-3 was 44 s at inflation cycle 1 and 50 s at inflation cycle 40. The leak-down at inflation cycle 40 was 0.1 bar in 24 hours for P-1, 0.1 bar in 24 hours for P-2 and 0.2 bar in 24 hours for P-3. On every inflation event of every valve core of Example 1, an audible snap was heard on removal of the inflation device. The audible snap indicates that a shape recovery event of the seat ring (30) occurred on removal of the inflation device at these test conditions; it is not a measurement of the over-travel distance, of the purge gap opening, or of the extent of the snap-back wipe.

[0159] After inflation cycle 40 the valve cores P-1, P-2 and P-3 were removed and inspected under a stereo microscope. In each, the sealing edge (34) of the seat ring (30) and the sealing face (42) of the poppet (40) were clean of sealant film. Cured sealant film was present on the outer surface of the seat ring in the region of the purge gap (60). The bench test did not include fatigue testing of the seat ring beyond the 40 inflation cycles, did not include testing at temperatures other than 22 °C, did not include cold-shock testing such as would occur with a compressed-CO2 inflation device, and did not separate the contribution of the air purge from that of the snap-back wipe.

#### Comparative Example 1 (actual): conventional valve core

[0160] Three conventional valve cores, designated C-1, C-2 and C-3, all commercial Presta-pattern valve cores of one manufacturer's standard type and lacking a deflectable ring element and a purge gap, were tested under the protocol of Example 1 on identical inflatable chambers with the same liquid sealant. C-1 failed by blockage at inflation cycle 14, its inflation time having risen from 41 s at inflation cycle 1 to 68 s at inflation cycle 13. C-2 failed by leak-down of 0.7 bar in 24 hours at inflation cycle 12, its inflation time having risen from 40 s at inflation cycle 1 to 44 s at inflation cycle 11. C-3 failed by blockage at inflation cycle 18, its inflation time having risen from 42 s at inflation cycle 1 to 75 s at inflation cycle 17. The conventional valve cores thus exhibited both of the failure modes described in the background, leak-down and blockage, between inflation cycles 12 and 18.

#### Example 2 (prophetic): resilient polymer seat ring embodiment

[0161] In this prophetic example the valve core of Example 1 is built with a seat ring (30) formed from a resilient polymer, PEEK, in place of the superelastic alloy, the seat ring having the same convoluted wall (32) and sealing edge (34), and the core body (20), poppet (40) with sealing face (42) and purge shoulder (44), return spring (50), purge gap (60) and lock nut (70) being as in Example 1. The seat ring of this example would be made by a route suited to the polymer, such as injection moulding, without the shape-setting and electropolishing steps of Example 1. On over-travel the purge shoulder would deflect the seat ring radially and open the purge gap, so that the air purge would operate as in Example 1. On removal of the inflation device the shape recovery of the polymer seat ring would be slower, and its recovery force lower, than the superelastic recovery of the seat ring of Example 1, so that the snap-back wipe would be weaker; the air purge would provide cleaning action independently of the snap-back wipe. The dimensions and the pressure values of Example 1 correspond to the stiffness and recovery characteristics of the superelastic alloy, and the person skilled in the art would adapt them to those of the resilient polymer. No inflation cycle, leak-down or inflation time result exists for this example.

#### Example 3 (prophetic): fixed seat and wiper ring embodiment

[0162] In this prophetic example, shown in FIG. 10A and FIG. 10B, the valve core comprises a core body (20) and valve stem (10) as in Example 1, a rigid fixed seat (130) of brass on which the sealing face (42) of the poppet (40) seats in the closed state, and a separate wiper ring (132) of stainless spring steel positioned on the chamber side of the fixed seat. The poppet, return spring (50) and lock nut (70) are as in Example 1. At and above the crack pressure the poppet would lift its sealing face from the fixed seat by the normal stroke, with the purge gap (60) closed. Above the over-travel threshold the purge shoulder (44) would deflect the wiper ring radially outward, opening the purge gap between the outer surface of the wiper ring and the core body bore (22), and the air purge would flow along the purge flow path (62) into the inflatable chamber. On removal of the inflation device the wiper ring would undergo shape recovery and the purge gap would close. This embodiment separates the sealing function, performed by the fixed seat, from the purging function and any wiping function, performed by the wiper ring, at the cost of one more part and greater axial length than Example 1. No result exists for this example.

#### Example 4 (prophetic): corrosion-resistant core body and wear-resistant sealing face

[0163] In this prophetic example the valve core of Example 1, Example 2 or Example 3 is built with a core body (20) of stainless steel 303 in place of brass CW614N, for corrosion resistance in service with a liquid sealant containing ammonia. A core body of stainless steel 303 has been machined; the bench test of Example 1 was performed with core bodies of brass only, and no result exists for a valve core having a core body of stainless steel 303. Independently of the core body material, in this prophetic example the poppet (40) carries a sealing face (42) of hard-anodised aluminium in place of the brass sealing face of Example 1, as a wear-resistant sealing face for repeated metal-to-metal seating on the sealing edge (34) of the seat ring (30) or on the fixed seat (130). The hard-anodised aluminium sealing face has been considered but not built. No result exists for either variant.

#### Data and results

[0164] The results of Example 1 and Comparative Example 1 are summarised in the following table. In the table, "censored" means that the test was stopped at inflation cycle 40 without failure of the valve core, so that the number of inflation cycles to failure is not known and is greater than 40.

| Valve core | Type | Inflation cycles completed without failure | Failure mode | Inflation time at inflation cycle 1 (s) | Inflation time at last inflation cycle (s) | Leak-down at last inflation cycle (bar in 24 h) |
|---|---|---|---|---|---|---|
| P-1 | Example 1 | 40 (censored) | none | 43 | 47 (inflation cycle 40) | 0.1 |
| P-2 | Example 1 | 40 (censored) | none | 41 | 46 (inflation cycle 40) | 0.1 |
| P-3 | Example 1 | 40 (censored) | none | 44 | 50 (inflation cycle 40) | 0.2 |
| C-1 | Comparative Example 1 | 13 | blockage at inflation cycle 14 | 41 | 68 (inflation cycle 13) | not the failure criterion |
| C-2 | Comparative Example 1 | 11 | leak-down of 0.7 bar in 24 h at inflation cycle 12 | 40 | 44 (inflation cycle 11) | 0.7 (inflation cycle 12) |
| C-3 | Comparative Example 1 | 17 | blockage at inflation cycle 18 | 42 | 75 (inflation cycle 17) | not the failure criterion |

[0165] The scope of the data is as follows. Three valve cores were tested in each group. The valve cores of Example 1 were run for 40 inflation cycles without failure and the test was then stopped, so the result is censored and the fatigue life of the seat ring (30), and its behaviour beyond 40 inflation cycles, are not established by the data. One liquid sealant, one inflation device, one operator, one inflatable chamber type, one hold temperature of 22 °C and one inflation pressure of 6 bar were used. The over-travel distance and the purge gap opening were not measured during the test; over-travel and shape recovery are indicated only by the audible snap on removal of the inflation device. No valve core of Example 2, Example 3 or Example 4 was tested.

[0166] Within that scope, the data show that the valve cores of Example 1 continued to seal, with a leak-down at inflation cycle 40 of 0.1 to 0.2 bar in 24 hours against a failure criterion of 0.5 bar in 24 hours, and continued to open, with an inflation time at inflation cycle 40 within 15 % of that at inflation cycle 1, over 40 sealant-loaded inflation cycles, whereas the conventional valve cores of Comparative Example 1 failed by blockage or leak-down between inflation cycles 12 and 18. No tool and no user action other than ordinary inflation was applied to any valve core of Example 1 during the test.

[0167] The post-test inspection of Example 1 shows which surfaces of the valve core were kept clear of sealant film. The sealing edge (34) of the seat ring (30) and the sealing face (42) of the poppet (40), which are the surfaces whose contact seals the valve core in the closed state and the surfaces across which the seat ring moves during the snap-back wipe, were clean. Sealant film remained on the outer surface of the seat ring in the region of the purge gap (60), a surface that neither seals in the closed state nor is wiped by the seat ring. The data do not separate the cleaning action of the air purge from that of the snap-back wipe, and no attribution between them is made herein; the cleaning action described herein is the air purge, the snap-back wipe, or both.

#### Robustness and failure modes

[0168] The following paragraphs describe conditions under which the performance of the valve core may be degraded, and the features described herein that address them. Where a feature has been tested it is so stated; where a feature has not been tested, it is described as a feature that may be used and no result is asserted for it.

[0169] Sealant film was found after 40 inflation cycles on the outer surface of the seat ring (30) in the region of the purge gap (60), a region that is closed, and therefore not purged, whenever the valve core is not in the purge state. Whether that film accumulates further over a service life longer than 40 inflation cycles, and whether it affects the opening or closing of the purge gap, was not tested. In some embodiments the purge gap opening is selected towards the upper end of the range of 0.10 mm to 0.25 mm, so as to increase the clearance and the velocity of the air purge in that region. In some embodiments the surface finish applied to the seat ring, such as electropolishing, is also applied to the adjoining surface of the core body bore (22) so as to reduce the adhesion of sealant film to it. The snap-back wipe occurring on every shape recovery may itself prevent sealant film in the closed purge gap from hardening; this has not been tested beyond 40 inflation cycles.

[0170] The seat ring (30) is subjected to radial deflection and shape recovery on every purge state, and the strain is concentrated at the root of each convolution of the convoluted wall (32). The fatigue life of the seat ring beyond the 40 inflation cycles of Example 1 has not been tested. In some embodiments the convoluted wall has two convolutions rather than one, so that the strain of a given radial deflection is distributed between them; in some embodiments a fillet radius is provided at the root of each convolution. No fatigue result is asserted for either feature.

[0171] The seat ring (30) of the illustrated embodiment is specified to have an austenite finish temperature below 5 °C, so that it is superelastic across ordinary riding temperatures. Its martensite start temperature has not been measured, and its behaviour if chilled below the martensite start temperature, whether by cold weather or by the expansion of gas from a compressed-CO2 inflation device while the seat ring is in the purge state, has not been tested; superelastic shape recovery may be impaired below the martensite start temperature until the seat ring warms. In some embodiments the superelastic alloy is selected, by its nickel content or by its shape-setting, to have a lower austenite finish temperature, giving more margin against chilling. In other embodiments the deflectable ring element is formed from a resilient metal or a resilient polymer whose shape recovery does not depend on a phase transformation, as described above in connection with the materials of the deflectable ring element, or the shape recovery of the deflectable ring element is positively driven by a formation of the poppet (40) on its return, as also described above. No value of the martensite start temperature and no cold-inflation margin is asserted herein.

[0172] Retention of the seat ring (30) in the illustrated embodiment relies on the interference fit of approximately 0.03 mm on diameter against the internal shoulder (24). The working range of the interference has not been determined, and no test of retention under thermal cycling or vibration has been performed. In some embodiments, supplementary ring retention is provided in addition to the interference fit, such as the crimped lip (224), the retaining sleeve (324), an adhesive bond, staking or laser welding described herein, so that the seat ring cannot migrate axially, rotate or come free into the inflatable chamber. In some embodiments the interference is held within a specified tolerance band and the press-in force or travel is checked at assembly, as described above, so that an interference at the tight end of the tolerance does not suppress the radial deflection of the seat ring or crack it at assembly, and an interference at the loose end does not leave the seat ring unretained.

[0173] In the illustrated embodiment the seal in the closed state is formed by metal-to-metal contact between the brass sealing face (42) of the poppet (40) and the sealing edge (34) of the seat ring (30). The bench test of Example 1 ran for 40 inflation cycles; the wear of the sealing face and the sealing edge over a service life of several thousand inflation cycles has not been tested. In some embodiments the sealing face is a hard-anodised aluminium sealing face, or carries a wear-resistant finish, as described in Example 4 and in connection with the alternatives above.

[0174] If the pressure differential rises rapidly and well beyond the over-travel threshold, for example on inflation from a shop compressor, the poppet (40) is driven into over-travel with greater force than on inflation with a floor pump. In some embodiments over-travel is limited independently of the deflectable ring element, as described above in connection with over-travel, so that the radial deflection of the seat ring (30) cannot exceed the recoverable strain of its material whatever the pressure differential applied. The bench test of Example 1 applied one inflation event per 24-hour inflation cycle with a floor pump; rapid repeated inflation events in a short period, inflation from a compressor, and the first inflation event after prolonged storage of the inflatable chamber in a deflated state, in which the sealant film near the inflation valve may have cured more fully than between the daily inflation cycles of the test, were not tested.

[0175] The austenite finish temperature, the convolution amplitude, the seat ring wall thickness after electropolishing and the over-travel threshold set by the second spring stage (54) each depend on a manufacturing step for which Example 1 gives the values used for the prototype valve cores and not a process window. In some embodiments production seat rings (30) are verified by sampling the austenite finish temperature after shape-setting, by measuring the convolution amplitude before shape-setting and the seat ring wall thickness after electropolishing, and by sorting or verifying the rate of the second spring stage at assembly, so that each production valve core lies within the ranges stated herein. These verification steps are described as manufacturing options and have not been practised for the prototype valve cores.

[0176] The liquid sealant of Example 1 contained ammonia. Brass is subject to stress-corrosion cracking in ammoniacal environments as a matter of general materials knowledge, and for that reason a core body (20) of stainless steel 303 is described in Example 4 and in connection with the alternatives above. Whether stress-corrosion attack occurs in service on the core body of brass CW614N or on the poppet (40) of the illustrated embodiment has not been tested. Liquid sealants that are free of ammonia, and liquid sealants of higher viscosity or with abrasive particulate fillers, were not tested, and the effect of the valve core with them is not asserted herein.

[0177] For storage and transport the lock nut (70) is used to hold the poppet (40) in the closed state, in which the purge shoulder (44) is clear of the seat ring (30) and the seat ring is at rest. A valve cap or accessory having an internal pin that depresses the poppet should not be used in a manner that holds the poppet in over-travel, since that would hold the seat ring in sustained radial deflection rather than the transient radial deflection of the purge state. Because the seat ring wall thickness is between 0.15 mm and 0.30 mm, a tool inserted into the valve core in the manner used to clear a conventional valve core may damage the convoluted wall (32); the valve core described herein is intended to be cleaned by the air purge and the snap-back wipe without tool insertion.

#### Industrial applicability and use

[0178] The inflation valve and the valve core described herein are for use with an inflatable chamber that holds liquid sealant, including a bicycle inner tube, as tested in Example 1, and a tubeless bicycle tyre set-up, in which the liquid sealant is likewise injected through the valve stem (10) and drawn towards the valve core on each inflation event. Use in a tubeless bicycle tyre set-up has not been tested. The valve core opens, closes and enters the purge state in response to the pressure differential alone; no tool and no user action beyond coupling and removing the inflation device is required for either cleaning action.

[0179] The purge state is reached when the pressure differential applied by the inflation device exceeds the over-travel threshold, which in Example 1 was 3.5 bar and was exceeded on every inflation event with a floor pump inflating the inflatable chamber from fully deflated to 6 bar. Whether a given inflation device reaches the over-travel threshold depends on the pressure differential it applies at the supply side: it is expected that floor pumps of the kind used in Example 1 do so, and hand pumps, compressors and compressed-CO2 inflation devices may or may not do so depending on the pressure differential they generate; only the floor pump of Example 1 has been tested. An inflation event in which the pressure differential does not exceed the over-travel threshold inflates the inflatable chamber through the main passage (64) in the normal-open state without entering the purge state, the purge gap (60) remaining closed; the air purge and the snap-back wipe occur on the inflation events in which the over-travel threshold is exceeded. Any inflation gas may serve as the air purge.

[0180] The valve core may be supplied as original equipment fitted to the valve stem (10) of an inflation valve, or as a replacement valve core for fitting to an existing valve stem in place of a conventional valve core, in which case it is threaded into the stem bore (12) in the same manner as the conventional valve core it replaces, and the lock nut (70) of the existing inflation valve may be retained. As shown in FIG. 5, the seat ring (30), or the seat ring together with the poppet (40) and the return spring (50), may also be supplied as a kit for assembly into a core body (20), as described above in connection with component supply. The inflation valve may be supplied fitted to a bicycle inner tube, a tubeless bicycle tyre set-up, a wheel, or a bicycle.
```

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

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/23.md`

````markdown
## Deliverable

### Dependent Claim Ladders

This is a drafting and analysis aid prepared by AI. It is not legal advice and says nothing about validity; qualified patent counsel signs off before anything is filed.

**Basis.** The ladders hang from the five independent claims of `22` (claims 1–5) and are numbered continuously from 6. The description does not yet exist: every rung is supported by the inventor's disclosure (§1–§9 via `01`, `03`), by `CONFIRMED.md` as quoted in `21`, `22` and `19`, by the `19` definitions and by the `16` blueprint section ids; paragraph anchors are mapped in P5d. Reference signs are the registry numerals of `20a`. Every range is a range the disclosure states (§4, §7); no intermediate value has been created. Rungs that rest on Gate 2 engineering candidates confirmed unattended, not on the inventor's own words, are marked **[candidate]** and must be reviewed at Gate 3; each has a matching `disclosure_requests` entry. Multiple dependencies are drafted EPO-style; counsel prunes for the US filing.

Each claim is followed by one note: added limitation | technical effect | support | the prior-art or design-around risk it answers.

#### Claim 1 (valve core)

6. The valve core of claim 1, wherein the deflectable ring element is a seat ring (30) having a sealing edge (34) on which the sealing face rests in the closed state.
> added: the ring element is itself the seat | effect: one element seals, is deflected to open the purge gap and recovers, so the sealing edge is cleaned in the same cycle that purges (clean sealing edge at cycle 40) | support: §3(3), §3(4), §8; 16 S8.4; 19 "seat ring" | answers: 09 row 6; fallback if the deflectable ring element genus is held too broad (03 Q5)

7. The valve core of claim 1, further comprising a fixed seat (130) carried by the core body and having a sealing edge on which the sealing face rests in the closed state, wherein the deflectable ring element is a wiper ring (132) separate from the fixed seat and located on the chamber side of the fixed seat.
> added: split architecture, sealing by a non-deflecting seat and purge by a separate wiper ring | effect: sealing is separated from deflection so the sealing edge does not move; at the cost of one more part and axial length | support: §6 Alternative B; 19 "wiper ring", "fixed seat"; 16 S10.5 | answers: 02 rank 6 and d2 R16/R17 (the inventor's own design-around); 08 value-map rank 6 row

8. The valve core of claim 6, wherein the seat ring has a wall arranged such that an axial load applied by the deflecting formation in the over-travel produces the radial deflection.
> added: axial-to-radial conversion by the wall of the seat ring | effect: the poppet's axial over-travel is turned into radial opening of the purge gap, with no other actuator | support: §3(3) ("translates into radial expansion"); 16 S10.2 | answers: 09 row 5 genus; EP1137892A1 (bodily moving ring) and US9982818B2 (thermal radial movement)

9. The valve core of claim 8, wherein the wall comprises a convoluted wall (32) having at least one convolution.
> added: the convoluted wall species | effect: a shallow convolution converts the axial load into radial deflection and recovers elastically at service temperature | support: §3(3), §4; 19 "convoluted wall"; 16 S10.2 | answers: 09 row 5; US9982818B2 (07 N3 ?)

10. The valve core of claim 9, wherein the convoluted wall has one convolution or two convolutions.
> added: convolution count | effect: one or two shallow convolutions give radial compliance without the axial compliance of a many-convolution wall | support: §3(3) ("one or two shallow convolutions"), §4 (number of convolutions) | answers: a bellows-type reading of the wall (LOCKED avoid-term rationale); 01 Q12

11. The valve core of claim 9 or claim 10, wherein the convoluted wall has a convolution amplitude of from 0.08 mm to 0.20 mm.
> added: convolution amplitude range | effect: sets the radial excursion available for the purge gap opening | support: §4 (0.08–0.20 mm; prototype 0.12 mm); 19 "convolution amplitude" | answers: 08 N6 (range as fallback once the concept is accepted); US9982818B2 gives no dimensions (07 Q3)

12. **[candidate]** The valve core of claim 8, wherein the wall is a frustoconical wall (232) or a slotted wall (332).
> added: alternative conversion geometries | effect: the same axial-to-radial conversion by a straight tapered wall or by a slotted wall (as the description states at the cited section; not in the inventor's disclosure) | support: CONFIRMED 12 E3.2, E4.3, E5.5; registry FIG. 12; 16 S10.2 | answers: d2 R8, R9 (straight wall, slotted collet)

13. The valve core of claim 6, wherein the seat ring has a seat ring inner diameter of from 2.0 mm to 2.6 mm and a seat ring wall thickness of from 0.15 mm to 0.30 mm.
> added: the claim 3 dimensional envelope | effect: places the seat ring in a valve core of this size with a wall thin enough to deflect and recover | support: §4; §7 (2.3 mm, 0.20 mm); 13 Table 1; 16 S7.10, S10.4 | answers: 08 N6; brings the family B distinction into family A as a fallback

14. The valve core of claim 13, wherein the seat ring has a seat ring free length of from 2.5 mm to 4.0 mm.
> added: free length range | effect: axial length over which the convolution acts | support: §4 (2.5–4.0 mm; prototype 3.0 mm); 19 "seat ring free length" | answers: 08 N6

15. The valve core of claim 1, wherein the core body has an internal shoulder (24) and the deflectable ring element is held in the core body against the internal shoulder, such that shape recovery of the deflectable ring element moves the deflectable ring element relative to the poppet.
> added: the ring element is fixed in the core body; recovery drives the relative movement | effect: the relative movement that wipes the poppet comes from recovery of the ring element, not from the stroke of the poppet | support: §2 ("wipes across the poppet face with a snap"), §3(3), §7 (pressed in against the internal shoulder); 16 S8.3, S8.4 | answers: 09 row 3; US4719938A, US6006954A, US11345196B2 (wiper carried on the moving member, 07 N1 A†)

16. The valve core of claim 15, wherein the deflectable ring element is retained in a core body bore (22) of the core body by an interference fit.
> added: retention by interference fit | effect: retains the ring element against the internal shoulder without a further part | support: §7; 19 general construction; LOCKED "interference fit" | answers: 11 DA-22 (a competitor omits the fit; this rung is the retention species, not the genus)

17. The valve core of claim 16, wherein the interference fit has an interference of approximately 0.03 mm on diameter.
> added: the prototype interference | effect: the tested retention condition | support: §7; 19 "about/approximately" | answers: support fallback only; note the tension with the purge gap opening (01 Q2)

18. **[candidate]** The valve core of claim 1, wherein the deflectable ring element is formed integrally with the core body.
> added: integral flexure | effect: no separate ring element to retain (as the description states at the cited section) | support: CONFIRMED 12 E4.5; 11 DA-5; 16 S10.6 | answers: d2 route in which the ring element is an integral formation of the core body

19. The valve core of claim 1, wherein, when the deflectable ring element undergoes shape recovery as the pressure differential falls, the deflectable ring element moves across a surface of the poppet so as to shear sealant film from that surface.
> added: the snap-back wipe | effect: partially cured sealant film is sheared off the poppet rather than embedded; clean poppet face at cycle 40 | support: §2; §8; bench data (audible snap; clean poppet face); 19 "snap-back wipe"; 16 S9.6 | answers: 09 row 3; d2 R7 (purge-only product does not have it, so the rung is a fallback, not the perimeter)

20. The valve core of claim 1, wherein the radial deflection is radially outward.
> added: direction of deflection | effect: the ring element expands away from the poppet, opening the purge gap on its outer side | support: §2 ("flexes radially outward"); 19 "radial deflection" (illustrated embodiment) | answers: 11 DA-3 (inward or tilting deflection are outside this rung by design; the independent claim is direction-neutral)

21. The valve core of claim 6, wherein the purge gap (60) is an annular radial clearance between an outer surface of the seat ring and a core body bore (22) of the core body.
> added: the illustrated purge gap location | effect: the air purge passes over the outside of the seat ring, where sealant film was found confined at cycle 40 | support: §3(6); §8; 19 "purge gap" (illustrated embodiment); 16 S8.7 | answers: sufficiency fallback for the functional purge gap of claim 1 (08 item 3; d2 R1); support conditional on 01 Q1/Q2

22. The valve core of claim 1, wherein the purge gap has a purge gap opening of from 0.10 mm to 0.25 mm in the purge state.
> added: purge gap opening range | effect: sizes the purge flow path for the air purge | support: §4 (0.10–0.25 mm; prototype 0.15 mm); 19 "purge gap opening" | answers: 08 N6; never measured on the prototype (01 Q23), so a support-risk rung

23. The valve core of claim 1, wherein the deflecting formation is a purge shoulder (44) of the poppet located on the chamber side of the sealing face.
> added: the locked species of the deflecting formation, and its position | effect: sealing and deflection are on distinct surfaces of the poppet; the sealing face is not the deflecting surface | support: §3(4); 19 "purge shoulder"; 16 S8.5, S11.3 | answers: 22 Q6 (if "deflecting formation" is refused, this is the locked term); 11 DA-4

24. **[candidate]** The valve core of claim 23, wherein the purge shoulder is a tapered purge shoulder (244).
> added: tapered contact geometry | effect: as the description states at the cited section (not in the inventor's disclosure) | support: CONFIRMED 11 DA-4 ("a taper on the poppet stem"); registry FIG. 11; 16 S11.3 | answers: 11 DA-4

25. **[candidate]** The valve core of claim 1, wherein the deflecting formation comprises a plurality of discrete lugs (344).
> added: lugs as the deflecting formation | effect: as the description states at the cited section | support: CONFIRMED 11 DA-4 ("lugs"); registry FIG. 11; 16 S11.3 | answers: 11 DA-4

26. The valve core of claim 1, wherein the deflecting formation is formed on a separate collar (444) fixed to the poppet.
> added: the formation on a collar | effect: the deflecting formation can be made and fitted separately from the poppet | support: 19 general construction ("a purge shoulder formed on a separate collar fixed to the poppet"); CONFIRMED 11 DA-4; registry FIG. 11; 16 S11.3 | answers: 11 DA-4; d2 route of a two-part poppet

27. The valve core of claim 1, further comprising a threshold-setting arrangement that resists movement of the poppet beyond the normal stroke and thereby sets the over-travel threshold.
> added: a structure that sets the threshold, stated as a genus | effect: the purge state is a distinct, higher-differential state, not a condition of every opening | support: LOCKED "second spring stage" Broader column; 19 general construction (functional terminology); 16 S7.7, S11.4 | answers: 09 row 1 note (b); US §112(f) anchor for the threshold relationship of claim 1

28. The valve core of claim 27, wherein the threshold-setting arrangement is a second spring stage (54) of the return spring, the return spring having a first spring stage (52) of lower rate that sets the crack pressure and the second spring stage of higher rate that is engaged at an end of the normal stroke and sets the over-travel threshold.
> added: the two-stage return spring | effect: separates the crack pressure from the over-travel threshold in one spring | support: §3(5), §4; 19 "second spring stage", "crack pressure", "over-travel threshold"; 16 S8.6 | answers: 09 row 7; EP1137892A1 claim 28, US9297373B2 (no sequential stages, 07 N5 ?)

29. **[candidate]** The valve core of claim 27, wherein the threshold-setting arrangement comprises an auxiliary spring (254) that is engaged by the poppet at an end of the normal stroke, or a detent (354).
> added: alternative threshold-setting structures | effect: as the description states at the cited section | support: CONFIRMED 11 DA-11; 16 S11.4; registry FIG. 14 | answers: 01 Q6; second §112(f) structure

30. **[candidate]** The valve core of claim 1, wherein the over-travel threshold is set by a stiffness of the deflectable ring element in the radial deflection.
> added: the ring element's own stiffness as the threshold | effect: no second spring stage is needed | support: CONFIRMED 12 E2.3; 16 S11.4 | answers: 09 row 1 note (b); 01 Q6

31. The valve core of claim 1, wherein the over-travel threshold is from 2.5 bar to 5.0 bar.
> added: over-travel threshold range | effect: a threshold that an ordinary floor pump reaches, so the purge state occurs in ordinary inflation events | support: §2 ("which every floor pump reaches"), §4 (2.5–5.0 bar; prototype 3.5 bar); 19 "over-travel threshold" | answers: 08 N6; 01 Q5 (basis of the threshold)

32. The valve core of claim 1 or claim 31, wherein the crack pressure is from 0.8 bar to 1.5 bar.
> added: crack pressure range | effect: normal inflation opens as in a conventional valve core | support: §4 (0.8–1.5 bar; prototype 1.0 bar); 19 "crack pressure" | answers: 08 N6

33. The valve core of claim 1, wherein the over-travel comprises an over-travel distance of from 0.4 mm to 0.9 mm.
> added: over-travel distance range | effect: the axial travel available to load the ring element | support: §4 (0.4–0.9 mm; prototype 0.5 mm); 19 "over-travel distance" | answers: 08 N6; never measured on the prototype (01 Q23)

34. The valve core of claim 1, wherein the crack pressure is about 1.0 bar and the over-travel threshold is about 3.5 bar.
> added: the prototype operating point | effect: the tested condition of the bench data | support: §4; §8; bench data; 19 "about/approximately" | answers: narrowest support fallback for the threshold relationship

35. The valve core of claim 1, wherein the deflectable ring element is of a superelastic alloy.
> added: superelastic material | effect: fast, stiff recovery gives the wipe its force; sealant film does not embed as in an elastomer seat | support: §2, §5; 19 "superelastic alloy"; 16 S10.1 | answers: 09 row 4 (dependent only); ref-02 [0024] + US6393765B1 (08 N4 increment *strong*)

36. The valve core of claim 35, wherein the superelastic alloy has an austenite finish temperature below 5 °C.
> added: transformation temperature | effect: superelastic at riding temperatures | support: §4; 19 "austenite finish temperature"; 14 footnotes [g], [h] | answers: 08 N4; CO2 cold-shock margin open (§9)

37. The valve core of claim 35 or claim 36, wherein the superelastic alloy is a nickel-titanium alloy having a nickel content of nominally 55.8 wt%.
> added: the prototype alloy | effect: the tested composition | support: §5; 19 "superelastic alloy" (illustrated embodiment) | answers: support fallback

38. The valve core of claim 1, wherein the deflectable ring element is of a resilient polymer.
> added: polymer material genus | effect: a lower-cost ring element with the same wall geometry (weaker wipe) | support: §6 Alternative A; 19 "seat ring" (resilient polymer); 16 S10.7 | answers: 02 rank 5; the inventor's own design-around

39. The valve core of claim 38, wherein the resilient polymer is polyether ether ketone.
> added: the PEEK species | effect: the named polymer of Alternative A | support: §6 | answers: support fallback

40. The valve core of claim 1, wherein the core body is of stainless steel.
> added: corrosion-resistant core body | effect: compatibility with ammonia-bearing liquid sealant | support: §5 (stainless 303); 16 S8.3 | answers: 02 rank 9; product-line rung (machined, not tested: 01 Q18)

41. The valve core of claim 1, wherein the core body has an external thread for reception in a stem bore of a valve stem, whereby the valve core is removable from the valve stem.
> added: the replaceable format | effect: the valve core is sold and fitted as a replacement part | support: §1 ("sold in multipacks"), §3(2) (threaded into the stem bore); 16 S8.2 | answers: 02 rank 1; 11 DA-19

42. **[candidate]** The valve core of claim 1, wherein the core body is a Schrader-pattern core body (620) and the poppet is a Schrader-pattern poppet (630).
> added: a second valve format | effect: as the description states at the cited section | support: CONFIRMED 12 E16.2; 11 DA-6; registry FIG. 15; 16 S11.9 | answers: 11 DA-6; 01 Q26

#### Claim 2 (inflation valve)

43. The inflation valve of claim 2, further comprising a core body (20) received in the stem bore (12), the deflectable ring element, the poppet and the return spring being carried by the valve stem through the core body.
> added: the removable-core format of the inflation valve | effect: the mechanism is carried in a core body that the valve stem receives | support: §3(1), §3(2); 16 S8.1, S11.9 | answers: the safe limb of claim 2 if the direct-carriage limb falls (22 Q5)

44. The inflation valve of claim 43, wherein the core body is threaded into the stem bore and is removable from the valve stem.
> added: threaded, removable core body | effect: the core can be replaced without replacing the valve stem | support: §1, §3(2); 16 S8.2 | answers: 02 ranks 1 and 3 together

45. The inflation valve of claim 43 or claim 44, wherein the core body, the deflectable ring element, the poppet and the return spring form a valve core according to any one of claims 1 and 6 to 42.
> added: the whole claim 1 ladder imported into the inflation valve | effect: every family A fallback is available to family C | support: as claims 1 and 6 to 42 | answers: as the imported rungs; counsel rewrites for the US if a cross-reference to another independent claim is not accepted

46. **[candidate]** The inflation valve of claim 2, wherein the deflectable ring element is a seat ring (730) carried directly by the valve stem.
> added: the direct-carriage limb as a rung | effect: an inflation valve with no separate core body (as the description states at the cited section) | support: CONFIRMED 12 E16.3, E14.6; registry FIG. 15; 16 S11.9 | answers: d2 R6; 11 Q6 (inventor has not stated it)

47. The inflation valve of claim 46, wherein the seat ring has a sealing edge on which the sealing face rests in the closed state and a convoluted wall arranged such that an axial load applied by the deflecting formation in the over-travel produces the radial deflection.
> added: the seat ring features for the direct-carriage limb | effect: the family B ring in the stem-integrated format | support: §3(3), §3(4); CONFIRMED 12 E16.3; 16 S10.2, S11.9 | answers: a fallback for claim 46, which cannot use claim 45

48. An inner tube defining an inflatable chamber and comprising an inflation valve according to any one of claims 2 and 43 to 47, the valve stem being fixed to the inner tube.
> added: the inner tube product | effect: the OEM unit sold with the inflation valve fitted | support: §1; 16 S11.9, S16 | answers: 02 rank 3; the increment is known (08, value-map rank 3 row), which is its purpose

49. **[candidate as to the wheel]** A wheel comprising a tubeless tyre defining an inflatable chamber and an inflation valve according to any one of claims 2 and 43 to 47 mounted to the wheel in communication with the inflatable chamber.
> added: the wheel product | effect: the complete-wheel OEM channel | support: §1, §6 (tubeless use); CONFIRMED 12 §16; 16 S11.9, S16 | answers: 02 rank 3; US11179979B2 claim 12 (known increment)

50. The inner tube of claim 48 or the wheel of claim 49, wherein the inflatable chamber holds liquid sealant.
> added: the sealant context on the product | effect: the product as sold for sealant use | support: §1; 19 "inflatable chamber", "liquid sealant" | answers: d2 R19 ("tubes only" label) at the product level

#### Claim 3 (seat ring)

51. The seat ring of claim 3, wherein the convoluted wall has one convolution or two convolutions.
> added: convolution count | effect: as claim 10 | support: §3(3), §4 | answers: as claim 10; US9982818B2 "at least one peak and at least one trough" is not distinguished by count alone, so this rung is a fallback only

52. The seat ring of claim 3 or claim 51, wherein the convoluted wall has a convolution amplitude of from 0.08 mm to 0.20 mm.
> added: amplitude range | effect: as claim 11 | support: §4 | answers: 08 value-map rank 2 row (dimensions move the rating to *moderate*)

53. The seat ring of any one of claims 3, 51 and 52, wherein the seat ring has a seat ring free length of from 2.5 mm to 4.0 mm.
> added: free length range | effect: as claim 14 | support: §4 | answers: as claim 52

54. The seat ring of claim 3, wherein the radial deflection is radially outward.
> added: direction of deflection | effect: as claim 20 | support: §2 | answers: as claim 20

55. The seat ring of claim 3, wherein the seat ring is of a superelastic alloy.
> added: material | effect: as claim 35 | support: §2, §5 | answers: 09 row 4; US9982818B2 claims 9, 11 (known material, so a fallback)

56. The seat ring of claim 55, wherein the superelastic alloy has an austenite finish temperature below 5 °C.
> added: transformation temperature | effect: as claim 36 | support: §4 | answers: 08 N4

57. The seat ring of claim 55 or claim 56, wherein the superelastic alloy is a nickel-titanium alloy having a nickel content of nominally 55.8 wt%.
> added: the prototype alloy | effect: as claim 37 | support: §5 | answers: support fallback

58. The seat ring of claim 3, wherein the seat ring is of a resilient polymer.
> added: polymer genus | effect: as claim 38 | support: §6 Alternative A ("the same convoluted wall") | answers: 02 rank 5

59. The seat ring of claim 58, wherein the resilient polymer is polyether ether ketone.
> added: PEEK | effect: as claim 39 | support: §6 | answers: support fallback

60. The seat ring of claim 3, wherein the seat ring inner diameter is about 2.3 mm, the seat ring wall thickness is about 0.20 mm, and the seat ring has a seat ring free length of about 3.0 mm and a convolution amplitude of about 0.12 mm.
> added: the prototype geometry | effect: the built and tested seat ring | support: §4, §7; bench data | answers: narrowest support fallback for family B

#### Claim 4 (method of inflating)

61. The method of claim 4, wherein, when the deflectable ring element undergoes shape recovery, the deflectable ring element moves across a surface of the poppet and shears sealant film from that surface.
> added: the snap-back wipe as a step | effect: as claim 19 | support: §2; bench data; 19 "snap-back wipe"; 16 S9.6 | answers: 09 row 3; d2 R7

62. The method of claim 4 or claim 61, wherein the air purge carries sealant film from surfaces of the inflation valve on which the sealant film has accumulated into the inflatable chamber.
> added: what the air purge does | effect: sealant film is blown into the inflatable chamber instead of remaining on the sealing surfaces | support: §2; 19 "air purge"; 16 S9.5 | answers: CN215861914U (air flow cleans on exhaust; here the purge flows into the chamber during inflation, 07 N0d A†)

63. The method of any one of claims 4, 61 and 62, wherein the crack pressure is from 0.8 bar to 1.5 bar and the over-travel threshold is from 2.5 bar to 5.0 bar.
> added: the operating ranges in the method | effect: as claims 31 and 32 | support: §4 | answers: 08 N6

64. The method of claim 4, wherein the inflation device is a floor pump and the pressure differential above the over-travel threshold is produced by the floor pump.
> added: the ordinary inflation device reaches the threshold | effect: the purge state occurs in ordinary floor-pump inflation without a tool or user action | support: §2 ("which every floor pump reaches"), §8 (floor pump to 6 bar); LOCKED "inflation device" species | answers: d2 R5 (a mechanically over-travelled core is outside the method; a pressure-over-travelled one is inside)

65. The method of claim 4, wherein the inflation device is a CO2 cartridge inflator supplying carbon dioxide as inflation gas.
> added: CO2 inflation | effect: the purge state under the second common inflation device | support: §9 item 2 (CO2 use conceived; cold-shock margin unknown); CONFIRMED 12 E8.5; 16 S7.8 | answers: coverage of CO2 inflation; the austenite finish temperature margin is an open risk (§9)

66. The method of claim 4, wherein the inflatable chamber is the interior of a bicycle inner tube or of a tubeless bicycle tyre.
> added: the two chamber types | effect: the disclosed uses | support: §1, §6; 19 "inflatable chamber" | answers: support fallback; covers both channels of 02 rank 3

67. The method of claim 4, wherein the liquid sealant is a latex emulsion containing ammonia.
> added: the tested sealant chemistry | effect: the sealant on which the bench data was obtained | support: §5, §8; 19 "liquid sealant" (tested embodiment) | answers: narrowest support fallback; ammonia-free sealants untested (§9)

68. The method of claim 4, further comprising repeating the coupling, the raising to at or above the crack pressure, the raising above the over-travel threshold and the removing over a plurality of inflation events, the purge state occurring in each inflation event.
> added: repetition over inflation events | effect: the sealing surfaces are purged on every inflation event, so sealant film does not accumulate over service (40 inflation cycles without blockage or leak-down) | support: §2 ("in the same inflation event ... automatically"), §8; bench data (audible snap on every prototype inflation) | answers: ref-01, US11904644B2 (maintenance or tool-based remedies)

69. The method of claim 4, wherein the inflation valve comprises a valve core according to any one of claims 1 and 6 to 42, or is an inflation valve according to any one of claims 2 and 43 to 47.
> added: the apparatus ladders imported into the method | effect: every apparatus fallback is available as a method fallback | support: as the imported claims | answers: as the imported rungs; counsel rewrites for the US if the cross-category reference is not accepted

#### Claim 5 (method of manufacturing)

70. The method of claim 5, wherein the tube stock has an outer diameter of about 2.7 mm and a wall of about 0.20 mm.
> added: the starting tube stock | effect: the tube from which the prototype seat ring was cut | support: §7 (2.7 mm OD, 0.20 mm wall) | answers: support fallback; 01 A2 (seat ring outer diameter inferred)

71. The method of claim 5 or claim 70, wherein the tube stock is supported on a mandrel while being laser cut.
> added: cutting on a mandrel | effect: supports the thin-walled tube stock during profiling | support: §7 ("laser-cutting ... on a mandrel") | answers: 08 N7 (CGK, so a fallback only)

72. The method of claim 5, wherein the convoluted wall is formed with one convolution or with two convolutions.
> added: convolution count in the process | effect: as claim 10 | support: §3(3), §4 | answers: as claim 10

73. The method of claim 5, wherein the seat ring blank is heated at about 500 °C for about 10 minutes and is then water quenched.
> added: the shape-setting point | effect: the tested shape-setting condition that fixes the convoluted wall geometry | support: §7; 19 "about/approximately" | answers: 08 N7; only the prototype point is disclosed (01 Q32)

74. The method of claim 5, further comprising electropolishing the shape-set seat ring to remove oxide and a heat-affected edge.
> added: electropolishing | effect: removes the oxide and the heat-affected edge left by laser cutting and shape-setting | support: §7; LOCKED "electropolishing" | answers: 08 N7; its contribution to the effect is unknown (03 Q15)

75. The method of claim 5, wherein the superelastic alloy is a nickel-titanium alloy having a nickel content of nominally 55.8 wt%.
> added: the prototype alloy | effect: as claim 37 | support: §5 | answers: support fallback

76. The method of claim 5 or claim 75, wherein the shape-set seat ring has an austenite finish temperature below 5 °C.
> added: the transformation temperature of the product | effect: the shape-setting yields a ring superelastic at riding temperatures | support: §4, §7 | answers: 08 N4; ties the process to the product

77. The method of claim 5, wherein the seat ring is a seat ring according to any one of claims 3 and 51 to 60.
> added: the family B product ladder imported | effect: the process claim survives through the product it makes | support: as the imported claims | answers: 08 value-map rank 4 row (the process survives only through the product)

78. The method of claim 5, further comprising pressing the seat ring into a core body bore (22) of a core body (20) of the valve core against an internal shoulder (24) of the core body with an interference fit.
> added: assembly into the core body (family F folded in) | effect: the seat ring is located axially and retained without a further part | support: §7; 16 S12.5; 15 FM-6, FM-7 | answers: 21 family F; ref-01 press-fitted sleeve (07 N6/7 ?) is a different part

79. The method of claim 78, wherein the interference fit has an interference of approximately 0.03 mm on diameter.
> added: the prototype interference | effect: as claim 17 | support: §7 | answers: support fallback; 01 Q2

## Rationale

**Order of the claim 1 ladder.** The rungs are grouped by what a competitor would remove first: the identity of the ring element (6, 7), then the wall that does the conversion (8–12), the ring dimensions (13, 14), retention and the recovery kinematics (15–18), the wipe (19), the purge gap species (20–22), the deflecting formation species (23–26), the threshold structure (27–30), the operating ranges (31–34), materials (35–39) and the body and format (40–42). Within each group the first rung is the broadest supported statement and the last is the prototype point, so that every group ends in a rung whose support is beyond argument.

**Genus before species.** Claims 8, 27 and 38 state a genus (wall that converts axial load, threshold-setting arrangement, resilient polymer) before the species the inventor built. Each genus is taken from the locked table's own Broader column or from the inventor's alternatives, not invented here; each species rung below it is what the inventor built or named. This is what gives the ladder value against the design-arounds in `11` and `d2`: a competitor who leaves the convoluted wall for a slotted wall still meets claim 8.

**The candidate rungs.** Claims 12, 18, 24, 25, 29, 30, 42, 46 and 49 rest on engineering candidates confirmed unattended at Gate 2 and drawn in figures 8–15 of the registry. I drafted them because the registry shows the description will describe them and because they are the rungs that answer the routes in `11` and `d2`; I marked them so that Gate 3 can strike any the inventor does not adopt, and each is a `disclosure_requests` entry naming the passage the description must contain. Their technical effects are deliberately stated as "as the description states": the inventor's disclosure does not give them, and I will not invent one. Registry items whose structure I cannot see in any text in front of me (cellular wall 432, purge port 262, flute 362, crimped lip 224, retaining sleeve 324) are not drafted; they are listed as disclosure requests for Prompt 25 to add if the description supports them.

**Claim 15 is the most important rung.** The `09` row 3 distinction is kinematic: the relative movement of the wipe comes from recovery of a ring element fixed in the core body, not from the stroke of the valve member. Claim 19 claims the wipe; claim 15 claims why it is different from US4719938A. Both are kept out of claim 1 because a purge-only product would not have them (d2 R7).

**What I declined.** A lock nut rung (conventional; no fallback value). A conical sealing face rung (cosmetic). A hard-anodised aluminium sealing face and a polymer core body (no text in front of me states their effect). Any rung on which poppet surface the wipe acts (01 Q10 open; drafting it would guess). A ratio between the over-travel threshold and the crack pressure (not stated; would be a created value). A normal stroke value rung (only the prototype 0.6 mm exists and it adds nothing the threshold rungs do not). A "purge state in every inflation event" rung on the apparatus (it is a use condition and sits in claim 68 of the method instead). The thermally actuated purge (outside the nucleus; Prompt 27 continuation candidate).

**Cross-references (claims 45, 69, 77).** They import whole ladders at the cost of one claim each. At the EPO they are ordinary dependent claims. In the US a claim referring to a claim of another category or another independent claim may be objected to or counted as an independent claim; counsel decides at filing whether to keep them or to expand the few rungs that matter for the US.

**Claim count.** Seventy-nine claims is far above the EPO fifteen-claim and US twenty-claim fee thresholds. That is intended: the depth of the ladder is the product of this prompt, and pruning for fees is a filing decision for counsel with the priorities marked here (groups 1, 2, 4, 5 and 8 of the claim 1 ladder first).

## Assumptions

A1. No Gate 1 answers exist: 01 Q1/Q2, 03 Q1, Q3, Q5, 01 Q6, Q10, Q12 are unanswered. The ladders follow `03` (air purge essential, wipe advantageous) and `09` rows 1–3. Blocking for P5 (25) and REVIEW.

A2. Gate 2 was confirmed unattended; the candidate rungs (12, 18, 24, 25, 29, 30, 42, 46, 49) use `CONFIRMED.md` items as it permits and are subject to Gate 3 review. Blocking for PACKAGE.

A3. The description will follow the `16` section ids and will describe every registry component drawn in figures 8–15; paragraph anchors are mapped in P5d. Blocking for P5 (25).

A4. The pressure differential is the supply-side pressure less the chamber-side pressure and the poppet opens towards the chamber side (01 A3–A5; 19 A4). Not blocking unless 01 Q3/Q4 reverse it.

A5. Multiple and cross-category dependencies (claims 11, 32, 37, 45, 48, 49, 50, 52, 53, 57, 62, 63, 69, 71, 76, 77) are acceptable EPO-style and will be pruned or rewritten by counsel for the US filing. Not blocking.

A6. "Stainless steel" (claim 40) is supported as a genus of the §5 stainless 303 by the 16 S8.3 passage; if the description names only grade 303, claim 40 narrows to it at Prompt 25. Not blocking.

## Open Questions

Q1. Where is the purge gap and how does it open against the interference fit (01 Q1, Q2)? Claims 21 and 17 assume the §3(6) location and the §7 fit together; if they cannot coexist, claim 21 falls and the purge gap species must be re-drafted. Blocks P5, REVIEW.

Q2. Which surface of the poppet does the recovering ring element wipe, in what direction and over what distance (01 Q10)? Claims 19 and 61 say "a surface of the poppet"; a narrower, more defensible rung cannot be drafted until answered. Blocks P5.

Q3. Does the description describe the registry components not drafted here (cellular wall 432, purge port 262, flute 362, crimped lip 224, retaining sleeve 324), and with what function? If so, rungs for each should be added at Prompt 25. Blocks P5 (25).

Q4. Did the inventor conceive any threshold-setting arrangement other than the second spring stage (01 Q6, Q7)? Decides whether claims 29 and 30 stand and whether claim 27 has more than one corresponding structure under 35 U.S.C. §112(f). Blocks P5, REVIEW.

Q5. Are Alternatives A and B within the invention (03 Q5; 01 Q20)? Decides claims 7, 38, 39, 58, 59. Blocks P5.

Q6. Did the inventor conceive the direct-carriage and Schrader-pattern formats (11 Q6; 01 Q26)? Decides claims 42, 46, 47. Blocks P5, PACKAGE.

Q7. Is CO2 inflation (claim 65) an intended use or only a noted risk (§9 item 2)? Decides whether claim 65 stands. Blocks P5.

Q8. How many claims will be filed, and in which jurisdictions first? Decides the pruning of this ladder and the fate of the cross-reference claims 45, 69 and 77. Blocks PACKAGE.

```json
{
  "prompt": "23",
  "status": "complete",
  "assumptions": [
    {"id": "A1", "text": "No Gate 1 answers; ladders follow 03 (air purge essential, wipe advantageous) and 09 rows 1-3.", "blocking": true},
    {"id": "A2", "text": "Gate 2 confirmed unattended; candidate rungs 12, 18, 24, 25, 29, 30, 42, 46, 49 use CONFIRMED.md items as permitted, subject to Gate 3 review.", "blocking": true},
    {"id": "A3", "text": "The description follows the 16 section ids and describes every registry component drawn in figures 8-15; paragraph anchors mapped in P5d.", "blocking": true},
    {"id": "A4", "text": "Pressure differential is supply-side less chamber-side pressure; poppet opens towards the chamber side (01 A3-A5; 19 A4).", "blocking": false},
    {"id": "A5", "text": "Multiple and cross-category dependencies are drafted EPO-style and will be pruned or rewritten by counsel for the US filing.", "blocking": false},
    {"id": "A6", "text": "'Stainless steel' in claim 40 is supported as a genus of stainless 303 by 16 S8.3; narrows to grade 303 at Prompt 25 if the description names only that grade.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "Purge gap location and opening against the interference fit (01 Q1, Q2); claims 21 and 17 assume the §3(6) location and the §7 fit coexist.", "blocks": ["P5", "REVIEW"]},
    {"id": "Q2", "text": "Which poppet surface the recovering ring element wipes, direction and distance (01 Q10); claims 19 and 61 stay at 'a surface of the poppet' until answered.", "blocks": ["P5"]},
    {"id": "Q3", "text": "Does the description describe cellular wall 432, purge port 262, flute 362, crimped lip 224, retaining sleeve 324, and with what function? Rungs to be added at Prompt 25 if so.", "blocks": ["P5"]},
    {"id": "Q4", "text": "Any threshold-setting arrangement other than the second spring stage conceived (01 Q6, Q7)? Decides claims 29, 30 and the §112(f) structures for claim 27.", "blocks": ["P5", "REVIEW"]},
    {"id": "Q5", "text": "Are Alternatives A and B within the invention (03 Q5; 01 Q20)? Decides claims 7, 38, 39, 58, 59.", "blocks": ["P5"]},
    {"id": "Q6", "text": "Direct-carriage and Schrader-pattern formats conceived (11 Q6; 01 Q26)? Decides claims 42, 46, 47.", "blocks": ["P5", "PACKAGE"]},
    {"id": "Q7", "text": "Is CO2 inflation an intended use or only a noted risk (§9 item 2)? Decides claim 65.", "blocks": ["P5"]},
    {"id": "Q8", "text": "Claim count and first jurisdictions; decides pruning and the cross-reference claims 45, 69, 77.", "blocks": ["PACKAGE"]}
  ],
  "new_terms": [
    {"term": "deflecting formation", "maps_to": "purge shoulder", "reason": "Locked genus of the purge shoulder (LOCKED Broader column); carried from claims 1, 2 and 4 of 22."},
    {"term": "threshold-setting arrangement", "maps_to": "second spring stage", "reason": "Locked genus of the second spring stage (LOCKED Broader column); the genus rung of claim 27."},
    {"term": "resilient polymer", "maps_to": null, "reason": "Material genus for the PEEK seat ring of §6 Alternative A (declared in 21); claims 38, 58."},
    {"term": "polyether ether ketone", "maps_to": null, "reason": "The PEEK of §6 Alternative A written in full; claims 39, 59."},
    {"term": "nickel-titanium alloy", "maps_to": "superelastic alloy", "reason": "The §5 species of the superelastic alloy, named as 19 names it; 'nitinol' and 'NiTi ring' are barred."},
    {"term": "stainless steel", "maps_to": "core body", "reason": "Material of the §5 stainless 303 core body variant, claimed as a genus (A6); claim 40."},
    {"term": "tube stock", "maps_to": null, "reason": "The §7 starting material for claim 5 (declared in 22); 'tube' alone is barred."},
    {"term": "seat ring blank", "maps_to": "seat ring", "reason": "The laser-cut part before shape-setting (declared in 22); claim 73."},
    {"term": "mandrel", "maps_to": null, "reason": "The §7 support on which the tube stock is laser cut; claim 71."},
    {"term": "heat-affected edge", "maps_to": null, "reason": "What the §7 electropolishing removes, as the LOCKED functional description states; claim 74."},
    {"term": "inflation gas", "maps_to": null, "reason": "Any gas from the inflation device (declared in 22); claim 65."},
    {"term": "CO2 cartridge inflator", "maps_to": "inflation device", "reason": "Locked species of the inflation device (LOCKED Narrower column); claim 65."},
    {"term": "floor pump", "maps_to": "inflation device", "reason": "Locked species of the inflation device (LOCKED Narrower column); claim 64."},
    {"term": "inner tube", "maps_to": "inflatable chamber", "reason": "Locked species ('bicycle inner tube', LOCKED Narrower column) named as the product of claim 48 and the chamber type of claim 66."},
    {"term": "tubeless tyre", "maps_to": "inflatable chamber", "reason": "Locked species ('tubeless bicycle tyre set-up') named in claims 49 and 66."},
    {"term": "wheel", "maps_to": null, "reason": "The system product of family C (02 rank 3; 12 §16; declared in 21); claim 49."},
    {"term": "tapered purge shoulder", "maps_to": "purge shoulder", "reason": "Registry component 244 (FIG. 11); species of the purge shoulder from CONFIRMED 11 DA-4; claim 24 (candidate)."},
    {"term": "discrete lugs", "maps_to": "purge shoulder", "reason": "Registry component 344 (FIG. 11); species of the deflecting formation from CONFIRMED 11 DA-4; claim 25 (candidate)."},
    {"term": "separate collar", "maps_to": "purge shoulder", "reason": "Registry component 444 (FIG. 11); the 19 general-construction example of a purge shoulder on a collar fixed to the poppet; claim 26."},
    {"term": "auxiliary spring", "maps_to": "second spring stage", "reason": "Registry component 254 (FIG. 14); threshold-setting species from CONFIRMED 11 DA-11; claim 29 (candidate)."},
    {"term": "detent", "maps_to": "second spring stage", "reason": "Registry component 354 (FIG. 14); threshold-setting species from CONFIRMED 11 DA-11; claim 29 (candidate)."},
    {"term": "frustoconical wall", "maps_to": null, "reason": "Registry component 232 (FIG. 12); alternative axial-to-radial wall geometry from CONFIRMED 12 E3.2/E5.5; claim 12 (candidate)."},
    {"term": "slotted wall", "maps_to": null, "reason": "Registry component 332 (FIG. 12); alternative wall geometry from CONFIRMED 12 E4.3; claim 12 (candidate)."},
    {"term": "Schrader-pattern core body", "maps_to": "core body", "reason": "Registry component 620 (FIG. 15); second valve format from CONFIRMED 12 E16.2; claim 42 (candidate)."},
    {"term": "Schrader-pattern poppet", "maps_to": "poppet", "reason": "Registry component 630 (FIG. 15); claim 42 (candidate)."},
    {"term": "seat ring (stem-integrated)", "maps_to": "seat ring", "reason": "Registry component 730 (FIG. 15); the direct-carriage species from CONFIRMED 12 E16.3; claim 46 (candidate)."},
    {"term": "shape-set seat ring", "maps_to": "seat ring", "reason": "The seat ring after the shape-setting step of claim 5, named to avoid an antecedent on the gerund; claims 74, 76."}
  ],
  "support_refs": [
    {"item": "Claims 6, 47: seat ring with sealing edge on which the sealing face rests in the closed state", "support": "intake/disclosure.md §3(3), §3(4), §8; runs/r1/P4/19.md 'seat ring', 'closed state'; runs/r1/P4/16.md S8.4; runs/r1/P2/09.md row 6"},
    {"item": "Claim 7: fixed seat and wiper ring on the chamber side of the fixed seat", "support": "intake/disclosure.md §6 Alternative B; runs/r1/P4/19.md 'wiper ring', 'fixed seat'; runs/r1/P4/16.md S10.5; terminology/LOCKED.md 'wiper ring'"},
    {"item": "Claims 8, 47: wall converting axial load from the deflecting formation into the radial deflection", "support": "intake/disclosure.md §3(3); runs/r1/P4/16.md S10.2; runs/r1/P5/22.md claim 3 wording"},
    {"item": "Claims 9, 10, 51, 72: convoluted wall, at least one convolution, one or two convolutions", "support": "intake/disclosure.md §3(3), §4; runs/r1/P4/19.md 'convoluted wall'; CONFIRMED.md 12 E5.2; terminology/LOCKED.md 'number of convolutions'"},
    {"item": "Claims 11, 52, 60: convolution amplitude 0.08-0.20 mm; prototype 0.12 mm", "support": "intake/disclosure.md §4; runs/r1/P4/19.md 'convolution amplitude'"},
    {"item": "Claim 12: frustoconical wall 232, slotted wall 332 (candidate)", "support": "CONFIRMED.md 12 E3.2, E4.3, E5.5 via runs/r1/P5/22.md; runs/r1/registry.json 232, 332; runs/r1/P4/16.md S10.2"},
    {"item": "Claims 13, 60: seat ring inner diameter 2.0-2.6 mm, wall thickness 0.15-0.30 mm; prototype 2.3 mm, 0.20 mm", "support": "intake/disclosure.md §4, §7; CONFIRMED.md 13 Table 1; runs/r1/P4/16.md S7.10, S10.4"},
    {"item": "Claims 14, 53, 60: seat ring free length 2.5-4.0 mm; prototype 3.0 mm", "support": "intake/disclosure.md §4; runs/r1/P4/19.md 'seat ring free length'"},
    {"item": "Claim 15: ring element held against the internal shoulder; recovery moves it relative to the poppet", "support": "intake/disclosure.md §2, §3(3), §7; runs/r1/P2/09.md row 3; runs/r1/P4/16.md S8.3, S8.4"},
    {"item": "Claims 16, 17, 78, 79: interference fit in the core body bore; approximately 0.03 mm on diameter", "support": "intake/disclosure.md §7; terminology/LOCKED.md 'interference fit'; runs/r1/P4/19.md 'about/approximately'; runs/r1/P4/16.md S12.5"},
    {"item": "Claim 18: ring element integral with the core body (candidate)", "support": "CONFIRMED.md 12 E4.5, 11 DA-5 via runs/r1/P5/22.md; runs/r1/P4/16.md S10.6"},
    {"item": "Claims 19, 61: snap-back wipe across a surface of the poppet shearing sealant film", "support": "intake/disclosure.md §2, §8; intake/data/bench-test.md (audible snap; clean poppet face); runs/r1/P4/19.md 'snap-back wipe'; runs/r1/P4/16.md S9.6"},
    {"item": "Claims 20, 54: radial deflection radially outward", "support": "intake/disclosure.md §2; runs/r1/P4/19.md 'radial deflection' (illustrated embodiment)"},
    {"item": "Claim 21: purge gap as annular radial clearance between the seat ring outer surface and the core body bore", "support": "intake/disclosure.md §3(6), §8; runs/r1/P4/19.md 'purge gap' (illustrated embodiment); runs/r1/P4/16.md S8.7; conditional on 01 Q1, Q2"},
    {"item": "Claim 22: purge gap opening 0.10-0.25 mm", "support": "intake/disclosure.md §4; runs/r1/P4/19.md 'purge gap opening'"},
    {"item": "Claim 23: purge shoulder on the chamber side of the sealing face", "support": "intake/disclosure.md §3(4); runs/r1/P4/19.md 'purge shoulder'; runs/r1/P4/16.md S8.5, S11.3"},
    {"item": "Claims 24, 25: tapered purge shoulder 244, discrete lugs 344 (candidates)", "support": "CONFIRMED.md 11 DA-4 via runs/r1/P5/22.md; runs/r1/registry.json 244, 344; runs/r1/P4/16.md S11.3"},
    {"item": "Claim 26: deflecting formation on a separate collar 444 fixed to the poppet", "support": "runs/r1/P4/19.md General construction, 'Direct and indirect coupling'; runs/r1/registry.json 444; runs/r1/P4/16.md S11.3"},
    {"item": "Claim 27: threshold-setting arrangement genus", "support": "terminology/LOCKED.md 'second spring stage' Broader column; runs/r1/P4/19.md General construction, 'Functional terminology'; runs/r1/P4/16.md S7.7, S11.4"},
    {"item": "Claim 28: first spring stage 52 sets the crack pressure; second spring stage 54 engaged at the end of the normal stroke sets the over-travel threshold", "support": "intake/disclosure.md §3(5), §4; runs/r1/P4/19.md 'second spring stage', 'crack pressure', 'over-travel threshold'; runs/r1/P4/16.md S8.6"},
    {"item": "Claims 29, 30: auxiliary spring 254, detent 354, ring-element stiffness (candidates)", "support": "CONFIRMED.md 11 DA-11, 12 E2.3 via runs/r1/P5/22.md; runs/r1/registry.json 254, 354; runs/r1/P4/16.md S11.4"},
    {"item": "Claims 31, 32, 34, 63: over-travel threshold 2.5-5.0 bar, crack pressure 0.8-1.5 bar, prototype 3.5 bar and 1.0 bar; floor pump reaches the threshold", "support": "intake/disclosure.md §2, §4, §8; runs/r1/P4/19.md 'crack pressure', 'over-travel threshold'"},
    {"item": "Claim 33: over-travel distance 0.4-0.9 mm", "support": "intake/disclosure.md §4; runs/r1/P4/19.md 'over-travel distance'"},
    {"item": "Claims 35-37, 55-57, 75, 76: superelastic alloy; austenite finish temperature below 5 °C; nickel-titanium nominally 55.8 wt% nickel content", "support": "intake/disclosure.md §2, §4, §5; runs/r1/P4/19.md 'superelastic alloy', 'austenite finish temperature'; CONFIRMED.md 14 footnotes [g], [h]; runs/r1/P4/16.md S10.1"},
    {"item": "Claims 38, 39, 58, 59: resilient polymer; polyether ether ketone", "support": "intake/disclosure.md §6 Alternative A; runs/r1/P4/19.md 'seat ring'; runs/r1/P4/16.md S10.7; runs/r1/P5/21.md new_terms 'resilient polymer'"},
    {"item": "Claim 40: stainless steel core body", "support": "intake/disclosure.md §5 (stainless 303); runs/r1/P1/02.md rank 9; runs/r1/P4/16.md S8.3"},
    {"item": "Claims 41, 43, 44: core body threaded into the stem bore, removable; carried by the valve stem through the core body", "support": "intake/disclosure.md §1, §3(1), §3(2); runs/r1/P4/19.md 'valve core', 'core body'; runs/r1/P4/16.md S8.1, S8.2, S11.9"},
    {"item": "Claim 42: Schrader-pattern core body 620 and poppet 630 (candidate)", "support": "CONFIRMED.md 12 E16.2, 11 DA-6 via runs/r1/P5/21.md; runs/r1/registry.json 620, 630; runs/r1/P4/16.md S11.9"},
    {"item": "Claim 46: seat ring 730 carried directly by the valve stem (candidate)", "support": "CONFIRMED.md 12 E16.3, E14.6 via runs/r1/P5/22.md; runs/r1/registry.json 730; runs/r1/P4/16.md S11.9"},
    {"item": "Claims 48-50, 66: inner tube, wheel with tubeless tyre, inflatable chamber holding liquid sealant", "support": "intake/disclosure.md §1, §6; CONFIRMED.md 12 §16 via runs/r1/P5/21.md; runs/r1/P4/19.md 'inflatable chamber', 'liquid sealant'; runs/r1/P4/16.md S11.9, S16"},
    {"item": "Claim 62: air purge carries sealant film into the inflatable chamber", "support": "intake/disclosure.md §2; runs/r1/P4/19.md 'air purge'; runs/r1/P4/16.md S9.5"},
    {"item": "Claim 64: floor pump produces the differential above the over-travel threshold", "support": "intake/disclosure.md §2, §8; terminology/LOCKED.md 'inflation device' species"},
    {"item": "Claim 65: CO2 cartridge inflator supplying carbon dioxide", "support": "intake/disclosure.md §9 item 2; CONFIRMED.md 12 E8.5 via runs/r1/P5/22.md; runs/r1/P4/16.md S7.8"},
    {"item": "Claim 67: latex emulsion containing ammonia", "support": "intake/disclosure.md §5, §8; runs/r1/P4/19.md 'liquid sealant'"},
    {"item": "Claim 68: repetition over inflation events, purge state in each", "support": "intake/disclosure.md §2, §8; intake/data/bench-test.md (audible snap on every prototype inflation; 40 inflation cycles)"},
    {"item": "Claims 70, 71, 73, 74: tube stock 2.7 mm OD and 0.20 mm wall; mandrel; 500 °C for 10 min and water quench; electropolishing to remove oxide and the heat-affected edge", "support": "intake/disclosure.md §7; terminology/LOCKED.md 'laser cutting', 'shape-setting', 'electropolishing'; runs/r1/P4/16.md S12.1-S12.3"},
    {"item": "Claims 45, 69, 77: cross-references importing the claim 1, claim 2 and claim 3 ladders", "support": "as the imported claims; runs/r1/P5/22.md rationale on US treatment of cross-category references"},
    {"item": "Prior-art and design-around risks in the rung notes", "support": "runs/r1/P2/09.md rows 1-7; runs/r1/P2/08.md Attack by claim concept; runs/r1/P2/07.md chart rows as cited; CONFIRMED.md 11 DA-3 to DA-22 and runs/r1/debate/d2-attack.md R1-R19 via runs/r1/P5/22.md"}
  ],
  "disclosure_requests": [
    {"limitation": "Claim 12: 'the wall is a frustoconical wall (232) or a slotted wall (332)'", "needed_disclosure": "An express passage (16 S10.2, FIG. 12) describing each wall as an alternative to the convoluted wall that converts axial load from the deflecting formation into radial deflection and recovers elastically, with its technical effect, labelled as a candidate pending 01 Q12."},
    {"limitation": "Claim 18: 'the deflectable ring element is formed integrally with the core body'", "needed_disclosure": "An express passage (16 S10.6) describing the integral flexure, how it is retained and deflected, and that 'carried by' in claim 1 includes it, labelled as a candidate."},
    {"limitation": "Claims 24, 25: 'tapered purge shoulder (244)'; 'a plurality of discrete lugs (344)'", "needed_disclosure": "An express passage (16 S11.3, FIG. 11) describing each as a species of the deflecting formation, where it contacts the deflectable ring element, and its technical effect, labelled as candidates."},
    {"limitation": "Claim 26: 'the deflecting formation is formed on a separate collar (444) fixed to the poppet'", "needed_disclosure": "An express passage (16 S11.3, FIG. 11) matching the 19 general-construction example, with how the collar is fixed to the poppet."},
    {"limitation": "Claim 27: 'a threshold-setting arrangement that resists movement of the poppet beyond the normal stroke and thereby sets the over-travel threshold'", "needed_disclosure": "An express genus statement (16 S7.7, S11.4) with at least two corresponding structures, so that the term is not limited to the second spring stage under 35 U.S.C. §112(f)."},
    {"limitation": "Claims 29, 30: 'an auxiliary spring (254) engaged by the poppet at an end of the normal stroke, or a detent (354)'; 'the over-travel threshold is set by a stiffness of the deflectable ring element in the radial deflection'", "needed_disclosure": "An express passage (16 S11.4, FIG. 14) describing each structure and how it sets the over-travel threshold, and the single-rate return spring case, labelled as candidates pending 01 Q6."},
    {"limitation": "Claim 15: 'held in the core body against the internal shoulder, such that shape recovery of the deflectable ring element moves the deflectable ring element relative to the poppet'", "needed_disclosure": "An express statement (16 S8.4, S9.6) that the ring element is fixed in the core body and that the relative movement of the snap-back wipe comes from its recovery, not from the stroke of the poppet."},
    {"limitation": "Claims 19, 61: 'moves across a surface of the poppet so as to shear sealant film from that surface'", "needed_disclosure": "An express statement (16 S9.6) naming the surface or surfaces of the poppet wiped, the direction and the distance (01 Q10); until answered the claims stay at 'a surface of the poppet'."},
    {"limitation": "Claim 21: 'an annular radial clearance between an outer surface of the seat ring and a core body bore (22)'", "needed_disclosure": "An express passage (16 S8.7, S9.4) describing this location as the illustrated embodiment and how the clearance opens against the interference fit of §7 (01 Q1, Q2); and, for later rungs, the inner-surface, end-face and through-wall species of 12 §7 (registry purge port 262, flute 362) with their function."},
    {"limitation": "Claims 16, 17 (and rungs not drafted): retention alternatives crimped lip (224) and retaining sleeve (324)", "needed_disclosure": "An express passage (16 S8.3, FIG. 8) describing the crimped lip and retaining sleeve as alternatives to the interference fit; if present, Prompt 25 adds a rung for each."},
    {"limitation": "Rung not drafted: cellular wall (432)", "needed_disclosure": "An express passage (FIG. 12) describing the cellular wall and its function; if present, Prompt 25 adds it to claim 12."},
    {"limitation": "Claim 40: 'the core body is of stainless steel'", "needed_disclosure": "An express statement (16 S8.3) that the core body may be of stainless steel, for example grade 303, and of its purpose with ammonia-bearing liquid sealant."},
    {"limitation": "Claim 42: 'Schrader-pattern core body (620) and Schrader-pattern poppet (630)'", "needed_disclosure": "An express passage (16 S11.9, FIG. 15) describing the Schrader-pattern format with the deflectable ring element and the deflecting formation, labelled as a candidate pending 01 Q26."},
    {"limitation": "Claims 46, 47: 'a seat ring (730) carried directly by the valve stem'", "needed_disclosure": "An express passage (16 S11.9, FIG. 15) describing the stem-integrated seat ring, how the poppet is guided and the return spring seated in that format, labelled as a candidate pending 11 Q6."},
    {"limitation": "Claim 49: 'A wheel comprising a tubeless tyre ... and an inflation valve ... mounted to the wheel'", "needed_disclosure": "An express statement (16 S11.9, S16) of the wheel and tubeless tyre incorporating the inflation valve, and of the inner tube with the valve stem fixed to it (claim 48)."},
    {"limitation": "Claims 64, 65: 'the inflation device is a floor pump and the pressure differential above the over-travel threshold is produced by the floor pump'; 'a CO2 cartridge inflator supplying carbon dioxide as inflation gas'", "needed_disclosure": "An express statement (16 S7.8, S9.3) that a floor pump produces a pressure differential above the over-travel threshold in ordinary use, and that inflation gas includes carbon dioxide from a CO2 cartridge inflator, with the austenite finish temperature caution of §9."},
    {"limitation": "Claim 68: 'the purge state occurring in each inflation event'", "needed_disclosure": "An express statement (16 S9.7, S13) that the purge state occurs in each inflation event in which the over-travel threshold is exceeded, with the bench-data observation of an audible snap on every prototype inflation."},
    {"limitation": "Claim 74: 'electropolishing the shape-set seat ring to remove oxide and a heat-affected edge'", "needed_disclosure": "An express statement (16 S12.3) of the purpose of electropolishing as in §7, and any effect on the sealing edge (03 Q15)."},
    {"limitation": "Claims 72, 73 (and claim 5): which step forms the convolution", "needed_disclosure": "An express statement (16 S12.1, S12.2) whether the convolution is formed by the laser cut, by a mandrel or by the shape-setting fixture (01 Q11), so that claim 72 can be tied to a step."}
  ],
  "open_disagreements": [],
  "narrowing_suggested": []
}
```
````

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/24.md`

````markdown
## Deliverable

### Three Formulations

This is a drafting and analysis aid prepared by AI. It is not legal advice and says nothing about validity; qualified patent counsel signs off before anything is filed.

All three formulations claim the same inventive concept, the nucleus of `09` rows 1 and 2: one poppet with two sequential ranges; the deflectable ring element untouched over the normal stroke and deflected radially only in over-travel above a threshold higher than the crack pressure; a purge gap, separate from the main passage, closed in the two lower states and opened by that deflection; shape recovery closing it again. They differ in *how* that concept is bounded: by named parts and their physical arrangement (Formulation 1), by pressure-defined states and the relationships between parts (Formulation 2), or by the sequence of events in one inflation event (Formulation 3). None recites a material, a number, the snap-back wipe, or the inflatable chamber as an element of the apparatus.

The description does not yet exist. Support is cited to the inventor's disclosure (§), the `19` definitions, the `01` state table and the `16` blueprint sections; paragraph anchors are mapped at Prompt 25 against the stitched description. Reference signs follow `registry.json`: core body (20), core body bore (22), internal shoulder (24), seat ring (30), convoluted wall (32), sealing edge (34), poppet (40), sealing face (42), purge shoulder (44), return spring (50), first spring stage (52), second spring stage (54), purge gap (60), purge flow path (62), main passage (64).

#### Formulation 1 - structural

A valve core for an inflation valve, the valve core comprising:
a core body (20) having a core body bore (22) and an internal shoulder (24);
a seat ring (30) received in the core body bore against the internal shoulder, the seat ring having a sealing edge (34) and a convoluted wall (32) having at least one convolution;
a poppet (40) guided by the core body and having a supply side, a chamber side, a sealing face (42) and, on the chamber side of the sealing face, a purge shoulder (44), the sealing face resting on the sealing edge in a closed state of the valve core so as to close a main passage (64) past the sealing face; and
a return spring (50) biasing the poppet towards the closed state, the return spring having a first spring stage (52) and a second spring stage (54) of higher rate than the first spring stage, the first spring stage resisting a normal stroke of the poppet from the closed state and the second spring stage being engaged at the end of the normal stroke;
wherein the purge shoulder is spaced from the seat ring by an axial clearance in the closed state and throughout the normal stroke, and bears on the seat ring in over-travel of the poppet beyond the normal stroke against the second spring stage;
wherein the convoluted wall is arranged such that axial load applied by the purge shoulder in the over-travel produces radial deflection of the seat ring, the radial deflection opening a purge gap (60) between an outer surface of the seat ring and the core body bore, the purge gap being closed in the closed state and throughout the normal stroke and, when open, forming a purge flow path (62), separate from the main passage, from the supply side to the chamber side; and
wherein the seat ring undergoes shape recovery to close the purge gap when the axial load is removed.

Support: core body, core body bore, internal shoulder and the seat ring carried against the internal shoulder, §3(2), §7 (`19` "core body"; `16` S8.3); seat ring with sealing edge and convoluted wall, §3(3) (`19` "seat ring", "convoluted wall"; `16` S8.4, S10.2); purge shoulder on the chamber side of the sealing face, contact only in over-travel, §3(4) (`19` "purge shoulder"; `16` S8.5, S9.2); first and second spring stages, the second engaged at the end of the normal stroke and setting the over-travel threshold, §3(5), §4 (`19` "second spring stage", "over-travel threshold"; `16` S8.6, S9.3); axial load converted to radial deflection, §3(3) "translates into radial expansion" (`19` "convoluted wall", "radial deflection"); purge gap between the seat ring outer surface and the core body bore, §3(6) (`19` "purge gap", illustrated embodiment; `16` S8.7) - **conditional**: §2 places the gap at the stem bore and the §7 interference fit is not reconciled with a radial clearance at the bore (01 Q1, Q2); purge flow path separate from the main passage, §2, §3(6), drawings README FIG-2 (`19` "purge flow path"; `16` S9.5); shape recovery, §2 (`19` "deflectable ring element"; `16` S9.6). The axial clearance is disclosed as a relationship (§3(4)) but its value in the closed state is not stated; the `22` disclosure request for that statement stands.

#### Formulation 2 - functional/relationship

A valve core for an inflation valve, the valve core comprising a core body (20), a poppet (40) guided by the core body, a deflectable ring element (30) carried by the core body, a return spring (50) biasing the poppet towards a closed state of the valve core, and a main passage (64) that is closed by a sealing face (42) of the poppet in the closed state;
the poppet having a supply side and a chamber side and being displaced from the closed state in response to a pressure differential between the supply side and the chamber side;
the valve core having:
the closed state, at a pressure differential below a crack pressure, in which the main passage is closed, the deflectable ring element is in its at-rest form and a purge gap (60) associated with the deflectable ring element is closed;
a normal-open state, at a pressure differential at or above the crack pressure and below an over-travel threshold higher than the crack pressure, in which the poppet is displaced within a normal stroke, the main passage is open, the deflectable ring element is in its at-rest form and the purge gap is closed; and
a purge state, at a pressure differential above the over-travel threshold, in which the poppet is in over-travel beyond the normal stroke and deflects the deflectable ring element radially, the radial deflection opening the purge gap so that a purge flow path (62), separate from the main passage, extends from the supply side through the purge gap to the chamber side;
the deflectable ring element undergoing shape recovery to its at-rest form and closing the purge gap when the pressure differential falls below the over-travel threshold.

Support: the three states and the pressure differential at which each occurs, `01` (i) state table, §2, §4 (`19` "closed state", "purge state", "crack pressure", "over-travel threshold"; LOCKED "normal-open state": poppet displaced within the normal stroke, flow through the main passage, purge gap closed; `16` S9.1-S9.4); deflectable ring element carried by the core body and deflected radially by the poppet in over-travel, §2, §3(3), §3(4), §6 (`19` "deflectable ring element", "over-travel": "during which the purge shoulder bears on the deflectable ring element"; `16` S7.4, S8.4); at-rest form in the two lower states, §3(4) "only contacts the ring during over-travel" and `19` "deflectable ring element": "shape recovery toward its at-rest form" (`16` S9.2, S9.6) - the words "at-rest form" must appear in the state description, requested below; purge gap "associated with the deflectable ring element", closed in the closed state and the normal-open state and opened by radial deflection in the purge state, `19` "purge gap" verbatim, §2, §3(6) (`16` S7.5, S9.4) - support conditional on 01 Q1, Q2 as for every formulation; purge flow path separate from the main passage, `19` "purge flow path", FIG-2 (`16` S9.5); shape recovery when the pressure differential falls below the over-travel threshold, §2, `19` "snap-back wipe" (timing) and "deflectable ring element" (`16` S9.6); pressure actuation, §2, `01` A3 (`19` "pressure differential").

#### Formulation 3 - process/interaction

A method of operating an inflation valve of an inflatable chamber that holds liquid sealant, the inflation valve having a valve core comprising a core body, a poppet having a supply side, a chamber side and a sealing face, a deflectable ring element carried by the core body, a main passage closed by the sealing face in a closed state of the valve core, and a return spring biasing the poppet towards the closed state, the method comprising, within a single inflation event:
coupling an inflation device to the supply side and raising a pressure differential between the supply side and the chamber side to at or above a crack pressure, whereby the poppet moves through a normal stroke into a normal-open state and inflation gas flows through the main passage into the inflatable chamber while the deflectable ring element remains in its at-rest form and a purge gap associated with the deflectable ring element remains closed;
continuing to raise the pressure differential above an over-travel threshold higher than the crack pressure, whereby the poppet moves into over-travel beyond the normal stroke and deflects the deflectable ring element radially, the radial deflection opening the purge gap, and passing inflation gas as an air purge along a purge flow path, separate from the main passage, from the supply side through the purge gap into the inflatable chamber across surfaces of the valve core on which sealant film accumulates; and
removing the inflation device from the supply side, whereby the pressure differential falls and the deflectable ring element undergoes shape recovery to its at-rest form and closes the purge gap.

Support: inflatable chamber holding liquid sealant, §1, §2 (`19` "inflatable chamber", "liquid sealant"; `16` S9.1); inflation event from coupling to removal, §2, §8, `01` (d) S1-S5 (`19` "inflation event"; `16` S9.9); the whole sequence in one inflation event, §2 as read in `09` row 1 ("in the same inflation event ... the purge state follows automatically"); normal-open flow with the ring element at rest, §2, §3(4), §4 (`16` S9.2); over-travel above the threshold, radial deflection, purge gap opening, §2, §3(4)-(6), §4 (`16` S9.3, S9.4); air purge along the purge flow path across the surfaces on which sealant film accumulates and into the inflatable chamber, §2, §8, `19` "air purge" verbatim, FIG-2 (`16` S9.5, S7.8); inflation gas rather than air, CONFIRMED 12 E8.5 via `22` (`16` S7.8); removal and shape recovery, §2, bench data (audible snap on removal of the pump head) (`16` S9.6). Support conditional on 01 Q1, Q2 for the purge gap, as above.

Support permits this formulation. It is the process counterpart of Formulation 2, not of `22` claim 4: it drops the deflecting formation, adds the single-inflation-event frame and the air purge across the fouling surfaces, and is written as a method of operating rather than a method of inflating. Prompt 25 should carry one method claim, not both; see the Comparison.

**Formulations considered and not drafted.** (a) A carrier-neutral apparatus claim in which the deflectable ring element and the deflecting formation are each carried by one of the poppet and the core body, without saying which (11 DA-8; `22` rationale). Not drafted: `19` defines the deflectable ring element as carried by the valve core and the purge shoulder as a formation of the poppet; nothing in the disclosure puts the ring element on the poppet. Recorded in `disclosure_requests`. (b) A claim without the over-travel threshold, the purge state defined by deflection alone (11 DA-1). Not drafted: it reads on ref-02 claim 4 with [0019] (08 item 2) and whether purging on every opening works is unanswered (03 Q3). (c) A wipe-only claim (d2 R7). Not drafted: the air purge is essential on 03 A2 until 03 Q1 is answered.

### Comparison

| Formulation | Breadth | Clarity | Prior-art exposure | Enablement risk | Design-around resistance |
|---|---|---|---|---|---|
| **1 - structural** | Narrowest. Species throughout: a seat ring that also seals (not the Alternative B wiper ring), a convoluted wall, the first and second spring stages as the threshold-setting arrangement, and the §3(6) purge gap location. Material-neutral, so the PEEK seat ring of §6 is within it | Highest. Every element is a named part visible on teardown; the three-state behaviour follows from structure (clearance, second spring stage, convoluted wall) rather than being recited as a result. "Engaged at the end of the normal stroke" needs the `19` definitions of normal stroke and second spring stage in the description; otherwise no relative terms. No §112(f) exposure: "seat ring" and "return spring" are structural nouns | Lowest to anticipation: no charted reference has a seat-deflecting formation held clear by a two-stage return spring (07 grid N0b). Inventive step rests on the same N0 relationships as the others; the added increments (seat ring as seat, convoluted wall, two spring stages) are each known alone (08 N2, N3, N5) and add little. EP1137892A1 claim 28 (two springs) and US9982818B2 (wave-profile ring) will be cited for the increments, not for the combination | Highest of the three on one point: it fixes the purge gap between the seat ring outer surface and the core body bore, the §3(6) reading that §2 contradicts and that the 0.03 mm interference fit does not obviously permit (01 Q1, Q2; 08 item 3). If the inventor's answer moves the gap, this claim is wrong as written, not merely narrow. Otherwise low: every element is the built prototype | Lowest. Escapes at no cost: a wall of other geometry converting axial load to radial deflection (12 E3.2, E5.5; d2 R9); a single-rate return spring with the threshold set by ring stiffness (12 E2.3); the Alternative B fixed seat plus wiper ring (§6); a purge gap through the ring wall or at another surface (12 §7); a ring element retained other than against an internal shoulder (11 DA-22). Covered: PEEK ring; purge shoulder on a separate collar (`19` coupling paragraph) |
| **2 - functional/relationship** | Broadest. No formation named (the sealing face, a taper, a collar or lugs all satisfy "the poppet ... deflects"; 11 DA-4 closed without the `22` Q6 risk); no threshold-setting structure; no gap location or deflection direction; the genus covers the seat ring and the Alternative B wiper ring. "At-rest form" in the normal-open state is satisfied whether the poppet is clear of the ring element or touches it without deflecting it, which "spaced from" (`22` claim 1) is not | Good at the EPO and UK: each state is fixed by a pressure differential band and by what is open and closed, all defined in `19`. In the US the state clauses are functional; §112(f) is not triggered for the claim as a whole (core body, poppet, spring are structural) but "deflectable ring element" is a generic noun plus function (LOCKED drafting note) and may be construed as means-plus-function limited to the seat ring and wiper ring and equivalents, which is acceptable if both are described. "Associated with" for the purge gap is the `19` wording; an examiner may ask what it excludes. Whether the pressure differential is static or transient must be defined (01 Q4) | Concentrated on two phrases. (i) "At-rest form" in the normal-open state: ref-02 claim 4 deflects the lip "during opening" and US4462449A has no main-passage flow before the elastomeric member is engaged (07 N0c, N0d), so both are outside as long as the description states plainly that the ring element is undeflected throughout the normal stroke. (ii) The purge state defined by a pressure band: EP1137892A1 claims 1(e), 8 open a gap above a threshold, but on chamber-side pressure, in a separate member, discharging outward (07 N0b, N0d); distinguished by the poppet's own over-travel doing the deflecting and by the path running to the chamber side. The 08 three-document combination (ref-02 + EP1137892A1 + CN215861914U) is the inventive-step attack and is no stronger here than for Formulation 1, because the combination attacks the N0 relationships that all three formulations share | Moderate, and of a different kind from Formulation 1. The functional purge gap survives whatever answer 01 Q1/Q2 brings, but a genus supported by one built species and a list of candidate species (12 §7) invites a US written-description attack and, at the EPO, an Art. 83 attack if the one species is not enabled (08 item 3). "Poppet ... deflects the deflectable ring element" with no formation named is supported by the purge shoulder embodiment plus the `19` coupling paragraph; the genus statement of `22`'s second disclosure request is needed for it to hold. The threshold relationship with no structure needs more than one corresponding threshold-setting arrangement described (`22` third disclosure request; 01 Q6) | Highest. Closes DA-4 (formation), DA-11 (threshold means), DA-2 and DA-3 (gap location and direction), R16 partially (any part of the poppet), and Alternative B. Remaining escapes are the same for every formulation and cannot be closed without new disclosure: purge on every opening (R4; 03 Q3), wipe only with the periphery sealed (R7; 03 Q1), a purge port with nothing deflecting (R2), over-travel by a depressor head with no pressure threshold (R5; 11 Q9), the ring element carried by the poppet (DA-8). Teardown proof is harder than for Formulation 1: the states are shown by a pressure test, not by measurement of parts |
| **3 - process/interaction** | Formulation 2's scope as a sequence of acts, narrowed by its context: the inflatable chamber must hold liquid sealant and an inflation device must be coupled and removed. Catches a valve of any construction that performs the sequence during inflation, including one outside Formulations 1 and 2 on a structural point, provided the ring element is deflected by the poppet | Good: the steps are the `01` (d) sequence in `19` terms. "Whereby" clauses in the US state the result of each act and are given weight only if they state a condition material to patentability, which here they do (the normal-open state with the ring element at rest; the purge gap opening). "Across surfaces of the valve core on which sealant film accumulates" is result-like and is the `19` definition of air purge; it can be dropped at 25 without loss if an examiner objects. "Single inflation event" is defined in `19` | Same novelty position as Formulation 2 over ref-02, US4462449A and EP1137892A1 (07 N0b-N0d). Slightly more exposed to the combination attack because it recites the air purge across the fouling surfaces, which is the contribution CN215861914U supplies to the 08 mosaic (07 CN215861914U N0d A†). Method claims for a purpose are read at the EPO as limited to that purpose, which helps novelty and costs nothing here since the sealant context is already a step | As Formulation 2 for the purge gap and the ring element genus. Lower on the threshold: the method needs no threshold-setting structure at all, only that the pressure differential be raised past two values, which §2 and §4 disclose directly. "Single inflation event" rests on §2 as read in `09` row 1 and on the bench data (snap on pump-head removal after every inflation); it should be stated expressly (requested below) | High against a competitor's product (the sequence is what the product does), but weak in enforcement: the direct infringer is the rider (02 rank 8, A3); the seller is reached through inducement, which needs instructions or marketing for sealant use, and the acts are momentary and internal (bench data detects the purge state only by an audible snap). Escapes as Formulation 2 plus a product sold and instructed for chambers without liquid sealant |
| **Recommendation** | **Formulation 2 goes forward as the independent valve core claim and, with "valve stem" as carrier, as the inflation valve claim (`22` claims 1 and 2 at Prompt 25); `22`'s "deflecting formation ... spaced from" wording moves to the first dependent rung of each, so that the file holds both readings of the normal-open state. Formulation 3 goes forward as the single method claim in place of `22` claim 4 (same claim number; changed wording recorded at 25), because it does not depend on the `22` Q6 answer and adds the single-inflation-event frame that ties the purge to ordinary use. Formulation 1 does not go forward as an independent claim: at the EPO a second independent claim in the same category is refused under Rule 43(2) EPC absent an exception, and its purge gap location commits the filing to the one reading of §3(6) that 01 Q1/Q2 may overturn. Its elements are the terminus of the Formulation 2 dependent ladder (Prompt 23: seat ring as the ring element; convoluted wall; first and second spring stages; gap at the core body bore), each rung added only if 01 Q1 confirms it. For a US filing counsel may add Formulation 1 as a further independent claim once 01 Q1 is answered, because there it is the claim whose infringement is proved by teardown alone.** | | | | |

## Rationale

**Why these three and not re-orderings of `22` claim 1.** `22` claim 1 sits between Formulations 1 and 2: it names a deflecting formation and a spatial relationship ("spaced from ... throughout the normal stroke") but leaves the carrier, the threshold means and the gap location functional. Prompt 24 asks for three scopes, so I moved outward from it in one direction (states and pressure bands, no formation) and inward in the other (the prototype architecture with every relationship expressed as a part), and wrote the process form as the counterpart of the broad one rather than of `22` claim 4. The result is that the file now contains, for the normal-open state, three distinct expressions with the same support: the ring element "in its at-rest form" (Formulation 2), the formation "spaced from" the ring element (`22`), and an "axial clearance" closed only in over-travel (Formulation 1). That is the point of the exercise: if one wording is held unclear or anticipated, the others are there to amend to.

**Why "at-rest form" rather than "spaced from".** Both are positive (lessons L1). "At-rest form" is the `19` phrase for the shape the ring element recovers to, so it is already a defined condition; it is broader in one respect a competitor would use (a formation that touches the ring element in the normal-open state without deflecting it) and it does not require the description to fix a clearance value. The risk is that the examiner reads "at-rest form" as a result; the cure is the express statement requested, and the fallback is the `22` wording on the next rung.

**Why Formulation 1 fixes the gap at the core body bore.** A structural formulation that keeps the purge gap functional is not a structural formulation; it is Formulation 2 with extra parts. I drafted the honest species and said in the table where it fails. If 01 Q1 confirms the §3(6) reading, the claim is the strongest teardown claim in the set; if it does not, nothing in Formulation 1 survives unchanged and the drafting must not depend on it.

**Why Formulation 3 replaces rather than joins `22` claim 4.** Two method claims of the same scope in different words is duplicate scope, which Prompt 25 would have to remove. Formulation 3 is preferred because it survives the `22` Q6 answer either way and because the single-inflation-event frame expresses the commercial point (`09` row 1: the purge is added on top of normal inflation, not a condition of it). The "across surfaces" clause is included because it is the `19` definition of air purge and states the technical effect the EPO will look for under problem-solution; it is marked as droppable.

**Why the carrier-neutral formulation was not forced.** DA-8 is the one design-around the three formulations leave open that is closable by drafting, but only if the ring-on-poppet arrangement is disclosed, and it is not. Drafting it would be a limitation without an anchor.

**Jurisdiction points folded into the table.** Rule 43(2) EPC drives the recommendation against two apparatus independents; US §112(f) drives the note on "deflectable ring element" and on the threshold relationship; the EPO reading of purpose-limited method claims and the US treatment of "whereby" drive the Formulation 3 clarity entry.

## Assumptions

A1. `description.md` does not exist; support is cited to the disclosure sections, the `19` definitions, the `01` state table and the `16` blueprint section ids, and paragraph anchors are mapped at Prompt 25 against the stitched description. Blocking for P5 (25).

A2. No Gate 1 answers exist (01 Q1, Q2, Q4, Q6; 03 Q1, Q3, Q5; 11 Q1-Q25). The air purge is essential and the snap-back wipe advantageous (03 A2); the purge gap is claimed by function and state in Formulations 2 and 3 and by the §3(6) location in Formulation 1. Blocking for P5 and REVIEW.

A3. "At-rest form" (Formulation 2 and 3) has the meaning of the `19` definition of deflectable ring element (the form to which the element recovers) and, in the normal-open state, is satisfied by the disclosed arrangement in which the purge shoulder does not contact the ring element (§3(4)); the description will state this expressly. Blocking for P5 (25) if the statement is not added.

A4. Pressure differential is supply-side pressure less chamber-side pressure and the poppet opens towards the chamber side (`01` A3-A5; `19` A4). Blocking for P5 only if 01 Q3/Q4 reverse it.

A5. Rule 43(2) EPC applies to a European filing with the default US/EPO/UK jurisdictions of `USER.md`; the recommendation against a second apparatus independent claim rests on it. Not blocking; counsel's call.

A6. The `22` disclosure requests (formation genus, threshold-setting structures, purge gap species, shape recovery modes) are carried forward unchanged and are not repeated except where a formulation adds a need. Not blocking.

## Open Questions

Q1. Where is the purge gap and how does it open against the interference fit (01 Q1, Q2)? Decides whether Formulation 1 can be used at all and whether the functional purge gap of Formulations 2 and 3 has an enabled species behind it. Blocks P5, REVIEW.

Q2. Is the deflectable ring element untouched by the poppet throughout the normal stroke, or merely undeflected (03 Q3; 22 Q6)? Decides whether "at-rest form" (Formulation 2) or "spaced from" (`22`) is the safer independent wording. Blocks P5.

Q3. Has any threshold-setting arrangement other than the first and second spring stages been conceived (01 Q6)? Decides how many corresponding structures the description must give for the pressure-band relationship of Formulation 2 under §112(f), and whether Formulation 1's spring-stage limitation is essential. Blocks P4, P5.

Q4. Is the pressure differential of the state definitions static or transient during pumping (01 Q4)? Formulation 2's pressure bands and Formulation 3's "raising" steps need the measurement basis defined. Blocks P4, P5.

Q5. Did the inventor conceive the deflectable ring element carried by the poppet with the deflecting formation on the core body (11 DA-8)? If yes, a carrier-neutral fourth formulation closes the last drafting-closable escape. Blocks P5.

Q6. Does the inventor want a standalone method claim asserted through inducement against sellers, given that the direct infringer is the rider (02 Q1, A3)? Decides whether Formulation 3 is kept as an independent claim or folded into an apparatus "configured to" dependent. Blocks P5.

Q7. Are Alternatives A and B within the invention (03 Q5)? Formulation 2's genus is drafted to cover both; if Alternative B is withdrawn the genus rests on one species and the seat ring wording of Formulation 1 becomes the safer noun. Blocks P5.

```json
{
  "prompt": "24",
  "status": "partial",
  "assumptions": [
    {"id": "A1", "text": "description.md does not exist; support cited to disclosure sections, 19 definitions, 01 state table and 16 blueprint ids; paragraph anchors mapped at Prompt 25.", "blocking": true},
    {"id": "A2", "text": "No Gate 1 answers; air purge essential and snap-back wipe advantageous (03 A2); purge gap claimed by function and state in Formulations 2 and 3 and by the §3(6) location in Formulation 1.", "blocking": true},
    {"id": "A3", "text": "'At-rest form' has the 19 meaning and is satisfied in the normal-open state by the disclosed non-contact arrangement (§3(4)); the description will state this expressly.", "blocking": true},
    {"id": "A4", "text": "Pressure differential is supply-side less chamber-side pressure and the poppet opens towards the chamber side (01 A3-A5; 19 A4).", "blocking": false},
    {"id": "A5", "text": "Rule 43(2) EPC applies to the European filing; the recommendation against a second apparatus independent claim rests on it.", "blocking": false},
    {"id": "A6", "text": "The 22 disclosure requests are carried forward unchanged and not repeated except where a formulation adds a need.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "Purge gap location and opening against the interference fit (01 Q1, Q2); decides whether Formulation 1 is usable and whether the functional purge gap has an enabled species.", "blocks": ["P5", "REVIEW"]},
    {"id": "Q2", "text": "Is the ring element untouched throughout the normal stroke, or merely undeflected (03 Q3; 22 Q6)? Decides 'at-rest form' versus 'spaced from' as the independent wording.", "blocks": ["P5"]},
    {"id": "Q3", "text": "Any threshold-setting arrangement other than the first and second spring stages (01 Q6)? Sets the §112(f) corresponding structures for Formulation 2 and the essentiality of Formulation 1's spring stages.", "blocks": ["P4", "P5"]},
    {"id": "Q4", "text": "Is the pressure differential static or transient during pumping (01 Q4)? Needed for the pressure bands of Formulation 2 and the raising steps of Formulation 3.", "blocks": ["P4", "P5"]},
    {"id": "Q5", "text": "Was the ring element carried by the poppet with the formation on the core body conceived (11 DA-8)? If yes, a carrier-neutral fourth formulation can be drafted.", "blocks": ["P5"]},
    {"id": "Q6", "text": "Does the inventor want a standalone method claim enforced through inducement (02 Q1, A3)? Decides whether Formulation 3 stays independent.", "blocks": ["P5"]},
    {"id": "Q7", "text": "Are Alternatives A and B within the invention (03 Q5)? Decides whether Formulation 2's genus rests on two species or one.", "blocks": ["P5"]}
  ],
  "new_terms": [
    {"term": "at-rest form", "maps_to": "shape recovery", "reason": "The 19 definition of deflectable ring element describes shape recovery 'toward its at-rest form'; used in Formulations 2 and 3 as the positive condition of the ring element in the closed state and the normal-open state."},
    {"term": "deflecting formation", "maps_to": "purge shoulder", "reason": "Locked genus of the purge shoulder (LOCKED Broader column); used in the Comparison and the not-drafted carrier-neutral formulation, as in 22."},
    {"term": "threshold-setting arrangement", "maps_to": "second spring stage", "reason": "Locked genus of the second spring stage (LOCKED Broader column); used in the Comparison for the structure Formulation 2 leaves open."},
    {"term": "axial clearance", "maps_to": null, "reason": "The spacing between the purge shoulder and the seat ring in the closed state and throughout the normal stroke (§3(4)), recited structurally in Formulation 1; the value is not disclosed (22 disclosure request)."},
    {"term": "inflation gas", "maps_to": null, "reason": "Any gas from the inflation device (12 E8.5 via 22; 16 S7.8), used in Formulation 3 so that CO2 inflation devices are covered."},
    {"term": "outer surface of the seat ring", "maps_to": "purge gap", "reason": "The LOCKED species column of purge gap names the 'seat ring outer surface' as one bounding surface (§3(6)); used in Formulation 1 to fix the gap location structurally."}
  ],
  "support_refs": [
    {"item": "Formulation 1: core body with core body bore and internal shoulder; seat ring received against the internal shoulder", "support": "intake/disclosure.md §3(2), §7; runs/r1/P4/19.md 'core body'; runs/r1/P4/16.md S8.3; registry.json 20, 22, 24, 30"},
    {"item": "Formulation 1: seat ring with sealing edge and convoluted wall of at least one convolution; axial load produces radial deflection", "support": "intake/disclosure.md §3(3) ('translates into radial expansion'), §6; runs/r1/P4/19.md 'seat ring', 'convoluted wall', 'radial deflection'; runs/r1/P4/16.md S8.4, S10.2; registry.json 32, 34"},
    {"item": "Formulation 1: purge shoulder on the chamber side of the sealing face, spaced from the seat ring in the closed state and throughout the normal stroke, bearing on it in over-travel", "support": "intake/disclosure.md §3(4) ('only contacts the ring during over-travel'), §4 (0.6 mm normal stroke); runs/r1/P4/19.md 'purge shoulder', 'normal stroke', 'over-travel'; runs/r1/P4/16.md S8.5, S9.2; registry.json 44"},
    {"item": "Formulation 1: first spring stage resists the normal stroke; second spring stage of higher rate engaged at the end of the normal stroke", "support": "intake/disclosure.md §3(5), §4; runs/r1/P2/09.md row 7; runs/r1/P4/19.md 'second spring stage', 'crack pressure', 'over-travel threshold'; runs/r1/P4/16.md S8.6, S9.3; registry.json 52, 54"},
    {"item": "Formulation 1: purge gap between the seat ring outer surface and the core body bore; closed in closed state and throughout the normal stroke; purge flow path separate from the main passage", "support": "intake/disclosure.md §3(6), §2; intake/drawings/README.md FIG-2 via runs/r1/P1/01.md (b)5; runs/r1/P4/19.md 'purge gap' (illustrated embodiment), 'purge flow path'; runs/r1/P4/16.md S8.7, S9.5; registry.json 60, 62, 64; conditional on 01 Q1, Q2"},
    {"item": "Formulation 1: shape recovery closes the purge gap when the axial load is removed", "support": "intake/disclosure.md §2; runs/r1/P4/19.md 'deflectable ring element', 'shape recovery' (LOCKED); runs/r1/P4/16.md S9.6"},
    {"item": "Formulation 2: closed state, normal-open state and purge state each fixed by a pressure differential band", "support": "runs/r1/P1/01.md (i) state table; intake/disclosure.md §2, §4; runs/r1/P4/19.md 'closed state', 'purge state', 'crack pressure', 'over-travel threshold', 'normal stroke', 'over-travel'; terminology/LOCKED.md 'normal-open state'; runs/r1/P4/16.md S9.1-S9.4"},
    {"item": "Formulation 2: deflectable ring element carried by the core body; poppet in over-travel deflects it radially", "support": "intake/disclosure.md §2, §3(3), §3(4), §6; runs/r1/P4/19.md 'deflectable ring element', 'over-travel', general construction (coupling); runs/r1/P4/16.md S7.4, S8.4, S9.3"},
    {"item": "Formulations 2 and 3: ring element in its at-rest form in the closed state and the normal-open state", "support": "intake/disclosure.md §3(4); runs/r1/P4/19.md 'deflectable ring element' ('shape recovery toward its at-rest form'); runs/r1/P4/16.md S9.2, S9.6; express statement requested"},
    {"item": "Formulations 2 and 3: purge gap associated with the deflectable ring element, closed in the two lower states, opened by radial deflection; purge flow path separate from the main passage to the chamber side", "support": "runs/r1/P4/19.md 'purge gap', 'purge flow path' (verbatim); intake/disclosure.md §2, §3(6); FIG-2; runs/r1/P4/16.md S7.5, S9.4, S9.5, S11.1; conditional on 01 Q1, Q2"},
    {"item": "Formulations 2 and 3: shape recovery when the pressure differential falls below the over-travel threshold", "support": "intake/disclosure.md §2; runs/r1/P4/19.md 'snap-back wipe' (timing), 'deflectable ring element'; intake/data/bench-test.md (audible snap on removal); runs/r1/P4/16.md S9.6"},
    {"item": "Formulation 3: inflatable chamber holding liquid sealant; coupling and removing the inflation device; single inflation event", "support": "intake/disclosure.md §1, §2, §8; runs/r1/P1/01.md (d) S1-S5; runs/r1/P2/09.md row 1 ('in the same inflation event'); runs/r1/P4/19.md 'inflatable chamber', 'liquid sealant', 'inflation event'; runs/r1/P4/16.md S9.1, S9.9"},
    {"item": "Formulation 3: air purge of inflation gas along the purge flow path across the surfaces on which sealant film accumulates, into the inflatable chamber", "support": "intake/disclosure.md §2, §8; runs/r1/P4/19.md 'air purge' (verbatim), 'sealant film'; CONFIRMED.md 12 E8.5 via runs/r1/P5/22.md; runs/r1/P4/16.md S7.8, S9.5"},
    {"item": "Comparison: prior-art exposure column", "support": "runs/r1/P2/07.md charts (ref-02 claim 4, [0019], [0020]; US4462449A claim 1; EP1137892A1 claims 1(e), 8, 28; US9982818B2; CN215861914U); runs/r1/P2/08.md items 1-4, N2, N3, N5; runs/r1/P2/09.md rows 1-7"},
    {"item": "Comparison: design-around column", "support": "CONFIRMED.md 11 DA-1 to DA-22 and 12 E2.3, E3.2, E5.5, §7 via runs/r1/P5/22.md; runs/r1/debate/d2-attack.md R2, R4, R5, R7, R9, R16 via 22; runs/r1/P1/02.md rank 8, A3"},
    {"item": "Comparison: commercial weighting of the method claim", "support": "runs/r1/P1/02.md rank 8, A3, Q1"}
  ],
  "disclosure_requests": [
    {"limitation": "Formulations 2 and 3: 'the deflectable ring element is in its at-rest form' in the closed state and in the normal-open state", "needed_disclosure": "An express statement in the operation section (16 S9.1, S9.2) that throughout the normal stroke the deflectable ring element remains in its at-rest form, undeflected, the purge shoulder not contacting it in the illustrated embodiment, and that 'at-rest form' means the form to which the element returns on shape recovery (19 'deflectable ring element')."},
    {"limitation": "Formulation 2: 'the valve core having: the closed state, at a pressure differential below a crack pressure ...; a normal-open state, at a pressure differential at or above the crack pressure and below an over-travel threshold ...; and a purge state, at a pressure differential above the over-travel threshold'", "needed_disclosure": "The 01 (i) state table reproduced in the description (16 S9.1) with each state tied to its pressure differential band in those words, and a definition of how the pressure differential is taken during pumping (static or transient; 01 Q4)."},
    {"limitation": "Formulation 2: 'the poppet ... deflects the deflectable ring element radially' with no formation named", "needed_disclosure": "As the second 22 disclosure request (16 S7.6, S11.3): the genus statement that the part of the poppet which bears on the deflectable ring element is the purge shoulder in the illustrated embodiment and may be the sealing face or a continuation of it, a taper, a collar or lugs."},
    {"limitation": "Formulation 1: 'the second spring stage being engaged at the end of the normal stroke' and 'the purge shoulder is spaced from the seat ring by an axial clearance in the closed state and throughout the normal stroke'", "needed_disclosure": "An express statement (16 S8.5, S8.6, S9.2) that the second spring stage engages at the end of the normal stroke, and the axial clearance between the purge shoulder and the seat ring in the closed state stated as at least the normal stroke (0.6 mm in the prototype), subject to inventor confirmation (01 Q7)."},
    {"limitation": "Formulation 1: 'a purge gap (60) between an outer surface of the seat ring and the core body bore'", "needed_disclosure": "Reconciliation of §2 (stem bore, outward flexing) with §3(6) (core body bore) and with the 0.03 mm interference fit of §7 (01 Q1, Q2), and a description of how a radial clearance opens at the bore when the seat ring is pressed into it; without it Formulation 1 must not be used."},
    {"limitation": "Formulation 3: 'within a single inflation event' the closed state, normal-open state, purge state and shape recovery occur in sequence", "needed_disclosure": "An express statement (16 S9.9) that in one inflation event with a floor pump or a CO2 inflation device the valve core passes from the closed state through the normal-open state into the purge state as the pressure differential rises past the crack pressure and the over-travel threshold, and returns through shape recovery when the inflation device is removed, with the bench observation of an audible snap on each removal."},
    {"limitation": "Formulation 3: 'across surfaces of the valve core on which sealant film accumulates'", "needed_disclosure": "An express statement (16 S9.5) naming those surfaces from §1, §2 and §8 (the sealing edge, the sealing face, the poppet stem and the outer surface of the seat ring in the purge gap region) as the surfaces the purge flow path crosses."},
    {"limitation": "Not drafted: carrier-neutral formulation with the deflectable ring element and the deflecting formation each carried by one of the poppet and the core body (11 DA-8)", "needed_disclosure": "Only if the inventor confirms the ring element carried by the poppet was conceived: an express embodiment (16 S11) of a deflectable ring element on the poppet deflected by a formation of the core body in over-travel, with the purge gap and shape recovery described for that arrangement."}
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

## Files you may read (not embedded: open only what you need)

- `/Users/ahmed/PatentCouncil/lessons.md`

## Files to write

Write each of these with your Write tool, at exactly this path, one file per call (the folders exist). Write nothing outside the run folder `{R}`. Do not run the checks yourself: the runner runs them and will tell you if anything fails.

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/25.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/claims.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/support-map.json`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/unsupported.md`

When every file is written, reply with one line per file (path and a few words on what it holds) and anything the runner must route: open questions, disclosure requests, open disagreements, narrowing suggested. Nothing else.
