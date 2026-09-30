# Patent Council · matter `valve-oc-20260930` · run `r1` · step `P4-part3` · profile full

You are the **Specification Drafter**. Follow your AGENTS.md. This message is the whole brief: what to do, the prompts to execute, every input (embedded below, so do not re-read those files), and the exact files to write.

## What to do

Draft **Part 3 of 5** of the detailed description: exactly the sections Prompt 16's blueprint assigns to Part 3. Rules: one `### Description` wrapper; section titles as `####` headings (never `##` or `###` inside); no paragraph numbers (the stitcher numbers them); reference numerals exactly as in the registry; locked terms verbatim. Answer the risks and attacks that fall in your sections. Do not repeat material that belongs to another part. Depth matters: every claim family must find its support here.

**Time budget:** about 12 minutes. The whole matter is planned to finish end to end in two hours. Be complete, but write each deliverable once: no drafts, no repetition, no padding.

## Prompt x-p4-compose-description — Compose the Description  (kind `compose`)

**Write your reply to:** `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P4/parts/part3.md`

*Runner template: the playbook has no prompt that emits the finished Description prose. This step assembles it from the Phase 4 outputs.*

Assemble the finished patent Description from the Phase 4 outputs embedded below: follow the section order and section ids of the specification blueprint (Prompt 16); honour the enablement audit (Prompt 17) by describing only what the audit found enabled and by including the additional disclosure it recommended where that disclosure is present in the confirmed embodiments; incorporate the worked examples (Prompt 18) with their actual / prophetic labelling intact; include the definitions (Prompt 19) as written; write the brief description of the drawings from the figure plan (Prompt 20) and the figure instructions (Prompt 20a); and refer to every component by its locked preferred term followed by its reference numeral from the registry on first mention in each paragraph. Produce, in order: title; technical field; background; summary; brief description of the drawings; detailed description (embodiments, definitions, examples, manufacturing/assembly, operation/use, alternatives and combinations, ranges, data/results where actual data exists); and a closing paragraph on the scope of alternatives. Number every paragraph of the body consecutively in the form [0001], [0002] ... starting at the technical field.

**How to work.** This is composition, not invention: every technical statement in the Description must already appear in one of the embedded Phase 4 outputs or in `CONFIRMED.md`; add no new technical matter, no new ranges, no new examples and no results. Where the inputs disagree, the enablement audit governs breadth, the definitions govern meaning, the registry governs numerals, and the locked terminology governs names - record each such resolution in `## Rationale`. The runner writes the `### Description` section verbatim to `description.md`, which the claims drafter and later the blind reviewer will read, so that section must contain only the Description text itself: no editorial notes, no bracketed placeholders, no headings other than the specification's own section headings, and paragraph numbers on every body paragraph. Anything the blueprint calls for that the inputs do not supply is omitted from the text and listed in `disclosure_requests` (for the human or the next round), never filled in. Reply exactly in the drafting output contract: `## Deliverable` (with the H3 sections named above), `## Rationale`, `## Assumptions`, `## Open Questions`, then one final fenced `json` envelope. No preamble before `## Deliverable`; nothing after the envelope. Reuse locked preferred terms verbatim; declare any other term in `new_terms` with a reason.

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

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P4/18.md`

````markdown
## Deliverable

### Worked Examples

Three principal embodiments are drafted below. Each is grounded directly in the intake disclosure (`intake/disclosure.md` §1–§9), which Method step 1 of this role permits regardless of the Gate 2 status question recorded in `## Rationale`: the superelastic seat ring embodiment (§2, §3–§5, §7), the PEEK seat ring embodiment (§6, Alternative A), and the fixed-seat-and-wiper-ring embodiment (§6, Alternative B). Reference numerals follow §3 and `terminology/LOCKED.md`: valve stem (10), core body (20), seat ring (30), poppet (40), sealing face (42), purge shoulder (44), return spring (50), purge gap (60), lock nut (70).

#### Actual examples

**Example 1 — superelastic seat ring embodiment (prototype cores P-1, P-2, P-3)**

*Components.* A Presta-pattern valve stem (10); a core body (20) threaded into the stem bore of the valve stem, carrying an internal shoulder and guiding the poppet; a seat ring (30) formed as a deflectable ring element with a convoluted wall, pressed against the internal shoulder; a poppet (40) with a conical sealing face (42) that rests on the sealing edge of the seat ring in the closed state, and a purge shoulder (44) on the chamber side of the sealing face; a two-rate return spring (50), of which the first spring stage biases the poppet through the normal stroke and the second spring stage sets the over-travel threshold; a lock nut (70).

*Materials.* Seat ring (30): superelastic alloy, NiTi of nominal composition 55.8 wt% Ni, with an austenite finish temperature specified below 5 °C (disclosure §5). Core body (20) and valve stem (10): free-machining brass CW614N. Poppet (40): brass. Return spring (50): stainless steel music wire (disclosure §5).

