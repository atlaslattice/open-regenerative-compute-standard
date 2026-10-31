# Beyond Q v1.4 — From trace-ion slowing to an eight-hour fuel-cycle clock

**Atlas Lattice / STARS 2.0 / Beyond Q. October 30, 2026, America/Chicago.**
Versioned extension of PR #48 at `674eb174ff935bcfc9829109b57c1187d25dc710`.
Historical releases are preserved. All physical gates G1–G5 remain OPEN.

## Outcome and exact scope

Six accepted WarpX cases were retained: the upstream ion-stopping benchmark,
two trace-drag resolutions, two simultaneous drag-and-DT resolutions and a
no-drag DT control. The five custom cases cover **0.1 second of physical time**.
They are prescribed-background, frozen-position, non-depositing collision tests.
Electrostatic mode removes electromagnetic wave evolution; there is no resolved
confinement, laser, particle transport or self-consistent plasma response.

The reduced drag/reaction model is compared with those actual runs. It then
supplies conditional fast/thermal burn and escape fractions to **54 eight-hour
fuel-cycle cases**. Eight hours is the plant accounting clock, not the duration
of fully resolved WarpX reactor dynamics. Increasing a timestep is not a proof
that omitted physics is negligible.

The original wrong attachment concerned a separate p–11B target project. The
user explicitly withdrew it. None of that pocket/laser-acoustic work is imported.

## Power-basis reconciliation

A new user-corrected power lock appeared on the v1.3 parent branch during this
work. It explicitly distinguishes gross fusion power from electrical output.

| Configuration identity | A gross DD fusion | B gross DT fusion | Interpretation |
|---|---:|---:|---|
| historical_20_1130 |20 MW|1130 MW| Published historical audit benchmark retained |
| dual_laser_1100_1100 |1100 MW|1100 MW| Current repository two-laser design input; performance unvalidated |

For the new laser scenario, the historical **20 MW net electrical assumption**
is a distinct field and is never used to determine reaction births. Explicit
`A_gross_fusion_W`, `B_gross_fusion_W`, computational MW values and named identity
must agree; mixed inputs are rejected. No older525 MW/500 MW configuration is
substituted. Old test fixtures retain their own historical meaning.

The laser cases prescribe gross fusion power averaged over an ON schedule slot.
No pulse energy, repetition rate, laser wall-plug efficiency, target gain or
plasma solution demonstrates that power. Reusing the reduced plasma and blanket
coefficients at that input level is an unqualified scaling scenario, not a laser
simulation or proof of sustained operation. B net electrical output remains
unresolved. Neither configuration is declared self-sufficient.

## Background-drag model and numerical verification

The source is WarpX 26.10's `background_stopping` implementation, citing Goldston
and Rutherford §14.2. Denote proper velocity u=gamma*v and
W=m_T*u²/2. For actual kinetic energy K:

`W=K+K²/(2*m_T*c²)` and `K=2W/(sqrt(1+2W/(m_T*c²))+1)`.

Electron drag applies `du/dt=-alpha_e*u`; thus `dW/dt=-2*alpha_e*W`.
Ion drag applies `dW/dt=-alpha_i/sqrt(W)`. The reduced combined equation is:

`dW/dt=-2*alpha_e*W-alpha_i/sqrt(W)`.

The code documents SI coefficients, charge, mass, Coulomb logarithms and
background temperatures. alpha_e has units1/s; alpha_i has unitsJ^(3/2)/s.
Kinetic versus proper-energy variables are not silently interchanged.

In the trace benchmark, initial T kinetic energy is1 MeV, electron density and
D-ion density are1e20m^-3, electron temperature10 keV, D temperature20 keV. Position
pushing and charge deposition are disabled, and the background is an externally
maintained reservoir. Electron-only, ion-only, combined and no-drag tracer
species have independent diagnostics. There is no energy diffusion or backreaction.
The upstream stopping case and its supplied analysis pass unchanged.

Electron-only and ion-only numerical results agree with the shared closed-form
solutions near floating-point precision. Combined-drag maximum relative energy
error is about8.70e-5 at1ms steps and approximately half that at0.5ms steps.
This is splitting convergence against the same approximate physics. It is not
an experimental test or a general finite-temperature Fokker–Planck validation.

## Simultaneous slowing and D-T reaction check

A separate test begins with a1 MeV trace-T population at1e12m^-3 and Maxwellian D
at1e20m^-3,20 keV. The8m³ numerical volume contains8e12 physical-weight tritons.
D/T/macroparticle populations are sampled, frozen in position, and allowed to
react while T experiences prescribed electron/ion drag. Products are He4 and
neutrons. No DD tritium birth occurs inside this particular case: the earlier
v1.3 DD-birth network is the separate source benchmark.

