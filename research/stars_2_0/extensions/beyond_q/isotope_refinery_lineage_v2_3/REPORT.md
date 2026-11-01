# Beyond Q v2.3: scientific lineage, recovery boundaries and benchmark readiness

Research checkpoint, 2026-11-01. Parent: v2.2, commit `50c4c322c239874f43a9908b7a4522007b621af8`, draft PR #66. This is an additive appendix, not a calibrated plasma model or new transport calculation.

## Findings and integration decisions

The isotope-refinery objective has a documented scientific lineage. Earlier work supports investigating a dedicated isotope-producing plasma and complementary reactors. It does not establish that Beyond Q's proposed source power, recovery train, electricity balance or commercial output is attainable. The evidence changes the reference framework and defines prospective comparisons; it does not close a physical gate or upgrade scenario efficiencies.

| Reference | Supported finding | Role in Beyond Q | What cannot be transferred |
|---|---|---|---|
| Greenspan–Miley 1982 [GM1982] | Theoretical recovery from deuterium-based plasmas feeding separate D-He3 reactors | Candidate plasma recovery and energy-balance benchmark | Overall saleable-product recovery or ARC operating point |
| Helion 2025/2026 [HELION2025, HELION2026] | Direct DD and decay pathways; fuel accountancy and separation interfaces | Process-boundary checklist | Measured ARC-compatible capture efficiency |
| Helion patent [HELION_PATENT] | DD product extraction, storage/decay and subsequent fuel use | Published technical lineage | Demonstration, turnkey tokamak retrofit or legal clearance |
| Kronos [KRONOS2026] | Proposed breeder/burner architecture with aging tritium | Distinct architecture and inventory comparator | Immediate direct-DD He3 yield |
| ARC particle-exhaust paper [ARC_EXHAUST2026] | Preliminary DT ash-exhaust estimate and planned validation | Closest geometry-family exhaust interface | Qualified He3 product recovery |

The claimed contribution should be a reproducible integration of isotope, energy, recovery, startup, financing and rollout ledgers. No claim of first invention, experimental endorsement or operating commercial DD isotope production follows from this review. The sources examined do not establish a commercial plant operating at the proposed scale; this is not an exhaustive worldwide absence claim.

## 1982 paper: verified abstract, unreproduced benchmark