*Dimensions/ranges.* Valve stem outer diameter 6 mm (Presta-pattern, conventional). Seat ring: inner diameter 2.3 mm, wall thickness 0.20 mm, free length 3.0 mm, convolution amplitude 0.12 mm, formed from tube stock of 2.7 mm outer diameter and 0.20 mm wall. Interference fit of the seat ring in the core body approximately 0.03 mm on diameter. Crack pressure 1.0 bar; over-travel threshold 3.5 bar; normal stroke 0.6 mm; over-travel distance 0.5 mm; purge gap opening 0.15 mm radial. All are the disclosure's stated prototype (representative) values; the disclosure separately gives broader "believed" ranges for each (§4) that were not independently built or tested (support: `intake/disclosure.md` §4). The over-travel distance and purge gap opening were not independently measured in the bench test; they are the disclosure's stated values, corroborated only indirectly by an audible snap on pump-head removal (support: `intake/data/bench-test.md`).

*Fabrication/assembly.* (1) Laser-cut the NiTi tube stock (2.7 mm outer diameter, 0.20 mm wall) to the convoluted profile on a mandrel. (2) Shape-set the ring at 500 °C for 10 minutes in a fixture holding the convoluted wall geometry, then water-quench. (3) Electropolish the ring to remove surface oxide and the heat-affected edge. (4) Press the seat ring into the core body with approximately 0.03 mm interference on diameter, seated against the internal shoulder. (5) Turn the core body and poppet by ordinary machining, with no other special process. (6) Assemble the poppet, return spring and lock nut into the core body, and thread the core body into the valve stem. (Support: `intake/disclosure.md` §7.)

*Operating sequence.* (S1) At or above the crack pressure (1.0 bar), the poppet lifts off the sealing edge of the seat ring by the normal stroke (0.6 mm), resisted only by the first spring stage. (S2) When the pressure differential exceeds the over-travel threshold (3.5 bar), the poppet moves beyond the normal stroke (over-travel, 0.5 mm) against the second spring stage. (S3) The purge shoulder bears on the seat ring; the seat ring undergoes radial deflection, described in the disclosure as outward; the purge gap opens (0.15 mm radial). (S4) Inflation air flows through the purge gap, described in the disclosure as across the surfaces on which sealant film accumulates, into the inflatable chamber, alongside flow through the main passage (air purge). (S5) On removal of the inflation device, the pressure differential collapses, the poppet returns, the seat ring undergoes shape recovery, producing the snap-back wipe across the poppet, and the purge gap closes. (Support: `intake/disclosure.md` §2; steps S1–S5 correspond to `runs/r1/P1/01.md` §(d).) **Flag:** the disclosure states the purge gap's location two ways — between the seat ring and the stem bore (§2) and between the seat ring outer surface and the core body bore (§3(6)) — and does not reconcile outward deflection of an interference-fitted ring with a gap opening at its outer surface. This example follows the disclosure's own words for S3–S4 without resolving that inconsistency; the mechanism is not treated here as fully enabled (see Open Questions Q1; this bears on Prompt 17).

*Inputs/outputs.* Input: a pressure differential between the supply side (inflation device, a floor pump) and the chamber side (a 700×28 inner tube charged with 60 ml of liquid sealant), applied over repeated inflation cycles (inflate to 6 bar, hold 24 h at 22 °C, deflate fully). Output: inflation of the inflatable chamber; the air purge and snap-back wipe cleaning actions; measured leak-down and inflation time. (Support: `intake/disclosure.md` §8; `intake/data/bench-test.md`.)

*Actual results (reported, not invented).* All three prototype cores (P-1, P-2, P-3) completed 40 inflation cycles with no failure, against a failure criterion of leak-down exceeding 0.5 bar in 24 h or the pump failing to open the valve within 5 s. Inflation time rose from cycle 1 to cycle 40: P-1, 43 s to 47 s; P-2, 41 s to 46 s; P-3, 44 s to 50 s. Leak-down at cycle 40: P-1, 0.1 bar/24 h; P-2, 0.1 bar/24 h; P-3, 0.2 bar/24 h. By comparison, three conventional valve cores (C-1, C-2, C-3) failed between cycles 12 and 18: C-1 blocked at cycle 14 (inflation time rising from 41 s to 68 s by cycle 13); C-2 reached a leak-down of 0.7 bar at cycle 12 (inflation time rising from 40 s to 44 s by cycle 11); C-3 blocked at cycle 18 (inflation time rising from 42 s to 75 s by cycle 17). Over-travel was indicated on every prototype inflation by an audible snap on removal of the inflation device. Post-test inspection of the prototype cores at cycle 40 under a stereo microscope found cured sealant film on the outer surface of the seat ring in the purge-gap region, while the sealing edge and the poppet face were clean. No fatigue or cold-shock testing was performed; the seat ring's fatigue life beyond 40 over-travel cycles, and its behaviour under CO2-inflator chilling, are not established. (Source for every value in this paragraph: `intake/data/bench-test.md`, corroborated by `intake/disclosure.md` §8, §9.)

*Expected technical effect.* The embodiment is reported, on this evidence, to keep sealing and keep opening over more sealant-loaded inflation cycles than the conventional comparator, without a tool or manual clearing step, consistent with the effect stated at `intake/disclosure.md` §2. The evidence does not establish which of the air purge and the snap-back wipe contributes how much, nor performance beyond 40 cycles, under CO2 inflation, or with ammonia-free sealants (support: `intake/disclosure.md` §9).

#### Prophetic examples

**Example 2 — PEEK seat ring embodiment (Alternative A)**

*Prophetic example.* This instantiates the embodiment disclosed at `intake/disclosure.md` §6, Alternative A, which the inventor has not built or tested. No measured result is reported for it.