The reduced comparison integrates `dS/dt=-n_D*<sigma*v>(K(t))*S`, using a
Gauss-Hermite Maxwellian-D quadrature and the same Bosch-Hale cross-section
parameterization. Shared nuclear physics means this checks implementation and
reduction assumptions, not independent experimental reaction data.

| Accepted case | WarpX T burn fraction over0.1 s | Reduced fraction | Relative model difference |
|---|---:|---:|---:|
| Coupled,1ms |0.003836614|0.003840305|+0.0962%|
| Coupled,0.5ms |0.003853316|0.003840305|−0.3377%|
| No drag |0.003327448|0.003336749|+0.2795%|

Surviving T reaches roughly750 keV under combined drag, while the no-drag control
remains1 MeV. Tritium-consumption and neutron-coproduct identities close in the
recorded weighted counts. The stochastic burn differences do not monotonically
shrink with timestep and are not presented as physical uncertainty intervals.

An initial attempted coupled setup incorrectly used a constant-momentum field
that left T at rest. It produced large disagreement and zero initial T energy.
Those three cases are **REJECTED_SETUP**, retained with inputs, logs and their
failed comparison under outputs/failures/cold_triton_initialization. Explicit
parsed momentum corrected the setup; a regression now requires the actual
initial diagnostic to equal1 MeV. No cross section was tuned to repair agreement.

## Energy boundary

The prescribed drag background absorbs energy and momentum without evolving.
A closed particle-only energy balance would therefore be the wrong boundary.
We record:

`external_background_sink = initial_particle_K + fusion_reaction_Q - final_particle_K`.

Fusion Q is17.58929696MeV per weighted DT reaction, counted once. For the1ms
coupled case, this inferred sink is~0.319838J; the reduced integrated drag sink
is~0.319749J. The no-drag inferred sink is−2.37e-8J, a retained roundoff residual
against a~3.86MJ background kinetic pool, not negative physical heating.

These tests do not predict recoverable heat or net electricity. The reservoir,
laser/heating power needed to maintain it, field dynamics, material deposition,
radiation and thermal removal are not solved. The reduced fast-particle energy
ledger separately tracks drag losses, energy carried by fast burn/escape and
survivors at the thermal transition. It never adds full fusion Q to neutron
kinetic energy or labels an external reservoir sink qualified useful output.

## Escape and fast-to-thermal reduction

A newborn-triton candidate starts at1.01 MeV, a nominal source assumption rather
than a fitted mean from the new test. Along the drag trajectory:

`dS/dt=-(lambda_DT(K)+1/tau_fast)*S`,
`dP_fast_burn/dt=lambda_DT(K)*S`,
`dP_fast_escape/dt=S/tau_fast`.

The fast-stage identity is `P_fast_burn+P_fast_escape+S=1`. Its energy partition
is checked separately. At an **assumed100 keV transition**, survivors enter a
thermal compartment with rate n_D*<sigma*v>_thermal and prescribed exponential
escape time tau_thermal. Eventual conditional thermal burn is
`r_thermal/(r_thermal+1/tau_thermal)`.

For n_e=n_D=1e20m^-3, Te10 keV, Ti20 keV, tau_fast=tau_thermal=1s:

- Time to transition:0.508307s.
- Fast burn probability:0.0279713.
- Fast escape probability:0.393193.
- Surviving transition fraction:0.578836.
- Conditional thermal burn:0.0418032.
- Eventual total burn:0.0521685.

These are **POTENTIAL-DERIVED**, not established confinement or reactor outputs.
An instantaneous conversion from100 keV to a30keV mean thermal state is assumed;
the corresponding kinetic-energy gap is explicitly assigned to the background.
A real thermal distribution, diffusion and equilibration are not demonstrated.
The fast-ion asymptotic drag approximation is especially unqualified near the
transition: v_T/v_thermal,D is only about1.5 at100 keV. Electron/ion temperatures
and escape times remain imposed. The0.1 s benchmark does not independently
validate extrapolation to the0.508 s transition or eventual burn.

A36-case scan varies density5e19/1e20/2e20m^-3, Te5/10/20 keV and residence
0.1/1/10/60s. Total candidate burn ranges~0.00176–0.8432. This is a sensitivity
envelope, not a probability/confidence interval for a physical reactor.
Transition100/200/300keV, quadrature order and ODE tolerance studies are retained.
Order12→16 changes reference burn probability by~6.2e-7 absolute. No37% target
is imposed, recovered as a required answer, or ruled out by this approximation.

## Eight-hour integration and conservation

