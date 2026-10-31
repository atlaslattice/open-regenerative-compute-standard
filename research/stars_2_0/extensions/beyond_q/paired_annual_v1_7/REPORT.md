# Beyond Q v1.7 — paired ARC / laser annual accounting

31 October 2026. Conditional research package, stacked on v1.6. This integrates
annual electricity, tritium fuel/inventory, direct He-3 and plasma He-4 products
for two proposed architectures. It supplies common bookkeeping and falsification
controls, not two physically validated reactor simulations.

**Campus purpose:** A is the isotope refinery; its direct D-D tritium supports
startup, loss makeup and reserves for B; B's own lithium blanket approximately
replaces B's consumption; He-3 is the primary candidate commercial coproduct.
He-4 is accounted for as a possible internal cryogenic feedstock. T external
sales are zero. No decay-derived He-3 revenue is credited.

## Configuration and clock locks

| Configuration | A primary D-D nominal fusion | B D-T nominal fusion | Within-operating-hour source duty | Meaning |
|---|---:|---:|---:|---|
| ARC reference |1100 MW|1130 MW|15/16|B rounded published reference; hypothetical D-D retrofit|
| ARC matched-power control |1100 MW|1100 MW|15/16|B power counterfactual, not another published ARC point|
| Laser prescribed source |1100 MW|1100 MW|1|Prescribed fusion, not achieved laser target gain|
| Laser matched-exposure control |1100 MW|1100 MW|15/16|Same source exposure as matched ARC; not a laser pulse simulation|

ARC's empirical point is 1133 MW in the source paper; 1130 MW is its rounded
reference here. Neither 400 MW net electricity nor 500 MW gross electricity is
used as a fusion source. The older 500 MW fusion scenario, A20MW/B1130MW
scenario and historical A20MW **net electrical** assumption remain preserved
in preceding packages; none is silently installed here.

Each run has seven days (168 h) of A-only startup, followed by a 365.25-day
(8766 h) modeled calendar year, with zero initial T. Cold-start controls omit
the precharge. Stocks and cumulative counters carry continuously across the
transition. This precharge is an assumption, not a minimum qualified reserve.
A full-power year means 8766 h at full nominal source. Thus a continuous ARC
calendar case with 15/16 source duty has 0.9375 B FPY exposure, not one full
B FPY. Macroscopic outage hours reduce exposure further. Both calendar clocks
and source FPY exposures are exported.

The source is averaged over subhour pulses, not resolved pulse-by-pulse. The
15/16 A retrofit duty is assumed. Thermal and laser pulse dynamics, startup
transients, ramp rates and restart/repair costs are not solved.

## B lithium replacement and A breeding cases

The default **B_replacement_A1** sets gross B TBR=1.0: one blanket-born T per
actual B D-T reaction. It is an **ASSUMED replacement-level scenario**, not a
neutronics result or proof of self-sufficiency. Extraction, holdup, decay,
permeation, repeated processing and permanent losses still apply; replacement
birth before losses does not mean recovered fuel delivery equals consumption.
A supplies initial stock and remaining makeup. B births cannot occur before
B burns. No B theoretical surplus is assumed or separately monetized.

**Official-source reconciliation:** the 2026 ARC V3A overview states TBR>1,
without a precise numerical breeding value in the inspected text. CFS's LIBRTI
statement also targets net tritium production, including fuel for future plant
startups. UKAEA confirms that breeding/extraction are to be tested at engineering
scale. Therefore literal zero B surplus is not the official design objective.
Our TBR1.0 case is a conservative replacement sensitivity; it is not ARC's quoted
TBR. The exact current gross TBR and recovered-delivery margin remain unresolved.
Do not substitute a number from the older ARC V0 geometry. See sources [S5-S6].


A0, A1 and A2 counterparts use this same B policy. A0 has no A blanket breeding;
A1 uses the inherited natural-lithium testbed response; A2 uses the inherited
exploratory enriched response. Their blanket efficiencies are unqualified for
an actual reactor. Two additional sensitivities preserve the inherited
A1+B-TBR1.044 response and disable breeding in **both** reactors respectively.
The all-zero case is an adverse control, not the normal campus architecture.

Six schedules share the same clocks: continuous; independent 14-day A/B
outages at different dates; correlated 14-day outage; A off for 90 days near
the start of B's year; B off for 90 days; and cold startup. They are explicit
stress calendars, not probability or reliability predictions. Processing and
extraction continue during reactor outages under inherited assumptions.

## Energy boundaries

### ARC reference

The public design balance is approximately 500 MW gross electricity minus
100 MW own electrical loads = 400 MW net. These values are already averaged
over 900 s fusion flattop and 60 s between flattops [S1]. Fuel source duty is
applied separately; the 400 MW net must not be averaged or debited twice.

For an on-hour, the screening B electrical term is:

`B_gross = 500MW × (B_nominal_fusion_MW/1130) × actual_burn/scheduled_burn`;
`B_net = B_gross - 100MW`.

