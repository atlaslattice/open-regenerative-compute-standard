# Beyond Q v1.9 — 350,000-liter total-capture targets with continuously scheduled B

1 November 2026. Additive continuation of v1.8/draft PR62. The user target is
**350,000 STP liters of total captured He-3 and direct D-D tritium coproduct
per model year, before any He-3 retention/sales split**, followed by explicit
accounting for B's burn and its separate lithium breeding. This corrects the
previous controller's external-sale-candidate target; it does not change nuclear
physics to force a result.

Two proposed1100MW ARC-class sources remain the primary architecture. A is the
D-D refinery; B is D-T. The owner-historical A+20MW net-electric projection is
separate from fusion power and remains unvalidated. Laser energy is a separate
matched-exposure variant, not the primary ARC apparatus or achieved laser yield.

## Resolve the gas-volume convention explicitly

All gas volumes here are STP at0C/1atm, using22.414L/mol, not liquid-helium liters.
Equal D-D branch counts produce equal T and He-3 **atom counts**, not identical
molecular gas volumes after collection.

| Meaning of350,000STP L | Isotope mass |
|---|---:|
| Monatomic He-3 |47.0960kg|
| T atom-equivalent volume |47.0963kg T|
| Molecular T2 gas volume |94.1927kg T|

The primary equal-atom convention matches the earlier paired-coproduct volume
comparison, while reporting T in kg prevents ambiguity. At that T mass,
physical T2 gas occupies175,000STP L. A companion run instead requires350,000L
of actual T2; it is not silently substituted into the primary result. T2 carries
two T atoms per molecule. No assumption that recovered T literally remains a
monatomic gas is made.

Targets are **minimum quantities**, not a hard cap. A can run longer for fuel
reserves or to meet the slower of the two capture routes. Direct birth equality
does not guarantee equal delivered quantities because secondary T burn, route
recovery and collection delay differ.

## Operating boundary and candidate assumptions

The model starts with zero isotope inventory, runs A alone for168hours, then
permits B in every hour of three365.25day model years. Unlike v1.8, no planned
macroscopic outage is inserted. The ARC15min-flattop/1min-between cycle is still
represented by15/16 source duty, so8766 clock hours are0.9375full-power years.
Actual B consumption remains bounded by available T. A switches on for either
production target or its10/20kg B-storage reserve hysteresis. The24hour on/off
limits remain candidate controls; the10kg trigger is not a qualified launch
reserve. Stocks never reset between years.

For1100MW D-T, one complete full-power year burns61.6540kg T. Continuous
calendar scheduling with15/16 source exposure burns57.8006kg/year. Both figures
are recorded in `mass_reference.json`; neither400MW net electricity nor500MW
gross electricity is used as the fusion source term.

A blanket breeding is zero (A0). B gross TBR0/0.95/1/1.05 are sensitivities;
TBR1 is the conservative replacement reference. Current public ARC materials
specify a goal above1, not the exact numerical V3A TBR used here. Gross B birth
is not recovered B fuel, and it cannot supply startup inventory before B burns.
All extraction, processing, permanent losses, decay and inventories remain in
the inherited candidate engine. Secondary D-He3 consumption is still omitted.

He-3 capture90% and1/day collection are assumed. T recovery comes from the
existing independently parameterized A plasma processing route, after A's
internal T consumption and its route losses. Its cumulative once-through
`a_plasma_processed` counter supplies the production target. B recirculated
throughput is never treated as fresh tritium production.

## Primary reference result: B gross TBR1

| Operating year | A on-hours | Total captured He-3 | Direct T recovered to storage | B T burned | B blanket T born | Total T stock change |
|---|---:|---:|---:|---:|---:|---:|
|1|3292|352,579STP L|47.209kg|57.801kg|57.801kg|+44.772kg|
|2|3316|352,581STP L|47.465kg|57.801kg|57.801kg|+42.658kg|
|3|3316|352,581STP L|47.465kg|57.801kg|57.801kg|+40.324kg|

These exclude the preceding startup phase, which is exported separately.
T atom-equivalent delivery is350,838L in year1 and352,740L in years2/3. B is
scheduled throughout and no modeled fuel shortfall occurs beyond roundoff.
Targets are met with small overshoot from timing and minimum on-periods.
All quantities remain POTENTIAL-DERIVED; captured material is not certified
research-grade product, and stock growth is not qualified usable surplus.

## Subtract B burn once, and credit B breeding once

The year1 direct-A-only screen is **47.209−57.801=−10.591kg** before crediting
B's blanket. Therefore350k atom-equivalent liters of A-produced T alone cannot
cover B's full annual burn at this power. B's own breeding is essential to the
reference interpretation. A's output must not be sold or counted twice while
also being claimed as consumed fuel.