*Components.* The same architecture as Example 1 — valve stem (10), core body (20), poppet (40) with sealing face (42) and purge shoulder (44), return spring (50), lock nut (70) — except that the seat ring (30) would be formed from a resilient polymer instead of a superelastic alloy.

*Materials.* Seat ring (30): PEEK. All other parts as in Example 1 (support: `intake/disclosure.md` §5, §6).

*Dimensions/ranges.* The disclosure states only that the PEEK seat ring would have "the same convoluted wall" as the superelastic seat ring (§6); no PEEK-specific dimensions are given. The dimensions and pressure/displacement values given for Example 1 (§4) were derived against the stiffness and recovery behaviour of superelastic NiTi and are not asserted to apply unmodified to a PEEK ring, which has lower stiffness and slower recovery (§6). A person skilled in the art would adapt them to PEEK's material properties; the specific adapted values are not in the disclosure and are recorded as a disclosure request below rather than invented here.

*Fabrication/assembly.* The disclosure does not state a fabrication process for the PEEK seat ring or how it would be retained in the core body. It would be assembled into the same core body and poppet architecture as Example 1, with the ring fitted against the internal shoulder in place of the NiTi ring. The forming process and retention method are recorded as a disclosure request below; no specific process parameters are asserted.

*Operating sequence.* The same closed, normal-open, purge and recovery states as Example 1 (S1–S5), except that on removal of the inflation device the seat ring's shape recovery would be slower and the resulting snap-back wipe force lower than for the superelastic ring, so the wipe would be weaker; the air purge would operate independently of the wipe (support: `intake/disclosure.md` §6).

*Inputs/outputs.* The same inputs and outputs as Example 1.

*Expected technical effect.* This embodiment is expected to provide the air purge cleaning action with a weaker snap-back wipe than Example 1, and is proposed by the inventor for a lower-cost product line (§6). No cycle-life, leak-down or inflation-time data exist for this embodiment; none is asserted.

**Example 3 — fixed seat and wiper ring embodiment (Alternative B)**

*Prophetic example.* This instantiates the embodiment disclosed at `intake/disclosure.md` §6, Alternative B, which the inventor has not built or tested. No measured result is reported for it.

*Components.* A valve stem (10) and core body (20) as in Example 1. A rigid fixed seat, in place of the seat ring, against which the sealing face (42) of the poppet seats in the closed state. A separate wiper ring, positioned on the chamber side of the fixed seat, deflected radially outward by the purge shoulder (44) during over-travel. A poppet (40), return spring (50) and lock nut (70) as in Example 1.

*Materials.* Fixed seat: brass. Wiper ring: stainless (spring) material (support: `intake/disclosure.md` §6).

*Dimensions/ranges.* Not given in the disclosure. The form, thickness and retention of the wiper ring are not stated (see Open Questions and disclosure requests below); no dimensions are invented for this example.

*Fabrication/assembly.* Not disclosed beyond the general architecture (a fixed seat plus a separate deflectable wiper ring). The inventor states this arrangement is "possibly easier to make," at the cost of one more part and more axial length than Example 1 (§6); no specific process steps are given.

*Operating sequence.* At or above the crack pressure, the poppet's sealing face seats on the fixed seat (closed state) and lifts by the normal stroke (normal-open state) as in Example 1. Above the over-travel threshold, the purge shoulder deflects the wiper ring outward, opening a purge gap through which the air purge would flow (purge state). On removal of the inflation device, the wiper ring would undergo shape recovery and the purge gap would close (recovery). Whether the recovering wiper ring also performs a snap-back wipe on the poppet, and if so which surface moves across which, is not stated in the disclosure.

*Inputs/outputs.* The same inputs and outputs as Example 1.

*Expected technical effect.* Separating sealing (at the fixed seat) from purging and any wipe (at the wiper ring) is disclosed as a way of building the mechanism, at the cost of an additional part and axial length (§6). No data exist on its cycle life, leak-down or inflation-time performance, and whether it provides a snap-back wipe of any effectiveness is an open question rather than an asserted effect.

## Rationale

**Choice of "principal embodiment."** The task instructs drafting from confirmed embodiments and names `CONFIRMED.md` as the source. That file's header states it was "Confirmed at Gate 2... Candidate status is lifted by this gate and by nothing else," but its body is a verbatim copy of `11.md`–`15.md`: a design-around risk register, an equivalent-architecture library, parameter ladders, a combination matrix and a failure-mode list, in which almost every entry is still individually marked "Status: candidate" and "Needs inventor confirmation" or "Not conceived — inventor to confirm," and several are marked "Cannot be closed without new matter." `intake/answers.md` (the Gate 1 answers that would resolve these) does not exist in this run. Treating that body of material as confirmed embodiment content would mean describing dozens of AI-generated design-around variants — most explicitly not within the inventor's stated conception — as though the inventor had disclosed them, which the role's "Never describe an unconfirmed candidate embodiment" rule forbids regardless of what a header claims.

I therefore did not draw the three principal embodiments from that candidate material. Instead I used the one class of source this role may always draft from regardless of Gate 2: the intake disclosure itself (`intake/disclosure.md` §1–§9), read through `runs/r1/P1/01.md` and `03.md`. §2 gives the baseline superelastic seat ring embodiment, actually built and bench-tested; §6 gives two further embodiments the inventor themself proposed — Alternative A (PEEK ring) and Alternative B (fixed seat plus wiper ring) — as embodiments, not as AI-generated design-arounds. These three are also the three core embodiments (E-I, E-II, E-III) that `14.md`'s Combination Matrix independently derived from the same source. This keeps the worked examples squarely within material the inventor is on record as having conceived, and defers the much larger candidate library to Claims Architect and to Gate 2/Gate 1 as design-around and fallback material, not as description content.

