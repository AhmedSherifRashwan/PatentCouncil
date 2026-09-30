## x-loopback-p3 (Invention Analyst, 2026-09-29)

- F-33-2: candidate proposals only; no description or claims text changed by this step (no description.v3.md / claims.v3.md written). AE-1 recovery-wipe valve and valve core with no purge gap limitation (support [0011], [0034], [0034a], [0055], [0117]; needs a consistency sentence in [0048] or [0011] and an amendment to [0016]); AE-2 matching method (new [0015a], support [0011], [0111]); AE-3 over-travel deflection enlarging the main flow passage (new matter, after [0116] and in [0045], only if Gate 2 confirms Q2). For x-p4-revise and x-p5-revise, after the Gate 2 delta.

## x-p4-revise (Specification Drafter, 2026-09-29)

New version: `description.v3.md` (from `description.v2.md`; every existing paragraph number unchanged; five lettered paragraphs added). Reply: `loop/c1/x-p4-revise.md`. No claims version written by this step. `registry.json` unchanged (no new numeral).

- F-33-2: addressed for the description. Added [0011a], [0015a], [0048a], [0111a]; amended [0016] (first sentence). AE-3 (over-travel deflection enlarging the main flow passage) not written: new matter, no inventor confirmation.
- F-28-2: partly. Amended [0124] (second sentence replaced) and [0125] (first words). [0093], [0104], [0106] not changed. Whether the ranges hold for the second and third embodiments is still a question for the inventor.
- F-38-1: partly. Amended the column headings of Table 1 under [0101] (no value changed); added [0101a]. Test dates in [0099] not changed: the inconsistency is in the intake record.
- F-30-1: not changed. Cannot support without new matter (purge gap geometry of the prototype).
- F-28-3: not changed. Cannot support without new matter (direction of the normal stroke and arrangement of the first embodiment).
- F-28-1: not changed. Cannot support without new matter (purge gap position of the third embodiment).
- F-30-2: not changed. Follows from F-30-1 and F-28-1.

Support map, for x-p5-revise: the positional ids of lettered paragraphs have moved. For `description.v3.md`: ¶17 = [0011a], ¶22 = [0015a], ¶45 = [0034a] (was ¶43), ¶61 = [0048a], ¶110 = [0094a] (was ¶107), ¶120 = [0101a], ¶133 = [0111a], ¶158 = [0132a] (was ¶153). `support-map.json` as it stands cites the v2 ids and fails against v3 (9 bad citations) until they are remapped.

## x-p5-revise (Claims Architect, 2026-09-29)

New version: `claims.v3.md` (from `claims.v2.md`; claims 1 to 60 word-for-word unchanged, none deleted, narrowed or renumbered; claims 61 to 81 added). Reply: `loop/c1/x-p5-revise.md` (status partial). Read against `description.v3.md`; no description version written by this step. `registry.json` unchanged. `support-map.json` rebuilt for `claims.v3.md` against `description.v3.md` (81 claims, 189 elements); the previous map is kept as `support-map.v2.json`.

- F-33-2: addressed. New independent claims 61 (valve), 70 (valve core) and 79 (method of operating), founded on the recovery wipe, with no purge gap limitation; dependent claims 62 to 67, 71 to 77 and 80 to 81; inflatable body claims 68 and 69; valve with valve stem claim 78. Support: [0011], [0011a], [0012], [0015a], [0016], [0048a], [0055], [0111a], [0117]. Rests on the inventors confirming the aspect (Q1).
- F-28-3: no claim changed. Claims 7, 14, 17, 39, 41, 57 and 59 stay as they are because the description still holds the conflicting statements (x-p4-revise CL-10) and only the inventors can say which is wrong. New claims 61 to 81 recite no orientation. Open; alternative for claim 7 in `narrowing_suggested`.
- F-30-1: no claim changed. Claims 16, 17, 40 and 41 quote [0031] and [0111], which are unchanged (x-p4-revise CL-9). Open; recast wording in `narrowing_suggested` for the human.
- F-30-2: no claim changed or narrowed. Follows from F-30-1 and F-28-3. New claims 61, 70 and 79 do not recite the purge gap, which reduces the exposure and does not remove it.

Checks on `claims.v3.md` / `description.v3.md`: contract pass, terms pass, claims-format pass (81 claims, independent 1, 2, 4, 61, 70, 79), antecedent pass (0 flags), numerals pass (0 problems), support-map pass (0 unmapped, 0 uncovered, 0 bad citations).

## x-formal-fix (Specification Drafter, 2026-09-29)

New versions: `description.v4.md` (from `description.v3.md`) and `claims.v4.md` (from `claims.v3.md`). Reply: `loop/c1/x-formal-fix.md` (status partial). No paragraph added, removed or renumbered; no claim added, deleted, moved or renumbered. `registry.json`, `P4/20.md` and `P4/20a.md` unchanged. `support-map.json` rebuilt for `claims.v4.md` against `description.v4.md`; the previous map is kept as `support-map.v3.json`. The positional ids of the lettered paragraphs are the same as for v3.

53 corrections supplied (Prompt 37: 15; 38: 22; 40a: 16): 36 applied, 17 not applied.

- Paragraphs changed (15): [0004], [0005], [0006] (pinpoints removed, 38-12 to 38-17); [0007] (38-1); [0009] (38-7); [0015] (38-11); [0017] (38-2 to 38-4); [0021] (40a-7); [0029] (38-18); [0041] (38-8); [0042] (38-9); [0050] (38-5); [0078], [0113] (38-10); [0079] (38-6). In [0113] one word ("and") was added to join the two clauses the correction left.
- Claims changed (15): 4 (F-37-1, corrections 37-1 to 37-3; reference sign 66, 40a-13); 79 (F-37-1, same wording as claim 4; **not in the corrections supplied**, claim 79 was added after the review with the same clauses); 1, 2 (reference sign 66, 40a-11, 40a-12); 8, 9, 10, 11, 12, 30, 31, 32, 33 (dependency ranges, 37-4 to 37-12); 25, 44 (superelastic branch excluded, 37-13, 37-14).
- F-37-1: addressed in claims 4 and 79; dependent claims 52 to 56, 80 and 81 inherit the fix.
- F-30-3: no change. The Description has no statement that the disclosure does not explain how the purge gap opens and no dossier reference. Drawing sheets, the figure plan and the drawing instructions are outside this step (route-notes.md).
- Not applied, claims: 37-15 (claim 7; `pc antecedent` flags the replacement, and the orientation is part of upheld F-28-3); 40a-2 (US claim set, for counsel); 40a-10 (reordering claims 57 to 60 with renumbering; for the package step); 40a-16 (heading; `pc assemble` supplies it).
- Not applied, Description: 40a-4 to 40a-6 (sequential paragraph numbers; computed for v2, wrong for v3; for the package step); 40a-1 (drawing sheets); 40a-3 (abstract, Prompt 39a).
- Not applied, drawing instructions and registry: 38-19 to 38-22, 40a-8, 40a-9, 40a-14, 40a-15. These need a Prompt 20a re-run scoped to FIG. 1, FIG. 2, FIG. 3, FIG. 4A, FIG. 4B, FIG. 6 and FIG. 8. Until then [0021] (one view each for FIG. 4A and FIG. 4B) and the drawing instructions (two views) differ.

Checks on `claims.v4.md` / `description.v4.md`: contract pass, terms pass, claims-format pass (81 claims, independent 1, 2, 4, 61, 70, 79), antecedent pass (0 flags), numerals pass (0 problems), support-map pass (0 unmapped, 0 uncovered, 0 bad citations).
