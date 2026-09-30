# Prior-art reference set — self-purging-valve-20260928 · run r1 · RES2 (Quick profile)

Prepared by the Prior-Art Researcher as a drafting and analysis aid. It is not a professional search, not a novelty or patentability opinion and not legal advice; qualified patent counsel signs off before anything is filed. Every entry below is `candidate` and was retrieved by an AI agent from a public database; none has been verified by a human.

**Yardstick.** Nucleus N0 and ladder N1–N10 (`P1/03.md`); search tracks 1–6 and the query strings of Prompt 06 (`P2/06.md`). Short concept tags used below:

- **C1** valve for an inflatable body containing sealant (tyre/tubeless valve, sealant fouling problem)
- **C2** valve member with a normal stroke from a valve seat
- **C3** over-travel above a second, higher threshold (two-stage opening)
- **C4** deflectable element deflected by the valve member, opening a gap closed at rest
- **C5** purge flow across sealing / sealant-accumulation surfaces
- **C6** recovery re-closing the gap
- **C7** recovery wipe / deposit removal from a sealing surface by sliding contact (N1)
- **C8** deflectable element is itself the valve seat; tubular seat ring deflecting radially (N4–N5)
- **C9** superelastic / NiTi element (N6)
- **C10** replaceable valve core in a valve stem (N7)
- **C11** laser-cut, shape-set NiTi manufacture (N9)

All references accessed **2026-09-28** from Google Patents; full text and claims are saved in `refs/<publication-number>.md`.

| # | Publication | Title | Assignee | Priority / filing / publication | URL | Concepts hit | Why it matters | Closeness 1–5 |
|---|---|---|---|---|---|---|---|---|
| 1 | US11338632B2 | Inflation system for tubeless tires | Santa Cruz Bicycles LLC | 2019-04-17 / 2021-02-23 / 2022-05-24 | https://patents.google.com/patent/US11338632B2/en | C1, C2, C10 (as the alternative it replaces) | States that Presta/Schrader valves "are often clogged by sealant due to their small diameter" [0004]; answers with an external valve seat and a resilient seating surface on a movable stem [0070], [0086] and a larger bore [0232]. Closest real art for the problem and context of N0. No over-travel, purge gap or wipe in the text read. Family: US20210323363A1, US11904644B2; related US12215796B2. | 3 |
| 2 | US11179979B2 | Valve for tubeless tires | Sport Components AG | 2016-08-18 / 2019-11-25 / 2021-11-23 | https://patents.google.com/patent/US11179979B2/en | C1, C4 (pressure/probe-opened, not over-travel), C6, C10 | Self-sealing one-way valve at the tyre-side end whose sealing lip and slit open "by displacing or deforming the at least one sealing lip" [0016], in series with a removable valve core; sealant-heavy context. | 3 |
| 3 | US3417778A | Check valve with resilient seat means | J. B. Ratelband (individual) | 1964-12-04 (parent) / 1967-10-05 / 1968-12-24 | https://patents.google.com/patent/US3417778A/en | C2, C4, C6, C8, C7 (partial) | The seat is "a tubular sleeve-like element of resilient material ... the sole valve seat and being radially expandable under fluid pressure" (claim 1); the valve body bears inside the lip; helical fins give "a scraping action" [9]. Structurally closest real art found to the seat ring of N4–N5. Not a tyre valve; no distinct purge gap; no second threshold. | 3 |
| 4 | US20080188352A1 | Two stage check valve for automatic transmission system | Schaeffler KG | 2007-02-05 / 2008-02-04 / 2008-08-07 | https://patents.google.com/patent/US20080188352A1/en | C3, second flow path | First valve means opens at a first pressure; a second valve means opens a second orifice at a higher second pressure [8], [26], [31]. Relevant to the over-travel threshold clause of N0. Different field; no deflectable element or cleaning. | 2 |
| 5 | US4050473A | Valve seat cleaning mechanism | Alfa Wassermann Inc | 1975-05-15 / 1975-05-15 / 1977-09-27 | https://patents.google.com/patent/US4050473A/en | C7 | Flexible disk on the valve head wipes the valve seat each stroke: particles "will be wiped away as the flexible disk moves against and finally past the valve seat" [13]. Wipe by a flexible element driven by valve-member motion (arrangement reversed relative to the disclosure). | 2 |
| 6 | US4236547A | Self-cleaning valve plug and seat assembly | Ogontz Controls Co | 1979-04-09 / 1979-04-09 / 1980-12-02 | https://patents.google.com/patent/US4236547A/en | C7 | Cutting edge on the plug "cleans the skirt portion of foreign matter which may be deposited thereon" on closing [6], [25]. Deposit removal from sealing surfaces by sliding on closing. Rigid parts. | 2 |
| 7 | US3570510A | Self-cleaning valve and method therefor | Ishikawajima-Harima Heavy Industries Co Ltd | 1967-06-30 / 1968-05-03 / 1971-03-16 | https://patents.google.com/patent/US3570510A/en | C5, annular purge gap at the seat | Clean gas blown through an annular slit between two seat rings, faster during closing, "to sweep the seal rings ... so that the sealing surfaces are free from contamination" [10]–[12], [26]. The purge-flow idea, but supplied from a separate store, not the inflation flow via a gap opened by over-travel. | 2 |
| 8 | US6053992A | Shape memory alloy sealing components | Memry Corp | 1995-12-06 / 1997-09-30 / 2000-04-25 | https://patents.google.com/patent/US6053992A/en | C9 (context only) | NiTi-based SMA plugs sealing high-pressure passages by recovery-driven interference [10]; two-stage stress–strain behaviour [5]. Only real art found touching NiTi as a sealing element; static and thermally recovered, not a superelastic valve seat. | 1 |

