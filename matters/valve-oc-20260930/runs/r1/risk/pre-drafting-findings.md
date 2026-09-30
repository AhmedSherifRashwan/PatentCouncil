## Summary

This report is a drafting and analysis aid prepared by AI. It is not legal advice and says nothing about whether the invention is patentable; qualified patent counsel signs off before anything is filed.

**Inputs read.** Phase 1 (`01`, `03`), Phase 2 (`08`, `09`, `10`), `CONFIRMED.md` (the content of 11–15), the Debate 2 attack (`debate/d2-attack.md`) and `lessons.md`. The Debate 1 attack on `09`, `07`, `02` and `terminology/LOCKED.md` were not embedded (A2, A3, A6, A7). Jurisdictions are US, EPO and UK (A5).

**Counts.** 21 findings: **2 critical**, **12 high**, **5 medium**, **2 low**. P4 owns 3 of them, P5 owns 3, and P4 and P5 share the other 15.

**The five risks that matter most:**

1. **PF-1 (critical).** The purge gap's location and opening mechanism contradict each other (§2 against §3(6) and §7). Drafting cannot fix this. The nucleus is not enabled until the inventor answers 01 Q1/Q2.
2. **PF-2 (critical).** A naive claim ("a resilient seat that the poppet deflects to open an additional flow path") reads on ref-02 claim 4 with [0019], and in the real art on US4462449A claim 1. On this pile, novelty rests on three relationships, and the independent claim must carry them.
3. **PF-3 (high).** The locked definition of `purge gap`, as `11` DA-2 quotes it, fixes one species: an annular radial clearance between the seat ring outer surface and the core body bore. That is both the contradicted location and a free design-around.
4. **PF-4 (high).** Gate 2 was confirmed unattended. Much of `CONFIRMED.md` is marked "not conceived — inventor to confirm", and the intermediate and preferred ranges in `13` come from an interpolation convention, not from the inventor. Writing either into the Description as the inventor's own is a possession and inventorship risk.
5. **PF-5 (high).** The threshold that carries novelty over ref-02 (PF-2) is also the cheapest design-around (DA-1 / R4, purge on every opening), and a teardown cannot detect it. Keep it in claim 1. Cover the escape with a second independent claim that does not rely on it.

**Coverage warning (L6).** Every novelty rating here was measured against a thin pile: 15 machine-retrieved extracts, English only, and two fictional requester summaries (08 Q1, Q2). A professional search is still warranted before counsel relies on any of it (PF-13).

## Findings

### PF-1 — Purge gap location and opening are self-contradictory

- **Category:** enablement. **Severity:** critical. **Owner:** P4+P5.
- **Concerns:** nucleus element N0(d) (C6, C7); `09` row 2; `10` items 1–3; every passage that describes the purge state.
- **Evidence:**
  - §2 places the gap at the "stem bore" and says the ring "flexes radially outward".
  - §3(6) places it between the "seat ring outer surface and the core body bore".
  - §7 presses the ring in with about 0.03 mm interference.
  - Outward flexing would close a gap at the outer surface, not open one (01 (m), Q1, Q2; 03 N0 enablement caution; 08 Q4; 12 §7 E7.1).
  - d2-attack R1: "copy the prototype, litigate the gap".
- **Risk:** Insufficiency and lack of written description (EPC Art. 83; 35 U.S.C. §112(a); UK s.14(3)), and a clarity attack on every claim that recites the purge gap. If N0(d) cannot be enabled, N0 falls back towards ref-02 claim 4 with [0019] (08 Q4). A genus wording cannot hide a contradiction in the only worked example.
- **Drafting response:**
  1. **Do not draft the purge-state mechanism until 01 Q1/Q2 are answered.** If they stay unanswered at P4, write the Description so that it states only what is consistent: the purge gap is closed at rest, opened by deflection of the deflectable ring element in over-travel, and carries flow into the inflatable chamber (FIG-2 per the README). Do not choose between §2 and §3(6), and do not use `12` E6.2 or E7.1–E7.4 as the inventor's mechanism.
  2. Once the answer exists, describe the prototype's surface pair, direction of movement and full air path in words, and reconcile the interference fit, for example by stating which band of the ring is fitted.
  3. **Independent claims:** define the purge gap by function and state only. It is a passage bounded at least in part by the deflectable ring element, closed in the closed state and in the normal-open state, and opened by the deflection. Do not recite the bounding surfaces or the direction of deflection.
  4. **Claims hedge:** make sure one independent claim (PF-6) stands on the over-travel sequence and on shape recovery, so the family does not depend entirely on N0(d).
  5. Route to the inventor as the first of the top-ten questions (L8).

### PF-2 — A naive "deflectable seat opens an extra path" claim is anticipated

- **Category:** novelty. **Severity:** critical. **Owner:** P4+P5.
- **Concerns:** independent claim to the valve core (value map rank 1; N0); the definitions of the states in P4.
- **Evidence:**
  - ref-02 claim 4 ("lip seal deflectable by the poppet during opening"), [0019] (deflection enlarges the flow passage) and [0020] (recovers when the pump is removed): 08, 09 row 1–2.
  - Real art: US4462449A claim 1 (the closure member deforms a resilient member after initial travel).
  - EP1137892A1 claims 1(e) and 8 (a gap opens above a threshold on chamber-side pressure).
  - 08 "What the attack shows" §1–2: none of the three relationships is in the pile.
- **Risk:** A claim that lets "purge gap" read on the main passage, or that drops the normal-stroke/over-travel sequence, falls for lack of novelty at the EPO, the USPTO and the UKIPO.
- **Drafting response:**
  1. **P5:** the broadest valve-core claim carries all three relationships, in positive wording (L1):
     - (i) the poppet has a normal stroke in which the main passage is open and the purge shoulder is spaced from the deflectable ring element;
     - (ii) over-travel beyond the normal stroke occurs when the pressure differential exceeds an over-travel threshold higher than the crack pressure, and in over-travel the purge shoulder bears on and deflects the deflectable ring element;
     - (iii) a purge gap, separate from the main passage, is closed in the closed state and the normal-open state and opened in the purge state.

     Use `09` rows 1–2 "possible claim language" as the starting point. Do not write "does not contact": use "is spaced from".
  2. **P4:** define `closed state`, `normal-open state` and `purge state` in one paragraph, using the claim's words (01 (i) state table), so that the support map (L2) can point to it.
  3. P4 must also say in terms that the main passage and the purge gap are different flow paths (FIG-2 README).

### PF-3 — The locked definition of "purge gap" fixes the contradicted species

