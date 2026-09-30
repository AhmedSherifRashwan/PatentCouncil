# Patent Council · matter `valve-oc-20260930` · run `r1` · step `PK-gate14` · profile full

You are the **Examiner**. Follow your AGENTS.md. This message is the whole brief: what to do, the prompts to execute, every input (embedded below, so do not re-read those files), and the exact files to write.

## What to do

Run the 14-question filing gate on the review package and the saved prior art. It feeds the grant-likelihood score in the Prosecution Assessment.

**Time budget:** about 9 minutes. The whole matter is planned to finish end to end in two hours. Be complete, but write each deliverable once: no drafts, no repetition, no padding.

## Prompt gate14 — The 14-question filing gate  (kind `review`)

**Write your reply to:** `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/review/r1/gate14.md`

*Answer the playbook's fourteen filing-gate questions against the exact package, as a structured checklist for the human.*

Answer each of the following questions about the finished package with yes, no or unclear, and give the evidence from the package for each answer:

1. Do the independent claims cover the product or architecture that would actually make money?
2. Can a competitor obtain substantially the same technical/commercial result while omitting one claim element?
3. Are the likely design-arounds expressly disclosed as alternatives where genuinely conceived?
4. Does every claim limitation have clear support in the application as filed, including the claimed combination?
5. Are there enough narrower fallback positions to survive the most credible prior art?
6. Does the disclosure enable the intended breadth without undue experimentation?
7. Have quantitative ranges, endpoints, intermediate ranges and representative values been captured where relevant?
8. Are manufacturing, use, system, device, consumable and software/control aspects protected where commercially justified?
9. Will infringement of the key claims be detectable from the competitor's product, documentation or process?
10. Have priority support and potential later-added subject matter been separated?
11. Have potential continuation/divisional themes been disclosed sufficiently in the first filing?
12. Does the Abstract accurately summarise the finalized claims with no new technical matter, legal phrases or "means for" language?
13. Has the formal/mechanical compliance pass (paragraph numbering, claim format, reference signs, drawing rules) been completed for the target jurisdiction(s)?
14. Has qualified patent counsel reviewed jurisdiction-specific legal and formal requirements before filing?

**How to work.** You are reviewing finished text only. You have not been given, and must not ask for, drafting rationale. The package in front of you (description, figures/figure instructions, claims, numeral registry, and the abstract once it exists) is exactly what an examiner, opponent or court would see; judge that text and nothing else. Under `### Fourteen-Question Gate` give a table: q | question (short form) | answer (yes / no / unclear) | evidence (quoted claim language or paragraph/figure citations). The envelope's `gate14[]` must contain exactly fourteen entries with `q` 1 to 14 and the same answers. Questions 1 and 9 depend on commercial facts you do not have: answer from the package text and mark the dependency in the evidence. Question 14 is always `no` unless the package itself records counsel's review; you cannot answer it on counsel's behalf. A `no` on questions 2 to 8 or 12 to 13 should also appear as a finding of the matching category unless one already exists in this review. This gate informs Human Gate 3; it does not replace it. Reply exactly in the review output contract: `## Findings` (opening with the H3 section(s) named above, then the ranked findings), `## Corrections` (may be empty), `## Assumptions`, `## Open Questions`, then one final fenced `json` envelope whose `findings[]` and `corrections[]` mirror the prose. Every finding must quote the claim language or cite the paragraph/figure it attacks. You never edit the specification or claims and you never clear the application for filing.

## Output contract (review)

You are reviewing finished text only. You have not been given, and must not ask for, drafting rationale. You do not edit the specification or the claims, and you do not clear the application for filing.

Your reply MUST be markdown with exactly these H2 headings, in this order, and nothing before the first one:

## Findings

If the task names deliverable sections, they appear here first as H3 headings (for example `### Support Matrix`), in the order named. Then the findings themselves, one H3 per finding or a ranked list, each finding stating its id, severity, category, the claim language it attacks (quoted) or the paragraph/figure it cites, the attack, and the least narrowing corrective action.

## Corrections

Exact, mechanical corrections to the claims or the description (formal and consistency items): one entry per correction with target, location, the exact text to replace and the exact replacement. This section may be empty; say `None.` if so.

## Assumptions

Numbered A1, A2 ...

## Open Questions

Numbered Q1, Q2 ..., for the human or counsel.

Then ONE final fenced ```json block, and nothing after it, with exactly this shape:

```json
{
  "prompt": "<id>",
  "status": "complete|partial",
  "findings": [
    {
      "id": "F-<prompt>-<n>",
      "source_prompt": "<id>",
      "category": "novelty|enablement|design-around|support|formal",
      "severity": "critical|high|medium|low",
      "title": "...",
      "claim_refs": ["1"],
      "spec_refs": ["[0042]", "Fig. 3"],
      "attack": "...",
      "least_narrowing_action": "...",
      "requires_new_disclosure": true,
      "suggested_target": "P3|P4|P5|in-place"
    }
  ],
  "corrections": [
    {"target": "claims|description", "location": "claim 7", "from": "...", "to": "...", "reason": "..."}
  ],
  "gate14": [{"q": 1, "answer": "yes|no|unclear", "evidence": "..."}],
  "assumptions": [],
  "open_questions": []
}
```

Rules:

- `findings[]` must mirror the findings in `## Findings` one for one; `corrections[]` must mirror `## Corrections`. Empty lists are `[]`, never omitted. `gate14[]` is filled only by the fourteen-question gate prompt (exactly fourteen entries, `q` 1 to 14); every other prompt returns `[]`.
- Finding ids are `F-<prompt>-<n>` with `<prompt>` the task id (e.g. `F-32-4`), numbered from 1 within the reply.
- Category guidance: `novelty` = novelty or inventive-step objections (Prompt 32); `enablement` = enablement or written-description gaps (Prompts 17, 32); `design-around` = design-around or detectability weaknesses (Prompts 11, 33, 35); `support` = support-matrix, priority or amendment-basis gaps (Prompts 28, 29, 31); `formal` = formal or consistency items (Prompts 37, 38, 40a). Only critical and high findings are routed back to the drafters; medium and low are reported to the human as residual findings, so set severity by the real consequence, not by how easy the fix is.
- `suggested_target` is where the fix belongs: `P3` for new embodiments or design-around responses, `P4` for added disclosure in the description, `P5` for claim reformulation, `in-place` for a mechanical correction that the owning drafter applies without re-entering a phase. `requires_new_disclosure` is `true` when the fix needs text the package does not yet contain.
- Every finding must quote the claim language or cite the paragraph or figure it attacks; a finding with neither is not accepted.
- Prefer the least narrowing action: added disclosure over claim narrowing, reformulation over deletion. If narrowing is the only credible fix, say so explicitly so the human can decide.
- Do not cite prior-art references from memory; you have been given none. State any common-general-knowledge premise as an assumption.
- British spelling. No preamble, no closing remarks.