This interpolation for fuel starvation and for the matched-power counterfactual
is an assumption, not a source-qualified part-load curve. During macroscopic
shutdown, B generation is zero and assumed shutdown demand is 5 MW. The source
already includes B's own plant loads; no second 100 MW subtraction is added.

A's D-D retrofit net electrical draw remains **UNRESOLVED**. Its primary row
therefore has no numerical ARC campus balance. Separate assumed net-draw stress
cases are 100/400/800 MW while A is on, and 5 MW when off. These are **net A
loads**, including any unmodeled A thermal recovery by definition; A reaction
heat is not separately credited on top. An assumed additional 10 MW campus /
isotope-processing load is debited once, outside the B reference boundary.

### Laser scenarios

Primary A D-D optical input = actual primary-DD fusion Q / assumed gain;
B optical budget = scheduled B D-T target energy / assumed gain, even when
B is fuel-limited. Wall electricity divides optical input by assumed efficiency.
Gain values 1/10/100 and wall-plug efficiencies 10%/20% are stress cases, not
technology forecasts. Gain for A is defined against **primary D-D only**;
secondary D-T reaction energy is additional and not an independent 18 MW input.

Formal gross electricity = (primary DD + actual A/B DT fusion Q) × assumed
90% collection × assumed 40% conversion. Combined laser auxiliaries are assumed
50 MW throughout, plus the separate 10 MW added load. No measured target gain,
laser source distribution or end-to-end laser reactor operation is established.

### Thermal ledger and unresolved reconciliation

Reaction Q is partitioned into charged-particle and neutron energy exactly
once. Those partitions are not added to total fusion Q. Assumed blanket nuclear
Q is exported separately and not appended to either electrical estimate.
The source ARC paper has its own blanket/plant heat balance. The inherited
all-Li6 blanket-Q assumption is not demonstrated to reproduce its approximately
100 MW blanket heat; this is an explicit **UNRESOLVED thermal reconciliation**,
not a calibration adjustment. Deposited heat and complete plant energy closure
remain unqualified. The comparison does not manufacture transport heat tallies.

Hourly imports and positive electricity accumulate separately. Later generation
cannot erase a startup import without a storage/settlement model. Year-only
energy and startup energy are exported alongside their combined 8934 h window.
Intrahour peaks, energy storage, export pricing and network tariffs are not solved.

## Isotope accounting

- Direct D-D T and He-3 are exclusive branches. Equal branches are retained
  for these annual scenarios; the archived WarpX branch sample is not silently
  installed as either an ARC or a laser operating distribution.
- A and B D-T consume one T and produce one He-4 each. Both sources are logged
  separately, then passed to a new He-4 collection compartment.
- He-3 and plasma He-4 each have mobile collection stock, captured stored stock
  and capture loss. Collection is integrated analytically with an assumed
  1/day extraction hazard and 90% capture. Stored stock does not disappear.
- Additional He-4 implied by Li6/Li7 blanket breeding is reported as conditional
  blanket birth and **unavailable**, without recovery or sale credit. This
  stoichiometric estimate assumes those pathways generated the modeled T.
- T decay creates He-3 atoms, logged separately and unavailable. It is not the
  direct coproduct source, nor the financial premise of this architecture.
- T remains fuel/reserve inventory. He-3 retains 50% of captured stock; an
  assumed 90% acceptance yield applies to the remainder. This is a hypothetical
  mass fraction passing quality checks, not a declaration of 90% chemical purity.
- He-4 may allocate up to an assumed 10 kg of accepted candidate stock internally.
  The remaining stored He-4 stays held. No refrigeration-energy savings or
  market value is credited; helium mass is not free cooling.

Actual qualified outputs remain null. Research-grade certification requires
impurity / residual D-T and radiological tests, separation, product handling
and the intended compressed-gas or liquid specification [S3]. Secondary D-He3
consumption, implanted/wall helium, collector capacity and isotope-separation
power per kg are unresolved. Omitting D-He3 can overstate saleable He-3.

## Numerical findings

For the normal B-replacement policy and continuous A1 reference:

| Operating-year quantity | ARC reference | Laser prescribed source |
|---|---:|---:|
| Direct T birth in A |139.355 kg|148.645 kg|
| T born in B blanket |59.377 kg|61.654 kg|
| T consumed by B |59.377 kg|61.654 kg|
| Total mobile T stock change |+224.375 kg|+239.337 kg|

The large stock changes include **unqualified A1 blanket contributions**, not
qualified surplus. In A0 with no A breeding but the same B replacement policy,
the stock changes are approximately +121.770 kg (ARC) and +129.892 kg (laser).
A2 changes are +241.031 / +257.103 kg. No T is sold in any run.

Captured candidate stock across startup plus the reference year is approximately
127.479 kg He-3 / 79.551 kg plasma He-4 for ARC, and 135.977 / 82.852 kg for the
laser prescribed source. These include A-secondary D-T He-4. Year-only birth
and recovered-flow columns are separate from terminal stock; terminal quantity
is not an indefinitely renewable yearly export.

