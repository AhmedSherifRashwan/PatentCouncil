# Patent Council · matter `valve-oc-20260930` · run `r1` · step `P4-17` · profile full

You are the **Specification Drafter**. Follow your AGENTS.md. This message is the whole brief: what to do, the prompts to execute, every input (embedded below, so do not re-read those files), and the exact files to write.

## What to do

Run Prompt 17 against the stitched description. Also write every enablement or sufficiency gap to `P4/enablement-gaps.md`, one line each with the paragraph and the disclosure needed: the fix pass answers them.

**Time budget:** about 9 minutes. The whole matter is planned to finish end to end in two hours. Be complete, but write each deliverable once: no drafts, no repetition, no padding.

## Prompt 17 — Enablement/sufficiency audit  (kind `analysis`)

**Write your reply to:** `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P4/17.md`

*Check whether the skilled person can actually practise the scope.*

Audit the disclosure for enablement/sufficiency across the full intended claim breadth. Identify embodiments that would require undue experimentation, missing materials/process conditions, unsupported functional breadth, unpredictable technical areas, absent examples and parameters that need explanation. Recommend additional disclosure or experiments before filing.

**How to work.** Draft only from confirmed embodiments (`CONFIRMED.md`), the Phase 1 outputs and the differentiation matrix; unconfirmed Phase 3 candidates are not in front of you and must not reappear. Use the locked terminology verbatim. Never fabricate experimental data or results. This audit is a gate on your own breadth: scope you cannot enable does not go out described as enabled. In inner-loop round 1 audit the blueprint and the confirmed embodiments; when `description.md` is supplied (round 2 onwards) audit that text instead and cite its paragraph numbers. Under `### Enablement Audit` give a table: id (EN-1 ...) | scope element (locked term) | issue type (undue experimentation / missing conditions / functional breadth / unpredictable art / no example / parameter unexplained) | severity | what would cure it (additional disclosure the inventors can supply, an experiment, or narrowing the described scope). Recommendations that need inventor input go in `open_questions`; those you can cure from confirmed material go in `disclosure_requests` addressed to yourself for the compose or revise step. Reply exactly in the drafting output contract: `## Deliverable` (with the H3 sections named above), `## Rationale`, `## Assumptions`, `## Open Questions`, then one final fenced `json` envelope. No preamble before `## Deliverable`; nothing after the envelope. Reuse locked preferred terms verbatim; declare any other term in `new_terms` with a reason.

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

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P1/01.md`

````markdown
## Deliverable

### Structured Invention Disclosure

This is a drafting and analysis aid prepared by AI. It is not legal advice and makes no statement about patentability; qualified patent counsel signs off before anything is filed.

**Sources.** Every technical fact below is taken from `intake/disclosure.md`, cited as §1–§9 by its section numbers. `intake/data/bench-test.md` (cited as "bench data") and `intake/drawings/README.md` (cited as "drawings README") are used as corroboration only. The two inventor sketches, FIG-1 and FIG-2, are known only from the README's one-line descriptions; the images have not been seen and nothing here describes them beyond what the README says (Q22). Anything inferred rather than read is labelled *inferred* and listed under Assumptions.

**Component names used throughout** are the inventor's own words where they are neutral, with the reference numerals given in §3 (the drawings README confirms the sketches use the same numerals): valve stem (10), core body (20), seat ring (30), poppet (40), sealing face (42), purge shoulder (44), return spring (50), purge gap (60), lock nut (70). Operating terms: *normal stroke*, *over-travel*, *crack pressure*, *over-travel threshold* (the pressure differential at which over-travel begins), *air purge* and *snap-back wipe* (the two cleaning actions), *sealant film*.

#### (a) Problem being solved

1. Riders use liquid sealant (typically a latex emulsion with ammonia and suspended particles) in bicycle inner tubes and tubeless set-ups, and inject it through the valve stem (§1).
2. On each inflation, sealant is drawn into the valve core bore "by the pressure surge and by capillary action along the poppet stem", and the film dries between rides (§1). This causal account is the inventor's own and is not separately evidenced.
3. After 10–20 inflation cycles, cured latex on the core seat causes one of two failures: the valve leaks slowly because the poppet no longer seats, or it blocks because the pump cannot open it (§1). The bench data corroborates both modes: C-1 and C-3 blocked, C-2 leaked.
4. The existing remedy is manual: unscrew the core with a tool, scrape it or replace it, and re-inject sealant. Cores are sold in multipacks for this reason (§1).
5. The inventor names existing attempts (a low-adhesion polymer coating on the poppet, an enlarged bore, a removable insert) and says they only slow build-up and do not remove a film once formed (§1). No specific product, patent or publication is identified (Q35).

#### (b) Core inventive concept

As stated in §2, read without narrowing:

1. The valve core carries a **seat ring (30)** of superelastic NiTi instead of a rigid brass seat or a rubber grommet. Its wall is thin and sinuous (convoluted) (§2, §3(3)).
2. Under normal inflation the poppet (40) lifts off the seat by its normal stroke (§2).
3. When the pump applies a pressure differential above a threshold, the poppet moves beyond its normal stroke. This is **over-travel** (§2).
4. Over-travel drives the **purge shoulder (44)** of the poppet against the seat ring. The ring flexes radially outward and opens an annular **purge gap (60)** (§2, §3(4), §3(6)).
5. Air at pump pressure flows through the purge gap "across the exact surfaces on which sealant accumulates" and blows the sealant film into the tube. This is the **air purge** (§2). The drawings README says FIG-2 shows air flowing both "through the main passage and through the purge gap into the tube".
6. When the pump head is removed, the differential collapses, the poppet returns and the seat ring recovers its shape. Because superelastic recovery is fast and stiff rather than a slow elastomer creep, the recovering ring wipes across the poppet face with a snap and shears off partially cured latex. This is the **snap-back wipe** (§2).
7. The inventor describes this as cleaning "twice per inflation": once by the air purge and once by the snap-back wipe (§2).

Observations for Prompt 03, not conclusions. The inventor's own alternatives (§6) replace NiTi with PEEK (Alternative A) and separate the sealing seat from a stainless spring wiper ring (Alternative B). On the face of the disclosure, then, the inventor conceives the invention more broadly than "a NiTi seat ring". Four elements recur across §2 and §6:
- (i) poppet movement beyond a normal opening stroke at a higher pressure differential;
- (ii) a resiliently deflectable ring element that a shoulder on the poppet contacts during that over-travel;
- (iii) a purge flow path opened by that deflection;
- (iv) recovery of the ring element on release.

Whether each of (i)–(iv) is essential is for the inventor to confirm (Q6, Q12, Q24).

#### (c) Technical effect

1. **Stated effect:** the valve "keeps sealing and keeps opening after far more sealant-loaded inflation cycles than a conventional core, with no tool and no rider action" (§2).
2. **Stated mechanisms:** the air purge removes sealant film through the purge gap, and the snap-back wipe shears off partially cured latex (§2). The inventor contrasts the wipe with a rubber seat, in which latex "would simply embed itself", and attributes the wipe to superelastic recovery being "fast and stiff" (§2).
3. **Evidence of the effect:** all three prototypes completed 40 cycles without failure, while all three conventional cores failed between cycles 12 and 18 (§8). Details are under (l).
4. **Not evidenced:**
   - how much each of the air purge and the snap-back wipe contributes;
   - a direct measurement of over-travel distance or purge-gap opening. Over-travel was inferred from an audible snap (bench data).

   See Q23 and Q24.

#### (d) Essential components/steps

The disclosure does not itself label components essential or optional. The table records what §2 needs for the stated mechanism to work. The "needed" column is *inferred* from §2 and §6 and awaits Prompt 03 and the inventor.

| # | Component (ref) | Function stated in the disclosure | Needed for the §2 mechanism? (*inferred*) | Source |
|---|---|---|---|---|
| D1 | Core body (20) | Threaded to the stem; carries the seat ring; guides the poppet | Yes, as carrier and guide. Material and form are open | §3(2) |
| D2 | Seat ring (30) | Sealing seat (upper edge). Deflects radially outward under over-travel to open the purge gap. Recovers with a snap to wipe the poppet face | Yes. NiTi is preferred; §6 Alternatives A and B show the inventor considers non-NiTi ring elements | §2, §3(3), §6 |
| D3 | Convoluted wall of the seat ring | One or two shallow convolutions, so that axial load on the upper edge becomes radial expansion | Stated as the mechanism of radial expansion. Whether a straight-walled ring could work is not addressed (Q12) | §3(3) |
| D4 | Poppet (40) with sealing face (42) | Moving valve member; its conical sealing face seats on the upper edge of the seat ring | Yes | §3(4) |
| D5 | Purge shoulder (44) | Below the sealing face; contacts the seat ring only during over-travel | Yes | §2, §3(4) |
| D6 | Return spring (50), two-rate | Soft first stage for normal opening; stiffer second stage that the pump differential must overcome to reach over-travel | Some means of setting an over-travel threshold is needed. Whether a two-rate spring is the only means is not addressed (Q6) | §3(5) |
| D7 | Purge gap (60) | Annular clearance, closed at rest, opened by ring expansion; carries the air purge | Yes. **Its location is stated inconsistently** (Q1, Q2) | §2, §3(6) |

Operating sequence, as described in §2 (not presented as a method claim):

| Step | Event | Source |
|---|---|---|
| S1 | The pump head applies pressure. At the crack pressure the poppet lifts off the seat ring by its normal stroke (first spring stage) | §2, §3(5), §4 |
| S2 | The pressure differential exceeds the over-travel threshold. The poppet over-travels against the second spring stage | §2, §3(5), §4 |
| S3 | The purge shoulder bears on the seat ring; the ring flexes radially outward; the purge gap opens | §2, §3(4), §3(6); drawings README (FIG-2) |
| S4 | Air at pump pressure flows through the purge gap across the sealant-bearing surfaces into the tube (air purge). Air also flows through the main passage | §2; drawings README (FIG-2) |
| S5 | The pump head is removed; the differential collapses; the poppet returns; the ring recovers and wipes the poppet face (snap-back wipe); the purge gap closes | §2; bench data (audible snap on pump-head removal) |

#### (e) Optional components

| Component | Status in the disclosure | Source |
|---|---|---|
| Lock nut (70) | Conventional; closes the poppet manually for storage and transport. Not part of the mechanism | §3(7) |
| Valve stem (10) | Conventional Presta-pattern brass stem, 6 mm OD, with a threaded bore. The mechanism is in the core. The disclosure does not say whether the core alone is a product, for example a replacement core for existing stems (Q33) | §3(1) |
| Electropolished ring surface | Manufacturing step that removes oxide and the heat-affected edge. Its functional importance (for example to the wipe or to fatigue life) is not stated | §5, §7 |
| Spring material | "Nothing in the concept depends on the spring material" | §5 |

#### (f) Alternative implementations

All are as stated in the disclosure. None has been built or tested except where the table says so.

| # | Alternative | What changes | Inventor's stated trade-off | Built/tested | Source |
|---|---|---|---|---|---|
| F1 | Stainless 303 core body | Core body material, for corrosion resistance with ammonia-bearing sealant | — | "was also machined". The bench data lists no stainless variant (Q18) | §5 |
| F2 | Hard-anodised aluminium sealing face on the poppet | Material of the poppet and sealing face | "considered" | No; the prototype poppet is brass | §5 |
| F3 | Alternative A: PEEK seat ring with the same convoluted wall | Seat ring material | Cheaper and gives some radial compliance, but recovery is slower and snap-back force lower, so the wipe is weaker. Proposed for a lower-cost line | No | §6 |
| F4 | Alternative B: two-piece seat. A rigid brass seat does the sealing; a separate thin stainless spring wiper ring below it is deflected outward by the purge shoulder | Separates sealing from purge and wipe | Possibly easier to make, at the cost of one more part and more axial length | No | §6 |
| F5 | Thermal variant: a two-way shape-memory NiTi ring (Af about 35–40 °C) that opens the purge gap when warmed by hand, for a manual purge without a pump | Actuation by temperature instead of over-travel | Inventor is "not sure this is worth pursuing"; no data | No | §6 |
| F6 | One or two convolutions in the ring wall | Ring geometry | — | The disclosure does not say which count the prototype used (Q11) | §3(3) |

The disclosure contains no other alternatives. It does not mention other alloys, other ring geometries, other threshold mechanisms, or Schrader and other valve types (Q14, Q26).

#### (g) Inputs/outputs

| Input | Output | Source |
|---|---|---|
| Pump-side pressure below crack pressure | Valve closed. The poppet sealing face rests on the upper edge of the seat ring; the purge gap is closed | §3(4), §3(6); drawings README (FIG-1) |
| Pressure differential at or above crack pressure (prototype 1.0 bar) | Normal stroke (prototype 0.6 mm). Air flows into the tube past the sealing face | §2, §4 |
| Pressure differential at or above the over-travel threshold (prototype 3.5 bar) | Over-travel (prototype 0.5 mm). The ring expands, the purge gap opens (prototype 0.15 mm radial) and the air purge runs | §2, §4; drawings README (FIG-2) |
| Pump head removed | The poppet returns, the ring recovers, the snap-back wipe occurs and the purge gap closes. The bench data reports an audible snap | §2; bench data |
| Lock nut operated by hand | Poppet held closed for storage and transport | §3(7) |
| Deflation "through the valve" (test protocol) | Tube emptied. The mechanism during deflation is not described (Q23) | §8 |

The disclosure does not define "pressure differential". Pump side against tube side is *inferred* (A3, Q4).

#### (h) Materials, dimensions, ranges and operating conditions

The disclosure labels the §4 values "prototype values, with the ranges we believe would work". Only the prototype value was built, and **no range endpoint is evidenced** (Q15).

| Parameter | Prototype value | Range given by inventor | Evidence | Source |
|---|---|---|---|---|
| Seat ring inner diameter | 2.3 mm | 2.0–2.6 mm | Prototype only | §4 |
| Seat ring wall thickness | 0.20 mm | 0.15–0.30 mm | Prototype only | §4, §7 |
| Seat ring outer diameter | 2.7 mm (*inferred* from the tube stock in §7) | Not given | — | §7 (A2) |
| Seat ring free length | 3.0 mm | 2.5–4.0 mm | Prototype only | §4 |
| Convolution amplitude | 0.12 mm | 0.08–0.20 mm | Prototype only | §4 |
| Number of convolutions | "one or two" | — | Prototype count not stated | §3(3) |
| Normal poppet stroke | 0.6 mm | Not given | Prototype only | §4 |
| Over-travel beyond the normal stroke | 0.5 mm | 0.4–0.9 mm | Prototype only; not measured in the test | §4 |
| Purge gap, fully open | 0.15 mm radial | 0.10–0.25 mm | Prototype value; not measured in the test | §4 |
| Crack pressure (first spring stage) | 1.0 bar | 0.8–1.5 bar | Prototype only | §4 |
| Over-travel threshold (second spring stage) | 3.5 bar | 2.5–5.0 bar | Prototype only | §4 |
| NiTi austenite finish temperature Af | "below 5 °C" (specified) | Upper bound only. No lower bound; As, Ms and Mf not given | A specification, not a measured value | §4 |
| NiTi composition | Nominally 55.8 wt% Ni | No tolerance | — | §5 |
| Ring press fit in the core body | Interference of approx. 0.03 mm on diameter | Not given | Prototype | §7 |
| Valve stem outer diameter | 6 mm (Presta-pattern) | — | Conventional | §3(1) |
| Test inflation pressure | 6 bar | — | Test condition | §8 |
| Test hold temperature | 22 °C | — | Test condition | §8 |
| Thermal variant Af | about 35–40 °C | — | No data | §6 |

Materials:

| Part | Prototype | Alternatives disclosed | Source |
|---|---|---|---|
| Seat ring (30) | Superelastic NiTi from drawn tube, shape-set and electropolished | PEEK (F3); stainless spring wiper ring with a brass seat (F4); two-way shape-memory NiTi (F5) | §5, §6 |
| Core body (20) and stem (10) | Free-machining brass CW614N | Stainless 303 (F1) | §5 |
| Poppet (40) | Brass | Hard-anodised aluminium sealing face (F2) | §5 |
| Return spring (50) | Stainless music wire | Material stated to be immaterial | §5 |

Operating conditions:
- **Stated:** "all riding temperatures" (§4; no temperature range given); ammonia-bearing latex sealant (§1, §5); floor-pump inflation (§2, §8).
- **Expressly unknown:** CO2 inflation, ammonia-free sealants and long service (§9). The bench data adds that no fatigue or cold-shock testing was done.

The disclosure does not give:
- the core body bore diameter at the ring;
- the geometry of the purge shoulder;
- the cone angle of the sealing face;
- spring rates, forces, or the stroke at which the second stage engages;
- what limits over-travel (a stop, coil-bind or the ring);
- the axial position of the ring against the internal shoulder.

See Q7, Q8, Q9, Q16 and Q36.

#### (i) Control logic/software

There is no software and no electronics. Control is entirely mechanical and actuated by pressure (§2, §3(5)):

| State | Condition | Poppet | Seat ring | Purge gap |
|---|---|---|---|---|
| Closed | Differential below crack pressure | Seated on the upper edge of the ring | At rest | Closed |
| Normal open | Differential between crack pressure and the over-travel threshold; first spring stage | Normal stroke | Not contacted by the purge shoulder | Closed |
| Purge | Differential above the over-travel threshold; second spring stage overcome | Over-travel | Deflected radially outward by the purge shoulder | Open |
| Recovery | Differential collapses when the pump head is removed | Returns | Superelastic recovery; snap-back wipe | Closes |
| Locked | Lock nut closed | Held closed | — | — |

The two-rate return spring sets the threshold (§3(5)). The disclosure does not say how much the ring's own stiffness contributes to it (Q6, Q7).

#### (j) Manufacturing methods

The prototype process, from §7:

1. Seat ring: laser-cut from NiTi tube (2.7 mm OD, 0.20 mm wall) "to the convoluted profile on a mandrel". It is ambiguous whether the convolution comes from the laser cut, from forming on the mandrel or from the shape-set fixture (Q11).
2. Shape-set at 500 °C for 10 minutes in a fixture that holds the wave geometry, then water-quenched.
3. Electropolished to remove the oxide and the heat-affected edge.
4. Pressed into the core body with an interference of approximately 0.03 mm on diameter and seated against the internal shoulder.
5. Core body and poppet: ordinary turning, with "no other special process".

The disclosure gives no process ranges and no volume-production route. It also names no alternative forming routes (for example stamping, etching or rolling a corrugated tube) and no alternative ways of retaining the ring (adhesive, crimp, snap feature) (Q17, Q32).

#### (k) Use cases

**Stated:**
- bicycle inner tubes with liquid sealant, and tubeless set-ups with sealant (§1);
- floor-pump inflation (§2, §8);
- a lower-cost product line using the PEEK ring (§6);
- manual purging without a pump, in the thermal variant (§6).

The test used 700×28 inner tubes (§8).

**Not stated:**
- testing in a tubeless set-up (only inner tubes were tested);
- Schrader valves or other vehicle tyres;
- other valves that carry sealant or are prone to fouling;
- sale of the core alone as a retrofit.

See Q25, Q26 and Q33.

#### (l) Experimental evidence

The bench test ran from 2026-08-12 to 2026-08-20 (§8, corroborated by the bench data):

| Item | Detail | Source |
|---|---|---|
| Samples | 3 prototype cores (P-1 to P-3). 3 conventional cores (C-1 to C-3), all the same manufacturer's standard Presta core; the manufacturer is not named | §8; bench data |
| Set-up | Identical 700×28 tubes, each charged with 60 ml of latex sealant. The sealant product and ammonia content are not stated | §8 |
| Cycle | Inflate to 6 bar with a floor pump; hold 24 h at 22 °C; deflate fully through the valve; repeat | §8 |
| Failure criterion | Leak-down > 0.5 bar in 24 h, or the pump fails to open the valve within 5 s of engagement | §8 |
| Inflation-time measure | From pump-head engagement to 6 bar, with the same pump and the same operator throughout | bench data |
| Conventional results | C-1: blocked at cycle 14 (inflation time 41 s at cycle 1, 68 s at cycle 13). C-2: leak-down of 0.7 bar at cycle 12 (40 s, then 44 s at cycle 11). C-3: blocked at cycle 18 (42 s, then 75 s at cycle 17) | §8; bench data |
| Prototype results | No failure in 40 cycles. Inflation time, cycle 1 → cycle 40: P-1 43 → 47 s; P-2 41 → 46 s; P-3 44 → 50 s. Leak-down at cycle 40: 0.1, 0.1 and 0.2 bar/24 h. The disclosure states that mean inflation time at cycle 40 was within 15 % of cycle 1 | §8; bench data |
| Over-travel indicator | "Over-travel was confirmed on every prototype inflation by an audible snap on pump-head removal." This is indirect: it indicates a recovery event, not a measured over-travel distance or purge-gap opening | bench data |
| Post-test inspection | Under a stereo microscope at cycle 40: cured film on the outer surface of the ring in the purge-gap region; sealing edge and poppet face clean | §8; bench data |
| Not tested | Fatigue and cold shock | §9; bench data |

The limits of the evidence, stated without judging it:
- the sample is small (n = 3 of each);
- the test used one sealant, one temperature, one inflation pressure, one floor pump, one operator, and inner tubes only;
- the test stopped at 40 cycles rather than running the prototypes to failure;
- over-travel and purge-gap opening were not measured directly;
- no test isolated the air purge from the snap-back wipe;
- Alternatives A, B, F1, F2 and F5 were not tested.

The rising inflation times of the conventional cores before failure, including the leaking core C-2, are recorded in the bench data but not discussed in the disclosure. Against a commercial target of "several thousand" cycles, §9 records 40 over-travel cycles per ring (Q23, Q24, Q27).

#### (m) Unresolved technical questions

The inventor's own known unknowns (§9):
- the fatigue life of the seat ring, and whether the purge gap stays closed after long service (Q27);
- whether chilling from a CO2 inflator takes the ring below its martensite start temperature, and whether Af below 5 °C is enough margin (Q28);
- whether the effect holds with ammonia-free sealants (Q29).

Gaps and inconsistencies found during extraction (each is a numbered open question below):

- **The purge gap's location is stated two ways:** "between the ring and the stem bore" (§2) and "between the seat ring outer surface and the core body bore" (§3(6)). The bench data (film on the ring's outer surface in the purge-gap region) is consistent with the §3(6) reading (Q1).
- **The gap-opening mechanism is not self-evidently consistent.** The ring is pressed into the core body with an interference fit (§7) and "flexes radially outward" (§2). Yet a gap is said to open between its outer surface and the core body bore (§3(6)), whereas outward expansion would ordinarily close a gap at the outer surface, not open it. The complete air path from the pump side, through the purge gap, to the tube is not described in words. FIG-2 is said to show it, but the image is not in the dossier (Q2, Q22). This bears directly on enablement.
- The direction of poppet travel, and the meaning of "upper", "below" and "under" (Q3).
- The definition of the pressure differential, and when over-travel occurs during an inflation (Q4). The basis for saying "every floor pump reaches" the threshold (Q5).
- Whether the two-rate spring is essential, and its construction and rates (Q6, Q7).
- The geometry of the purge shoulder, the sealing face and the wipe (Q8, Q9, Q10). The form of the convolution and whether it is essential (Q11, Q12).
- The NiTi transformation temperatures and composition tolerance, and whether other alloys would work (Q13, Q14).
- The basis for each §4 range (Q15). The core body bore and the ring OD (Q16). How the ring is retained (Q17).
- The status of alternatives F1–F5 (Q18–Q21).
- The sketch images, which are absent (Q22). Details of the bench test that the data does not give (Q23). How the effect divides between the two cleaning actions (Q24).
- Tubeless use, other valve types, and sale as a retrofit core (Q25, Q26, Q33).
- The film found in the purge-gap region and its long-term effect (Q30). The sealing path at rest (Q31). Manufacturing alternatives and process windows (Q32).
- Prior public disclosure, use or sale of the prototypes (Q34). Prior solutions known to the inventor (Q35). What limits over-travel (Q36).

## Rationale

I treated §2 as the inventor's statement of the concept and §3–§8 as the embodiment, and kept them apart. That lets Prompt 03 build the nucleus ladder from §2 and §6 rather than from the prototype. The §6 alternatives matter disproportionately because they show the inventor already sees two things as open: the ring element need not be NiTi, and sealing and wiping can be separated. I therefore recorded the recurring elements (i)–(iv) in (b) as an observation, not as the nucleus.

As the brief requires, the bench data and the drawings README are used only as corroboration. Specifically:
- The per-core figures are reproduced in (l) because Prompt 03 and the Description will need them.
- The "audible snap" is recorded as an indirect indicator of over-travel, not as a measurement.
- The mean-inflation-time statement in §8 is quoted from the disclosure, not recomputed as a new fact.
- The sketches are cited only through the README's own words. The images are not in the dossier and I have not described them.

The most consequential finding is the inconsistency over the purge gap:
- §2 and §3(6) name different bores.
- The interference fit in §7 is hard to reconcile with a gap opening at the ring's outer surface when the ring expands outward.
- The README's description of FIG-2 confirms that there is a purge flow path, but it does not describe the mechanism.

I did not resolve this with a plausible mechanism, such as a fit over only part of the ring's length or the ring's edge lifting axially, because either reading would be an invented fact. The point is captured in Q1 and Q2, which should be the inventor's first questions: the Description cannot enable the air purge without the answer.

Every §4 range is marked "believed", not evidenced, because the inventor says so. This sets how far the Phase 3 ladders can go without inventor confirmation.

The inventor's name is labelled fictional and concerns inventorship, so it is not flagged as unrelated personal data. No third-party personal data appears. The test operator is not named.

This file replaces the earlier P1a output at the same path, which was written when `intake/data/` and `intake/drawings/` were empty. The questions have been renumbered: the earlier Q22 (missing bench data) is resolved, and the drawings question is now Q22.

## Assumptions

A1. "Presta-pattern" (§3(1)) is read as meaning the stem and core are dimensioned to work with conventional Presta pump heads and rims. *Inferred.* Not blocking.

A2. The prototype seat ring's outer diameter is taken as 2.7 mm. This is *inferred* from the tube stock in §7 (2.7 mm OD, 0.20 mm wall), which is consistent with the 2.3 mm ID in §4. The disclosure does not state the ring OD. Not blocking; confirm at Gate 1.

A3. "Pressure differential" (§2, §4) is read as the difference between pump-side pressure and tube-side pressure across the poppet. *Inferred.* Blocks P4 and P5 until Q4 is answered.

A4. "Upper" (§3(4)) is read as the pump or outer side, and "below"/"under" (§3(4), §3(5)) as the tube side. *Inferred from conventional valve orientation.* Blocks P4 (figure descriptions) until Q3 is answered.

A5. The poppet is taken to open and over-travel by moving towards the tube interior. *Inferred.* Blocks P4 until Q3 is answered.

A6. The two cleaning actions (air purge and snap-back wipe) are treated as the inventor's explanation of the mechanism. The bench test evidences the outcome, not how it divides between the two. Not blocking for P2; relevant to P3 and P5 through Q24.

A7. The three prototype cores are taken to share the §4 prototype values. *Inferred:* neither the disclosure nor the bench data says whether they differed. Not blocking.

A8. "Twice per inflation" (§2) is read as once per inflation event (from pump-head engagement to removal), not per pump stroke. *Inferred.* The bench data's audible snap "on pump-head removal" is consistent with this reading. Not blocking for P2; tied to Q4 for P4.

A9. The audible snap reported in the bench data is taken as indirect evidence that over-travel and recovery occurred at the test conditions (inflation from fully deflated to 6 bar, floor pump). It is not taken as evidence of over-travel distance, purge-gap size, or over-travel at other tube pressures. Not blocking; relevant to Q4 and Q23.

## Open Questions

Q1. Where is the purge gap (60)? §2 places it between the seat ring and "the stem bore"; §3(6) places it between the seat ring's outer surface and "the core body bore". Which is correct, or are both involved? Blocks P3, P4, P5.

Q2. How does the purge gap open when the seat ring is pressed into the core body with about 0.03 mm interference (§7) and expands radially outward (§2)? Which portion of the ring is in the interference fit, which surface moves away from which, and what is the full air path from the pump side through the purge gap into the tube? Please describe it in words, in addition to FIG-2. Blocks P3, P4, P5.

Q3. In which direction does the poppet move to open and to over-travel, and what do "upper", "below" and "under" refer to (pump side or tube side)? Blocks P4.

Q4. How is the over-travel pressure differential defined: pump side minus tube side, static or a transient surge? The test inflated from fully deflated. Does over-travel also occur when topping up a tube already near its target pressure, and does it occur on every pump stroke or only once per inflation? Blocks P3, P4, P5.

Q5. What is the basis for saying "every floor pump reaches" the threshold (§2)? The test used one floor pump. Does over-travel occur with hand pumps, CO2 inflators and compressors? Blocks P3, P4.

Q6. Is the two-rate return spring essential, or could the over-travel threshold be set by other means, for example a single-rate spring plus the seat ring's own stiffness, a second spring, or a detent? Is the prototype's second stage a variable-pitch spring, two springs, or something else? Blocks P3, P5.

Q7. What are the spring rates or forces of each stage, and at what stroke does the second stage engage? Does engagement coincide with the purge shoulder contacting the seat ring? Blocks P3, P4.

Q8. What is the geometry of the purge shoulder (form, diameter)? Where on the seat ring does it bear (upper edge or inner surface), and what is its axial clearance to the ring at rest and at the end of the normal stroke? Blocks P4.

Q9. What is the cone angle of the sealing face (42)? Is the at-rest seal metal-to-metal (brass poppet on the edge of the NiTi ring), with no elastomer anywhere in the seal path? Blocks P4.

Q10. In the snap-back wipe, which surface of the seat ring moves across which part of the poppet face, in what direction and over what distance? Blocks P3, P4.

Q11. Did the prototype ring have one or two convolutions? What are the convolution's profile and orientation? Is the wave produced by the laser cut, by forming on the mandrel or by the shape-set fixture (§7 is ambiguous)? Blocks P3, P4.

Q12. Would a straight-walled ring (no convolution), or another geometry that converts axial load into radial movement, work? Is the convolution essential? Blocks P3, P5.

Q13. What are the ring's As, Ms and Mf temperatures? What Af was actually achieved, and how was it measured? Is there a lower bound on Af? Blocks P3, P4.

Q14. What tolerance applies to the 55.8 wt% Ni composition, and has the inventor conceived other superelastic alloys (for example ternary NiTi alloys or copper-based alloys)? Blocks P3.

Q15. The §4 ranges are "ranges we believe would work". Which of them, if any, rest on tests, calculation or experience beyond the prototype value? Blocks P3, P4, P5.

Q16. What is the core body bore diameter at the seat ring, and what is the ring's actual OD? Blocks P4.

Q17. What range of interference fit works? Has the inventor conceived other ways of retaining the ring (adhesive, crimp, snap feature, integral forming)? Blocks P3, P4.

Q18. Was the stainless 303 core body built into a working core and tested? The bench data lists only brass-body prototypes, by implication. Blocks P4.

Q19. Was the hard-anodised aluminium sealing face built? Are other poppet materials or coatings conceived? Blocks P3.

Q20. Does the inventor regard Alternative A (PEEK ring) and Alternative B (brass seat plus stainless wiper ring) as within the invention? For B: what are the wiper ring's form and thickness, and how is it retained? Are other polymers conceived? Blocks P3, P4, P5.

Q21. Should the thermal two-way shape-memory variant (§6) be included as an embodiment, given the inventor's doubt and the absence of data? Blocks P3, P4.

Q22. The images of the sketches FIG-1 (at rest) and FIG-2 (full over-travel) are not in the dossier; only the README describes them. Please supply them. Are there, or can there be, sketches of the normal-stroke state, the snap-back wipe and Alternatives A and B? Blocks P4, PACKAGE.

Q23. Bench-test details that the data does not give:
- the sealant product and its ammonia content;
- how each tube was deflated "through the valve" (lock nut, manual poppet press), and whether deflation triggered over-travel;
- whether over-travel or purge-gap opening was ever measured directly, beyond the audible snap;
- whether the rising inflation times of the conventional cores were caused by partial blockage.

Blocks P4.

Q24. Has any test separated the air-purge effect from the snap-back wipe? Which does the inventor believe is necessary, and would either alone suffice? Blocks P3, P5.

Q25. Has the valve been used or tested in a tubeless set-up? Blocks P3, P4.

Q26. Has the inventor conceived use in Schrader or other valve types, in other tyres (motorcycle, car, wheelchair), or in other fluid valves prone to fouling? Blocks P3, P4, P5.

Q27. What is the seat ring's fatigue life beyond 40 over-travel cycles? Does residual strain build up, and does the purge gap stay closed at rest after long service (§9 item 1; the bench data confirms no fatigue testing)? Blocks P3, P4.

Q28. Under CO2 inflation, does chilling take the ring below Ms, and does it stay deformed until it warms (§9 item 2; the bench data confirms no cold-shock testing)? Blocks P3, P4.

Q29. Does the effect hold with ammonia-free sealants (§9)? Blocks P3, P4.

Q30. After 40 cycles, cured film was found on the ring's outer surface in the purge-gap region (§8; bench data). Does it build up over longer service, and could it stop the purge gap opening or closing? Has any mitigation been conceived? Blocks P3.

Q31. At rest, is the sealing face on the ring's edge the only seal, or must the ring's outer surface also seal against the core body (that is, is the closed purge gap airtight)? Blocks P4.

Q32. Manufacturing windows and alternatives: the laser-cut parameters; shape-set temperature and time ranges beyond 500 °C for 10 minutes; the depth removed by electropolishing; and any alternative forming routes conceived for the ring (stamping, etching, rolling, drawing a corrugated tube). Blocks P3, P4.

Q33. Is the core (parts 20–60) intended to be sold on its own as a replacement core for conventional Presta stems? Blocks P3, P5.

Q34. Before filing, has anyone shown the prototypes, the concept or the test results in public, used them in public, offered them for sale or published them? Grace-period treatment differs between the US, the EPO and the UK. Blocks P2, PACKAGE.

Q35. Can the inventor identify the existing coated-poppet, enlarged-bore and removable-insert products or documents referred to in §1? Blocks P2.

Q36. What limits over-travel to 0.5 mm in the prototype: a mechanical stop, coil-bind of the spring, or the seat ring itself? Blocks P4.

```json
{
  "prompt": "01",
  "status": "complete",
  "assumptions": [
    {"id": "A1", "text": "'Presta-pattern' read as dimensioned to work with conventional Presta pump heads and rims (inferred from §3(1)).", "blocking": false},
    {"id": "A2", "text": "Prototype seat ring OD taken as 2.7 mm, inferred from tube stock in §7; not stated as a ring dimension.", "blocking": false},
    {"id": "A3", "text": "'Pressure differential' read as pump-side minus tube-side pressure across the poppet (inferred).", "blocking": true},
    {"id": "A4", "text": "'Upper' read as pump/outer side, 'below'/'under' as tube side (inferred from conventional orientation).", "blocking": true},
    {"id": "A5", "text": "Poppet opens and over-travels towards the tube interior (inferred).", "blocking": true},
    {"id": "A6", "text": "Air purge and snap-back wipe treated as the inventor's explanation of mechanism; test evidences outcome, not attribution.", "blocking": false},
    {"id": "A7", "text": "The three prototype cores share the §4 prototype values (inferred).", "blocking": false},
    {"id": "A8", "text": "'Twice per inflation' read as per inflation event, not per pump stroke (inferred; consistent with the bench data's snap on pump-head removal).", "blocking": false},
    {"id": "A9", "text": "Audible snap in the bench data taken as indirect evidence of over-travel and recovery at test conditions only, not of over-travel distance, purge-gap size or behaviour at other tube pressures.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "Purge gap location: §2 says ring–stem bore; §3(6) says ring outer surface–core body bore. Which is correct?", "blocks": ["P3", "P4", "P5"]},
    {"id": "Q2", "text": "How does the purge gap open when the ring is interference-fitted (~0.03 mm) in the core body and expands radially outward? Full air path from pump side to tube, in words as well as FIG-2?", "blocks": ["P3", "P4", "P5"]},
    {"id": "Q3", "text": "Direction of poppet opening/over-travel and meaning of 'upper', 'below', 'under'.", "blocks": ["P4"]},
    {"id": "Q4", "text": "Definition of the over-travel pressure differential; does over-travel occur when topping up near target pressure; every stroke or once per inflation?", "blocks": ["P3", "P4", "P5"]},
    {"id": "Q5", "text": "Basis for 'every floor pump reaches' the threshold; hand pumps, CO2 inflators, compressors?", "blocks": ["P3", "P4"]},
    {"id": "Q6", "text": "Is the two-rate return spring essential, or can the threshold be set otherwise? Construction of the second stage?", "blocks": ["P3", "P5"]},
    {"id": "Q7", "text": "Spring rates/forces per stage and stroke at which the second stage engages; coincides with purge shoulder contact?", "blocks": ["P3", "P4"]},
    {"id": "Q8", "text": "Purge shoulder geometry, where it bears on the ring, and axial clearance at rest and at end of normal stroke.", "blocks": ["P4"]},
    {"id": "Q9", "text": "Sealing face cone angle; is the at-rest seal metal-to-metal with no elastomer?", "blocks": ["P4"]},
    {"id": "Q10", "text": "Snap-back wipe geometry: which ring surface moves across which poppet surface, direction and distance.", "blocks": ["P3", "P4"]},
    {"id": "Q11", "text": "Prototype convolution count, profile and orientation; is the wave made by laser cut, mandrel forming or shape-set fixture?", "blocks": ["P3", "P4"]},
    {"id": "Q12", "text": "Would a straight-walled ring or other geometry work; is the convolution essential?", "blocks": ["P3", "P5"]},
    {"id": "Q13", "text": "Ring As, Ms, Mf; achieved Af and how measured; lower bound on Af.", "blocks": ["P3", "P4"]},
    {"id": "Q14", "text": "Tolerance on 55.8 wt% Ni; other superelastic alloys conceived?", "blocks": ["P3"]},
    {"id": "Q15", "text": "Basis for each §4 'believed' range beyond the prototype value.", "blocks": ["P3", "P4", "P5"]},
    {"id": "Q16", "text": "Core body bore diameter at the ring and actual ring OD.", "blocks": ["P4"]},
    {"id": "Q17", "text": "Working range of interference fit; other ring retention methods conceived?", "blocks": ["P3", "P4"]},
    {"id": "Q18", "text": "Was the stainless 303 core body built into a working core and tested?", "blocks": ["P4"]},
    {"id": "Q19", "text": "Was the anodised aluminium sealing face built; other poppet materials/coatings conceived?", "blocks": ["P3"]},
    {"id": "Q20", "text": "Are Alternatives A (PEEK) and B (brass seat plus stainless wiper ring) within the invention; details of B's wiper ring; other polymers?", "blocks": ["P3", "P4", "P5"]},
    {"id": "Q21", "text": "Include the thermal two-way shape-memory variant as an embodiment despite inventor doubt and no data?", "blocks": ["P3", "P4"]},
    {"id": "Q22", "text": "FIG-1 and FIG-2 images are not in the dossier (README only); supply them; any sketches of normal stroke, snap-back wipe, Alternatives A and B?", "blocks": ["P4", "PACKAGE"]},
    {"id": "Q23", "text": "Bench-test details: sealant product/ammonia; deflation method and whether it triggered over-travel; any direct measurement of over-travel or gap opening beyond the audible snap; cause of conventional cores' rising inflation times.", "blocks": ["P4"]},
    {"id": "Q24", "text": "Has any test separated air purge from snap-back wipe; is either alone sufficient?", "blocks": ["P3", "P5"]},
    {"id": "Q25", "text": "Used or tested in a tubeless set-up?", "blocks": ["P3", "P4"]},
    {"id": "Q26", "text": "Schrader or other valve types, other tyres, other fouling-prone fluid valves conceived?", "blocks": ["P3", "P4", "P5"]},
    {"id": "Q27", "text": "Seat-ring fatigue life beyond 40 over-travel cycles; residual strain; does the purge gap stay closed at rest after long service?", "blocks": ["P3", "P4"]},
    {"id": "Q28", "text": "CO2 inflation: does chilling take the ring below Ms; does it stay deformed until warm?", "blocks": ["P3", "P4"]},
    {"id": "Q29", "text": "Does the effect hold with ammonia-free sealants?", "blocks": ["P3", "P4"]},
    {"id": "Q30", "text": "Cured film on the ring outer surface (purge-gap region) after 40 cycles: long-term accumulation and effect on gap opening/closing; mitigation?", "blocks": ["P3"]},
    {"id": "Q31", "text": "At rest, is the sealing face on the ring edge the only seal, or must the closed purge gap also be airtight?", "blocks": ["P4"]},
    {"id": "Q32", "text": "Manufacturing windows (laser, shape-set, electropolish) and alternative ring forming routes conceived?", "blocks": ["P3", "P4"]},
    {"id": "Q33", "text": "Is the core intended to be sold alone as a replacement core for conventional Presta stems?", "blocks": ["P3", "P5"]},
    {"id": "Q34", "text": "Any public showing, use, offer for sale or publication of prototypes, concept or results before filing?", "blocks": ["P2", "PACKAGE"]},
    {"id": "Q35", "text": "Can the inventor identify the coated-poppet, enlarged-bore and removable-insert products or documents referred to in §1?", "blocks": ["P2"]},
    {"id": "Q36", "text": "What limits over-travel to 0.5 mm: mechanical stop, spring coil-bind or the seat ring?", "blocks": ["P4"]}
  ],
  "new_terms": [
    {"term": "over-travel threshold", "maps_to": null, "reason": "Neutral short name for the inventor's 'pressure differential to reach over-travel (second spring stage)' (§4); avoids tying the concept to the spring."},
    {"term": "normal stroke", "maps_to": null, "reason": "Short form of the inventor's 'normal poppet stroke' (§4), used to distinguish from over-travel."},
    {"term": "air purge", "maps_to": null, "reason": "Names the first cleaning action described in §2 (air through the purge gap) so it can be referred to consistently."},
    {"term": "snap-back wipe", "maps_to": null, "reason": "Names the second cleaning action described in §2 (inventor's 'snap-back' and 'wiping action')."},
    {"term": "sealant film", "maps_to": null, "reason": "Inventor's 'film'/'cured latex' (§1, §2); neutral name for the deposit being removed, not limited to latex."}
  ],
  "support_refs": [
    {"item": "(a) problem: sealant drawn into core bore, dries, leak or block after 10–20 cycles", "support": "intake/disclosure.md §1; corroborated by intake/data/bench-test.md (C-1 to C-3 failure modes)"},
    {"item": "(a) existing attempts: coated poppet, enlarged bore, removable insert", "support": "intake/disclosure.md §1"},
    {"item": "(b) superelastic NiTi seat ring with sinuous wall; over-travel; purge shoulder; radial flex; purge gap; air purge; snap-back wipe", "support": "intake/disclosure.md §2, §3(3)–(6); intake/drawings/README.md (FIG-1, FIG-2)"},
    {"item": "(c) technical effect: keeps sealing and opening over more sealant-loaded cycles, no tool", "support": "intake/disclosure.md §2, §8; intake/data/bench-test.md"},
    {"item": "(d) components 10–70 and their functions", "support": "intake/disclosure.md §3(1)–(7); intake/drawings/README.md"},
    {"item": "(d) two-rate return spring", "support": "intake/disclosure.md §3(5)"},
    {"item": "(e) lock nut conventional; spring material immaterial", "support": "intake/disclosure.md §3(7), §5"},
    {"item": "(f) stainless 303 core body; anodised aluminium sealing face", "support": "intake/disclosure.md §5"},
    {"item": "(f) Alternative A PEEK ring; Alternative B two-piece seat; thermal two-way variant", "support": "intake/disclosure.md §6"},
    {"item": "(h) dimensions, ranges, pressures, Af", "support": "intake/disclosure.md §4"},
    {"item": "(h) materials and NiTi composition", "support": "intake/disclosure.md §5"},
    {"item": "(h) ring OD 2.7 mm (inferred) and interference 0.03 mm", "support": "intake/disclosure.md §7"},
    {"item": "(i) pressure-actuated state behaviour", "support": "intake/disclosure.md §2, §3(5), §4"},
    {"item": "(j) laser cut, shape-set 500 °C/10 min, water quench, electropolish, press fit", "support": "intake/disclosure.md §7"},
    {"item": "(k) inner tubes and tubeless with sealant; lower-cost line; manual purge", "support": "intake/disclosure.md §1, §6"},
    {"item": "(l) bench test protocol, failure criterion and summary results", "support": "intake/disclosure.md §8"},
    {"item": "(l) per-core cycles, failure modes, inflation times, leak-down; audible-snap indicator; stereo-microscope inspection; no fatigue or cold-shock test", "support": "intake/data/bench-test.md"},
    {"item": "(m) fatigue, CO2, ammonia-free sealants", "support": "intake/disclosure.md §9; intake/data/bench-test.md notes"}
  ],
  "disclosure_requests": [
    {"limitation": "Purge gap location and air path (§2 vs §3(6), with §7 interference fit)", "needed_disclosure": "Consistent written description of which surfaces bound the purge gap, how outward ring deflection opens it, and the complete air path from pump side to tube, sufficient for enablement."},
    {"limitation": "Over-travel threshold mechanism", "needed_disclosure": "Spring stage rates/forces, engagement stroke, over-travel stop, and whether means other than a two-rate spring can set the threshold."},
    {"limitation": "§4 ranges", "needed_disclosure": "Basis (test, calculation or experience) for each range beyond the prototype value."},
    {"limitation": "Evidence of over-travel and purge-gap opening", "needed_disclosure": "Any direct measurement of over-travel distance and purge-gap opening, beyond the audible snap on pump-head removal."},
    {"limitation": "Figures for reference numerals 10–70", "needed_disclosure": "The FIG-1 and FIG-2 image files, and sketches of the normal-stroke state and of Alternatives A and B if the inventor has them."}
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

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/intake/data/bench-test.md`

```markdown
<!-- FICTIONAL example for testing; not a real invention -->

# Bench test — sealant-loaded inflation cycling

Test dates: 2026-08-12 to 2026-08-20. Tube: 700×28, 60 ml latex sealant. Cycle: inflate to 6 bar with a floor pump, hold 24 h at 22 °C, deflate fully through the valve. Failure: leak-down > 0.5 bar in 24 h, or pump unable to open valve within 5 s. All values fictional.

| Core | Type | Cycles to first failure | Failure mode | Inflation time, cycle 1 (s) | Inflation time, last cycle (s) | Leak-down at last cycle (bar/24 h) |
|---|---|---|---|---|---|---|
| C-1 | Conventional | 14 | blocked (pump could not open) | 41 | 68 (cycle 13) | 0.1 |
| C-2 | Conventional | 12 | leak-down 0.7 bar | 40 | 44 (cycle 11) | 0.7 |
| C-3 | Conventional | 18 | blocked | 42 | 75 (cycle 17) | 0.2 |
| P-1 | Prototype (NiTi seat) | none in 40 | — | 43 | 47 (cycle 40) | 0.1 |
| P-2 | Prototype (NiTi seat) | none in 40 | — | 41 | 46 (cycle 40) | 0.1 |
| P-3 | Prototype (NiTi seat) | none in 40 | — | 44 | 50 (cycle 40) | 0.2 |

Notes:
- Inflation time measured from pump-head engagement to 6 bar, same pump, same operator.
- Over-travel was confirmed on every prototype inflation by an audible snap on pump-head removal.
- Prototype rings were inspected under a stereo microscope at cycle 40: cured film present on the ring outer surface in the purge-gap region; sealing edge and poppet face clean.
- No fatigue or cold-shock testing was performed.
```

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

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/intake/data`/

## Files to write

Write each of these with your Write tool, at exactly this path, one file per call (the folders exist). Write nothing outside the run folder `{R}`. Do not run the checks yourself: the runner runs them and will tell you if anything fails.

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P4/17.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P4/enablement-gaps.md`

When every file is written, reply with one line per file (path and a few words on what it holds) and anything the runner must route: open questions, disclosure requests, open disagreements, narrowing suggested. Nothing else.
