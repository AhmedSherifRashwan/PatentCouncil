# Self-purging bicycle tube valve — review round 1

| Area | Critical | High | Medium | Low | Total |
|---|---|---|---|---|---|
| design-around and detectability | 0 | 1 | 6 | 2 | 9 |
| enablement and written description | 2 | 9 | 8 | 2 | 21 |
| formal and consistency | 0 | 2 | 11 | 14 | 27 |
| novelty and inventive step | 0 | 0 | 2 | 2 | 4 |
| support, priority and amendment basis | 0 | 5 | 9 | 3 | 17 |
| **All areas** | **2** | **17** | **36** | **23** | **78** |

**Adjudication.** Every critical and high finding was checked against the text by the Adjudicator after the owning drafter's rebuttal: not adjudicated 57, rejected 11, upheld 10. Only upheld findings (and unclear critical ones) were sent back for revision; every finding is reported.

## Critical findings (2)

#### F-30-1 — Purge gap of the first embodiment cannot open by radial expansion, and has no outlet

**Severity** critical · **Area** enablement and written description · **Claims** 16, 17, 40, 41, 15 · **Specification** [0031], [0035], [0068], [0109], [0111], Fig. 2

**Raised by** ip-reviewer (review step 30)

**The objection.** Claim 16 'opens when the seat ring expands' and claim 17 'the radial expansion opening the purge gap' place the gap between the outer surface 38 and the core bore 22, while the seat ring is interference-fitted in that bore ([0035]). Radial expansion moves the outer surface towards the bore and closes, not opens, the gap; no path from the lower end of the gap past the locating shoulder 24 into the inflatable body is described. Not enabled under US 112(a), EPC Art 83, UK s.14(3).

**Least narrowing fix.** Add the inventors' actual gap geometry (separating surfaces, direction, outlet path) to the description and FIG. 1/2 from their sketches; only if unavailable, delete or recast claims 16, 17, 40, 41.  
*This fix needs disclosure the application does not yet contain.*


**Ruling** upheld — Correct on the text; lead finding for this defect. [0031], claims 16 and 40 place the purge gap 60 'between the outer surface 38 of the seat ring 30 and the core bore 22' and say it 'opens when the seat ring 30 expands'; claims 17 and 41 say 'the radial expansion opening the purge gap'. [0035], [0068], [0109] and claim 15 hold the same ring in the same bore by an interference fit of approximately 0.03 mm on diameter, and [0084] defines 'outward' as radially away from the axis. Outward expansion of the outer surface reduces, and cannot open, a gap between that surface and the bore, and the text nowhere says where the fit acts or which surfaces separate. No path from the gap past the locating shoulder 24 into the inflatable body is described ([0046] says only that the gap 'may communicate at its ends'), and registry.md FIG. 2 instructs 'draw no inlet or outlet feature'. The review package's own figure plan (figures.md, second paragraph) records that 'the disclosure does not explain how the purge gap opens'. [0103] (cured sealant on the outer surface 38 'in the region of the purge gap') shows the prototype had a gap there, but not how it opened. Claims 16, 17, 40 and 41 recite a mechanism the skilled person cannot build as described (s.112(a), Art. 83, UK s.14(3)), so critical is right for those claims. Correction also reaches claim 9 and [0048], [0066] and [0126] (radial measurement of the purge gap width) once the inventors state the actual geometry.

#### F-32-1 — Radial expansion of an interference-fitted seat ring cannot open a gap against its own bore, and the gap has no outlet

**Severity** critical · **Area** enablement and written description · **Claims** 16, 17, 40, 41 · **Specification** [0031], [0035], [0109], [0111]

**Raised by** ip-reviewer (review step 32)

**The objection.** Claim 16 'opens when the seat ring expands' and claim 17 'the radial expansion opening the purge gap (60)' place the gap between the outer surface 38 and the core bore 22 in which the seat ring is interference-fitted ([0035]); expansion drives the surface into the bore and closes the gap, and no outlet past the locating shoulder 24 to the inflatable body is described.

**Least narrowing fix.** Add the prototype's actual gap geometry and outlet path from the inventors' sketches or records, and draw it; delete or recast only if unavailable.  
*This fix needs disclosure the application does not yet contain.*


**Ruling** rejected — Duplicates F-30-1: the same quotation of claims 16 and 17, the same interference fit ([0035]) and the same missing outlet past the locating shoulder 24. Upheld there as critical.

## High findings (17)

#### F-33-2 — Purge gap limited to a second parallel path; enlarging the seat gap on over-travel avoids claims 1, 2 and 4

**Severity** high · **Area** design-around and detectability · **Claims** 1, 2, 4 · **Specification** [0011], [0034], [0034a], [0046], [0055], [0117]

**Raised by** ip-reviewer (review step 33)

**The objection.** Claims 1 and 2 require 'a purge gap (60), which is a second path for inflation gas ... in parallel with the main flow passage' and [0046] says purge gas 'does not pass between the sealing face and the valve seat'. A core whose over-travel flexes the seat element to widen the seat annulus, and which wipes the sealing face on recovery, has no second path and avoids every independent claim while keeping both cleaning actions of [0010]. The recovery wipe is claimed only in dependent claims hanging on the purge gap.