I flag the header/body conflict in `CONFIRMED.md` as an open disagreement for the human, since an "auto-unattended" Gate 2 that stamps a candidate risk register as confirmed, without the Gate 1 questions ever having been put to the inventor, is a process gap this role is built to catch rather than paper over.

**Actual vs prophetic.** Example 1 is actual: every reported value is traced to `intake/data/bench-test.md` or to `intake/disclosure.md` §7–§8, with the source named next to each figure, and no result is stated for anything not measured (fatigue life, cold-shock behaviour, the relative contribution of the air purge versus the snap-back wipe). Examples 2 and 3 are prophetic: written in the conditional, naming the confirmed disclosure passage each instantiates (§6, Alternatives A and B), and reporting no measured result. Where the disclosure does not give a dimension, process or behaviour for these two (PEEK forming process; wiper ring form, thickness and retention; whether the wiper ring wipes), I left it unspecified and raised a disclosure request rather than inventing a plausible number, consistent with the "never fabricate" rule and with `14.md`'s own footnotes [a]–[d], which flag exactly these gaps.

**Materials F1/F2 not elevated to separate examples.** The disclosure also mentions a stainless 303 core body (F1) and a hard-anodised aluminium sealing face (F2) as considered material variants (§5). Whether either was ever built into a working, tested core is unstated (01 Q18, Q19), and each is a single-part material substitution rather than a structurally distinct embodiment, so I noted them here rather than drafting them as separate numbered examples; they remain available as dependent material for Claims Architect and for later Description sections.

## Assumptions

A1. The three principal embodiments for this prompt are the superelastic seat ring embodiment (§2 baseline, actually built), the PEEK seat ring embodiment (§6 Alternative A) and the fixed-seat-and-wiper-ring embodiment (§6 Alternative B), drawn from the intake disclosure rather than from the Phase 3 candidate library in `CONFIRMED.md`. Not blocking; reasoned above.

A2. The Phase 3 design-around and equivalent-architecture candidates (`11.md` DA-1–DA-25; `12.md` E1.1–E16.3) are treated as not confirmed for drafting purposes, despite `CONFIRMED.md`'s header, because their own text still reads "Status: candidate" / "Needs inventor confirmation" / "Not conceived," and Gate 1 (`intake/answers.md`) does not exist. Blocking for P4 and P5 until the human resolves the Gate 2 status question (see Open Disagreements).

A3. Example 1's values for over-travel distance (0.5 mm) and purge gap opening (0.15 mm) are reported as the disclosure's stated prototype values, flagged as not independently measured in the bench test (only indirectly indicated by an audible snap). Not blocking for this prompt; blocking for Prompt 17's enablement audit.

A4. Example 1's operating sequence follows §2's and §3(6)'s stated mechanism (purge shoulder deflects the seat ring outward; purge gap opens) without resolving the inconsistency between that mechanism and the interference-fitted retention of §7. Blocking for P4 (Prompt 17 enablement audit) until Q1/Q2 (from `01.md`/`03.md`) are answered.

A5. No fabrication process or dimensions are asserted for the PEEK seat ring (Example 2) or for the wiper ring's form, thickness and retention (Example 3) beyond what §6 states; gaps are recorded as disclosure requests rather than invented values. Not blocking for this prompt; blocking for a fuller Description of Examples 2 and 3.

## Open Questions

Q1. How does the purge gap actually open, given that §2/§3(6) describe outward radial deflection of the seat ring while §7 describes the seat ring as interference-fitted against the core body bore? (Carried from `01.md` Q1/Q2 and `03.md` Q2.) Blocks P4 (Prompt 17 enablement audit), P5.

Q2. Did the prototype seat ring have one or two convolutions, and what is the convolution's exact profile? (Carried from `01.md` Q11.) Blocks P4.

Q3. For the fixed-seat-and-wiper-ring embodiment (Example 3): what are the wiper ring's form, thickness and retention method, and does it wipe the poppet on recovery? (Carried from `01.md` Q20 and `03.md` Q7.) Blocks P4, P5.

Q4. What fabrication process would be used to form a PEEK seat ring, and what dimensions would be adapted from the superelastic-ring values to suit PEEK's lower stiffness and slower recovery? (Carried from `01.md` Q11, Q20.) Blocks P4.

Q5. Was the stainless 303 core body (F1) ever built into a working, tested core? (Carried from `01.md` Q18.) Blocks P4 if F1 is later elevated to its own example.

Q6. Does the runner/human intend the `CONFIRMED.md` Gate 2 stamp to have actually resolved the "needs inventor confirmation" items it contains, given that Gate 1 (`intake/answers.md`) does not exist in this run? This governs how much of the Phase 3 candidate library may be used in later Description sections. Blocks P4, P5, PACKAGE.

