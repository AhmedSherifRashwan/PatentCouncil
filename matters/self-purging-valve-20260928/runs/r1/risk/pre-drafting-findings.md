# Pre-drafting findings report — self-purging-valve-20260928 · r1

This report is a drafting and analysis aid prepared by AI. It is not legal advice, a patentability opinion or a filing decision; qualified patent counsel signs off before anything is filed. Every finding is `candidate`. The report goes to the Specification Drafter (P4) and the Claims Architect (P5) only. The reviewers must not see it.

## Summary

**Inputs.** `P1/01`, `P1/03`, `P2/08`, `P2/09` (quick profile: there is no Debate 1 and no `09r`), `P2/10`, `CONFIRMED.md` (Gate 2, auto-unattended), `terminology/LOCKED.md`, `prior-art/INDEX.md` and `~/PatentCouncil/lessons.md`. I checked the passages that carry the two lead findings against the saved text: `refs/US11179979B2.md` [0016] and [0101], `refs/US20080188352A1.md` [14] and [26], and `refs/US3417778A.md` [15]. `intake/answers.md` does not exist. No inventor answer is reflected anywhere in the dossier, and Gate 1 and Gate 2 were both decided unattended.

**Counts.** 20 findings: 3 critical, 9 high, 6 medium, 2 low. By category: formal 5, support 4, novelty 4, design-around 4, enablement 3.

**The five risks that matter most**

1. **PF-1 (critical, enablement).** The disclosure does not explain how the purge gap opens. As written, a seat ring held by an interference fit of about 0.03 mm expands outward against the core bore and still opens a gap of 0.15 mm against the same bore, which is physically contradictory. Every claim that relies on the purge gap depends on the answer. Drafting cannot fix this alone. It must stop the contradiction entering the description and claim the purge gap by function.
2. **PF-2 (critical, novelty).** If "over-travel" is not anchored, US11179979B2 reads on N0. Its sealing lip is deflected to open a slit when "a higher pressure outside ... will result in an opening of the slit ... when inflating a tire" ([0016]). The independent claim holds only if it says three things: the *same* valve member travels *beyond its normal stroke*; that travel is caused by the pressure differential exceeding an over-travel threshold *higher than the opening pressure*; and it is that travel of the valve member which deflects the deflectable element.
3. **PF-3 (critical, formal and support).** The over-travel threshold is a pressure differential that no passage explains how to measure. The prototype's 3.5 bar threshold sits below the 6 bar inflation pressure of the bench test, and the dossier does not say across which two pressures the differential is taken (01 Q5; 13 ladder note 2). Without a stated measuring condition, every threshold rung is indefinite (US) or an unclear parameter (EPO/UK), and N8 cannot be relied on at all.
4. **PF-4 (high, support and inventorship).** Gate 2 confirmed, without a human, several dozen embodiments, rungs and mitigations whose own text says "Rests on: nothing yet", "proposed, needs confirmation" or "candidate - needs confirmation". If P4 writes them as the inventor's embodiments, or P5 claims them, AI-generated content becomes stated invention content. That breaks the user's directive, and in the US it raises an inventorship question for any claim whose only contribution is such an entry.
5. **PF-5 (high, novelty and support).** "A purge gap separate from the main flow passage" is the clause that separates N0 from US11179979B2, whose slit lies in series in the only flow path (07 R5). The dossier never describes the purge flow's inlet or outlet (01 Q2), so the word "separate" has only the FIG-2 caption behind it. That caption has not been seen as an image.

**Response obligations.** Each drafter answers every critical and high finding (PF-1 to PF-12) in its response table (`P4/pre-drafting-response-P4.md`, `P5/pre-drafting-response-P5.md`). Where a finding names both owners, both answer it.

## Findings

### PF-1 — The purge-gap mechanism is not described in a way a skilled person can carry out

- **Category:** enablement · **Severity:** critical · **Owner:** P4+P5
- **Concerns:** N0 (purge gap closed in the rest state, opened by deflection); 09 D1; 10 item 6; N4; N8 purge gap width; every "purge gap" definition.
- **Evidence:** 01 (b) and M1: §2 puts the gap "between the ring and the stem bore", while §3 item 6 puts it between "the seat ring outer surface and the core body bore". §3 item 3 and §7 say the ring is pressed in with ≈0.03 mm diametral interference. 03, "Enablement flag on N0": "outward expansion against a surrounding bore closes a gap rather than opening one." CONFIRMED 13 ladder note 1: "those two numbers cannot both describe the same surface." CONFIRMED 12 purge-gap preface: the E10 topologies are "coherent topologies ... not a statement of what the prototype does". E10.1 to E10.5 each say "Rests on: nothing yet".
- **Risk:** US: 35 U.S.C. §112(a) enablement and written description. EPO: Art. 83 EPC sufficiency. UK: s.14(3) PA 1977. All are judged on the filed text, and none can be repaired after filing without new matter (Art. 123(2) EPC; s.76 PA 1977; 35 U.S.C. §132). If the description repeats §2 and §3 literally, it contains two inconsistent locations and a mechanism an examiner or an opponent can call inoperable. If it adopts one of the E10 topologies as "the prototype", it states an invented fact.
- **Drafting response required:**
  - P5: define the purge gap in the independent claim by function and state only: "a purge gap, separate from the main flow passage, through which purge flow is prevented in the rest state and which is opened by the deflection of the deflectable element". Keep out of every independent claim: the gap's location (core bore or stem bore), the direction of deflection ("radially outward"), the interference fit and any purge gap width. A location clause may appear in a dependent claim only once the inventor answers 01 Q1.
  - P4: write one express definition of "purge gap" and one of "rest state", both functional, as LOCKED note 6 requires. Describe the prototype in the inventor's words only as far as they are consistent: the seat ring expands, the purge gap is closed at rest and opens on over-travel, and the gap is annular. Do not reproduce the §2/§3 contradiction, and do not reproduce the interference-fit value next to the 0.15 mm gap as if both act on one surface. Describe E10.1 to E10.5 only as alternative constructions, and only if Gate 2's confirmation is accepted for them (see PF-4). List each one in the response table as "AI-proposed, not inventor-confirmed".
  - Both: raise a `disclosure_requests` entry for 01 Q1, Q2 and Q10 and name them as a filing blocker for counsel. This risk cannot be fully answered by drafting.
