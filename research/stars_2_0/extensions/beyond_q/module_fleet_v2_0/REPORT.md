# Beyond Q v2.0 — isotope-first module, fleet and reactor-only financials

2026-11-01. Research direction: Dave / Atlas Lattice / Nightmare Lab. Implementation and accounting review: GPT Work. Prior documented analytical contributions: GPT-6/Tidal Lantern (research and reconciliation), DeepSeek (independent cross-audit), Gemini Argon (candidate burn/extraction equations and review). No experiment, author, company or institution has endorsed or validated this architecture.

## Result and scope

This release connects a dynamic, mass-conserving candidate dual-reactor model to financial calculations and staged 1–50-module operation over 60 years. It excludes GPU/QPU configurations, capital, financing and revenues. Every module has its own tritium inventory and startup event. It is a computational research scenario, not a demonstration of self-sustaining reactors or an industrial He3 recovery train.

Both default proposed sources remain 1,100 MW fusion: A primary D-D; B D-T. An explicit B=1,130 MW option preserves the public ARC reference. The older A=20 MW fusion and B=525 MW cases are not substituted. A's historical +20 MWe NET projection remains unvalidated; the executed energy sensitivity instead ASSUMES A draws 100 MWe while operating, with explicit shutdown and shared loads. No new WarpX or OpenMC calculation was performed. Existing short kinetic experiments do not calibrate long-term plasma confinement, D-He3 consumption or plant draw.

## Operating and recovery conventions

- Fixed-exposure A operation, NOT v1.9's 350k target controller. Prior releases are untouched. Availability permissions are synthetic daily independent A/B Bernoulli draws plus a common daily fleet event; they do not model realistic multi-day failure/repair distributions.
- A macro availability is 85%; B is 90%; shared outage probability is 2%, with independent residual permissions chosen to preserve those marginal probabilities. ARC source duty 15/16 is applied ONCE in addition to macro availability. These are ASSUMED schedules, not forecasts.
- The preferred overall eventual He3 recovery cases are 37.5% conservative potential, 75% planning and 90% optimistic. Exact source, two pipeline inventories and eventual exits are modeled. The scenario fraction is applied ONCE to pipeline exits; the remainder is a lumped sink. No second quality multiplier is imposed. The fraction does not imply measured capture, isotopic purity, radiological acceptance or product certification. Physical D-He3 consumption is not resolved; lumped loss cannot be used to infer its reaction rate or energy.
- The mobile and purification stages use assumed 1/day and 4/day rates. They are NOT adsorption isotherms, pump capacities, saturation/regeneration cycles, membrane areas or distillation-column calculations. Candidate patent mechanisms are documented below as future interfaces, not parameter validation.
- 50% of recovered He3 is retained internally as requested; the remaining candidate allocation enters a sale bank. This policy is not evidence that a host campus requires that amount. Market-limited unsold He3 accumulates; stable He3 does not undergo radioactive decay in this ledger.
- A0 has zero A blanket breeding. B gross TBR=1 is an assumption, distinct from recovered tritium. Transport yields remain unresolved. A plasma processing recovery and B blanket/recirculation processing recovery are independent.
- Tritium is born, internally burned, extracted, recycled, processed, transferred, stored, decayed, lost or conditionally exported. A and B share no external source after commissioning. T-decay He3 is not credited as product.
- B starts only after B storage reaches one uninterrupted full-power YEAR of burn plus a 10 kg reserve: 71.654 kg at 1.10 GW. This is a policy threshold, not a proof of one-year operation without breeding: single-pass feed, holdup and processing also matter. The model separately checks served fuel demand.
- A-only startup begins with zero tritium. Zero initial T is an idealization of D-D commissioning; no amount of this accounting establishes a feasible D-D startup plasma.
- Conditional T exports are physically withdrawn once annually, capped at 20 kg/module/year and 100 kg/fleet/year, retaining the startup threshold in B storage. These are assumed sales scenarios, NOT certified surplus. No consumed atom is also exported. No intermodule T sharing is implemented; enabling it raises a visible error.
- Illustrative 30-day replacement outages occur every two operating-calendar years, with B's replacement clock starting at actual B startup. This is NOT source-qualified FPY/damage-based lifetime modeling. Housing, replacement CAPEX, cooldown/ramp physics and replacement cost remain unresolved. Extraction and processing continue during reactor outages, an explicit simplifying assumption.

## Equations and ledgers

Constants: Avogadro 6.02214076e23 mol^-1; eV 1.602176634e-19 J; T mass 0.00301604928 kg/mol; He3 0.0030160293201 kg/mol; He4 0.00400260325413 kg/mol; FPY 365.25 days; gas STP 0 C / 1 atm, 22.414 L/mol. T atom-equivalent liters remain distinct from molecular T2 liters (factor two).

