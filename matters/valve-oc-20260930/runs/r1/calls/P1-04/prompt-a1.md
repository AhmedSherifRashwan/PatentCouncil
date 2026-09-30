# Patent Council · matter `valve-oc-20260930` · run `r1` · step `P1-04` · profile full

You are the **Invention Analyst**. Follow your AGENTS.md. This message is the whole brief: what to do, the prompts to execute, every input (embedded below, so do not re-read those files), and the exact files to write.

## What to do

Run Prompt 04. It runs in parallel with its siblings: use their outputs if they are embedded.

**Time budget:** about 6 minutes. The whole matter is planned to finish end to end in two hours. Be complete, but write each deliverable once: no drafts, no repetition, no padding.

## Prompt 04 — Terminology and ontology  (kind `analysis`)

**Write your reply to:** `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P1/04.md`

*Prevent accidental narrowing and inconsistent language.*

Create a terminology table for the invention. For every important component or action provide: preferred neutral term, possible synonyms, broader genus terms, narrower species terms, functional descriptions and terms to avoid because they may unnecessarily narrow scope. Identify terms that require an express definition in the specification. This table becomes the locked terminology reference for every later drafting prompt (see R2).

**How to work.** This table is copied as-is into `terminology/LOCKED.md` at Gate 1 and parsed by machine, so the format is mandatory: under `### Terminology Table` emit exactly one markdown table with these seven columns in this order and these exact header spellings: `Preferred term | Synonyms | Broader (genus) | Narrower (species) | Functional description | Terms to avoid | Needs definition`. One row per component or action; separate multiple synonyms, genus, species or avoid-terms with semicolons; `Needs definition` is `yes` or `no`. Cover every component, step and parameter named in `01` and every feature in the `03` ladder, and use the same preferred term for each that `01` and `03` used unless you deliberately rename it, in which case record the rename in `new_terms`. Put any explanatory notes after the table, not inside it. Reply exactly in the drafting output contract: `## Deliverable` (with the H3 sections named above), `## Rationale`, `## Assumptions`, `## Open Questions`, then one final fenced `json` envelope. No preamble before `## Deliverable`; nothing after the envelope. Reuse locked preferred terms verbatim; declare any other term in `new_terms` with a reason.

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

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/intake/disclosure.md`

```markdown
<!-- FICTIONAL example for testing; not a real invention -->

# Invention disclosure — self-purging bicycle tube valve with shape-memory seat

Inventor: J. Okafor (fictional). Date of disclosure: 2026-08-30. Status: bench prototype, three units built.

## 1. The problem

Bicycle inner tubes and tubeless set-ups are increasingly run with liquid sealant — typically a latex emulsion with ammonia and suspended particles — injected through the valve stem. Every time the tyre is inflated, a small quantity of sealant is drawn up into the valve core bore by the pressure surge and by capillary action along the poppet stem. Between rides the film dries. After ten to twenty inflation cycles the core seat is coated with cured latex and the valve either leaks slowly (the poppet no longer seats) or blocks entirely (the pump cannot open it). The standard remedy is to unscrew the core with a tool, scrape it or replace it, and re-inject sealant. Riders do this constantly, and cores are sold in multipacks for this reason.

Existing attempts to fix this either coat the poppet with a low-adhesion polymer, enlarge the bore, or fit a removable insert. None of them removes the film once it has formed; they only slow its build-up.

## 2. The concept

The valve core carries a seat ring made of a superelastic nickel–titanium (NiTi) alloy rather than a rigid brass seat or a rubber grommet. The seat ring has a thin, sinuous wall. During normal inflation the poppet lifts off the seat by its usual stroke. When the pump head applies a pressure differential above a threshold — which every floor pump reaches — the poppet travels beyond its normal stroke (we call this "over-travel"). The over-travel drives a shoulder on the poppet against the seat ring, which flexes radially outward and opens a secondary annular gap between the ring and the stem bore. Air at pump pressure then rushes through this purge gap, across the exact surfaces on which sealant accumulates, and blows the sealant film down into the tube where it belongs.

When the pump head is removed the differential collapses, the poppet returns, and the seat ring recovers its shape. Because the recovery of a superelastic ring is fast and stiff (it is not a slow elastomer creep), the recovering ring wipes across the poppet face with a snap. That wiping action shears off partially cured latex that a rubber seat would simply embed itself in. So the valve cleans itself twice per inflation: once by air flow through the purge gap, and once mechanically by the snap-back wipe.

The technical effect we observed is that the valve keeps sealing and keeps opening after far more sealant-loaded inflation cycles than a conventional core, with no tool and no rider action.

## 3. Components

1. Valve stem (10) — conventional Presta-pattern brass stem, 6 mm outer diameter, with a threaded bore to accept the core.
2. Core body (20) — turned brass or stainless steel, threaded to the stem, carrying the seat ring and guiding the poppet.
3. Seat ring (30) — the NiTi element. A short tube with a wall that is not straight in section but has one or two shallow convolutions (a wave), so that axial load on its upper edge translates into radial expansion. It is pressed into the core body with a light interference fit and located against a shoulder.
4. Poppet (40) — the moving valve member with a conical sealing face (42) that seats on the upper edge of the seat ring, and a purge shoulder (44) below the sealing face that only contacts the ring during over-travel.
5. Return spring (50) — a light compression spring under the poppet, as in a conventional core, but with a two-rate characteristic: a soft first stage for normal opening and a stiffer second stage that the pump differential must overcome to reach over-travel.
6. Purge gap (60) — the annular clearance between the seat ring outer surface and the core body bore that opens when the ring expands; closed at rest.
7. Lock nut (70) — conventional, for manual closing of the poppet for storage and transport.

