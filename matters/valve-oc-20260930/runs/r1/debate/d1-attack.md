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