E. Greenspan and G. H. Miley, *Deuterium-Based Plasmas as a Source for Helium-3*, Nuclear Technology – Fusion 2(1), 43–54, January 1982, DOI [10.13182/FST82-A20733](https://doi.org/10.13182/FST82-A20733). The publisher abstract and ANS volume index agree on title, authors and pagination. The 2017 online posting date is not the original research date.

The abstract reports approximately 70% recoverable He3 for its driven semi-catalyzed deuterium cases, and an approximately 80% bound in its ignited-plasma study. It associates these with roughly 70 and 50 MeV of fusion energy per recovered atom respectively, and emphasizes sensitivity to plasma energy balance. These are **SOURCE-TRACED theoretical findings**, not reproduced results here. [GM1982]

The fractions concern modeled plasmas. They cannot establish pump capture, regeneration, purification or product-assay performance. Nor is the study-specific 80% figure a universal ceiling. Full text was not obtained: direct ANS article/download retrieval failed and the accessible publisher evidence was its abstract. Consequently we have not reconstructed its equations, profiles, confinement assumptions, thermal balance or numerical points. `historical_benchmark.calibration_enabled=false` makes this limitation explicit.

Our source normalization uses **primary DD fusion power** and 3.65 MeV per primary event. The historical paper's quoted energy-per-recovered-atom denominator is not interchangeable with that definition or with wall-plug energy. A numerical overlay requires the full paper's energy and recovery boundaries first. We do not use its 70% result to certify the 75% scenario or fit a new reaction kernel.

## Birth-to-product boundaries

For an explicitly resolved steady-flow scenario, define conditional fractions:

\[
N_{3,\mathrm{product}}=N_{3,\mathrm{born}}\,s_{\mathrm{plasma}}\,e_{\mathrm{exhaust}}\,c_{\mathrm{pump}}\,p_{\mathrm{purification}}.
\]

Each fraction is relative to the preceding stream. Secondary consumption, retention, exhaust losses, pump/regeneration losses and purification rejection must each enter once. Time-dependent retained material remains inventory; it is not automatically a permanent loss. Passing purity/assay specifications remains an additional evidence requirement, not an assumed permission to call modeled material qualified.

`audit.product_ledger` offers mutually exclusive overall and explicit-stage accounting modes. With illustrative plasma survival 0.70, exhaust delivery 0.90, pump recovery 0.90 and purification yield 0.95, the combined fraction is **0.53865**, not 0.70. This is a bookkeeping demonstration, not a sourced flowsheet. The stages close separately to the birth amount and cannot create product from zero birth.

The existing v2.2 37.5%, 75% and 90% inputs are **overall birth-to-product-candidate assumptions**, applied once; they already lump unresolved losses and contain no separate He3 secondary-burn model. Adding another 70% plasma factor to the same overall input would change the scenario boundary. No such change is made. We retain 37.5% as the conservative-potential planning baseline, 75% as upside and 90% as stretch. None is an evidence-derived lower bound; actual recovery could be below 37.5%.

## Reconciling 939,000 liters with the simulator

The deterministic gross-birth relation is

\[
V_3=\frac{P_{DD}\,10^6}{\bar E_{DD}\,J_{\mathrm{MeV}}}
\frac{b_3\,(365.25)(86400)\,a_{\mathrm{eff}}}{N_A}\,V_m.
\]

Units are MW, MeV/event, J/MeV, atoms/event, seconds/year, atoms/mol and L/mol. Inputs are 1100 MW primary DD, 3.65 MeV/event, equal-branch convention \(b_3=0.5\), and \(V_m=22.414\) L/mol at 273.15 K and 101325 Pa. He3 is monatomic gas; tritium gaseous-liter conventions require a separate T-atom versus T2-molecule definition. Equal branches are an assumption for normalization, not a universal temperature-independent measured ratio.

| Effective exposure convention | Gross He3 STP L/year | 37.5% product candidate | 75% | 90% |
|---|---:|---:|---:|---:|
| Pasted estimate: 85% effective | 938,968 | 352,113 | 704,226 | 845,071 |
| Parent expected exposure: 85% macro × 93.75% source duty | 880,282 | 330,106 | 660,212 | 792,254 |

These are annual steady-throughput arithmetic, **VERIFIED-DERIVED given the stated assumptions**, and potential production scenarios are **POTENTIAL-DERIVED**. The second row is an expected-exposure comparator before replacement outages, stochastic realization and pipeline holdup; it is not a rerun of v2.2 annual outputs. `normalization.csv` stores the unrounded results. The first row confirms the pasted numbers. The difference is exposure accounting, not an atom-count contradiction. Actual v2.2 year-one product is also affected by initial holdup and realized schedules.

No separate secondary D-He3 burn is applied in these rows. If an explicit burn model is introduced later, either resolve all conditional stages or redefine the overall fraction with a documented boundary. Preserve the current inputs and earlier calculations as independent historical cases.

## Process interfaces from Helion and ARC

Helion's March 2025 company article describes direct DD and tritium-decay He3 pathways, fuel separation and getter storage. Its June 2026 account describes exhaust analysis, distinct hydrogen/helium/impurity streams, hydrogen and helium isotope separation, current batch operation and proposed continuous fuel recycling. These are useful accountancy/process interfaces, not measured Beyond Q recoveries. [HELION2025, HELION2026]

Integration should specify species-resolved feed, pressure, temperature, throughput, residence inventory, cross-contamination, regeneration loss and product assay at each interface. A pulsed FRC exhaust arrangement cannot be copied directly to an ARC tokamak. Hydrogen-isotope separation does not replace He3/He4 separation. Helium-rich product, candidate storage and buyer-qualified product remain separate states.

Patent US11469003B2, by Slough, Kirtley and Pihl, assigned to Helion, lists 2014-02-07 priority and 2022-10-11 publication. It discloses DD He3/T production, pulsed removal of tritium before secondary DT burn, storage/decay and reuse. It is a material precedent for technical lineage; we perform no patent claim/FTO determination. Its approximate 11-year decay wording does not replace the parent's explicit 12.32-year half-life. [HELION_PATENT]

The ARC paper, JPP 92(3), E66, DOI [10.1017/S002237782610155X](https://doi.org/10.1017/S002237782610155X), treats helium exhaust as an uncertain preliminary design calculation requiring future transport studies and SPARC experiments. Section 5.2 uses approximately 20 Pa, 30 m3/s and 900 K to estimate enrichment for a core helium concentration below 2%. These do not establish a He3 product yield. Its printed equation 5.4 gives 3.2e20/s for 1100 MW / 17.6 MeV; direct conversion gives about 3.90e20/s. This existing source-arithmetic discrepancy remains open and is not silently used as pump calibration. [ARC_EXHAUST2026]

## Kronos: a separate decay-inventory comparator

The company's fuel-cycle page describes HYPERION DT breeding feeding a separate D-He3 burner, with a TBR scan treated as a design lever. Its approximately 4 kg/year T and 1.97 kg/year He3 figures are projections; the page attributes He3 supply to an aging tritium inventory without fully reconciling the time origin and stock for those flows. This is a conceptual comparator, not measured production or a substitute for direct DD births. [KRONOS2026]

For an independent illustration, assume **net** 4 kg/year addition to an initially empty T aging store, no withdrawal or other loss, and 12.32-year half-life. With \(\lambda=\ln2/12.32\), mass ratio \(r=M_3/M_T\),

\[
I_T(t)=\frac{4}{\lambda}(1-e^{-\lambda t}),\qquad
\dot m_3=r\lambda I_T.
\]

A 1.97 kg/year instantaneous daughter flow requires about **35.0 kg** aging T inventory and is reached around **12.06 years** under those assumptions. The first year's integrated daughter birth is only about **0.110 kg**. See `decay_comparator.json` for exact arithmetic. This does not reconstruct Kronos's plant or show its projection wrong; it identifies missing stock/time boundaries. Decayed T cannot also be delivered to B. Daughter production does not establish daughter recovery. No decay-derived He3 revenue is added to v2.2.

## Next calibration work and gate status

1. Obtain the full Greenspan–Miley article and extract equations, operating points, units, fusion-energy boundary and loss assumptions. Reproduce its own reported cases before comparing to Beyond Q. The present abstract is insufficient.
2. Resolve He3 secondary consumption and residence-time distributions against a plasma solution; connect its exhaust source to a mass-conserving process train. Existing short WarpX tests do not close this requirement.
3. Specify measured regeneration/capture and purification interfaces, including T contamination and buyer assay requirements. Helion's process descriptions and ARC exhaust modeling inform the questions, not numerical efficiencies.
4. Continue transport, heat, electrical-load and cost reconciliation independently. Run new cascade/financial sensitivities only after documenting any changed source/recovery boundary.

G1–G5 remain **OPEN**. No new WarpX, OpenMC or experimental execution occurred in this appendix. Software checks establish normalization and ledger consistency only. The new precedents neither prove positive isotope economics nor demonstrate operational self-sufficiency, continuous islanded power or indefinite operation.

## Provenance and credit

Dave / Atlas Lattice originated the isotope-first dual-reactor research direction and requested this integration. GPT Work performed source checks and the present reproducible audit. GPT-6/Tidal Lantern, DeepSeek and Gemini Argon supplied the analytical contributions recorded in earlier release histories; the supplied cross-thread synthesis prompted this lineage review. Greenspan, Miley, patent inventors, Helion, Kronos and ARC authors retain credit for their own published work. Citation implies no endorsement. Full primary URLs, locators, access scope and transfer limits are in `sources.json`; historical releases remain unchanged.