**Outage falsification:** with B replacement credited, the tested 90-day A
outage has no modeled B shortfall. With both blankets disabled, the same outage
leaves approximately 12.620 kg (ARC) or 13.009 kg (laser) unserved, despite
positive final annual stock growth. Cold startup with B replacement also fails:
approximately 0.281 / 0.283 kg unserved, because B's own breeding cannot supply
initial fuel. Replacement breeding does not remove startup inventory needs.

Representative B-year electrical sensitivities at full service are +290 MW,
-10 MW and -410 MW for the ARC A-draw100/400/800 cases, before other unmodeled
costs. The combined startup-plus-year mean is lower because B is off during
startup. Laser gain10/20% and gain100/20% also produce opposite electrical
signs; these depend on the assumed inputs and are not demonstrated performance.

## Economic screen, not profitability

He-3 price sensitivities are **assumed $500/$1000 per STP liter**, with assumed
external demand caps of 10,000/100,000 STP L over the combined window. Imported
electricity is assumed $0.10/kWh. These are not quotations, forecasts or demand
measurements. Candidate revenue assumes all allocated product qualifies;
actual qualified revenue remains null. Sales are evaluated at the terminal
boundary and do not supply startup working capital.

The screen subtracts import charges only. Internal electricity has capital and
opportunity costs; lack of grid imports does not make energy free. B generation,
A's net draw, internal allocations and gross laser input must not each be charged
again as overlapping complete costs. Export credit, T sales and He-4 revenue
are zero/uncredited. CAPEX, financing, non-electric OPEX, replacement, purification
and full costs remain null. Therefore no total profit or commercial self-sufficiency
is reported, even when an electricity-only margin is positive.

## Verification and uncertainty

120 source/schedule cases, 600 electrical rows (including unknown ARC A-draw
rows), and 2160 price/demand sensitivities are reproducible. Sixteen tests cover
legacy unit-duty replay, power locks, ARC 400 MW accounting, unfueled costs,
unknown inputs, T/He conservation, nuclear-energy partitions, driver-matched
source identity, startup/outage falsification, separate import/export accumulation,
T retention and demand caps.

Reducing the fuel timestep from 15 to 7.5 minutes in two adverse outage controls
changes unserved T by about -2.37/-2.38 g and final total stock by about
-2.73/-2.76 g. Numerical disagreement is retained in `timestep_comparison.json`.
These are numerical comparisons, not confidence intervals on reactor physics.
Parameter stress envelopes are not statistical uncertainty bounds or calibrated
probabilities. Initial test failures and their resolutions remain append-only. Dashboard JavaScript syntax and all120 selector combinations pass a mocked DOM/canvas smoke test; this is not a full visual browser test.

## Gate status and next work

| Gate | Status | Remaining requirement |
|---|---|---|
| G1 plasma / secondary burn |OPEN|Driver-specific distributions, confinement, slowing and D-He3 consumption|
| G2 neutronics |OPEN|Source-qualified ARC/laser geometry, materials, spectra and benchmarked yields|
| G3 extraction / recovery |OPEN|Measured T/He capture, purity, holdup, loss and energy requirements|
| G4 inventory / operation |OPEN|Qualified startup/outage reserves and repeated-year dispatch/replacement|
| G5 thermal / electrical |OPEN|A retrofit draw, full deposited heat and plant/load reconciliation|

The bookkeeping integration is executable. Physical and commercial closure are
not complete. Priority next steps are A retrofit net-load provenance; a source-
qualified laser input/gain distribution; TBR/recovery reconciliation for B;
He isotope capture and certification; and multi-year dispatch that reduces A
operation when reserves and credible He-3 demand are already filled.

## Reproduce and inspect

From this directory, Python standard library:

```bash
python compare.py
python refine.py
python -m unittest test_compare -v
python render_dashboard.py
node check_dashboard.cjs
```

Open `dashboard.html` locally for the offline interactive comparison. The plot
uses weekly samples of the continuous reference; full daily reference values
are in CSV. Outage tables are available for every case, while their full hourly
trajectories are regenerated by the engine rather than copied into large files.
Optional `python plot_results.py` requires matplotlib (generated with 3.10.8).
`SOURCES.md`, input Git/SHA256 hashes, package hashes and `CORE_CHANGES.diff`
record provenance. The neighboring v1.4 scenario input is required. Earlier
research releases are unchanged; no new WarpX or OpenMC run is claimed.

SOURCE-TRACED: public design/specification sources and pinned code inputs.
VERIFIED-DERIVED: conditional identities, unit conversions and software checks.
POTENTIAL-DERIVED: all campus output, recovery and economic sensitivities.
UNRESOLVED: physical performance, purity, full costs and qualified usable surplus.

Dave Sheldon / Atlas Lattice supplies the research direction and the principle
that useful coproducts should not be discarded. GPT-6/Tidal Lantern, DeepSeek
and Gemini Argon retain credit for their documented analytical contributions.
No company, university, laboratory or cited author endorsement or experimental
validation is implied.