- **Least narrowing:** the functional definition gives up no scope. Any narrowing to a location or deflection direction gives up DA-6, DA-9 and E10.3 to E10.5, and should wait for the inventor.

### PF-2 — "Over-travel" must be anchored, or US11179979B2 anticipates N0

- **Category:** novelty · **Severity:** critical · **Owner:** P4+P5
- **Concerns:** N0 over-travel clauses; 09 D2; definitions of "normal stroke", "over-travel" and "over-travel threshold".
- **Evidence:** `refs/US11179979B2.md` [0016]: the first valve's sealing lip is displaced or deformed to open a slit, and "a higher pressure outside of the tire/rim-space will result in an opening of the slit ... when inflating a tire". [0101]: the core rod 16 of a Presta- or Schrader-type valve core. 08 Objection 1: weak only if the claim requires "(i) over-travel caused by the pressure differential exceeding an over-travel threshold, and (ii) a purge gap separate from the main flow passage"; otherwise moderate. 08 A8 and 09 A2: ratings assume over-travel is defined relative to the valve seat. US20080188352A1 [26]: a second valve means opens a second path at a second pressure (the 08 "second rigid member" reading).
- **Risk:** Without all of these clauses, the lip of US11179979B2 is a pressure-deflected deflectable element that opens a closed gap during inflation: (a) the same valve member; (b) travel beyond a normal stroke from the valve seat; (c) a threshold higher than the opening pressure; (d) the over-travel of that valve member doing the deflecting. That is a novelty objection in all three offices. It is stronger under US inherency than under the EPO/UK "directly and unambiguously" test, but it is live in all three.
- **Drafting response required:**
  - P5: independent claim wording in locked terms, along these lines: "the valve member being movable away from the valve seat through a normal stroke when the pressure differential exceeds the opening pressure, and beyond the normal stroke through an over-travel when the pressure differential exceeds an over-travel threshold higher than the opening pressure, the over-travel of the valve member deflecting the deflectable element". Do not replace "over-travel of the valve member" with a result ("when the purge gap opens") or with "a second stage".
  - P4: define "normal stroke" and "over-travel" together with "opening pressure" and "over-travel threshold", as LOCKED note 6 requires, so that neither is circular. The normal stroke is the travel under a pressure differential between the opening pressure and the over-travel threshold; over-travel is the travel beyond it. State expressly that the deflectable element is not deflected during the normal stroke (§3 item 4, "only contacts the ring during over-travel"). Write at least one paragraph describing the three pressure bands of 10 item 5.
- **Least narrowing:** do not anchor over-travel to "relative to the valve seat" in the independent claim if the three-band wording above already excludes US20080188352A1. The "relative to the valve seat" wording is what DA-12 (a seat that moves with the valve member) escapes. Keep it as a dependent or definitional fallback.

### PF-3 — The over-travel threshold has no measuring condition, and 3.5 bar sits below the 6 bar test pressure

- **Category:** formal · **Severity:** critical · **Owner:** P4+P5
- **Concerns:** "pressure differential", "opening pressure", "over-travel threshold"; N8 pressure rungs; CONFIRMED 13 Table B.
- **Evidence:** LOCKED, "pressure differential": "pump pressure minus inflatable body pressure". 01 A3 and M5: when over-travel occurs during an inflation is unknown. The bench notes record the audible snap only "on pump-head removal". CONFIRMED 13 ladder note 2: "Whether the threshold is a differential between the inflation device and the inflatable body, or an absolute value, decides what the Table B rungs mean." CONFIRMED 15 FM-7: the threshold may be crossed once per pump stroke.
- **Risk:** US §112(b): a threshold whose measuring conditions a skilled person cannot determine invites an indefiniteness rejection. EPO/UK Art. 84 and s.14(5): EPO practice on parameters requires the measuring method to be derivable from the application. The inconsistency on the face of the data will also draw a sufficiency attack. If the differential is pump pressure minus tube pressure, a floor pump filling a tube to 6 bar may never impose 3.5 bar *across* the valve during flow. The inventor's statement that "every floor pump reaches" it is unevidenced (01 A6).
- **Drafting response required:**
  - P4: state how the opening pressure and the over-travel threshold are determined. The only framing the dossier supports is the locked definition (pressure on the inflation-device side minus pressure on the inflatable-body side). Say that the prototype values were set as that differential, but do not invent a test rig, a flow rate or a static procedure. If Prompt 17 finds the procedure missing, record a `disclosure_requests` entry (01 Q5) rather than write one. Do not describe the timing of over-travel within an inflation beyond the bench note (the audible snap on pump-head removal).
  - P5: claim the threshold relationally ("an over-travel threshold higher than the opening pressure"). This is the only pressure rung CONFIRMED 13 Table B marks as needing no confirmation. Keep numbers to dependent claims, and keep them in bar of pressure differential with the definition cross-referenced.
- **Least narrowing:** the relational claim gives up nothing. A numeric threshold in an independent claim would give up DA-17 and invite the US20080188352A1 [14] overlap (PF-13).

### PF-4 — Auto-confirmed AI proposals must not be drafted or claimed as the inventor's conception

- **Category:** support · **Severity:** high · **Owner:** P4+P5
- **Concerns:** all of `CONFIRMED.md`, in particular 11 DA closing genera marked "needs inventor confirmation", 12 entries marked "Rests on: nothing yet", 13 rungs marked "proposed, needs confirmation", 13 Table E ratios, and 15 mitigations marked "candidate - needs confirmation".
- **Evidence:** `gates/gate-2.md`: "No human, and in particular not the inventor, reviewed them ... Counsel should treat every entry marked 'needs inventor confirmation' as unconfirmed by the inventor and check it for new matter before filing." CONFIRMED 15 note 1 on the over-travel stop: "If they have not, it is new matter and must stay out." USER.md: "Never fill a factual gap about the invention on his behalf."
- **Risk:** Filing these entries does not create new matter; they would be in the original text. But the description would then state as the inventor's things the inventor never conceived. Counsel cannot tell them apart without a record. US: any claim whose only contribution is an AI-generated feature raises an inventorship question under USPTO guidance on AI-assisted inventions. All offices: a later declaration or opposition exposes invented statements. Omitting the entries costs amendment basis. Including them unmarked costs integrity.
- **Drafting response required:**
  - P4: draft "Rests on: §..." entries as embodiments. For each "nothing yet" entry, list it in the response table with its E, DA, FM or 13-rung id and a disposition: included as an alternative (the option counsel may strike), or omitted. Never describe a "nothing yet" entry as built, tested, preferred or "of the prototype". Never give a proposed rung the label "preferred". Label the 13 Table E ratios as arithmetic only, or omit them (13 Q11).
  - P5: no independent claim may need a "nothing yet" entry for novelty or support. Dependent claims resting only on such entries go in a separate block flagged for counsel (for example E3.2 over-travel stop, E5.2 to E5.6, E10.x locations, E15.2 Schrader-pattern valve core), and in `narrowing_suggested` or `open_disagreements` as appropriate.