**Least narrowing fix.** Add an independent valve and valve-core claim to the recovery-wipe aspect of [0011] (normal stroke, over-travel above a higher threshold deflecting the deflectable element, and recovery with the deflectable element sliding across the sealing face), with no purge-gap limitation; supported by [0011], [0034], [0034a], [0055], [0117]. A new claim, not a narrowing; counsel to weigh proximity to US4050473A and US4236547A.


**Ruling** upheld — Correct on the text. [0011] expressly provides an aspect 'founded on the recovery wipe' that 'may be combined with the purge gap', and [0055] and [0117] support it, but the only claims to the recovery wipe (claims 5, 35, 52, 57, 59) hang from claims 1, 2 and 4, each of which requires a purge gap that is 'a second path ... in parallel with the main flow passage' ([0046]: gas that 'does not pass between the sealing face and the valve seat'). A valve whose over-travel deflects the seat element to widen the seat annulus and which wipes on recovery falls outside every independent claim, although the description supports claiming it. The remedy is a new independent claim family, needs no new disclosure, and is a drafting choice within the Claims Architect's lane. Counsel must weigh it against US4050473A and US4236547A (a flexible disc or cutting edge on the valve head acting on the seat on closing; [0006] of the description) and US3417778A (resilient seat lip radially expanded by the valve body, [4], [15]), which press harder on a claim without the purge gap.

#### F-28-3 — The first embodiment's stated geometry cannot perform the claimed over-travel

**Severity** high · **Area** enablement and written description · **Claims** 1, 2, 4, 7, 14, 17, 39, 41, 53, 57, 59 · **Specification** [0029], [0030], [0034a], [0039], [0054], [0084], [0111], Fig. 1, Fig. 2

**Raised by** ip-reviewer (review step 28)

**The objection.** With upper defined as towards the inflation device ([0084]), the sealing face seating on the upper edge 32 ([0030]) and the purge shoulder below the sealing face ([0029]) bearing on that upper edge during over-travel ([0111] step 706), the shoulder can reach the edge only by moving upwards against the pressure differential, and its load would then lift the ring off the locating shoulder rather than compress it. The direction of the normal stroke is stated nowhere, so the only built embodiment is not enabled on the text (Art. 83, s.112(a), UK s.14(3)), and claims 7, 14, 17, 39 and 41 recite the arrangement itself.

**Least narrowing fix.** Add the inventors' statement of the actual arrangement (direction of the stroke, the side of the seat ring the sealing face seals on, the position of the purge shoulder and the direction of the load), align [0029], [0030], [0054], [0084], [0111] and the FIG. 1 and FIG. 2 instructions, and reword claims 7, 14 and 17 to match without narrowing.  
*This fix needs disclosure the application does not yet contain.*


**Ruling** upheld — Correct on the text. [0084] fixes 'upper'/'below' by the inflation-device end and the inflatable body. The pressure differential is positive from the inflation-device side ([0039]), so the normal stroke and over-travel are towards the inflatable body ([0043]: over-travel is 'in the direction of the normal stroke'). [0030] and [0111] have the sealing face 42 seal on, and lift from, the upper edge 32; [0029] and claim 7 put the purge shoulder 44 'below the sealing face 42'; [0111] step 706 and [0034a] have that shoulder bear on the upper edge 32 during over-travel with 'an axial load'. A shoulder below the sealing face moves further from the upper edge as the valve member moves towards the inflatable body, so these statements cannot all hold. The functional definitions in [0054] and [0119] and the 'schematic' disclaimers in [0026] and [0091] do not say which statement is wrong, so the error is not one the skilled person could correct unambiguously, and correction after filing (Rule 139 EPC) would not be available. The combination claim 7 -> 12 -> 14 -> 17 recites the inconsistent arrangement: an Art. 84/s.112(b) objection and an Art. 83/s.112(a) attack on the only built embodiment. The reviewer's further point that the load would lift the ring off the locating shoulder 24 is not established, because the text does not say on which side of the ring the shoulder 24 lies ([0028]). Lead finding for F-29-3 and F-32-3.

#### F-28-4 — The purge gap cannot open where claims 16 and 40 put it, and its outlet is not described

**Severity** high · **Area** enablement and written description · **Claims** 1, 9, 15, 16, 17, 40, 41 · **Specification** [0028], [0031], [0035], [0046], [0048], [0068], [0126]

**Raised by** ip-reviewer (review step 28)

**The objection.** The purge gap is said to lie between the outer surface 38 and the core bore 22 and to open when the seat ring expands outward ([0031], [0048]), yet the ring is held in that bore by an interference fit ([0035]); outward expansion of a ring in a bore closes a gap on its outer surface and cannot open one. No passage is described by which purge flow leaves the gap past the locating shoulder 24 into the inflatable body ([0046] says only 'may communicate'). Claim 16, through claim 15, recites the contradictory combination itself.