## Inputs (embedded)

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/review/r1/package/description.md`

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

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/review/r1/package/claims.md`

```markdown
1. A valve core for an inflation valve, the valve core comprising a core body (20), a poppet (40) guided by the core body, a deflectable ring element (30) carried by the core body, a return spring (50) biasing the poppet towards a closed state of the valve core, and a main passage (64) past a sealing face (42) of the poppet, the main passage being closed by the sealing face in the closed state; the poppet having a supply side and a chamber side and being displaced from the closed state in response to a pressure differential between the supply side and the chamber side; the valve core having: the closed state, at a pressure differential below a crack pressure, in which the main passage is closed, the deflectable ring element is in its at-rest form and a purge gap (60) associated with the deflectable ring element is closed; a normal-open state, at a pressure differential at or above the crack pressure and not exceeding an over-travel threshold higher than the crack pressure, in which the poppet is displaced within a normal stroke, the main passage is open, the deflectable ring element is in its at-rest form and the purge gap is closed; and a purge state, at a pressure differential exceeding the over-travel threshold, in which the poppet is in over-travel beyond the normal stroke and produces a radial deflection of the deflectable ring element, the radial deflection opening the purge gap so that a purge flow path (62), separate from the main passage, extends from the supply side through the purge gap to the chamber side; the deflectable ring element undergoing shape recovery to its at-rest form and closing the purge gap when the pressure differential falls below the over-travel threshold.

2. The valve core of claim 1, wherein the poppet has a deflecting formation (44) which is spaced from the deflectable ring element in the closed state and throughout the normal stroke and which bears on the deflectable ring element in over-travel so as to produce the radial deflection.

3. The valve core of claim 2, wherein the deflecting formation is a purge shoulder (44) of the poppet on the chamber side of the sealing face.

4. The valve core of claim 3, wherein the purge shoulder is an annular shoulder integral with the poppet which bears axially on the deflectable ring element in over-travel.

5. The valve core of claim 2, wherein the deflecting formation is a tapered purge shoulder (244) having a frustoconical flank which enters the deflectable ring element in over-travel and deflects the deflectable ring element radially outward by direct radial contact with an inner surface of the deflectable ring element.

6. The valve core of claim 2, wherein the deflecting formation comprises two or more discrete lugs (344) spaced around a circumference of the poppet, which load the deflectable ring element at discrete points so that the purge gap opens over arcs of a circumference of the deflectable ring element.

7. The valve core of claim 2, wherein the deflecting formation is provided on a separate collar (444) fixed on a poppet stem (41) of the poppet.

8. The valve core of any one of claims 1 to 7, wherein the deflectable ring element is a seat ring (30) having a sealing edge (34) on which the sealing face rests in the closed state.

9. The valve core of any one of claims 1 to 7, further comprising a fixed seat (130) carried by the core body, the fixed seat not deflecting in over-travel and providing a sealing edge on which the sealing face rests in the closed state, wherein the deflectable ring element is a wiper ring (132) separate from the fixed seat and positioned on the chamber side of the fixed seat.

10. The valve core of any one of claims 1 to 9, wherein the deflectable ring element has a wall arranged such that an axial load applied to the deflectable ring element by the poppet in over-travel is converted into the radial deflection.

11. The valve core of claim 10, wherein the wall comprises a convoluted wall (32) having one or more convolutions.

12. The valve core of claim 11, wherein the convoluted wall has one convolution or two convolutions.

13. The valve core of claim 11 or claim 12, wherein the convoluted wall has a convolution amplitude of from 0.08 mm to 0.20 mm.

14. The valve core of any one of claims 11 to 13, wherein a root of each convolution of the convoluted wall is provided with a fillet radius.

15. The valve core of claim 10, wherein the wall is a frustoconical wall (232), a slotted wall (332) or a cellular wall (432).

16. The valve core of claim 8, wherein the seat ring has a seat ring inner diameter of from 2.0 mm to 2.6 mm and a seat ring wall thickness of from 0.15 mm to 0.30 mm.

17. The valve core of claim 16, wherein the seat ring has a seat ring free length of from 2.5 mm to 4.0 mm.

18. The valve core of any one of claims 1 to 17, wherein the core body has an internal shoulder (24) and the deflectable ring element is retained in the core body against the internal shoulder, the radial deflection being an elastic deformation of a wall of the deflectable ring element while the deflectable ring element remains retained in the core body.

19. The valve core of claim 18, wherein the deflectable ring element is retained in a core body bore (22) of the core body by an interference fit.

20. The valve core of claim 19, wherein the interference fit has an interference of approximately 0.03 mm on diameter.

21. The valve core of claim 19 or claim 20, wherein the interference fit is provided over an axial band of the deflectable ring element adjacent the internal shoulder, and a remainder of an outer surface of the deflectable ring element, including a portion of the wall which undergoes the radial deflection, is not in interference with the core body bore.

22. The valve core of any one of claims 18 to 21, wherein the deflectable ring element is retained by a crimped lip (224) formed on the core body over an end of the deflectable ring element remote from the internal shoulder, or by a retaining sleeve (324) pressed or threaded into the core body and clamping the deflectable ring element against the internal shoulder.

23. The valve core of any one of claims 18 to 22, wherein the deflectable ring element is further retained by an adhesive bond, by staking of the core body over the deflectable ring element, by laser welding of the deflectable ring element to the core body, by over-moulding of the core body around the deflectable ring element, or by clamping of the deflectable ring element between two parts of the core body.

24. The valve core of any one of claims 1 to 17, wherein the deflectable ring element is an integral flexure section of the core body formed in one piece with the core body, the core body being formed from a resilient polymer or from stainless steel of spring temper.

25. The valve core of any one of claims 1 to 24, wherein, as the deflectable ring element undergoes shape recovery when the pressure differential falls, the deflectable ring element moves across a surface of the poppet and shears sealant film from that surface.

26. The valve core of claim 25, wherein the surface of the poppet is the sealing face.

27. The valve core of claim 25 or claim 26, wherein the deflectable ring element has a defined wiping edge at an inner surface of the deflectable ring element which is presented to the poppet as the deflectable ring element undergoes shape recovery.

28. The valve core of any one of claims 1 to 27, wherein the poppet has a second formation, on a side of the deflectable ring element opposite to a side on which the poppet bears in over-travel, which meets the deflectable ring element on a return movement of the poppet and drives the deflectable ring element towards its at-rest form.

29. The valve core of any one of claims 1 to 28, wherein the radial deflection is radially outward.

30. The valve core of claim 8, wherein the purge gap is an annular radial clearance between an outer surface of the seat ring and a core body bore (22) of the core body.

31. The valve core of claim 8, wherein the purge gap is bounded by an inner surface of the seat ring and the poppet on the chamber side of the sealing edge, and the purge flow path passes along a poppet stem (41) of the poppet.

32. The valve core of any one of claims 1 to 29, wherein the purge gap is formed by one or more openings through a wall of the deflectable ring element, the openings being closed in the closed state and in the normal-open state and being opened or uncovered by the radial deflection in the purge state.

33. The valve core of any one of claims 1 to 32, wherein the purge flow path includes one or more purge ports (262) formed through a wall of the core body on the chamber side of the purge gap.

34. The valve core of any one of claims 1 to 33, wherein the purge flow path includes one or more flutes (362) formed as axial grooves in a core body bore (22) of the core body at an axial position of the deflectable ring element, an outer surface of the deflectable ring element lying on lands between the flutes and closing the flutes in the closed state and in the normal-open state.

35. The valve core of any one of claims 1 to 34, wherein the purge gap has a purge gap opening of from 0.10 mm to 0.25 mm in the purge state.

36. The valve core of any one of claims 1 to 35, further comprising a threshold-setting arrangement by which a force resisting movement of the poppet rises at an end of the normal stroke, the threshold-setting arrangement setting the over-travel threshold.

37. The valve core of claim 36, wherein the threshold-setting arrangement is a second spring stage (54) of the return spring, the return spring having a first spring stage (52) of lower rate which resists the normal stroke and sets the crack pressure, and the second spring stage having a higher rate than the first spring stage, coming into action when the normal stroke is complete and setting the over-travel threshold.

38. The valve core of claim 36, wherein the threshold-setting arrangement comprises an auxiliary spring (254) which is engaged when a lost-motion clearance between the auxiliary spring and the poppet closes at the end of the normal stroke, after which the auxiliary spring acts in parallel with the return spring.

39. The valve core of claim 36, wherein the threshold-setting arrangement comprises a detent (354) which holds the poppet at the end of the normal stroke until a force on the poppet exceeds a breakaway value.

40. The valve core of any one of claims 1 to 35, wherein the return spring has a single rate and the over-travel threshold is set by a stiffness of the deflectable ring element.

41. The valve core of any one of claims 1 to 40, wherein the over-travel threshold is from 2.5 bar to 5.0 bar.

42. The valve core of any one of claims 1 to 41, wherein the crack pressure is from 0.8 bar to 1.5 bar.

43. The valve core of any one of claims 1 to 42, wherein in over-travel the poppet moves beyond an end of the normal stroke by an over-travel distance of from 0.4 mm to 0.9 mm.

44. The valve core of any one of claims 1 to 40, wherein the crack pressure is about 1.0 bar and the over-travel threshold is about 3.5 bar.

45. The valve core of any one of claims 1 to 44, wherein the core body has an over-travel stop which the poppet meets at an end of over-travel, the over-travel stop limiting an over-travel distance of the poppet.

46. The valve core of any one of claims 1 to 45, wherein the poppet is additionally movable into over-travel by mechanical depression of the poppet by a depressor in a head of an inflation device or in an adaptor fitted between the inflation device and the supply side.

47. The valve core of any one of claims 1 to 46, wherein the deflectable ring element is formed from a superelastic alloy.

48. The valve core of claim 47, wherein the superelastic alloy has an austenite finish temperature below 5 °C.

49. The valve core of claim 47 or claim 48, wherein the superelastic alloy is a nickel-titanium alloy of nominally 55.8 wt% nickel content.

50. The valve core of claim 47 or claim 48, wherein the superelastic alloy is a NiTiCu alloy, a NiTiFe alloy or a NiTiCr alloy.

51. The valve core of any one of claims 1 to 46, wherein the deflectable ring element is formed from a resilient metal which recovers its shape elastically without a phase transformation, the resilient metal being stainless steel of spring temper, cold-worked austenitic stainless steel, precipitation-hardened stainless steel or a beta-titanium alloy.

52. The valve core of any one of claims 1 to 46, wherein the deflectable ring element is formed from a resilient polymer.

53. The valve core of claim 52, wherein the resilient polymer is polyether ether ketone.

54. The valve core of any one of claims 1 to 53, wherein the core body is formed from stainless steel.

55. The valve core of any one of claims 1 to 54, wherein the sealing face is of hard-anodised aluminium or carries a hard low-adhesion coating.

56. The valve core of any one of claims 1 to 55, wherein the core body has an external thread for engagement in a stem bore of a valve stem, the valve core being removable from the valve stem as a unit.

57. The valve core of any one of claims 1 to 56, wherein the core body is a Schrader-pattern core body (620) and the poppet is a Schrader-pattern poppet (630).

58. An inflation valve for an inflatable chamber, the inflation valve comprising a valve stem (10) having a stem bore (12) and, carried by the valve stem, a deflectable ring element (30), a poppet (40) and a return spring (50), the poppet having a sealing face (42), a supply side and a chamber side, a main passage (64) past the sealing face being closed by the sealing face in a closed state of the inflation valve, the return spring biasing the poppet towards the closed state, and the poppet being displaced from the closed state in response to a pressure differential between the supply side and the chamber side; the inflation valve having: the closed state, at a pressure differential below a crack pressure, in which the main passage is closed, the deflectable ring element is in its at-rest form and a purge gap (60) associated with the deflectable ring element is closed; a normal-open state, at a pressure differential at or above the crack pressure and not exceeding an over-travel threshold higher than the crack pressure, in which the poppet is displaced within a normal stroke, the main passage is open, the deflectable ring element is in its at-rest form and the purge gap is closed; and a purge state, at a pressure differential exceeding the over-travel threshold, in which the poppet is in over-travel beyond the normal stroke and produces a radial deflection of the deflectable ring element, the radial deflection opening the purge gap so that a purge flow path (62), separate from the main passage, extends from the supply side through the purge gap to the chamber side; the deflectable ring element undergoing shape recovery to its at-rest form and closing the purge gap when the pressure differential falls below the over-travel threshold.

59. The inflation valve of claim 58, further comprising a core body (20) received in the stem bore, the deflectable ring element, the poppet and the return spring being carried by the valve stem through the core body.

60. The inflation valve of claim 59, wherein the core body is threaded into the stem bore and is removable from the valve stem as a unit with the deflectable ring element, the poppet and the return spring.

61. The inflation valve of claim 59 or claim 60, wherein the core body, the deflectable ring element, the poppet and the return spring form a valve core according to any one of claims 1 to 57.

62. The inflation valve of claim 58, wherein the inflation valve has no separate core body, the valve stem directly carrying the deflectable ring element, which is a seat ring (730), together with the poppet and the return spring, and the valve stem providing a locating formation against which the seat ring is retained and a bore in which the poppet is guided.

63. The inflation valve of claim 62, wherein the seat ring has a sealing edge on which the sealing face rests in the closed state and a convoluted wall which converts an axial load applied to the seat ring by the poppet in over-travel into the radial deflection.

64. An inflatable chamber comprising a bicycle inner tube or a tubeless bicycle tyre set-up fitted with an inflation valve according to any one of claims 58 to 63.

65. The inflatable chamber of claim 64, wherein the inflatable chamber holds liquid sealant.

66. A wheel or a bicycle incorporating an inflatable chamber according to claim 64 or claim 65.

67. A seat ring (30) for a valve core of an inflation valve, the seat ring being an annular element having a sealing edge (34) at one axial end of the seat ring for seating a sealing face of a poppet, and a wall between the one axial end and an opposite axial end of the seat ring, the wall comprising a convoluted wall (32) having one or more convolutions, the convoluted wall converting an axial load applied to the seat ring into a radial deflection of the seat ring, the seat ring undergoing shape recovery to its at-rest form on removal of the axial load, and the seat ring having a seat ring inner diameter of from 2.0 mm to 2.6 mm and a seat ring wall thickness of from 0.15 mm to 0.30 mm.

68. The seat ring of claim 67, wherein the convoluted wall has one convolution or two convolutions.

69. The seat ring of claim 67 or claim 68, wherein the convoluted wall has a convolution amplitude of from 0.08 mm to 0.20 mm.

70. The seat ring of any one of claims 67 to 69, wherein the seat ring has a seat ring free length of from 2.5 mm to 4.0 mm.

71. The seat ring of any one of claims 67 to 70, wherein the seat ring is a continuous ring and the sealing edge is continuous around a circumference of the seat ring.

72. The seat ring of any one of claims 67 to 71, wherein the radial deflection is radially outward.

73. The seat ring of any one of claims 67 to 72, wherein the seat ring is formed from a superelastic alloy.

74. The seat ring of claim 73, wherein the superelastic alloy has an austenite finish temperature below 5 °C.

75. The seat ring of claim 73 or claim 74, wherein the superelastic alloy is a nickel-titanium alloy of nominally 55.8 wt% nickel content.

76. The seat ring of any one of claims 67 to 72, wherein the seat ring is formed from a resilient polymer.

77. The seat ring of claim 76, wherein the resilient polymer is polyether ether ketone.

78. The seat ring of any one of claims 67 to 75, wherein the seat ring inner diameter is 2.3 mm, the seat ring wall thickness is 0.20 mm, the seat ring has a seat ring free length of 3.0 mm, and the convoluted wall has a convolution amplitude of 0.12 mm.

79. A method of operating an inflation valve of an inflatable chamber which holds liquid sealant, the inflation valve comprising a poppet having a supply side, a chamber side and a sealing face, a deflectable ring element, a main passage past the sealing face which is closed by the sealing face in a closed state of the inflation valve, and a return spring biasing the poppet towards the closed state, the method comprising, within one inflation event: coupling an inflation device to the supply side and raising a pressure differential between the supply side and the chamber side to at or above a crack pressure, whereby the poppet moves through a normal stroke into a normal-open state in which inflation gas flows through the main passage into the inflatable chamber while the deflectable ring element remains in its at-rest form and a purge gap associated with the deflectable ring element remains closed; raising the pressure differential above an over-travel threshold higher than the crack pressure, whereby the poppet moves into over-travel beyond the normal stroke and produces a radial deflection of the deflectable ring element, the radial deflection opening the purge gap, and inflation gas flows as an air purge along a purge flow path, separate from the main passage, from the supply side through the purge gap into the inflatable chamber across surfaces on which sealant film accumulates; and removing the inflation device from the supply side, whereby the pressure differential falls and the deflectable ring element undergoes shape recovery to its at-rest form and closes the purge gap.

80. The method of claim 79, wherein, as the deflectable ring element undergoes shape recovery, the deflectable ring element moves across a surface of the poppet and shears sealant film from that surface.

81. The method of claim 79 or claim 80, wherein the air purge carries sealant film from the surfaces on which sealant film accumulates into the inflatable chamber.

82. The method of any one of claims 79 to 81, wherein the crack pressure is from 0.8 bar to 1.5 bar and the over-travel threshold is from 2.5 bar to 5.0 bar.

83. The method of any one of claims 79 to 82, wherein the inflation device is a floor pump and the pressure differential exceeding the over-travel threshold is produced by the floor pump.

84. The method of any one of claims 79 to 82, wherein the inflation device is a compressed-gas inflation device.

85. The method of any one of claims 79 to 84, wherein the inflatable chamber is a bicycle inner tube or a tubeless bicycle tyre set-up.

86. The method of any one of claims 79 to 85, wherein the liquid sealant is an emulsion of latex containing ammonia.

87. The method of any one of claims 79 to 86, further comprising repeating the coupling, the raising and the removing over a plurality of inflation events, the purge gap opening and the air purge occurring in each inflation event in which the pressure differential exceeds the over-travel threshold.

88. The method of any one of claims 79 to 87, further comprising, while the inflatable chamber is pressurised and no inflation device is supplying gas to the supply side, pressing the poppet into over-travel so that the purge gap opens and gas from the inflatable chamber flows through the purge gap from the chamber side to the supply side, carrying sealant film out of the inflation valve.

89. The method of any one of claims 79 to 88, wherein the inflation valve comprises a valve core according to any one of claims 1 to 57 or is an inflation valve according to any one of claims 58 to 63.

90. A method of manufacturing a seat ring (30) for a valve core of an inflation valve, the method comprising: providing tube stock of a superelastic alloy; laser cutting a profile of the seat ring from the tube stock, the seat ring having a sealing edge (34) at one axial end of the seat ring; forming, in a wall of the seat ring, a convoluted wall (32) having one or more convolutions, the convoluted wall being defined by the laser cutting, by forming on a mandrel, by shape-setting, or by a combination thereof; and shape-setting the seat ring by holding the seat ring in a fixture which constrains the convoluted wall to its intended geometry, heating the seat ring in the fixture and then water quenching the seat ring, the shape-setting fixing an at-rest geometry of the seat ring to which the seat ring returns by shape recovery, the convoluted wall converting an axial load applied to the seat ring into a radial deflection of the seat ring.

91. The method of claim 90, wherein the tube stock has an outer diameter of 2.7 mm and a wall of 0.20 mm.

92. The method of claim 90 or claim 91, wherein the tube stock is mounted on a mandrel during the laser cutting.

93. The method of any one of claims 90 to 92, wherein the convoluted wall is formed with one convolution or with two convolutions.

94. The method of any one of claims 90 to 93, wherein the shape-setting comprises heating the seat ring in the fixture at 500 °C for 10 minutes and then water quenching the seat ring.

95. The method of any one of claims 90 to 94, wherein a shape-setting temperature and a shape-setting time are selected so that the seat ring has an austenite finish temperature below 5 °C, and the austenite finish temperature is verified on sampled seat rings after the shape-setting.

96. The method of any one of claims 90 to 95, further comprising, after the shape-setting, electropolishing the seat ring to remove surface oxide and a heat-affected edge left by the laser cutting.

97. The method of claim 96, wherein a depth of the electropolishing is limited at an inner surface of the seat ring so as to preserve a defined wiping edge formed by the laser cutting.

98. The method of any one of claims 90 to 97, wherein the superelastic alloy is a nickel-titanium alloy of nominally 55.8 wt% nickel content.

99. The method of any one of claims 90 to 98, wherein the seat ring is a seat ring according to any one of claims 67 to 78.

100. The method of any one of claims 90 to 99, further comprising pressing the seat ring into a core body bore (22) of a core body (20) of the valve core until the seat ring seats against an internal shoulder (24) of the core body, with an interference fit between the seat ring and the core body bore.

101. The method of claim 100, wherein the interference fit has an interference of approximately 0.03 mm on diameter.

102. The method of claim 100 or claim 101, further comprising checking a press-in force or a press-in travel of the seat ring during the pressing.
```

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/review/r1/package/figures.md`

```markdown
### Figure Plan

