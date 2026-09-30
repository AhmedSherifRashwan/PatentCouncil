# Patent Council · matter `valve-oc-20260930` · run `r1` · step `RES` · profile full

You are the **Prior-Art Analyst**. Follow your AGENTS.md. This message is the whole brief: what to do, the prompts to execute, every input (embedded below, so do not re-read those files), and the exact files to write.

## What to do

Starts at minute zero, alongside Phase 1. (1) Run Prompt 06 from the disclosure itself (Phase 1 outputs are optional: use any that are embedded). (2) Search with your web tools: patent databases (Google Patents, Espacenet, Lens) and the technical literature, using its strings and classes. **Generic technical queries only: never disclosure text, never the invention's own phrasing.** Read the strongest candidates' claims. (3) Choose the 10–20 closest references and write `prior-art/INDEX.md`: one row per reference with the publication number written in full (e.g. `US 10,123,456 B2`, `EP 3456789 A1`), title, assignee, priority and publication dates, URL, the concepts it hits and closeness 1–5. The runner fetches every numbered patent's full text into `prior-art/refs/<number>.md` from the number alone. For a non-patent reference, save its relevant text yourself as `prior-art/refs/NPL-<n>.md` with URL and access date. (4) `prior-art/search-log.md`: every query run, where, and what was kept or dropped.

**Time budget:** about 18 minutes. The whole matter is planned to finish end to end in two hours. Be complete, but write each deliverable once: no drafts, no repetition, no padding.

## Prompt 06 — Search concept decomposition  (kind `analysis`)

**Write your reply to:** `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P2/06.md`

*Create a search strategy before relying on known references.*

Break the invention into searchable technical concepts and combinations. Generate keyword families, synonyms, CPC/IPC themes, applicant/assignee categories and search strings. Separate searches for the core architecture, individual components, functional equivalents, manufacturing method, use method and adjacent technologies.

**How to work.** The synonym and genus/species columns of the terminology table are your keyword seed; extend them for search purposes but do not treat search synonyms as drafting terms (they do not need `new_terms` entries unless you propose them for the specification). Under `### Search Concept Decomposition` give one sub-heading per search track (core architecture, individual components, functional equivalents, manufacturing method, use method, adjacent technologies) each with: concept statement, keyword families, CPC/IPC themes (mark any classification you are not certain of as an assumption), applicant/assignee categories, and ready-to-run search strings. The strings are for the human or a search tool; you do not run them. Reply exactly in the drafting output contract: `## Deliverable` (with the H3 sections named above), `## Rationale`, `## Assumptions`, `## Open Questions`, then one final fenced `json` envelope. No preamble before `## Deliverable`; nothing after the envelope. Reuse locked preferred terms verbatim; declare any other term in `new_terms` with a reason.

**Machine-readable search strings.** In the JSON envelope add `"search_queries"`: a list of 6 to 12 objects `{"query": "<Google Patents query>", "purpose": "<what it targets>"}`. Each `query` must be a runnable Google Patents search: quoted multi-word phrases, `OR` between synonyms inside parentheses, at most one CPC/IPC group written as a bare code (for example `F16K15/20`, no `cpc:` prefix), no prose, no labels, no placeholders. Order them core architecture first, then components, functional equivalents, manufacturing, use, adjacent technologies. The runner sends only these strings to the search service when the matter has opted in.

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

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/prior-art/refs`/
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/intake/prior-art`/

## Inputs that do not exist yet (work without them; do not wait)

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/prior-art/INDEX.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P1/02.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P1/01.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P1/03.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P1/04.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/terminology/LOCKED.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/intake/answers.md`

## Files to write

Write each of these with your Write tool, at exactly this path, one file per call (the folders exist). Write nothing outside the run folder `{R}`. Do not run the checks yourself: the runner runs them and will tell you if anything fails.

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/P2/06.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/prior-art/INDEX.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/prior-art/search-log.md`

When every file is written, reply with one line per file (path and a few words on what it holds) and anything the runner must route: open questions, disclosure requests, open disagreements, narrowing suggested. Nothing else.
