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