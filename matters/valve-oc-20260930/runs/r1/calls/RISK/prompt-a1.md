# Patent Council · matter `valve-oc-20260930` · run `r1` · step `RISK` · profile full

You are the **Prior-Art Analyst**. Follow your AGENTS.md. This message is the whole brief: what to do, the prompts to execute, every input (embedded below, so do not re-read those files), and the exact files to write.

## What to do

Write `risk/pre-drafting-findings.md` from Phases 1–3, the attacks (whatever is embedded) and the lessons file. Every critical and high risk names its owner (P4, P5 or both) and the drafting response.

**Time budget:** about 8 minutes. The whole matter is planned to finish end to end in two hours. Be complete, but write each deliverable once: no drafts, no repetition, no padding.

## Inputs (embedded)

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

## Files to write

Write each of these with your Write tool, at exactly this path, one file per call (the folders exist). Write nothing outside the run folder `{R}`. Do not run the checks yourself: the runner runs them and will tell you if anything fails.

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/risk/pre-drafting-findings.md`

When every file is written, reply with one line per file (path and a few words on what it holds) and anything the runner must route: open questions, disclosure requests, open disagreements, narrowing suggested. Nothing else.
