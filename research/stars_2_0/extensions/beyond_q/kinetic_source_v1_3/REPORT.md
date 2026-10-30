# Beyond Q v1.3 — Actual WarpX D-D/D-T Benchmark and Inventory-Kernel Comparison

**Atlas Lattice / STARS2.0 / Beyond Q · October 30, 2026.** New versioned
artifact dependent on v1.2 draft PR #46. No earlier release or physics input is
overwritten. B remains1.13 GW DT; A remains hypothetical20 MW primary DD.

## What was run and what it establishes

WarpX 26.10 executed two upstream fusion tests and nine bounded collision-network
cases. Both upstream tests pass their supplied numerical analyses. The coupled
network begins with **zero tritium**, produces T through D+D→T+p, retains
D+D→He3+n, and consumes some newborn T through D+T→He4+n. Separate neutron
species preserve branch identity. Physical weights, not macroparticle counts,
feed reaction, energy, source and inventory ledgers.

This establishes a reproducible **numerical comparison target** for our source
bookkeeping and exact compartment kernel. It is not an experimental benchmark,
full tokamak simulation, calibrated slowing-down model or end-to-end simulation
of both reactor plants. B's DT operator is exercised by the upstream test;
blanket breeding, extraction, storage and campus recirculation remain in the
existing OpenMC/fuel-cycle suite. They are not modeled by WarpX here.

| Label | Application |
|---|---|
| SOURCE-TRACED | Pinned upstream fixtures, code documentation, published algorithms and package identity |
| VERIFIED-DERIVED | Numerical stoichiometry, source normalization, recorded test results and replay conditional on stated inputs |
| POTENTIAL-DERIVED | Collision-box reaction yields, spectra, inferred hazards and comparisons applied to proposed A/B research |
| UNRESOLVED | Reactor confinement/operability, source-qualified reactor spectra, physical uncertainty, damage, extraction and qualified self-sufficiency |

## Executable, source and reproducibility boundaries

Installed conda-forge WarpX **26.10**, build `np2py314h0f05cbd_0`, with a saved
explicit dependency lock, package URL/checksums and executable SHA256.
The executable prints **WarpX(Unknown)**, AMReX 26.10 and PICSAR 26.10. We do not
invent an embedded WarpX git hash. The reference upstream release 26.10 tag
resolves to `ec1660d961696c865c87c26728b7e248b5454082`; vendored numerical test
fixtures and documentation were obtained at that commit. Package identity and
reference-source identity are recorded separately; no bit-for-bit source-build
attestation is claimed. No solver modification or public WarpX fork was needed.

The unmodified upstream DD test has8×8×16 cells,10000 macroparticles/cell per
reactant, one step. The DT test uses its supplied multiple populations and two
steps; its supplied analysis checks the first-step output. Upstream code checks
weighted particle accounting, charge, energy/momentum and reaction yields, with
its documented stochastic/empirical tolerances. Their large event multipliers
are sampling devices with reduced daughter weights and corresponding reactant
weight removal. They do not enhance physical cross sections or energy yield.

## Bounded DD-born-T collision network

An8×8×8 periodic cube spans[-1mm,+1mm] in each dimension, volume8e-9m³.
D density is1e26m^-3 and its initial Gaussian momentum corresponds approximately
to20 keV temperature. Initially only D exists:512000 macroparticles at1000/cell.
All particles are frozen in position and do not deposit charge/current. There
is no self-consistent field response, Coulomb collision operator, slowing down,
confinement, escape, fueling, heating, material interaction or blanket. Thus
this is **kinetic fusion-collision sampling in a prescribed frozen distribution**,
not a self-consistent plasma solution. It is intentionally different from our
reference scenario's lower density and long residence-time assumptions.

Reference step1e-13s,20steps, total **2 ps**. The three enabled reaction operators
are DDT, DDN and DT, in that input order. Same-species DD pairing includes its
statistical symmetry correction; physical expectation is0.5*n_D²*<σv>*V*dt,
not n_D²*<σv>*V*dt. T birth precedes the DT update within a step, so comparing
against continuous sources requires discretization care. Proton and He3
secondary reactions are intentionally disabled. No claim of network completeness.