At equal D-D branches: R_DD=P_DD/(3.65 MeV), R_T=R_He3=R_DD/2. Primary DD neutron births equal R_He3, not all DD reactions. D-T consumes one T nucleus and produces one neutron and one He4 nucleus per event, Q_DT=17.6 MeV. This gives ~56.049 kg T/(GW fusion FPY), compared with the retained historical 55.8 convention; the latter is not silently used in this execution.

For each constant-rate compartment, dI/dt=S-sum(k_j)I. Exact integrated exits use phi=-expm1(-K dt)/K and integral I dt=I0*phi+S*(dt-phi)/K, with a small-K series for numerical stability. Inter-compartment coupling uses ordered splitting; its error is measured by timestep refinement, not eliminated by each compartment being exact.

A's inherited candidate fast-burn/escape partition and thermal burn-versus-escape hazards are copied as assumptions from the prior source register. For constant operating rates, the resulting eventual T consumption fraction is f_fast + (1-f_fast-f_fast_escape)*k_burn/(k_burn+k_escape+lambda), not an independent 18 MW assumption. Secondary DT power is derived from counted T burns. The rates themselves do not validate G1.

T balance for EACH module: initial inventory + direct DD births + B blanket births = final inventory + A burns + B burns + decay + permeation + process loss + terminal exports. A-storage-to-B transfers and B unburned recirculation are internal flows, never sources. The model does not import T to hide a deficit.

Deuterium consumption is independently derived from two D nuclei per primary DD event and one per DT event. Li6-equivalent consumption is reported assuming all prescribed blanket T births follow Li6(n,t)alpha. Actual lithium enrichment, Li7 pathways, replacement supply and finite blanket composition evolution remain unresolved. These flows make clear that the modeled lithium-breeding architecture requires lithium replenishment as well as deuterium; it is not indefinitely sustained by deuterium alone.

He3 balance before the overall fraction: direct births = mobile pipeline + purification pipeline + cumulative pipeline exits. Exits partition into recovered candidate and lumped loss once. He4 counts plasma A/B DT products separately; blanket-path He4 remains unavailable and earns no revenue. He3 secondary fusion is unresolved, so no inferred He4 from that route is fabricated.

Neutron ledger: N_DD = DD_fusion_J/(2*3.65 MeV), N_DT=(A_burn+B_burn)/m_T. Fusion neutron kinetic energy = N_DD*2.45 MeV + N_DT*14.1 MeV. Charged fusion energy = total fusion energy minus fusion neutron energy. Assumed blanket reaction Q is recorded separately and never added a second time as neutron kinetic energy. Qualified deposited thermal heat remains null: transport heating, leakage and energy multiplication are not established.

The electrical screen assumes the published B 500 MWe gross / 100 MWe own-load comparator at 1,130 MW fusion, scaling gross power to B's configured fusion power and actual served burn fraction. Pulse duty is already incorporated in that electrical comparator and is not applied twice. A's assumed net draw includes its internal conversion and auxiliaries by definition; additional shared processing load is separate. P_net=P_B_gross-P_B_own-P_A_net_draw-P_shared. Integrate exports and imports separately at each step; annual positive net energy is NOT continuous electrical independence. This is a prescribed electrical sensitivity, not a bottom-up thermal plant model.

## Executed results

Python 3.12 with NumPy 2.3.5; fixed seed 119; default time step 0.25 day. Physical trajectories: one module and 50 separately inventoried modules for 60 calendar years. Fleet commissions one module every 0.1 year, reaching 50 over 4.9 years. Recovery/price/offtake comparisons reuse each physical trajectory, since they do not feed back to fixed A dispatch. This differs deliberately from target-controlled v1.9, not a replacement or recalibration of that release.

| Conditional output | Single module year 1 | Single module year 10 | Single module year 60 |
|---|---:|---:|---:|
| He3 candidate at 37.5% overall recovery, STP L | 335,841 | 337,214 | 322,955 |
| He3 candidate at 75%, STP L | 671,682 | 674,428 | 645,909 |
| T export in the modeled export sensitivity, kg | 20 | 20 | 20 |
| Net electricity, MWh | 119,053 | 2,199,117 | 2,294,496 |
| Imported electricity, MWh | 629,520 | 73,590 | 52,680 |

B first starts at day 246.0 in this seeded single-module case. Scheduled B burn after startup is served without shortages in the executed baseline. This is a conditional inventory result, NOT operational self-sufficiency. The annual net electricity is positive but imports remain: startup, maintenance and outages prevent an islanded-operation claim. Battery/storage/grid and failure-duration studies are not yet implemented.

