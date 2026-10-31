# Beyond Q v1.8 — reserve- and isotope-target-driven three-year operation

31 October 2026. Additive research continuation of draft PR60/v1.7. This replaces
A's prescribed all-year schedule with a tested heuristic controller while
preserving all fuel compartments between model years. It also reconciles the
newly located primary **two-ARC** design lock and the historical A+20MWe net
projection. Laser energy sensitivities remain a separate comparison variant.

This is a conditional operating-policy experiment. It does not calculate a
self-consistent1100MW D-D plasma, validate blanket recovery or certify products.

## Architecture and unresolved operating budget

Both reactors have proposed1100MW fusion sources. The current design lock
names ARC-class tokamaks as primary and preserves A's historical+20MW net
projection. The older20/25MW-DD scenarios cannot supply that operating budget.
`POWER_BASIS_RECONCILIATION.md` records exactly what was located and what was
not. +20MW is not silently promoted into a physics-derived result.

For electricity, this package reuses v1.7's matched1100/1100 ARC and laser
adapters. Both receive15/16 source exposure for a controlled comparison. The
laser duty here is not a simulated pulse train. ARC B gross electricity scales
the published approximate500MW at1130MW fusion to1100MW, then subtracts the
approximate100MW own load once. That interpolation remains assumed; it is not
an exact new ARC design point. The additional10MW campus/processing load,
shutdown loads and other engineering assumptions are unchanged from v1.7.

ARC A net-draw cases are unknown, **−20MW** (the owner-historical+20MW net output
projection),100MW and400MW. The unknown row stays null. Laser gain10/100 at20%
wall-plug efficiency are sensitivities. No new kinetic or neutron-transport run
is performed. All physical G1–G5 remain OPEN.

## Fuel and product policies

The model starts with zero inventory and7days of A-only precharge, followed by
three365.25-day years. It includes one assumed14-day common outage in year2.
Stocks continue across precharge and every year boundary; no year-end refill
or reset is introduced. B operates whenever its permitted calendar allows it,
subject to actual available fuel. No fresh external T enters after startup.

A's blanket breeding is set to zero (A0) for this experiment. B gross TBR values
0.95/1.0/1.05 are **assumed sensitivities**, not published ARC values. Official
current ARC materials state a goal above1 but do not supply an exact V3A number
in the inspected sources. Gross breeding remains distinct from delivered fuel;
extraction, processing, permanent losses and decay remain in the model.

B-storage reserve hysteresis calls A on below10kg and releases that call above
20kg. The10kg threshold is a controller trigger, not a hard startup reserve: B starts
after the assumed7day precharge even if storage is below10kg. A also runs if the selected model year's He-3 candidate-production target
is not met. Targets are0/10k/100k/500k STP liters per model year, not measured
customer demand. Target0 gives reserve-only operation. Always-on is the baseline.
The controller uses captured He-3 accumulated in the current year, not gross
birth or current spot value. It retains50% of captured He-3, then applies an
assumed90% quality-acceptance yield to the remaining fraction.

Collection rate1/day and capture90% are inherited assumptions. This quality
acceptance is not a chemical purity claim. Direct D-D He-3 is the coproduct
source; T-decay He-3 receives no sales or controller credit. No T is sold.
No He-3 is actually sold in the physical stock trajectory either: the quantity
is a potential annual allocation, with actual qualification/revenue unresolved.
Real sales, internal consumption and tank capacity need subsequent coupling.

Minimum on/off times are assumed24hours, except a low-reserve emergency can
request A earlier. The controller cannot override a maintenance prohibition.
A shutdown is not assumed to change nuclear cross sections; it changes the
source and the inherited plasma escape/burn gates. Thermal inertia, heating to
restart, magnet ramping, reaction-rate transients and restart wear are not solved.
The policy is a transparent heuristic, not an economic or physically qualified
optimum. Production targets apply afresh each year; physical isotope stocks do
not reset. Unsold previous stock is not a new birth or revenue stream.

## Three-year findings

At assumed B TBR1.0, with the same candidate recovery parameters:

| A policy | A operating hours, including startup | Final total T stock | He-3 candidate output by year1/2/3 |
|---|---:|---:|---:|
| Always on |26,130|343.788kg|419,428 /403,352 /419,429 STP L|
| Reserve only |1,498|17.868kg|64,784 /0 /0 STP L|
| Reserve +10k L/year |1,964|24.006kg|64,784 /11,148 /11,148 STP L|
| Reserve +100k L/year |6,487|83.235kg|101,196 /101,149 /101,149 STP L|
| Reserve +500k L/year |26,130|343.788kg|419,428 /403,352 /419,429 STP L|

