# Beyond Q v1.2 — Source-resolved Neutronics and Dynamic Fuel-Cycle Research

**Atlas Lattice / STARS 2.0 / Beyond Q. October 30, 2026.** New versioned
research package; depends on draft PR #41 at
`dbb01d6d96a429cd3aeae5d6edaf5c006afb3f02`. v1.0 through v1.1.2 are preserved.

## Result and scope

We executed 44 OpenMC neutron-transport calculations using source-locked
FENDL-3.2c data and coupled their source-resolved salt-tritium yields to the
existing conservative inventory model. This replaces arbitrary response
coefficients **only within the specified spherical testbed scenarios**.
It does not establish ARC TBR, reactor operability, measured extraction,
qualified fuel supply or a self-sufficient campus. All physical gates G1–G5
remain open; computational progress is recorded separately.

B remains **1.13 GW D-T fusion power**. A remains **hypothetical 20 MW primary
D-D fusion**, with secondary D-T derived from conditional triton hazards.
Neither is silently replaced by the historical 525 MW ARC design. Their actual
geometries are not asserted to be identical; shared testbed responses are an
explicit comparison assumption. Both require shielding and heat removal.
A0 retains shielding and cooling-channel space, but has no designed functional
coolant in that space: thermal feasibility is unresolved.

| Evidence label | Meaning in this release |
|---|---|
| SOURCE-TRACED | Official OpenMC/data releases, hashes, inherited literature and identified news sources |
| VERIFIED-DERIVED | Source normalization, replay, analytic identities and recorded software checks, conditional on explicit inputs |
| POTENTIAL-DERIVED | Actual transport in assumed geometry and coupled scenario outputs; no reactor-performance qualification |
| UNRESOLVED | Physical plasma feasibility, ARC-specific transport, extraction calibration, qualified startup/reserves, deposited heat, damage and economics |

## Source normalization and candidate plasma model

One FPY is exactly the chosen 365.25 days = 31,557,600 s. Integrated cases use
365 **calendar days**, not one FPY. With equal DD branches and mean Q_DD=3.65
MeV, R_DD=P_DD/(Q_DD·1.602176634e-13 J/MeV). Triton and neutron births are
separate exclusive branches: R_T=0.5R_DD and R_n,DD=0.5R_DD≈1.71e19/s.
One primary DD event must not be assigned two half-branch neutrons. The old
8.55e18/s factor-of-two error remains regression-tested.

Argon's candidate is f=f_fast+(1-f_fast)x/(1+x), x=n_D<σv>τ_p. x is
unitless; f_fast must refer only to pre-thermalization burn. The thermal
formula assumes competing reaction/escape hazards with exponential residence,
not fixed exposure. The alternative 1-exp(-x) has different assumptions.
This is **not** a self-consistent slowing-down/plasma-power calculation.
Reference hazards are 864/day burn and 1449.66442953/day escape,
f_fast=0, giving f≈0.37343 and roughly 18 MW secondary power. Zero hazards
for burn retain the primary DD neutron source. Conditional steady P_DT,max is
48.219 MW with Q_DT=17.6 MeV (48.192 MW at 17.59); Argon's 48.19 value is
compatible with its rounded convention. No achievable confinement is inferred.

Each transport history begins with **one** isotropic point-source neutron,
DD 2.45 MeV or DT 14.1 MeV. B has one source neutron per DT event. A blanket
births are N_n,DD*y_DD + N_T,burn*y_DT atoms. For equal DD branches, the
A weighted yield per primary DD neutron is y_DD+f*y_DT, not a new TBR per
DT reaction. Source fractions are 1/(1+f) and f/(1+f), not energy fractions.
A secondary triton is consumed before its neutron is credited to breeding;
that atom cannot also be delivered or decay-banked.

T consumption is derived from reaction Q, isotope molar mass and Avogadro:
`k = 1e9 * FPY_s / (Q_DT * MeV_J) * (0.00301604928 / 6.02214076e23)`.
At 17.6 MeV, k=56.0490732962 kg/GW-FPY and B burns 63.3354528247 kg/FPY.
The legacy 55.8 convention gives 63.054, while historical displayed arithmetic
uses 63.1. All are preserved; no mixed convention enters a conservation ledger.

## Geometry, materials and evaluated-data limitations

A centered spherical cavity has radius 100 cm. Radial layers are W armour
0.3 cm; inner structural surrogate 1 cm; FLiBe coolant 2 cm; Be multiplier
1 cm; outer structure 3 cm; FLiBe blanket 60/90/120 cm; steel-like tank 3 cm;
B4C shield 25 cm; void flux probe 5 cm; vacuum outer boundary. A penetration
control explicitly removes a polar cone of solid-angle fraction 0.10 through
the layers. It is not a scalar coverage correction and is not an ARC port map.
No divertor, coil, spatial plasma, realistic supports or toroidal asymmetry is
source-qualified. A point source is not a spatially extended tokamak plasma.