**Scope and mapping to the inventor's own sketches.** The intake supplies two inventor sketches by name only (`intake/drawings/README.md`): FIG-1.png (axial section, closed state) and FIG-2.png (axial section, full over-travel, with air-flow arrows). Their content is known only from the README's one-line descriptions (01 Q22); no image has been seen and nothing here describes them beyond what the README states. FIG-1.png becomes planned **FIG. 1** below; FIG-2.png becomes planned **FIG. 3**. No other inventor sketch exists, so FIGs. 2, 4–15 below are new.

**Embodiments drawn.** Three confirmed core embodiments are covered, per the combination matrix (`14.md`): **E-I** (one-piece superelastic NiTi seat ring), **E-II** (one-piece PEEK seat ring, same structure, Alternative A), and **E-III** (fixed seat plus separate wiper ring, Alternative B). Confirmed design-around and equivalent-architecture entries (`11.md`, `12.md`) are drawn where they add real disclosure value and are technically coherent; entries that cannot be closed without new matter (**DA-7, DA-23, DA-24**) are not drawn, because no embodiment exists for them in the confirmed material. The thermally actuated purge variant (F5 / DA-25) is not drawn: the inventor states doubt about pursuing it and no data exists (`§6`; 01 Q21); it is left to Gate 2/inventor confirmation whether a figure should be added later.