- **Category:** design-around. **Severity:** high. **Owner:** P4+P5.
- **Concerns:** `terminology/LOCKED.md` entry for `purge gap`; every claim and paragraph that uses the term.
- **Evidence:** 11 DA-2 quotes the locked term as "an annular radial clearance between the seat ring outer surface and the core body bore, §3(6)". DA-3 (slotted or segmented purge openings) and d2-attack R1 and R8 all escape an "annular" gap at a fixed surface pair. 12 §7 gives a functional genus.
- **Risk:** Locked terms are law (non-negotiable 7). If the locked definition is written into the Description as the meaning of the term, every claim inherits the §3(6) location, which is both contradicted (PF-1) and avoidable at no cost (DA-2, DA-3). Under US claim construction and at the EPO, a definition in the Description limits the claim.
- **Drafting response:**
  1. Do not reproduce the locked species definition as the definition of `purge gap`. Define `purge gap` functionally (PF-1, step 3).
  2. Present the §3(6) location as the prototype's location, and only after 01 Q1/Q2 are answered.
  3. Describe "annular gap, slits or apertures through the wall, or gaps between fingers" only if the inventor confirms them (11 Q3).
  4. Raise with the runner, as an open disagreement, that the lock should be amended to the functional definition (Q11).

### PF-4 — Unattended Gate 2: unconceived entries and AI-interpolated ranges

- **Category:** support. **Severity:** high. **Owner:** P4+P5.
- **Concerns:** the whole of `CONFIRMED.md`. This covers 12 entries marked "not conceived — inventor to confirm", 11's "needs inventor confirmation" genera, 13's "(proposed)" intermediate and preferred ranges, and the candidate mitigations in 15 (FM-1 to FM-21).
- **Evidence:**
  - `CONFIRMED.md` header: "Confirmed at Gate 2 by Orchestrator (auto-unattended)".
  - d2-attack §7 item 6 and A3.
  - 13 method note: the ranges come from "a drafting convention … not itself data".
  - Non-negotiable 4 ("nothing the inventor has not conceived goes into the specification as though they had").
  - USER.md directives on candidates and on filling gaps.
- **Risk:**
  - In the US, content the inventor did not conceive raises inventorship and oath problems.
  - Prosecution arguments that rest on those passages invite lack-of-possession attacks.
  - The 13 ranges invent preferred sub-ranges with no basis. Two of them are asymmetric because of clipping: convolution amplitude 0.08–0.16 and over-travel 0.4–0.65. An examiner or opponent will ask what the basis is, and the answer is "none".
  - Leaving the alternatives out, on the other hand, gives away the design-around cover (PF-9). They cannot be added after filing without new matter.
- **Drafting response:**
  1. P4 writes only disclosed content (*disclosed (§n)*) as the inventor's embodiments.
  2. Hold every "not conceived" entry out of the Description until the inventor confirms it, and put it in the top-ten question form (L8) grouped by claim impact (Q4).
  3. If the run must finish unanswered, keep a list of the held passages in the package cover note so counsel can add them before filing.
  4. For 13, use only the §4 broad ranges and the prototype values. Do not use the proposed intermediate or preferred ranges unless the inventor adopts them (Q10).
  5. P5 does not rely on any held passage for support.

### PF-5 — The novelty-carrying threshold is the cheapest, undetectable design-around