- **Least narrowing:** not a scope question. The response is about labelling and traceability.

### PF-5 — "Separate from the main flow passage" carries the novelty case but has almost no disclosure behind it

- **Category:** support · **Severity:** high · **Owner:** P4+P5
- **Concerns:** 09 D1 and D3; N0 purge flow clause; the definitions of "main flow passage" and "purge flow".
- **Evidence:** 07 US11179979B2 R5 (absent): the slit lies in series in the only flow path. 08 "What the attack shows" item 1: R5 is one of the three clauses no single reference discloses. 01 Q2 and M2: the purge gap's inlet and outlet are not described. The FIG-2 caption ("air flow through the main passage and through the purge gap") is the only textual anchor, and the image has not been seen (01 sources line). CONFIRMED 12 E11.1: "the inlet and outlet are not described".
- **Risk:** If "separate" is not supported, P5 cannot rely on it (US §112(a) written description; EPO Art. 84 support and Art. 123(2) on amendment). Without it, the fallback is D2 alone against US11179979B2.
- **Drafting response required:**
  - P4: the description must say in terms that purge flow passes through the purge gap *in addition to*, and not through, the main flow passage past the valve seat, citing §2 para 1 and the FIG-2 caption. Describe the path only to the extent §2 and §3 item 6 give it. Treat E11.1 to E11.3 under PF-4.
  - P5: use "separate from the main flow passage" in the independent claim, and map it in `support-map.json` to that paragraph (L2). Do not add inlet or outlet structure in independent claims.
- **Least narrowing:** keep the clause at the level of "a second flow path". Any inlet/outlet structure narrows to the E11 species.

### PF-6 — Nucleus choice (purge flow vs recovery wipe) is unresolved, and the evidence cannot separate them

- **Category:** support · **Severity:** high · **Owner:** P4+P5
- **Concerns:** N0 vs N0-W (03); 09 D5; 10 items 3–4; 11 DA-1 and DA-16.
- **Evidence:** 03 Q1 and 08 Q2: undecided, and blocks P5. 01 (l): no test isolates the two mechanisms. The bench notes say that at inflation cycle 40, cured film remained "on the ring outer surface in the purge-gap region" while the sealing edge and the valve member face were clean. That is at least as consistent with the wipe as with the purge. 08 per-concept table: N0-W is rated moderate to strong on inventive step (ref-02 [0020] + US4236547A [6]).
- **Risk:** At the EPO, an effect that the claim does not credibly deliver across its scope cannot support inventive step. A purge-only independent claim covers DA-16 (no wipe), for which there is no evidence. In the US and UK the risk is lower but the same passage will be argued. If the wipe proves to be the operative mechanism, a purge-only nucleus has been claimed on the weaker ground.
- **Drafting response required:**
  - P4: present the two actions as the inventor does (§2 para 2, "cleans itself twice per inflation"). Give each its own effect statement, cite the bench inspection for the wipe, and do not state that either alone is sufficient.
  - P5: follow 03 and 11. N0, with purge flow, is the independent claim; the recovery wipe is the first dependent rung. Also prepare a second independent claim or an alternative formulation (Prompt 24) built on N0-W, so that either answer to 03 Q1 leaves a claim with support. Record the choice in `open_disagreements` for counsel.
- **Least narrowing:** do not put both actions in the independent claim. That would give up DA-16 and DA-1 at once.

### PF-7 — Inventive step against the three-document mosaic depends on how the problem and effect are written

- **Category:** novelty · **Severity:** high · **Owner:** P4
- **Concerns:** Background, Summary and technical-effect passages; 08 Objection 2.
- **Evidence:** 08 Objection 2: US11338632B2 [0004] (sealant fouling) + US20080188352A1 [26] (second path above a higher pressure) + US3570510A [26] (purge across the sealing surfaces). Rated moderate. "Where the attack is thin": none of the three opens a flow path by deflecting a resilient element through over-travel, and US3570510A needs a separate gas store ([22]). 09 D3 and D5.
- **Risk:** If the description frames the problem as "keeping a valve seat clean" and the solution as "flushing plus a two-stage valve", it writes the examiner's combination for them.
- **Drafting response required:** P4 frames the effect around what one moving part does. The inflation gas itself, admitted through a gap that exists only while the deflectable element is deflected by over-travel, cleans the surfaces on which sealant film forms. There is no stored gas, no added valve and no rider action, and below the over-travel threshold the valve behaves conventionally (09 D2, D3, D4; 10 item 5). State the effect of the single deflection event (purge on deflection, wipe on recovery) as the inventor states it. Do not concede in the text that "flushing a valve seat with the working fluid" or "two-stage spring valves" are well known (08 A2 and A3 are unsupported CGK assertions).
- **Least narrowing:** a drafting-only response; no scope given up.

### PF-8 — Keep the seat ring, the convoluted wall, the superelastic alloy and Af out of the independent claims

- **Category:** design-around · **Severity:** high · **Owner:** P5
- **Concerns:** N4, N5, N6, N6-A, N4-B; 09 D7 and D8; 11 DA-2, DA-3, DA-5, DA-10, DA-18.
- **Evidence:** 11 findings: "the seat ring, the convoluted wall, the superelastic alloy, the two-rate characteristic and the purge shoulder are preferred, not essential." §6 paras 1–2: the inventor's own alternatives A (PEEK) and B (rigid valve seat plus wiper ring). 08: the Af increment is rated strong on US6053992A [3].
- **Risk:** Any of these in an independent claim is escaped by the inventor's own alternative B (DA-2), rated "the most likely first design-around".
- **Drafting response required:** P5 uses "deflectable element" and "valve seat" as distinct terms in the independent claims. "Seat ring", "wiper ring", "convoluted wall" and "superelastic alloy" enter only in dependent claims, with N5 (convoluted wall; R14 absent in all charts) placed early because it has no reference against it (10 item 2). Consider a material-neutral article claim to the seat ring with a convoluted wall (10 item 2), flagged for counsel.
- **Least narrowing:** already least narrowing. The only cost is a longer dependent ladder.

