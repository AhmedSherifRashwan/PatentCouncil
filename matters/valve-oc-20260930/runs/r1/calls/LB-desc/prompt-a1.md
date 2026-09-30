# Patent Council · matter `valve-oc-20260930` · run `r1` · step `LB-desc` · profile full

You are the **Specification Drafter**. Follow your AGENTS.md. This message is the whole brief: what to do, the prompts to execute, every input (embedded below, so do not re-read those files), and the exact files to write.

## What to do

Fix ONLY the upheld findings in the embedded findings file, plus the reviewers' mechanical corrections (embedded). Prefer added disclosure to narrowing; a narrowing you consider necessary goes in `narrowing_suggested` for the human, never applied. Novelty and design-around findings are answered by adding disclosure drawn from CONFIRMED.md and the attacks' closed escape routes, never by inventing embodiments. Also answer every item in `P5/unsupported.md` and `P4/enablement-gaps.md` (embedded if they exist).

**Do not re-type the description.** Under `### Description` in your Deliverable, give ONLY edit blocks against the numbered paragraphs of the description embedded below, each starting on its own line:

```
@@ REPLACE [0042]
<the full new text of paragraph 0042; more paragraphs may follow>
@@ AFTER [0042]
<one or more new paragraphs (or #### headings) to insert after 0042>
@@ DELETE [0042]
```

No paragraph numbers inside the new text (the runner numbers inserted paragraphs 0042a, 0042b ...). Use reference numerals exactly as in the registry and locked terms verbatim. Under `### Change Log` list each edit with the finding ids it answers. Then write `CHANGED-desc.md`: one line per finding id addressed, with the paragraphs changed.

Findings routed to you: F-28-1, F-28-2, F-28-3, F-30-6, F-32-1, F-32-2, F-32-20, F-32-4, F-33-2, F-33-4, F-36-1, F-36-2, F-gate14-2, F-gate14-4, F-gate14-5, F-30-7, F-gate14-1.

**Time budget:** about 15 minutes. The whole matter is planned to finish end to end in two hours. Be complete, but write each deliverable once: no drafts, no repetition, no padding.

## Prompt x-p4-revise — Revise the Description  (kind `revise`)

**Write your reply to:** `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/loop/c1/x-p4-revise.md`

*Runner template: inner-loop round 2+ and loop-back re-entry into Phase 4. Revise, do not restart.*

Revise the current Description embedded below so that it satisfies each disclosure request from the claims drafter and each finding routed to Phase 4, by ADDING disclosure that is already within the inventors' conception as recorded in the confirmed embodiments (`CONFIRMED.md`). Never narrow the described scope to fit a claim or to answer a finding; if a request or finding can only be satisfied by narrowing or by matter the confirmed embodiments do not contain, leave the text unchanged on that point and report why. Keep every existing paragraph number stable; insert new paragraphs with the next free numbers at the end of the relevant section or as lettered sub-numbers ([0042a]) where the jurisdiction convention allows, and say which convention you used. Keep every reference numeral consistent with the registry; if a newly described component needs a numeral, use the next free numeral in the appropriate series and list it so the registry can be updated. Then list every change.

