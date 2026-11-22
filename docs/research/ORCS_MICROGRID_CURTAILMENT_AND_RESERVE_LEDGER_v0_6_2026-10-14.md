# ORCS v0.6 — Observed Curtailment to Resilience Battery Ledger

**2026-10-14 · NEW VERSION / EMPIRICAL-DATA-ONLY / PROPOSED / NON-OPERATIONAL / ZERO REALIZED CREDIT**

## Hypothesis
Prefer charging verified available, otherwise-curtailed electricity into consented, grid-connected or islandable microgrid storage. Retain an emergency-accessible portion for essential loads; consider releasing the remainder into domestic demand where voltage, power/energy limits, grid constraints, tariffs, permission and safety allow. Compare storage against direct delivery, demand response, and non-battery options. This is a **planning hypothesis**, not an instruction to automatically divert all excess power.

## Distinctions that must never be collapsed
1. **Generation minus demand ≠ curtailment or free surplus**. Balancing authority output includes interchange, losses, schedule obligations and reliability requirements; EIA-930 hourly public datasets typically lag operations and cannot establish control-grade spare deliverable power. Historical public data can calibrate.
2. **Curtailment** needs explicit telemetry (MWh withheld from otherwise feasible renewable production), not inferred from wholesale price or a generation-demand differential. Charging may also occur from noncurtailed low-price energy, but must be labeled separately.
3. **Storage inventory** is MWh state of charge, while charge and discharge capabilities are MW; conversion efficiency, usable depth, degradation, power limits, interconnection, ramp rates, fire safety and reserve commitments must be considered.
4. **Domestic distribution** cannot imply unrestricted national transfer. Transmission congestion, distribution voltage/thermal limits, grid codes and human owner/ISO approvals govern achievable dispatch.
5. **Emergency reserve** must be geographically reachable, islandable when needed and adequate for *critical services*; an owner's battery without islanding/black-start capability is not a guaranteed emergency backup.

## Model contract (new additive module)
Input row keys: observed timestamp and region/BA, `observed_curtailed_mwh` with traceable source if known, `available_storage_headroom_mwh`, authorized charging power MW and window hours, charging efficiency, state of charge, output efficiency, minimum protected reserve MWh, discharge limit MW, domestic reachable load MWh, authorized transfer margin MWh, consent/permit flag. Unknown values remain `null` and block any quantified allocation. Simulation is **single-period screening**, not actual utility dispatch.

Charge ceiling = min(verified curtailable MWh, available storage headroom / charge efficiency, allowed charge MW × available hours); stored increment = charged input × charge efficiency. Only excess above locally protected accessible emergency inventory becomes eligible for domestic delivery, capped by output efficiency and physical grid constraints. No charge/discharge automation, purchase instruction or reserve-release authority. Time-resolved state updates and degradation require future v0.7 development.

## Records needed
- EIA-930 hourly demand/generation/interchange (historical BA context, not real-time spare capacity): https://www.eia.gov/electricity/gridmonitor/
- ISO/RTO actual curtailment reports and interval dispatch data, e.g., ERCOT and CAISO official reports after specific datasets/licensing are confirmed.
- EIA-860/923 storage and generation plant inventory / state electric power statistics: https://www.eia.gov/electricity/data/
- DOE microgrid integration: https://www.energy.gov/oe/renewable-energy-integration
- NREL grid-scale batteries FAQ: https://www.nrel.gov/docs/fy19osti/74426.pdf

## Guardrails
No synthetic utility/hazard records in empirical results. Mathematical unit tests may use minimal numerical fixtures, clearly labeled **tests, not observations**. Existing petroleum import diversion remains primary ORCS economic model; electricity is a complementary resilience ledger. No older papers, GPTBrain or fiction overwritten.

Status: Concept ledger and code test additions on isolated PR branch; no independently validated daily national curtailment totals and no verified dispatch recommendations yet.