The 37.5% annual He3 output does not reproduce exactly 350k because this execution uses 85% MACRO availability AND separate 15/16 source duty, explicit holdup and replacements. Earlier ~939k gross figures used 85% EFFECTIVE fusion exposure. Do not interpret the exposure difference as failure of the earlier arithmetic. The current model reports actual output rather than forcing a target to pass.

The 50-module scenario reaches roughly 15.9 million L/year He3 candidate at 37.5% in year 60, while selected fleet-wide capped-sales stress remains 350k L/year. This cap is an illustrative sensitivity, NOT a demand estimate. The alternative full-He3-offtake sensitivity is exported too and must NOT be treated as guaranteed unlimited demand. Annual T market cap remains 100 kg across both sensitivities and is reflected in actual withdrawals. Fleet energy is not 50 times a synchronized best year: commissioning, independent permissions, common outages and separate replacements are represented. No procurement-learning discount is assumed.

## Connected finance and costs still needed

User-requested prices: He3 $1,500/STP L, tritium $1,500/g. Price-pressure comparison: $500/L and $500/g. These are nominal illustrative prices kept constant to expose sensitivity, not market forecasts for 60 years. Annual production does not automatically become sales. Financial receipts assume candidate exports meet qualification; actual qualified receipts and actual profit remain NULL.

Loan: 30 annual end-year payments at 5%, 100% debt by default. Annuity factor 0.0650514351 per year. The modeled lower-scope hardware subtotal is two HISTORICALLY ASSUMED $2.8B chassis plus $300M adaptation = $5.9B/module; initial annual debt on that subtotal is $383.803M/module. It is not a complete installed cost or CFS price. A and B housing, shared site/cooling/electrical infrastructure, construction interest/fees, OPEX, replacement cost and decommissioning allowances are exposed separately and left NULL. A scope-verification flag prevents reporting full-cost cash flow before checking that housing is not already in chassis cost. Missing values are not represented as known zero costs.

The output `revenue_less_known_charges_USD` subtracts priced imports and partial-scope debt plus any supplied costs, leaving unpriced energy and unknown costs explicitly unresolved. It is NOT profit or a full financial projection. `conditional_cash_flow_before_tax_USD` is only populated when all declared cost inputs and an electricity export valuation are supplied and scope is verified. `actual_profit_USD` remains null even then. GPU/QPU value and financing are excluded completely. No double credit is given for both internal electricity use and a sale of those MWh.

Initial borrowing ends after each module's 30 payment years, not after fleet calendar year 30 for every module. Staggered modules still have debt in year 31; all original module loans have ended by year 35 in this schedule. Refurbishment, replacements and future debt do not disappear. No residual value or immortal hardware is assumed. Long-horizon operation is modeled conditional on the assumed replacement program, not established as indefinite.

## Numerical evidence and adverse controls

Sixteen automated checks passed, including scalar-versus-vector compartment agreement with the inherited inventory kernel, donor-bounded T exports, startup from no external T, zero-source controls, zero B breeding, secondary A DT disabled while preserving DD neutrons, source-energy normalization, recovery applied once, sale caps/unsold inventory, unknown-cost protection, loan amortization, independently commissioned 50-module inventories, timestep refinement, a negative electrical case, invalid-input rejection and a fully costed but explicitly conditional cash-flow example. Historical DD source and neutron corrections remain regression identities.

Three-year refinement from 0.25 to 0.125 to 0.0625 day preserves day-246 startup and B total burn to roundoff. Coarse final T differs from the finest result by 0.02156%; cumulative He3 pipeline exits differ by ~0.01223%. This is a limited convergence check on one scenario, not a universal accuracy bound or validation of physical assumptions.

In 60-year runs, maximum per-module T closure residual is below 4.4e-9 kg; He3 pipeline and He4 residuals are below 9.0e-9 kg. See execution.json for exact values. Recovery ranges are scenario bounds, NOT statistical confidence intervals. One seeded daily-outage realization is not a reliability uncertainty distribution.

The audit records an initial dashboard failure from NumPy integer serialization, corrected by casting counts without changing physics. Prior failed assumptions and corrections are not overwritten.

## Equipment interfaces and sources

SOURCE-TRACED describes a document/announcement, not verification of its claims. VERIFIED-DERIVED describes arithmetic only. POTENTIAL-DERIVED covers simulations under assumed conditions. UNRESOLVED covers physical qualification and unpriced costs.