**Least narrowing fix.** Add the inventors' statement of where the interference fit acts and where the outer surface is in clearance, which surfaces separate when the gap opens, and the passage past the locating shoulder; correct [0031], [0048], [0126] and claims 9, 16 and 40 if the gap actually opens by inward movement or at the upper edge.  
*This fix needs disclosure the application does not yet contain.*


**Ruling** rejected — Duplicates F-30-1 (same defect: [0031] purge gap between outer surface 38 and core bore 22 opening 'when the seat ring 30 expands', against the interference fit of [0035], and no outlet past the locating shoulder 24, [0046] 'may communicate'). F-30-1 is upheld as the lead; the corrections this finding names for claim 9, [0048] and [0126] are carried in that ruling.

#### F-29-1 — Path 5 has no coherent purge gap mechanism to amend into

**Severity** high · **Area** enablement and written description · **Claims** 15, 16, 17, 40, 41 · **Specification** [0031], [0035], [0048]

**Raised by** ip-reviewer (review step 29)

**The objection.** The seat ring is interference-fitted in the core bore, so its outward expansion cannot open a gap on its outer surface, and no outlet past the locating shoulder 24 is described; the most distinctive structural fallback cannot be relied on as filed.

**Least narrowing fix.** Before filing, add the inventors' statement of where the interference fit acts, which surfaces separate, and the passage by which purge flow reaches the inflatable body.  
*This fix needs disclosure the application does not yet contain.*


**Ruling** rejected — Duplicates F-30-1: the same interference-fit and missing-outlet defect in [0031], [0035] and [0048], stated as its effect on amendment path 5 (claims 15 to 17, 40, 41). Resolved by the F-30-1 correction.

#### F-29-3 — Paths 2, 4, 5 and 8 have no coherent geometry to amend into

**Severity** high · **Area** enablement and written description · **Claims** 6, 7, 14, 17, 39, 41 · **Specification** [0029], [0030], [0054], [0084], [0111]

**Raised by** ip-reviewer (review step 29)

**The objection.** On the orientation of [0084], a purge shoulder below a sealing face that seals on the upper edge cannot bear on that upper edge by travel away from the seat under a pressure differential from the upper side, so every fallback built on the first embodiment inherits an Art. 83 and Art. 84 objection that cannot be cured after filing.

**Least narrowing fix.** Before filing, add the inventors' statement of the stroke direction, the side on which the sealing face seals, and where and in which direction the purge shoulder loads the seat ring; align [0029], [0030], [0054], [0111] and the FIG. 1 and FIG. 2 instructions.  
*This fix needs disclosure the application does not yet contain.*


**Ruling** rejected — Duplicates F-28-3: the same inconsistency between [0084], [0029], [0030] and [0111] step 706 on the direction of the stroke and the position of the purge shoulder 44, stated as its effect on amendment paths 2, 4, 5 and 8. Resolved by the F-28-3 correction.

#### F-30-2 — Genus claims 1, 2 and 4 rest on a mechanism not coherently disclosed in any embodiment

**Severity** high · **Area** enablement and written description · **Claims** 1, 2, 4 · **Specification** [0116], [0094], [0094a], [0031], [0026], [0093]

**Raised by** ip-reviewer (review steps 30, 32)

**The objection.** Claim 1 covers any 'deflectable element' opening any 'purge gap'; [0116] calls the principle 'of general application', yet the first embodiment's gap cannot open as described and the wiper ring embodiment's gap position, mounting and thickness are 'not stated'. Full-scope enablement (Amgen v Sanofi; Regeneron v Kymab; EPC Art 83/84) is exposed.

**Least narrowing fix.** Supply the missing gap disclosure for the first embodiment and at least one stated gap topology for the wiper ring; narrowing claim 1 to a stated topology only as a fallback, for the human to decide.  
*This fix needs disclosure the application does not yet contain.*


**Ruling** upheld — Correct on the text. Claims 1, 2 and 4 claim any deflectable element whose deflection opens a parallel purge gap ([0116]: the principle is 'of general application'). The only embodiments offered are the seat ring 30 of the first and second embodiments, whose gap mechanism is incoherent as written (F-30-1: [0031] against [0035]), and the wiper ring 130, whose gap position, mounting and thickness are 'not stated herein' ([0094], [0094a]) and whose stated position is below the seat (F-28-1). [0026] and [0046] disclaim any particular position, so the description gives no coherent example of the feature that defines the genus. This is a credible support/sufficiency and written-description objection to the independent claims (Art. 83, Art. 84; s.112(a); UK s.14(3), s.14(5)(c)). It is high rather than critical because the art is simple mechanics and the functional teaching of [0046] and [0048] gives an examiner less purchase than in the unpredictable arts of the cited cases, and because curing F-30-1 alone would supply one coherent way. Its resolution follows from F-30-1 and F-28-1.

#### F-32-3 — The directions of seat, sealing face, purge shoulder and spring cannot all be true at once

**Severity** high · **Area** enablement and written description · **Claims** 7, 14, 17, 39, 41 · **Specification** [0029], [0030], [0033], [0084], [0111]

**Raised by** ip-reviewer (review step 32)