Nine cases are baseline, seeds219/319, secondary-off, no-T-birth, product-creation
off, half timestep with40steps, double particles/cell, and a tenfold smaller
sampling multiplier. The case named `no_reactions` disables product creation;
it is a **diagnostic negative control**, not a claim that the cross-section
kernel has been removed. Its physical particle/source counts remain zero.

## Baseline numerical results

| Quantity over2 ps | Physical weight / result |
|---|---:|
| DD tritium births (proton coproduct proxy) |194729212.115633 atoms |
| DD neutron births (He3 coproduct proxy) |210149422.927211 atoms |
| Secondary DT consumption / neutron births |6.672601048114 atoms |
| Remaining T |194729205.443032 atoms |
| Secondary T burn fraction |3.4266050664e-8 |
| T branch fraction of primary DD reactions |0.4809569962 |

Fractional physical weights are valid Monte Carlo estimates, not integer atoms
individually resolved by the simulation. The baseline produces about0.5% fewer
DDT births and0.2% fewer DDN births than an independent Maxwellian quadrature
using the same Bosch-Hale cross-section parameterization. DD rate comparisons
pass the stated five-proxy-SE screen. Proxy SE is sqrt(2*sum daughter weights²),
accounting for paired daughter macroparticles; it is not a calibrated complete
uncertainty model and excludes finite initial-distribution sampling and pairing
correlations. Reference seeds and particle/multiplier variations are provided.

The~0.481 branch fraction is a result of this20 keV model and sampling, not a new
universal DD branching constant. The v1.2 equal-branch convention remains
unchanged. The tiny2 ps secondary burn fraction **neither confirms nor falsifies**
a37% long-residence reactor scenario. It cannot be extrapolated to a reactor
without physical confinement, slowing-down, loss and density/temperature histories.

Observed neutron spectra are weighted distributions, not forced monoenergetic
lines: DD neutrons cluster around2.45MeV, while fusion of fast DD-born tritons
creates a broad secondary-DT spectrum. Spectra are stored separately by source,
normalized both conditionally and jointly. Full baseline daughter momenta allow
future angular analysis. Isotropic product scattering is the prescribed default;
this release does not qualify differential cross sections or source anisotropy
for a reactor. Cross-section upper-fit domains, nonthermal tails and operating
conditions need their own qualification; executing upstream fits is not such a check.

## Independently checkable numerical ledgers

Let P be weighted proton coproduct count, H3 weighted He3 count and H4 weighted
He4 count, with no initial products. Then DD T birth=P, DD neutron birth=H3,
DT T consumption=H4, and:

`T_remaining + H4 = P`

`nDD = H3; nDT = H4`

`D_initial - D_remaining = 2*(P+H3)+H4`.

Charge and nucleon counts are also recorded. T closure stays within numerical
roundoff and all neutron coproduct identities close. Disabling T birth yields
no DT burn; disabling secondary DT retains primary DD neutrons and unburned T.
No consumed T is exported by the source interface or mass replay.

A significant numerical reporting issue is retained: ordinary reduced-diagnostic
D summation over the~8e17-atom background shows apparent residuals of order
1e6 atoms. Compensated `math.fsum` of the stored particle weights gives baseline
final donor residual **35.24 atoms**, below one128-atom ULP of the background
pool. All cases are within the declared1024-atom donor screen. The large-pool
D diagnostic cannot individually resolve the few-atom secondary consumption;
the T and product ledgers are the more sensitive checks. We do not claim
atom-exact donor conservation from a rounded background total.

Collision energy check is kinetic-energy change versus
`P*4.032653948 + H3*3.26891111 + H4*17.58929696` MeV, converted once to joules.
Baseline maximum residual is~1.59e-11J (~6.75e-8 of final released Q); other
cases meet the1e-5-relative-Q screen. Momentum conservation is recorded. These
are collision-network energy checks, not deposited blanket heat, recovered
thermal power or net electricity. Initial thermal kinetic energy is not counted
again as fusion reaction Q. The frozen/disconnected field boundary is explicit.

## Comparison with our existing inventory code

