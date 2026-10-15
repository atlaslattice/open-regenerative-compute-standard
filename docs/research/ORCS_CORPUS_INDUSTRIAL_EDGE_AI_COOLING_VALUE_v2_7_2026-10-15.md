# ORCS v2.7 — Corpus Christi industrial edge AI node and integrated cooling value

**2026-10-15 | PROPOSED / NON-CANON / ZERO REALIZED SAVINGS / APPEND-ONLY**

## Central proposition
On-site, modest-scale AI inference/optimization is distinct from hyperscale model training. Its value can accrue from verified energy/load optimization of LNG liquefaction and water/desal process systems, predictive maintenance, anomaly detection, brine chemistry process controls, alarm triage, faster local sensor fusion, independent operations during network outages, and lower network/central cloud data transfer. A local node has its own compute power and cooling requirements; data transfer cost reductions are not automatically equal to net power savings. Human-approved control boundaries and process safety interlocks are not delegated to AI.

### Corpus Christi special thermodynamic guardrail
Cheniere Corpus Christi **exports** LNG. Refrigeration is purchased/created to **liquefy** the feed gas; siphoning cold from active refrigerant systems might add electrical compressor load and reduce LNG throughput. This is not directly comparable to Dongjiakou LNG **import/regas** terminals with otherwise-discarded cold. If a measured, contractible **excess cooling capacity** or warmer industrial cooling service exists, adjacent DC cooling may become attractive. Typical process reject heat can be useful for adsorption chilling/heat-driven chillers, but capex, thermal coefficient of performance, environmental limits and load matching must be included. Absorption cooling from low-grade heat does not always beat electric chiller COP and can need cooling water.

### Onboard edge compute workload eligibility
- ✅ Non-safety-critical forecasts: compressor efficiency curves and maintenance, antifouling, brine recovery setpoints recommended to authorized operators, energy pricing, sensor diagnostics, outfall monitoring, water quality, inventory/freight scheduling.
- ✅ Local streaming anomaly detection, log aggregation, camera inference when authorized and privacy assessed, intermittent backhaul and digest summaries.
- ✅ Optimization *recommendations* with operator approval, audit trails, rollback, hard engineering limits and redundant independent safety systems.
- ❌ No direct AI authority over critical plant shutdowns, chemical dosing, hazardous process transitions or legal export authorization without validated safety/control governance.
- ❌ No assumption that a local inference rack is equivalent to zero-cost computing or that WAN bytes reduce grid bills by an identical energy amount.

## Three additive value ledgers (no double count)
**A. Cooling:** Existing baseline chiller consumption kWh/yr minus proposed cooling plant + pumps + distribution + refrigerant opportunity cost + thermal-storage overhead, with availability/redundancy constraints. An export terminal cooling diversion must include added LNG liquefaction compressor load and lost product opportunity cost.

**B. Process optimization:** Electricity/fuel kWh or MMBtu saved from an independently metered operational A/B design, valued at temporal energy tariff; incremental product/water/mineral yield qualified and only monetized with real offtake; reduced maintenance/downtime separately from energy and production to avoid value double-counting.

**C. Data & inference:** Remote cloud inference/API/storage spend displaced, net of software licensing, local server electricity, cooling overhead, staffing, cybersecurity, amortization and networking; bandwidth savings based on metered outbound bytes * actual cost, not arbitrary $/GB. Latency/reliability benefits are non-cash until measured.

**Gross-benefit formula** =
eligible process savings + verified incremental margin + actual avoided remote cloud/network bills + verified cooling kWh reduction×energy tariff + verified net maintenance benefit.
**Net incremental annual benefit** =
gross benefit − rack compute/cooling energy − operator/cyber costs − depreciation/annualized capex − additional pumps/storage and LNG compressor penalties − attributable revenue cannibalization/counterfactual losses.
Do not count the same energy savings under A and B. Do not include a hypothetical price times a mineral content ceiling as realized revenue.

## Calibration sensitivity — all numbers illustrative, not site facts
Example **small 100-kW IT edge node** at 80% utilization: 100 kW × 8760 h × .8 = 700,800 kWh IT/year. At conventional PUE 1.4: 981,120 kWh facility electricity; at engineered PUE 1.2: 840,960 kWh facility electricity; difference **140,160 kWh/year**, 14.3% reduction of baseline facility consumption. At assumed $0.08–$0.15/kWh: **$11,213–$21,024 annual facility energy avoided** due solely to PUE improvement. Cooling-only delta may be a subset of facility overhead. That alone will rarely repay bespoke cryogenic plant/cross-property piping capex. A separate measured 1% process energy improvement at a genuine industrial plant *could* be far larger, but no plant baseline MWh/yr has been supplied; do NOT price hypothetical process savings without actual data.

The scenario for localizing data: if raw sensor payloads are filtered such that 90% fewer bytes leave site, the network charge saving is 0 if the tariff has unlimited data and no metered transfer fee; otherwise calculate measured GB difference × contracted unit rate. Local AI's impact on physical transmission equipment's fixed electrical load may be small, and cloud providers may aggregate work at more efficient facilities. Compare net workloads and alternatives honestly.

## Design candidate — test rather than assume
Proof-of-value A: One secure industrial edge rack with plant historian read-only replica, streaming quality/audit, non-safety-critical optimization advisory and a published measurement baseline.
Proof-of-value B: Simulate cooling with site-specific hour-by-hour duty, cold exergy and process opportunity costs for Cheniere/Harbor Island. Compare air cooling, evaporative/chilled water, absorption-from-waste-heat and any physically verified spare cryogenic streams against optimized conventional design.
Proof-of-value C: Simulate local and cloud inference using same tasks/models and workload SLAs, including model update sync, physical bytes and full node energy.
Gate any operator adoption behind permission, security/OT segmentation, IEC 62443 practices, third-party cyber review, performance metering and revertible, human-approved controls.

## Project-specific verdict
At Corpus Christi, cost reduction from **industrial optimization and avoided downtime is a better a priori hypothesis** than recovering 'free LNG cold' from export liquefaction. Simple colocated compute + optimized conventional cooling should be a baseline before bespoke thermal hardware. No throughput, savings, partner agreement, or access to Cheniere plant data is established.

Sources/references preserved in docs/research/ORCS_CORPUS_CHRISTI_LNG_DATA_CENTER_COLD_INTEGRATION_SCREEN_v2_6_2026-10-15.md, and existing Dongjiakou LNG cascade mirror.
