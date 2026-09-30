# D2a — Competitor escape routes

Matter `self-purging-valve-20260929` · run `r1` · Litigator · 2026-09-29. One-way attack: there is no defence round, so each route states what the description and the claims must contain to close it, or says that it cannot be closed.

Read: `runs/r1/CONFIRMED.md`, `runs/r1/P2/09.md`, `runs/r1/terminology/LOCKED.md`, `runs/r1/prior-art/INDEX.md` and the saved references quoted below, `intake/disclosure.md` and `intake/data/bench-test.md` (section references §n). Nothing here has been built or tested. Every closure is a **candidate**: where it needs matter the inventor has not stated, it is marked `needs inventor confirmation` and must not be drafted as though conceived. This is a drafting and analysis aid, not a view on patentability or freedom to operate; qualified patent counsel signs off on anything filed.

## Embodiment key

`CONFIRMED.md` does not number its embodiments. The routes below use these labels.

| Label | Embodiment | Where confirmed |
|---|---|---|
| E1 | One-piece superelastic NiTi alloy seat ring with a convoluted wall, purge shoulder on the poppet, return spring with a two-rate characteristic, annular purge gap to the core body bore (the built prototype) | 14 columns 2–4; 12 throughout; §2–§4 |
| E2 | Polymer seat ring | 12 shape recovery item 1; 14 column 5; §6 |
| E3 | Two-piece seat: rigid seat plus wiper ring | 12 seat ring item 1; 14 column 6; §6 |
| E4 | Thermal variant | 12 austenite finish temperature item 2; 14 last row; §6 |
| G | Genus closures and equivalent architectures | 11.r1 DA-1 to DA-19; 12.r1 |
| L | Parameter ladders | 13 |
| C / F | Combination matrix / failure-mode embodiments | 14 / 15 |

## Ranked escape routes

Ranked by how cheaply the competitor keeps the commercial result (a tool-free valve core that keeps sealing and opening in sealant) while standing outside the text. Routes already in the register (DA-n) are not repeated; R-routes are either absent from it or defeat the closure it proposes.

| Route | Escape | Avoids | Cost to competitor | Closable from the record? |
|---|---|---|---|---|
| R1 | Rider-released travel limiter: over-travel reached at ordinary opening pressure once a stop is backed off | E1, E2, E3 (the second threshold) | Near zero: the lock nut becomes an adjustable stop | Only with inventor confirmation |
| R2 | No return spring: poppet closed by tyre chamber pressure; second threshold from the seat ring alone | E1, E2, E3; every claim reciting a return spring or a two-rate characteristic; the locked definition of valve core | Negative: removes a part | Only with inventor confirmation; lock defect |
| R3 | Inversion: deflectable element carried by the poppet, stationary load-applying surface on the core body, element contracts inward | E1, E2, E3; G closures of DA-3, DA-5, DA-7 | Low: a slotted skirt on the poppet | Only with inventor confirmation |
| R4 | Deflectable wall formed in the core body or valve stem itself; or purge gap bounded by the valve stem bore | E1, E3; "seat ring", "core body bore", interference fit, locating shoulder | Low: one fewer part | Partly (valve stem bore is in §2); integral wall needs confirmation |
| R5 | Rigid floating seat displaced axially against a spring, uncovering ports | E1, E2, E3; shape recovery; deflectable element | Low: brass sleeve and stock spring | Only with inventor confirmation |
| R6 | Secondary path opened by pressure acting directly on an elastic band or ring, not by the poppet | E1, E2, E3; row 3 of 09 | Very low: an elastomer band over a port | No: closing it reads onto saved art |
| R7 | Purge gap restricted at rest, not closed; widened in over-travel | E3 chiefly; any claim reciting "closed at rest" | Zero: a tolerance choice | Yes, by definition and description |
| R8 | Cold-worked, linearly superelastic NiTi alloy with no transformation | E1 material species; E4; locked definition of superelastic | Low: a different temper of the same alloy | Partly: by definition; values need confirmation |
| R9 | Threshold set by flow, with no static over-travel differential to measure | E1, E2, E3 threshold limitation; L pressure rows | Zero: it is a proof problem, not a redesign | Yes, by a stated test method |
| R10 | Purge range that is not "beyond the normal stroke": purge first, or on the return stroke only | E1, E2, E3; the DA-2 closure | Low | Only with inventor confirmation |
| R11 | Unit of sale: valve core alone, or seat ring and poppet as a service kit | All, where the claim recites valve stem, tyre chamber or sealant | Zero | Yes, by claim category |
| R12 | Step outside the ladders, or make the parameter unmeasurable | L | Zero | Partly |
| R13 | Thermal variant with a one-way alloy and a bias spring, or another heat source | E4 | Low | Only with inventor confirmation |
| R14 | No cleaning mechanism at all: keep sealant out, or enlarge the bore | All | Already on the market in the saved art | No: prior art |
| R15 | Species substitution in the closed material lists | E2, C | Zero | Yes, as dependents only |