### PF-9 — The two-rate biasing member must not carry the over-travel threshold in any independent claim

- **Category:** design-around · **Severity:** high · **Owner:** P4+P5
- **Concerns:** N2; 09 D10; 10 item 5; 11 DA-4; CONFIRMED 12 E5.1 to E5.6.
- **Evidence:** 01 Q6: how the two-rate characteristic is realised is not disclosed. 08 N2: the increment is "strong" on US20080188352A1 [16], [25]. 11 DA-4(b): the purge shoulder meeting the seat ring after the normal stroke may already be the second stage. CONFIRMED 12 E5.4: "Rests on: nothing yet".
- **Risk:** Claiming the two-rate characteristic of the biasing member as the source of the threshold gives up DA-4, which is cheap and plausible, for a distinction 08 rates as obvious. It also invites a written-description objection to "two-rate" as a function with no disclosed structure.
- **Drafting response required:**
  - P5: claim the three-band behaviour (PF-2), not the means that sets the threshold. "A biasing member having a two-rate characteristic" is a dependent claim.
  - P4: describe the two-rate characteristic as §3 item 5 states it (soft first stage for normal opening, stiffer second stage to reach over-travel). Say that the concept requires an over-travel threshold above the opening pressure, which the two-rate biasing member provides in the prototype. Treat E5.1 to E5.6 under PF-4; E5.1 is "probably how the prototype spring is made, though the disclosure does not say".
- **Least narrowing:** no scope given up.

### PF-10 — Claim categories and the sealant limitation decide who infringes

- **Category:** design-around · **Severity:** high · **Owner:** P5
- **Concerns:** claim preambles; N7; 10 items 3 and 7; 02 ranks 2–4.
- **Evidence:** 10 item 7: the valve core is "the likely unit of sale". The same subject matter can be claimed at the valve core, valve and inflatable-body levels. 10 item 3: "Enforcing a method claim against riders is impractical." LOCKED avoid list: "latex only", "bicycle tube only", "floor pump only".
- **Risk:** An apparatus claim whose body requires sealant *in* the inflatable body, or requires an inflation device, is not directly infringed by the maker or seller of a valve core. A method-only lead claim is infringed mainly by end users.
- **Drafting response required:** P5 leads with a claim to the valve, or the valve core, "for an inflatable body" (intended use, so sealant is not a positive limitation). Add independent claims at the valve core level (N7, unit of sale) and the inflatable-body level (OEM supply). Put the purging method as a further independent claim, not the lead. Keep "sealant", "latex", "bicycle", "Presta" and named inflation devices out of the independent claims.
- **Least narrowing:** adds categories; gives up nothing.

### PF-11 — Deflection by the valve member must stay: pressure-deflected resilient seats are in the art

- **Category:** novelty · **Severity:** high · **Owner:** P5
- **Concerns:** N0 "over-travel deflects a deflectable element"; 11 DA-11, DA-14.
- **Evidence:** `refs/US3417778A.md` [15]: a lip "constituting the sole valve seat and being radially expandable under fluid pressure". US11179979B2 [0016]: a lip deformed by the pressure gradient during inflation. 11 DA-14: "the 'deflected by the valve member' clause is what separates N0 from US3417778A and should stay."
- **Risk:** A genus admitting deflection "by the valve member or by the pressure differential" reads on both references.
- **Drafting response required:** P5 keeps deflection caused by the over-travel of the valve member in the independent claim, and accepts DA-14 as an escape rather than close it. For DA-11, P5 may cover deflection "directly or through a part moved by the valve member" only if P4's description has a sentence for it, which needs inventor confirmation under PF-4. Otherwise leave it.
- **Least narrowing:** the recommended wording gives up DA-14, which cannot be closed without reading on the art.

### PF-12 — The drawings have not been seen; the figure plan must come from text alone

- **Category:** formal · **Severity:** high · **Owner:** P4
- **Concerns:** Prompt 20 figure plan, `registry.json`, reference numerals 10 to 70.
- **Evidence:** 01 sources line: "file names and captions only; the images were not supplied and have not been seen". 10 A5: no reference figure seen either. LOCKED keeps the inventor's numerals (10) to (70).
- **Risk:** US 35 U.S.C. §113 requires drawings where necessary to understand the invention. Features shown only in a figure cannot be added after filing without new matter (EPO Art. 123(2); UK s.76). If the purge-gap geometry (PF-1) is drawn from an AI reading, the figures state an invented fact. L4: unregistered numerals reached counsel in a past run.
- **Drafting response required:** P4 plans figures from the captions and §3 only. It keeps the inventor's numerals 10, 20, 30, 40, 42, 44, 50, 60 and 70 for the parts they name, and registers every new numeral (L4; `pc numerals`). In each figure brief, say that the purge-gap region must match the inventor's drawing once supplied. Do not specify a gap topology in any figure until 01 Q1 is answered. Add a request for the drawing files to `disclosure_requests`.
- **Least narrowing:** not a scope question.

### PF-13 — No range has criticality; the over-travel threshold range overlaps US20080188352A1

- **Category:** novelty · **Severity:** medium · **Owner:** P4+P5
- **Concerns:** N8; CONFIRMED 13 Tables A to F.
- **Evidence:** `refs/US20080188352A1.md` [14]: "about 65 psi to about 100 psi (400-700 kPa)". This overlaps the 2.5–5.0 bar threshold range above about 4.5 bar (08 N8). 01 A5: the §4 ranges are the inventor's estimates, and no end was tested. CONFIRMED 13 notes 3 and 4.
- **Risk:** Ranges without shown effect are attacked as arbitrary selections in all three offices. Presenting them as "critical" or "optimal" invites an effect argument the data cannot carry.
- **Drafting response required:**
  - P4: state each §4 range with its prototype value and name each endpoint individually (13 "Endpoints"), for amendment basis. Call the ranges "for example" or "in embodiments", never "critical" or "optimal". Do not state the proposed intermediate or preferred rungs as the inventor's (PF-4).
  - P5: no numeric range in an independent claim. The threshold range in dependent claims only.