## Requester-supplied references (not part of the searched set)

`intake/prior-art/ref-01-sealant-resistant-core.md` and `ref-02-elastomer-seat-valve.md` are marked **FICTIONAL** in their own text ("this reference does not exist"). They were not searched for, fetched or verified here, and no real reference was found under their numbers' descriptions. Downstream charts may use them only as test inputs; they cannot support a novelty position on a real filing.

## Triage view for Prompt 07 (chart / do not chart)

- **Chart:** #3 US3417778A (high structural relevance to N4–N5), #1 US11338632B2 (problem/context, N0 preamble), #2 US11179979B2 (deformable element in a sealant tyre valve), #4 US20080188352A1 (second threshold), #7 US3570510A (purge flow), #5 US4050473A and #6 US4236547A (wipe, N1). A plausible combination objection an examiner might attempt is #1 or #2 with #3 and #4; charting them is how Prompt 07/08 tests that — this index draws no conclusion on it.
- **Do not chart:** #8 US6053992A — context for the NiTi material only; no valve action.

## Coverage — what this set does not contain (read this before relying on it)

- **C3 + C4 + C5 together (the N0 mechanism):** no reference found in which over-travel of a valve member beyond its normal stroke deflects a resilient element to open a *separate* purge gap that is closed at rest. Each clause appears separately (#4, #3, #7), never combined, in any field searched.
- **C1 + C7:** no tyre or inflation valve found that wipes or purges sealant film from its sealing surfaces. The tubeless art found (#1, #2) avoids clogging by geometry or by a separate one-way valve.
- **C9 as a valve seat:** no superelastic NiTi valve seat or seat ring found; #8 is a static plug.
- **C11:** no manufacturing art (laser-cut, shape-set NiTi seat rings) was searched to completion; nothing saved.
- **Track 6 (adjacent fields: sealant/adhesive dispensing valves, aerosol valves, medical check valves):** only touched incidentally; not searched properly.
- **Jurisdictions and sources:** Google Patents via a general web-search engine only. No Espacenet, DEPATISnet, CNIPA/JPO full-text or classification browsing of F16K15/20 and B60C29/00 was run, and there is no non-patent literature (product documentation for commercial "high-flow / no-clog" tubeless valves exists but was not fetched). Asian and German-language utility models for bicycle valves are a likely blind spot.

The absence of a document here is not evidence that none exists. A professional search, including classification searching in F16K15/20, B60C29/00 and F16K15/14, is still needed before filing.