### R1 — Rider-released travel limiter (avoids E1, E2, E3)

**Escape.** Keep the seat ring, the purge shoulder and the purge gap exactly as disclosed. Fit a single-rate return spring. A stop limits the poppet to the normal stroke; the rider backs the stop off by a fraction of a turn with the fingers (the lock nut, §3 item 7, already sits on the poppet) and the next pump stroke drives the poppet into over-travel at ordinary opening pressure.

**Why it is outside.** 09 row 2 proposes "through an over-travel beyond the normal stroke only when the pressure differential exceeds an over-travel differential greater than the crack pressure". This core has no second pressure threshold: over-travel occurs at any pressure differential above the crack pressure once the stop is released, and never while it is set. DA-15 (mechanical force on the poppet) and DA-2 (purge on every opening) do not cover it: nothing pushes the poppet but air, and the purge does not occur on every opening.

**Why it works commercially.** No special spring. Purging monthly instead of on every inflation cycle cuts the over-travel count by an order of magnitude, which answers the unresolved fatigue question (§9 item 1; FM-1, FM-2) better than the disclosed core does. "Twist to purge" is a selling point, and still tool-free.

**Closure.** Independent claim: the second travel range defined by what happens in it (the poppet bears on the element; the purge gap opens), without reciting how it is reached. Dependent claims: reached above an over-travel differential; reached on release of a travel limiter; reached by force on the poppet. Description: a travel limiter embodiment. `needs inventor confirmation`: nothing in §2–§6 describes selectable over-travel.

### R2 — No return spring (avoids E1, E2, E3)

**Escape.** Presta-pattern cores on the market are closed by the pressure in the tyre chamber and a nut, without a spring (premise A1). The competitor keeps that layout: tyre chamber pressure returns the poppet; the axial stiffness of the seat ring, met by the purge shoulder at the end of the normal stroke, is the only added resistance.

**Why it is outside.** The locked functional description of valve core is an "assembly of core body, seat ring, poppet and return spring", and crack pressure is defined "against the first spring stage". A claim using either term imports a spring. The DA-1 closure ("provided by the return spring, by the seat ring, or by both") and the DA-6 genus ("a return bias having a two-rate characteristic") still presuppose a spring or a bias element; here the first stage is gas pressure on the poppet area.

**Why it works commercially.** It is the existing core plus one ring. The disclosed core adds a spring the market's Presta-pattern cores do not have, and with it pumping effort.

**Closure.** Independent claim recites no spring and no bias element: "a resistance to movement of the poppet that is greater in the over-travel than in the normal stroke", with the sources (return spring, seat ring, pressure in the tyre chamber) in the description and dependents. The lock rows for valve core, crack pressure and over-travel differential need definitions in the description that make the spring optional; as locked they are a defect for claim scope, reported here rather than worked around. `needs inventor confirmation` that a springless core is within the conception (§3 item 5 says "as in a conventional core", which suggests the inventor assumed a spring).

### R3 — Inversion: the poppet carries the deflectable element (avoids E1, E2, E3 and the G closures)

**Escape.** The seat stays rigid brass. The poppet carries a thin slotted skirt or collet below the sealing face. In over-travel the skirt runs into a conical or stepped surface of the core body and is squeezed radially inward, opening a gap between the skirt and the bore it sealed against at rest. On return it springs outward and wipes the bore.