## 4. Dimensions and ranges (prototype values, with the ranges we believe would work)

- Seat ring inner diameter: 2.3 mm on the prototype (range 2.0–2.6 mm).
- Seat ring wall thickness: 0.20 mm (range 0.15–0.30 mm).
- Seat ring free length: 3.0 mm (range 2.5–4.0 mm).
- Convolution amplitude: 0.12 mm (range 0.08–0.20 mm).
- Normal poppet stroke: 0.6 mm; over-travel beyond that: 0.5 mm (range 0.4–0.9 mm).
- Purge gap when fully open: 0.15 mm radial (range 0.10–0.25 mm).
- Crack pressure of the poppet (first spring stage): 1.0 bar (range 0.8–1.5 bar).
- Pressure differential to reach over-travel (second spring stage): 3.5 bar on the prototype (range 2.5–5.0 bar).
- NiTi austenite finish temperature (Af): specified below 5 °C so the ring is superelastic at all riding temperatures.

## 5. Materials

- Seat ring: superelastic NiTi, nominally 55.8 wt% Ni, from drawn tube, shape-set and electropolished (see manufacturing note).
- Core body and stem: free-machining brass CW614N; a stainless 303 variant was also machined for corrosion resistance with ammonia-bearing sealant.
- Poppet: brass with a hard-anodised aluminium alternative considered for the sealing face; the prototype is brass.
- Spring: stainless music wire. Nothing in the concept depends on the spring material.

## 6. Alternatives we have considered

Alternative A — polymer seat ring. A PEEK ring with the same convoluted wall would give some radial compliance and would be cheaper, but its recovery is slower and it has a lower snap-back force, so the wiping effect is weaker. We have not built this; it is a considered option for a lower-cost product line.

Alternative B — two-piece seat. A rigid brass seat for sealing plus a separate thin stainless spring wiper ring below it that is deflected outward by the purge shoulder. This separates the sealing function from the purge/wipe function and might be easier to manufacture, at the cost of one more part and more axial length. Not built.

A thermal variant was also discussed: a NiTi ring trained with a two-way shape memory so that warming it by hand (Af around 35–40 °C) opens the purge gap for a manual purge without a pump. We are not sure this is worth pursuing and have no data.

## 7. Manufacturing note

Seat rings were laser-cut from NiTi tube (2.7 mm OD, 0.20 mm wall) to the convoluted profile on a mandrel, shape-set at 500 °C for 10 minutes in a fixture holding the wave geometry, water-quenched, then electropolished to remove the oxide and the heat-affected edge. Rings were pressed into the core body with an interference of approximately 0.03 mm on diameter and seated against the internal shoulder. Ordinary turning for the body and poppet; no other special process.

## 8. Test result

Bench test, 2026-08-12 to 2026-08-20. Three prototype cores and three conventional cores (same manufacturer's standard Presta core) were fitted to identical 700×28 tubes each charged with 60 ml of latex sealant. Each tube was cycled: inflate to 6 bar with a floor pump, hold 24 hours at 22 °C, deflate fully through the valve, repeat. Failure was defined as either a leak-down of more than 0.5 bar in 24 hours or the pump failing to open the valve within 5 seconds of engagement.

All three conventional cores failed between cycle 12 and cycle 18. All three prototype cores completed 40 cycles without failure; the mean inflation time at cycle 40 was within 15 % of cycle 1. The full table is in `data/bench-test.md`. On disassembly at cycle 40 the prototype seat rings showed a thin cured film on the outside of the ring (in the purge gap region) but a clean sealing edge and a clean poppet face.

## 9. Known unknowns

1. Fatigue life of the seat ring. We have 40 over-travel cycles per ring. A commercial valve should survive several thousand. NiTi in superelastic cycling can accumulate residual strain; we have no data on the ring's behaviour beyond 40 cycles and do not know whether the purge gap stays closed at rest after long service.
2. CO2 inflation. A CO2 cartridge inflator chills the valve to well below 0 °C for a few seconds. If the ring's temperature drops below its martensite start temperature it will lose its superelastic recovery temporarily. We do not know whether the specified Af below 5 °C is a sufficient margin, or whether a cold-shocked ring stays deformed until it warms up.

We would also like to know whether the effect holds with ammonia-free sealants, which cure differently, but we have not tested any.
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

## Inputs that do not exist yet (work without them; do not wait)

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P1/02.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P1/03.md`

## Files to write

Write each of these with your Write tool, at exactly this path, one file per call (the folders exist). Write nothing outside the run folder `{R}`. Do not run the checks yourself: the runner runs them and will tell you if anything fails.

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P1/04.md`

When every file is written, reply with one line per file (path and a few words on what it holds) and anything the runner must route: open questions, disclosure requests, open disagreements, narrowing suggested. Nothing else.