The complete campus ledger is instead:

`change in T stocks = DD T births + B blanket T births - A internal DT burn - B DT burn - decay - processing loss - permeation`.

Recovered A delivery and B blanket extraction are internal transfers, not
additional births to append to that identity. The output therefore reports
both the direct-delivery-minus-gross-B-burn screen and the conserved campus
stock change. It also reports B's gross births minus burn, separately from
extracted-to-processing material. B's gross replacement margin is zero at
TBR1, while recovery losses and delays remain real modeled sinks/holdup.

The positive reference stock change is after all modeled sinks. It remains
unqualified retained inventory, not sales cash or a demonstrated indefinite
supply. Its decline across years reflects growing inventory decay. No tritium
sales are credited, and decay-derived He-3 supplies no production/revenue credit.

## Adverse control and the molecular interpretation

When B breeding is set to zero, reserve control runs A beyond the350k target.
Captured He-3 becomes approximately509k/496k/408k L across years1/2/3. Direct
T delivery becomes68.578/66.533/55.178kg. B still burns57.801kg each year;
year3 draws accumulated reserve, with a4.229kg decline in total T stocks. This
finite-horizon result is not proof that a fixed350k production ceiling could
sustain B without breeding. The controller explicitly allows greater production.

For the companion **350k molecular-T2-liter** target at B TBR1, year1 delivers
approximately94.288kg T (350,353T2 liters), with approximately702,289L captured
He-3. A meets the larger T molecule count by producing more D-D reactions; it
does not create a factor-of-two isotope bonus. Both volume conventions remain
visible in every annual row.

## Electricity, He-4 and product allocations

Both architecture electricity adapters run on the actual A/B schedule. ARC
unknown A net draw stays null; owner-historical+20MW net and100/400MW draw
cases remain assumptions. Laser gains10/100 at20% efficiency remain scenarios.
ARC's published net output is not charged a second own-load deduction.
No new physical laser gain or A retrofit budget is inferred from this dispatch.

Plasma He-4 from actual A/B D-T is retained in its candidate capture ledger.
Blanket He-4 implied by Li pathways is separately unavailable. No research-grade
certification or refrigeration-energy credit is assigned. The inherited50%
He-3 retention and90% quality-acceptance assumptions apply only downstream of
the350k total-capture target: they cannot halve the target itself or make every
captured liter a sale. Actual revenue, full costs and profit remain unresolved.
No actual He-3 sales or internal helium withdrawals occur in the stock model.

## Verification, provenance and use

Twelve three-year source simulations compare three policies at four B-TBR
values. Outputs contain48startup/year fuel-product rows,288architecture-energy
rows, weekly stocks, an independent mass/volume reference and a filtered350k
reference table. The source model is shared at matched exposure; ARC/laser
energy differences are not driver-specific isotope yield predictions.

Twelve checks pass: total capture versus sales target; explicit molecular
convention; exact factor two and mass conversion; continuously permitted B;
reference target attainment; direct-only deficit distinguished from campus
balance; zero-breeding source control; T conservation; stock continuity;
electrical/null-revenue accounting; no repeated counting of recovered T;
and physical-status/isotope-mass residual checks.

From this directory, Python standard library:

```bash
python capture_provenance.py
python run.py
python summarize.py
python -m unittest test_target -v
```

Optional `python plot_results.py` requires matplotlib. The neighboring versioned
v1.4/v1.7/v1.8 modules must remain at repository paths. Exact imported source
bytes are checked using Git blob and SHA256 manifests; historical artifacts
are preserved. Numerical timestep caveats and the isolated controller hook are
documented in v1.7/v1.8; no new WarpX/OpenMC run is performed.

SOURCE-TRACED: pinned code, current two-ARC design lock and prior source registers.
VERIFIED-DERIVED: conditional atom/molecule conversions and numerical ledgers.
POTENTIAL-DERIVED: all annual production, recovery, inventory and energy cases.
UNRESOLVED: achieved DD operating point, actual TBR, qualified recovery/purity,
D-He3 burn, restart dynamics, replacement, external demand and full economics.
Physical G1–G5 remain OPEN; successful arithmetic does not validate a reactor.

This is the user-directed total-coproduct target checkpoint. Next close the
physical recovery/operating-point gaps and couple real withdrawals, capacity,
reserves and costs before promoting retained stock into qualified usable surplus.

Dave Sheldon / Atlas Lattice provides research direction. GPT-6/Tidal Lantern,
DeepSeek and Gemini Argon retain credit for documented analytical contributions.
No institutional endorsement or experimental validation is implied.