**The objection.** With 'upper' towards the inflation device ([0084]), a valve member opening downward cannot lift from an upward-facing 'upper edge (32)' seat; a spring 'acting under the valve member' ([0033]) pushes it away from such a seat; and a purge shoulder 'below the sealing face' moves away from, not onto, the upper edge during further travel. The first embodiment cannot be reconstructed.

**Least narrowing fix.** Correct the orientation words to the inventors' actual construction and state the direction of the normal stroke relative to the upper edge; claims 7, 14, 17, 39, 41 follow.  
*This fix needs disclosure the application does not yet contain.*


**Ruling** rejected — Duplicates F-28-3 on its sound part: the purge shoulder 44 'below the sealing face' ([0029]) cannot reach the upper edge 32 by further travel towards the inflatable body ([0084], [0111]). Its other two premises do not follow from the text. 'Upper edge (32)' does not say the seating surface faces upwards: a conical sealing face 42 can seal on the inner arris of the upper edge from below. On that reading a spring 'acting under the valve member' ([0033]) urges the valve member onto the seat, as a spring must, and does not push it away.

#### F-32-4 — The wiper-ring purge gap lies below the rigid valve seat, so it is in series with the main flow passage, not in parallel

**Severity** high · **Area** enablement and written description · **Claims** 27, 28, 29, 45, 58, 60 · **Specification** [0046], [0094], [0094a], Fig. 3

**Raised by** ip-reviewer (review step 32)

**The objection.** Claim 28 'positioned below the rigid valve seat (132), towards the inflatable body' means gas reaching the wiper-ring gap has already passed between the sealing face and the rigid seat, i.e. in series, which [0046] excludes from 'purge gap'; no bypass is described.

**Least narrowing fix.** Add a described purge gap inlet that bypasses the rigid valve seat if conceived; otherwise delete the wiper-ring claims or reframe that embodiment on the recovery wipe alone.  
*This fix needs disclosure the application does not yet contain.*


**Ruling** rejected — Duplicates F-28-1: the same quotation of claim 28 ('positioned below the rigid valve seat (132), towards the inflatable body') against [0046], and the same absence of a described bypass ([0094], [0094a]). Upheld there.

#### F-36-2 — The first embodiment's purge gap opens "when the seat ring 30 expands" into the bore that holds it by interference

**Severity** high · **Area** enablement and written description · **Claims** 1, 2, 16, 40 · **Specification** [0031], [0035], [0111], [0026], [0046]

**Raised by** ip-reviewer (review step 36)

**The objection.** [0031] and claims 16 and 40 say the purge gap 'is formed between the outer surface 38 of the seat ring 30 and the core bore 22 ... and opens when the seat ring 30 expands', while [0035] holds the seat ring in that bore by an interference fit. Outward radial expansion drives the outer surface into the bore; the text does not say how a gap opens between them, where the fit acts, or how gas enters and leaves the gap. The only built embodiment's mechanism is not taught: insufficiency (Art. 83, s.14(3)) and enablement (112(a)) exposure.

**Least narrowing fix.** Add the inventors' description of the first embodiment's purge-gap geometry: the region held by the interference fit, the region forming the purge gap, which surface moves from which in over-travel, and the gas path in and out, with the sketch. Correct claims 16 and 40 only if the added text shows a different location.  
*This fix needs disclosure the application does not yet contain.*


**Ruling** rejected — Duplicates F-30-1: the same quotation of [0031] and claims 16 and 40 against the interference fit of [0035], and the same missing gas path in and out. Upheld there as critical.

#### F-38-1 — Example 1 is internally impossible as written (test dates and C-2 failure row)

**Severity** high · **Area** enablement and written description · **Claims** — · **Specification** [0099], [0100], [0101], [0102], [0129], [0132a]

**Raised by** ip-reviewer (review step 38)

**The objection.** [0099] states forty inflation cycles each with 'a hold of 24 hours', yet 'The test ran from 2026-08-12 to 2026-08-20' (eight days for at least forty days of holds). Table 1 row C-2 records 0.7 bar leak-down at last measured cycle 11 but failure at cycle 12, against the 0.5 bar criterion of [0100]. The only actual example is impeachable, and the error is not correctable after filing because the correct values are not derivable from the text (EPC Rule 139).

**Least narrowing fix.** Obtain the actual test record from the inventor and correct the dates or hold duration in [0099], [0100] and [0059], and the C-2 row and column headings of Table 1. No claim change.  
*This fix needs disclosure the application does not yet contain.*


**Ruling** upheld — Correct on the text, and it needs the inventors' record. [0099] and [0059] define each inflation cycle as including 'a hold of 24 hours'; [0102] and Table 1 report forty cycles for P-1 to P-3; yet [0099] states 'The test ran from 2026-08-12 to 2026-08-20', about eight days. Running the six cores in parallel does not help, because each core needs at least forty days of holds. In Table 1, C-2 shows 'Leak-down at last measured cycle' of 0.7 bar at last measured cycle 11, above the 0.5 bar criterion of [0060] and [0100], yet first failure at cycle 12. C-1 and C-3 (failure at 14 and 18, last measured 13 and 17) show that 'last measured cycle' is the cycle before failure, so the C-2 row contradicts itself. This is the only actual example ([0098]), relied on in [0017], [0129] and [0132a]. Filing inconsistent test data engages the duty of candour (37 CFR 1.56) and invites an impeachment attack. The correct values cannot be derived from the text, so Rule 139 EPC correction would not be available after filing. No claim change, but the fix must come from the inventor before filing.

