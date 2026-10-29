# Stars operating tracks v0.2 — grid-assisted burn
2026-10-28 America/Chicago. Additive requirement supplement to energy_screen_v0_1. PHYSICAL_CANDIDATE; no confirmed sustained burn, ignition or profitable isotope output is claimed.

## Three research tracks
1. Startup then drive-off burn hypothesis: external startup, followed by a specified interval with no sustaining heating. Ancillary grid services remain in the ledger.
2. Externally driven operation: grid-supported reactions; a useful self-heating contribution is not presumed.
3. Grid-assisted burn hypothesis: reaction-product self-heating contributes to the energy balance while measured supplemental heating/control power maintains the chosen state.

Single-pass beam–target remains the reference fixture, not an additional ignition claim. Track 3 is a physically differentiated subset of continuously driven operation, not a new energy source. Its supplemental power must remain visible in every total.

## Evidence status is independent
A track selection is a hypothesis. Record NOT_TESTED, SIMULATED, BENCHMARKED or EXPERIMENTALLY_SUPPORTED with source receipts, duration and criteria separately. An observation of sustained reactions while externally powered does not alone demonstrate ignition or quantify the self-heating fraction. A confirmed self-sustaining regime may still require electricity for pumps, magnets, controls and fuel handling. If supplemental heating becomes necessary, report assisted operation for that interval without rewriting the earlier drive-off evidence.

## Accounting and decision
Net cycle electricity = delivered electrical output minus startup, supplemental heating and all ancillary electrical inputs, with consistent stored-energy state and downtime boundary. Supplemental heating is wall electricity, not deposited plasma heating; driver/coupling efficiencies must be explicit.

Fusion products partition among self-heating, collection, other deposition and escaping losses. Recovering more alpha energy externally may reduce fuel heating, so collection and supplementary power cannot be optimized independently by keeping fusion yield artificially fixed.

Keep three distinct outcomes:
- sustained-state physics and stability over a declared interval;
- net electrical energy, with startup amortization and uncertainties;
- economic margin from actual saleable products, electricity/heat offtake and all costs including installed capital, replacements, recovery and downtime.

Economic breakeven can occur with negative net electricity if defensible product margins cover purchased power and other costs. Electrical breakeven alone does not establish profitability. Isotope revenue never changes the physical energy balance. Avoid applying both an electricity bill credit and an electricity sale credit to the same output.

## Implementation mapping and current limits
The existing v0.1 CONTINUOUSLY_DRIVEN arithmetic can represent track 3's wall-energy screen using explicit sustaining_wall_J, auxiliary_wall_J and alpha_self_heat_fraction. That is an accounting representation only; its fusion_J remains externally assumed. Do not claim a new dynamic burn solver or calibrated third-track result from this supplement.

The next physical implementation must solve time-dependent self-heating, supplemental deposition, electron/ion exchange, radiation, expansion/confinement, ash/fuel inventory and control response. Compare drive-off, assisted and externally driven cases with shared initial conditions and independently constrained parameters. Test stability, transient energy storage, restart costs and uncertainty before claiming a favorable operating point.

Required future outputs: track, evidence status, startup_J, supplemental_wall_J, ancillary_wall_J, deposited_external_heat_J, fusion_self_heat_J, fusion_energy_J, collected_energy_J, net_electric_J, duration, stored_energy_change_J, product_inventory_source, dated_price_snapshot, installed_capex_source and missing-data flags.

All current physical/calibration and market gaps remain open. No unverified isotope profitability or assumed sustained burn is inserted as a default.
