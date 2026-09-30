# Patent Council · matter `valve-oc-20260930` · run `r1` · step `LB-abstract` · profile full

You are the **Specification Drafter**. Follow your AGENTS.md. This message is the whole brief: what to do, the prompts to execute, every input (embedded below, so do not re-read those files), and the exact files to write.

## What to do

From the FINAL description and claims (embedded): the Abstract (Prompt 39a) as the reply, the abstract text alone in `abstract.md` (no heading), and `list-of-figures.md`: one line per figure, `Fig. N — what it shows`, matching the figures and reference numerals the description uses.

**Time budget:** about 5 minutes. The whole matter is planned to finish end to end in two hours. Be complete, but write each deliverable once: no drafts, no repetition, no padding.

## Prompt 39a — Abstract drafting  (kind `compose`)

**Write your reply to:** `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/loop/c1/39a.md`

*Draft the required, format-constrained summary - last, and only from finished text.*

Using only the finalized detailed description and finalized claims (not the drafting history or earlier phase outputs), draft the Abstract: a single paragraph, approximately 50-150 words depending on jurisdiction, stating the technical field and the core technical solution in plain, non-legal language. Do not introduce new technical matter, do not use "means for" or other claim-style language, and do not include marketing or legal-conclusion language. Flag if the finalized claims changed after this draft was produced, since the abstract would then need to be re-checked.

**How to work.** You have been given only the finished description and the finished claims, on purpose; do not ask for or rely on anything else. Under `### Abstract` write exactly one paragraph of 50 to 150 words, no heading inside it, no reference numerals in parentheses unless the target jurisdiction convention requires them, no 'means for', no 'the invention', no 'novel' or 'improved', and no claim-style enumeration. Every technical statement in the abstract must be traceable to a claim or description paragraph; list those references in `support_refs`. State the word count in `## Rationale`. In `## Assumptions` record the claims file identity you drafted against so the runner can detect a later change. Reply exactly in the drafting output contract: `## Deliverable` (with the H3 sections named above), `## Rationale`, `## Assumptions`, `## Open Questions`, then one final fenced `json` envelope. No preamble before `## Deliverable`; nothing after the envelope. Reuse locked preferred terms verbatim; declare any other term in `new_terms` with a reason.

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

### `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/claims.v2.md`