#### F-30-3 — No drawings; the figure files are drafting instructions carrying internal references and damaging statements

**Severity** high · **Area** formal and consistency · **Claims** — · **Specification** [0018], [0025], figures.md, registry.md

**Raised by** ip-reviewer (review steps 30, 32)

**The objection.** The description refers to FIG. 1 to FIG. 8 but the package holds only a figure plan citing CONFIRMED.md, P1/01 and PF-1 and stating 'the disclosure does not explain how the purge gap opens', plus drawing instructions with draftsperson's notes. Missing drawings engage 35 USC 113, Rule 56 EPC and UK s.15; the statement is a sufficiency admission if filed.

**Least narrowing fix.** Produce drawing sheets for FIG. 1 to FIG. 8, matching FIG. 1 to FIG. 3 to the inventors' sketches, and keep the plan and instructions out of anything filed.  
*This fix needs disclosure the application does not yet contain.*


**Ruling** upheld — Correct on the text. [0018] to [0025] describe FIG. 1 to FIG. 8, but the package has no drawing sheets: figures.md is a figure plan citing CONFIRMED.md, P1/01, P2/09, PF-1 and PF-12, and registry.md is a set of drawing instructions with draftsperson's notes. figures.md (second paragraph) states that 'the disclosure does not explain how the purge gap opens', and registry.md FIG. 2 instructs 'draw no inlet or outlet feature'; if either were filed, that would be an admission against sufficiency. Filing without the drawings referred to engages 35 USC 113, Rule 56 EPC (late-filed drawings re-date the application or references to them are deemed deleted) and the UK missing-parts provisions (s.15(5)). FIG. 1 and FIG. 2 cannot be drawn truthfully until F-30-1 is resolved. Formal, but a filing blocker. Lead finding for F-36-1.

#### F-37-1 — Claim 4: distinguishing method steps are conditional, so the method reads on any inflation of any valve

**Severity** high · **Area** formal and consistency · **Claims** 4, 52, 53, 54, 55, 56 · **Specification** [0015], [0111], Fig. 7

**Raised by** ip-reviewer (review step 37)

**The objection.** Under BRI (Ex parte Schulhauser; MPEP 2111.04 II) the steps introduced by 'when the pressure differential exceeds an opening pressure' and 'when the pressure differential exceeds an over-travel threshold' need not be performed. Only 'applying, by the inflation device, a pressure differential across the valve' is required, which any tyre-valve inflation (e.g. reference 1, US11338632B2) meets. This is a credible US anticipation rejection that needs an amendment.

**Least narrowing fix.** Recite the rise of the pressure differential above the opening pressure and then above the over-travel threshold as a positive step, and recast the two 'when' clauses as consequences of it ('as the pressure differential exceeds ...'). Scope is unchanged; see Corrections 1 to 3.


**Ruling** upheld — Correct for the US. Claim 4 positively recites only 'applying, by the inflation device, a pressure differential across the valve' and 'the pressure differential falling'. The distinguishing steps are conditioned: 'when the pressure differential exceeds an opening pressure', 'when the pressure differential exceeds an over-travel threshold' and 'while the purge gap is open'. Under Ex parte Schulhauser (PTAB 2016, precedential) and MPEP 2111.04 II, steps conditioned on an event the claim does not require need not be performed under the broadest reasonable interpretation. Nothing in claim 4 requires the pressure differential to reach either value, and [0042] and [0078] say expressly that an inflation may never reach the over-travel threshold. What remains is inflation of a valve having a deflectable element, which a US examiner can credibly read on conventional tyre-valve inflation. [0015] already describes the method with positive steps ('a pressure differential ... which exceeds the opening pressure'; 'the pressure differential exceeding the over-travel threshold'), so the fix is in place and costs no scope. Dependent claims 52 to 56 inherit the defect. EPO and UK practice read the claimed sequence as required, so the issue is US-specific but still needs the amendment.

#### F-28-1 — A wiper ring below the rigid valve seat is not described with a purge gap in parallel with the main flow passage

**Severity** high · **Area** support, priority and amendment basis · **Claims** 1, 27, 28, 29, 45, 58, 60 · **Specification** [0032], [0046], [0053], [0094], [0094a], Fig. 3

**Raised by** ip-reviewer (review step 28)

**The objection.** Claim 1 requires a purge gap in parallel with the main flow passage, whose gas does not pass between the sealing face and the valve seat ([0046]). A wiper ring below the rigid valve seat ([0094]) can only see gas that has already passed that seat, so its purge gap is in series, which [0032] and [0046] exclude. [0094] and [0094a] leave the gap position, the mounting and the geometry unstated, so the combination of claims 27 and 28 with claim 1 is not disclosed (Art. 84; s.112(a)), and amending into it later would meet an added-matter objection.