**Categories covered**, against the prompt's list: system overview and state sections — FIGs. 1–4; exploded view — FIG. 5; cross-section detail — FIG. 6; use sequence / mechanical control logic (there is no software or electronics; control is entirely mechanical, 01(i)) — FIG. 7; manufacturing sequence — FIG. 8; alternative architectures and combinations — FIGs. 9–15.

**Numbering scheme (detail in Prompt 20a).** Reference numerals 10, 20, 30, 40, 42, 44, 50, 60, 70 are the inventor's own, fixed by `intake/disclosure.md` §3 and `terminology/LOCKED.md`; they are not changed. Numerals in the decades 11–79 extend them by component family for the preferred embodiment (FIG. 1 onward). Numerals in the 100s, 200s, 300s, 400s, 600s and 700s are reserved for alternative-embodiment and alternative-species components, by group, first introduced in FIGs. 8 and 10–15.

**Claim-concept references.** Prompt 16 (blueprint) has not yet run, so no blueprint section ids exist to cite; the entries below cite the nucleus rungs (N0–N7), feature codes (C-codes) and design-around/equivalent-architecture ids (DA-/E-) from `11.md`–`15.md` instead. Blueprint cross-referencing is left to Prompt 16 (see Open Questions).

#### FIG. 1

- **View type.** Axial section through the valve core, on the plane containing the poppet axis.
- **What it shows.** The valve core at rest, in the closed state: crack pressure not reached, purge gap closed. Corresponds to the inventor's FIG-1.png.
- **Confirmed embodiment(s).** E-I (preferred, superelastic NiTi seat ring). Serves as the baseline against which E-II, E-III and the alternative-species figures are read.
- **Components to be numbered.** Valve stem; stem bore; core body; core body bore; internal shoulder; seat ring; convoluted wall; sealing edge; poppet; poppet stem; sealing face; purge shoulder; return spring; first spring stage; second spring stage; purge gap (shown closed); lock nut.
- **Claim concepts/fallbacks supported.** The full nucleus N0(a)–(e) in its rest condition; N1 (snap-back wipe, latent); N2 (seat ring also forms the seat); N3 (convoluted wall); N4 (superelastic alloy, by material of the seat ring — supports CB1); N7 (interference fit, at the internal shoulder). Supports the closed-state limitation common to every independent claim family.