```json
{
  "prompt": "18",
  "status": "partial",
  "assumptions": [
    {"id": "A1", "text": "Three principal embodiments taken as the superelastic seat ring embodiment (§2), the PEEK seat ring embodiment (§6 Alt A) and the fixed-seat-and-wiper-ring embodiment (§6 Alt B), drawn from the intake disclosure rather than the Phase 3 candidate library.", "blocking": false},
    {"id": "A2", "text": "Phase 3 design-around/equivalent-architecture candidates in CONFIRMED.md treated as not confirmed for drafting, despite the file's header, because their own text and status fields still read candidate/needs-confirmation and Gate 1 answers do not exist.", "blocking": true},
    {"id": "A3", "text": "Over-travel distance (0.5 mm) and purge gap opening (0.15 mm) reported as stated prototype values, flagged as not independently measured (only indicated by an audible snap).", "blocking": false},
    {"id": "A4", "text": "Example 1's operating sequence follows the disclosure's stated purge-gap mechanism without resolving its inconsistency with the interference fit.", "blocking": true},
    {"id": "A5", "text": "No fabrication process or dimensions invented for the PEEK ring or the wiper ring beyond what §6 states; gaps recorded as disclosure requests.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "How does the purge gap open given outward deflection of an interference-fitted seat ring (01 Q1/Q2, 03 Q2)?", "blocks": ["P4", "P5"]},
    {"id": "Q2", "text": "One or two convolutions in the prototype seat ring, and their exact profile (01 Q11)?", "blocks": ["P4"]},
    {"id": "Q3", "text": "Wiper ring form, thickness, retention and whether it wipes on recovery (01 Q20, 03 Q7)?", "blocks": ["P4", "P5"]},
    {"id": "Q4", "text": "Fabrication process and adapted dimensions for a PEEK seat ring (01 Q11, Q20)?", "blocks": ["P4"]},
    {"id": "Q5", "text": "Was the stainless 303 core body (F1) ever built into a working, tested core (01 Q18)?", "blocks": ["P4"]},
    {"id": "Q6", "text": "Does the human intend the CONFIRMED.md Gate 2 stamp to have resolved the needs-inventor-confirmation items despite Gate 1 answers not existing?", "blocks": ["P4", "P5", "PACKAGE"]}
  ],
  "new_terms": [],
  "support_refs": [
    {"item": "Example 1 components, materials, dimensions, fabrication", "support": "intake/disclosure.md §2, §3, §4, §5, §7"},
    {"item": "Example 1 operating sequence S1-S5", "support": "intake/disclosure.md §2; runs/r1/P1/01.md (d)"},
    {"item": "Example 1 actual bench results (cycles, leak-down, inflation time, inspection findings)", "support": "intake/data/bench-test.md; intake/disclosure.md §8, §9"},
    {"item": "Example 1 purge-gap location/mechanism flag", "support": "runs/r1/P1/01.md Q1, Q2; runs/r1/P1/03.md Q2"},
    {"item": "Example 2 PEEK seat ring embodiment", "support": "intake/disclosure.md §6 (Alternative A)"},
    {"item": "Example 3 fixed seat and wiper ring embodiment", "support": "intake/disclosure.md §6 (Alternative B)"},
    {"item": "Reference numerals 10-70", "support": "intake/disclosure.md §3; terminology/LOCKED.md"}
  ],
  "disclosure_requests": [
    {"limitation": "PEEK seat ring fabrication process and adapted dimensions (Example 2)", "needed_disclosure": "The process used or intended to form a PEEK seat ring, and dimensions validated for PEEK's stiffness and recovery, since the §4 values are derived against superelastic NiTi."},
    {"limitation": "Wiper ring form, thickness and retention (Example 3)", "needed_disclosure": "The wiper ring's geometry, material spec and how it is retained relative to the fixed seat and core body."},
    {"limitation": "Wiper ring wipe action (Example 3)", "needed_disclosure": "Whether the wiper ring performs a snap-back wipe on recovery, and if so which surfaces are involved."},
    {"limitation": "Purge gap opening mechanism (Example 1)", "needed_disclosure": "A reconciled written description of how the interference-fitted seat ring's outward deflection opens a purge gap, and the complete air path, needed before the operating sequence can be described as enabled."}
  ],
  "open_disagreements": [
    {"topic": "Status of CONFIRMED.md content", "position": "The Specification Drafter treated only the intake disclosure (§1-§9) as source for this prompt's principal embodiments, and excluded the Phase 3 AI-generated design-around and equivalent-architecture candidates from 11.md/12.md/13.md/15.md, notwithstanding CONFIRMED.md's header statement that Gate 2 lifted their candidate status, because the embedded documents' own body text still marks them candidate/needs-confirmation and Gate 1 answers (intake/answers.md) do not exist in this run. This should be resolved by the human before later phases rely on CONFIRMED.md's candidate library as though it were inventor-confirmed."}
  ],
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

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P4/20.md`

````markdown
## Deliverable

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

## Rationale

The figure set is organised around the four axial-section states (FIGs. 1–4) because the purge state (FIG. 3) is the figure every claim family ultimately depends on, and the inventor's own two sketches already anchor the closed and purge states. Adding the normal-open and recovery states as separate figures, rather than folding them into callouts on FIG. 1/3, gives each nucleus rung (N0(a) normal stroke, N1 snap-back wipe) its own drawn support, which strengthens both enablement (Prompt 17) and the claim-to-figure support map Claims Architect will need.