**Least narrowing fix.** Add the inventors' statement of where the third embodiment's purge gap lies and how inflation gas reaches it without passing the rigid valve seat, for example a bypass passage in the core body closed at rest by the wiper ring; if none exists in their conception, re-hang claims 27 to 29, 45, 58 and 60 from a recovery-wipe claim (narrowing, for the human to decide).  
*This fix needs disclosure the application does not yet contain.*


**Ruling** upheld — Correct on the text. [0094] and [0053] place the wiper ring 130 'below the rigid valve seat 132, on the side of the rigid valve seat 132 towards the inflatable body', and claim 28 recites the same. [0046] requires the purge gap to be bounded at least in part by a surface of the deflectable element and defines 'separate from the main flow passage' as gas that 'does not pass between the sealing face and the valve seat'. Nothing in [0094], [0094a], [0107] or FIG. 3 (drawn schematically, [0026]; figures.md FIG. 3 says the purge gap position is 'not stated') describes how inflation gas reaches a gap bounded by a ring below the seat without first passing the seat, and [0094a] states the mounting of the wiper ring is 'not stated herein'. As filed, claims 27 to 29, 45, 58 and 60 combine claim 1's parallel purge gap with a position for which no parallel path is described: a written-description (s.112(a)) and support/sufficiency (Art. 84, Art. 83; UK s.14(3), s.14(5)(c)) exposure for those dependent claims. The added-matter limb is overstated: claims filed in this form are part of the original disclosure, so the risk is support and enablement, not Art. 123(2) at filing. Needs the inventors' statement of the gap position and inlet; lead finding for F-29-2 and F-32-4.

#### F-28-2 — Ranges disclosed for the first embodiment are claimed for embodiments the description expressly leaves without them

**Severity** high · **Area** support, priority and amendment basis · **Claims** 19, 25, 30, 31, 32, 33, 34, 47 · **Specification** [0040], [0042], [0043], [0066], [0093], [0104], [0106], [0124], [0125]

**Raised by** ip-reviewer (review step 28)

**The objection.** Through multiple dependency, claims 30 to 34 and 47 apply the pressure, over-travel and purge gap width ranges to the polymer seat ring and the wiper ring, and claim 25 via claim 19 applies the convolution amplitude to the polymer seat ring. Yet [0124] and [0125] tie those values to the first embodiment and [0093], [0104] and [0106] say no dimension is stated for the alternatives. Meanwhile [0040], [0042], [0043] and [0066] state the same ranges generally. This is an Art. 84 inconsistency, and after filing it becomes an intermediate-generalisation objection to any amendment that adds a range to claim 1.

**Least narrowing fix.** Obtain the inventors' confirmation whether the pressure, over-travel and purge gap width ranges apply to every embodiment; if so, amend [0124] and [0125] to state them for the valve generally, keeping the seat ring dimensions tied to the seat ring; if not, restrict the dependencies of claims 19, 30 to 34 and 47 to the first-embodiment claims (narrowing of dependent claims only).  
*This fix needs disclosure the application does not yet contain.*


**Ruling** upheld — Correct on the text. [0040], [0042], [0043] and [0066] state the pressure, over-travel and purge gap width ranges 'in some embodiments' without restriction, and [0016] says the ranges 'apply in some embodiments'; but [0124] says 'The dimensions and pressures of the section on ranges are those of the first embodiment', [0125] ties the section to 'the seat ring 30 of superelastic alloy of the prototype', and [0093], [0104] and [0106] state that no dimension is given for the polymer seat ring or the wiper ring. Claims 30 to 34 (dependent on 'any one of claims 1 to 29', which includes claims 25 to 29), claim 47 (via claims 44 and 45) and claim 25 via claim 19 therefore claim combinations the description both supports and disclaims: an Art. 84 inconsistency now, and an intermediate-generalisation argument against any later amendment putting a pressure range into claim 1. It cannot be repaired after filing, which justifies high. Lead finding for F-29-4.

#### F-29-2 — Path 9 lacks a disclosed purge gap for the wiper ring

**Severity** high · **Area** support, priority and amendment basis · **Claims** 1, 27, 28, 45 · **Specification** [0046], [0094], [0094a]

**Raised by** ip-reviewer (review step 29)

**The objection.** A wiper ring below the rigid valve seat sees only gas that has passed the seat, so its purge gap is not the parallel path that claim 1 and [0046] require, and [0094] leaves the gap position unstated; combining claim 1 with the wiper ring would be added matter as the text stands.

**Least narrowing fix.** Add the inventors' statement of where the third embodiment's purge gap lies and how inflation gas reaches it without passing the rigid valve seat 132; if there is none, confine Path 9 to the recovery-wipe aspect of [0011].  
*This fix needs disclosure the application does not yet contain.*


**Ruling** rejected — Duplicates F-28-1: the same wiper-ring purge gap below the rigid valve seat 132 ([0094], [0094a], claim 28) with no parallel path, stated as its effect on amendment path 9. Resolved by the F-28-1 correction.

#### F-29-4 — The pressure and travel ranges are tied to the first embodiment by [0124] and [0125], defeating Path 7

