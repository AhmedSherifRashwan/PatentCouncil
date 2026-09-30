# Review round 1: route notes (CP-ROUTE-1, 2026-09-29)

Profile quick, mode unattended, cap 1 per category. Route plan: `route-plan.json`. Loop-back state: `../../loop/loopback.json`.

## Adjudication
- 78 findings (2 critical, 19 high, 35 medium, 22 low). One reviewer only (ip-reviewer); no consensus findings.
- 21 rulings (`rulings.json`, from `rulings-1.json`): 10 upheld, 11 rejected. 57 medium/low findings unruled, which is expected because the Adjudicator rules only on critical and high findings.
- Upheld: F-28-1, F-28-2, F-28-3, F-30-1 (critical), F-30-2, F-30-3, F-33-1 (medium), F-33-2, F-37-1, F-38-1.
- Upheld medium F-33-1 was not routed. The route step acts only on upheld critical and high findings.

## Loop-back c1 (PAT-44 to PAT-48)
- x-loopback-p3 (Invention Analyst): F-33-2
- x-p4-revise (Specification Drafter): F-28-1, F-28-2, F-28-3, F-30-1, F-30-2, F-38-1, F-33-2
- x-p5-revise (Claims Architect): F-28-3, F-30-1, F-30-2, F-33-2
- x-formal-fix (Specification Drafter): F-30-3 (scoped, see below), F-37-1

With cap 1, support, enablement and design-around are all at their cap after this cycle. Any upheld critical or high finding still open in review round 2 is REVIEW REQUIRED.

## For the human (not applied)
Narrowing suggested by the route step:
- F-28-1: Add the inventors' statement of where the third embodiment's purge gap lies and how inflation gas reaches it without passing the rigid valve seat, for example a bypass passage in the core body closed at rest by the wiper ring; if none exists in their conception, re-hang claims 27 to 29, 45, 58 and 60 from a recovery-wipe claim (narrowing, for the human to decide).
- F-28-2: Obtain the inventors' confirmation whether the pressure, over-travel and purge gap width ranges apply to every embodiment; if so, amend [0124] and [0125] to state them for the valve generally, keeping the seat ring dimensions tied to the seat ring; if not, restrict the dependencies of claims 19, 30 to 34 and 47 to the first-embodiment claims (narrowing of dependent claims only).

Both depend on facts only the inventors can supply. The drafters must not supply them.

## F-30-3: filing blocker outside any drafting prompt
F-30-3 was upheld: "No drawings; the figure files are drafting instructions carrying internal references and damaging statements". No prompt produces drawing sheets, and x-formal-fix can return only the whole claims or the whole description. PAT-47 was scoped to correct any matching statement in the description and nothing more. The remaining items are for counsel:
- Drawing sheets for FIG. 1 to FIG. 8 must be prepared before filing (35 USC 113, Rule 56 EPC, UK s.15(5)). The ruling notes that FIG. 1 and FIG. 2 cannot be drawn truthfully until F-30-1 is resolved.
- The figure plan (P4/20.md) and drawing instructions (P4/20a.md) are internal working files. They contain dossier references and the statement "the disclosure does not explain how the purge gap opens", so they must never be filed. The review package copies them verbatim, which is a known package-builder behaviour.

## Process note
The adjudicated `findings-report.md` was written to the same path as the pre-adjudication report and replaced it. The pre-adjudication report was regenerated from the unchanged `findings.json` as `findings-report.pre.md`.