FLiBe uses Li2BeF4 atom stoichiometry and assumed density 1.94 g/cm³, Li6 atom
fractions .075/.20/.30/.90. Structural weight-fraction surrogates are:
Inconel-like Ni .53/Cr .19/Fe .18/Nb .05/Mo .03/Ti .01/Al .01 at 8.19 g/cm³;
Eurofer-like Fe .895/Cr .09/W .01/V .005 at 7.8; V4Cr4Ti V .92/Cr .04/Ti .04
at 6.1. Tank Fe .66/Cr .17/Ni .12/Mo .03/Mn .02 at 8.0. These are explicit
major-element approximations, not certified alloy specifications. Minor
elements and material state can materially affect results.

The 46 official IAEA ACE files are at **293.6 K**, converted with OpenMC's
Python API. There is no hot-salt broadening/interpolation, bound thermal
scattering law or depletion calculation. Combining this library temperature
with assumed liquid density is an unqualified physical-state approximation,
not a modeled operating FLiBe state. Evaluated-file/source and converted-file
hashes, reaction MTs, data index and pinned processed-repository commit are
recorded in outputs/nuclear_data_manifest.json. OpenMC 0.15.3 and the explicit
Linux dependency lock are saved. No proprietary ARC model or fabricated
nuclear data is used. Public official files were accessible; the former
software/data access blocker is resolved for this bounded calculation.

## Calculations, tallies and numerical checks

The 44 runs comprise 24 DD/DT×four-enrichment×three-thickness calculations,
four alternative-alloy cases, 14 adverse controls and two seed/history checks.
Ordinary runs use 30 batches×2000 particles, two threads and explicit seeds.
The larger-history case uses 240,000 histories; ordinary cases use 60,000.
All input XMLs, config, raw tally sums/squares, output logs and result/provenance
hashes are retained. Raw HDF5 statepoints are archived; evaluated libraries are
retrieved separately with locked source hashes.

H3-production is an **atom-production score**, persisted by OpenMC as
`(n,Xt)`, not simply an unweighted count of one arbitrarily chosen reaction.
Salt total, Li6-only, Li7-only and all-material production are distinct.
The salt score includes possible Be/F production: Li6+Li7 need not equal total.
Do not add Li components to total again. At natural-Li DT reference, Li6
contributes 0.933452 and Li7 0.103158 per neutron; remaining salt production is
about 0.007516. DD Li7 contribution is zero at this source energy, while the
primary DD source still breeds via other pathways.

Particle accounting tests `1 + nu-scatter - scatter - absorption - leakage`.
All 44 cases close to numerical precision. This global identity is a useful
implementation check but is not independent experimental evidence. Collision
and tracklength salt-yield estimators agree within the declared conservative
comparison bound; they share histories and are not independent experiments.
Aggregated standard-error bounds sum marginal cell SEs, avoiding an unjustified
independence assumption. Three-SE comparisons use sums of those bounds.

A separate **synthetic one-group method benchmark** (Σa=Σt=1/cm, unit-radius
sphere, no scatter) gives leakage 0.368310±0.000914 SE versus exp(-1)=0.367879,
with 200,000 histories. Vacuum controls give leakage=1, no reaction production,
no kerma and exact probe path length. These are analytic transport-method
checks, not fusion-blanket validation. No experimental fusion blanket benchmark
has been independently reproduced here. Same-seed DT replay changes reported
means by at most 2.85e-14 in their recorded units. Binary timestamps may differ.
Zero observed leakage/zero SE is a nondetection, not proof of zero exposure.

## Selected actual transport results — POTENTIAL-DERIVED

Yields below are **salt T atoms per source neutron**, not qualified recovered
tritium. Errors are conservative one-SE aggregation bounds, not physical
uncertainty intervals.

| Case | Mean yield | SE bound |
|---|---:|---:|
| DD_Li0.075_cm90 | 0.787759 | 0.004437 |
| DT_Li0.075_cm90 | 1.044126 | 0.005209 |
| DT_port10 | 0.840062 | 0.005106 |
| DT_more_histories | 1.038176 | 0.003114 |
| DT_vanadium_4cr4ti | 1.209801 | 0.005777 |

The 10% explicit port reduces DT yield to ~0.840, markedly different from
multiplying the reference by 0.9; leakage rises to ~0.229/source. This is a
geometrical-control result, not a prediction of actual port penalties.
The vanadium comparison changes the assumed structural composition only;
it is not evidence of a certified feasible wall or a materials lifetime gain.