**Severity** high · **Area** support, priority and amendment basis · **Claims** 30, 31, 32, 33, 34, 47 · **Specification** [0040], [0042], [0043], [0066], [0124], [0125], [0126], [0127]

**Raised by** ip-reviewer (review step 29)

**The objection.** An examiner will cite [0124] and [0125] to say that the pressure and travel ranges are disclosed only with the superelastic seat ring of the first embodiment, making their addition to claim 1 an intermediate generalisation (Art. 123(2)) unless the seat ring features are added too, which collapses Path 7 into Path 8.

**Least narrowing fix.** Obtain the inventors' confirmation; if the ranges belong to the valve as such, restate them in [0126] and [0127] for every embodiment and confine [0124] and [0125] to the seat ring dimensions.  
*This fix needs disclosure the application does not yet contain.*


**Ruling** rejected — Duplicates F-28-2: the same tie of the pressure and travel ranges to the first embodiment by [0124] and [0125], against the general statements of [0040], [0042], [0043] and [0066]; F-28-2 already states the intermediate-generalisation consequence for adding a range to claim 1. Resolved by the F-28-2 correction.

#### F-36-1 — No drawings exist; the purge gap is drawn "schematically" with no inlet or outlet

**Severity** high · **Area** support, priority and amendment basis · **Claims** 1, 2, 16, 40 · **Specification** figures.md FIG. 1, figures.md FIG. 2, [0026]

**Raised by** ip-reviewer (review step 36)

**The objection.** figures.md records that the inventors' sketches 'exist by name only; no image has been seen' and instructs 'draw no inlet or outlet feature' for the purge gap; [0026] says it is shown schematically. There are no drawings, drawings cannot be added after filing without added-matter exposure, and figures.md contains internal working references and draftsperson's notes that are not filing text.

**Least narrowing fix.** Obtain the inventors' sketches and prepare formal drawings of FIG. 1 to FIG. 8, with FIG. 1 and FIG. 2 showing the actual purge-gap region and flow path at rest and in over-travel; file drawings and a brief description, not the figure plan.  
*This fix needs disclosure the application does not yet contain.*


**Ruling** rejected — Duplicates F-30-3 (no drawing sheets; figures.md and registry.md are internal plan and instructions citing dossier references, including 'exist by name only; no image has been seen' at figures.md paragraph 1 and 'draw no inlet or outlet feature' at registry.md FIG. 2). The missing inlet and outlet is the defect upheld in F-30-1. Both upheld there.

## Medium and low findings (59)