**How to work.** Work request by request and finding by finding. Under `### Description` return the complete revised Description (the runner replaces `description.md` with this section verbatim, so it must be whole, numbered and free of notes). Under `### Change Log` give a table: change id | trigger (disclosure request text, finding id, correction, or open disagreement) | location (paragraph numbers) | change (added / amended / not changed) | text added or amended (quoted) | basis in `CONFIRMED.md` (which confirmed embodiment) | note. A request you could not satisfy from confirmed material stays in `disclosure_requests` in the envelope, re-addressed to the human, with the reason; a disagreement with the claims drafter you still hold goes in `open_disagreements`. Use locked terms verbatim. Reply exactly in the drafting output contract: `## Deliverable` (with the H3 sections named above), `## Rationale`, `## Assumptions`, `## Open Questions`, then one final fenced `json` envelope. No preamble before `## Deliverable`; nothing after the envelope. Reuse locked preferred terms verbatim; declare any other term in `new_terms` with a reason.

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

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P4/17.md`

````markdown
## Deliverable

### Enablement Audit

This audit is a drafting and analysis aid prepared by AI. It is not legal advice and says nothing about patentability; qualified patent counsel signs off before anything is filed.

**What was audited.** The stitched `description.md` ([0001]–[0180]), read against `CONFIRMED.md`, the Phase 1 outputs (`01`, `03`), the differentiation matrix (`09`), the locked terminology and the bench data. No Gate 1 answers exist, so every Phase 1 open question is treated as unanswered. The audit asks one question of each scope element: could the person skilled in the art practise it, across the full breadth the description claims for it, from this text without undue experimentation and without fabricated facts. Paragraph anchors are those of `description.md`.

**Severity.** *Critical*: the nucleus (claim family CF-A) cannot be practised as described for the illustrated embodiment. *High*: a principal embodiment or a claim family is unsupported across its stated breadth. *Medium*: an alternative embodiment, a dependent claim or a parameter is at risk. *Low*: a reproducibility or clarity detail.

**Headline finding.** The description does not state, for the illustrated embodiment, how the purge gap (60) opens or how the purge flow path (62) gets from the supply side past the internal shoulder (24) into the inflatable chamber (EN-1, EN-2, EN-21). The text offers coherent species ([0036], [0054], [0103], [0109], [0110]) but names none as the prototype's, and in several places it pairs outward radial deflection with a purge gap at the outer surface of the seat ring (30) against the core body bore (22), which is the pairing `01` Q2 and `03` found unexplained. Until the inventor answers, the nucleus is enabled only as a genus of described species, not as the tested mechanism, and the Examiner will say so. Everything else in the audit is curable by drafting or is ordinary dependent-claim risk.

| id | scope element (locked term) | issue type | severity | what would cure it |
|---|---|---|---|---|
| EN-1 | purge gap; purge flow path; interference fit; internal shoulder — illustrated embodiment. [0036], [0040], [0053], [0056], [0059], [0155]–[0156] | missing conditions | critical | **Inventor** (01 Q1, Q2; 03 Q2): which surfaces bound the purge gap (60) in the prototype; which axial band of the seat ring (30) carries the interference fit; the complete route of the purge flow path (62) from the supply side, past the interference fit and the internal shoulder (24), into the inflatable chamber. **Drafter, now**: [0056] and [0059] assert a complete purge flow path for the illustrated embodiment that the text does not describe past the internal shoulder; revise so that the route past the ring retention is stated as a species (clearance beyond the axial band of the interference fit; flutes (362); purge ports (262)) without naming one as the prototype's. No narrowing closes this gap; CF-A support for the purge gap (matrix row 2 of `09`) stays conditional. |
| EN-2 | radial deflection (sense) paired with purge gap location. [0020], [0040], [0053], [0054], [0093], [0103], [0113], [0162] | missing conditions (internal inconsistency) | critical | **Drafter, now**: [0020] states "in the illustrated embodiment the radial deflection is outward" while [0040] and [0053] place the purge gap (60) between the outer surface of the seat ring (30) and the core body bore (22), and [0103] explains that such a gap opens by *inward* movement of the bounding surface. [0093] and [0162] make the same outward-plus-outer-surface pairing for the wiper ring (132). [0113] has the tapered purge shoulder (244) expand the seat ring (30) outward without saying where its purge gap is. Revise each so that no passage pairs a sense of radial deflection with a purge gap location that the sense cannot open, unless the passage says how; for [0113] cite the inner-surface ([0105]) or through-wall ([0106]) species. **Inventor** (01 Q1, Q2): the sense of radial deflection actually observed at the surface that bounds the purge gap. |
| EN-3 | purge shoulder: where it bears, its geometry, axial clearance at rest. [0038], [0046], [0088] | parameter unexplained | medium | **Drafter, now**: [0046] defines the normal stroke as displacement up to first contact, so the axial clearance between the purge shoulder (44) and the seat ring (30) at rest equals the normal stroke (0.6 mm in the prototype); say so in [0038]. **Inventor** (01 Q8): whether the purge shoulder (44) bears on the end of the seat ring (30) at the sealing edge (34), on its inner surface, or on a convolution, and its diameter. |
| EN-4 | second spring stage; threshold-setting arrangement; crack pressure; over-travel threshold (rates, engagement stroke, effective area, sealing face cone angle). [0039], [0048], [0119] | parameter unexplained | medium | **Drafter, now**: no spring rate, preload or poppet effective area is given, so the skilled person cannot size a return spring (50) to the stated crack pressure and over-travel threshold without design work; add the design relation (force on the poppet (40) = pressure differential × effective area at the sealing edge (34); first spring stage (52) preload sets the crack pressure; second spring stage (54) engagement and rate set the over-travel threshold; both verified by measuring the pressure differential at which the poppet (40) lifts and at which the purge shoulder (44) contacts the seat ring (30) on the assembled valve core). No numbers. **Inventor** (01 Q7, Q9): rates, engagement stroke, whether engagement coincides with purge shoulder contact, cone angle of the sealing face (42). |
| EN-5 | over-travel distance; over-travel stop. [0049], [0174] | missing conditions | medium | **Inventor** (01 Q36): what limits over-travel to 0.5 mm in the prototype. [0049] lists three alternatives with none identified; [0174] promises that over-travel "cannot exceed the recoverable strain" in some embodiments, which is only true if an over-travel stop or coil-bind, not the seat ring (30), is the limit. Keep [0174] hedged as "in some embodiments" until answered. |
| EN-6 | over-travel threshold close to crack pressure; purge state on every opening; single-rate return spring. [0051] | functional breadth; no example | medium | **Inventor** (03 Q3; 11 DA-1): whether deflection on every opening keeps leak-down and fatigue acceptable. Not built. **Drafter, now**: add that this embodiment has not been tested; keep "in some embodiments". **Narrowing**: do not claim it independently of a threshold-setting arrangement until confirmed. |
| EN-7 | cleaning action: snap-back wipe alone; air purge alone. [0014], [0023], [0065], [0124], [0167] | functional breadth | high | **Inventor** (03 Q1; 01 Q24): whether the air purge alone, the snap-back wipe alone, or both produce the effect. **Drafter, now**: [0014] defines the deflectable ring element as deflected "so as to open a purge flow path", but the wipe-only embodiment of [0065] seals the ring element at its periphery so that no purge flow path opens; reconcile the definition with the embodiment, and state that neither the wipe-only nor the purge-only embodiment has been tested. **Narrowing**: no independent claim to wipe-only or purge-only cleaning until 03 Q1 is answered. |
| EN-8 | snap-back wipe: which surface moves across which, direction, distance. [0060]–[0062], [0124] | missing conditions | medium | **Inventor** (01 Q10). **Drafter, now**: [0062] states as the illustrated mechanism that the region of the sealing edge (34) wipes the sealing face (42); §2 says only "wipes across the poppet face". Soften [0062] to the sealing face (42) or an adjacent surface of the poppet (40), as [0060] already does, so the figure instruction for FIG. 4 does not assert a geometry the inventor has not given. |
| EN-9 | ranges: seat ring inner diameter; seat ring wall thickness; seat ring free length; convolution amplitude; purge gap opening; over-travel distance; crack pressure; over-travel threshold. [0006], [0088]–[0091], [0146] | functional breadth (endpoints unevidenced; intermediate and preferred rungs are drafting proposals) | medium | **Inventor** (01 Q15; 03 Q13): basis of each §4 endpoint beyond the prototype value. The combination of endpoints is not shown to be self-consistent (for example seat ring wall thickness 0.30 mm with purge gap opening 0.25 mm within recoverable strain). [0088] gives the relationships that govern and [0091] says only the prototype was built; that is the honest position and should stay. **Drafter, now**: [0091] and [0146] state that ranges are adapted for a resilient polymer, a resilient metal or a wiper ring (132) but give no guidance; add that no range is stated herein for those materials and that the relationships of [0088] govern. **Narrowing**: numeric dependent claims limited to the superelastic seat ring (30) with a convoluted wall (32). |
| EN-10 | austenite finish temperature; martensite start temperature. [0026], [0035], [0073], [0100], [0171] | parameter unexplained | medium | **Drafter, now**: no measurement method is defined; add to [0026] that the austenite finish temperature is determined by differential scanning calorimetry or an equivalent standard method (a definitional convention, not a fact about the prototype). **Inventor** (01 Q13, Q28): achieved austenite finish temperature, how measured, martensite start temperature. **Experiment recommended before filing**: measure the transformation temperatures of one prototype seat ring (30); optionally a cold-shock test with a compressed-CO2 inflation device, since [0100] and [0171] can now only say "not tested". |
| EN-11 | shape-setting; electropolishing (process window; depth removed). [0148], [0149], [0175] | parameter unexplained | low | The single working point (500 °C, 10 min, water quench) enables Example 1. **Inventor** (01 Q32): the window and the electropolishing depth, for the production verification options in [0175]. No drafting cure. |
| EN-12 | convoluted wall; number of convolutions; laser cutting (which step forms the convolution). [0034], [0079], [0147], [0155]–[0156] | missing conditions | medium | **Inventor** (01 Q11): the prototype's number of convolutions and which step imparts the radial excursion. **Drafter, now**: Example 1 ([0155]–[0156]) is silent on the count; state that the count of the prototype seat rings is not recorded, so the worked example is not read as either species; [0147] should not imply that laser cutting alone imparts a radial excursion unless the inventor confirms it. |
| EN-13 | axial-to-radial conversion geometry alternatives: frustoconical wall (232); slotted wall (332); cellular wall (432); conical annular disc; plain wall with tapered purge shoulder (244). [0081]–[0084] | no example | low | Prophetic alternatives, adequately hedged; the skilled person can design each from the relation in [0084]. [0082] already says the conical annular disc gives small radial movement. **Narrowing**: no numeric ranges are to be claimed for these geometries. |
| EN-14 | resilient polymer seat ring (PEEK; PPS; PEI). [0076], [0091], [0146], [0161] | no example; unpredictable (creep under a sustained interference fit; moulding a 0.20 mm wall over 3.0 mm) | medium | **Inventor** (01 Q20; 03 Q5): confirm PEEK is within the conception and whether any dimensioning was done. **Experiment recommended**: build one PEEK seat ring (30) to Example 2 before relying on CF-I. **Drafter, now**: [0161] should say that no dimensions are given for the polymer seat ring and that [0088] governs. |
| EN-15 | resilient metal deflectable ring element; ternary NiTi; copper-based superelastic alloys. [0074], [0075] | no example | low | Conditional language is present ([0074] ammonia-free liquid sealant only; [0075] thinner wall or slotted wall). Adequate for genus support; no dependent claim to a specific alloy without inventor confirmation (01 Q14). |
| EN-16 | wiper ring; fixed seat. [0016], [0055], [0093], [0125], [0162] | missing conditions | medium | **Inventor** (01 Q20; 03 Q7): form, thickness, ring retention of the wiper ring (132), and whether it wipes the poppet (40). **Drafter, now**: fix the sense-versus-location pairing in [0093] and [0162] (EN-2); [0093]'s statement that form, thickness and retention "follow from the material and geometry selected" is the most that can be said. **Narrowing**: CF-H stays a dependent family. |
| EN-17 | threshold-setting arrangement species: seat ring stiffness alone; detent (354); auxiliary spring (254); separate purge actuator. [0120]–[0123] | no example | low | Conventional mechanisms, hedged. **Drafter, now**: add that in every species the over-travel threshold is verified on the assembled valve core by measuring the pressure differential at which the deflecting formation contacts the deflectable ring element (same sentence as EN-4). [0123] already limits the purge actuator to larger-bore valve cores. |
| EN-18 | over-travel by mechanical depression or by hand; purge state during deflation with reversed flow. [0066], [0067] | functional breadth; no example | medium | **Inventor**: whether user-actuated over-travel and purge during deflation are within the conception (12 E1.4, E1.5 conflict with §2 "no tool and no rider action"; 11 DA-9, DA-20). **Drafter, now**: [0067] asserts that reversed flow carries sealant film out of the valve core; not tested, and the flow then carries liquid sealant towards the inflation device; hedge to "may" and state not tested. |
| EN-19 | valve core formats: Schrader-pattern; Dunlop-pattern; non-removable inflation valve. [0136]–[0138] | no example | low | Schematic disclosure with the scaling statement of [0091] is adequate for genus support. **Inventor** (01 Q26): conception. No drafting cure. |
| EN-20 | inverted arrangement (deflectable ring element carried by the poppet); integral flexure section; polymer core body. [0096], [0117], [0131] | no example | low | One-sentence disclosures, adequate to keep the genus open but not to support a dependent claim with structure. **Narrowing**: no claim to these without further disclosure. |
| EN-21 | closed state: the purge gap "closed"; the seal of the purge flow path at rest. [0018], [0036], [0037], [0040], [0045] | missing conditions | high | The purge flow path (62) is parallel to the main passage (64) and bypasses the sealing edge (34). Whatever closes the purge gap (60) at rest is therefore part of the closed-state seal, yet [0037] and [0040] say the seal is formed at the sealing edge (34) only, and [0036] frees the outer surface of the seat ring (30) from the core body bore (22) away from the interference band. **Inventor** (01 Q31; 03 Q11): what makes the closed purge gap airtight. **Drafter, now** (15 FM-22 recommendation): state in [0040] that in the closed state the purge flow path (62) is closed at the purge gap (60) by contact between the deflectable ring element and the surface that bounds the purge gap, or by the ring retention, and that the pressure-retaining seal between the supply side and the chamber side is at the sealing edge (34); stated as species, none named as the prototype's. |
| EN-22 | core body bore (diameter at the seat ring); seat ring outer diameter (inferred). [0033], [0089] | parameter unexplained | medium | **Inventor** (01 Q16; 01 A2): the core body bore (22) diameter at the seat ring (30), the actual seat ring outer diameter, and the at-rest radial clearance, if any, in the purge gap region. The purge gap opening of 0.15 mm cannot be placed without them. [0089] correctly labels 2.7 mm as nominal from tube stock. |
| EN-23 | thermally actuated purge. [0142] | unpredictable art; no example | medium (CF-M only) | **Inventor** (03 Q12; 01 Q21): keep or drop. If kept: two-way shape-memory behaviour requires a training treatment that is not described, and how the warmed deflectable ring element opens the purge gap (60) with the poppet (40) closed is not described. **Narrowing**: dependent claim or continuation only; [0142] already says not built or tested. |
| EN-24 | Example 1 reproducibility: liquid sealant product and ammonia content; floor pump; deflation method; whether over-travel or purge gap opening was ever measured. [0157]–[0159], [0165] | missing conditions | low | **Inventor** (01 Q23). [0156], [0158] and [0165] already state that over-travel distance and purge gap opening were not measured. **Experiment recommended before filing**: one direct measurement of over-travel distance and purge gap opening on a prototype, so that the worked example rests on more than the audible snap. |
| EN-25 | over-travel threshold reached by the inflation device (floor pump; hand pump; compressed-CO2 inflation device; compressor). [0011], [0058], [0090], [0179] | functional breadth | low | [0179] is properly hedged; [0011] says the threshold is "selected so that it is exceeded" with a floor pump, which is the design intent and is supported by Example 1. **Inventor** (01 Q5; 03 Q9): basis for "every floor pump". Optional experiment: measure the pressure differential at the pump head for a hand pump and a CO2 inflation device. |
| EN-26 | positively driven shape recovery; defined wiping edge; fixed wiping land; rotational wipe. [0099], [0126], [0127], [0149] | no example | low | Adequately hedged alternatives; no values claimed. No cure needed. |
| EN-27 | interference fit (working tolerance); supplementary ring retention. [0135], [0152], [0172] | parameter unexplained | low | **Inventor** (01 Q17): working range of the interference. [0172] already says the range has not been determined. No drafting cure. |

**Verdict by claim family (per the blueprint in `16`).**

- CF-A (valve core): enabled as a genus of described species; **not** enabled as the prototype mechanism until EN-1, EN-2 and EN-21 are answered. The three-state sequence (closed state, normal-open state, purge state) and the deflectable ring element are adequately described; the purge gap and purge flow path of the illustrated embodiment are not.
- CF-B (seat ring): enabled for the superelastic seat ring (30) with a convoluted wall (32) at the worked-example values; the ranges rest on relationships plus one built point (EN-9); the convolution count of the prototype is unrecorded (EN-12).
- CF-D (method of use): enabled as the sequence of states; the cleaning action is enabled as "air purge, snap-back wipe, or both" only (EN-7).
- CF-E, CF-F, CF-G (manufacture, assembly, product-by-process): enabled at the single process point; windows absent (EN-11, EN-27).
- CF-H (fixed seat and wiper ring): enabled as a described alternative at genus level only (EN-16, EN-2).
- CF-I (material genus): resilient polymer is a prophetic embodiment with no dimensions (EN-14); resilient metal and other alloys hedged (EN-15).
- CF-J (threshold-setting arrangement): species described; sizing needs the design relation of EN-4; purge on every opening untested (EN-6).
- CF-K, CF-L: enabled; commercial intent open (16 Q5). CF-M: concept only (EN-23).

**Recommended before filing.** (1) Inventor answers to EN-1, EN-2 and EN-21 (01 Q1, Q2, Q16, Q31) are mandatory; nothing else in this audit matters as much. (2) Four short experiments would convert prophetic or hedged text into results: direct measurement of over-travel distance and purge gap opening on one prototype (EN-24); transformation temperatures of one prototype seat ring (30) by a standard method (EN-10); one PEEK seat ring (30) built to Example 2 (EN-14); a cold-shock test with a compressed-CO2 inflation device (EN-10). (3) The drafting fixes listed under "Drafter, now" are made in the fix pass from confirmed material and add no matter; they are listed one per line in `P4/enablement-gaps.md`.

## Rationale

The audit ranks the purge gap problem first because the nucleus depends on it and because the stitched text, in trying to keep every species open, has in places asserted both halves of the inventor's inconsistency at once ([0020] outward; [0040] gap at the outer surface). The description's own paragraph [0103] contains the reconciliation (inward movement of the bounding surface, or a fit confined to a band), so the fix is to stop asserting a mechanism for the illustrated embodiment rather than to add one. I did not resolve the inconsistency by choosing a mechanism: any choice would be an invented fact about the prototype.

EN-21 is rated high, above most of the alternatives, because it is a leak-path argument an Examiner will make from the text alone: a purge flow path parallel to the main passage must be sealed at rest by something, and the description says the only seal is at the sealing edge. `15` FM-22 already recommended the express statement; the compose step did not make it.

The design relation for the return spring (EN-4) and the measurement convention for the austenite finish temperature (EN-10) are recommended as drafting additions because they are general engineering knowledge that enable the stated parameters, not facts about the invention; they contain no numbers and assert nothing the inventor has not said.

Alternatives from `12` (EN-13, EN-15, EN-17, EN-19, EN-20, EN-26) are rated low: they are hedged prophetic embodiments that keep the genus open, and the skilled person can design each from conventional practice. They are not enabled for dependent claims with structure, which is recorded as narrowing.

Intermediate and preferred rungs of the ranges ([0089], [0090]) are drafting proposals from `13`, not data. The description is honest about this in [0091]; the audit records the breadth risk but does not recommend removing the rungs, because they are within the inventor's stated broad range and the fallback value outweighs the risk.

## Assumptions

A1. No Gate 1 answers exist; every open question in `01` and `03` is unanswered. Blocking for the fix pass on EN-1, EN-2 and EN-21.

A2. The unattended Gate 2 confirmation is treated as permitting the `12` alternatives to be described with hedged language; the audit rates them on that footing and does not ask whether they should be present. Not blocking for P4; blocking for PACKAGE (human review at Gate 3).

A3. `01` A3–A5 carry forward: the pressure differential is supply side less chamber side; the poppet opens towards the chamber side. Blocking for the figures until 01 Q3, Q4 are answered.

A4. Enablement is judged to the standard common to the US, EPO and UK (practicable across the claimed breadth without undue experimentation); no jurisdiction-specific difference changes any row. Not blocking.

A5. The design relation of EN-4 and the measurement convention of EN-10 are treated as common general knowledge that may be added without new matter. Not blocking; counsel confirms.

## Open Questions

Q1. Which surfaces bound the purge gap (60) in the prototype, which axial band of the seat ring (30) carries the interference fit, and what is the complete route of the purge flow path (62) from the supply side past the internal shoulder (24) into the inflatable chamber (01 Q1, Q2)? Blocks P4 (fix pass), P5, REVIEW.

Q2. In which sense does the surface of the seat ring (30) that bounds the purge gap (60) move in the prototype: outward, inward, or non-uniformly (01 Q1, Q2)? Blocks P4, P5.

Q3. What makes the closed purge gap airtight at rest, or is the sealing edge (34) the only seal (01 Q31; 03 Q11)? Blocks P4, P5.

Q4. What is the core body bore (22) diameter at the seat ring (30), the actual seat ring outer diameter, and the at-rest clearance in the purge gap region (01 Q16)? Blocks P4.

Q5. Where does the purge shoulder (44) bear on the seat ring (30), and what is its geometry (01 Q8)? Blocks P4.

Q6. What are the rates and preloads of the first spring stage (52) and second spring stage (54), at what stroke does the second spring stage engage, does engagement coincide with purge shoulder contact, and what is the cone angle of the sealing face (42) (01 Q7, Q9)? Blocks P4, P5.

Q7. What limits over-travel to 0.5 mm in the prototype (01 Q36)? Blocks P4, P5.

Q8. Would the valve core work with the purge state reached on every opening, with a single-rate return spring (50) (03 Q3)? Blocks P5.

Q9. Does the air purge alone, the snap-back wipe alone, or both produce the effect (03 Q1; 01 Q24)? Blocks P4, P5.

Q10. Which surface of the seat ring (30) moves across which surface of the poppet (40) in the snap-back wipe, in what direction and over what distance (01 Q10)? Blocks P4, P5.

Q11. What is the basis of each §4 range endpoint beyond the prototype value, and are the endpoint combinations self-consistent (01 Q15; 03 Q13)? Blocks P5.

Q12. What austenite finish temperature was achieved, how was it measured, and what is the martensite start temperature (01 Q13, Q28)? Blocks P4, P5.

Q13. Did the prototype seat ring (30) have one or two convolutions, and which step imparts the radial excursion (01 Q11)? Blocks P4.

Q14. Is the PEEK seat ring (30) within the conception, and was any dimensioning done for it (01 Q20; 03 Q5)? Blocks P5.

Q15. For the wiper ring (132): form, thickness, ring retention, and whether it wipes the poppet (40) (01 Q20; 03 Q7)? Blocks P4, P5.

Q16. Are user-actuated over-travel and purge during deflation within the conception (12 E1.4, E1.5; 11 DA-9, DA-20)? Blocks P5.

Q17. Is the thermally actuated purge to be kept or dropped, and if kept, how is the two-way shape-memory behaviour obtained and how does the warmed ring open the purge gap (60) (03 Q12)? Blocks P5.

Q18. Example 1 details: liquid sealant product and ammonia content, floor pump, deflation method, and whether over-travel or purge gap opening was ever measured (01 Q23). Blocks P4.

```json
{
  "prompt": "17",
  "status": "complete",
  "assumptions": [
    {"id": "A1", "text": "No Gate 1 answers exist; every open question in 01 and 03 is unanswered.", "blocking": true},
    {"id": "A2", "text": "Unattended Gate 2 confirmation treated as permitting the 12 alternatives to be described with hedged language; human review at Gate 3.", "blocking": true},
    {"id": "A3", "text": "01 A3–A5 carry forward: pressure differential is supply side less chamber side; poppet opens towards the chamber side.", "blocking": true},
    {"id": "A4", "text": "Enablement judged to the standard common to US, EPO and UK; no jurisdictional difference changes a row.", "blocking": false},
    {"id": "A5", "text": "The return-spring design relation (EN-4) and the austenite finish temperature measurement convention (EN-10) are common general knowledge addable without new matter; counsel confirms.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "Surfaces bounding the purge gap in the prototype, axial band of the interference fit, and the complete purge flow path past the internal shoulder into the inflatable chamber (01 Q1, Q2).", "blocks": ["P4", "P5", "REVIEW"]},
    {"id": "Q2", "text": "Sense of movement (outward, inward, non-uniform) of the seat ring surface that bounds the purge gap in the prototype (01 Q1, Q2).", "blocks": ["P4", "P5"]},
    {"id": "Q3", "text": "What makes the closed purge gap airtight at rest, or is the sealing edge the only seal (01 Q31; 03 Q11)?", "blocks": ["P4", "P5"]},
    {"id": "Q4", "text": "Core body bore diameter at the seat ring, actual seat ring outer diameter, at-rest clearance in the purge gap region (01 Q16).", "blocks": ["P4"]},
    {"id": "Q5", "text": "Where the purge shoulder bears on the seat ring and its geometry (01 Q8).", "blocks": ["P4"]},
    {"id": "Q6", "text": "Spring stage rates and preloads, engagement stroke, coincidence with purge shoulder contact, sealing face cone angle (01 Q7, Q9).", "blocks": ["P4", "P5"]},
    {"id": "Q7", "text": "What limits over-travel to 0.5 mm in the prototype (01 Q36)?", "blocks": ["P4", "P5"]},
    {"id": "Q8", "text": "Would purge on every opening with a single-rate return spring work (03 Q3)?", "blocks": ["P5"]},
    {"id": "Q9", "text": "Air purge alone, snap-back wipe alone, or both (03 Q1; 01 Q24)?", "blocks": ["P4", "P5"]},
    {"id": "Q10", "text": "Snap-back wipe geometry: which seat ring surface across which poppet surface, direction, distance (01 Q10).", "blocks": ["P4", "P5"]},
    {"id": "Q11", "text": "Basis of each §4 range endpoint and self-consistency of endpoint combinations (01 Q15; 03 Q13).", "blocks": ["P5"]},
    {"id": "Q12", "text": "Achieved austenite finish temperature, measurement method, martensite start temperature (01 Q13, Q28).", "blocks": ["P4", "P5"]},
    {"id": "Q13", "text": "Prototype number of convolutions and which step imparts the radial excursion (01 Q11).", "blocks": ["P4"]},
    {"id": "Q14", "text": "Is the PEEK seat ring within the conception and was it dimensioned (01 Q20; 03 Q5)?", "blocks": ["P5"]},
    {"id": "Q15", "text": "Wiper ring form, thickness, ring retention, and whether it wipes the poppet (01 Q20; 03 Q7).", "blocks": ["P4", "P5"]},
    {"id": "Q16", "text": "Are user-actuated over-travel and purge during deflation within the conception (12 E1.4, E1.5; 11 DA-9, DA-20)?", "blocks": ["P5"]},
    {"id": "Q17", "text": "Keep or drop the thermally actuated purge; if kept, how the two-way behaviour is obtained and how the warmed ring opens the purge gap (03 Q12).", "blocks": ["P5"]},
    {"id": "Q18", "text": "Example 1 details: liquid sealant product and ammonia content, floor pump, deflation method, any direct measurement of over-travel or purge gap opening (01 Q23).", "blocks": ["P4"]}
  ],
  "new_terms": [
    {"term": "deflecting formation", "maps_to": "purge shoulder", "reason": "Locked genus of the purge shoulder; used for the tapered, lug, collar and retainer species as in 16."},
    {"term": "threshold-setting arrangement", "maps_to": "second spring stage", "reason": "Locked genus of the second spring stage; used for the non-spring species as in 16."},
    {"term": "axial-to-radial conversion geometry", "maps_to": "convoluted wall", "reason": "Locked genus of the convoluted wall; used for the frustoconical, slotted, cellular and disc species as in 16."},
    {"term": "resilient polymer", "maps_to": null, "reason": "Material genus for the PEEK seat ring and the PPS/PEI candidates, declared in 16; no locked polymer genus exists."},
    {"term": "resilient metal", "maps_to": "superelastic alloy", "reason": "Locked genus used for non-superelastic spring metals as in 16."},
    {"term": "over-travel stop", "maps_to": null, "reason": "Structural formation limiting over-travel (15 FM-9), declared in 16."},
    {"term": "ring retention", "maps_to": "interference fit", "reason": "Locked genus of the interference fit; used for crimp, sleeve, adhesive and integral species as in 16."},
    {"term": "purge port", "maps_to": "purge flow path", "reason": "Species of purge flow path through the core body wall (12 E8.2), declared in 16; numeral 262 in the description."},
    {"term": "flute", "maps_to": "purge flow path", "reason": "Species of purge flow path as axial grooves in the core body bore (12 E8.3); numeral 362 in the description."},
    {"term": "purge opening", "maps_to": "purge gap", "reason": "Covers slits, apertures and finger gaps through the wall of the deflectable ring element (11 DA-3) as well as the annular gap; declared in 16."},
    {"term": "wiping edge", "maps_to": "snap-back wipe", "reason": "Species of 12 E10.4 used in [0127] and [0149]; declared in 16."},
    {"term": "effective area", "maps_to": null, "reason": "General engineering quantity (area of the poppet on which the pressure differential acts at the sealing edge) needed to state the spring design relation in EN-4; not a component."}
  ],
  "support_refs": [
    {"item": "EN-1 purge gap and purge flow path of the illustrated embodiment unstated past the internal shoulder", "support": "description.md [0036], [0040], [0053], [0056], [0059]; 01 (m), Q1, Q2; 03 N0 enablement caution; 09 row 2"},
    {"item": "EN-2 outward radial deflection paired with a purge gap at the outer surface", "support": "description.md [0020], [0040], [0053], [0093], [0103], [0113], [0162]; intake/disclosure.md §2, §3(6), §7 via 01 (m)"},
    {"item": "EN-3 axial clearance equals the normal stroke", "support": "description.md [0012], [0046]; intake/disclosure.md §4 (normal stroke 0.6 mm)"},
    {"item": "EN-4 spring rates, effective area, cone angle absent", "support": "description.md [0039], [0048], [0119]; 01 Q7, Q9; 13 Table 4"},
    {"item": "EN-5 over-travel limit unstated", "support": "description.md [0049], [0174]; 01 Q36; 15 FM-9"},
    {"item": "EN-6 purge on every opening untested", "support": "description.md [0051]; CONFIRMED.md 11 DA-1; 03 Q3"},
    {"item": "EN-7 wipe-only and purge-only embodiments untested; definition conflict", "support": "description.md [0014], [0065], [0167]; CONFIRMED.md 11 DA-10; 03 A2, Q1; bench data (no separation of the two actions)"},
    {"item": "EN-8 wipe geometry asserted beyond §2", "support": "description.md [0060]–[0062]; intake/disclosure.md §2 via 01 (b)6; 01 Q10"},
    {"item": "EN-9 ranges believed not evidenced; intermediate/preferred rungs proposed", "support": "description.md [0088]–[0091]; intake/disclosure.md §4; CONFIRMED.md 13 Table 1; 14 footnote [d]"},
    {"item": "EN-10 austenite finish temperature measurement and martensite start temperature absent", "support": "description.md [0026], [0073], [0171]; 01 Q13, Q28; 13 Tables 2, 4"},
    {"item": "EN-11 single process point", "support": "description.md [0148], [0149]; intake/disclosure.md §7; 01 Q32; 15 FM-14, FM-17"},
    {"item": "EN-12 convolution count and forming step", "support": "description.md [0079], [0147], [0155]; 01 Q11; 13 Table 2"},
    {"item": "EN-13 alternative wall geometries prophetic", "support": "description.md [0081]–[0084]; CONFIRMED.md 12 E4.3, E4.4, E5.3, E5.4, E5.5"},
    {"item": "EN-14 PEEK seat ring not built", "support": "description.md [0076], [0161]; intake/disclosure.md §6 Alternative A; CONFIRMED.md 12 E15.4; 14 footnote [d]"},
    {"item": "EN-15 other alloys and metals hedged", "support": "description.md [0074], [0075]; CONFIRMED.md 12 E12.2–E12.4"},
    {"item": "EN-16 wiper ring details absent", "support": "description.md [0093], [0162]; intake/disclosure.md §6 Alternative B; 01 Q20; 03 Q7"},
    {"item": "EN-17 threshold-setting species prophetic", "support": "description.md [0120]–[0123]; CONFIRMED.md 12 E1.2, E2.2–E2.6"},
    {"item": "EN-18 mechanical/hand over-travel and purge during deflation", "support": "description.md [0066], [0067]; CONFIRMED.md 12 E1.4, E1.5; 11 DA-9, DA-20"},
    {"item": "EN-19 valve formats", "support": "description.md [0136]–[0138]; CONFIRMED.md 12 E16.2, E16.3"},
    {"item": "EN-20 inverted arrangement and integral flexure section", "support": "description.md [0096], [0117], [0131]; CONFIRMED.md 11 DA-8; 12 E4.5"},
    {"item": "EN-21 closed-state seal of the purge flow path", "support": "description.md [0018], [0036], [0037], [0040]; 01 Q31; 03 Q11; CONFIRMED.md 15 FM-22"},
    {"item": "EN-22 core body bore diameter absent; ring outer diameter inferred", "support": "description.md [0033], [0089]; 01 A2, Q16"},
    {"item": "EN-23 thermally actuated purge concept only", "support": "description.md [0142]; intake/disclosure.md §6 via 01 F5; 03 C32, Q12"},
    {"item": "EN-24 Example 1 reproducibility", "support": "description.md [0157]–[0159], [0165]; intake/data/bench-test.md; 01 Q23"},
    {"item": "EN-25 inflation device reach", "support": "description.md [0011], [0179]; intake/disclosure.md §2; 01 Q5; 03 Q9"},
    {"item": "EN-26 wiping alternatives", "support": "description.md [0099], [0126], [0127]; CONFIRMED.md 12 E9.4, E10.3–E10.5"},
    {"item": "EN-27 interference tolerance", "support": "description.md [0135], [0172]; intake/disclosure.md §7; 01 Q17; 15 FM-6, FM-7"}
  ],
  "disclosure_requests": [
    {"limitation": "EN-1 purge flow path of the illustrated embodiment, [0056], [0059]", "needed_disclosure": "Revise so the route past the ring retention and internal shoulder (24) is stated as species (clearance beyond the axial band of the interference fit; flutes (362); purge ports (262)) and no complete route is asserted for the prototype."},
    {"limitation": "EN-2 sense of radial deflection versus purge gap location, [0020], [0040], [0053], [0093], [0113], [0162]", "needed_disclosure": "Remove or qualify every pairing of outward radial deflection with a purge gap between the outer surface of the deflectable ring element and the core body bore (22); for [0113] cite the inner-surface or through-wall species."},
    {"limitation": "EN-3 axial clearance of the purge shoulder at rest, [0038]", "needed_disclosure": "State that the clearance equals the normal stroke by definition ([0046]); 0.6 mm in the prototype."},
    {"limitation": "EN-4 and EN-17 sizing of the threshold-setting arrangement, [0039], [0119], [0122]", "needed_disclosure": "Add the general design relation (pressure differential × effective area at the sealing edge; first spring stage preload sets the crack pressure; second spring stage sets the over-travel threshold; verified on the assembled valve core), with no numbers."},
    {"limitation": "EN-6, EN-7, EN-18 untested embodiments, [0051], [0065], [0066], [0067]", "needed_disclosure": "Add an express 'not tested' statement to each; hedge [0067]'s assertion that reversed flow carries sealant film out of the valve core to 'may'."},
    {"limitation": "EN-7 definition of the deflectable ring element, [0014]", "needed_disclosure": "Reconcile 'so as to open a purge flow path' with the wipe-only embodiment of [0065] in which the periphery is sealed."},
    {"limitation": "EN-8 snap-back wipe geometry, [0062]", "needed_disclosure": "Soften to 'the sealing face (42) or an adjacent surface of the poppet (40)', matching [0060] and §2."},
    {"limitation": "EN-9 and EN-14 ranges for other materials, [0091], [0146], [0161]", "needed_disclosure": "State that no range is given for a resilient polymer, a resilient metal or a wiper ring (132) and that the relationships of [0088] govern."},
    {"limitation": "EN-10 austenite finish temperature measurement, [0026]", "needed_disclosure": "Add the definitional convention: determined by differential scanning calorimetry or an equivalent standard method."},
    {"limitation": "EN-12 number of convolutions in Example 1, [0155]–[0156], [0147]", "needed_disclosure": "State that the count of the prototype seat rings is not recorded; do not imply that laser cutting alone imparts the radial excursion."},
    {"limitation": "EN-21 closed-state seal of the purge flow path, [0040]", "needed_disclosure": "State that in the closed state the purge flow path (62) is closed at the purge gap (60) by contact between the deflectable ring element and the surface bounding the purge gap, or by the ring retention, as species, and that the pressure-retaining seal is at the sealing edge (34)."}
  ],
  "open_disagreements": [],
  "narrowing_suggested": [
    "No independent claim to cleaning by the snap-back wipe alone or the air purge alone until 03 Q1 is answered (EN-7).",
    "No claim to the purge state on every opening independent of a threshold-setting arrangement until 03 Q3 is answered (EN-6).",
    "Numeric dependent claims (ranges of [0089], [0090]) limited to the superelastic seat ring with a convoluted wall (EN-9).",
    "No numeric ranges claimed for the frustoconical, slotted, cellular or disc geometries (EN-13).",
    "No dependent claim with structure to the inverted arrangement or the integral flexure section (EN-20).",
    "Thermally actuated purge as a dependent claim or continuation only (EN-23).",
    "CF-H (fixed seat and wiper ring) as a dependent family only until 01 Q20 and 03 Q7 are answered (EN-16)."
  ]
}
```
````

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/loop/c1/findings-desc.json`

```json
{
 "findings": [
  {
   "id": "F-28-1",
   "source_prompt": "28",
   "category": "support",
   "severity": "high",
   "title": "Dimension and pressure ranges confined by the description to the superelastic convoluted seat ring but claimed generally",
   "claim_refs": [
    "67",
    "13",
    "16",
    "17",
    "35",
    "41",
    "42",
    "43",
    "57",
    "69",
    "70",
    "76",
    "77",
    "82"
   ],
   "spec_refs": [
    "[0028]",
    "[0088]",
    "[0089]",
    "[0090]",
    "[0091]",
    "[0146]",
    "[0161]"
   ],
   "attack": "[0088] and [0091] state that the ranges 'correspond to the superelastic seat ring (30) with a convoluted wall (32)' and are to be adapted for polymer, resilient metal, other geometries, wiper rings and larger bores; claims 67 (independent, no material), 76/77 (PEEK) and the dependent range claims apply them to all of those. Art 84 lack of support over the claimed scope; 'seat ring wall thickness' is defined only for a convoluted wall yet claimed via claim 8.",
   "least_narrowing_action": "Ask the inventor whether the ranges hold for PEEK, resilient metal and other geometries; if so, add that statement, remove the self-limiting sentences in [0091], [0146], [0161], and redefine seat ring wall thickness in [0028]. If not, narrowing is the only route: claim 67 takes 'formed from a superelastic alloy' and claims 76/77 lose the claim 67 ranges (scope given up: polymer or plain-metal seat rings of the claimed dimensions).",
   "requires_new_disclosure": true,
   "suggested_target": "P4",
   "reviewers": [
    "ip-reviewer",
    "ip-reviewer-b"
   ],
   "sources": [
    "28",
    "36",
    "29"
   ],
   "consensus": true,
   "ruling": "upheld",
   "ruling_reason": "Correct on the text. [0088] gives the ranges as those 'within which the mechanism is expected to operate with a seat ring (30) of that material and wall geometry'; [0091] 'The ranges correspond to the superelastic seat ring (30) with a convoluted wall (32)' and must be adapted for polymer, resilient-metal, other geometries, wiper ring (132) and larger bores; [0094], [0146] and [0161] repeat this. Claim 67 recites no material, claims 76-77 apply the claim 67 ranges to PEEK, and claim 16 on claim 8 has neither the convoluted wall nor the material. Best defence, [0006] (disclosure of a range is disclosure of every sub-range), does not answer it: it goes to sub-ranges, not to the material and wall to which [0088] ties them. The fix must also cover the combinations listed in F-28-4 (dismissed as its duplicate): claims 41-44 reached through claims 9, 24, 51-53 and 57, and claim 82, which recites no material or wall. The 'seat ring wall thickness' definition in [0028] (convoluted wall only) is part of this finding; see F-28-6."
  },
  {
   "id": "F-28-2",
   "source_prompt": "28",
   "category": "enablement",
   "severity": "high",
   "title": "Illustrated purge gap cannot open by the outward deflection described",
   "claim_refs": [
    "29",
    "30",
    "34",
    "72",
    "9"
   ],
   "spec_refs": [
    "[0020]",
    "[0040]",
    "[0053]",
    "[0054]",
    "[0093]",
    "[0103]",
    "[0110]",
    "[0159]",
    "[0162]",
    "Fig. 1",
    "Fig. 3",
    "Fig. 6",
    "Fig. 10B"
   ],
   "attack": "The description says the illustrated seat ring (and the wiper ring) deflects radially outward and thereby opens a purge gap between its outer surface and the core body bore; outward movement of an outer surface closes that clearance. [0103] itself says the gap opens only where the outer surface moves away from the bore. The FIG. 1 instruction draws a clearance there in the closed state, contrary to claim 1's 'purge gap ... closed'. Insufficiency and clarity objection against the only built embodiment and claims 29/30/72.",
   "least_narrowing_action": "Obtain the inventor's statement of the built mechanism; rewrite [0020], [0040], [0053], [0054], [0093], [0162] and the FIG. 1, 3, 6, 10B instructions to it, keeping [0103]-[0106] as alternatives; remove the closed-state clearance from FIG. 1. No claim narrowing.",
   "requires_new_disclosure": true,
   "suggested_target": "P4",
   "reviewers": [
    "ip-reviewer"
   ],
   "sources": [
    "28"
   ],
   "consensus": false,
   "ruling": "upheld",
   "ruling_reason": "Correct on the text. For the illustrated embodiment the purge gap is 'an annular radial clearance between the outer surface of the seat ring 30 and the core body bore 22' ([0018], [0040], [0053], [0102]), and 'In the illustrated embodiment the radial deflection is outward' ([0020]; [0054] 'radially outward, as described for the embodiment of FIG. 3'); FIG. 3 plan 'seat ring deflected radially outward, purge gap open'. [0103] states that such a gap 'opens where the bounding portion of the outer surface ... moves away from the core body bore', by inward or non-uniform movement, and [0110] likewise. An outer surface moving outward inside a rigid bore closes, not opens, that clearance. The wiper ring has the same contradiction ([0093], [0125], [0162], FIG. 10 plan: 'deflected outward ... opening a purge gap between the wiper ring's outer surface and the core body bore'). No passage reconciles it for the only built embodiment, and claim 29 read with claim 30, and claim 72, rest on it. The clearance drawn in the FIG. 1 closed state is dealt with under F-28-9. The rewrite must also cover the flutes (362) of [0110] and the FIG. 13B plan ('when the seat ring's outer surface moves inward'), raised in F-29-7."
  },
  {
   "id": "F-28-3",
   "source_prompt": "28",
   "category": "enablement",
   "severity": "high",
   "title": "Load path and purge exit of the illustrated embodiment cannot be reconstructed from the text",
   "claim_refs": [
    "1",
    "4",
    "21",
    "30",
    "31",
    "58",
    "79"
   ],
   "spec_refs": [
    "[0010]",
    "[0036]",
    "[0038]",
    "[0046]",
    "[0052]",
    "[0053]",
    "[0056]",
    "[0059]",
    "[0079]",
    "[0088]",
    "[0105]",
    "[0112]",
    "[0116]",
    "Fig. 3",
    "Fig. 6"
   ],
   "attack": "The poppet opens chamber-ward ([0046]); the purge shoulder is on the chamber side of the sealing face ([0038]); the seat ring is seated against the internal shoulder at the end opposite the sealing edge ([0079]) which [0116] places on the chamber side; the purge gap is the outer clearance with the interference band at the internal shoulder ([0036], [0053]) and the flow leaves to the chamber side ([0056], [0059]). The text never names the surface of the ring on which the shoulder bears, and describes no exit from the outer clearance past the interference band and the internal shoulder for the illustrated embodiment. [0105] and claim 31 put a purge gap on the chamber side of the sealing edge along the poppet stem although [0088] has the stem in the ring bore; [0116] has a chamber-ward moving part bearing on the seated chamber-side end. The FIG. 6 instruction calls the interference-fit/purge-gap convention a drafting assumption, not a confirmed mechanism. No drawing exists to resolve it.",
   "least_narrowing_action": "Add disclosure in [0038]/[0052] of the ring surface that receives the axial load and its axial position relative to the sealing edge and the seated end; add in [0056]/[0059] where the purge flow leaves the outer clearance in the embodiment of FIGS. 1 to 4; reconcile [0079], [0105] and [0116]; give the FIG. 3 and FIG. 6B instructions the same contact location and exit. No claim narrowing.",
   "requires_new_disclosure": true,
   "suggested_target": "P4",
   "reviewers": [
    "ip-reviewer-b"
   ],
   "sources": [
    "28"
   ],
   "consensus": false,
   "ruling": "upheld",
   "ruling_reason": "Correct on the text. The poppet opens by moving 'towards the chamber side, lifting the sealing face (42) from the sealing edge (34)' ([0046]), so the sealing face lies on the chamber side of the sealing edge. The purge shoulder is 'on the chamber side of the sealing face' ([0038], [0052], [0112], claim 3), so it moves away from the seat ring in the opening direction. [0079] seats the ring at the end opposite the sealing edge, and [0116] calls the end remote from the sealing edge the 'chamber-side end', which would put the sealing edge on the supply side, the opposite of [0046]. No paragraph names the ring surface that the shoulder bears on. For the purge exit, [0036]/[0053] place the interference band at the internal shoulder, while [0056]/[0059] send the purge flow 'to the chamber side of the seat ring' by no stated route past that band. registry.md flag 3 records the FIG. 6 convention as 'a drafting assumption ... not a confirmed mechanism'. [0105]/claim 31 (a gap between the inner surface and the poppet 'on the chamber side of the sealing edge') cannot be placed either. Severity stays high for the claim set. Claims 3-4 may be unworkable as literally drafted ('chamber side of the sealing face'), so the inventor's layout must be checked against the claim 3 wording in the same fix. This ruling covers F-28-5, F-29-1 and F-29-2, dismissed as its duplicates."
  },
  {
   "id": "F-30-6",
   "source_prompt": "30",
   "category": "enablement",
   "severity": "high",
   "title": "Preferred embodiment: outward deflection is said to open a gap at the outer surface",
   "claim_refs": [
    "1",
    "29",
    "30",
    "72",
    "9"
   ],
   "spec_refs": [
    "[0020]",
    "[0040]",
    "[0053]",
    "[0093]",
    "[0103]",
    "[0159]",
    "[0162]",
    "[0169]",
    "Fig. 1",
    "Fig. 3",
    "Fig. 6",
    "Fig. 10",
    "[0036]",
    "Fig. 6B",
    "Fig. 10B"
   ],
   "attack": "An outward-moving outer surface reduces its clearance to the core body bore, so the described mechanism of the only built embodiment and of Example 3 is not credible as written. The registry calls the FIG. 6 convention an unconfirmed drafting assumption and draws a clearance at rest, contradicting a closed purge gap. No route for the purge flow past the sealed interference band at the internal shoulder is described. Claim 1 survives on [0054], [0103] and [0106], but the tested embodiment, claim 30, and claims 29 and 30 together face insufficiency and Art. 84 attack.",
   "least_narrowing_action": "Obtain the actual P-1 to P-3 mechanism (moving surface, sense, gap location, bypass of the retention band) and rewrite [0040], [0053], [0093] and the FIG. 3, 6 and 10 instructions to match, amending 'outward' in the illustrated embodiment if the movement is inward or ovalising. A description correction; claim 1 is not narrowed.",
   "requires_new_disclosure": true,
   "suggested_target": "P4",
   "reviewers": [
    "ip-reviewer"
   ],
   "sources": [
    "30",
    "36"
   ],
   "consensus": false,
   "ruling": "upheld",
   "ruling_reason": "Best defence: [0053] says the gap opens when deflection 'moves a surface of the seat ring away from the surface against which it bounds the purge gap', and [0054]/[0103] disclose inward and ovalising deflection. That saves claim 1, but not the illustrated embodiment. [0020] says 'In the illustrated embodiment the radial deflection is outward', and [0040]/[0053] place the gap 'between the outer surface of the seat ring (30) and the core body bore (22)'. An outer surface moving outward approaches the bore, so it cannot open that gap. [0103] itself says a gap at the outer surface opens by 'an inward movement of the bounding portion'. The same contradiction appears for the wiper ring in [0093] and [0162] ('deflect the wiper ring radially outward, opening the purge gap between the outer surface of the wiper ring and the core body bore') and in the FIG. 3 and FIG. 10 instructions. [0036]/[0053] confine the interference fit to a band at the internal shoulder (24), but no text explains how purge flow from the supply side ([0056], [0059]) passes that full-circumference band to reach the chamber side; the flutes and ports of [0109]-[0110] are alternatives, not the illustrated embodiment. Claims 29 and 30 read together (outward deflection, outer-surface gap) and claim 72 recite the contradicted combination. High is right: the only built embodiment is described with a mechanism that cannot work as written. The fix needs the actual P-1 to P-3 mechanism from the inventor."
  },
  {
   "id": "F-32-1",
   "source_prompt": "32",
   "category": "novelty",
   "severity": "high",
   "title": "Claim 67 (seat ring): a known wave ring plus routine dimensions",
   "claim_refs": [
    "67",
    "68",
    "69",
    "70",
    "71",
    "72",
    "76",
    "77",
    "78"
   ],
   "spec_refs": [
    "[0088]",
    "[0089]",
    "[0141]"
   ],
   "attack": "Claim 67 recites no poppet, over-travel, gap or material; for a valve core limits only to suitability. Index #1 is summarised as a NiTi wave-section ring giving radial displacement. The remaining dimensions are, by the description's own admission in [0088], routine consequences of the parameter relationships.",
   "least_narrowing_action": "Narrowing required: add superelastic alloy with Af below 5 C and a continuous sealing edge (gives up polymer and resilient-metal rings as components), or recast as the matched kit of [0141] (gives up the bare-ring claim); check #1's full text first.",
   "requires_new_disclosure": false,
   "suggested_target": "P5",
   "reviewers": [
    "ip-reviewer",
    "ip-reviewer-b"
   ],
   "sources": [
    "32"
   ],
   "consensus": true,
   "ruling": "upheld",
   "ruling_reason": "Upheld as an inventive-step objection, not novelty. On the saved text, US 9,982,818 B2 does not anticipate. Its claim 1 recites an SMA ring whose wave-like body runs between planar inner and outer sealing portions, used as a static seal between two members. Its recovery is thermal: claim 10 deforms the ring 'below the martensitic phase transformation temperature' and heats it 'above the austenitic phase transformation temperature'. It shows no sealing edge at an axial end for a poppet, no recovery on removal of an axial load, and no dimensions in mm. Obviousness is credible all the same. Claim 67 recites no poppet, over-travel, gap or material. Its distinguishing features are two dimensional ranges suited to a Presta bore, and 'for a valve core'/'for seating' suitability wording. [0088] presents those dimensions as consequences of stated relationships, and no stated effect attaches to them. Wave-section ring (#1) plus superelastic NiTi seal (#5, US 6,393,765 B1) plus dimensioning for the bore is a credible combination. High is right; narrowing (material and Af, or the matched kit of [0141]) is needed."
  },
  {
   "id": "F-32-2",
   "source_prompt": "32",
   "category": "novelty",
   "severity": "high",
   "title": "Claim 90 (manufacture): standard NiTi processing applied to a known ring form",
   "claim_refs": [
    "90",
    "92",
    "94",
    "95",
    "96",
    "97",
    "98"
   ],
   "spec_refs": [
    "[0147]",
    "[0148]",
    "[0149]",
    "[0150]"
   ],
   "attack": "Laser cutting NiTi tube on a mandrel, shape-setting in a fixture around 500 C, quenching and electropolishing is common general knowledge for NiTi components; claim 90 departs only in the product, which F-32-4 shows is weak; no process effect is asserted.",
   "least_narrowing_action": "Narrowing required: tie the method to the product features that survive F-32-4, or to making the valve core of claim 1 (combining claims 90 and 100 with claim 1), giving up seat-ring manufacture outside such a core.",
   "requires_new_disclosure": false,
   "suggested_target": "P5",
   "reviewers": [
    "ip-reviewer"
   ],
   "sources": [
    "32"
   ],
   "consensus": false,
   "ruling": "upheld",
   "ruling_reason": "Claim 90's steps (tube stock, laser cutting, fixture shape-setting, heating, water quench) carry no process feature beyond what is needed to make the product. The sealing edge and convoluted wall are product features, and [0147]-[0150] assert no process effect. Claim 90 therefore stands or falls with the ring, which F-32-1 shows is exposed. Caveat for counsel: no saved reference documents this NiTi tube-processing route; that it is standard is a general technical point an examiner would readily support with documents from the tube-component field. High stands. Lead finding; F-32-3 is a duplicate."
  },
  {
   "id": "F-32-20",
   "source_prompt": "32",
   "category": "enablement",
   "severity": "high",
   "title": "The axial load path of the purge shoulder is not described and reads against the opening direction",
   "claim_refs": [
    "3",
    "4",
    "22"
   ],
   "spec_refs": [
    "[0038]",
    "[0046]",
    "[0116]"
   ],
   "attack": "The poppet opens chamber-wards, so a shoulder on the chamber side of the sealing face moves away from the sealing edge and can meet only an undescribed supply-facing ring surface further chamber-wards; the axial order of shoulder 24, edge 34, convolutions and shoulder 44 is never stated, and the retainer of [0116] appears reversed.",
   "least_narrowing_action": "Add a paragraph stating the axial order and the face contacted, taken from the prototype and the inventor sketches, and correct [0116] if it is reversed.",
   "requires_new_disclosure": true,
   "suggested_target": "P4",
   "reviewers": [
    "ip-reviewer"
   ],
   "sources": [
    "32"
   ],
   "consensus": false,
   "ruling": "upheld",
   "ruling_reason": "Upheld. Severity is raised because the text, as written, puts the core mechanism of claims 3, 4 and 22 into an arrangement that cannot work. [0046]: on opening, 'the poppet (40) moves ... towards the chamber side, lifting the sealing face (42) from the sealing edge (34)'. So the sealing edge lies on the supply side of the sealing face. [0038], [0052] and claim 3 place the purge shoulder 'on the chamber side of the sealing face'. A shoulder there moves away from the seat ring as the poppet opens, and could bear on it only through a supply-facing ring surface lying further chamber-wards. No paragraph or figure description discloses such a surface. [0116] puts the retainer contact at 'the chamber-side end of the seat ring ... remote from the sealing edge', which places the sealing edge at the supply-side end, and that is hard to reconcile with [0046]. The axial order of internal shoulder (24), sealing edge (34), convolutions (32a, 32b) and purge shoulder (44) is never stated. As drafted, claim 3 faces a credible support and enablement objection, and the ordering must come from the inventor's sketches or prototype before filing, because it cannot be added afterwards.",
   "severity_original": "medium"
  },
  {
   "id": "F-32-4",
   "source_prompt": "32",
   "category": "design-around",
   "severity": "high",
   "title": "Every independent claim ties the purge to over-travel of the poppet caused by the pressure differential",
   "claim_refs": [
    "1",
    "46",
    "57",
    "58",
    "79"
   ],
   "spec_refs": [
    "[0066]",
    "[0112]",
    "[0123]",
    "[0137]"
   ],
   "attack": "Depressor or hand over-travel [0066], a separate purge actuator with the poppet on its normal stroke only [0123], and Schrader cores opened by the head pin [0137] all fall outside claims 1, 58 and 79; claim 57 describes a combination a competitor would not build; if F-32-2 shows depression, the tested embodiment is outside the claims too.",
   "least_narrowing_action": "Define the purge state by the poppet or a deflecting formation moving with it being beyond the normal stroke, with the pressure-differential trigger and mechanical depression as sibling dependent claims; or add an independent claim with a deflecting formation driven by the poppet or a pressure-responsive purge actuator.",
   "requires_new_disclosure": false,
   "suggested_target": "P5",
   "reviewers": [
    "ip-reviewer"
   ],
   "sources": [
    "32"
   ],
   "consensus": false,
   "ruling": "upheld",
   "ruling_reason": "Claims 1 and 58 define the purge state as occurring 'at a pressure differential exceeding the over-travel threshold, in which the poppet is in over-travel', and claim 79 requires 'raising the pressure differential above an over-travel threshold, whereby the poppet moves into over-travel'. The description discloses three routes outside that wording: over-travel by a depressor or by hand 'whatever the pressure differential', with the second spring stage omitted ([0066]); a separate purge actuator carrying the deflecting formation 'the poppet (40) performing only its normal stroke' ([0123]); and Schrader poppets depressed by the pump head ([0137]). A competitor with a single-rate spring and pin-driven over-travel, or with an actuator, escapes claims 1, 58 and 79. In the US, disclosed but unclaimed subject matter risks dedication to the public. Claim 46 adds depression only as an extra to the pressure-driven device, and claim 57 keeps the pressure trigger. High is right. The proposed remedy keeps the normal-stroke/over-travel structure. The purge-actuator limb of F-32-6 is carried here."
  },
  {
   "id": "F-33-2",
   "source_prompt": "33",
   "category": "design-around",
   "severity": "high",
   "title": "Normal-open state requires the ring 'in its at-rest form': escaped by light contact or by a ring-stiffness threshold",
   "claim_refs": [
    "1",
    "58",
    "79",
    "40"
   ],
   "spec_refs": [
    "[0010]",
    "[0050]",
    "[0102]",
    "[0118]",
    "[0122]"
   ],
   "attack": "A deflecting formation that touches and slightly loads the ring during the normal stroke, without opening the purge gap, removes the 'at-rest form' of the normal-open state, so claims 1, 58 and 79 are not met. The ring-stiffness threshold of [0122] (initial elastic rise before the plateau), and [0050], describe exactly this, making claim 40 arguably fall outside claim 1. [0118] ('not touched') supports the narrow construction. Proof needs micro-CT or sectioning under pressure.",
   "least_narrowing_action": "Delete 'the deflectable ring element is in its at-rest form and' from the normal-open state of claims 1, 58 and 79, keeping 'the purge gap is closed' ([0102]). Add a sentence to [0118] and [0122] that the formation may contact and elastically load the ring below the threshold without opening the purge gap, and amend 'is not touched' to 'is not deflected so as to open the purge gap'. Broadening only.",
   "requires_new_disclosure": true,
   "suggested_target": "P3",
   "reviewers": [
    "ip-reviewer"
   ],
   "sources": [
    "33"
   ],
   "consensus": false,
   "ruling": "upheld",
   "ruling_reason": "The normal-open state of claims 1, 58 and 79 requires 'the deflectable ring element is in its at-rest form'. [0010] ('at rest when it is not deflected by the purge shoulder'), [0047] ('not loaded ... retains its at-rest form') and [0118] ('the deflectable ring element is not touched') support a narrow reading, which a light-contact formation escapes. The finding also exposes an internal conflict. Under claim 40 and [0122], with a single-rate spring and the threshold set by ring stiffness, the formation must load the ring through its 'initial elastic rise' while the pressure differential is still below the threshold, that is, in the normal-open state. Claim 40 therefore sits uneasily with claim 1. Deleting 'the deflectable ring element is in its at-rest form and' from the normal-open state is broadening and is supported by [0043] and [0102] ('purge gap ... closed in ... the normal-open state'). Amending [0118] and [0122] needs inventor confirmation that sub-threshold contact is within the conception."
  },
  {
   "id": "F-33-4",
   "source_prompt": "33",
   "category": "design-around",
   "severity": "high",
   "title": "Purge state tied to the pressure differential; depressor-actuated and deflation-only purges escape",
   "claim_refs": [
    "1",
    "58",
    "79",
    "46",
    "88"
   ],
   "spec_refs": [
    "[0066]",
    "[0067]",
    "[0137]",
    "Fig. 7",
    "Fig. 15A"
   ],
   "attack": "Claim 1 places the purge state 'at a pressure differential exceeding the over-travel threshold' and claim 79 requires 'raising the pressure differential above an over-travel threshold'; [0066] discloses over-travel by a pump-head depressor 'whatever the pressure differential' and [0067] a deflation-only purge, so a Schrader-style depressor product or a deflation-purge product infringes no independent claim.",
   "least_narrowing_action": "Reformulate the purge state in an independent claim by poppet position ('when the poppet is displaced beyond the normal stroke into over-travel'), with the pressure threshold, the depressor and the deflation purge as dependent alternatives; supported by [0012], [0066], [0067].",
   "requires_new_disclosure": false,
   "suggested_target": "P5",
   "reviewers": [
    "ip-reviewer-b"
   ],
   "sources": [
    "33"
   ],
   "consensus": false,
   "ruling": "upheld",
   "ruling_reason": "Claim 79 requires 'raising the pressure differential above an over-travel threshold', which a depressor-actuated purge never performs. [0066] discloses over-travel by a depressor 'whatever the pressure differential', [0137] says this is how a Schrader poppet is operated, and [0067] discloses a deflation-only purge. For claims 1 and 58 the drafter's best defence is a capability reading: any sprung poppet has some pressure at which it over-travels. The defendant answers with [0058] (threshold 'within the pressure differential that the intended inflation device produces') and with claim 46's 'additionally', which implies that a pressure-driven purge is required. Both are credible. The disclosed but unclaimed routes also invite a US dedication argument. A position-defined purge state ('poppet displaced beyond the normal stroke into over-travel'), with pressure, depressor and deflation as dependents, is supported by [0012], [0066] and [0067]."
  },
  {
   "id": "F-36-1",
   "source_prompt": "36",
   "category": "enablement",
   "severity": "high",
   "title": "Load path of the purge shoulder and through-route of the purge flow past the retention band not stated for the illustrated embodiment",
   "claim_refs": [
    "1",
    "4",
    "58",
    "79"
   ],
   "spec_refs": [
    "[0034]",
    "[0036]",
    "[0038]",
    "[0053]",
    "[0056]",
    "[0116]",
    "Fig. 3",
    "Fig. 6A"
   ],
   "attack": "The description never states which end of the seat ring carries the sealing edge relative to the internal shoulder, which ring surface the purge shoulder (on the chamber side of the sealing face, moving in the opening direction) bears on, or how gas in the annular outer-surface purge gap passes the interference band that seats the ring against the internal shoulder; the registry's flag 3 concedes the FIG. 6 convention is a drafting assumption, so sufficiency and clarity of claim 1's through-flow for the FIG. 1 embodiment are exposed.",
   "least_narrowing_action": "Add to [0034], [0038] and [0056] a plain statement of the axial arrangement and of the route by which the purge flow enters the annular purge gap at the supply side and leaves at the chamber side (past the free end and the freed region, or via purge ports 262 or flutes 362), taken from the inventor's sketches.",
   "requires_new_disclosure": true,
   "suggested_target": "P4",
   "reviewers": [
    "ip-reviewer-b"
   ],
   "sources": [
    "36"
   ],
   "consensus": false,
   "ruling": "upheld",
   "ruling_reason": "The text does not give the axial arrangement or the purge route for the FIG. 1 embodiment. [0079] puts the sealing edge at the end opposite the internal shoulder. [0116] makes the chamber-side end of the ring 'remote from the sealing edge', so the internal shoulder and the interference band ([0036], [0053]) sit at the chamber-side end, which is the end the purge gas must leave by ([0056], [0059]). No paragraph says how gas in the outer-surface gap passes that band. The mechanism also does not cohere as described: [0040] and [0053] place the gap at the outer surface, closed at rest and opened when the surface 'moves away from' the bore, yet [0020], [0053] and [0093] (and FIG. 3 in the plan) give the illustrated deflection as outward, which moves the outer surface towards the bore. [0103] concedes that this location needs inward movement. The figure plan (FIG. 6) calls the band convention a drawing convention 'adopted to reconcile' the disclosure, not something taken from the inventor. Best defence: claim 1 is generic, and the third arrangement ([0105], inner-surface gap opened by outward deflection) is coherent and supports it. That saves claim 1's scope, but not the enablement of the illustrated embodiment, and claims 4, 30 and 21 read directly on it. Only the inventor's sketches can resolve this, so it needs an answer at the gate, not a drafting assumption."
  },
  {
   "id": "F-36-2",
   "source_prompt": "36",
   "category": "support",
   "severity": "high",
   "title": "No drawings exist: the package holds a figure plan that contains internal working references",
   "claim_refs": [],
   "spec_refs": [
    "[0030]",
    "Fig. 1",
    "Fig. 3",
    "Fig. 6",
    "Fig. 15"
   ],
   "attack": "The description relies on FIGs. 1-15, but the package holds only a figure plan and draftsperson instructions. Filing without drawings risks re-dating (EPC R. 56) or loss of the figure references, and the US requires drawings where necessary (35 USC 113). The plan text contains internal references ('01 Q22', 'DA-7', 'Assumption A2 in Prompt 20') that must not be filed.",
   "least_narrowing_action": "Produce FIGs. 1-15 from registry.md (after F-36-1 for FIGs. 1, 3, 6 and 10), complete the deferred numeral cross-check, add a Brief Description of the Drawings, and exclude all figure-plan working text from the filing.",
   "requires_new_disclosure": true,
   "suggested_target": "P4",
   "reviewers": [
    "ip-reviewer"
   ],
   "sources": [
    "36"
   ],
   "consensus": false,
   "ruling": "upheld",
   "ruling_reason": "The package holds only figures.md, a 'Figure Plan' that expressly says no inventor image has been seen and that FIGs. 2 and 4\u201315 are new. The description relies on drawings throughout ([0030], [0053], [0081], [0093], [0109], [0120], [0137]). The plan text carries internal working references ('01 Q22', 'DA-7, DA-23, DA-24', 'Prompt 16', '14.md'), which must not be filed. Without drawings, US 35 USC 113 is engaged and the EP figure references are exposed. There is also no Brief Description of the Drawings. The FIG. 1, 3 and 6 geometry depends on F-36-1 being resolved first."
  },
  {
   "id": "F-gate14-2",
   "source_prompt": "gate14",
   "category": "enablement",
   "severity": "high",
   "title": "Axial layout of seat ring, sealing edge, internal shoulder and chamber-side purge shoulder cannot be reconstructed from the text",
   "claim_refs": [
    "3",
    "4",
    "8"
   ],
   "spec_refs": [
    "[0038]",
    "[0046]",
    "[0061]",
    "[0088]",
    "[0116]",
    "Fig. 1"
   ],
   "attack": "The poppet opens towards the chamber, so the sealing face lies on the chamber side of the sealing edge; a purge shoulder on the chamber side of the sealing face then moves away from a ring whose 2.3 mm bore admits only the stem, and [0116] puts the sealing edge at the supply-side end. With no drawing sheets, the preferred embodiment of claims 3 and 4 cannot be built from the words (Art. 83/84; 112(a)).",
   "least_narrowing_action": "Add one paragraph, from the inventor's FIG-1 sketch, stating the axial order of the parts, and draw it; if the shoulder is not on the chamber side of the sealing face, conform [0021], [0038], [0112] and claim 3.",
   "requires_new_disclosure": true,
   "suggested_target": "P4",
   "reviewers": [
    "ip-reviewer"
   ],
   "sources": [
    "gate14"
   ],
   "consensus": false,
   "ruling": "upheld",
   "ruling_reason": "Correct on the text. [0046]: to open, the poppet 'moves ... towards the chamber side, lifting the sealing face (42) from the sealing edge (34)', so the sealing face sits on the chamber side of the sealing edge. [0021], [0038] and [0112] then place the purge shoulder 'on the chamber side of the sealing face', so it moves further from the sealing edge as the poppet opens. [0088] makes the ring bore (2.3 mm, [0089]) admit only 'the poppet stem (41)'. [0116] puts the chamber-side end of the seat ring 'remote from the sealing edge', implying the ring extends chamber-ward from the edge. No paragraph explains how a ring whose bore takes only the stem can present a surface on the chamber side of the poppet head for the shoulder to reach in over-travel. [0038] only asserts the result ('contacts the seat ring 30 only during over-travel'). Best defence: claim 1 is functional and [0105], [0113] and [0116] describe other workable arrangements, so claim 1 itself is not left without an enabled form. But claims 3 and 4 and the tested embodiment cannot be rebuilt from the words, and there are no drawings (F-gate14-1). High stands. It is resolved only by the inventor's FIG-1 sketch or an account of the axial order of the parts, which is a disclosure request."
  },
  {
   "id": "F-gate14-4",
   "source_prompt": "gate14",
   "category": "enablement",
   "severity": "high",
   "title": "Illustrated embodiment's outward deflection said to open an outer-surface clearance that the description says needs inward movement",
   "claim_refs": [
    "9",
    "29",
    "30",
    "72"
   ],
   "spec_refs": [
    "[0020]",
    "[0040]",
    "[0053]",
    "[0054]",
    "[0093]",
    "[0103]",
    "Fig. 3",
    "Fig. 6",
    "Fig. 10B"
   ],
   "attack": "Outward movement of the outer surface towards the core body bore narrows the clearance between them and cannot open it; [0103] itself says such a gap opens by inward movement. The only built embodiment and FIG. 3/10B as instructed therefore depict a mechanism the specification rules out. The FIG. 1 instructions draw a clearance at rest, contradicting 'purge gap closed'. This draws Art. 84/112 objections against claims 29 and 30 and undermines the evidential weight of Example 1.",
   "least_narrowing_action": "Get the inventor to confirm the prototype's actual kinematics, then conform [0020], [0040], [0053], [0054], [0093] and the FIG. 1/3/6/10B instructions (using the wording of [0103] if the gap opens by inward movement). No claim narrowing.",
   "requires_new_disclosure": true,
   "suggested_target": "P4",
   "reviewers": [
    "ip-reviewer"
   ],
   "sources": [
    "gate14"
   ],
   "consensus": false,
   "ruling": "upheld",
   "ruling_reason": "Correct on the text. [0040] and [0053] place the purge gap of the illustrated embodiment between 'the outer surface of the seat ring (30) and the core body bore (22)'. [0020] and [0054] say the illustrated deflection 'is outward', and [0093] does the same for the wiper ring ('deflects the wiper ring (132) radially outward, opening the purge gap ... between the outer surface of the wiper ring (132) and the core body bore (22)'). But [0103] says such a gap 'opens where the bounding portion of the outer surface ... moves away from the core body bore (22). That movement may be an inward movement', which is the only kinematics consistent with the geometry: outward movement closes that clearance. Separately, [0036], [0053] and [0103] say the non-interference remainder of the outer surface is 'free of the core body bore', which reads as a clearance at rest, against [0040] 'In the closed state the purge gap 60 is closed'. Best defence: claim 29 (outward) is supported by the third arrangement [0105], and claim 30 by the inward movement of [0103], so each claim alone has a coherent basis. But the only built embodiment, Example 1 ([0155]-[0159]) and the FIG. 3/10B instructions describe a mechanism the specification itself rules out, which undermines the example's evidential weight and invites Art. 83/84 and 112(a)/(b) objections. High stands. The prototype's actual kinematics are an inventor fact, so this goes out as a disclosure request."
  },
  {
   "id": "F-gate14-5",
   "source_prompt": "gate14",
   "category": "design-around",
   "severity": "high",
   "title": "Wipe-only embodiment disclosed but outside every independent claim",
   "claim_refs": [
    "1",
    "58",
    "67",
    "79"
   ],
   "spec_refs": [
    "[0061]",
    "[0065]",
    "[0124]",
    "[0165]",
    "[0167]"
   ],
   "attack": "A competitor seals the ring periphery so that no purge flow path exists and keeps the over-travel deflection and recovery wipe of the sealing face. [0167] shows the clean surfaces are the wiped ones. This escapes claims 1, 58 and 79 (all require the purge gap and purge flow path), and escapes claim 67 outside the dimensional window.",
   "least_narrowing_action": "Add an independent valve-core claim, supported by [0065], [0124] and [0061], reciting over-travel radial deflection of the ring and recovery movement across a poppet surface, without the purge gap; claim 1 is kept.",
   "requires_new_disclosure": false,
   "suggested_target": "P5",
   "reviewers": [
    "ip-reviewer"
   ],
   "sources": [
    "gate14"
   ],
   "consensus": false,
   "ruling": "upheld",
   "ruling_reason": "Correct. [0065] expressly discloses an embodiment in which the cleaning action is 'provided by the snap-back wipe alone, the deflectable ring element being sealed at its periphery so that no inflation gas flows past it'. [0167] records that the clean surfaces after testing were the wiped ones (sealing edge and sealing face). Claims 1, 58 and 79 each require the purge gap to open and a purge flow path 'from the supply side through the purge gap', so a peripherally sealed wipe-only core escapes all three. Claim 67 is bounded by an inner diameter of 2.0-2.6 mm and a wall of 0.15-0.30 mm, so a seat ring outside that window escapes it too. In the US, subject matter disclosed but not claimed is at risk of being dedicated to the public. Support for the proposed independent claim is in [0061], [0065] and [0124]. On the saved art, no reference discloses recovery of the seat itself wiping the poppet (INDEX coverage statement; #3, #7 and #12 use separate wipers or rotation). High stands. Whether to add the claim, and how it fits unity, is a counsel decision."
  },
  {
   "id": "F-30-7",
   "source_prompt": "30",
   "category": "formal",
   "severity": "high",
   "title": "Rule 43(2) and unity: claims 67 and 90 do not share the purge-gap feature with claim 1",
   "claim_refs": [
    "1",
    "58",
    "67",
    "79",
    "90"
   ],
   "spec_refs": [],
   "attack": "Three independent product claims plus two methods; claims 67-78 and 90-102 recite no purge gap, over-travel or threshold, so a posteriori they share no special technical feature with claim 1 once a convoluted thin-walled ring or the standard laser-cut/shape-set route is found.",
   "least_narrowing_action": "Narrowing is the only in-application route: add the superelastic alloy and a link to the sealing-and-purging function to claim 67 and make claim 90 recite that ring, or divide claims 67-78 and 90-102 out; scope given up is the polymer seat ring per se and the generic route.",
   "requires_new_disclosure": false,
   "suggested_target": "P5",
   "reviewers": [
    "ip-reviewer-b"
   ],
   "sources": [
    "30",
    "32"
   ],
   "consensus": false,
   "ruling": "upheld",
   "ruling_reason": "Claim 67 recites a seat ring with a sealing edge, a convoluted wall, shape recovery and two dimensions, but no poppet, over-travel, threshold or purge gap. Claim 90 recites a manufacturing route for such a ring. The feature they share with claim 1 is a ring deflecting radially and recovering, which claim 1 does not even limit to a convoluted wall. A posteriori, that shared feature is weak: saved ref US 9,982,818 B2, claim 1, discloses an SMA sealing ring with a 'wave-like shape comprising at least one peak and at least one trough'. Best defence under R. 43(2)(a), interrelated products, fails because claim 67 is not specifically adapted to claim 1's purge-gap/over-travel features ([0141] ties the matched kit to those features, but claim 67 does not recite the kit). Lack of unity plus the R. 43(2) objection to three product independents (1, 58, 67) needs amendment or division in the EPO and GB and will draw a US restriction. Lead finding on unity; F-30-24 is a duplicate."
  },
  {
   "id": "F-gate14-1",
   "source_prompt": "gate14",
   "category": "formal",
   "severity": "high",
   "title": "Abstract, drawing sheets, brief description of drawings and field/background/summary absent; [0160] refers to a missing background",
   "claim_refs": [],
   "spec_refs": [
    "[0001]",
    "[0160]",
    "Figs. 1-15"
   ],
   "attack": "An abstract is required in the US, at the EPO and in the UK; a brief description of the drawings is required by 37 CFR 1.74 and EPC Rule 42(1)(d). Drawings relied on throughout but not filed trigger EPO Rule 56 and US 35 U.S.C. 113 consequences. [0160]'s cross-reference points to no background section.",
   "least_narrowing_action": "The owning drafter supplies the abstract, the list of figures, the field/background/summary and the drawing sheets (from stripped instructions), and points [0160] at the background or rewords it to 'both failure modes, leak-down and blockage, as defined herein'.",
   "requires_new_disclosure": true,
   "suggested_target": "P4",
   "reviewers": [
    "ip-reviewer"
   ],
   "sources": [
    "gate14"
   ],
   "consensus": false,
   "ruling": "upheld",
   "ruling_reason": "Correct on the package. It contains a description beginning at '#### Definitions and conventions' [0001], the claims, and figures.md, which is a figure plan ('Their content is known only from the README's one-line descriptions'), not drawing sheets. There is no abstract, no brief description of the drawings, and no field, background or summary. [0160] says the conventional cores 'exhibited both of the failure modes described in the background', but no background exists. The description relies on FIGS. 1-15 throughout (e.g. [0030], [0053], [0081], [0113]). Filed without drawings, this triggers Rule 56 EPC (the date moves or the references are deleted) and 35 U.S.C. 113. If the abstract and list of figures are produced at a later step outside this package, that limb closes there; the missing drawings, the missing summary and the [0160] cross-reference remain. High is right: filed as is, the date or the figure-based support is at risk. The drawings need the inventor's sketches (a disclosure request)."
  }
 ]
}
```

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/loop/c1/corrections-desc.json`

```json
[
 {
  "target": "description",
  "location": "[0060]",
  "from_text": "When the inflation device is removed from the supply side, the pressure differential collapses.",
  "to": "When the inflation device is removed from the supply side, the pressure differential falls.",
  "reason": "Only occurrence of the locked avoid-term 'collapse'; 'falls' is used consistently elsewhere for the same event.",
  "source": "38b.envelope"
 },
 {
  "target": "description",
  "location": "[0176]",
  "from_text": "Brass is subject to stress-corrosion cracking in ammoniacal environments as a matter of general materials knowledge, and for that reason a core body (20) of stainless steel 303 is described in Example 4 and in connection with the alternatives above.",
  "to": "Liquid sealants containing ammonia can attack brass over time. A core body (20) of stainless steel 303 is described in Example 4 and in connection with the alternatives above as an option for applications where this is a concern.",
  "reason": "Removes an express admission that the stainless-steel core body is an obvious response to common general knowledge; resolves F-38-2.",
  "source": "38b.envelope"
 },
 {
  "target": "description",
  "location": "[0078]",
  "from_text": "The geometry is loaded mechanically by the purge shoulder (44), at a defined location and at service temperature; no heating or other external actuation is involved in reaching the purge state.",
  "to": "The geometry is loaded mechanically by the purge shoulder (44), at a defined location and at service temperature; for the mechanically actuated embodiments described in this section, no heating or other external actuation is involved in reaching the purge state by this route.",
  "reason": "Avoids apparent contradiction with the thermally actuated purge of [0142]; resolves F-38-4.",
  "source": "38b.envelope"
 },
 {
  "target": "description",
  "location": "[0031]",
  "from_text": "a valve stem 10 having a stem bore 12",
  "to": "a valve stem (10) having a stem bore (12)",
  "reason": "F-40a-3, representative instance.",
  "source": "40a.envelope"
 },
 {
  "target": "description",
  "location": "[0033]",
  "from_text": "The core body 20 is a turned component having an external thread engaged in the stem bore 12, a core body bore 22 that receives the seat ring 30, and an internal shoulder 24",
  "to": "The core body (20) is a turned component having an external thread engaged in the stem bore (12), a core body bore (22) that receives the seat ring (30), and an internal shoulder (24)",
  "reason": "F-40a-3.",
  "source": "40a.envelope"
 },
 {
  "target": "description",
  "location": "before [0001]",
  "from_text": "(no equivalent paragraph present)",
  "to": "A short summary paragraph stating the technical problem and the general solution at a level no narrower than claim 1.",
  "reason": "F-40a-4.",
  "source": "40a.envelope"
 }
]
```

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P5/unsupported.md`

```markdown
# P5 unsupported limitations (Prompt 25 audit against description.md v1)

Each line: source claim | limitation as drafted | what the description says | action taken in the Final Claim Set. Nothing below was left in a claim.

- 22 cl.3, 22 cl.5, 23 cl.47 | "first axial end" / "second axial end" | [0034] "sealing edge 34 at one axial end ... convoluted wall 32 between its ends"; the words "first/second axial end" do not appear | re-worded to "at one axial end of the seat ring" and "between the one axial end and an opposite axial end" (claims 67, 90).
- 22 cl.3 | "on which a sealing face of a poppet is seatable" | [0047] "the seat ring (30) serving only to seat the sealing face (42)"; "seatable" does not appear | re-worded to "for seating a sealing face of a poppet" (claim 67).
- 22 cl.3, 23 cl.8 | "recovers elastically on removal of the axial load" | [0060] "the load applied by the purge shoulder (44) to the seat ring (30) is removed, and the seat ring (30) undergoes shape recovery to its at-rest form"; "recovers elastically" is not used of the seat ring as a component | re-worded to "undergoing shape recovery to its at-rest form on removal of the axial load" (claim 67).
- 22 cl.5, 23 cl.73, 23 cl.74, 23 cl.76 | "seat ring blank" / "shape-set seat ring" | [0147]-[0149] use "the seat ring" and "the cut seat ring (30)"; neither term appears | "the seat ring" throughout claims 90-102.
- 22 cl.5 | "then quenching" (genus) | [0148] "and then water-quenched"; no other quench medium is disclosed | narrowed to "water quenching" (claim 90); disclosure request raised so that the genus can be restored at the fix pass.
- 23 cl.15 | "such that shape recovery of the deflectable ring element moves the deflectable ring element relative to the poppet" | [0061] "the wall of the seat ring (30) returns radially across the surface of the poppet (40) as the poppet (40) passes it"; [0020], [0052] "elastic deformation ... while it remains retained" | split: retention and elastic deformation while retained in claim 18; the movement across the poppet in claim 25 in the [0060] words.
- 23 cl.49 | "A wheel comprising a tubeless tyre defining an inflatable chamber and an inflation valve ... mounted to the wheel in communication with the inflatable chamber" | [0139] "a wheel and a bicycle incorporating such an inflatable chamber and inflation valve"; no mounting or communication statement | re-worded to "A wheel or a bicycle incorporating an inflatable chamber according to claim 64 or claim 65" (claim 66).
- 23 cl.65 | the locked CO2 inflator species term "supplying carbon dioxide as inflation gas" | [0023] "a compressed-gas inflation device, such as a CO2 inflation device"; [0058] "gas from a compressed-CO2 inflation device"; the locked CO2 inflator species term of the inflation device row does not appear | re-worded to "a compressed-gas inflation device" (claim 84); disclosure request raised to add the locked term.
- 23 cl.68 | "the purge state occurring in each inflation event" | [0069] an inflation event may be completed in the normal-open state without entering the purge state | qualified to "in each inflation event in which the pressure differential exceeds the over-travel threshold" (claim 87) per [0068], [0179].
- 23 cl.60 | "about 2.3 mm ... about 0.20 mm ... about 3.0 mm ... about 0.12 mm" | [0089], [0156] give the worked-example values without "about"; [0007] defines "about" but the claim value is a reported value, not an approximation | exact values claimed (claim 78).
- 23 cl.11, 23 cl.52 (context) and 24 Formulation 1 | "a purge gap (60) between an outer surface of the seat ring and the core body bore" as an independent-claim element | supported at [0040], [0053] but carried only as a species (claim 30); Formulation 1 not carried as a second apparatus independent claim (Rule 43(2) EPC) | claim 30.
- 22 cl.1 / 22 cl.2 | "the deflecting formation being spaced from the deflectable ring element throughout the normal stroke" as an independent-claim element | supported at [0038], [0047]; moved out of the independent claims because it accidentally excludes a formation that touches without deflecting, which the "at-rest form" wording of [0013], [0047] covers | claim 2.
- 24 Formulation 2/3 | "below the over-travel threshold" for the normal-open state together with "above the over-travel threshold" for the purge state | [0013] "does not exceed the over-travel threshold" / "exceeds the over-travel threshold"; the 24 wording left a pressure differential equal to the threshold in no state | [0013] wording used in claims 1, 58.
- 23 cl.33 | "the over-travel comprises an over-travel distance of" | [0012], [0090] "the axial distance the poppet moves beyond the end of the normal stroke" | re-worded (claim 43).
- 23 cl.45, 23 cl.69, 23 cl.77 | cross-category references ("valve core according to any one of claims ...") | not a support issue; kept EPO-style in claims 61, 89, 99 | counsel rewrites for the US filing.
```

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P4/enablement-gaps.md`

```markdown
# Enablement gaps — Prompt 17 (valve-oc-20260930, r1)

One line per gap. `id | severity | paragraphs | disclosure needed | who supplies`. "Drafter" gaps are cured in the fix pass from confirmed material with no new matter; "Inventor" gaps need a Gate answer and until then the fix pass can only hedge. Prepared by AI as a drafting aid; qualified patent counsel signs off.

- EN-1 | critical | [0036], [0040], [0053], [0056], [0059] | Complete purge flow path of the illustrated embodiment from the supply side past the interference fit and internal shoulder (24) into the inflatable chamber; which surfaces bound the purge gap (60); which axial band carries the interference fit. Fix pass: state the route past the ring retention as species (clearance beyond the band; flutes (362); purge ports (262)) and assert no complete route for the prototype. | Inventor (01 Q1, Q2); Drafter hedge
- EN-2 | critical | [0020], [0040], [0053], [0093], [0113], [0162] | Remove or qualify every pairing of outward radial deflection with a purge gap between the outer surface of the deflectable ring element and the core body bore (22); [0103] gives the reconciling species; [0113] to cite the inner-surface ([0105]) or through-wall ([0106]) species. | Drafter; Inventor for the prototype's sense
- EN-21 | high | [0018], [0036], [0037], [0040] | State what closes the purge flow path (62) at rest (contact of the deflectable ring element with the surface bounding the purge gap, or the ring retention), as species, and that the pressure-retaining seal is at the sealing edge (34). | Drafter (15 FM-22); Inventor (01 Q31)
- EN-7 | high | [0014], [0065], [0167] | Reconcile the definition "so as to open a purge flow path" with the sealed-periphery wipe-only embodiment; add "not tested" to the wipe-only and purge-only embodiments. | Drafter; Inventor (03 Q1)
- EN-3 | medium | [0038] | State that the axial clearance between the purge shoulder (44) and the seat ring (30) at rest equals the normal stroke ([0046]); 0.6 mm in the prototype. Where the purge shoulder bears and its diameter remain open. | Drafter; Inventor (01 Q8)
- EN-4 | medium | [0039], [0048], [0119] | Add the general design relation: force on the poppet (40) = pressure differential × effective area at the sealing edge (34); first spring stage (52) preload sets the crack pressure; second spring stage (54) engagement and rate set the over-travel threshold; both verified on the assembled valve core. No numbers. | Drafter; Inventor (01 Q7, Q9) for values
- EN-5 | medium | [0049], [0174] | Keep the over-travel limit as three unnamed species; keep [0174] as "in some embodiments". What limits over-travel in the prototype. | Inventor (01 Q36)
- EN-6 | medium | [0051] | Add "not tested" to the embodiment in which the purge state is reached on every opening with a single-rate return spring (50). | Drafter; Inventor (03 Q3)
- EN-8 | medium | [0062] | Soften to "the sealing face (42) or an adjacent surface of the poppet (40)", matching [0060] and §2; the FIG. 4 instruction must not fix a geometry the inventor has not given. | Drafter; Inventor (01 Q10)
- EN-9 | medium | [0091], [0146] | State that no range is given for a resilient polymer, a resilient metal or a wiper ring (132) and that the relationships of [0088] govern; basis of each §4 endpoint and self-consistency of endpoint combinations remain open. | Drafter; Inventor (01 Q15)
- EN-10 | medium | [0026], [0073], [0171] | Add the definitional convention that the austenite finish temperature is determined by differential scanning calorimetry or an equivalent standard method. Achieved value, method and martensite start temperature remain open. | Drafter; Inventor (01 Q13, Q28)
- EN-12 | medium | [0147], [0155]–[0156] | State in Example 1 that the number of convolutions of the prototype seat rings is not recorded; do not imply that laser cutting alone imparts the radial excursion. | Drafter; Inventor (01 Q11)
- EN-14 | medium | [0161] | State that no dimensions are given for the PEEK seat ring (30) and that [0088] governs; whether PEEK was dimensioned remains open. | Drafter; Inventor (01 Q20)
- EN-16 | medium | [0093], [0162] | Fix the outward-plus-outer-surface pairing (EN-2); wiper ring (132) form, thickness, ring retention and whether it wipes remain open. | Drafter; Inventor (01 Q20; 03 Q7)
- EN-18 | medium | [0066], [0067] | Add "not tested" to mechanical and hand over-travel and to purge during deflation; hedge "carrying sealant film out of the valve core" to "may". Whether within the conception remains open. | Drafter; Inventor (12 E1.4, E1.5)
- EN-22 | medium | [0033], [0089] | Core body bore (22) diameter at the seat ring (30), actual seat ring outer diameter, at-rest clearance in the purge gap region. No drafting cure. | Inventor (01 Q16)
- EN-23 | medium | [0142] | Keep or drop the thermally actuated purge; if kept, the two-way shape-memory treatment and how the warmed ring opens the purge gap (60). No drafting cure. | Inventor (03 Q12)
- EN-17 | low | [0120]–[0123] | Add that in every threshold-setting arrangement species the over-travel threshold is verified on the assembled valve core by measuring the pressure differential at which the deflecting formation contacts the deflectable ring element (same sentence as EN-4). | Drafter
- EN-11 | low | [0148], [0149], [0175] | Shape-setting window and electropolishing depth. No drafting cure. | Inventor (01 Q32)
- EN-13 | low | [0081]–[0084] | No change; do not claim numeric ranges for the frustoconical, slotted, cellular or disc geometries. | Drafter (claims note)
- EN-15 | low | [0074], [0075] | No change; hedged. | none
- EN-19 | low | [0136]–[0138] | No change; [0091] scaling statement suffices. | Inventor conception (01 Q26)
- EN-20 | low | [0096], [0117], [0131] | No change; no dependent claim with structure to these. | Drafter (claims note)
- EN-24 | low | [0157]–[0159] | Liquid sealant product and ammonia content, floor pump, deflation method, any direct measurement of over-travel or purge gap opening. No drafting cure. | Inventor (01 Q23)
- EN-25 | low | [0011], [0179] | No change; basis for "every floor pump" remains open. | Inventor (01 Q5)
- EN-26 | low | [0099], [0126], [0127] | No change; hedged. | none
- EN-27 | low | [0135], [0172] | Working range of the interference fit. No drafting cure. | Inventor (01 Q17)
```

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/debate/d1-attack.md`

```markdown
---
matter: valve-oc-20260930
run: r1
step: D1a
agent: Litigator
target: runs/r1/P2/09.md (Differentiation Matrix)
date: 2026-09-30
---

# Debate 1 — Litigator's attack on the differentiation matrix

This is an adversarial reading prepared by AI as a drafting and analysis aid. It is not a legal opinion, does not say the invention is or is not patentable, and qualified patent counsel signs off before anything is filed. Every attack below is anchored to a saved reference in `prior-art/refs/` or to the intake files as quoted in `09`; nothing is cited from memory. There is no defence round: the drafters and the pre-drafting report answer these in the text.

## Attack strength scale

- **Kills**: the distinction as written is disclosed, or falls to an obvious combination of two saved references that an examiner would make without hindsight.
- **Strong**: a credible §102/§103 (Art. 54/56) rejection that needs an amendment or added disclosure to survive.
- **Moderate**: the distinction survives the saved references but the gap is narrower than `09` states, or its support is the real weakness.
- **Survives**: searched, nothing found; the searches are listed.

## What I searched (generic vocabulary only)

Web search, 2026-09-30, five queries: (i) poppet valves with a resilient seat deflected by further poppet travel to open a secondary passage; (ii) tubeless bicycle valve cores, sealant clogging, self-cleaning, class B60C 29; (iii) superelastic NiTi valve seats in poppet valves; (iv) the Schwalbe Clik Valve publication number; (v) two-stage check valves where a second seat opens above a higher pressure differential. Two references were fetched, read in full and saved: **US 8,043,186 B2** (Schaeffler, two-stage check valve) and **US 12,215,796 B2** (Santa Cruz Bicycles, inflation valve for tubeless tyres). Both are appended to `prior-art/INDEX.md` as rows 16 and 17. The Clik Valve search returned product pages only and no publication number; it is not indexed. US 8,397,748 B2 (Ausco, check valve having two seats) was read and not saved: its second seat is a back-flow seal in the open position, not a second flow path.

---

## Row 1 — Two sequential poppet ranges on one poppet (normal stroke, then over-travel above a higher threshold)

### Attack 1.1 — Two pressure thresholds opening two flow paths in one valve assembly is known. **Strong (§103 / Art. 56)**

**Reference:** US 8,043,186 B2, saved as `refs/US8043186B2.md`.

**Passages:**
- Abstract: "a first member that opens in response to a first pressure and a second member which opens in response to a second pressure where the second pressure is higher than the first pressure."
- Description, "The Invention": "The first pressure is set such that it starts the flow of oil, while the second pressure is selected to lessen the restricted flow and allow for proper operation."
- Detailed Description, FIGS. 1a–1b: "When the system pressure reaches a determined value, the first pressure, ball 3 is axially displaced from valve seat 10 such that an annular orifice is opened … When the pressure of the flow path increases to a certain level, second pressure, the tubular poppet 2 is axially displaced from valve seat 11 such that an annular orifice opens … The opening of the second orifice allows for greater oil flow rate through the check valve."
- Claim 7: "a first valve means for opening in response to a first pressure … a second valve means for opening in response to a second pressure, said second valve means housing said first valve means … wherein said first pressure is less than said second pressure."

**The attack as an examiner would put it.** `09` row 1 rests on "three states: closed state, normal-open state, purge state", the third reached "only when the pressure differential exceeds a higher over-travel threshold". US 8,043,186 discloses exactly a closed state, a first-open state at a first spring-set pressure, and a second-open state at a higher spring-set pressure that opens an additional annular orifice, all in one cartridge, each threshold set by its own compression spring. Combine with EP 1137892 A1 (a tyre valve core with a calibrated spring and bleed apertures exposed above a set pressure; claim 1(e)) or with US 4,408,632 A (poppet with primary and secondary seats and a resilient seal ring) and the "two thresholds, two paths" architecture is in the tyre-valve art. The remaining difference is that in the reference the second path is opened by a second *member* rather than by over-travel of the *same* poppet deflecting a *seat*. That difference is real but it is a narrower one than `09` claims, and `09`'s possible claim language ("the poppet being movable through a normal stroke … and into over-travel beyond the normal stroke when the pressure differential exceeds an over-travel threshold higher than the crack pressure") is met in substance by the outer poppet of US 8,043,186 travelling further, at a higher pressure, than the inner ball. The "one poppet" reading has to be carried by explicit claim language, not by the phrase "over-travel".

**What answers it.** The distinction that survives is not "two thresholds" but "the same poppet, whose first range opens the main passage without touching the deflectable ring element, and whose second range deflects that element". The claim must say both: the purge shoulder is spaced from the deflectable ring element throughout the normal stroke, and the same poppet bears on it in over-travel. The Description must explain why one poppet with two ranges is different in kind from two nested members (single moving part, no second seat to clog, the ring is a seat not a valve member). Add to the pre-drafting report that US 8,043,186 will be the examiner's secondary reference for the threshold architecture.

### Attack 1.2 — The purge shoulder "spaced from" the ring during the normal stroke is not evidenced as necessary. **Moderate (support / enablement, not art)**

**Anchor:** `09` row 1 design-around (a) and Q2 concede that "contact on every opening" is unanswered (03 Q3). The bench data reports "an audible snap on every prototype inflation", which is consistent with every inflation reaching the threshold and says nothing about a normal-open state that stops short of it.

**The attack.** If every floor-pump inflation reaches 3.5 bar differential, the normal-open state without purge is never observed and the three-state table is a construct rather than a disclosed mode of operation. An opponent will argue that the "threshold" is a description of the prototype's spring curve, not a technical feature that distinguishes it from ref-02 claim 4 ("lip seal deflectable by the poppet during opening"). If the ring were contacted on every opening the device would read on ref-02 claim 4 as `09` itself admits.

**What answers it.** Disclose at least one inflation event where the differential stays below the threshold (a low-pressure hand pump, a CO2 cartridge tail, a top-up) and the purge state is not entered, with the reason it matters (fatigue life of the ring; sealing edge preserved when purge is not needed). If no such data exists, say so and rest the independent claim on the same-poppet two-range structure rather than on the threshold as a functional result.

### Attack 1.3 — US 4,462,449 A already has a needle that travels freely, then deforms a resilient member on further travel. **Moderate**

**Passage:** claim 1: "a needle … extending toward said elastomeric member but not contacting said elastomeric member unless moved toward said elastomeric member to penetrate and move through said elastomeric member against the normally collapsed state thereof".

**The attack.** `09` disposes of this because "no flow reaches the chamber until that member is penetrated". Correct on the facts, but the examiner's use of it is different: it shows a tyre valve core in which the moving member has a first range of travel out of contact with a resilient member and a second range in which it deforms it. Combined with US 8,043,186 (second range entered only above a higher pressure) the sequence is assembled from two references. The distinction that survives is that in the invention the main passage is already open in the first range. That must be in the claim.

---

## Row 2 — A purge gap separate from the main passage, closed in the closed and normal-open states, opened by radial deflection of the ring

### Attack 2.1 — EP 1137892 A1 claim 8 is closer than `09` allows. **Moderate**

**Passages:** claim 1(e): "one or more bleed apertures that allow air to exit said stem valve housing through the inflation-side end when air pressure inside the tire exceeds a desired value"; claim 7–8: "the moveable disk comprises an O-ring … the aperture comprises a gap between the O-ring and the second solid support"; claim 67 (numbered "3." in the fetched text): "an O-ring … forming an air-tight seal with the inner wall of the valve stem when seated against the shoulder … the O-ring moves along the longitudinal axis toward the inflation-side end of the valve stem when the internal pressure of the tire exceeds a desired value creating an aperture through which excess air escapes."

**The attack.** A gap between a resilient ring and a solid support, closed below a pressure threshold and opened above it, in a tyre valve core, is disclosed. `09` distinguishes on direction (outward discharge, chamber-side pressure). Those are correct, but the direction of flow is a matter of which side the pressure is on, and an examiner will say that reversing the sense of a threshold-opened gap is an obvious rearrangement. The structural distinction that holds is that in EP 1137892 the ring *moves bodily* and the gap opens *between the ring and its seat*; in the invention the ring is *held* and the gap opens by *radial deflection of the ring's wall*. The `09` claim language ("opened by radial deflection of the deflectable ring element") captures this, but only if "deflectable" is construed as elastic deformation of a fixed part, not as movement. The Description must define it that way.

### Attack 2.2 — The purge gap is not enabled on the package's own account. **Strong (support / enablement; this is the row's real weakness)**

**Anchor:** `09` row 2 says: "The location of the purge gap is stated two ways (§2 'stem bore' against §3(6) 'core body bore'), and its opening is hard to reconcile with the 0.03 mm interference fit (§7)"; `09` Q1.

**The attack as an opponent would put it.** A ring pressed into a bore with 0.03 mm radial interference is, by definition, in contact with the bore around its full circumference. For a gap to open between that ring and the bore, the ring's outer surface must move away from the bore: a wall deflecting *inward* under an axial load on a convoluted section. But row 5 says the convoluted wall converts axial load into "radial expansion" (§3(3), inventor's words). Radial expansion of a ring already in interference with its bore closes nothing and opens nothing; it increases contact pressure. Either the gap opens between the ring and the poppet (in which case it is not "separate from the main passage" in any useful sense, because the poppet's sealing face is already off the sealing edge in the normal-open state), or it opens through a feature of the ring or bore not yet described (a relieved region, a slot, a scalloped shoulder). As written, the two rows contradict each other and the "purge gap" is result-only language. Under EPO practice the drafters will not be able to add a mechanism after filing.

**What answers it.** This needs new disclosure from the inventor, not drafting: which two surfaces bound the purge gap in the closed state, which of them moves, in which direction, by how much (the 0.10–0.25 mm figure is quoted but its two bounding surfaces are not named), and how the interference fit at the shoulder is preserved while the gap opens elsewhere on the ring. Without that, row 2 must not carry the independent claim.

### Attack 2.3 — The purge effect is not separated from the wipe effect. **Moderate**

**Anchor:** `09` row 3: "The wipe's share of the effect is not isolated from the air purge (01 Q24)"; row 4: "Not isolated experimentally (08 Q6)".

**The attack.** The 40-cycle result is one experiment on a device that has both mechanisms. An examiner assessing inventive step of row 2 alone will ask what the purge contributes; the package cannot say. The EPO problem-solution approach will take the closest art (US 11,904,644 B2 or ref-02), formulate the problem as "reduce sealant blockage", and ask whether opening a second air path across the seat is obvious. US 4,462,449 A ("swept through" on inflation, INDEX row 6) and CN 215861914 U (air flow cleans a filter) are the answer the examiner will give. A comparison run with the purge gap blocked, or with the wipe disabled (a ring with the same convolution but a stiff material, which the PEEK data partly gives), would break this.

---

## Row 3 — Snap-back wipe driven by shape recovery of a ring held in the core body

### Attack 3.1 — Wiping by a resiliently loaded element on the closing stroke is in the saved art; "recovery-driven" is a difference in what moves, not in what happens. **Moderate**

**Passages:**
- US 4,719,938 A, abstract: "a wiper ring cleans debris from the inner surface of the valve cylinder … The wiper ring is expansible in order to provide a wiping action along the entire taper"; claim 5: "a spring ring pressing outward against the wiper ring".
- US 6,006,954 A, claim 1: "the wiper means scrapes the inner surface to thereby remove solid matter deposited thereon"; claim 6: "at least the perimeter of the wiper means is flexible and is deformed against the inner surface".

**The attack.** Both references have a resiliently loaded, deformable wiper whose own elastic force provides the wiping contact while the valve member moves. `09` says the invention differs because "the relative movement comes from the ring's recovery, not from the stroke of the valve member". But the poppet *is* moving during the return (the differential falls, the return spring closes the valve), and the ring recovers at the same time. Relative movement between poppet and ring occurs in both references and in the invention; who "drives" it is not observable from the product and will be construed as a functional result. The kinematic distinction is real only if it can be claimed structurally: the ring is fixed in the core body, the poppet passes it, and the ring's wall returns radially across the poppet face. Even then, US 4,719,938 has a fixed cylinder wall being wiped by a moving ring; reversing which part carries the wiper is the kind of rearrangement (MPEP 2144.04, T-decisions on reversal of parts as CGK) that an examiner will call obvious unless the reversal produces a stated, evidenced effect.

**What answers it.** The effect must be pinned to the reversal: the wipe acts on the poppet *sealing face*, which is the surface that seals and the surface where film matters, and the wiping element is the seat itself so there is no separate wiper to clog. The 40-cycle data ("sealing edge and poppet face were clean") supports that. Say it in the Description, with the observation of which surface was clean.

### Attack 3.2 — The wipe surfaces and direction are undefined, so the distinction is unclaimable in the form `09` proposes. **Moderate (support)**

**Anchor:** `09` Q3 and row 3 design-around (c): "Which ring surface wipes which poppet surface is unknown (01 Q10)".

**The attack.** "Moving across the poppet so as to wipe it" is a result. Without the surfaces, an opponent will argue the claim covers any ring that touches any poppet on closing, which reads on ref-02 claim 4 and [0020] (a resilient seat that recovers when the pump is removed). New disclosure is required.

### Attack 3.3 — "Snap" is an acoustic observation, not a disclosed mechanism. **Low, but it will be asked**

**Anchor:** bench data "audible snap on removal of the pump head"; `09` row 1 "(indirect evidence only; 01 A9)".

**The attack.** The snap is consistent with the poppet reseating under the return spring, which every valve core does. Nothing in the package ties the sound to ring recovery rather than poppet closure. Do not rely on it as evidence of the wipe.

---

## Row 4 — Superelastic alloy seat ring, austenite finish below 5 °C

### Attack 4.1 — Superelastic NiTi as a repeatedly deformed, self-recovering seal element is disclosed; putting it in a valve is a change of application. **Strong for an independent claim, as `09` already concedes; moderate as a dependent**

**Passages:**
- US 6,393,765 B1, claim 1: "said sheet metal element being a shape memory metal selected for endowment thereof with superelastic properties to establish improved sealage conditions by said deformation, without external control"; Summary: "seal elements to be deformed by engagement in response to closure displacement".
- US 9,982,818 B2, Background: "when above the transformation temperature, the SMA may exhibit pseudoelastic behaviour. This advantageously allows the SMA to absorb high strains whilst maintaining a certain stress or sealing force, which gives such sealing members a high fatigue resistance"; claim 9/11: "the SMA comprises an NiTi alloy".

**The attack.** The material and its reason for use (large recoverable strain, fatigue resistance, sealing force without external control) are stated in the saved art. The Af-below-5 °C limitation is the ordinary way of specifying that an NiTi part is superelastic at ambient temperature; an examiner will treat it as inherent in choosing a superelastic grade for a room-temperature application. `09` already rates this a fallback; I agree and add that the CO2-cold-shock margin (§9 item 2, unknown) is a point an opponent will use to say the claimed temperature is arbitrary.

**What answers it.** Keep it dependent. In the Description, tie the material to the *function that the elastomer cannot do*: the ring must deflect 0.10–0.25 mm radially under the poppet load and return within one closing stroke with enough force to shear a partially cured film, and the PEEK comparison (§6) is the evidence. State the strain at the convolution (the amplitude and wall figures in §4 allow it to be computed) so the choice of superelastic alloy is shown to be required by the strain, not merely preferred.

### Attack 4.2 — Cold-cycling of the ring material. **Survives on the saved art**

Nothing saved discusses NiTi fatigue or low-temperature behaviour in a repeatedly loaded valve seat. Searched (iii) above; the results were elastic metal seat rings in industrial valves without NiTi. The point remains an enablement question for the human (§9 item 2), not an art attack.

---

## Row 5 — Convoluted wall converting axial load into radial deflection

### Attack 5.1 — A wave-section NiTi ring whose peaks and troughs move its inner and outer portions radially is disclosed. **Moderate**

**Passages:** US 9,982,818 B2 claim 1: "a wave-like shape comprising at least one peak and at least one trough"; claim 5: "heating the ring above the transformation temperature of the SMA causes the radially inner sealing portion to move radially inwardly and the radially outer sealing portion to move radially outwardly".

**The attack.** The geometry is the same: a thin NiTi ring with a wave profile whose deformation produces radial displacement of its sealing portions. `09` distinguishes on the driver (thermal versus axial mechanical load). An examiner will say that a wave-profile ring is a spring washer, that a spring washer converts axial load into radial displacement as a matter of mechanics, and that using the ring's own superelastic recovery rather than a heating step is the obvious choice for a device that has no heater. The "at service temperature, with no heating" effect is not a distinction; it is the absence of a step.

**What answers it.** The distinction that holds is that the convolution is loaded *by the poppet* at a defined shoulder and the resulting radial deflection *opens a gap that is closed at rest*. That is row 2's mechanism, so row 5 stands or falls with the purge-gap disclosure (Attack 2.2). Keep it dependent and claim the load path (purge shoulder, convolution, radial deflection, gap) as one chain.

### Attack 5.2 — Alternative geometries. **Survives on the saved art; the risk is design-around, not novelty**

Searched (i) and (iii); nothing saved shows another axial-to-radial seat geometry in a valve core. `09` Q5 stands: a straight thin wall with a chamfered shoulder, or a slotted collet, would convert axial load into radial movement and would avoid a "convoluted wall" claim. Whether the inventor has conceived these is a disclosure question.

---

## Row 6 — One seat ring, two jobs (sealing edge plus deflection to open the purge gap)

### Attack 6.1 — A single resilient seat that both seals and deflects under the poppet is ref-02 claim 1 and claim 4, on `09`'s own account. **Strong as an independent feature; `09` concedes this**

**Anchor:** `09` row 6 ("On its own it is known from ref-02 claim 1"); row 1 quotes ref-02 claim 4: "lip seal deflectable by the poppet during opening"; [0020] (recovers when the pump is removed). I have not read the intake file itself and rely on `09`'s quotations; if the quotations are accurate, the "one ring seals and deflects" feature is anticipated and only the *purpose* of the deflection (opening a separate gap rather than enlarging the main passage) distinguishes.

**What answers it.** Row 6 has no independent life. Fold it into row 2 as a dependent claim ("wherein the deflectable ring element is the seat ring carrying the sealing edge") and cover Alternative B by the genus. The Description should state the trade-off in §6 (one more part and more axial length) as the reason the one-ring form is preferred, not as a distinction.

---

## Row 7 — Two spring stages setting two thresholds

### Attack 7.1 — Two springs setting two opening pressures in one check valve is disclosed. **Strong as an independent feature**

**Passages:** US 8,043,186 B2, claim 8: "said first valve means is a ball biased in a closed position by a first spring; and said second valve means is an outer poppet biased in a closed position by a second spring"; claim 7: "said first pressure is less than said second pressure".

**The attack.** Two compression springs, each setting one of two sequential opening pressures, in one valve cartridge. The invention's springs act on one poppet in series (second stage engaged at the end of the normal stroke) rather than on two members. That is a real structural difference, and it is also exactly the difference between a "two-rate spring stack" and two valves, which every spring designer knows: a preloaded secondary spring that is picked up at a set deflection is a standard rising-rate arrangement (I state this as common general knowledge; `08` already rates the row a *strong* increment, which I read as meaning known). US 4,627,461 A claim 3 ("said spring offers a progressively increasing resistance to compression") and US 9,297,373 B2 claim 1 ("progressive springs") corroborate that progressive rates in valve return springs are routine.

**What answers it.** Dependent only, as `09` says. The independent claim should recite the *threshold*, not the spring, and the Description must give at least one threshold-setting structure that is not a second spring stage (a ring whose own stiffness sets the threshold, a stop that limits the normal stroke until a set force is exceeded) so that a functional "threshold-setting arrangement" has more than one supporting structure for §112(f) and for Art. 84 clarity. `09` Q6 stands and is blocking.

---

## Attacks on the "not distinctions" list and on the matrix as a whole

### Attack 8.1 — The matrix's primary reference is wrong for the EPO. **Moderate, affects the risk report**

`09` orders the rows by their answer to `08`, with ref-02 as the foil. For EPO problem-solution the closest prior art is the document in the same field with the most features in common and the same purpose. That is a real document, not a fictional one: US 11,904,644 B2 (tubeless bicycle valve, built because "Presta or Schrader valves … are often clogged by sealant due to their small diameter", with a resilient seating surface unseated by stem travel), or US 4,462,449 A (tyre valve core, resilient member deformed on further travel, "self cleaning"). The pre-drafting report should run the problem-solution analysis from US 11,904,644 B2, then from US 4,462,449 A, and list the distinguishing features over each. Against US 11,904,644 B2 every row survives on the face of the text (that reference has no seat deflection, no second path, no threshold), which is a stronger position than the matrix currently shows because it argues against a fictional document.

### Attack 8.2 — US 12,215,796 B2 read for completeness. **Survives**

The newest saved tubeless-valve document from the same assignee (saved as `refs/US12215796B2.md`) claims anti-rotation features on a through-stem with an external seat. It has no deforming seat, no second flow path, no threshold and no wipe. Its value is as evidence that the art continues to attack clogging by enlarging and externalising the seat, which the drafters should say in the background.

### Attack 8.3 — The Clik Valve. **Not indexed; flag for the professional search**

Search (iv) returned product pages describing a spring-loaded poppet valve with "up to 50% higher airflow for tubeless setups" and no publication number. It is a 2024 product from a major tyre manufacturer with a new core design and it could not be linked to a publication in the time available. The professional search that `09` Q7 calls for should look for it by applicant and CPC (B60C 29/00, F16K 15/20).

---

## Ranked summary for the drafters

| # | Distinction (`09` row) | Strongest attack | Reference and passage | Strength | What answers it |
|---|---|---|---|---|---|
| 1 | Row 2: separate purge gap | Not enabled: interference fit against radial expansion; bounding surfaces unnamed | `09` row 2 support note; §7 versus §3(3) as quoted in `09` | **Strong (support)** | New disclosure from the inventor (Attack 2.2). Until then row 2 cannot carry the independent claim |
| 2 | Row 1: two poppet ranges, two thresholds | Two spring-set thresholds opening two paths in one cartridge, plus EP 1137892 or US 4,408,632 | US 8,043,186 B2 abstract, "The Invention", claims 7–8 | **Strong (§103)** | Claim the *same poppet* with a first range out of contact with the ring and a second range bearing on it; explain in the Description why one poppet differs in kind from nested members |
| 3 | Row 7: two spring stages | Two springs, two pressures, one valve | US 8,043,186 B2 claims 7–8; US 4,627,461 A claim 3; US 9,297,373 B2 claim 1 | **Strong** | Dependent only; give a second threshold-setting structure |
| 4 | Row 6: one ring seals and deflects | Anticipated on `09`'s own quotation of ref-02 claims 1 and 4 | ref-02 as quoted in `09` (intake file not read here) | **Strong** | Fold into row 2 as a dependent |
| 5 | Row 4: superelastic alloy, Af < 5 °C | Material and its reason for use are in the saved art; Af figure inherent | US 6,393,765 B1 claim 1; US 9,982,818 B2 background, claims 9/11 | **Strong as independent; moderate as dependent** | Dependent; tie to the strain the elastomer cannot survive, with the PEEK comparison as evidence |
| 6 | Row 5: convoluted wall | Wave-profile NiTi ring giving radial displacement is disclosed; the driver is the only difference | US 9,982,818 B2 claims 1, 5 | **Moderate** | Claim the load chain from purge shoulder to gap; stands or falls with row 2 |
| 7 | Row 3: recovery-driven wipe | Resiliently loaded deformable wiper on the closing stroke is disclosed; reversal of parts | US 4,719,938 A abstract, claim 5; US 6,006,954 A claims 1, 6 | **Moderate** | Pin the effect to the reversal (the seat wipes the sealing face; no separate wiper); name the surfaces (new disclosure) |
| 8 | Row 2: threshold-opened gap in a tyre core | Reversing the sense of a threshold-opened gap | EP 1137892 A1 claims 1(e), 8, 67 | **Moderate** | Define "deflectable" as elastic deformation of a held part, not bodily movement |
| 9 | Row 1: normal-open state without purge | Never observed; every inflation snaps | bench data as quoted in `09` | **Moderate (support)** | Disclose a sub-threshold inflation event, or rest the claim on structure |
| 10 | Row 2 / row 3: purge versus wipe contribution | Single experiment, two mechanisms | `09` rows 3–4 | **Moderate** | One comparison run, or the PEEK data reframed as the wipe-off control |

## Disclosure the attacks require (for the runner to route)

1. Row 2: the two surfaces bounding the purge gap in the closed state, which moves, in which direction, by how much, and how the interference fit at the shoulder is kept while the gap opens (`09` Q1). Blocking for P3, P4, P5.
2. Row 1: any inflation event that stays below the over-travel threshold and what happens in it (`09` Q2). Blocking for P5.
3. Row 3: which ring surface wipes which poppet surface, direction and distance (`09` Q3). Blocking for P4, P5.
4. Row 7 / row 1: any threshold-setting structure other than the second spring stage (`09` Q6). Blocking for P4, P5.
5. Rows 2–3: whether any run isolates the purge from the wipe (`09` Q4). Not blocking for drafting; blocking for the inventive-step argument in the pre-drafting report.

## Assumptions

A1. ref-01 and ref-02 are quoted here only as `09` quotes them; I did not open the intake files, which are outside the files named for this step. If the quotations are wrong, Attacks 1.3 (in part) and 6.1 change.
A2. That a preloaded secondary spring picked up at a set deflection is a standard rising-rate arrangement is stated as common general knowledge of a mechanical designer, corroborated by US 4,627,461 A claim 3 and US 9,297,373 B2 claim 1 but not proved by them.
A3. That a wave-profile thin ring converts axial load into radial displacement is stated as common general knowledge (spring-washer mechanics), corroborated by US 9,982,818 B2 claim 5 for the thermal case.
A4. US 8,043,186 B2 is hydraulic and in a transmission; I assume an examiner in F16K 15/20 or B60C 29/00 would cite it as a secondary reference for the threshold architecture. That is a judgement, and counsel may weigh it differently for the EPO than for the USPTO.

## Open Questions

Q1. Does the purge gap open between the ring and the bore, between the ring and the poppet, or through a feature of the ring? Nothing in the package as reflected in `09` answers it, and Attack 2.2 turns on it.
Q2. Is there any inflation event in the bench data that did not produce the snap?
Q3. Has the Clik Valve, or any other 2023–2026 tubeless core, a publication that a professional search would surface? Search (iv) found none.
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

## Files you may read (not embedded: open only what you need)

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/debate/d2-attack.md`

## Files to write

Write each of these with your Write tool, at exactly this path, one file per call (the folders exist). Write nothing outside the run folder `{R}`. Do not run the checks yourself: the runner runs them and will tell you if anything fails.

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/loop/c1/x-p4-revise.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/loop/c1/CHANGED-desc.md`

When every file is written, reply with one line per file (path and a few words on what it holds) and anything the runner must route: open questions, disclosure requests, open disagreements, narrowing suggested. Nothing else.