- **Category:** design-around. **Severity:** high. **Owner:** P4+P5.
- **Concerns:** N0(b), C3, C17; the threshold-setting arrangement; 11 DA-1, DA-11; d2-attack R4, R12.
- **Evidence:**
  - 08 rates N0 novelty *weak* only if the normal-stroke/over-travel sequence is kept.
  - 11 DA-1 (single-rate spring, purge on every opening) is rated commercially high.
  - 12 E2.3 (the ring's own stiffness as the threshold).
  - d2-attack R4: whether a product has a distinct threshold "is a bench measurement of force against stroke", not visible in a teardown.
  - Whether purging on every opening works is unanswered (03 Q3; 11 Q1).
- **Risk:** Removing the threshold from claim 1 brings it back onto ref-02 (PF-2). Keeping it leaves an escape that is hard to prove. Tying the threshold to the two-stage return spring loses DA-11/R12 as well. A "threshold-setting arrangement" claimed without structure may be construed under 35 U.S.C. §112(f), limited to the disclosed structures and their equivalents.
- **Drafting response:**
  1. **P5:** keep the threshold relationship in the main valve-core claim, stated as a relationship ("an over-travel threshold higher than the crack pressure"), not as a spring.
  2. **P5:** cover DA-1 with a separate independent claim built on the separate purge gap plus shape recovery, or on the wipe (PF-6), which does not need a second threshold. Do this only if the inventor confirms that purging on every opening works.
  3. **P4:** disclose more than one structure for the threshold-setting arrangement so that a §112(f) reading is not fatal. Beyond the two-stage return spring (§3(5)) that means E2.2–E2.5 and E2.3, and only once the inventor confirms them (Q3). Unconfirmed, the arrangement has one species, and P5 must know that.
  4. **P4 and P5:** add teardown-visible dependent rungs: a second spring stage, a lost-motion clearance, and the axial clearance between the purge shoulder and the deflectable ring element at the end of the normal stroke (01 Q7, Q8).

### PF-6 — Effect is not attributed to purge or wipe; the family needs a second nucleus

- **Category:** support. **Severity:** high. **Owner:** P4+P5.
- **Concerns:** N0(d) against N1; 03's wipe-based alternative nucleus; 11 DA-10; d2-attack R7, R17.
- **Evidence:**
  - The bench test does not separate the air purge from the snap-back wipe (01 (l), Q24; 03 Q1, A2; 08 Q5).
  - 08 rates the wipe-based alternative nucleus *weak* on novelty (row N1 is absent from all 17 references) and *moderate* on inventive step (ref-02 + US4719938A, kinematic inversion).
  - `09` row 3: the relative movement comes from recovery of a ring held in the core body, not from the valve member's stroke.
- **Risk:** If the air purge is claimed as essential and the wipe turns out to carry the effect, a competitor seals the periphery (R7) and escapes, and a teardown cannot show it. If the Description says either action alone is sufficient, it asserts a fact nobody has tested.
- **Drafting response:**
  1. **P4:** describe the cleaning action as "the air purge, the snap-back wipe, or both", and describe the snap-back wipe independently of any flow. State the bench result honestly: the outcome is shown, and the attribution is not.
  2. **P5:** file two independent valve-core claims:
     - (A) the PF-2 claim, with the separate purge gap;
     - (B) the over-travel sequence plus a deflectable ring element held in the body whose shape recovery, when the pressure differential falls, moves it across a surface of the poppet (`09` row 3 wording). No flow limitation.

     Claim (B) also covers the DA-1 route if the threshold is dropped from it after the inventor confirms (PF-5). Claim (B) must answer the kinematic-inversion argument: the recovery of the fixed ring, not the stroke, drives the relative movement.
  3. Revisit after 03 Q1 is answered (Q2).

### PF-7 — Inventive-step mosaic, and effect evidence that is not against the closest art

- **Category:** novelty (inventive step). **Severity:** high. **Owner:** P4.
- **Concerns:** the N0 inventive-step position; problem-and-effect passages in the Description; the Examples.
- **Evidence:**
  - 08: ref-02 (or US4462449A) + EP1137892A1 + CN215861914U, rated *moderate*. It is stronger in the US (a combination of known elements) than under the EPO problem-solution approach or UK practice.
  - The EP1137892A1 threshold acts on chamber-side pressure and releases air outwards.
  - The bench data compares the prototypes only against conventional cores, not against a deflecting-seat valve (08 Q6).
- **Risk:** At the EPO the objective problem is framed against ref-02, and the effect then has to be credible against a deflecting seat. With no statement of why each relationship matters, the examiner frames the problem as "an alternative valve", and the combination becomes obvious.
- **Drafting response:**
  1. **P4:** state the technical problem as the inventor does in §1: sealant film cures on the valve core surfaces over repeated inflations, and coatings and bores only slow the build-up.
  2. Tie each relationship to its effect, in the Description:
     - the threshold means inflation and sealing behave as in a conventional valve core until the purge state is reached;
     - the purge flows in the inflation direction, into the inflatable chamber;
     - the fixed ring's recovery drives the wipe.
  3. Report the bench test as an Example with its limits: n = 3 per group, one sealant, 40 cycles, over-travel inferred from an audible snap.
  4. Do not characterise the effect against a ref-02-type seat without data. Route 08 Q6 so that a comparison can be added in prosecution as post-filing evidence where the jurisdiction allows it.

### PF-8 — Wipe wording invites the "no snap" and "rubber disclaimer" arguments

- **Category:** design-around. **Severity:** high. **Owner:** P4+P5.
- **Concerns:** `snap-back wipe`, §2's rubber comparison, §6's "weaker wipe" for PEEK; d2-attack R14, R15; 11 DA-15; 14 footnote [a] and sentence 6.
- **Evidence:** §2 ("fast and stiff"; latex "would simply embed itself" in rubber). §6 (the PEEK "wipe is weaker"). No lower bound on wipe force or speed is disclosed.
- **Risk:**
  - A claim to a "snap-back" wipe is indefinite, or simply not met, against a PEEK or polymer ring.
  - §2 copied as written reads as a disclaimer of elastomer-like rings in all three jurisdictions.
- **Drafting response:**
  1. **P4:** define the snap-back wipe as movement of the recovering deflectable ring element across a surface of the poppet, with no speed or force qualifier.
  2. **P4:** present superelastic recovery as preferred because it gives a stronger wipe, not as the definition.
  3. **P4:** rewrite §2's rubber point as a disadvantage of soft seats that deform under the sealing face, not as an exclusion of a class of material.
  4. **P4:** describe the PEEK wipe as within the definition (14 sentence 6).
  5. **P5:** keep "snap" and "fast/stiff" out of every claim.
  6. An elastomer embodiment stays out unless the inventor conceived one (11 Q15).

### PF-9 — Nucleus components defined by the prototype species

- **Category:** design-around. **Severity:** high. **Owner:** P4+P5.
- **Concerns:**
  - the purge shoulder (DA-4, R9);
  - a separate versus an integral deflectable ring element (DA-5, R10);
  - a continuous versus a slotted or segmented ring, and resilient metal or polymer (DA-3, DA-13, DA-14, R8, R13);
  - the valve format: core body versus the valve stem, and Schrader-pattern (DA-6, R6);
  - over-travel produced by mechanical actuation (DA-9, R5).
- **Evidence:** 11 findings 2–4; 12 §§3, 4, 12, 16; d2-attack §7 item 2 and ranking table (R5, R6, R8, R9 and R10 all rated high commercial pull).
- **Risk:** Each prototype word used in claim 1 (shoulder, separate ring, annular, NiTi, core body threaded into a Presta stem) is a cheap escape. The OEM integrated-stem route (R6) takes the highest-value channel (02 rank 3).
- **Drafting response:**
  1. **P5:** use the genus words in the independent claims:
     - a purge shoulder of the poppet (not "an annular shoulder below the sealing face");
     - a deflectable ring element, not tied to material or form;
     - a valve body carrying it (no "threaded", no "Presta-pattern").
  2. **P5:** add an independent claim to the inflation valve as well as the core, and do not recite what causes over-travel in the apparatus claim.
  3. **P4:** describe each broader species only once the inventor confirms it (Q4). Until then, describe the disclosed species (§3, §6) and state that the terms are not limited to them, **without listing unconceived species**.

### PF-10 — Behaviour-only limitations and divided infringement

- **Category:** design-around. **Severity:** high. **Owner:** P4+P5.
- **Concerns:** limitations that only a bench test can prove: the threshold, flow through the purge gap, the wipe (R4, R7, R14); d2-attack R5 (the pump head drives over-travel, so the core and the head come from different suppliers).
- **Evidence:** d2-attack §7 item 3; 11 finding 6 (DA-1, DA-9 and DA-10 need a bench test on the product); `10` item 2 (the method is hard to detect in infringement).
- **Risk:** Claims that are infringed but cannot be proven, and claims whose infringers are split between a valve maker, a pump maker and the rider.
- **Drafting response:**
  1. **P5:** pair each functional independent claim with dependent rungs that a teardown shows:
     - a second spring stage;
     - a lost-motion clearance;
     - a deflectable ring element held in the body with the purge shoulder axially spaced from it at rest;
     - the prototype geometry once PF-1 is resolved.
  2. **P5:** add a claim to the valve core combined with an inflation head that depresses the poppet into over-travel, only if the inventor confirms mechanical actuation (11 Q9). E1.5 (over-travel by hand) conflicts with §2's "no rider action", and the inventor decides.
  3. **P5:** use the method of operation only as a dependent or use claim (`10` item 2).
  4. **P4:** describe the structures that produce each behaviour, so that the dependent rungs have support (L2).

### PF-11 — Figure images absent

- **Category:** formal. **Severity:** high. **Owner:** P4.
- **Concerns:** Brief Description of the Drawings; the reference numerals 10–70; the description of the purge state (FIG-2).
- **Evidence:** 01 Q22 (only the README describes FIG-1 and FIG-2); 01 A4/A5 (orientation inferred); L4.
- **Risk:**
  - Drawings are needed to understand a mechanical valve (35 U.S.C. §113; the EPC and UK practice equivalents). New drawing content cannot be added after filing without new matter.
  - Figure descriptions written from a one-line README invent detail.
  - Wrong orientation words ("upper" and "below") propagate into the claims.
- **Drafting response:**
  1. Describe the figures only to the extent the README states them, and do not describe unseen geometry.
  2. Register numerals 10–70 (L4).
  3. Hold orientation words until 01 Q3 is answered, or define them once ("supply side" and "chamber side", as `10` does) and use only those.
  4. Flag in the package that FIG-1 and FIG-2 images, and a normal-open-state figure, are needed before filing (Q5).

### PF-12 — Seat ring component claim is exposed to US9982818B2

- **Category:** novelty. **Severity:** high. **Owner:** P4+P5.
- **Concerns:** value map rank 2 (the seat ring as a component); `10` item 6; d2-attack R18 (kit or component sale).
- **Evidence:** 08 rates the claim *strong* against a ring defined only by material and wave wall, citing US9982818B2 (abstract; claims 3, 4, 9: a NiTi wave-profile sealing ring). A "for a valve core" preamble is read as "suitable for" at the EPO and usually does not limit in the US. The extract gives no dimensions (08 Q3).
- **Risk:** A component claim loses the valve context that carries novelty. A claim to "a NiTi ring with a convoluted wall" is anticipated or obvious.
- **Drafting response:**
  1. **P5:** file a component claim only with:
     - a sealing edge;
     - a convoluted wall that converts axial load on the sealing edge into radial deflection;
     - the §4 broad dimensions.
  2. **P5:** consider a kit claim (ring + poppet with purge shoulder + return spring) that carries the relationship from PF-2. This depends on 11 Q19.
  3. **P4:** describe the axial-to-radial function and the §4 ring dimensions in words (§3(3), §4).
  4. The Prosecution Assessment should mark this claim as dependent on the full text of US9982818B2 (Q9).

### PF-13 — Thin, partly fictional reference set

- **Category:** novelty. **Severity:** high. **Owner:** P4+P5.
- **Concerns:** every novelty and inventive-step position in this report and in 08–10.
- **Evidence:**
  - 08 Q1–Q3: 15 machine-retrieved extracts, English only, one engine, no non-patent literature, no CPC walk.
  - ref-01 and ref-02 are fictional.
  - The full texts of US4462449A, US9982818B2, EP1137892A1 and US4719938A are not yet read.
  - Lessons L6.
- **Risk:** The *weak* novelty ratings for N0 and N1 are weak against this pile only. A first office action may cite art that removes one of the three relationships.
- **Drafting response:**
  1. **P4:** make the fallback ladder deep. Describe every disclosed rung (N1–N7 of `03`, and `09` rows 1–7) with its effect, so that amendment has a basis whatever turns up.
  2. **P5:** build dependent claims so that each of the three relationships and the wipe can be promoted on its own.
  3. The package states the coverage limit plainly and recommends a professional search before filing (Q9).
  4. Do not describe any prior document in the Background beyond what §1 says.

### PF-14 — Numbers, materials and field of use in independent claims

- **Category:** design-around. **Severity:** high. **Owner:** P5.
- **Concerns:** N4 (superelastic alloy, Af), N6 (ranges), PEEK, sealant, tubeless; d2-attack R11, R13, R19; 11 DA-16.
- **Evidence:**
  - §4 says the ranges are "believed", not evidenced (01 (h)).
  - 08 rates the N6 ranges *strong* as routine optimisation.
  - A polymer has no Af (14 [g]).
  - R19: a core sold "for tubes only" escapes any claim that recites sealant.
- **Risk:** The whole patent is avoided by a tolerance, a material or a label.
- **Drafting response:**
  1. Keep ranges, materials, Af, PEEK, sealant, tubeless and Presta-pattern out of every independent apparatus claim.
  2. Lead with relationships: the over-travel threshold is above the crack pressure and within what the inflation device reaches; the purge gap is closed at rest.
  3. Put sealant only in dependent claims, in use claims and in the inflatable chamber claim (value map rank 3).
  4. Condition the Af dependent claim on the superelastic species (14 sentence 2).

### PF-15 — Ladder increments N2, N4–N7 and the manufacturing method carry no inventive step

- **Category:** novelty. **Severity:** medium. **Owner:** P5.
- **Concerns:** the dependent claim ladder; value map rank 4 (method of manufacture).
- **Evidence:**
  - N2 is known from ref-02 claim 1.
  - N4 is known from US6393765B1 and US9982818B2.
  - N5 is standard means (US9297373B2, EP1137892A1 claim 28, US4627461A).
  - N6 and N7 are routine or CGK.
  - The method claim is rated *moderate to strong* once the ring is known (08).
- **Risk:** Prosecution budget spent defending fallbacks that cannot stand on their own. A method claim that survives only through its product.
- **Drafting response:**
  1. Keep these as dependent claims for commercial scope and for amendment, not as the independent inventive contribution.
  2. Do not file a separate method-of-manufacture family unless the inventor supplies a process effect or process windows (01 Q32; 03 Q15).
  3. **Narrowing noted, not applied:** if one of the three relationships falls, the next promotion is the snap-back wipe (N1), not the material (N4).

### PF-16 — Alternative B: thin support and inventive-step exposure

- **Category:** support. **Severity:** medium. **Owner:** P4+P5.
- **Concerns:** E-III; 11 DA-17; `10` item 4; d2-attack R16, R17.
- **Evidence:**
  - §6 gives one paragraph and no geometry (03 Q7).
  - 08 rates ref-01 + US4719938A as *moderate* (kinematic inversion).
  - d2-attack: E-III claimed without the purge gap "is a scraper".
- **Risk:** Written description limited to one sentence. An E-III claim that is obvious if it relies only on "a wiper ring deflected by the poppet".
- **Drafting response:**
  1. **P4:** describe E-III no further than §6 until the inventor answers 03 Q5 and Q7.
  2. **P5:** cover E-III through the deflectable ring element genus in the main claims, not through a separate independent claim, unless that claim carries the over-travel-only purge gap and the threshold (PF-2).

### PF-17 — Undisclosed mechanism details: orientation, spring stages, over-travel stop, geometry

- **Category:** enablement. **Severity:** medium. **Owner:** P4.
- **Concerns:**
  - the direction of travel and the meaning of "upper" and "below" (01 Q3);
  - spring rates and the engagement stroke (01 Q7);
  - what limits over-travel (01 Q36; 15 FM-9);
  - the purge shoulder geometry (01 Q8);
  - the sealing face cone angle (01 Q9);
  - the wipe geometry (01 Q10).
- **Evidence:** 01 (h) list of values not given; 13 Table 4.
- **Risk:** Enablement probably holds for a skilled valve designer given the prototype values. What is missing is support for dependent rungs, and the assertion in §2 that "every floor pump reaches" the threshold (01 Q5), which has no basis.
- **Drafting response:**
  1. Describe what the disclosure gives and leave out what it does not.
  2. Do not add a stop, rates or angles.
  3. Qualify "every floor pump" as the inventor's expectation, citing the 6 bar floor-pump test (§8).
  4. Route the questions (Q6).

### PF-18 — Durability, cold and evidence overstatement

- **Category:** support. **Severity:** medium. **Owner:** P4.
- **Concerns:** statements of effect and lifetime; Af; 15 FM-3 and FM-4.
- **Evidence:**
  - Testing stopped at 40 cycles against a target of "several thousand" (§9), and the result is censored.
  - No fatigue or cold-shock testing was done (bench data).
  - No lower bound on Af, and As, Ms and Mf are not given (01 Q13, Q28).
- **Risk:** An unsupported statement of lifetime or robustness to CO₂ in the Description becomes an admission against the patentee, or a credibility attack at the EPO when the effect is relied on.
- **Drafting response:**
  1. State the result as "no failure within 40 cycles in the test", against conventional cores that failed at cycles 12–18.
  2. Make no fatigue or CO₂ claim.
  3. Present Af below 5 °C as the prototype specification, chosen so that the ring is superelastic at riding temperatures.
  4. Describe 15's mitigations only if confirmed (PF-4).

### PF-19 — Routes that cannot be closed without new matter

- **Category:** design-around. **Severity:** medium. **Owner:** P4+P5.
- **Concerns:**
  - 11 DA-7 / R2 (over-travel uncovers a port; nothing deflects);
  - DA-23 / R3 as a stand-alone product (a rigid wiping land);
  - DA-24 (a ring deflected by pressure, without contact).
- **Evidence:** 11 finding 5; d2-attack §7 item 6.
- **Risk:** R2 is a cheap all-brass "self-purging" core, and no claim built on a deflectable ring element reaches it. Writing it into the Description without the inventor's conception risks inventorship and possession attacks (PF-4).
- **Drafting response:**
  1. **P4:** do not describe these routes.
  2. E10.3 (a fixed wiping land) may be described only as an addition to the recovering ring, never as the invention, and only if confirmed.
  3. **P5:** record the lost scope in the Prosecution Assessment inputs.
  4. Route to the inventor. If the inventor did conceive port purging, a genus "purge flow path opened by over-travel" becomes available (11 Q7).

### PF-20 — Thermal variant

- **Category:** novelty. **Severity:** low. **Owner:** P4+P5.
- **Concerns:** §6's two-way shape-memory purge (03 C32; `10` item 12; 11 DA-25).
- **Evidence:** 08 rates the inventive-step attack *moderate to strong* (US9982818B2 claim 5; US6393765B1 claim 1). The inventor doubts the variant and has no data.
- **Risk:** Little value, and an embodiment with no data that dilutes the Description.
- **Drafting response:** Describe it briefly as §6 does, as a separate alternative, and only if the inventor keeps it (01 Q21). No independent claim.

### PF-21 — Formal hygiene carried from the lessons

- **Category:** formal. **Severity:** low. **Owner:** P4+P5.
- **Concerns:** the support map, antecedent basis, numerals and terminology in the first drafts and revisions.
- **Evidence:** L2–L5. Earlier phases used "ring element" and "threshold arrangement" (03), which have since been replaced by the locked `deflectable ring element` and `threshold-setting arrangement` (08–10 new_terms).
- **Risk:** Loop-back cycles caused by avoidable support, antecedent and terminology findings.
- **Drafting response:**
  - Map every element of the state definitions (PF-2) and every genus word (PF-9) to a paragraph that uses the same words.
  - Use only the locked terms. Do not carry forward 03's superseded terms.
  - Run the antecedent, numeral and terms checks on every revision.

## Assumptions

A1. There are no Gate 1 answers, and Gate 2 was confirmed unattended. Every inventor question in 01, 03 and 11 is treated as unanswered. Blocking for P4 and P5.

A2. The Debate 1 attack on `09` is not embedded, so this report answers the attack in `08`, the design-around register in `11` and the Debate 2 attack. The d2-attack's statement that `09` does not exist is out of date: `09` and `10` are embedded and were used. Not blocking.

A3. `terminology/LOCKED.md` is not embedded. The locked terms are taken from their use in 08–10 and 11–15, and the locked `purge gap` definition from 11 DA-2's quotation of it. Not blocking; PF-3 depends on the quotation being accurate.

A4. ref-01 and ref-02 are fictional. They are treated as art for this matter (08 A2), and each conclusion that relies on them has a real counterpart (US4462449A, EP1137892A1). Not blocking.

A5. The jurisdictions are US, EPO and UK (USER.md). `matter.json` is not embedded. Not blocking.

A6. `07` is not embedded. Its chart rows are relied on only as 08–10 cite them. Not blocking.

A7. `02` is not embedded. Value-map ranks are cited through 08, 10 and 14. Not blocking.

## Open Questions

Q1. Where is the purge gap, how does it open against the interference fit, and what is the full air path into the inflatable chamber (01 Q1, Q2)? Without this the nucleus is not enabled (PF-1). Blocks P4, P5.

Q2. Does the air purge alone, the snap-back wipe alone, or both produce the effect (03 Q1)? This decides the relative weight of independent claims A and B (PF-6). Blocks P4, P5.

Q3. Does purging on every opening work, and has the inventor conceived any threshold-setting arrangement other than the two-stage return spring, including the ring's own stiffness (11 Q1, Q11; 01 Q6)? Blocks P4, P5 (PF-5).

Q4. Which of the genera in 11 and 12 that are marked "not conceived" are within the inventor's conception? In order of impact: purge shoulder genus; slotted or segmented ring; integral ring element; resilient metal or polymer; valve stem and Schrader formats; mechanical actuation of over-travel (11 Q3–Q6, Q9, Q13, Q14). Blocks P4, P5 (PF-4, PF-9).

Q5. Please supply the images of FIG-1 and FIG-2, and a normal-open-state sketch (01 Q22). Blocks P4, PACKAGE (PF-11).

Q6. What are the direction of poppet travel, the spring stage forces and engagement stroke, the over-travel stop, and the purge shoulder and wipe geometry (01 Q3, Q7, Q8, Q10, Q36)? Blocks P4 (PF-17).

Q7. Are Alternatives A and B within the invention, and what are the form of B's wiper ring and its wiping action (03 Q5, Q7)? Blocks P4, P5 (PF-16).

Q8. Has anyone shown, used, offered for sale or published the prototypes, the concept or the results before filing (01 Q34)? Grace periods differ between the US, the EPO and the UK. Blocks PACKAGE.

Q9. Should a professional search be commissioned, and should the full texts of US4462449A, US9982818B2, EP1137892A1 and US4719938A be read, and the fictional ref-01 and ref-02 rebased onto real art (08 Q1–Q3)? Blocks P5, PACKAGE (PF-12, PF-13).

Q10. May the intermediate and preferred ranges proposed in `13` be used, and what is the basis of each §4 range (01 Q15)? Blocks P4, P5 (PF-4, PF-14).

Q11. For the runner: should the locked definition of `purge gap` be amended to the functional definition in PF-1, step 3? Blocks P4, P5 (PF-3).

```json
{
  "prompt": "x-predraft-risk",
  "status": "partial",
  "findings": [
    {"id": "PF-1", "category": "enablement", "severity": "critical", "title": "Purge gap location and opening are self-contradictory", "concerns": "N0(d), C6, C7; 09 row 2; 10 items 1-3; purge-state description", "evidence": "§2 'stem bore' and 'flexes radially outward' vs §3(6) outer surface/core body bore vs §7 0.03 mm interference fit; 01 (m), Q1, Q2; 03 N0 enablement caution; 08 Q4; 12 E7.1; d2-attack R1", "risk": "Insufficiency/written description (EPC Art. 83; 35 U.S.C. 112(a); UK s.14(3)) and clarity attack on every claim reciting the purge gap; if N0(d) cannot be enabled N0 falls back towards ref-02 claim 4 with [0019]", "drafting_response": "Hold the purge-state mechanism until 01 Q1/Q2 are answered; if unanswered, describe only what is consistent and do not choose between §2 and §3(6) or adopt 12 E6.2/E7.x; once answered, describe surface pair, direction and full air path in words and reconcile the fit; independent claims define the purge gap by function and state only (bounded in part by the deflectable ring element, closed in closed and normal-open states, opened by the deflection), no surface pair or direction; keep independent claim B (PF-6) free of N0(d)", "owner": "P4+P5"},
    {"id": "PF-2", "category": "novelty", "severity": "critical", "title": "Naive 'deflectable seat opens an extra path' claim is anticipated", "concerns": "Independent valve-core claim (value map rank 1, N0); state definitions", "evidence": "ref-02 claim 4, [0019], [0020]; US4462449A claim 1; EP1137892A1 claims 1(e), 8; 08 'What the attack shows' 1-2; 09 rows 1-2", "risk": "Claim letting the purge gap read on the main passage, or omitting the normal-stroke/over-travel sequence, lacks novelty in US, EPO and UK", "drafting_response": "Claim 1 carries three relationships in positive wording (L1): normal stroke with main passage open and purge shoulder spaced from the deflectable ring element; over-travel above an over-travel threshold higher than the crack pressure, purge shoulder deflecting the ring element only then; purge gap separate from the main passage, closed in closed and normal-open states. P4 defines closed, normal-open and purge states in one paragraph in the claim's words and states that main passage and purge gap are distinct paths", "owner": "P4+P5"},
    {"id": "PF-3", "category": "design-around", "severity": "high", "title": "Locked 'purge gap' definition fixes the contradicted species", "concerns": "LOCKED.md purge gap entry; every use of the term", "evidence": "11 DA-2 quotes the lock as 'an annular radial clearance between the seat ring outer surface and the core body bore, §3(6)'; 11 DA-3; d2-attack R1, R8; 12 §7 genus", "risk": "A definition in the Description limits every claim to a contradicted and freely avoidable species", "drafting_response": "Do not reproduce the locked species definition as the meaning of the term; define purge gap functionally; present the §3(6) location only as the prototype's once confirmed; describe slit/aperture/finger openings only if confirmed (11 Q3); runner to amend the lock", "owner": "P4+P5"},
    {"id": "PF-4", "category": "support", "severity": "high", "title": "Unattended Gate 2: unconceived entries and interpolated ranges", "concerns": "CONFIRMED.md: 12 'not conceived' entries, 11 'needs inventor confirmation' genera, 13 proposed intermediate/preferred ranges, 15 candidate mitigations", "evidence": "CONFIRMED.md header (auto-unattended); d2-attack §7 item 6, A3; 13 method note; non-negotiable 4; USER.md directives", "risk": "Inventorship/oath and lack-of-possession attacks; invented preferred sub-ranges with no basis (asymmetric 0.08-0.16 and 0.4-0.65); omission forfeits design-around cover that cannot be added later", "drafting_response": "P4 writes only disclosed content as the inventor's; hold 'not conceived' entries pending the top-ten inventor form (L8) and list held passages in the package cover note; use only §4 broad ranges and prototype values unless the inventor adopts 13's proposals; P5 relies on no held passage for support", "owner": "P4+P5"},
    {"id": "PF-5", "category": "design-around", "severity": "high", "title": "Novelty-carrying threshold is the cheapest undetectable design-around", "concerns": "N0(b), C3, C17; threshold-setting arrangement; 11 DA-1, DA-11; d2-attack R4, R12", "evidence": "08 N0 novelty weak only with the sequence; 11 DA-1; 12 E2.3; d2-attack R4 (bench measurement needed); 03 Q3, 11 Q1 unanswered", "risk": "Dropping the threshold returns claim 1 to ref-02; keeping it leaves an escape that is hard to prove; tying it to the spring loses DA-11; possible 35 U.S.C. 112(f) construction with one disclosed structure", "drafting_response": "Keep the threshold as a relationship in the main claim; cover DA-1 with independent claim B (PF-6) without a second threshold if the inventor confirms; disclose several threshold-setting structures once confirmed, else P5 treats it as single-species; add teardown-visible dependents (second spring stage, lost-motion clearance, purge-shoulder axial clearance)", "owner": "P4+P5"},
    {"id": "PF-6", "category": "support", "severity": "high", "title": "Effect not attributed to purge or wipe; family needs a second nucleus", "concerns": "N0(d) vs N1; 03 wipe-based alternative nucleus; 11 DA-10; d2-attack R7, R17", "evidence": "01 (l), Q24; 03 Q1, A2; 08 wipe-based nucleus weak novelty, moderate inventive step; 09 row 3", "risk": "Air-purge-only claims escaped by a sealed periphery that no teardown shows; asserting either action alone suffices is an untested fact", "drafting_response": "P4 describes cleaning as air purge, snap-back wipe or both, wipe described independently of flow, bench result stated as outcome not attribution; P5 files independent claim A (PF-2 with purge gap) and claim B (over-travel sequence plus ring element held in the body whose shape recovery moves it across a poppet surface; no flow), with the recovery-driven movement answering kinematic inversion", "owner": "P4+P5"},
    {"id": "PF-7", "category": "novelty", "severity": "high", "title": "Inventive-step mosaic; effect evidence not against closest art", "concerns": "N0 inventive step; problem and effect passages; Examples", "evidence": "08: ref-02/US4462449A + EP1137892A1 + CN215861914U, moderate; EP1137892A1 threshold is chamber-side and outward; 08 Q6", "risk": "EPO objective problem framed as 'alternative valve' and the combination found obvious; US mosaic of known elements", "drafting_response": "State the §1 problem; tie each relationship to its effect (conventional behaviour up to threshold; purge in inflation direction into the inflatable chamber; recovery of the fixed ring drives the wipe); report the bench test as an Example with its limits; no comparison with a ref-02-type seat without data; route 08 Q6 for post-filing evidence", "owner": "P4"},
    {"id": "PF-8", "category": "design-around", "severity": "high", "title": "Wipe wording invites 'no snap' and 'rubber disclaimer' arguments", "concerns": "snap-back wipe; §2 rubber comparison; §6 weaker PEEK wipe; d2-attack R14, R15; 11 DA-15; 14 [a]", "evidence": "§2 'fast and stiff', latex embeds in rubber; §6 'wipe is weaker'; no lower bound on wipe force or speed", "risk": "Snap-back wipe indefinite or unmet against polymer rings; §2 read as a disclaimer", "drafting_response": "Define the wipe as movement of the recovering deflectable ring element across a surface of the poppet, no speed or force qualifier; superelastic recovery presented as preferred; recast §2 as a disadvantage of soft seats deforming under the sealing face; PEEK wipe within the definition; no 'snap' or 'fast/stiff' in claims; no elastomer embodiment unless conceived", "owner": "P4+P5"},
    {"id": "PF-9", "category": "design-around", "severity": "high", "title": "Nucleus components defined by prototype species", "concerns": "Purge shoulder (DA-4, R9); separate vs integral ring (DA-5, R10); continuous vs slotted, metal or polymer (DA-3, DA-13, DA-14, R8, R13); valve format (DA-6, R6); mechanical over-travel (DA-9, R5)", "evidence": "11 findings 2-4; 12 §§3, 4, 12, 16; d2-attack §7 item 2 and ranking", "risk": "Each prototype word in claim 1 is a cheap escape; R6 takes the OEM channel", "drafting_response": "P5 uses genus words in independent claims (purge shoulder of the poppet, deflectable ring element, valve body; no threaded/Presta/material) and adds an inflation-valve independent claim without reciting the cause of over-travel; P4 describes broader species only once confirmed, and otherwise states non-limitation without listing unconceived species", "owner": "P4+P5"},
    {"id": "PF-10", "category": "design-around", "severity": "high", "title": "Behaviour-only limitations and divided infringement", "concerns": "Threshold, purge flow and wipe provable only by bench test (R4, R7, R14); pump head produces over-travel (R5)", "evidence": "d2-attack §7 item 3; 11 finding 6; 10 item 2", "risk": "Infringement that cannot be proven, or is split between valve maker, pump maker and rider", "drafting_response": "P5 pairs functional claims with teardown-visible dependents (second spring stage, lost-motion clearance, ring held in the body with the purge shoulder axially spaced at rest, prototype geometry after PF-1); valve-core-plus-depressing-head claim only if 11 Q9 confirmed; method only as dependent or use claim; P4 describes the structures behind each behaviour", "owner": "P4+P5"},
    {"id": "PF-11", "category": "formal", "severity": "high", "title": "Figure images absent", "concerns": "Figure descriptions; numerals 10-70; FIG-2 purge state; orientation words", "evidence": "01 Q22; 01 A4, A5; L4", "risk": "Drawings needed for understanding and not addable later without new matter; invented figure detail; wrong orientation propagating into claims", "drafting_response": "Describe figures only as far as the README states; register numerals 10-70; use 'supply side' and 'chamber side' instead of upper/below until 01 Q3 is answered; package flags FIG-1, FIG-2 and a normal-open-state figure as needed before filing", "owner": "P4"},
    {"id": "PF-12", "category": "novelty", "severity": "high", "title": "Seat ring component claim exposed to US9982818B2", "concerns": "Value map rank 2; 10 item 6; d2-attack R18", "evidence": "08: strong against material plus wave wall; US9982818B2 abstract, claims 3, 4, 9; 'for a valve core' read as suitable for; 08 Q3", "risk": "Component claim loses the valve context and is anticipated or obvious", "drafting_response": "P5 claims the ring only with a sealing edge, a convoluted wall converting axial load on the sealing edge into radial deflection, and the §4 broad dimensions; consider a kit claim carrying the PF-2 relationship (11 Q19); P4 describes the axial-to-radial function and dimensions in words; assessment marks the claim as pending the full text", "owner": "P4+P5"},
    {"id": "PF-13", "category": "novelty", "severity": "high", "title": "Thin, partly fictional reference set", "concerns": "Every novelty and inventive-step position", "evidence": "08 Q1-Q3: 15 machine-retrieved extracts, English only, no NPL, no CPC walk; ref-01, ref-02 fictional; full texts unread; L6", "risk": "Weak ratings are weak against this pile only; unseen art may remove one of the three relationships", "drafting_response": "P4 describes every disclosed rung with its effect for amendment basis; P5 structures dependents so each relationship and the wipe can be promoted alone; package states the coverage limit and recommends a professional search; Background goes no further than §1", "owner": "P4+P5"},
    {"id": "PF-14", "category": "design-around", "severity": "high", "title": "Numbers, materials and field of use in independent claims", "concerns": "N4, N6, PEEK, Af, sealant, tubeless, Presta-pattern; d2-attack R11, R13, R19; 11 DA-16", "evidence": "§4 'believed'; 08 N6 strong as routine optimisation; 14 [g]; R19 'tubes only' label", "risk": "Whole patent avoided by a tolerance, a material or a label", "drafting_response": "Keep ranges, materials, Af, PEEK, sealant, tubeless and Presta-pattern out of independent apparatus claims; lead with relationships; sealant only in dependent, use and chamber claims; Af dependent conditioned on the superelastic species", "owner": "P5"},
    {"id": "PF-15", "category": "novelty", "severity": "medium", "title": "Ladder increments and manufacturing method carry no inventive step", "concerns": "Dependent ladder N2, N4-N7; value map rank 4", "evidence": "08: N2 in ref-02 claim 1; N4 in US6393765B1, US9982818B2; N5 standard means; N6, N7 routine/CGK; method moderate to strong", "risk": "Prosecution effort on fallbacks that cannot stand alone", "drafting_response": "Keep as dependents for scope and amendment; no separate method family without a process effect or windows (01 Q32); if a relationship falls, promote the snap-back wipe (N1) before the material (N4)", "owner": "P5"},
    {"id": "PF-16", "category": "support", "severity": "medium", "title": "Alternative B: thin support and inventive-step exposure", "concerns": "E-III; 11 DA-17; 10 item 4; d2-attack R16, R17", "evidence": "§6 one paragraph, no geometry (03 Q7); 08 ref-01 + US4719938A moderate", "risk": "One-sentence written description; E-III claimed alone reads as a scraper", "drafting_response": "P4 describes E-III no further than §6 until 03 Q5, Q7 are answered; P5 covers it through the deflectable ring element genus, with no separate independent claim unless it carries the over-travel-only purge gap and threshold", "owner": "P4+P5"},
    {"id": "PF-17", "category": "enablement", "severity": "medium", "title": "Undisclosed orientation, spring stages, stop and geometry", "concerns": "01 Q3, Q5, Q7, Q8, Q9, Q10, Q36; 15 FM-9", "evidence": "01 (h) values not given; 13 Table 4", "risk": "Missing support for dependent rungs; unsupported 'every floor pump reaches'", "drafting_response": "Describe only what is given; add no stop, rates or angles; qualify 'every floor pump' as the inventor's expectation, citing the 6 bar floor-pump test; route the questions", "owner": "P4"},
    {"id": "PF-18", "category": "support", "severity": "medium", "title": "Durability, cold and evidence overstatement", "concerns": "Effect and lifetime statements; Af; 15 FM-3, FM-4", "evidence": "40 cycles, censored, against a 'several thousand' target (§9); no fatigue or cold-shock test; Af upper bound only (01 Q13, Q28)", "risk": "Unsupported robustness statements become admissions or credibility attacks", "drafting_response": "State 'no failure within 40 cycles in the test' against conventional failures at cycles 12-18; no fatigue or CO2 statements; Af below 5 °C as the prototype specification for superelasticity at riding temperatures; mitigations only if confirmed", "owner": "P4"},
    {"id": "PF-19", "category": "design-around", "severity": "medium", "title": "Routes that cannot be closed without new matter", "concerns": "11 DA-7/R2 port purge; DA-23/R3 stand-alone rigid land; DA-24 pressure-deflected ring", "evidence": "11 finding 5; d2-attack §7 item 6", "risk": "Cheap all-brass self-purging core outside every ring-based claim; writing it in risks inventorship and possession attacks", "drafting_response": "Do not describe these routes; E10.3 only as an addition to the recovering ring and only if confirmed; P5 records the lost scope for the Prosecution Assessment; route 11 Q7 to the inventor", "owner": "P4+P5"},
    {"id": "PF-20", "category": "novelty", "severity": "low", "title": "Thermal variant", "concerns": "§6 two-way shape-memory purge; 03 C32; 10 item 12; 11 DA-25", "evidence": "08 moderate to strong (US9982818B2 claim 5; US6393765B1 claim 1); inventor doubt, no data", "risk": "Low value; dilutes the Description", "drafting_response": "Describe briefly as §6 does, only if the inventor keeps it (01 Q21); no independent claim", "owner": "P4+P5"},
    {"id": "PF-21", "category": "formal", "severity": "low", "title": "Formal hygiene from the lessons", "concerns": "Support map, antecedents, numerals, terms", "evidence": "L2-L5; 03's 'ring element' and 'threshold arrangement' superseded by the locked 'deflectable ring element' and 'threshold-setting arrangement'", "risk": "Avoidable loop-back cycles", "drafting_response": "Map state definitions and genus words to paragraphs in the same words; use locked terms only; run the antecedent, numeral and terms checks on every revision", "owner": "P4+P5"}
  ],
  "assumptions": [
    {"id": "A1", "text": "No Gate 1 answers; Gate 2 confirmed unattended; all inventor questions in 01, 03 and 11 treated as unanswered.", "blocking": true},
    {"id": "A2", "text": "Debate 1 attack on 09 not embedded; report answers 08, 11 and the Debate 2 attack; d2-attack's statement that 09 does not exist is out of date.", "blocking": false},
    {"id": "A3", "text": "LOCKED.md not embedded; locked terms taken from 08-10 and 11-15 usage, and the purge gap definition from 11 DA-2's quotation.", "blocking": false},
    {"id": "A4", "text": "ref-01 and ref-02 are fictional, treated as art per 08 A2, each with a real counterpart.", "blocking": false},
    {"id": "A5", "text": "Jurisdictions US, EPO and UK per USER.md; matter.json not embedded.", "blocking": false},
    {"id": "A6", "text": "07 not embedded; chart rows relied on only as 08-10 cite them.", "blocking": false},
    {"id": "A7", "text": "02 not embedded; value-map ranks cited through 08, 10 and 14.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "Purge gap location, opening against the interference fit, and full air path (01 Q1, Q2).", "blocks": ["P4", "P5"]},
    {"id": "Q2", "text": "Air purge alone, snap-back wipe alone, or both (03 Q1)?", "blocks": ["P4", "P5"]},
    {"id": "Q3", "text": "Does purging on every opening work; any threshold-setting arrangement other than the two-stage return spring, including ring stiffness (11 Q1, Q11; 01 Q6)?", "blocks": ["P4", "P5"]},
    {"id": "Q4", "text": "Which 'not conceived' genera in 11 and 12 are within the inventor's conception (purge shoulder genus, slotted/segmented ring, integral ring element, resilient metal or polymer, stem and Schrader formats, mechanical over-travel)?", "blocks": ["P4", "P5"]},
    {"id": "Q5", "text": "Supply FIG-1 and FIG-2 images and a normal-open-state sketch (01 Q22).", "blocks": ["P4", "PACKAGE"]},
    {"id": "Q6", "text": "Direction of travel, spring stage forces and engagement stroke, over-travel stop, purge shoulder and wipe geometry (01 Q3, Q7, Q8, Q10, Q36).", "blocks": ["P4"]},
    {"id": "Q7", "text": "Are Alternatives A and B within the invention; form and wiping action of B's wiper ring (03 Q5, Q7)?", "blocks": ["P4", "P5"]},
    {"id": "Q8", "text": "Any public showing, use, offer for sale or publication before filing (01 Q34)?", "blocks": ["PACKAGE"]},
    {"id": "Q9", "text": "Commission a professional search, read full texts of US4462449A, US9982818B2, EP1137892A1 and US4719938A, and rebase fictional ref-01/ref-02 (08 Q1-Q3)?", "blocks": ["P5", "PACKAGE"]},
    {"id": "Q10", "text": "May 13's proposed intermediate and preferred ranges be used; basis of each §4 range (01 Q15)?", "blocks": ["P4", "P5"]},
    {"id": "Q11", "text": "Runner: amend the locked purge gap definition to the functional definition in PF-1?", "blocks": ["P4", "P5"]}
  ]
}
```