| Id | Severity | Area | Title | Claims | Ruling |
|---|---|---|---|---|---|
| F-33-1 | medium | design-around | "Undeflected" in ranges (a) and (b) is an absolute limitation avoided by a light preload | 1, 2, 4 | upheld |
| F-33-3 | medium | design-around | Deflection only by the valve member's over-travel; deflection by gas pressure or by the pump head avoids the claims | 1, 2, 4 | — |
| F-33-4 | medium | design-around | Method claim 4 is performed by the rider, so it reaches a competitor only through indirect infringement | 4, 52, 53, 54, 55, 56 | — |
| F-33-5 | medium | design-around | Purge flow and purge-gap closure are provable only by a bench test the description does not describe | 1, 2, 4 | — |
| F-35-1 | medium | design-around | Method claim 4 scores 2 for detectability and 2 for evidentiary ease | 4 | — |
| F-37-3 | medium | design-around | 'Remains undeflected' in range (b) is an unnecessary, measurable limitation | 1, 2, 4 | — |
| F-28-7 | medium | enablement | The only evidence of over-travel is a snap on removal, not purge flow during inflation | 1, 4, 55, 56 | — |
| F-30-8 | medium | enablement | The evidence that over-travel and purge flow occurred is an audible snap | 1, 4 | — |
| F-32-10 | medium | enablement | Undeflected at rest, although the seating load bears on the upper edge that converts axial load into expansion | 1, 2 | — |
| F-32-9 | medium | enablement | The technical effect rests on an audible snap and the inventors' attribution | 1, 4 | — |
| F-36-3 | medium | enablement | Behaviour on manual depression of the valve member and with the lock nut is not stated | 1, 2, 4 | — |
| F-36-4 | medium | enablement | No dimensions for the polymer seat ring or the wiper ring | 25, 26, 27, 28, 29, 44, 45, 58, 60 | — |
| F-36-7 | medium | enablement | The geometry of the recovery wipe is not stated | 5, 35, 52, 57, 59 | — |
| F-38-5 | medium | enablement | The summary states a sealant-film removal effect that the only data partly contradict |  | — |
| F-28-6 | medium | formal | The figures in the package are a plan and draftsperson's instructions, not drawings, and carry internal cross-references |  | — |
| F-30-4 | medium | formal | Austenite finish temperature has no fixed measuring method | 21, 38, 42 | — |
| F-30-7 | medium | formal | Sealant-accumulation surfaces is defined by use | 1, 2, 4 | — |
| F-30-9 | medium | formal | US multiple dependency on multiple dependent claims; claim fees in all three offices | 8, 22, 49, 54 | — |
| F-32-11 | medium | formal | US multiple dependent claims depend on other multiple dependent claims | 8, 22, 49, 54, 17, 30, 48 | — |
| F-32-5 | medium | formal | Af parameter with an open measuring method | 21, 38, 42 | — |
| F-32-6 | medium | formal | Pressure thresholds are claimed with no measuring condition | 1, 2, 4, 32, 33, 34, 47 | — |
| F-37-2 | medium | formal | 'Deflectable element' invites a US means-plus-function construction | 1, 2, 4 | — |
| F-37-4 | medium | formal | Claims 25 and 44 include a self-contradictory superelastic-and-polymer branch | 25, 44, 10, 38 | — |
| F-37-5 | medium | formal | Claims 8-12 and 30-33 depend on claims of another category | 8, 9, 10, 11, 12, 30, 31, 32, 33 | — |
| F-40a-1 | medium | formal | No drawing sheets exist, though the description relies on eight figures |  | — |
| F-32-7 | medium | novelty | The recovery wipe is known in kind from US4050473A and US4236547A | 5, 35, 52, 57, 59 | — |
| F-32-8 | medium | novelty | The seat ring fallbacks add features known from US3417778A | 9, 11, 14, 39 | — |
| F-28-5 | medium | support | The breadth of deflectable element and purge gap rests on a principle plus two species with open mechanisms | 1, 2, 4 | — |
| F-29-5 | medium | support | No basis exists to amend the method to over-travel during a pump stroke | 4, 55, 56 | — |
| F-30-5 | medium | support | Deflectable element construction: 112(f) placeholder in the US and displacement reading under BRI | 1, 2, 4 | — |
| F-30-6 | medium | support | Range claims extend to alternatives for which the description says no ranges are stated | 19, 25, 30, 31, 32, 33, 34, 47 | — |
| F-36-5 | medium | support | No range is stated for the normal stroke | 31 | — |
| F-36-6 | medium | support | Only the Presta pattern is disclosed; no Schrader or other valve-standard embodiment | 1, 2, 48 | — |
| F-38-2 | medium | support | 'The valves described herein' statements exclude viable embodiments (added valve, one moving part, whole mechanism in the core) | 1, 2, 3, 4 | — |
| F-38-3 | medium | support | Definitions of 'sealing face' and 'inflatable body' import dependent-claim features into independent claims | 1, 2, 3, 4, 5, 35, 50, 52 | — |
| F-38-4 | medium | support | Ranges disclaimed for the polymer seat ring and wiper ring, yet claims 30-34 and 47 depend on those embodiments | 30, 31, 32, 33, 34, 47, 25, 26, 27, 28, 29, 44, 45 | — |
| F-33-6 | low | design-around | Recovery-wipe dependent claims are hard to prove on a commercial product | 5, 35, 52, 57, 59 | — |
| F-37-6 | low | design-around | Claim 24 is a product-by-process fallback of little value | 24 | — |
| F-36-8 | low | enablement | Spring rates and the effective area of the valve member are not stated | 8, 37 | — |
| F-36-9 | low | enablement | The thermal purge variant is disclosed without a mechanism |  | — |
| F-28-8 | low | formal | Claim 50 adds nothing because inflatable body is defined as containing sealant | 3, 50 | — |
| F-30-10 | low | formal | Lettered paragraph numbers |  | — |
| F-32-12 | low | formal | According to the inventors attributions and has been considered in the specification |  | — |
| F-32-13 | low | formal | Product-by-process with process parameters | 24 | — |
| F-32-14 | low | formal | The method recites events and parts' behaviour rather than steps | 4 | — |
| F-37-7 | low | formal | Claim 7: 'below' has no reference direction in the claim | 7 | — |
| F-38-7 | low | formal | Background pinpoints use database paragraph indices, not the documents' own numbering |  | — |
| F-38-8 | low | formal | The description contradicts itself on the core body material of the tested prototype |  | — |
| F-40a-2 | low | formal | 'Inflation gas' carries no reference sign (66) in claims 1, 2 and 4 | 1, 2, 4 | — |
| F-40a-3 | low | formal | Claimed tubeless tyre set-up and outward-deflected wiper ring are not shown in any figure | 51, 28, 45 | — |
| F-40a-4 | low | formal | Claims 57 to 60 are not grouped with the claims they depend on | 57, 58, 59, 60 | — |
| F-40a-5 | low | formal | FIG. 4A and FIG. 4B each combine two different views |  | — |
| F-40a-6 | low | formal | No abstract in the package |  | — |
| F-40a-7 | low | formal | The claims have no heading | 1 | — |
| F-32-2 | low | novelty | Obvious over US20080188352A1 in view of US3417778A; under broadest reasonable interpretation, possible anticipation | 1, 2, 3, 4 | rejected |
| F-38-6 | low | novelty | 'Operates as a conventional valve' characterises the claimed normal-stroke behaviour as known | 1, 2 | — |
| F-28-9 | low | support | Stainless steel is generalised from 303 stainless steel | 13 | — |
| F-29-6 | low | support | The direction of the recovery wipe is unstated, so no amendment can use it | 5, 35, 52 | — |
| F-38-9 | low | support | The method summary in [0015] is narrower than claim 4 | 4 | — |
