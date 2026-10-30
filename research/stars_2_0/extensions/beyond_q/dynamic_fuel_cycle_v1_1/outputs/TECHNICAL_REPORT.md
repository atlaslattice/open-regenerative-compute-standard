# Beyond Q v1.1 — Dynamic Fuel-Cycle Computational Results

Atlas Lattice / STARS 2.0 / Stellar Forge extension. Candidate research release.
Reference baseline commit: `876bb375d278e9ccb934638fbfbe64852fbcbfbd`.

**No physical self-sufficiency or qualified usable surplus is established.**
Gemini Argon's exact candidate equations were supplied during implementation.
They are implemented and audited; their physical inputs remain unvalidated.

## Reproduction and configuration

All 28 v1 CSV scenarios reproduce within 0.000051 kg rounding tolerance.
Original script also runs at eventual recovery 1.0 and 0.85. Exact legacy
display benchmarks remain +4.912 and -4.7423 kg/FPY; A=3.65 kg is explicitly
an unqualified annual assumption. v1 remains unchanged.

B is locked at 1130 MW D-T fusion. A is locked at hypothetical 20 MW primary
D-D. Rounded reaction energies and the stated atomic mass give A direct
birth 2.702640 kg/FPY and B burn 63.335453 kg/FPY. These use a common
stoichiometric constant; the legacy 55.8 kg/GW FPY and 63.1 display basis
are retained only in the benchmark module. These differences expose rounding/
conversion drift in inherited numbers, not a new physical effect. Argon quoted
2.712 kg/FPY primary birth and 1.013 kg/FPY secondary consumption; this common
conversion yields 2.702640 and 1.008883 kg/FPY respectively. Classification: VERIFIED-DERIVED
conditional stoichiometry; reactor operating points remain assumed/design targets.

## Illustrative dynamic cases (730 calendar days)

| Case | Assumed A births/source neutron | Final inventory kg-T | Change kg-T | Unserved B burn kg-T |
|---|---:|---:|---:|---:|
| A0 | 0.000 | 13.460001 | 3.460001 | 0.000000 |
| A1 | 0.520 | 16.522125 | 6.522125 | 0.000000 |
| A2 | 0.700 | 17.582091 | 7.582091 | 0.000000 |

Every dynamic case is POTENTIAL-DERIVED. A0 means nonbreeding functional
shield/coolant, not no shielding. A1 uses an illustrative yield of 0.52
T atoms per primary-plus-secondary source neutron. A2=0.70 is an explicitly
assumed exploratory surrogate, **not an optimized blanket calculation**.
v1 defines no numerical A2 blanket; natural-lithium chemistry does not determine
a TBR by itself. Initial B stock is 10.0 kg externally acquired T,
not a prediction of required startup inventory. No subsequent imports are modeled.

Common outage probability is 0.05; independent on-probabilities
are 0.9/0.9 before the common outage.
Planned A outage days 180–194 and B outage days 365–394 are zero-based.
Extraction/processing continue during reactor outages; no processor-failure
model is inferred. Minimum daily B storage is reported, but substep minima
and licensing reserves are not qualified. Unserved burn measures inability to
meet requested power: the simulator reduces B burn and blanket births together,
so fuel starvation cannot manufacture fuel at rated power.

## Uncertainty and numerical limits

64 reproducible parameter/schedule draws use the explicit uniform ranges in
`inputs/uncertainty_v1_1.json`. They are assumption-conditioned scenario bounds,
not measured uncertainty, confidence bounds, or a calibrated Bayesian posterior.
The assumed ranges are independent; input covariance and model discrepancy
are missing. Common shocks correlate outages. The 5/50/95% final inventory
quantiles are 10.1523 / 16.2280 /
23.8198 kg-T. Compare unserved burn alongside inventory:
a high remaining inventory alone does not prove successful operation.

All compartments integrate constant source/linear hazards analytically and
remain nonnegative. Coupled updates use first-order operator splitting; this
has timestep bias. Default step 0.125 day differs from 0.0625-day
final stock by 0.0110043 kg in this run.
Refinement is a numerical check, not physical validation. Benchmark and tests
do not certify reactor feasibility.

## Independently checkable ledgers

Daily CSV columns record each compartment, source, sink, feed, recirculation,
transfer and cumulative residual. Identity in kg-T:
`initial + DD births + A blanket births + B blanket births = remaining +
A burn + B burn + decay + permeation + processing losses`.
Transfers cancel globally. One consumed T atom cannot reach a storage account.
Decay is tracked as kg-T-equivalent transformed into He-3, not unaccounted T.
This is a tritium isotope mass ledger, not total elemental/isotopic depletion.
Li/Be/F/D and structural depletion are not solved; blanket reactants are an
assumed inexhaustible reservoir within the short screening horizon.

The JSON summaries partition fusion energy into charged-particle and neutron
kinetic energy. Their sum equals fusion Q; neutron heat is never added again.
Blanket Q uses an assumed Li-6/Li-7 birth partition and is separately named.
This is source nuclear release, not deposited thermal heat or net electricity.
Neutron source births are countable, but capture/leakage/multiplication fate
closure is UNRESOLVED without transport. No assumed TBR can close that ledger.

## Gate status

| Gate | Computational progress | Evidence still required / status |
|---|---|---|
| G1 | Conservative DD birth and candidate secondary-burn hazards; 18 MW no longer independently forced | Density / T distribution / reactivity / confinement and power balance; OPEN |
| G2 | OpenMC preflight and surrogate input generator | Installed engine/data plus V3A-compatible documented geometry/materials/ports; OPEN |
| G3 | Extraction, holdup, permeation, recirculation and decay compartments | Measured FLiBe transport/speciation/recovery under relevant loads; OPEN |
| G4 | Time-resolved inventory, independent schedules, common outages, seed and conservation tests | Calibrated schedules, subcomponent failures, startup/reserve qualification; OPEN for physical closure |
| G5 | Nuclear source energy partition without duplicate neutron energy | Full heat deposition, wall-plug/RF/cooling/magnets/materials/economics; OPEN |

v1 G6 is preserved as cross-cutting independent replication/provenance.
No gate is declared physically validated. See `TECHNICAL_METHODS.md` for equations,
`SOURCES.md` for exact source relevance and access limits, and `AUDIT_HISTORY.jsonl`
for append-only corrections and Argon review.

## Credit and direction

Research conception/direction: Dave Sheldon / Atlas Lattice. GPT-6: documented
v1 audit/synthesis and v1.1 computational implementation through ChatGPT Work.
DeepSeek: v1 conditional blanket/recovery scenarios and critique. Gemini Argon:
v1 literature and material/enrichment challenges; candidate burn and extraction equations supplied by the user. Contributions are analytical discourse/software, not experiments,
institutional endorsements, or independent peer review.