- **Least narrowing:** the 2.5–4.5 bar rung avoids the overlap but is AI-proposed (PF-4).

### PF-14 — The superelastic alloy has no isolated evidence of effect

- **Category:** support · **Severity:** medium · **Owner:** P4+P5
- **Concerns:** N6; 09 D8; 10 "considered and not listed" (Af).
- **Evidence:** 08 N6: "material moderate; Af increment strong". 08 Q3 and 09 Q5: the bench test compares whole cores, not NiTi with an elastomer. §6 para 1: the inventor says PEEK gives a "lower snap-back force, so the wiping effect is weaker".
- **Risk:** A dependent claim to the superelastic alloy will draw a "mere material choice" objection, and the description has only the inventor's statement to answer it.
- **Drafting response required:**
  - P4: record the inventor's stated reason for the material (§2 para 2 fast, stiff recovery; §6 para 1 comparison) as a statement, not a result. Describe Af below 5 °C as the specification limit in §4, not a measured value (01 Q20).
  - P5: place N6 below N5 and N3 in the ladder, not above them.
- **Least narrowing:** none needed.

### PF-15 — The purge shoulder must be claimed by function, not position

- **Category:** design-around · **Severity:** medium · **Owner:** P4+P5
- **Concerns:** N3; 09 D4; 10 item 1; 11 DA-11; CONFIRMED 12 E6.5 and E6.6.
- **Evidence:** 07 R10 is absent in all ten charts; this is the rung with no reference against it (10 item 1). 09 D4: "The contact point is easy to move ... the phrase must not require a seat ring." E6.6 notes that a taper continuing past the seating line "blurs the distinction 09 D4 relies on".
- **Risk:** "A purge shoulder below the sealing face" is escaped by E6.5-type contact from below. "Contacts the ring" excludes alternative B.
- **Drafting response required:**
  - P4: define "purge shoulder" (LOCKED marks it for definition) as a portion of the valve member that bears on the deflectable element only during over-travel, with "below the sealing face" as the prototype's position.
  - P5: the N3 dependent claim uses the functional wording and "deflectable element", not "seat ring".
- **Least narrowing:** functional wording gives up nothing that the disclosure supports.

### PF-16 — The recovery wipe's contacting surfaces and direction are not disclosed

- **Category:** enablement · **Severity:** medium · **Owner:** P4+P5
- **Concerns:** N1; 09 D6; 10 item 4; CONFIRMED 12 E12.1 to E12.6.
- **Evidence:** 01 Q7: which surfaces slide, and in which direction, is not known. 09 D6: rated "moderate to high" design-around risk. CONFIRMED 12 E12.1 is itself a "prototype reading".
- **Risk:** A dependent claim specifying a direction or contact line will lack support. One drafted as a pure result ("shears off film") will draw a US result-language objection and an EPO/UK objection that it states a result to be achieved.
- **Drafting response required:**
  - P4: describe the recovery wipe as §2 para 2 does: the deflectable element, as it recovers, slides across the sealing face. Add E12.4's reading (both parts may move) only under PF-4.
  - P5: word N1 structurally ("as the deflectable element recovers it slides across the sealing face of the valve member"), without direction and without "shearing" as a limitation.
- **Least narrowing:** no direction clause.

### PF-17 — Result language and overstatement in the description and claims

- **Category:** formal · **Severity:** medium · **Owner:** P4+P5
- **Concerns:** Summary, advantages and claim clauses on "across the sealant-accumulation surfaces"; the title; the abstract.
- **Evidence:** LOCKED avoid list and note 5 ("self-cleaning", "clog-proof", "every floor pump", "any pump"). 01 (c) and A6. The evidence is n = 3, 40 cycles, one sealant, one temperature (01 (l)).
- **Risk:** Overstated effects become admissions against the patentee in the US and give an EPO/UK opponent a plausibility and sufficiency target. A clause defined by the result ("so that the surfaces are cleaned") is unclear in all three offices.
- **Drafting response required:**
  - P4: report the bench result as run: 3 of 3 prototype valve cores, 40 inflation cycles, no failure against the §8 criterion, and conventional cores failing at cycles 12, 14 and 18. State the conditions and say the test stopped at 40. Use none of the avoid-list terms, including in the title and abstract.
  - P5: locate the purge gap so that purge flow passes "along the sealant-accumulation surfaces" as a structural relation (defined term), not as a cleaning result.
- **Least narrowing:** none.

### PF-18 — The background must use only saved, real references and must not adopt the inventor's characterisation as admitted art

- **Category:** formal · **Severity:** medium · **Owner:** P4
- **Concerns:** Background section.
- **Evidence:** `prior-art/INDEX.md`: ref-01 and ref-02 are "FICTIONAL ... cannot support a novelty position on a real filing". 01 (a): the prior attempts in §1 para 2 (low-adhesion coating, enlarged bore, removable insert) are "the inventor's characterisation, not a prior-art finding". L6: the reference set is thin.
- **Risk:** Citing a fictional reference, or presenting the inventor's generalisations as known art, creates admitted prior art (US) and false statements. The inventor's characterisations can be used against the patentee.
- **Drafting response required:** P4 cites only the eight saved real references, and only for what their saved text says. It describes the problem (sealant drawn into the valve, film cures, leak-down or blockage after about 10 to 20 inflation cycles) as the problem the disclosure addresses, without calling the §1 para 2 attempts "known" or "prior art". Say nothing about the absence of prior art.
- **Least narrowing:** not a scope question.

### PF-19 — Terminology drift, antecedent basis and numerals (lessons L3, L4, L5)

- **Category:** formal · **Severity:** low · **Owner:** P4+P5
- **Concerns:** every drafted file and revision.
- **Evidence:** LOCKED table and avoid list. The inventor's "poppet", "crack pressure", "return spring" and "snap-back wipe" appear in the sources, and "poppet" is on the avoid list. Gate 2 found drift in 12, 13 and 14 that needed `.r1` corrections. L3: 34 antecedent flags on one claim set. L5: drift is worst in revisions.
- **Risk:** Contract violations, and objections for unclear or inconsistent terms.
- **Drafting response required:** Run `pc terms` on every draft and revision, `pc antecedent` on every claim set, and `pc numerals` after every description revision. Use "valve member" throughout. Quote "poppet" only inside a direct quotation of the bench data, if at all.
- **Least narrowing:** none.

### PF-20 — The thermal purge variant: record it, do not claim it