The versioned v1.2 inventory implementation is adapted to explicit schedule
slots:480 minutes, each1/1440 calendar day. All rates remain1/day; the output
clock ends at8 h. There are eight nonnegative stocks: A plasma, A/B blanket,
independent A plasma/blanket processing, B processing and A/B storage.

Fast burn, fast escape and entry to the thermal compartment are disjoint
fractions. Fast escape feeds A plasma-derived processing; it does not disappear
or burn again. The subsecond fast-stage delay is collapsed at the minute scale;
its omitted transit holdup is bounded by DD T birth rate times transition time,
about43.5micrograms in the historical case and2.39mg in the laser-power case.
That timing approximation is disclosed; it is not a qualified startup correction.

Actual v1.2 DD/DT neutron-response means are reused for A0/A1/A2 and B. Their
assumed spherical geometry,293.6K data, structural surrogates and monoenergetic
source boundaries remain unqualified for the new laser design. There is no new
OpenMC run, new TBR validation or transport uncertainty propagation here. A0
retains the inherited nonbreeding-shield/thermal-engineering limitations. A2 is
an exploratory enrichment/thickness candidate, not an engineering optimum.

Each power identity has27 cases: A0/A1/A2 times continuous, independent15min B
outage, common30min outage, B processor/extractor30min outages, zero initial B,
poor recovery, zero A transfer reserve and secondary-off. Common shocks and
independent schedules remain separate. Scheduled B demand is fuel-limited:
no fuel means no actual fusion, blanket birth or source energy.

| Eight-hour A1 continuous quantity | Historical20/1130 MW | Dual-laser1100/1100 MW input |
|---|---:|---:|
| DD T birth |2.46648g|135.656g|
| A internal T burn |0.12867g|7.07687g|
| B actual T burn |57.8010g|56.2665g|
| Total mobile-stock change |+6.31853g|+240.244g|
| B final available storage, initial10kg |9.36015kg|9.37713kg|
| A→B transfer with inherited0.25kg A reserve |0|0|

A positive total-stock change does not establish usable export or replenished B
storage. Processing/blanket/A stocks account for material unavailable to B at
that instant. Under the inherited A reserve policy, neither power identity
exports T to B within eight hours. The zero-A-reserve control delivers about
0.256g and14.099g, respectively, showing the policy/timing dependence. It does
not establish a qualified reserve policy.

Zero-initial-B cases cannot serve their full scheduled burn; retained A material
is not silently made available across the reserve rule. Finite-horizon startup
bisections give A1 initial-B brackets near0.63937kg historical and0.62239kg
laser-power input; processor-outage brackets rise to~0.65361/~0.63625kg.
These are arithmetic fuel-availability brackets under stated assumptions,
not qualified startup inventory or indefinite-operation thresholds.

All54 mobile mass ledgers close below1e-8kg. Minute/30s/15s refinement changes
A1 final total stock by~0.20mg historical and~6.27mg laser-power input. Startup
bisection endpoint digits are algorithmic resolution, not physical accuracy.
Tritium decay, permeation and separate processing losses remain explicit. B
recirculation/processing counts are throughput of existing atoms, not new births.
Kg and percentage of actual B burn are reported; qualified-surplus fields are null.

## Evidence and remaining gates

SOURCE-TRACED: pinned software, sources, input provenance and power-basis receipt.
VERIFIED-DERIVED: units, numerical identities, software checks and conditional
arithmetic. POTENTIAL-DERIVED: all assumed-background/plasma/plant outputs.
UNRESOLVED: physical model validity and qualification for the intended reactor.

| Gate | Progress | Remaining physical requirement |
|---|---|---|
| G1 | Actual drag/DT numerical comparisons and conservative escape model | Self-consistent plasma/confinement, diffusion, thermal transition and laser operating state |
| G2 | Reuses bounded v1.2 transport | Qualified geometry, source spectra, hot-state nuclear data and external blanket benchmarks |
| G3 | Separate source recovery and extraction paths retained | Measured material chemistry, permeation, processing purity/efficiency and wall inventory |
| G4 | Explicit eight-hour clocks, adverse controls, startup brackets | Qualified reserves, operating/repair schedules and long-duration deployment model |
| G5 | Open-background collision energy ledger and source boundaries | Laser/heating inputs, full material energy closure, heat removal and net electricity |

All remain physically OPEN. Independent complete Fokker–Planck/particle-collision
comparison near the thermal transition is a priority. Longer times in a reduced
model do not replace those missing physical tests. No indefinite tritium supply,
validated power plant, qualified surplus or institutional endorsement is claimed.

Final numerical verification: **19 new v1.4 tests and16 archived v1.3 tests pass**. Machine-readable results and full suite logs are retained. These checks do not change any physical gate status.