I drew alternative embodiments and design-around species only where the confirmed material (`11.md`, `12.md`) gives enough structural detail to instruct a draftsperson without inventing geometry, and where the entry is not marked "cannot be closed without new matter" (DA-7, DA-23, DA-24 excluded) or effectively withdrawn by the inventor's own stated doubt with no data (F5/DA-25 excluded, left to 01 Q21). I did not draw every one of the 25 design-around entries or 60-odd equivalent architectures individually; several entries (E1.2 separate purge actuator, E1.3 two-part poppet with purge sleeve, E9.4 positively driven recovery, E6.2/E6.3 alternative deflection directions, E7.2–E7.4 alternative purge-gap locations, E12/E13 alternative alloys and transformation temperatures, E15 alternative manufacturing routes) are left undrawn within this figure-plan scope; they are candidates for a later figure-plan revision once Prompt 16's blueprint identifies which of them the claims actually need drawn support for, and are listed in Open Questions so they are not silently dropped.

The most consequential drafting choice is FIG. 6's interference-fit convention. §2 says the seat ring "flexes radially outward"; §3(6) locates the purge gap at the seat ring's outer surface against the core body bore; §7 presses the ring in with an interference fit. Outward expansion ordinarily closes a gap at the outer surface, not opens one (01 Q2). Rather than inventing a resolving mechanism, FIG. 6 shows the interference fit confined to the region against the internal shoulder, leaving the remainder of the seat ring's outer surface — the region where the purge gap opens — free of interference. This is consistent with §7's own statement that the ring is "seated against the internal shoulder," and it is the reading the locked terminology table already adopts for the "purge gap" species (subject to Q1). It is flagged, not asserted as fact, and the underlying inconsistency remains open pending inventor confirmation.

FIGs. 11–15 draw single representative geometries for each design-around family (for example one tapered-shoulder species, not every angle) to keep the sheet count proportionate; the combination matrix's own conditional/incompatible cells (`14.md` footnotes) were respected — no figure combines electropolishing with the PEEK ring, and no figure gives the PEEK or wiper-ring embodiments an austenite finish temperature callout.

## Assumptions

A1. The inventor's FIG-1.png and FIG-2.png show the closed and full-over-travel states respectively, consistent with the README's descriptions; no other content of those images is assumed. Not blocking; blocks final figure sheets until the images (or a description of their actual content) are supplied (01 Q22).

A2. The interference fit (§7) is confined to the region of the seat ring against the internal shoulder, leaving the remainder of its outer surface free to move, so that outward radial deflection can open a purge gap at that surface without contradicting the interference fit. This is a drafting convention adopted to draw FIG. 6 consistently with §2, §3(6) and §7; it is not asserted as the inventor's actual construction. Blocking for P4 (enablement audit, Prompt 17) and P5 until confirmed or corrected at Gate 1/2.

A3. The direction of poppet travel and the meaning of "upper"/"below"/"under" follow 01 A4/A5 (poppet moves, and over-travels, towards the chamber side/tube interior). Blocking for figure orientation until 01 Q3 is answered.

A4. Schrader-pattern and non-removable architectures (FIG. 15) are drawn schematically only, without asserting specific Schrader-core or valve-stem-integrated dimensions, since none are disclosed. Not blocking for P4; blocks a to-scale FIG. 15 until the inventor supplies or confirms dimensions (01 Q26).

## Open Questions

Q1. Does the inventor confirm the interference-fit convention adopted for FIG. 6 (A2 above), or is the seat ring's outer surface interference-fitted along its full length, in which case the purge-gap opening mechanism needs a different explanation before FIG. 1/3/6 can be treated as enabled? Blocks P4 (Prompt 17 enablement audit), P5.

Q2. Should FIGs. 11–15's undrawn siblings (alternative purge-gap locations E7.2–E7.4; alternative deflection directions E6.2/E6.3; separate purge actuator E1.2/E1.3; positively driven recovery E9.4; alternative alloys/transformation temperatures E12/E13; alternative manufacturing routes E15.2–E15.7) be added as figures once Prompt 16's blueprint shows which claim families need them, or does the human consider the 15-figure set in this plan sufficient disclosure? Blocks P4 (registry finalisation), P5.

Q3. Is the thermally actuated purge variant (F5/DA-25) to be included as a figure at all, given the inventor's stated doubt and the absence of data? If yes, on what structural basis (no geometry beyond "a two-way shape-memory ring") should it be drawn? Blocks P4.

Q4. Once Prompt 16 (blueprint) exists, which figures does each claim family in fact need cited against — this plan currently maps figures to nucleus rungs (N0–N7) and DA/E ids only, not to blueprint section ids. Blocks P4 (final figure-to-claim cross-reference), P5.