`compare_inventory.py` imports the exact v1.2 `fuelcycle.inventory.advance`
operator. It uses the actual time-dependent WarpX DD tritium birth history,
not a fitted annual production coefficient. A separate final-spectrum sampling
estimator calculates a nonrelativistic D-T hazard: draw weighted T momenta and
20 keV Maxwellian D velocities, average σ(E_relative)*v_relative, multiply by n_D.
That hazard is fixed for the comparison interval. Its approximation ignores
birth-time dependence, relativistic pairing details and distribution evolution.
It uses the same cross-section physics as WarpX and is not an independent
nuclear-data validation.

The compartment operator advances kg-T with seconds consistently converted to
days and hazard s^-1 converted to day^-1. It integrates continuous within-step
birth and burn exactly. WarpX sampling follows discrete collision updates.
Across six cases the kernel predicts total secondary burn **2.49–7.78% below**
WarpX; baseline difference is **-2.54%**. The discrepancy is reported, not
removed by changing a recovery coefficient or forcing exact agreement. Half
timestep does not monotonically remove disagreement: stochastic sampling,
source history and final-spectrum approximation also matter. The post-run10%
regression screen is an exploratory software criterion, not a preregistered
physics acceptance threshold or physical uncertainty interval.

A second replay simply subtracts observed consumption from observed birth in
material kg, preserving the atom-to-mass convention. This is a bookkeeping
identity, not an independent rate prediction. These comparisons show that our
kernel can accept externally generated kinetic sources; they do not validate
the entire campus fuel cycle.

## Source interface and reference powers

`source_interface.json` is **ACTUAL_WARPX_SOURCE_SAMPLE_NOT_TRANSPORT**. It
retains the2 ps time window and flags stationary reactor qualification false.
Its formal normalization to20 MW primary-DD reaction Q keeps branch-specific
sources and consumed T separate. The very small secondary power derived under
that normalization is not a new predicted operating point. No such source is
silently installed in v1.2 or presented as an ARC blanket calculation.

B's1130 MW DT reaction-rate conversion is reported at both our17.6 MeV convention
and WarpX's17.58929696 MeV Q: rates differ by~0.06085%. This is a numerical
convention reconciliation, not a reactor improvement. The legacy55.8kg/GW-FPY
and derived56.049073kg/GW-FPY remain documented in earlier releases. Neither
reactor is replaced by525 MW or500 MW configurations.

## Gate status, limits and next work

All physical gates **G1–G5 remain OPEN**. G1 gains executable source/collision
verification and an external kinetic benchmark for our inventory kernel.
There is no new reactor confinement result. G2's actual simplified OpenMC work
is preserved; these neutron samples are not new blanket yields. G3/G4 recovery,
purity, wall inventory, schedules, startup reserves and qualified export stay
unresolved physically. G5 lacks a full plasma-input, material-deposition,
heat-removal and electrical boundary. No qualified usable surplus or operational
self-sufficiency is declared.

Next priority: a separately benchmarked fast-triton slowing-down calculation,
then prescribed escape/time-distribution comparisons with Argon's competing-
hazard candidate. Only source-qualified geometry and plasma conditions justify
passing new distributions into a new OpenMC campaign. Do not mistake this2 ps
frozen box for a validated full-device kinetic simulation.

## Evidence, tests and credit

Sixteen new regressions pass;17 v1.2 regressions also pass in its OpenMC-enabled
environment. Same-seed replay number/energy/momentum logs are byte-identical.
Initial setup/dependency failures and reduction issues are retained in
AUDIT_HISTORY.jsonl. Full plotfiles are regenerable; baseline raw daughter
particles, all used inputs/reduced diagnostics, upstream analyses, spectra,
ledgers, environment and hashes are included.

Dave Sheldon / Atlas Lattice supplied research direction. GPT-6/Tidal Lantern,
DeepSeek and Gemini Argon receive credit for documented preceding analytical
contributions, including Argon's candidate burn/extraction equations. WarpX
contributors receive their own code/algorithm credit under retained upstream
notices. These credits imply no laboratory, university, company or author
endorsement of Beyond Q and no experimental validation.