- **Category:** enablement · **Severity:** low · **Owner:** P4+P5
- **Concerns:** 10 item 10; 11 DA-21; CONFIRMED 12 E3.5 and E13.8; 13 Table C row.
- **Evidence:** §6 para 3: the inventor is "not sure this is worth pursuing and [has] no data". 01 Q14 and 03 Q6: how warming opens the purge gap is not described. 11 DA-21: with an Af of 35–40 °C "the purge gap could open in service".
- **Risk:** A claim to the variant would be neither enabled nor supported. Describing it as working states an unknown as fact.
- **Drafting response required:**
  - P4: at most, one paragraph recording the inventor's idea as §6 para 3 states it, including the Af of 35–40 °C and that it has not been tested. It can also be left out if counsel prefers; say which in the response table.
  - P5: no claim.
- **Least narrowing:** not claimed, so no scope at stake.

## Assumptions

- A1. The quick profile has no Debate 1, so `P2/09` stands in for `09r`, and `debate/` is empty. Not blocking.
- A2. `CONFIRMED.md` is the embodiment set P4 drafts from, as Gate 2 records. Its "nothing yet" entries are treated as eligible for the description but not as inventor-conceived (PF-4). Not blocking; counsel decides.
- A3. Findings are measured only against the ten references charted in 07 (eight real, two fictional); the two fictional references are used only as 08 used them. Blocking for PACKAGE until a professional search (L6).
- A4. The findings cite US, EPO and UK provisions by name for orientation only. They are not legal conclusions; counsel applies them. Not blocking.
- A5. `intake/matter.json` records `"fictional_test": true`. The report is written as for a real filing, because that is the behaviour under test. Not blocking.

## Open Questions

- Q1. How does the purge gap open against an interference-fitted seat ring, and against which bore (01 Q1, Q2, Q10)? PF-1 and PF-5 cannot be fully answered without it. Blocks P4, P5 and PACKAGE.
- Q2. Across which two pressures, and under what conditions, are the opening pressure and the over-travel threshold measured, and when during an inflation does over-travel occur (01 Q5)? Blocks P4 and P5 (PF-3).
- Q3. Does purge flow alone, the recovery wipe alone, or only both give the effect (03 Q1)? Blocks P5 (PF-6).
- Q4. Which Gate 2 entries marked "nothing yet" or "needs confirmation" has the inventor conceived (PF-4)? Blocks PACKAGE.
- Q5. Can the drawing files for FIG-1 and FIG-2 be supplied (PF-12)? Blocks P4.
- Q6. Has there been any public disclosure, sale or offer before filing (01 Q24)? US and EP/GB grace-period rules differ. Blocks PACKAGE.