```markdown
1. A valve core for an inflation valve, the valve core comprising a core body (20), a poppet (40) guided by the core body, a deflectable ring element carried by the core body, a return spring (50) biasing the poppet towards a closed state of the valve core, and a main passage (64) past a sealing face (42) of the poppet, the main passage being closed by the sealing face in the closed state; the poppet having a supply side and a chamber side and being movable from the closed state in an opening direction through a normal stroke and beyond the normal stroke into over-travel; the valve core having: the closed state, in which the main passage is closed, the deflectable ring element is in its at-rest form and a purge gap (60) associated with the deflectable ring element is closed; a normal-open state, in which the poppet is displaced from the closed state within the normal stroke, the main passage is open and the purge gap is closed; and a purge state, in which the poppet is in over-travel beyond the normal stroke and produces a radial deflection of the deflectable ring element, the radial deflection opening the purge gap so that a purge flow path (62), separate from the main passage, extends from the supply side through the purge gap to the chamber side; and wherein, when the poppet returns from over-travel, the deflectable ring element undergoes shape recovery to its at-rest form and closes the purge gap.

2. The valve core of claim 1, wherein the poppet is displaced from the closed state in response to a pressure differential between the supply side and the chamber side, the valve core being in the closed state at a pressure differential below a crack pressure, in the normal-open state at a pressure differential at or above the crack pressure and not exceeding an over-travel threshold higher than the crack pressure, and in the purge state at a pressure differential exceeding the over-travel threshold.

3. The valve core of claim 1 or claim 2, wherein the poppet has a deflecting formation (44) which is spaced from the deflectable ring element in the closed state and throughout the normal stroke and which bears on the deflectable ring element in over-travel so as to produce the radial deflection.

4. The valve core of claim 3, wherein the deflecting formation is a purge shoulder (44) of the poppet on the chamber side of the sealing face.

5. The valve core of claim 4, wherein the purge shoulder is an annular shoulder integral with the poppet which bears axially on the deflectable ring element in over-travel.

6. The valve core of claim 3, wherein the deflecting formation is a tapered purge shoulder (244) having a frustoconical flank which enters the deflectable ring element in over-travel and deflects the deflectable ring element radially outward by direct radial contact with an inner surface of the deflectable ring element.

7. The valve core of claim 3, wherein the deflecting formation comprises two or more discrete lugs (344) spaced around a circumference of the poppet, which load the deflectable ring element at discrete points so that the purge gap opens over arcs of a circumference of the deflectable ring element.

8. The valve core of claim 3, wherein the deflecting formation is provided on a separate collar (444) fixed on a poppet stem (41) of the poppet.

9. The valve core of any one of claims 1 to 8, wherein the deflectable ring element is a seat ring (30) having a sealing edge (34) on which the sealing face rests in the closed state.

10. The valve core of any one of claims 1 to 8, further comprising a fixed seat (130) carried by the core body, the fixed seat not deflecting in over-travel and providing a sealing edge on which the sealing face rests in the closed state, wherein the deflectable ring element is a wiper ring (132) separate from the fixed seat and positioned on the chamber side of the fixed seat.

11. The valve core of any one of claims 1 to 10, wherein the deflectable ring element has a wall arranged such that an axial load applied to the deflectable ring element by the poppet in over-travel is converted into the radial deflection.

12. The valve core of claim 11, wherein the wall comprises a convoluted wall (32) having one or more convolutions.

13. The valve core of claim 12, wherein the convoluted wall has one convolution or two convolutions.

14. The valve core of claim 12 or claim 13, wherein the convoluted wall has a convolution amplitude of from 0.08 mm to 0.20 mm.

15. The valve core of any one of claims 12 to 14, wherein a root of each convolution of the convoluted wall is provided with a fillet radius.

16. The valve core of claim 11, wherein the wall is a frustoconical wall (232), a slotted wall (332) or a cellular wall (432).

17. The valve core of claim 9, wherein the seat ring has a seat ring inner diameter of from 2.0 mm to 2.6 mm and a seat ring wall thickness of from 0.15 mm to 0.30 mm.

18. The valve core of claim 17, wherein the seat ring has a seat ring free length of from 2.5 mm to 4.0 mm.

19. The valve core of any one of claims 1 to 18, wherein the core body has an internal shoulder (24) and the deflectable ring element is retained in the core body against the internal shoulder, the radial deflection being an elastic deformation of a wall of the deflectable ring element while the deflectable ring element remains retained in the core body.

20. The valve core of claim 19, wherein the deflectable ring element is retained in a core body bore (22) of the core body by an interference fit.

21. The valve core of claim 20, wherein the interference fit has an interference of approximately 0.03 mm on diameter.

22. The valve core of claim 20 or claim 21, wherein the interference fit is provided over an axial band of the deflectable ring element adjacent the internal shoulder, and a remainder of an outer surface of the deflectable ring element, including a portion of the wall which undergoes the radial deflection, is not in interference with the core body bore.

23. The valve core of any one of claims 19 to 22, wherein the deflectable ring element is retained by a crimped lip (224) formed on the core body over an end of the deflectable ring element remote from the internal shoulder, or by a retaining sleeve (324) pressed or threaded into the core body and clamping the deflectable ring element against the internal shoulder.

24. The valve core of any one of claims 19 to 23, wherein the deflectable ring element is further retained by an adhesive bond, by staking of the core body over the deflectable ring element, by laser welding of the deflectable ring element to the core body, by over-moulding of the core body around the deflectable ring element, or by clamping of the deflectable ring element between two parts of the core body.

25. The valve core of any one of claims 1 to 18, wherein the deflectable ring element is an integral flexure section of the core body formed in one piece with the core body, the core body being formed from a resilient polymer or from stainless steel of spring temper.

26. The valve core of any one of claims 1 to 25, wherein, as the deflectable ring element undergoes shape recovery, the deflectable ring element moves across a surface of the poppet and shears sealant film from that surface.

27. The valve core of claim 26, wherein the surface of the poppet is the sealing face.

28. The valve core of claim 26 or claim 27, wherein the deflectable ring element has a defined wiping edge at an inner surface of the deflectable ring element which is presented to the poppet as the deflectable ring element undergoes shape recovery.

29. The valve core of any one of claims 1 to 28, wherein the poppet has a second formation, on a side of the deflectable ring element opposite to a side which the poppet contacts to produce the radial deflection in over-travel, which meets the deflectable ring element on a return movement of the poppet and drives the deflectable ring element towards its at-rest form.

30. The valve core of any one of claims 1 to 29, wherein the radial deflection is radially outward.

31. The valve core of any one of claims 1 to 29, wherein the radial deflection is radially inward at a surface of the deflectable ring element which bounds the purge gap.

32. The valve core of claim 9, wherein the purge gap is an annular radial clearance between an outer surface of the seat ring and a core body bore (22) of the core body, which opens where a bounding portion of the outer surface moves away from the core body bore in the purge state.

33. The valve core of claim 9, wherein the purge gap is bounded by an inner surface of the seat ring and the poppet on the chamber side of the sealing edge, and the purge flow path passes along a poppet stem (41) of the poppet.

34. The valve core of any one of claims 1 to 31, wherein the purge gap is formed by one or more openings through a wall of the deflectable ring element, the openings being closed in the closed state and in the normal-open state and being opened or uncovered by the radial deflection in the purge state.

35. The valve core of any one of claims 1 to 34, wherein the purge flow path includes one or more purge ports (262) formed through a wall of the core body on the chamber side of the purge gap.

36. The valve core of any one of claims 1 to 35, wherein the purge flow path includes one or more flutes (362) formed as axial grooves in a core body bore (22) of the core body at an axial position of the deflectable ring element, an outer surface of the deflectable ring element lying on lands between the flutes and closing the flutes in the closed state and in the normal-open state.

37. The valve core of any one of claims 1 to 36, wherein the purge gap has a purge gap opening of from 0.10 mm to 0.25 mm in the purge state.

38. The valve core of claim 2, or of any one of claims 3 to 37 when dependent on claim 2, further comprising a threshold-setting arrangement by which a force resisting movement of the poppet rises at an end of the normal stroke, the threshold-setting arrangement setting the over-travel threshold.

39. The valve core of claim 38, wherein the threshold-setting arrangement is a second spring stage (54) of the return spring, the return spring having a first spring stage (52) of lower rate which resists the normal stroke and sets the crack pressure, and the second spring stage having a higher rate than the first spring stage, coming into action when the normal stroke is complete and setting the over-travel threshold.

40. The valve core of claim 38, wherein the threshold-setting arrangement comprises an auxiliary spring (254) which is engaged when a lost-motion clearance between the auxiliary spring and the poppet closes at the end of the normal stroke, after which the auxiliary spring acts in parallel with the return spring.

41. The valve core of claim 38, wherein the threshold-setting arrangement comprises a detent (354) which holds the poppet at the end of the normal stroke until a force on the poppet exceeds a breakaway value.

42. The valve core of claim 2, or of any one of claims 3 to 37 when dependent on claim 2, wherein the return spring has a single rate and the over-travel threshold is set by a stiffness of the deflectable ring element.

43. The valve core of claim 2, or of any one of claims 3 to 42 when dependent on claim 2, wherein the over-travel threshold is from 2.5 bar to 5.0 bar.

44. The valve core of claim 2, or of any one of claims 3 to 43 when dependent on claim 2, wherein the crack pressure is from 0.8 bar to 1.5 bar.

45. The valve core of any one of claims 1 to 44, wherein in over-travel the poppet moves beyond an end of the normal stroke by an over-travel distance of from 0.4 mm to 0.9 mm.

46. The valve core of claim 2, or of any one of claims 3 to 42 when dependent on claim 2, wherein the crack pressure is about 1.0 bar and the over-travel threshold is about 3.5 bar.

47. The valve core of any one of claims 1 to 46, wherein the core body has an over-travel stop which the poppet meets at an end of over-travel, the over-travel stop limiting an over-travel distance of the poppet.

48. The valve core of any one of claims 1 to 47, wherein the poppet is movable into over-travel by mechanical depression of the poppet by a depressor in a head of an inflation device, or in an adaptor fitted between the inflation device and the supply side, when the inflation device is coupled to the supply side.

49. The valve core of any one of claims 1 to 48, wherein the purge flow path is arranged to carry flow through the purge gap in either direction between the supply side and the chamber side.

50. The valve core of any one of claims 1 to 49, wherein the deflectable ring element is formed from a superelastic alloy.

51. The valve core of claim 50, wherein the superelastic alloy has an austenite finish temperature below 5 °C.

52. The valve core of claim 50 or claim 51, wherein the superelastic alloy is a nickel-titanium alloy of nominally 55.8 wt% nickel content.

53. The valve core of claim 50 or claim 51, wherein the superelastic alloy is a NiTiCu alloy, a NiTiFe alloy or a NiTiCr alloy.

54. The valve core of any one of claims 1 to 49, wherein the deflectable ring element is formed from a resilient metal which recovers its shape elastically without a phase transformation, the resilient metal being stainless steel of spring temper, cold-worked austenitic stainless steel, precipitation-hardened stainless steel or a beta-titanium alloy.

55. The valve core of any one of claims 1 to 49, wherein the deflectable ring element is formed from a resilient polymer.

56. The valve core of claim 55, wherein the resilient polymer is polyether ether ketone.

57. The valve core of any one of claims 1 to 56, wherein the core body is formed from stainless steel.

58. The valve core of any one of claims 1 to 57, wherein the sealing face is of hard-anodised aluminium or carries a hard low-adhesion coating.

59. The valve core of any one of claims 1 to 58, wherein the core body has an external thread for engagement in a stem bore of a valve stem, the valve core being removable from the valve stem as a unit.

60. The valve core of any one of claims 1 to 59, wherein the core body is a Schrader-pattern core body (620) and the poppet is a Schrader-pattern poppet (630).

61. A valve core for an inflation valve, the valve core comprising a core body (20), a poppet (40) guided by the core body, a deflectable ring element carried by the core body, a return spring (50) biasing the poppet towards a closed state of the valve core, and a main passage (64) past a sealing face (42) of the poppet, the main passage being closed by the sealing face in the closed state; the poppet having a supply side and a chamber side and being movable from the closed state in an opening direction through a normal stroke, within which the main passage is open, and beyond the normal stroke into over-travel, in which the poppet bears on the deflectable ring element and produces a radial deflection of the deflectable ring element while the deflectable ring element remains retained by the core body; and wherein, when the poppet returns from over-travel, the deflectable ring element undergoes shape recovery to its at-rest form and, as it undergoes shape recovery, moves across a surface of the poppet and shears sealant film from that surface.

62. The valve core of claim 61, wherein the poppet has a deflecting formation (44) which is spaced from the deflectable ring element in the closed state and throughout the normal stroke and which bears on the deflectable ring element in over-travel so as to produce the radial deflection.

63. The valve core of claim 61 or claim 62, wherein the deflectable ring element is a seat ring (30) having a sealing edge (34) on which the sealing face rests in the closed state, and the surface of the poppet across which the seat ring moves is the sealing face.

64. The valve core of any one of claims 61 to 63, wherein the deflectable ring element has a wall arranged such that an axial load applied to the deflectable ring element by the poppet in over-travel is converted into the radial deflection, the wall comprising a convoluted wall (32) having one or more convolutions.

65. The valve core of any one of claims 61 to 64, wherein the deflectable ring element is formed from a superelastic alloy.

66. The valve core of any one of claims 61 to 65, wherein the deflectable ring element is sealed at its periphery so that no inflation gas flows past the deflectable ring element while it is deflected.

67. The valve core of any one of claims 61 to 66, wherein the deflectable ring element has a defined wiping edge at an inner surface of the deflectable ring element which is presented to the poppet as the deflectable ring element undergoes shape recovery.

68. The valve core of any one of claims 61 to 67, wherein the poppet is displaced from the closed state in response to a pressure differential between the supply side and the chamber side, the poppet beginning the normal stroke at a crack pressure and entering over-travel at a pressure differential exceeding an over-travel threshold higher than the crack pressure.

69. An inflation valve for an inflatable chamber, the inflation valve comprising a valve stem (10) having a stem bore (12) and, carried by the valve stem, a deflectable ring element, a poppet (40) and a return spring (50), the poppet having a sealing face (42), a supply side and a chamber side, a main passage (64) past the sealing face being closed by the sealing face in a closed state of the inflation valve, the return spring biasing the poppet towards the closed state, and the poppet being movable from the closed state in an opening direction through a normal stroke and beyond the normal stroke into over-travel; the inflation valve having: the closed state, in which the main passage is closed, the deflectable ring element is in its at-rest form and a purge gap (60) associated with the deflectable ring element is closed; a normal-open state, in which the poppet is displaced from the closed state within the normal stroke, the main passage is open and the purge gap is closed; and a purge state, in which the poppet is in over-travel beyond the normal stroke and produces a radial deflection of the deflectable ring element, the radial deflection opening the purge gap so that a purge flow path (62), separate from the main passage, extends from the supply side through the purge gap to the chamber side; and wherein, when the poppet returns from over-travel, the deflectable ring element undergoes shape recovery to its at-rest form and closes the purge gap.

70. The inflation valve of claim 69, wherein the poppet is displaced from the closed state in response to a pressure differential between the supply side and the chamber side, the inflation valve being in the closed state at a pressure differential below a crack pressure, in the normal-open state at a pressure differential at or above the crack pressure and not exceeding an over-travel threshold higher than the crack pressure, and in the purge state at a pressure differential exceeding the over-travel threshold.

71. The inflation valve of claim 69 or claim 70, further comprising a core body (20) received in the stem bore, the deflectable ring element, the poppet and the return spring being carried by the valve stem through the core body.

72. The inflation valve of claim 71, wherein the core body is threaded into the stem bore and is removable from the valve stem as a unit with the deflectable ring element, the poppet and the return spring.

73. The inflation valve of claim 71 or claim 72, wherein the core body, the deflectable ring element, the poppet and the return spring form a valve core according to any one of claims 1 to 68.

74. The inflation valve of claim 69 or claim 70, wherein the inflation valve has no separate core body, the valve stem directly carrying the deflectable ring element, which is a seat ring (730), together with the poppet and the return spring, and the valve stem providing a locating formation against which the seat ring is retained and a bore in which the poppet is guided.

75. The inflation valve of claim 74, wherein the seat ring has a sealing edge on which the sealing face rests in the closed state and a convoluted wall which converts an axial load applied to the seat ring by the poppet in over-travel into the radial deflection.

76. An inflatable chamber comprising a bicycle inner tube or a tubeless bicycle tyre set-up fitted with an inflation valve according to any one of claims 69 to 75.

77. The inflatable chamber of claim 76, wherein the inflatable chamber holds liquid sealant.

78. A wheel or a bicycle incorporating an inflatable chamber according to claim 76 or claim 77.

79. A seat ring (30) for a valve core of an inflation valve, the seat ring being an annular element having a sealing edge (34) at one axial end of the seat ring for seating a sealing face of a poppet, and a wall between the one axial end and an opposite axial end of the seat ring, the wall comprising a convoluted wall (32) having one or more convolutions, the convoluted wall converting an axial load applied to the seat ring into a radial deflection of the seat ring, the seat ring undergoing shape recovery to its at-rest form on removal of the axial load, and the seat ring having a seat ring inner diameter of from 2.0 mm to 2.6 mm and a seat ring wall thickness of from 0.15 mm to 0.30 mm.

80. The seat ring of claim 79, wherein the convoluted wall has one convolution or two convolutions.

81. The seat ring of claim 79 or claim 80, wherein the convoluted wall has a convolution amplitude of from 0.08 mm to 0.20 mm.

82. The seat ring of any one of claims 79 to 81, wherein the seat ring has a seat ring free length of from 2.5 mm to 4.0 mm.

83. The seat ring of any one of claims 79 to 82, wherein the seat ring is a continuous ring and the sealing edge is continuous around a circumference of the seat ring.

84. The seat ring of any one of claims 79 to 83, wherein the radial deflection is radially outward.

85. The seat ring of any one of claims 79 to 84, wherein the seat ring is formed from a superelastic alloy.

86. The seat ring of claim 85, wherein the superelastic alloy has an austenite finish temperature below 5 °C.

87. The seat ring of claim 85 or claim 86, wherein the superelastic alloy is a nickel-titanium alloy of nominally 55.8 wt% nickel content.

88. The seat ring of any one of claims 79 to 84, wherein the seat ring is formed from a resilient polymer.

89. The seat ring of claim 88, wherein the resilient polymer is polyether ether ketone.

90. The seat ring of any one of claims 79 to 87, wherein the seat ring inner diameter is 2.3 mm, the seat ring wall thickness is 0.20 mm, the seat ring has a seat ring free length of 3.0 mm, and the convoluted wall has a convolution amplitude of 0.12 mm.

91. A kit for a valve core of an inflation valve, the kit comprising a seat ring according to any one of claims 79 to 90, a poppet (40) having a sealing face (42) and a purge shoulder (44), and a return spring (50) having a first spring stage (52) and a second spring stage (54), for fitting into a core body (20), the seat ring, the poppet and the return spring being matched so that, when assembled into the core body, the purge shoulder is spaced from the seat ring throughout a normal stroke of the poppet and bears on the seat ring only in over-travel of the poppet beyond the normal stroke, and a purge gap (60) associated with the seat ring is closed in a closed state and in a normal-open state of the valve core.

92. A method of operating an inflation valve of an inflatable chamber which holds liquid sealant, the inflation valve comprising a poppet (40) having a supply side, a chamber side and a sealing face (42), a deflectable ring element, a main passage (64) past the sealing face which is closed by the sealing face in a closed state of the inflation valve, and a return spring (50) biasing the poppet towards the closed state, the method comprising, within one inflation event: coupling an inflation device to the supply side, whereby the poppet moves from the closed state through a normal stroke into a normal-open state in which inflation gas flows through the main passage into the inflatable chamber while a purge gap (60) associated with the deflectable ring element remains closed; moving the poppet beyond the normal stroke into over-travel, whereby the poppet produces a radial deflection of the deflectable ring element, the radial deflection opening the purge gap, and inflation gas flows as an air purge along a purge flow path (62), separate from the main passage, from the supply side through the purge gap into the inflatable chamber across surfaces on which sealant film accumulates; and removing the inflation device from the supply side, whereby the poppet returns from over-travel and the deflectable ring element undergoes shape recovery to its at-rest form and closes the purge gap.

93. The method of claim 92, wherein the poppet is moved through the normal stroke by raising a pressure differential between the supply side and the chamber side to at or above a crack pressure, and is moved into over-travel by raising the pressure differential above an over-travel threshold higher than the crack pressure.

94. The method of claim 92, wherein the poppet is moved into over-travel by a depressor in a head of the inflation device, or in an adaptor fitted between the inflation device and the supply side, on coupling of the inflation device to the supply side.

95. The method of any one of claims 92 to 94, wherein, as the deflectable ring element undergoes shape recovery, the deflectable ring element moves across a surface of the poppet and shears sealant film from that surface.

96. The method of any one of claims 92 to 95, wherein the air purge carries sealant film from the surfaces on which sealant film accumulates into the inflatable chamber.

97. The method of claim 93, or of claim 95 or claim 96 when dependent on claim 93, wherein the crack pressure is from 0.8 bar to 1.5 bar and the over-travel threshold is from 2.5 bar to 5.0 bar.

98. The method of claim 93 or claim 97, or of claim 95 or claim 96 when dependent on claim 93, wherein the inflation device is a floor pump and the pressure differential exceeding the over-travel threshold is produced by the floor pump.

99. The method of any one of claims 92 to 97, wherein the inflation device is a compressed-gas inflation device.

100. The method of any one of claims 92 to 99, wherein the inflatable chamber is a bicycle inner tube or a tubeless bicycle tyre set-up.

101. The method of any one of claims 92 to 100, wherein the liquid sealant is an emulsion of latex containing ammonia.

102. The method of any one of claims 92 to 101, further comprising repeating the coupling, the moving and the removing over a plurality of inflation events, the purge gap opening and the air purge occurring in each inflation event in which the poppet moves into over-travel.

103. The method of any one of claims 92 to 102, further comprising, while the inflatable chamber is pressurised and no inflation device is supplying gas to the supply side, pressing the poppet into over-travel so that the purge gap opens and gas from the inflatable chamber flows through the purge gap from the chamber side to the supply side, carrying sealant film out of the inflation valve.

104. The method of any one of claims 92 to 103, wherein the inflation valve comprises a valve core according to any one of claims 1 to 68 or is an inflation valve according to any one of claims 69 to 75.

105. A method of manufacturing a seat ring (30) for a valve core of an inflation valve, the method comprising: providing tube stock of a superelastic alloy; laser cutting a profile of the seat ring from the tube stock, the seat ring having a sealing edge (34) at one axial end of the seat ring; forming, in a wall of the seat ring, a convoluted wall (32) having one or more convolutions, the convoluted wall being defined by the laser cutting, by forming on a mandrel, by shape-setting, or by a combination thereof; and shape-setting the seat ring by holding the seat ring in a fixture which constrains the convoluted wall to its intended geometry, heating the seat ring in the fixture and then water quenching the seat ring, the shape-setting fixing an at-rest geometry of the seat ring to which the seat ring returns by shape recovery, the convoluted wall converting an axial load applied to the seat ring into a radial deflection of the seat ring.

106. The method of claim 105, wherein the tube stock has an outer diameter of 2.7 mm and a wall of 0.20 mm.

107. The method of claim 105 or claim 106, wherein the tube stock is mounted on a mandrel during the laser cutting.

108. The method of any one of claims 105 to 107, wherein the convoluted wall is formed with one convolution or with two convolutions.

109. The method of any one of claims 105 to 108, wherein the shape-setting comprises heating the seat ring in the fixture at 500 °C for 10 minutes and then water quenching the seat ring.

110. The method of any one of claims 105 to 109, wherein a shape-setting temperature and a shape-setting time are selected so that the seat ring has an austenite finish temperature below 5 °C, and the austenite finish temperature is verified on sampled seat rings after the shape-setting.

111. The method of any one of claims 105 to 110, further comprising, after the shape-setting, electropolishing the seat ring to remove surface oxide and a heat-affected edge left by the laser cutting.

112. The method of claim 111, wherein a depth of the electropolishing is limited at an inner surface of the seat ring so as to preserve a defined wiping edge formed by the laser cutting.

113. The method of any one of claims 105 to 112, wherein the superelastic alloy is a nickel-titanium alloy of nominally 55.8 wt% nickel content.

114. The method of any one of claims 105 to 113, wherein the seat ring is a seat ring according to any one of claims 79 to 90.

115. The method of any one of claims 105 to 114, further comprising pressing the seat ring into a core body bore (22) of a core body (20) of the valve core until the seat ring seats against an internal shoulder (24) of the core body, with an interference fit between the seat ring and the core body bore.

116. The method of claim 115, wherein the interference fit has an interference of approximately 0.03 mm on diameter.

117. The method of claim 115 or claim 116, further comprising checking a press-in force or a press-in travel of the seat ring during the pressing.

118. The method of any one of claims 115 to 117, further comprising inserting a poppet (40) into the core body so that a poppet stem (41) of the poppet is guided by the core body and a sealing face (42) of the poppet rests on the sealing edge, and fitting a return spring (50) so that the return spring biases the poppet towards a closed state, thereby forming a valve core according to any one of claims 1 to 68.
```

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

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/description.v2.md`

## Files to write

Write each of these with your Write tool, at exactly this path, one file per call (the folders exist). Write nothing outside the run folder `{R}`. Do not run the checks yourself: the runner runs them and will tell you if anything fails.

- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/loop/c1/39a.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/loop/c1/abstract.md`
- `/Users/ahmed/PatentCouncil/matters/valve-oc-20260930/runs/r1/loop/c1/list-of-figures.md`

When every file is written, reply with one line per file (path and a few words on what it holds) and anything the runner must route: open questions, disclosure requests, open disagreements, narrowing suggested. Nothing else.
