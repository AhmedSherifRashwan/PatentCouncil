# Pre-drafting response — Claims Architect (P5)

One row per finding of `risk/pre-drafting-findings.md` owned by P5 or by P4+P5, against the Final Claim
Set of `P5/25.md` (written to `claims.md`, 86 claims), the stitched `description.md` ([0001] to [0350])
and `support-map.json`. Findings owned by P4 alone that give P5 an instruction (PF-3, PF-20) are in
Part 2. This is a drafting and analysis aid; qualified patent counsel signs off on anything filed.

## Part 1 — Findings owned by P5 or P4+P5

| PF | Addressed? | Where | How | If not, why |
|---|---|---|---|---|
| PF-1 (critical) | Yes | Claims 1, 2, 3; [0014], [0065], [0071], [0072], [0298], [0299] | Both pillars are in each independent claim: a normal stroke and an over-travel of the same poppet, with the load-applying surface spaced from the radially deflectable element throughout the normal stroke and bearing on it in the over-travel; and a purge gap that is a secondary flow path distinct from the main passage, closed at rest and throughout the normal stroke. | — |
| PF-2 (critical) | Yes | Claims 1, 2 ("a load-applying surface that is moved by the poppet ... bears on the radially deflectable element and applies an axial load that produces a radial expansion"); claims 13, 14, 38; [0016], [0102], [0135] | The mechanical load path is in the independent claims. The purge shoulder below the sealing face is claim 14 and the inflow of air is claim 38, both dependent, so DA-18 is not given up in claim 1. | — |
| PF-4 (high) | Yes | Claim 19; claim 22; [0134], [0237] | The purge gap width appears once, in claim 19, below the boundary claims 16 to 18. Claim 22 recites that the convolution flattens and the convoluted wall deforms by bending, which is the description's answer to the hoop-strain point. | — |
| PF-6 (high) | Yes | Claims 1, 2, 5, 51; [0071], [0072], [0300] | The over-travel is defined structurally in the independent claims. "An over-travel differential that is greater than the crack pressure" is the first dependent claim of the valve core (5) and of the method (51). | Support for actuation other than by pressure rests on the definitions only (`P5/unsupported.md`, item 5). |
| PF-7 (high) | Partly | Claims 1, 16, 18, 40, 44, 67; [0190], [0193] | Claim 1 recites the purge gap with no location and without "annular". The annular form is claim 18, the wall slots are claims 44 and 67, the slotted sleeve is claim 40. | DA-10 and DA-14 (rigid parts, no radially deflectable element) are not claimed: the description defines the purge gap as opened by the deflection of the element ([0065]) and the inventor has not confirmed that the air purge alone gives the effect. |
| PF-8 (high) | Yes | Claims 1, 6 to 10; [0101], [0142] to [0147], [0301] | No threshold means in any independent claim. Claim 6 recites "a return bias ... that has a two-rate characteristic"; claims 7 to 10 give four constructions. No "means for" wording is used. | — |
| PF-9 (high) | Yes | Claims 1, 3, 21, 62; [0020], [0104] | The convoluted wall is in no independent claim. Claim 3 claims the seat ring by the functional relationship (axial load, load-converting geometry, radial expansion that opens the purge gap). The convoluted wall is claim 21 (valve core) and claim 62 (seat ring). | — |
| PF-10 (high) | Yes | Claims 27 to 29, 70 to 73; [0203], [0204] | No material in claims 1 to 3. Superelastic material, NiTi alloy and the austenite finish temperature are dependent claims. Claim 4 recites the NiTi alloy because shape-setting is a step for that alloy ([0098], [0255]). | — |
| PF-11 (high) | Yes | Claims 32, 56, 76; [0085], [0138] | The snap-back wipe is in dependent claims only and is recited for the seat ring, as [0085] defines it. | — |
| PF-12 (high) | Yes | Claims 11, 12, 19, 33, 34, 53, 68, 69, 81, 85; [0230] to [0239], [0250] | No range in an independent or first-level dependent claim. Only the inventors' ranges and the prototype values are claimed; the narrower bands of [0241] to [0248] are not. | — |
| PF-13 (high) | Yes | Claims 1, 2; [0099], [0102], [0104], [0105], [0106]; `support-map.json` | Each genus term is used only now that its definition exists, and each is mapped to its paragraph. | — |
| PF-14 (high) | Yes | Claims 5 to 50, 51 to 61, 62 to 77, 78 to 86 | 82 dependent claims: thresholds, load path, location of the purge gap, form of the element, material, snap-back wipe, operating window, product forms. | The detent, the spring-loaded stop, the spring seat washer, the strut pattern, the helical slot and the garter spring are described ([0148], [0151], [0155], [0171], [0173], [0211]) and not claimed; they remain amendment basis. |
| PF-15 (medium) | Yes | No claim; `P5/unsupported.md`, item 2 | The two-piece seat claims of `P5/23.md` (41, 42) were removed. The genus of claim 1 stays supported by the seat ring and the polymer seat ring. | The wording is kept ready to restore once the purge flow path is described. |
| PF-16 (medium) | Yes | Claims 1, 46, 47 to 49; [0158], [0159], [0346] | Claim 1 recites "a valve core for a tyre valve" with no pattern. Claim 46 is the removable threaded valve core in the valve core category; claim 49 is the valve core integral with the valve stem. No claim names a valve pattern. | — |
| PF-19 (low) | Yes | Claims 2, 52, 59; [0274] | The method is a supporting claim. Claim 2 recites no pump head; the pump head is claim 52. The valve core (1) and the removable threaded valve core (46) lead. | — |

## Part 2 — Instructions to P5 in findings owned by P4

| PF | Addressed? | Where | How | If not, why |
|---|---|---|---|---|
| PF-3 (critical) | Partly | Claims 16, 17, 45, 65 | The boundary is claimed as "a bore surrounding" the element (16) or the seat ring (65), and in no independent claim. | Claim 17 recites the core body bore one level below claim 16, because [0124] and [0308] state it for the principal embodiment; the bore of the valve stem is claim 45 and the two are never in one chain. If the Orchestrator reads PF-3 as forbidding claim 17, it can be deleted without changing any other claim's scope. |
| PF-20 (low) | Yes | No claim | The thermal variant is not claimed. | — |

## Part 3 — Checks

Run on `claims.md`, `support-map.json` and `description.md`:

- `pc contract --kind drafting --reply P5/25.md`: ok, no repairs.
- `pc terms --locked terminology/LOCKED.md --reply P5/25.md --kind drafting`: ok, 0 violations, 0 warnings; 26 declared `new_terms` recorded as drift.
- `pc support-map`: ok. 86 claims, 0 unmapped claims, 0 uncovered limitations, 0 bad citations. 34 weak citations, advisory: 32 are dependency preambles ("The valve core of any one of claims ...") cited to the paragraph of their claim, 2 are secondary anchors (claim 6 to [0075], claim 60 to [0273]).
- `pc claims-format`: ok, 86 claims numbered 1 to 86, no problems.
- `pc antecedent`: ok, 0 flags.
- `pc numerals` (extra): ok, 0 problems.
- `pc support` (extra, heuristic): every limitation rated explicit or likely; the 9 rows rated unsupported are dependency preambles, not limitations.