#### FIG. 2

- **View type.** Axial section, same plane as FIG. 1.
- **What it shows.** The valve core in the normal-open state: pressure differential between crack pressure and the over-travel threshold, poppet displaced by the normal stroke against the first spring stage only, purge shoulder not yet in contact with the seat ring, purge gap still closed, air flow arrows through the main passage.
- **Confirmed embodiment(s).** E-I.
- **Components to be numbered.** Poppet (displaced); sealing face (lifted off the sealing edge); first spring stage (compressed); main passage (flow arrows); purge shoulder (shown clear of the seat ring, with a dimension line to the sealing edge).
- **Claim concepts/fallbacks supported.** N0(a) (normal stroke) as distinct from over-travel; the crack-pressure/over-travel-threshold distinction (03 C2, C18) that DA-1 shows is not universally essential — this figure supports the claim family that retains the distinction, with DA-1 as the disclosed fallback narrowing point if the inventor confirms purging on every opening (01 Q1 of `11.md`'s findings).

#### FIG. 3

- **View type.** Axial section, same plane as FIG. 1.
- **What it shows.** The valve core in the purge state: pressure differential above the over-travel threshold, poppet in over-travel against the second spring stage, purge shoulder bearing on the seat ring, seat ring deflected radially outward, purge gap open, air-flow arrows through both the main passage and the purge gap into the inflatable chamber. Corresponds to the inventor's FIG-2.png.
- **Confirmed embodiment(s).** E-I.
- **Components to be numbered.** Purge shoulder (in contact); seat ring (deflected, shown in dashed outline against its at-rest profile from FIG. 1); purge gap (open, with a radial dimension line); purge flow path (flow arrows, distinguished from the main-passage arrows); second spring stage (further compressed).
- **Claim concepts/fallbacks supported.** The core of N0(b)–(e): over-travel, the threshold-setting arrangement engaged, the purge shoulder contacting the deflectable ring element, radial deflection, the purge gap open, the air purge running. This is the single most important figure for claim support of the independent claim(s); it is also the figure a competitor's teardown most directly maps onto DA-2 through DA-6 (`11.md`, "Detectability").

#### FIG. 4

- **View type.** Axial section, same plane as FIG. 1.
- **What it shows.** The valve core immediately after the inflation device is removed: pressure differential collapsing, poppet returning, seat ring in shape recovery, in the course of the snap-back wipe across the poppet's sealing face, purge gap closing.
- **Confirmed embodiment(s).** E-I.
- **Components to be numbered.** Seat ring (shown mid-recovery, with a motion arrow across the sealing face); purge gap (shown narrowing).
- **Claim concepts/fallbacks supported.** N1 (snap-back wipe) as a distinct, drawable step, supporting a method/process claim reciting recovery and wipe as separate from purge-gap closure; also supports DA-10's fallback (wipe-only embodiment, no flow) by showing the wipe as a discrete visual event independent of the flow arrows already retired by this state.

#### FIG. 5

- **View type.** Exploded perspective view.
- **What it shows.** Every part of the valve core assembly separated along the poppet axis, in assembly order.
- **Confirmed embodiment(s).** E-I (baseline parts set); callouts note the alternative parts substituted in E-II and E-III (see FIG. 9, FIG. 10).
- **Components to be numbered.** Valve stem; core body; seat ring; poppet; return spring (as first and second spring stage, if separable parts — otherwise as a single two-rate part); lock nut.
- **Claim concepts/fallbacks supported.** Supports a kit/component claim family (DA-19: seat ring, or seat ring with poppet and return spring, sold separately) and the replacement-core question (01 Q33; CB5 in `14.md`).

#### FIG. 6

- **View type.** Enlarged cross-section detail, two sub-views: **FIG. 6A** (at rest) and **FIG. 6B** (over-travel).
- **What it shows.** The seat ring, internal shoulder, core body bore and purge shoulder region only, enlarged, with the convoluted wall, the sealing edge, the purge gap and its opening dimension called out.
- **Confirmed embodiment(s).** E-I.
- **Components to be numbered.** Internal shoulder; core body bore; seat ring; convoluted wall (with each convolution individually labelled where two are shown); sealing edge; purge shoulder; purge gap (closed in 6A, open with a radial dimension line in 6B).
- **Claim concepts/fallbacks supported.** N3 (convoluted wall; one or two convolutions, N6 range for convolution amplitude); N6 ranges generally (seat ring wall thickness, free length, convolution amplitude, purge gap opening — the Table 1 ranges of `13.md`); N7 (interference fit, shown confined to the internal-shoulder region, leaving the remainder of the seat ring's outer surface free to move — the drawing convention adopted to reconcile §7's interference fit with §2's outward deflection and §3(6)'s gap location, per the Rationale below and 01 Q1/Q2).

#### FIG. 7

- **View type.** State/flow diagram (schematic, not a section).
- **What it shows.** The mechanical control logic of the valve core as a state machine: closed → normal-open → purge → recovery → (optionally) locked, with the governing condition (a range of the pressure differential, or the lock nut) labelled on each transition, matching the operating sequence of `01.md` (d) and (i).
- **Confirmed embodiment(s).** E-I; the same diagram applies to E-II and E-III with a note that the transition conditions may differ in degree (E-II: slower recovery per §6; E-III: recovery and wipe conditional per `14.md` footnotes [a]/[b]).
- **Components to be numbered.** None (schematic; states and transition conditions are labelled by name, not by reference numeral).
- **Claim concepts/fallbacks supported.** Supports a method/process claim reciting the full state sequence, and DA-9's fallback (over-travel produced mechanically or by hand rather than solely by the pressure differential) as an alternative transition condition.

#### FIG. 8

- **View type.** Process-flow diagram (schematic sequence of steps), with two additional sub-views **FIG. 8D** and **FIG. 8E** for retention alternatives.
- **What it shows.** The seat ring manufacturing and assembly sequence: **8A** laser cutting from tube stock; **8B** shape-setting in a fixture; **8C** water quench and electropolishing, then pressing into the core body with an interference fit against the internal shoulder (baseline retention, cross-referenced to FIG. 1); **8D** an alternative retention step, a crimped lip rolled or swaged over the seat ring by the core body; **8E** an alternative retention step, a separate retaining sleeve clamping the seat ring against the internal shoulder.
- **Confirmed embodiment(s).** E-I (process); the retention alternatives 8D/8E apply to E-I, E-II and E-III alike (DA-22; E14.2, E14.3).
- **Components to be numbered.** Seat ring (through each process step); internal shoulder; crimped lip (8D only); retaining sleeve (8E only).
- **Claim concepts/fallbacks supported.** N7 as claimed (interference fit) plus its disclosed fallback genus, ring retention (DA-22; E14.2–E14.4), closing the design-around route of retaining the ring by a method other than interference.

#### FIG. 9

- **View type.** Axial section, same plane and state as FIG. 1 and FIG. 3 (shown as a single figure with a rest/purge-state note, to avoid repeating FIG. 1–4 in full).
- **What it shows.** The seat ring formed from PEEK instead of superelastic NiTi, otherwise structurally identical to FIG. 1/FIG. 3 (same convoluted wall, same numeral for the seat ring). A callout notes the disclosed trade-off: slower recovery and a weaker snap-back wipe (§6), without asserting the wipe is as effective as in E-I (per `14.md` footnote [a]).
- **Confirmed embodiment(s).** E-II (Alternative A).
- **Components to be numbered.** Seat ring (same numeral as FIG. 1, material callout "PEEK" added); all other components as FIG. 1/3, reused.
- **Claim concepts/fallbacks supported.** CB3 (lower-cost line); the N4 fallback ladder (deflectable ring element in polymer, DA-13); supports a claim reciting the deflectable ring element functionally (deflects, opens the purge gap, recovers) rather than by requiring a superelastic alloy.

#### FIG. 10

- **View type.** Axial section, two sub-views: **FIG. 10A** (closed state) and **FIG. 10B** (purge state), same plane as FIG. 1/3.
- **What it shows.** The fixed-seat-and-wiper-ring architecture: a rigid fixed seat performs sealing; a separate wiper ring, on the chamber side, is deflected outward by the purge shoulder during over-travel, opening a purge gap between the wiper ring's outer surface and the core body bore.
- **Confirmed embodiment(s).** E-III (Alternative B).
- **Components to be numbered.** Fixed seat (new component, not present in E-I/E-II); wiper ring (new component); purge shoulder; purge gap (same numeral as FIG. 1, now bounded by the wiper ring); core body bore; core body; poppet; sealing face.
- **Claim concepts/fallbacks supported.** CB4 (design-around-closing split architecture); the N2 fallback (seat ring also forms the seat is not essential — DA-17); closes the competitor route of splitting sealing from purging specifically to avoid a one-piece-ring claim.

#### FIG. 11

- **View type.** Three sub-views, schematic partial sections: **FIG. 11A**, **FIG. 11B**, **FIG. 11C**.
- **What it shows.** Alternative deflecting-formation geometries on the poppet, each shown contacting the seat ring during over-travel in place of the baseline annular purge shoulder of FIG. 1/3: **11A** a tapered (frustoconical) purge shoulder acting by direct radial contact; **11B** discrete radial lugs (two to four) in place of a continuous annular shoulder; **11C** a separate collar fixed onto the poppet stem.
- **Confirmed embodiment(s).** Design-around/equivalent-architecture candidates confirmed at Gate 2: DA-4, E3.2 (11A); E3.3 (11B); E3.4 (11C).
- **Components to be numbered.** Tapered purge shoulder (11A); discrete lugs (11B); separate collar (11C); each shown against the seat ring and core body bore, reusing those numerals.
- **Claim concepts/fallbacks supported.** The purge shoulder/deflecting formation genus (N0(c)), supporting claim language defining the purge shoulder by function (contact with the deflectable ring element during over-travel) rather than by the single disclosed annular-shoulder-on-the-poppet species; closes DA-4.

#### FIG. 12

- **View type.** Three sub-views, schematic partial sections: **FIG. 12A**, **FIG. 12B**, **FIG. 12C**.
- **What it shows.** Alternative axial-to-radial conversion geometries for the deflectable ring element wall, each replacing the convoluted wall of FIG. 1/6: **12A** a frustoconical wall; **12B** a slotted wall with axial slots forming fingers that splay radially; **12C** a cellular (laser-cut lattice) wall.
- **Confirmed embodiment(s).** DA-3, DA-12, DA-18, E4.3, E4.4, E5.3, E5.4.
- **Components to be numbered.** Frustoconical wall (12A); slotted wall, with individual fingers labelled by letter suffix (12B); cellular wall (12C).
- **Claim concepts/fallbacks supported.** N3 as claimed (convoluted wall) plus its genus fallback, axial-to-radial conversion geometry, supporting a claim that does not require a convoluted (wave) profile specifically; closes DA-3/DA-12/DA-18, the cheapest mechanical escapes from N3 identified in `11.md`.

#### FIG. 13

- **View type.** Two sub-views, schematic partial sections: **FIG. 13A**, **FIG. 13B**.
- **What it shows.** Alternative purge-flow-path geometries: **13A** radial purge ports through the wall of the core body, on the chamber side of the purge gap; **13B** axial flutes in the core body bore, behind the seat ring, connecting to the supply side when the seat ring's outer surface moves inward or the ring is one of the FIG. 12 species.
- **Confirmed embodiment(s).** E8.2, E8.3.
- **Components to be numbered.** Purge port (13A); flute (13B); core body bore (reused).
- **Claim concepts/fallbacks supported.** The purge flow path genus (locked term), supporting claim language that does not limit the purge flow path to the single annular-gap species of FIG. 1/3; closes the "purge exits sideways" and "flute-metered flow" design-around routes.

#### FIG. 14

- **View type.** Two sub-views, schematic partial sections: **FIG. 14A**, **FIG. 14B**.
- **What it shows.** Alternative threshold-setting arrangements, each replacing the two-rate return spring of FIG. 1: **14A** an auxiliary compression spring engaged only when a lost-motion clearance closes at the end of the normal stroke; **14B** a detent (spring-loaded ball or magnetic) that releases at a breakaway force.
- **Confirmed embodiment(s).** E2.2, E2.4 (14A, as representative of the lost-motion family); E2.5 (14B).
- **Components to be numbered.** Auxiliary spring (14A); detent (14B).
- **Claim concepts/fallbacks supported.** N5 as claimed (two-stage return spring) plus its genus fallback, threshold-setting arrangement, supporting claim language reciting a threshold-setting arrangement functionally; closes DA-11.

#### FIG. 15

- **View type.** Two sub-views, schematic (not to the Presta-pattern scale of FIG. 1–4): **FIG. 15A**, **FIG. 15B**.
- **What it shows.** Alternative valve architectures carrying the same mechanism: **15A** a Schrader-pattern valve core; **15B** a non-removable inflation valve in which the seat ring, poppet and return spring are carried directly by the valve stem, with no separate core body.
- **Confirmed embodiment(s).** DA-6, E16.2 (15A); E14.6, E16.3 (15B).
- **Components to be numbered.** Schrader-pattern core body and Schrader-pattern poppet (15A, new numerals; the mechanism-carrying parts reuse the seat-ring/spring/purge-gap numerals conceptually but are not drawn to component level here); seat ring carried directly by the valve stem (15B, new numeral).
- **Claim concepts/fallbacks supported.** The valve-mechanism genus (not limited to a removable Presta-pattern core), supporting a claim family at the level of "an inflation valve" rather than "a valve core"; closes DA-6 and the core-level claim escape identified for DA-19/E14.6/E16.3.
```

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/review/r1/package/registry.md`

```markdown
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
```

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
| 16 | US 8,043,186 B2 | Two stage check valve for automatic transmission system | Schaeffler KG | 2007-02-05 | 2011-10-25 (grant); pre-grant publication 2008-08-07 | https://patents.google.com/patent/US8043186B2/en | N3, N4 (in principle) | Added by the Litigator at D1a. One check-valve assembly with two spring-set opening pressures: a first member opens at a first pressure to start flow, a second member opens at a higher second pressure to open a second annular orifice and "lessen the restricted flow". Two thresholds, two flow paths, one assembly, in a hydraulic transmission. Both paths open by movement of separate members, not by deflection of a seat, and the second path is not closed by a resilient element. Combination partner against the normal-stroke/over-travel sequence. Full text saved in `refs/`. | 2 |
| 17 | US 12,215,796 B2 | Inflation valve for tubeless tires | Santa Cruz Bicycles LLC | 2021-08-20 | 2025-02-04 (grant); pre-grant publication 2024-03-28 | https://patents.google.com/patent/US12215796B2/en | N7 | Added by the Litigator at D1a. Same family of thinking as #2: external valve seat, resilient seating surface on a through-stem, anti-rotation features. Read to test whether the newest tubeless-valve art from the leading assignee discloses any deforming seat, over-travel or purge path; it does not. Evidence that the tubeless-valve art continues to solve clogging by enlarging and externalising the seat. Full text saved in `refs/`. | 2 |

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

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/intake/priority`/
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/prior-art/refs`/

## Files to write

Write each of these with your Write tool, at exactly this path, one file per call (the folders exist). Write nothing outside the run folder `{R}`. Do not run the checks yourself: the runner runs them and will tell you if anything fails.

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/review/r1/gate14.md`

When every file is written, reply with one line per file (path and a few words on what it holds) and anything the runner must route: open questions, disclosure requests, open disagreements, narrowing suggested. Nothing else.