```json
{
  "prompt": "20",
  "status": "complete",
  "assumptions": [
    {"id": "A1", "text": "FIG-1.png/FIG-2.png show the closed and full-over-travel states per the README; no other content assumed.", "blocking": false},
    {"id": "A2", "text": "Interference fit is drawn as confined to the internal-shoulder region, leaving the rest of the seat ring's outer surface free, to reconcile §2/§3(6)/§7 for FIG. 6; a drafting convention, not an asserted fact.", "blocking": true},
    {"id": "A3", "text": "Poppet travel/over-travel direction follows 01 A4/A5 (towards the chamber side).", "blocking": true},
    {"id": "A4", "text": "FIG. 15 (Schrader-pattern, non-removable) is schematic only, no asserted dimensions.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "Confirm or correct the FIG. 6 interference-fit convention (A2); needed before FIG. 1/3/6 can be treated as enabled.", "blocks": ["P4"]},
    {"id": "Q2", "text": "Should the undrawn equivalent-architecture siblings be added as figures, or is the current 15-figure set sufficient?", "blocks": ["P4"]},
    {"id": "Q3", "text": "Include the thermally actuated purge variant (F5/DA-25) as a figure, and on what structural basis?", "blocks": ["P4"]},
    {"id": "Q4", "text": "Map figures to blueprint section ids once Prompt 16 exists.", "blocks": ["P4"]}
  ],
  "new_terms": [
    {"term": "tapered purge shoulder", "maps_to": "purge shoulder", "reason": "Species from E3.2/DA-4, a frustoconical alternative to the disclosed annular shoulder."},
    {"term": "discrete lugs", "maps_to": "purge shoulder", "reason": "Species from E3.3, a segmented alternative to the continuous annular purge shoulder."},
    {"term": "separate collar", "maps_to": "purge shoulder", "reason": "Species from E3.4, a purge shoulder fixed onto the poppet stem as a distinct part."},
    {"term": "frustoconical wall", "maps_to": "convoluted wall", "reason": "Species from E5.3/DA-12, a conical alternative axial-to-radial conversion geometry."},
    {"term": "slotted wall", "maps_to": "convoluted wall", "reason": "Species from E4.3/DA-3, a finger-forming alternative wall geometry."},
    {"term": "cellular wall", "maps_to": "convoluted wall", "reason": "Species from E5.4, a laser-cut lattice alternative wall geometry."},
    {"term": "purge port", "maps_to": "purge flow path", "reason": "Species from E8.2, a through-wall alternative purge-flow-path structure."},
    {"term": "flute", "maps_to": "purge flow path", "reason": "Species from E8.3, an axial-groove alternative purge-flow-path structure."},
    {"term": "auxiliary spring", "maps_to": "second spring stage", "reason": "Species from E2.2/E2.4, a lost-motion alternative threshold-setting arrangement."},
    {"term": "detent", "maps_to": "second spring stage", "reason": "Species from E2.5, a breakaway-force alternative threshold-setting arrangement."},
    {"term": "crimped lip", "maps_to": "interference fit", "reason": "Species from E14.2/DA-22, an alternative ring-retention structure."},
    {"term": "retaining sleeve", "maps_to": "interference fit", "reason": "Species from E14.3/DA-22, an alternative ring-retention structure."},
    {"term": "Schrader-pattern valve core", "maps_to": "valve core", "reason": "Species from DA-6/E16.2, an alternative valve-pattern architecture."},
    {"term": "non-removable inflation valve", "maps_to": "inflation valve", "reason": "Species from E14.6/E16.3, an architecture with no separate core body."}
  ],
  "support_refs": [
    {"item": "FIG. 1 closed state, FIG. 3 purge state", "support": "intake/disclosure.md §2, §3; intake/drawings/README.md"},
    {"item": "FIG. 9 PEEK seat ring", "support": "intake/disclosure.md §6 (Alternative A); runs/r1/P3/14.md CB3, footnote [a]"},
    {"item": "FIG. 10 fixed seat + wiper ring", "support": "intake/disclosure.md §6 (Alternative B); runs/r1/P3/14.md CB4"},
    {"item": "FIG. 11 alternative purge-shoulder geometries", "support": "runs/r1/P3/11.md DA-4; runs/r1/P3/12.md E3.2-E3.4"},
    {"item": "FIG. 12 alternative wall geometries", "support": "runs/r1/P3/11.md DA-3, DA-12, DA-18; runs/r1/P3/12.md E4.3, E4.4, E5.3, E5.4"},
    {"item": "FIG. 13 alternative purge-flow-path geometries", "support": "runs/r1/P3/12.md E8.2, E8.3"},
    {"item": "FIG. 14 alternative threshold-setting arrangements", "support": "runs/r1/P3/11.md DA-11; runs/r1/P3/12.md E2.2, E2.4, E2.5"},
    {"item": "FIG. 15 alternative valve architectures", "support": "runs/r1/P3/11.md DA-6; runs/r1/P3/12.md E14.6, E16.2, E16.3"},
    {"item": "FIG. 6 interference-fit convention", "support": "intake/disclosure.md §2, §3(6), §7; runs/r1/P1/01.md Q1, Q2"}
  ],
  "disclosure_requests": [
    {"limitation": "Purge-gap opening mechanism given the interference fit", "needed_disclosure": "Confirmation of which part of the seat ring's outer surface is interference-fitted and which is free, so FIG. 6 can be drawn from a confirmed mechanism rather than a reconciling convention."},
    {"limitation": "What limits over-travel (FIG. 2/3 geometry)", "needed_disclosure": "Whether a mechanical stop, spring coil-bind, or the seat ring itself limits the 0.5 mm over-travel distance, so FIG. 2/3 can show the limiting feature (01 Q36)."}
  ],
  "open_disagreements": [],
  "narrowing_suggested": []
}
```
````

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P4/20a.md`

````markdown
## Deliverable

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

## Rationale

The registry preserves the inventor's own nine reference numerals unchanged, as `terminology/LOCKED.md` requires, and extends them by family rather than restarting a 100-series at FIG. 1, because FIG. 1–8 are all views of the single preferred embodiment and gain nothing from a figure-indexed numbering scheme; the 100/200/300/400/600/700 blocks are reserved instead for genuinely alternative components and species, which is where a reviewer or examiner most needs the numbering to signal "this is a different embodiment," per Claims Architect's likely need to map dependent claims to specific alternative figures.

I used letter suffixes (32a/32b, 344a/344b, 332a/332b) for repeated instances of one component rather than separate base numerals, to keep the registry table to one row per distinct component as the machine-parsed table format requires, while still letting the drawing instructions show multiple instances where the geometry needs it (two convolutions, several lugs, several fingers).

FIG. 15's schematic sub-views are given new numerals only where the carrying part differs (730, because the seat ring is carried by the valve stem rather than a core body); where the Schrader-pattern architecture reuses the same mechanism, I did not invent new numerals for the seat ring, purge shoulder or purge gap, to avoid implying a structural difference that is not confirmed.

## Assumptions

A1. Two convolutions (32a, 32b) are shown as an option in FIG. 1 and FIG. 6, with a note to omit the second if the description confirms only one; the prototype's actual count is unstated (01 Q11). Blocking for P4 finalisation of FIG. 1/6 once the count is confirmed.

A2. The FIG. 6 interference-fit/purge-gap convention (Prompt 20, Assumption A2) is carried into the registry as a flagged, not confirmed, mechanism. Blocking for P4/P5 until 01 Q1/Q2 are answered.

A3. Component instance suffixes (32a/32b, etc.) are not separately registered in the four-column table, consistent with the "one component, one numeral" registry convention; individual instances are documented in the Figure Instructions instead. Not blocking.

## Open Questions

Q1. Confirm the seat ring's convolution count (one or two) so FIG. 1/6 can drop the optional 32b. Blocks P4.

Q2. Confirm or correct the interference-fit/purge-gap mechanism (numeral 60/24 region) before FIG. 6 and its registry entry are treated as final. Blocks P4, P5.

Q3. When `description.md` and `claims.md` exist, re-run the cross-check this registry defers (flag 1): every component named in those texts must have a numeral here, and every numeral here that the description relies on must appear in the description. Blocks P4 (Prompt 38), PACKAGE.

Q4. Should FIG. 15's Schrader-pattern sub-view register its own seat-ring/purge-shoulder/purge-gap numerals distinct from 30/44/60, given that a real Schrader-pattern part would differ in bore and thread even if the deflection mechanism is unchanged? Left unregistered pending Prompt 16's blueprint decision on how broadly the valve-core claims are pursued. Blocks P4.

```json
{
  "prompt": "20a",
  "status": "complete",
  "assumptions": [
    {"id": "A1", "text": "Two convolutions (32a, 32b) shown as an option pending confirmation of the actual count (01 Q11).", "blocking": true},
    {"id": "A2", "text": "FIG. 6 interference-fit/purge-gap convention carried into the registry as flagged, not confirmed.", "blocking": true},
    {"id": "A3", "text": "Component instance suffixes are documented in the Figure Instructions, not as separate registry rows.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "Confirm the seat ring's convolution count.", "blocks": ["P4"]},
    {"id": "Q2", "text": "Confirm or correct the interference-fit/purge-gap mechanism before FIG. 6/numeral 60 is final.", "blocks": ["P4", "P5"]},
    {"id": "Q3", "text": "Re-run the description/claims cross-check once those files exist.", "blocks": ["P4", "PACKAGE"]},
    {"id": "Q4", "text": "Should FIG. 15A register its own numerals distinct from 30/44/60?", "blocks": ["P4"]}
  ],
  "new_terms": [],
  "support_refs": [
    {"item": "Numerals 10, 20, 30, 40, 42, 44, 50, 60, 70", "support": "intake/disclosure.md §3; terminology/LOCKED.md (reference numerals note)"},
    {"item": "FIG. 6 interference-fit convention", "support": "runs/r1/P4/20.md Assumption A2; intake/disclosure.md §2, §3(6), §7"},
    {"item": "FIG. 10 numerals 130, 132", "support": "intake/disclosure.md §6 (Alternative B); terminology/LOCKED.md rows 'fixed seat', 'wiper ring'"},
    {"item": "FIG. 11-14 alternative-species numerals", "support": "runs/r1/P3/12.md E3.2-E3.4, E4.3, E4.4, E5.3, E5.4, E8.2, E8.3, E2.2, E2.4, E2.5"},
    {"item": "FIG. 8D/8E retention numerals 224, 324", "support": "runs/r1/P3/11.md DA-22; runs/r1/P3/12.md E14.2, E14.3"},
    {"item": "FIG. 15 numerals 620, 630, 730", "support": "runs/r1/P3/11.md DA-6; runs/r1/P3/12.md E14.6, E16.2, E16.3"}
  ],
  "disclosure_requests": [],
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

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/risk/pre-drafting-findings.md`

````markdown
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
````

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
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/intake/drawings`/

## Inputs that do not exist yet (work without them; do not wait)

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P4/17.md`

## Files to write

Write each of these with your Write tool, at exactly this path, one file per call (the folders exist). Write nothing outside the run folder `{R}`. Do not run the checks yourself: the runner runs them and will tell you if anything fails.

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P4/parts/part3.md`

When every file is written, reply with one line per file (path and a few words on what it holds) and anything the runner must route: open questions, disclosure requests, open disagreements, narrowing suggested. Nothing else.
