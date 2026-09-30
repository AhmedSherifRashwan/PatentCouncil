# Patent Council · matter `valve-oc-20260930` · run `r1` · step `P4a` · profile full

You are the **Specification Drafter**. Follow your AGENTS.md. This message is the whole brief: what to do, the prompts to execute, every input (embedded below, so do not re-read those files), and the exact files to write.

## What to do

Run Prompt 16. Its section plan must split the detailed description into **5 parts** of similar size that can be drafted independently: list them as `Part 1` … `Part 5`, each with its sections, figures and claim families. The risk report may still be in progress: use it if embedded.

**Time budget:** about 10 minutes. The whole matter is planned to finish end to end in two hours. Be complete, but write each deliverable once: no drafts, no repetition, no padding.

## Prompt 16 — Specification blueprint  (kind `drafting`)

**Write your reply to:** `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P4/16.md`

*Build the disclosure before polishing prose.*

Create a complete patent specification outline comprising title, technical field, background, problem, summary, brief description of drawings, detailed description, definitions, embodiments, examples, manufacturing/assembly, operation/use, alternatives, ranges, data/results and claim-support sections. Map every proposed claim family to the sections needed to support it.

**How to work.** Draft only from confirmed embodiments (`CONFIRMED.md`), the Phase 1 outputs and the differentiation matrix; unconfirmed Phase 3 candidates are not in front of you and must not reappear. Use the locked terminology verbatim. Never fabricate experimental data or results. Under `### Specification Blueprint` give the outline as a nested list with a stable section id for each node (S1, S1.1 ...), a one-line statement of what the section will contain and which dossier material feeds it. Under `### Claim-Family Support Map` give a table: claim family (from the value map: apparatus, system, method of use, method of manufacture, composition, kit, consumable, controller/software, product-by-process as justified) | sections that must support it | confirmed embodiments relied on | gaps. This blueprint drives Prompts 17-20a and the description compose step, so the section ids must be reused there. Reply exactly in the drafting output contract: `## Deliverable` (with the H3 sections named above), `## Rationale`, `## Assumptions`, `## Open Questions`, then one final fenced `json` envelope. No preamble before `## Deliverable`; nothing after the envelope. Reuse locked preferred terms verbatim; declare any other term in `new_terms` with a reason.

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

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/intake/drawings/README.md`

```markdown
<!-- FICTIONAL example for testing; not a real invention -->

# Drawings supplied with the disclosure

Two inventor sketches exist. They are referenced by name only in this fixture;
no image binaries are committed. The runner passes this README to the agents so
they know the figures exist and what each shows; the agents cannot see images.

| File | Placeholder | Content |
|---|---|---|
| `FIG-1.png` | not present in fixture | Axial section of the valve core in the closed, at-rest state: stem (10), core body (20), seat ring (30) with its convoluted wall, poppet (40) with sealing face (42) and purge shoulder (44), two-rate return spring (50), purge gap (60) closed, lock nut (70). |
| `FIG-2.png` | not present in fixture | The same section at full over-travel during inflation: poppet displaced beyond normal stroke, purge shoulder (44) bearing on the seat ring (30), ring expanded radially, purge gap (60) open, arrows showing air flow through the main passage and through the purge gap into the tube. |

Reference numerals in the sketches match those used in `disclosure.md` §3.
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

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/intake/data`/
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/intake/drawings`/

## Inputs that do not exist yet (work without them; do not wait)

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P2/09.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P2/10.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/risk/pre-drafting-findings.md`

## Files to write

Write each of these with your Write tool, at exactly this path, one file per call (the folders exist). Write nothing outside the run folder `{R}`. Do not run the checks yourself: the runner runs them and will tell you if anything fails.

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P4/16.md`

When every file is written, reply with one line per file (path and a few words on what it holds) and anything the runner must route: open questions, disclosure requests, open disagreements, narrowing suggested. Nothing else.