1. CFS, *ARC: Putting fusion energy on the grid*, https://cfs.energy/technology/arc/ . Approximately 400 MWe public D-T design comparator, not the D-D conversion or a capital quote. The inherited 500 gross/100 own/1,130 fusion numerical convention is recorded in `../paired_annual_v1_7/inputs.json`; its transfer/scaling is a modeling assumption.
2. Published ARC 2026 physics overview, https://doi.org/10.1017/S0022377826101706 . Source-bounded reactor reference, not validation of a D-D operating point or this fleet.
3. Meschini, S.; Ferry, S. E.; Delaporte-Mathurin, R.; Whyte, D. G. (2023), *Modeling and analysis of the tritium fuel cycle for ARC- and STEP-class D-T fusion power plants*, Nuclear Fusion 63, 126005. https://doi.org/10.1088/1741-4326/acf3fc . Compartment/fuel-cycle precedent; H/D/T isotope separation does not establish He3/He4 purification.
4. ASIPP/Hefei, April 21 2025, *Large composite cryopump capable of deuterium/helium separation*, https://hf.cas.cn/kxyj/kyjz/202504/t20250421_7605156.html . Reports 1.2 m body, 0.58 m valve, 4 tonnes, D 110,000 L/s and He 40,000 L/s pumping speed, independent regeneration. These vacuum speeds are NOT STP product throughput or recovery efficiencies. Capacity, He isotope, inlet conditions, regeneration purity/loss and cycle lifetime remain open.
5. CN107993733B, *Three-stage cryopump processing of radioactive fusion exhaust*, https://patents.google.com/patent/CN107993733B/zh . Existing design reference: 70–80 K, 10–20 K and charcoal-bearing 4.2–10 K stages. Helium adsorption is not ordinary fuel condensation. A granted patent does not establish throughput or purity.
6. KIT EP3061098B1, *Continuous reprocessing of fusion exhaust*, https://patents.google.com/patent/EP3061098B1/en ; Colorado School of Mines US20250360467A1, https://patents.google.com/patent/US20250360467A1 . Hydrogen permeates the metal foil; helium stays on the feed/residual side and requires a controlled outlet. These are candidate alternatives/configurations, not mandatory series equipment.
7. Gebhart, T. E. et al. (2026), *Preliminary Testing of a Continuous Cryopump for Primary Fusion Device Pumping and Direct Internal Recycling*, IEEE Transactions on Plasma Science 54(6), 2665–2671. https://doi.org/10.1109/TPS.2025.3635057 ; institutional abstract https://impact.ornl.gov/en/publications/preliminary-testing-of-a-continuous-cryopump-for-primary-fusion-d/ . Reported >99% DIR for tested D2 flows below 50.7 Pa m3/s with 1% He is a FUEL recycling result, not He3 product recovery.
8. Linde US20240261731A1, https://patents.google.com/patent/US20240261731A1/en . Distillation design predominantly for trace He3 in natural helium; actual fusion helium mixture needs a new calculation. No patent-based numerical efficiency is inserted here.
9. Historical local canonical register: `../reserve_dispatch_v1_8/sources/ARC_CANONICAL_2026-10-31.md`. Preserves $5.67B versus $5.87B arithmetic, approximate $300M adaptation scope, +20 MWe historical A projection and unit corrections. These are research assumptions, not vendor quotations.
10. USGS, *Mineral Commodity Summaries 2026: Helium and rare gases*, https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-helium.pdf . Estimated world He3 production ~40,000 L/year in 2024/2025. This contextual reference does not establish future offtake; 350k cap in this release is deliberately a stress input.

Additional Chinese purification/pump patents CN224822076U and CN120544972A remain leads pending accessible original documents. The claimed Shenzhen quasi-pulsed D-D/FRC recovery patent is unresolved and supplies no model parameter. Current source citations were inspected in the preceding research session; no external performance measurement has been manufactured.

## Gate status and next work

| Gate | Software progress | Physical status |
|---|---|---|
| G1 plasma / secondary burn | Counted inherited candidate T burn and source-normalized isotope/neutron events | OPEN: full D-D operating point, fast-ion distributions, He3 secondary burn and wall transport |
| G2 neutronics | Interface currently accepts assumed B TBR; A0 breeding disabled | OPEN: qualified geometry/data/transport yields, spectra and benchmarks; no new OpenMC result |
| G3 extraction / recovery | Explicit transient stages and 37.5/75/90% overall bounds | OPEN: pump saturation/regeneration, purification yield, buyer specs and energy |
| G4 inventory / operation | Separate module reserves, startup, loss, decay, bounded exports and replacements | OPEN: qualified rates, failure-duration distributions, intermodule transfer controls and reserve validation |
| G5 thermal / electrical | Separate nuclear-energy and prescribed electrical ledgers; imports/exports explicit | OPEN: bottom-up A power balance, deposited heat, load dynamics and electrical autonomy |

The next evidence-bearing improvements are the pump regeneration/buyer-spec interfaces, independently calculated plasma and transport parameters, and installed building/site/OPEX/replacement costs. A successful arithmetic or software test does not close these gates.