**Why it is outside.** Every rung assumes a stationary seat ring loaded by a moving surface. The closures the register proposes all fail on this: DA-7 "a load-applying surface moved by the poppet" (here it is stationary); DA-3 "radial expansion" (here contraction); DA-5 "opened by deformation of the seat ring" (no seat ring deforms); 09 row 1 "between an outer surface of the seat ring and the core body bore". Seat ring item 2 (slotted sleeve) shows the mechanics are ordinary.

**Why it works commercially.** The poppet is the part riders already replace; a poppet-only upgrade fits existing core bodies and sells as a retrofit.

**Closure.** Genus by relative movement: "a deflectable element carried by one of the core body and the poppet, and a load-applying surface on the other, brought together in the over-travel", radial deflection "outward or inward". `needs inventor confirmation`.

### R4 — Deflectable wall integral with the core body; gap bounded by the valve stem bore (avoids E1, E3)

**Escape (a).** The core body is drawn or turned with a thin convoluted end section that is itself the seat and the deflectable wall. There is no separate seat ring, no interference fit and no locating shoulder. **Escape (b).** The seat ring projects beyond the end of the core body and expands against the valve stem bore, as §2 literally says ("between the ring and the stem bore").

**Why it is outside.** (a) A claim to "a core body" and "a seat ring" carried by it, with a purge gap "between an outer surface of the seat ring and the core body bore", requires two parts and a gap between them. (b) 09 A1 treats §2 as loose wording and fixes the boundary as the core body bore; if the claim follows A1, the valve core as sold contains no purge gap boundary at all, and the maker of the valve core is at most an indirect infringer.

**Why it works commercially.** (a) removes a part and the press-fit operation, and removes the unresolved conflict between the interference fit and the purge gap on one surface (09 Q2). (b) needs no relief in the core body.

**Closure.** Description: the radially deflectable element "separate from or integral with the core body"; the purge gap bounded by "a surface surrounding the element, being a surface of the core body or of the valve stem". 12 purge gap item 2 already carries (b) as a candidate and must reach the claims, not only the description. (a) `needs inventor confirmation`.

### R5 — Rigid floating seat (avoids E1, E2, E3)