Fixed-90-cm comparisons and independent thickness-grid searches are saved
separately. For B the highest point estimate in this grid occurs at intermediate
Li6 (.30); for the A mixed source it occurs at .90. All enrichment-specific
point maxima select 120 cm, but some thickness differences are smaller than
MC error. No unique optimum, universal enrichment ranking or engineering
optimum is claimed; selection bias and cost/geometry constraints remain open.
A2_grid_candidate is a label for the .90/120-cm A candidate, not a validated
optimized reactor. No constant Li6 atom-count requirement is imposed. The
427-tonne example remains solely 118.6×.90/.25=426.96 conditional arithmetic.

A0's mobile salt breeding is zero. Its all-material T production is **not**
zero (~0.00947 DD, ~0.04671 DT per source neutron) because other nuclides can
produce T. The integrated ledger separately estimates nonfuel-boundary births;
it does not deliver those atoms. Their retention, permeation, decay and release
require a future whole-facility wall/material inventory model. Mobile-fuel
closure must not be described as whole-facility radiological accountancy.

## Dynamic extraction, processing, inventory and transfers

The inherited eight nonnegative stocks are A plasma, A/B blanket, A plasma
processing, A blanket processing, B processing and A/B storage. Transfers
always have a donor and recipient; unburned B feed returns to processing,
not to nuclear births. B actual fusion is fuel-limited: unmet demand does not
create neutrons, tritium or energy. Sources stop with reactor outages, while
processing/extraction continue unless separately failed (scenario assumption).

For a stock I [kg] with source s [kg/day], extraction k_ext [1/day], permeation
k_perm and decay λ=ln2/(12.32×365.25)/day:
`dI/dt=s-(k_ext+k_perm+λ)I`.
Exact constant-hazard substeps use expm1-stable integrated exits. Different
compartments are operator-split, so conservation can be exact while coupled
trajectories still have timestep error. Reference step=0.125 day. A1 final
inventory at steps .125/.0625/.03125 is 16.406569/16.399795/16.396593 kg:
coarse-to-finest spread **~9.98 g**. This is a numerical sensitivity, not
physical accuracy. Startup bracket endpoints are algorithmic resolution only.

Argon's well-mixed `k_ext=epsilon/tau_loop` is dimensionally consistent but
differs from fixed discrete-pass survival `k=-ln(1-epsilon)/tau_loop`.
Reference epsilon=.85, loop=10 min gives 122.4/day. The one-ISS steady recovery
`[k_ext/(k_ext+k_perm+λ)](1-f_ISS_loss)` does not include later storage decay or
repeated B processing cycles. Low per-pass efficiency causes holdup, not
instant disappearance. No extraction rate is established by molecular binding
energy or assumed to be measured plant recovery.

A plasma and blanket process independently at 4/day and 1/day with assumed
permanent recoveries .95 and .90. B processes at 4/day with .9999 recovery,
5% single-pass burn and 95% recirculation. Permeation=.0001/day, initial B=10
kg, A=0, A reserve=.25 kg, A→B transfer=2/day. These remain uncalibrated
parameters. Cumulative B processing includes recycled atoms; it is not a fresh
source and must never be added to gross breeding as new supply.

The mobile mass identity is initial + DD births + A/B blanket births minus
A/B consumption, decay, permeation and irreversible processing losses = final
mobile inventory. Counter totals and their subcategories are not added twice.
All 48 cases close below 1e-8 kg. Salt recirculation is implicit well-mixing;
no resolved pipe residence-time distribution or two-phase chemistry is solved.

## Adverse controls, conditional balances and secondary-burn tradeoff

Three A cases × secondary on/off × eight conditions give 48 integrated runs:
reference, poor recovery, independent outages, common outages, zero-reserve
startup, seven-day B processor outage, seven-day B extractor outage and B port.
Daily Bernoulli schedules have explicit common shocks; no measured MTBF or
repair-duration distribution is inferred. Correlated and independent uptime
are not collapsed to one campus capacity factor. Reduced multiplier, doubled
structure and isotope-zero controls are retained in transport outputs.

With secondary ON and full scheduled uptime, 365-day mobile stock growth is
A0 **3.622 kg**, A1 **6.407 kg**, A2-grid **6.755 kg**, conditional on every
listed assumption. These are not annual qualified usable surplus. The separate
calendar_balance_percent.csv reports kg and percentage of actual B burn.
The B-port condition changes A1 growth to **-6.152 kg**. Poor recovery can
produce a deficit. Cold starts cause unmet B burn in all A cases. A seven-day
processor outage causes unmet demand despite positive final inventory:
positive end-of-year stock does not establish uninterrupted operation.

Finite-horizon bisection gives reference initial-B brackets near 1.092 kg,
but A1's seven-day processor-outage bracket is near **25.105 kg**. These
quantities are affected by 5% feed burn, recirculation holdup, timestep, delays
and chosen horizon. They are not regulatory or physically qualified startup
inventories. Current 365-day brackets do not demonstrate 20-year autonomy.