```json
{
  "prompt": "x-predraft-risk",
  "status": "complete",
  "findings": [
    {"id": "PF-1", "category": "enablement", "severity": "critical", "title": "Purge-gap mechanism not described in a way a skilled person can carry out", "concerns": "N0 purge gap; 09 D1; 10 item 6; N4; N8 purge gap width", "evidence": "01 (b), M1; 03 enablement flag; CONFIRMED 13 ladder note 1; CONFIRMED 12 E10 preface and E10.1-E10.5 'nothing yet'", "risk": "Interference fit of about 0.03 mm and a 0.15 mm gap opened by outward expansion against the same bore are contradictory; sufficiency and enablement (35 USC 112(a), Art. 83 EPC, s.14(3) PA 1977) judged on the filed text", "drafting_response": "P5: define the purge gap functionally in independent claims (separate from main flow passage, purge flow prevented in rest state, opened by deflection); no location, direction, fit or width in independent claims. P4: functional definitions of purge gap and rest state; do not reproduce the section 2/section 3 contradiction; E10 topologies only as flagged alternatives; disclosure request for 01 Q1, Q2, Q10 as a filing blocker", "owner": "P4+P5"},
    {"id": "PF-2", "category": "novelty", "severity": "critical", "title": "Over-travel must be anchored or US11179979B2 anticipates N0", "concerns": "N0 over-travel clauses; 09 D2; definitions of normal stroke, over-travel, over-travel threshold", "evidence": "US11179979B2 [0016] lip deformed by pressure to open slit when inflating; [0101]; 08 Objection 1; 08 A8; US20080188352A1 [26]", "risk": "Without same valve member, travel beyond normal stroke, threshold higher than opening pressure and deflection by that over-travel, the pressure-deformed lip reads on N0", "drafting_response": "P5: independent claim recites normal stroke above opening pressure and over-travel beyond it above a higher over-travel threshold, the over-travel of the valve member deflecting the deflectable element; keep 'relative to the valve seat' as fallback only. P4: non-circular joint definitions of normal stroke, over-travel, opening pressure, over-travel threshold; state no deflection during normal stroke; describe the three pressure bands", "owner": "P4+P5"},
    {"id": "PF-3", "category": "formal", "severity": "critical", "title": "Over-travel threshold has no measuring condition; 3.5 bar is below 6 bar test pressure", "concerns": "pressure differential, opening pressure, over-travel threshold; N8; CONFIRMED 13 Table B", "evidence": "LOCKED pressure differential definition; 01 A3, M5, A6; bench notes (snap on pump-head removal); CONFIRMED 13 ladder note 2; CONFIRMED 15 FM-7", "risk": "Indefiniteness (35 USC 112(b)) and unclear parameter (Art. 84 EPC, s.14(5) PA 1977); sufficiency attack on whether ordinary inflation produces the differential", "drafting_response": "P4: state the threshold as the locked differential; do not invent a test procedure; disclosure request for 01 Q5; describe timing only as the bench notes record it. P5: claim the threshold relationally (higher than the opening pressure); numbers only in dependent claims", "owner": "P4+P5"},
    {"id": "PF-4", "category": "support", "severity": "high", "title": "Auto-confirmed AI proposals must not be drafted or claimed as the inventor's conception", "concerns": "CONFIRMED.md entries marked 'nothing yet', 'proposed, needs confirmation', 'candidate - needs confirmation'; 11 DA closing genera", "evidence": "gates/gate-2.md (no human reviewed); CONFIRMED 15 note 1; USER.md directive on factual gaps", "risk": "Description states unconceived content as the invention; US inventorship question for claims resting only on AI-generated features; exposure at declaration or opposition", "drafting_response": "P4: draft 'Rests on: section' entries as embodiments; list each 'nothing yet' entry by id in the response table as included-as-alternative or omitted; never call such an entry built, tested, preferred or prototype; label Table E ratios as arithmetic or omit. P5: no independent claim may depend on such an entry; dependent claims resting on them flagged for counsel", "owner": "P4+P5"},
    {"id": "PF-5", "category": "support", "severity": "high", "title": "'Separate from the main flow passage' carries novelty but has little disclosure", "concerns": "09 D1, D3; N0 purge flow; main flow passage and purge flow definitions", "evidence": "07 US11179979B2 R5 absent; 08 'What the attack shows' item 1; 01 Q2, M2; FIG-2 caption only (image not seen); CONFIRMED 12 E11.1", "risk": "Unsupported 'separate' cannot be relied on; fallback would rest on D2 alone", "drafting_response": "P4: state that purge flow passes through the purge gap in addition to, not through, the main flow passage, citing section 2 para 1 and FIG-2 caption; E11 paths only under PF-4. P5: keep the clause in the independent claim, mapped in support-map.json; no inlet/outlet structure in independent claims", "owner": "P4+P5"},
    {"id": "PF-6", "category": "support", "severity": "high", "title": "Nucleus choice (purge flow vs recovery wipe) unresolved and unseparated by evidence", "concerns": "N0 vs N0-W; 09 D5; 10 items 3-4; 11 DA-1, DA-16", "evidence": "03 Q1; 08 Q2; 01 (l); bench notes (film in purge-gap region, sealing edge and valve member face clean); 08 N0-W rated moderate to strong", "risk": "EPO effect not credible across claim scope for purge-only embodiments; purge-only nucleus may be claimed on the weaker ground", "drafting_response": "P4: present both actions with separate effect statements as section 2 para 2 does; do not claim either alone is sufficient. P5: N0 independent, recovery wipe first dependent, plus an N0-W-based alternative independent or formulation; record in open_disagreements", "owner": "P4+P5"},
    {"id": "PF-7", "category": "novelty", "severity": "high", "title": "Inventive step against the three-document mosaic depends on problem and effect framing", "concerns": "Background, Summary, technical-effect passages; 08 Objection 2", "evidence": "08 Objection 2 (US11338632B2 [0004] + US20080188352A1 [26] + US3570510A [26]); US3570510A [22] separate gas store; 09 D3, D5; 08 A2, A3", "risk": "Framing the problem as generic seat cleaning and the solution as flushing plus two-stage valve writes the combination for the examiner", "drafting_response": "P4: frame the effect around one deflection event using the inflation gas itself through a gap existing only during over-travel, no stored gas or added valve, conventional behaviour below the threshold; do not concede flushing or two-stage springs as well known", "owner": "P4"},
    {"id": "PF-8", "category": "design-around", "severity": "high", "title": "Seat ring, convoluted wall, superelastic alloy and Af stay out of independent claims", "concerns": "N4, N5, N6, N6-A, N4-B; 09 D7, D8; 11 DA-2, DA-3, DA-5, DA-10, DA-18", "evidence": "11 findings on preferred vs essential; section 6 paras 1-2; 08 Af increment strong on US6053992A [3]", "risk": "Inventor's own alternative B (DA-2) escapes any independent claim reciting these", "drafting_response": "P5: 'deflectable element' and 'valve seat' as distinct terms in independent claims; seat ring, wiper ring, convoluted wall, superelastic alloy in dependent claims with N5 early; consider a material-neutral seat ring article claim flagged for counsel", "owner": "P5"},
    {"id": "PF-9", "category": "design-around", "severity": "high", "title": "Two-rate biasing member must not carry the over-travel threshold in independent claims", "concerns": "N2; 09 D10; 10 item 5; 11 DA-4; CONFIRMED 12 E5.1-E5.6", "evidence": "01 Q6; 08 N2 increment strong on US20080188352A1 [16], [25]; 11 DA-4(b); E5.4 'nothing yet'", "risk": "Gives up cheap design-around DA-4 for an obvious increment; functional term without disclosed structure", "drafting_response": "P5: claim the three-band behaviour, not the means; two-rate characteristic as a dependent claim. P4: describe section 3 item 5 as stated and that the concept requires a threshold above the opening pressure; E5 entries under PF-4", "owner": "P4+P5"},
    {"id": "PF-10", "category": "design-around", "severity": "high", "title": "Claim categories and the sealant limitation decide who infringes", "concerns": "claim preambles; N7; 10 items 3, 7; 02 ranks 2-4", "evidence": "10 item 7 (valve core is unit of sale); 10 item 3 (method claims against riders impractical); LOCKED avoid list", "risk": "Apparatus claims requiring sealant or an inflation device are not directly infringed by valve core makers; method-led set enforceable mainly against end users", "drafting_response": "P5: lead with valve or valve core 'for an inflatable body'; independent claims at valve core and inflatable-body levels; purging method as a further independent claim; keep sealant, latex, bicycle, Presta and named inflation devices out of independent claims", "owner": "P5"},
    {"id": "PF-11", "category": "novelty", "severity": "high", "title": "Deflection by the valve member must stay; pressure-deflected resilient seats are in the art", "concerns": "N0 deflection clause; 11 DA-11, DA-14", "evidence": "US3417778A [15] lip radially expandable under fluid pressure; US11179979B2 [0016]; 11 DA-14 finding", "risk": "A genus admitting pressure-driven deflection reads on both references", "drafting_response": "P5: keep deflection caused by over-travel of the valve member in the independent claim; accept DA-14 as an escape; cover DA-11 (through a part moved by the valve member) only if P4 has inventor-confirmed support", "owner": "P5"},
    {"id": "PF-12", "category": "formal", "severity": "high", "title": "Drawings not seen; figure plan must come from text alone", "concerns": "Prompt 20 figure plan; registry.json; numerals 10-70", "evidence": "01 sources line (images not supplied); 10 A5; LOCKED numerals; lesson L4", "risk": "35 USC 113; figure-only features cannot be added later (Art. 123(2) EPC, s.76 PA 1977); an AI-drawn purge-gap topology states an invented fact", "drafting_response": "P4: plan figures from captions and section 3 only; keep inventor numerals; register every new numeral and run pc numerals; no purge-gap topology in any figure until 01 Q1 is answered; disclosure request for the drawing files", "owner": "P4"},
    {"id": "PF-13", "category": "novelty", "severity": "medium", "title": "No range has criticality; over-travel threshold range overlaps US20080188352A1", "concerns": "N8; CONFIRMED 13 Tables A-F", "evidence": "US20080188352A1 [14] 400-700 kPa; 08 N8; 01 A5; CONFIRMED 13 notes 3-4", "risk": "Arbitrary-selection objection; claiming criticality invites an effect argument the data cannot carry", "drafting_response": "P4: state section 4 ranges with prototype values and individually named endpoints, as examples, never critical or optimal; proposed rungs not as the inventor's. P5: no numeric range in independent claims", "owner": "P4+P5"},
    {"id": "PF-14", "category": "support", "severity": "medium", "title": "Superelastic alloy has no isolated evidence of effect", "concerns": "N6; 09 D8", "evidence": "08 N6; 08 Q3; 09 Q5; section 6 para 1", "risk": "Mere-material-choice objection answered only by the inventor's statement", "drafting_response": "P4: record the inventor's stated reason as a statement; Af below 5 C as a specification limit, not measured. P5: N6 below N5 and N3 in the ladder", "owner": "P4+P5"},
    {"id": "PF-15", "category": "design-around", "severity": "medium", "title": "Purge shoulder must be claimed by function, not position", "concerns": "N3; 09 D4; 10 item 1; 11 DA-11; CONFIRMED 12 E6.5, E6.6", "evidence": "07 R10 absent in all charts; 09 D4 design-around note", "risk": "'Below the sealing face' is escaped by contact from below; 'contacts the ring' excludes alternative B", "drafting_response": "P4: define purge shoulder as a portion of the valve member bearing on the deflectable element only during over-travel, position as prototype detail. P5: N3 dependent uses the functional wording and 'deflectable element'", "owner": "P4+P5"},
    {"id": "PF-16", "category": "enablement", "severity": "medium", "title": "Recovery wipe contacting surfaces and direction not disclosed", "concerns": "N1; 09 D6; 10 item 4; CONFIRMED 12 E12", "evidence": "01 Q7; 09 D6; E12.1 is a prototype reading", "risk": "Direction-specific claims unsupported; result-only wording unclear", "drafting_response": "P4: describe the wipe as section 2 para 2 does; E12.4 only under PF-4. P5: structural N1 wording without direction and without 'shearing' as a limitation", "owner": "P4+P5"},
    {"id": "PF-17", "category": "formal", "severity": "medium", "title": "Result language and overstatement in description and claims", "concerns": "Summary, advantages, title, abstract; purge flow clause", "evidence": "LOCKED avoid list and note 5; 01 (c), A6, (l)", "risk": "Overstated effects become admissions and plausibility targets; result-defined clauses are unclear", "drafting_response": "P4: report the bench result as run (3 of 3, 40 cycles, stopped at 40, conditions stated); no avoid-list terms anywhere. P5: purge flow along the sealant-accumulation surfaces as a structural relation, not a cleaning result", "owner": "P4+P5"},
    {"id": "PF-18", "category": "formal", "severity": "medium", "title": "Background must cite only saved real references and not adopt the inventor's characterisation as admitted art", "concerns": "Background section", "evidence": "prior-art/INDEX.md (ref-01, ref-02 fictional); 01 (a) on section 1 para 2; lesson L6", "risk": "Citing fictional references or inventor generalisations creates admitted prior art and false statements", "drafting_response": "P4: cite only the eight saved real references for what their text says; describe the problem without calling the section 1 para 2 attempts known art; say nothing about absence of prior art", "owner": "P4"},
    {"id": "PF-19", "category": "formal", "severity": "low", "title": "Terminology drift, antecedent basis and numerals", "concerns": "all drafts and revisions", "evidence": "LOCKED table and avoid list; gate-2.md .r1 corrections; lessons L3, L4, L5", "risk": "Contract violations; unclear or inconsistent terms", "drafting_response": "Run pc terms on every draft and revision, pc antecedent on every claim set, pc numerals after every description revision; 'valve member' throughout, never 'poppet' outside a quotation", "owner": "P4+P5"},
    {"id": "PF-20", "category": "enablement", "severity": "low", "title": "Thermal purge variant: record, do not claim", "concerns": "10 item 10; 11 DA-21; CONFIRMED 12 E3.5, E13.8; 13 Table C", "evidence": "section 6 para 3 (no data, inventor unsure); 01 Q14; 03 Q6; 11 DA-21", "risk": "Neither enabled nor supported; describing it as working states an unknown as fact", "drafting_response": "P4: at most one paragraph recording the idea as section 6 para 3 states it, untested, or omit and say so in the response table. P5: no claim", "owner": "P4+P5"}
  ],
  "assumptions": [
    {"id": "A1", "text": "Quick profile: no Debate 1, so P2/09 stands in for 09r; debate/ is empty.", "blocking": false},
    {"id": "A2", "text": "CONFIRMED.md is the drafting set; its 'nothing yet' entries are eligible but not inventor-conceived (PF-4).", "blocking": false},
    {"id": "A3", "text": "Findings are measured only against the ten references charted in 07; professional search still needed.", "blocking": true},
    {"id": "A4", "text": "Statutory provisions are named for orientation only; counsel applies them.", "blocking": false},
    {"id": "A5", "text": "matter.json marks the matter as a fictional test; the report is written as for a real filing.", "blocking": false}
  ],
  "open_questions": [
    {"id": "Q1", "text": "How does the purge gap open against an interference-fitted seat ring, and against which bore (01 Q1, Q2, Q10)?", "blocks": ["P4", "P5", "PACKAGE"]},
    {"id": "Q2", "text": "Across which pressures and under what conditions are the opening pressure and over-travel threshold measured; when does over-travel occur (01 Q5)?", "blocks": ["P4", "P5"]},
    {"id": "Q3", "text": "Does purge flow alone, the recovery wipe alone, or only both give the effect (03 Q1)?", "blocks": ["P5"]},
    {"id": "Q4", "text": "Which Gate 2 entries marked 'nothing yet' or 'needs confirmation' has the inventor conceived?", "blocks": ["PACKAGE"]},
    {"id": "Q5", "text": "Can the FIG-1 and FIG-2 drawing files be supplied?", "blocks": ["P4"]},
    {"id": "Q6", "text": "Any public disclosure, sale or offer before filing (01 Q24)?", "blocks": ["PACKAGE"]}
  ]
}
```