**Escape.** A rigid seat sleeve slides in the core body against a stiff spring. The poppet shoulder pushes it back in over-travel and it uncovers ports or a groove in the core body bore. US4044791A (INDEX #2) shows the architecture: "a floating valve seat and an engageable poppet ... means disposed on the body for yieldably biasing the valve seat into engagement with the poppet".

**Why it is outside.** Nothing deflects and nothing recovers its shape: N0 features 2 and 3 are both absent. DA-10 (poppet passes a groove) and DA-16 (positive return) are near it but neither describes a displaced seat; the DA-9 genus "a deflectable element whose deformation ..." does not read on a rigid sleeve.

**Why it works commercially.** Turned brass and a stock spring; no NiTi alloy, no shape-setting, no fatigue question. The sleeve sliding back over the bore gives a wipe of its own.

**Closure.** "A seat element that is deformable or displaceable by the poppet in the over-travel to open the purge gap, and that returns when the load is removed". `needs inventor confirmation`, and the closure moves the claim towards US4044791A, whose second path opens for a different purpose: the description would have to carry the sealant-swept location of the purge gap (09 row 1) as the distinction.

### R6 — Pressure-opened secondary path (avoids E1, E2, E3)

**Escape.** A port in the core body beside the seat is covered by an elastic band or ring whose opening pressure is above the crack pressure. Pump pressure lifts the band directly; the poppet never touches it and has no over-travel. US5924444A (INDEX #15) shows a ring seal opened by the flow itself: "Flow exiting out of channel 184 at the sealing surface 158 in valving region 154 will move upwardly so as to produce a gap between sealing surface 158 and O-ring 160".

**Why it is outside.** 09 row 3 distinguishes the art precisely by mechanical causation: "a purge shoulder of the poppet engaging the seat ring only during the over-travel". Remove the poppet from the load path and that limitation is not met.

**Why it works commercially.** The cheapest route here: one elastomer band. Its weakness is the inventor's own point that elastomer embeds sealant (§2), so the competitor would use a thin metal or polymer band.

**Closure.** None that is safe. A claim broad enough to cover a pressure-opened element reads onto US5924444A and onto ref-02 [0019] as 09 describes it. Record it as an open route for the assessment; the description should state why poppet-driven opening is repeatable where pressure-driven opening is not (09 row 3, technical effect), so that the distinction is at least argued.

### R7 — Restricted, not closed (avoids E3; weakens E1, E2)

**Escape.** Where the seal is made on a rigid seat (E3), the wiper ring sits in series with that seal, so its gap need not shut. The competitor leaves a small permanent clearance and widens it in over-travel.

**Why it is outside.** The purge gap is locked as a "clearance, closed at rest, that opens". A gap that is never closed does not open; it enlarges. The record also undermines the patentee's own reading: cured sealant film was found "on the ring outer surface in the purge-gap region" at cycle 40 (bench data; FM-4), and FM-2 contemplates incomplete closure, so the patentee's product may not be "closed" in service either.

**Closure.** Define "closed at rest" in the description as including a residual clearance through which no more than a stated flow passes, or describe the purge gap as "closed or restricted at rest and enlarged in the over-travel". Any numerical residual `needs inventor confirmation`.

### R8 — Linearly superelastic, cold-worked NiTi alloy (avoids E1 material species, E4)

**Escape.** Use NiTi alloy in the cold-worked condition. US6019118A (INDEX #16): "Due to the relatively high cold working, these materials are deprived of the shape memory effect, i.e., these materials are deprived of the temperature dependent transformation from martensite to au[stenite]", with "a high elastic deformability, even at very low temperatures".

**Why it is outside.** Superelastic is locked as recovery "at temperatures above its austenite finish temperature". An alloy with no transformation has no austenite finish temperature, so it meets neither "superelastic" as defined nor "austenite finish temperature below 5 °C". The DA-4 list of substitutes does not include it.

**Why it works commercially.** It removes the cold-shock failure the inventor cannot answer (§9 item 2; FM-12, FM-13), so the escape is a better product for riders who inflate from a CO₂ cartridge.

**Closure.** Define the material by behaviour, "a metal that recovers the strain imposed by the radial expansion on unloading", with transformation-superelastic and cold-worked NiTi alloy as species; keep the austenite finish temperature in a dependent claim only. The definition of superelastic is closable by drafting; any recoverable-strain value `needs inventor confirmation`.

### R9 — No static over-travel differential to prove (avoids the threshold limitation of E1–E3; L)

**Attack.** Once the poppet lifts at the crack pressure the main passage is open, and the pressure differential across the poppet is whatever the flow produces. The 3.5 bar figure (§4) is therefore a function of pump stroke rate and main passage restriction, not a property of the valve core alone. A competitor sizes the main passage so that the differential at ordinary pumping rates is ambiguous, then argues non-infringement on any numeric threshold and indefiniteness on the functional one.

**Closure.** The description must state how the crack pressure and the over-travel differential are measured (static or at a stated flow, where the two pressures are taken, at what temperature). Without it the ladders for both pressures are unprovable in an accused core of 2.3 mm bore. The measurement conditions of the prototype values are not on the record: `needs inventor confirmation`.

### R10 — Purge range that is not beyond the normal stroke (avoids E1–E3 and the DA-2 closure)

**Escape.** The shoulder loads the seat ring in the first part of the poppet travel and releases it at full lift (purge first, then ordinary flow); or the ring is loaded only on the return stroke.

**Why it is outside.** Over-travel is locked as travel "beyond the normal stroke". The DA-2 closure ("a threshold equal to the crack pressure") still places the purge at or after the end of the normal stroke.

**Closure.** "In a purge range of the travel of the poppet", the range beyond the normal stroke being preferred. `needs inventor confirmation`.

### R11 — Unit of sale (all embodiments)

**Escape.** Valve cores are sold in multipacks (§1), separately from the valve stem and the tyre chamber; seat rings and poppets can be sold as a service kit and assembled by the rider.

**Closure.** Independent claims to the valve core alone, with valve stem, tyre chamber and sealant recited only as "for"; an independent claim to the seat ring as a part, by its sealing edge and load-converting wall; a kit claim. 09 row 7's "a valve core for a tyre valve of a tyre chamber containing sealant" is the right form. No new disclosure needed.

### R12 — Parameter ladders (avoids L)

Every intermediate and preferred rung in 13 is a proposed band with no stated basis, so a competitor steps 0.01 mm outside it. Two specific points: the purge gap width is "radial", which has no single value for a slotted, lobed or through-wall purge gap (DA-5); and 12 records that 0.15 mm on a 1.35 mm radius is about 11 % hoop strain, so the prototype figure itself is open to the attack that it cannot be what is claimed. **Closure:** ranges in dependents only; state how and where each dimension is measured; resolve radial against diametral (12 Q5, `needs inventor confirmation`).

### R13 — Thermal variant (avoids E4)

**Escape.** A one-way alloy with a bias spring gives the same opening on warming without two-way training; heat from a warm pump head or warm water instead of the hand; a transformation temperature outside 35 °C to 40 °C. **Closure:** "a seat ring that opens the purge gap on warming above a transformation temperature", training and heat source in dependents. `needs inventor confirmation`; the inventor is unsure whether to keep E4 at all (§6).

### R14 — Substitutes that need no mechanism (all embodiments)

Not closable, and they bound what the claims are worth. US11179979B2 (INDEX #19) puts "a self-sealing one-way valve ... which is operable although a sealant is present" at the tyre end of the valve stem, and states that it "usually will prevent sealant from entering into the valve stem". US20210323363A1 (INDEX #6) enlarges the bore for "higher air flow and reduced clogging". Both give a tool-free answer to fouling with rigid parts. The description should state why exclusion and a larger bore fall short (§1 says they only slow build-up) only so far as the inventor can support it; the statement in §1 is unevidenced against these two documents.

### R15 — Species lists (avoids E2, C)

PEEK, stainless steel 303 and hard-anodised aluminium are single species. Any other polymer, corrosion-resistant alloy or hard surface escapes a claim reciting them. **Closure:** genus in the description ("a polymer having radial compliance", "a corrosion-resistant metal"), species in dependents; 12 already lists PPS and PEI as candidates.

## Register closures that do not hold as worded

| Closure in 11.r1 | Defeated by |
|---|---|
| DA-1 "by the return spring, by the seat ring, or by both" | R2 (pressure in the tyre chamber is the first stage) |
| DA-2 threshold "from the crack pressure upwards" | R1 (no pressure threshold), R10 (purge not beyond the normal stroke) |
| DA-3 "radial expansion" | R3 (inward contraction) |
| DA-5 "opened by deformation of the seat ring" | R3, R4(a), R5 |
| DA-7 "a load-applying surface moved by the poppet" | R3 (stationary surface), R6 (no surface) |
| DA-9 "a deflectable element whose deformation ..." | R5 (rigid, displaced) |
| DA-15 "pressure differential or a mechanical force" | R1 (neither: release of a stop) |

## What cannot be closed from the record

R6 and R14 cannot be closed without claiming the saved art. R1, R2, R3, R4(a), R5, R10 and R13 can be closed only with matter the inventor has not stated; with `intake/answers.md` absent, none of them may be drafted as conceived. R7, R8 (definition), R9, R11, R12 and R15 can be closed by drafting alone.

## Assumptions

A1. Presta-pattern valve cores on the market are closed by pressure and a nut, without a spring. Common general knowledge, supported only by a web search summary (BikeRadar, https://www.bikeradar.com/advice/buyers-guides/presta-vs-schrader-valves ; Wikipedia, https://en.wikipedia.org/wiki/Presta_valve ; accessed 2026-09-29, pages not fetched in full or saved). To be verified before R2 is relied on.
A2. The label scheme E1–E4, G, L, C, F is mine; `CONFIRMED.md` carries no embodiment numbers.
A3. Commercial attractiveness is judged from part count and process steps on the record; no cost data exists in the dossier.
A4. The two requester-supplied references are fictional (09 A4); ref-02 is cited only through 09's account of it.

## Open Questions

Q1. Did the inventor contemplate over-travel that the rider selects, rather than over-travel reached on every inflation cycle? Decides R1.
Q2. Does the prototype need its return spring, or would the pressure in the tyre chamber return the poppet? Decides R2 and the lock defect.
Q3. Was any arrangement considered in which the poppet, not the seat, carries the part that deflects? Decides R3.
Q4. How were the 1.0 bar and 3.5 bar figures measured? Decides R9.
Q5. Is the purge gap meant to be fully shut at rest in the two-piece seat? Decides R7.