Matched ON−OFF comparison at fixed primary DD source gives recovered A plasma
changes about -0.957264 kg; extra recovered blanket supply is A0 0,
A1 +0.944831 kg, A2-grid +0.974461 kg. Reference campus-stock differences are
**-0.931762, -0.009825, +0.019087 kg**, respectively. Small near-zero differences
must be assessed against MC, timestep and unquantified physical uncertainties;
no sign of net benefit is physically established. Static idealized isotope
threshold is eta_AB*y_DT > eta_AP (equal other conditions), with .95/.90
threshold y_DT>1.05556; it is not sufficient for dynamic operation or economics.
Damage, activation, maintenance, RF/input power and incremental NPV remain
unresolved; energy and tritium opportunity costs cannot cancel neutron damage
in incompatible units. This implements the new parent addendum's matched
comparison without claiming its broader lifetime/economic questions solved.

Uncertainty draws (32 per A reference) propagate tally-statistical bounds
with nonnegative Gaussian approximation and shared response reuse correlation.
They are exploratory numerical draws, not calibrated physical confidence or
credible intervals. Nuclear-data covariance, plasma uncertainty, full geometry,
hot-state material uncertainty and qualified recovery bounds remain unresolved.
The spread across scenarios is not a probability distribution of a real plant.

## Neutron and thermal-energy boundaries

For recorded source counts, fusion Q = initial charged-particle energy +
initial neutron kinetic energy. The CSV neutron_thermal_energy_ledger.csv
records those partitions and a **separate neutron kerma** estimate from MT301
`heating`. Do not add full fusion Q to kerma: neutron energy already belongs
to fusion Q. Likewise do not append Li6 reaction Q to a tally that already
accounts for that energy. The inherited blanket-Q screening field is not used
as calibrated deposited heat in this release; the all-Li6 default is not a
transport-derived isotope partition.

Photon transport is disabled; no coupled photon deposition, full reaction-Q
inventory, leakage-energy spectrum or thermal-hydraulic removal calculation
closes actual material energy balance. `heating` is not mislabeled fully
deposited `heating-local`. Nuclear heating per source and fast probe flux are
recorded, but no REBCO lifetime, dpa, cooling feasibility, net electric output
or reactor power gain follows. Probe flux bins are particle-cm/source; divide
by the recorded probe volume and multiply source neutrons/s for cm^-2 s^-1.
The vacuum and toy energy identities do not close G5 for material runs.

## Research gates and next falsification work

| Gate | Completed bounded computation | Remaining physical work | Status |
|---|---|---|---|
| G1 | Source stoichiometry, candidate burn coupling, ON/OFF controls | Self-consistent fast/thermal triton kinetics, confinement and plasma power balance | OPEN |
| G2 | Evaluated-data transport, provenance, source normalization, estimator/replay and analytic QA | Experimental fusion blanket benchmark, qualified hot-state data/materials and exact reactor geometry incl. ports/divertor | OPEN; bounded computational milestone only |
| G3 | Separate recovery routes, extraction/permeation/processing accounting | Measured rates, chemical speciation, wall retention, qualified recovered purity and uncertainty | OPEN |
| G4 | Conservative stocks, independent/common outages, fuel starvation and startup brackets | Validated plant schedules/repair times, qualified reserve policy and multiyear deployment model | OPEN |
| G5 | Nonduplicated fusion source partitions, separate kerma tally | Coupled nuclear energy closure, heat removal, auxiliaries, electricity, activation/damage and economic boundary | OPEN |

Priority is an external transport benchmark and source-qualified geometry,
followed by material-temperature qualification and validated extraction data.
The October 30 news appendix supplies leads, not replacement model inputs.
A 20-year campus model additionally needs element feedstock, Be/Li isotope
supply, replacement components, heat rejection and external dependencies.
The retired 1.3–2.6 kg/FPY A blanket envelope stays historical only. Earlier
3.85→3.65 arithmetic, DD source factor-two and neutron-energy double-counting
corrections remain regression checked. Software success never qualifies an
assumed TBR or processing efficiency as operational self-sufficiency.

## Attribution and reproducibility record

Dave Sheldon / Atlas Lattice originated the research direction and supplied
the review work orders. GPT-6/Tidal Lantern supplied documented reconciliation
and tradeoff analysis; DeepSeek supplied cross-audit findings and source leads;
Gemini Argon supplied candidate burn/extraction equations and research leads.
This implementation records their analytical contributions as supplied, without
institutional coauthorship, experimental validation or endorsement.

See SOURCES.md for primary/official sources and transfer limits; README.md for
commands, archive and environment; AUDIT_HISTORY.jsonl for retained failures;
outputs/check_status.json for regression results. All previous artifacts are
preserved. No failed assumption is removed to force a positive outcome.