Reserve-only runs A for about5.7% of the always-on hours over this finite
experiment. The100k target uses about24.8%. The year1 reserve buildup can
produce more He-3 than a low production target requests. The500k target is
unreachable under these source/capture/retention assumptions: its shortfall is
explicit, rather than filled by a fabricated source. Year2 has the shared outage.

No modeled B fuel shortfall occurs in the15 tested policy/TBR combinations
beyond floating-point roundoff. This means the candidate controller and stocks
serve this finite three-year schedule **conditional on the assumed breeding
and recovery**. It does not validate B self-sufficiency, select a qualified startup
reserve or demonstrate indefinite operation. Larger independent outages,
maintenance/replacement, lower recovery and altered physics can change results.

## Energy interpretation

Every actual on/off hour feeds both architecture adapters. Imports and positive
electricity accumulate separately. Startup and each model year have independent
energy rows; no later export cancels an earlier physical import. Actual A T
consumption creates secondary D-T energy only once, and B energy follows actual
burn; unfueled operation does not generate fictitious fusion heat.

If A really delivered the historical+20MW net, switching it off would reduce
that net generation; a production-target heuristic would not automatically
maximize electricity or profit. If A instead draws100/400MW, reduced runtime
reduces its electrical burden. The laser cases retain their own gain-dependent
wall-plug balance and never inherit ARC's net-power figure. Full economic or
commercial conclusions remain unresolved in every case.

## Helium and conservation

The He-3 collection compartment used by the controller is independently replayed
from the completed reaction counters for reporting. Source, mobile stock,
capture loss and accumulated storage close. Plasma He-4 from both A-secondary
and B D-T is also collected at assumed1/day,90% capture, with no sale or free-
cooling credit. B blanket helium implied by Li6/Li7 breeding is separately
reported as unavailable; no blanket gas-extraction system is invented.

T balance per year is direct DD birth + B blanket birth − A/B burn − decay −
processing loss − permeation = stock change. Internal transfer is not a source.
He-3/He-4 atoms use their own isotope masses, and reaction energies retain the
v1.7 convention3.65MeV weighted DD /17.6MeV DT. The newly recovered design lock
uses slightly different rounding; no physics improvement is inferred from it.
D-He3 secondary consumption remains omitted, so He-3 survival is unqualified.

## Verification and reproducibility

Fifteen architecture-neutral source simulations run five policies at three
B-TBR sensitivities. Each covers startup plus three years with matched1100MW
fusion sources. Their energy is evaluated by separate ARC and laser adapters;
this is not30 independent plasma simulations. Outputs contain60 phase/year
fuel rows,360 electrical rows and weekly stocks for all15 cases.

Twelve tests pass: canonical power/projection separation; unchanged-engine replay;
maintenance permissions; reserve hysteresis/emergency; yearly T closure; no stock
reset; reduced reserve-only runtime; visible unreachable target; T retention and
null revenue/profit; unknown energy; electrical balances; isotope conservation.
Input Git-blob/SHA256 verification includes the independently updated design lock.
`CORE_CHANGES.diff` isolates the hourly policy hook. A callback receives copies
of stocks/counters and cannot activate a prohibited reactor.

From this directory, Python standard library:

```bash
python provenance.py
python run.py
python -m unittest test_dispatch -v
```

The neighboring versioned v1.7 and v1.4 inputs must remain at repository paths.
Optional `python plot_results.py` requires matplotlib (figure generated3.10.8).
Weekly stock plots are samples, not a claim that intrahour behavior is resolved.
Earlier releases and failure histories are unchanged. See v1.7 for timestep
comparisons; this release does not reinterpret their numerical errors as physical
uncertainty bounds. Assumed TBR/target sensitivities are not probability intervals.

## Evidence and next work

SOURCE-TRACED: owner design lock, recovered older archive and pinned code.
VERIFIED-DERIVED: clocks, conditional balances, controller execution and tests.
POTENTIAL-DERIVED: every reactor-scale output and operating-policy result.
UNRESOLVED: A's full net-power derivation, plasma confinement, actual TBR/recovery,
product grade, market demand, sales withdrawals, tank capacity, replacement
schedule, full costs and profitable/indefinite operation.

Priority next inputs are the current-power A thermal/electrical operating sheet;
qualified TBR and route recovery; measured He isotope extraction and D-He3 burn;
restart/replacement dynamics; and demand-linked internal/external withdrawals.
A true operating optimization must include those costs and constraints before
ranking policies. No need to force a positive surplus or economic outcome.

Dave Sheldon / Atlas Lattice supplied the research direction and isotope-refinery
objective. GPT-6/Tidal Lantern, DeepSeek and Gemini Argon retain credit for their
documented analytical contributions. No institutional endorsement, achieved
laser gain, experimental validation or operating commercial reactor is implied.
