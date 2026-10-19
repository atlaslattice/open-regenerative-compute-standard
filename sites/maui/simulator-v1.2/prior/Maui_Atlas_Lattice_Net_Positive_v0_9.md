# Atlas Lattice Maui v0.9 — Net-Positive Integrated Resource Campus

**Date:** 2026-10-19  
**Status:** PROPOSED / NON-CANON; no construction, savings, environmental outcomes, or generation verified by this design  
**Scope:** Maui island; independent comparisons for Central Maui, West Maui, North Shore, and South Maui.  
**Mission:** Produce a resilient, circular network whose operation improves island outcomes across separately audited environmental, human, infrastructure, and economic ledgers.

## Executive architecture

Four complementary regional functions, not four identical mega-plants:

1. **Central Maui resource/energy campus:** existing wastewater interfaces; organics preprocessing; appropriately scaled anaerobic digestion; conditional HTL evaluation for wet biosolids and segregated feedstocks; nutrient recovery; materials sorting/upcycling; grid-interactive biosolar/batteries; modular inference data center; micro-haul coordination.
2. **West Maui/Lahaina:** water reuse, food-waste aggregation, emergency storage and microgrid, solar, targeted recycling, resilient localized service and habitat protection.
3. **North Shore agricultural campus:** farm and grocery organics, clean green waste, compost/soil amendments, agricultural water reuse, compatible solar and habitat restoration.
4. **South Maui/Kihei:** existing wastewater and reuse assets, food/hospitality waste collection, resilience integration. Independently account for local water and ecological conditions.

**Kanahā Pond Wildlife Sanctuary:** independent ecological restoration and hydrology program with ring-fenced capital and operating budgets, cultural and wildlife agency governance, pump redundancy and habitat/water-quality monitoring. No industrial discharge, fertilizer leachate, or untreated biosolids into the wetland. Siting must account for flooding, coastal exposure, noise, light, habitat buffers and truck traffic.

## Governing principle: non-fungible positive outcomes

A weighted positive 'ESG' score is never sufficient. Each domain has (a) legal and ecological non-regression gates, (b) a baseline, (c) measured net outcomes, (d) a net-benefit target, and (e) uncertainty ranges. A surplus in one ledger does **not** offset a violation in another. The design is a *target*, not a claim that all metrics can become positive in every operating hour.

### Boundary definitions

- **Campus operational:** imported electricity and fuels, exported electricity/usable fuels, water intake and discharge, local emissions, residues and direct employment.
- **Cradle-to-grave lifecycle:** embodied construction/solar/battery/compute impacts, transport, fuel upgrading, chemicals, parts replacements, full disposal, leakages, land impacts.
- **Island consequential:** truly displaced imports; changes in island disposal and water demand; grid dispatch/capacity; existing services; shifts in household bills and local wages. No assumed marginal displacement without actual buyers and tariffs.
- **Ecological catchment:** wetland hydrology, coastal/marine quality, habitat and freshwater withdrawals—not limited to plant property lines.
- **30-year cash-flow:** lifetime capex, replacement, financing, operations, end-of-life and decommissioning, compared with conservative status quo and realistic alternative investments.

## Mandatory domain scorecard

| Domain | Primary net-positive measure | Protective gate | Method / instrumentation |
|---|---|---|---|
| Electricity | Annual generation minus **all** campus electric use, imports, storage/line losses (MWh/yr) | No grid reliability degradation; no double count of gross generation | Revenue-grade meters; hourly grid imports/exports, dispatch and curtailment |
| Resilience energy | Critical service hours maintained, reduced unserved load (MWh/yr) | Backup power, black-start and fuel reserves tested | Islandable microgrid drills; hourly outage modeling |
| Fuel / transport | Verified imported diesel/gasoline/other fuel displacement (gallons or GGE/yr) | Approved specifications, emissions, sustainable feeds | Fuel chain of custody, buyers' metered use and avoided purchases |
| Heat | Purchased heating/cooling truly displaced (MWh-th/yr) | Industrial/biological process-temperature constraints met | Thermal meters; matched hourly profiles; heat pump parasitics |
| Climate | Lifecycle avoided GHG minus caused GHG (tCO2e/yr and 30-y cumulative) | No unsupported offsets; include methane and N2O leakage | Inventory using transparent factors, boundaries, and independent validation |
| Freshwater | Groundwater/surface withdrawals reduced; potable reliability and reserves improved (MGD; days) | Safe drinking water; aquifer and downstream ecology protected | Flow and quality meters, water-source attribution, rainfall and aquifer monitoring |
| Wastewater | Effluent reused or safely treated above baseline (MGD) | Compliance on pathogens, nutrients, PFAS, metals, microplastics | Influent/effluent labs, permitted monitoring, matched demand |
| Marine | Ocean pollutant loads avoided (kg/yr); salinity/temperature compliance | No harmful brine plume; marine ecological limits | Coastal baseline, continuous salinity and ecological stations |
| Organics | Diverted *net new* food/green/farm waste (wet/dry tons/yr) | Food rescue and soil-retention needs first | Generator manifests and mass balance; reject rates |
| Nutrients | Verified useful nitrogen/phosphorus/soil product substitution (t/yr) | Contaminants safe; no nutrient runoff increase | Lab assays, agronomic trials, buyer receipts |
| Materials | Virgin material imports displaced by qualified recovery (t/yr) | Product safety; no off-island contamination dumping | Input/output testing and downstream purchaser evidence |
| Biodiversity | Native habitat quality, wetland hydroperiod, species occupancy/breeding improvements | No measurable habitat loss or critical-species harm | Independent ecological surveys, control/reference sites |
| Soil | Soil organic matter, infiltration, erosion and crop yields vs control | No contaminants, salts or invasive species introduced | Multi-season farmside trials and accredited labs |
| Air / nuisance | Local PM, NOx, odor, noise and truck exposure vs baseline | Permit and health limits; sanctuary buffer | Monitoring stations, complaint logging, traffic census |
| Public health | Waterborne incidents, exposure pathways, sanitation reliability | All health protections met; no speculative medical claims | County/public-health measures with privacy controls |
| Equity & affordability | Household utility and food cost reduction ($/household/yr); local hire/pay | No net displacement or worsening costs for vulnerable residents | Bills, wage and housing impact studies, distributional audit |
| Jobs & development | Net durable local jobs, skills, procurement retained locally | Safe working conditions and fair wages | Payroll and contract ledgers, training outcomes |
| Financial | 30-year discounted net benefit, cost/t of treated waste, $/MG reused | No opaque subsidy dependence; contingency funded | Audited cash flows, sensitivities, capex and O&M |
| Governance | Public data availability, auditability and local participation | Consent/permits, Native Hawaiian consultation, independent oversight | Quarterly public dashboard, receipt-level evidence and appeal process |

**Important accounting notes:** Net electricity surplus is insufficient by itself if the facility increases peak imports or unreliability. Water produced is not 'water created'; assess displaced withdrawals and ecological impacts. A tonne of sludge or food waste cannot yield full biodigestion and HTL products at the same time. Biocrude is not finished diesel without upgrading. Methane leakage can erase climate benefits. Financial avoided costs, revenues, grants and economic multipliers must be kept separate.

## Flow-ledger structure

Each verified batch or volume has a distinct `source_id`, `facility_id`, `stream_id`, `period`, `input_mass_wet`, `dry_solids`, `water_volume`, `energy_import`, `product_output`, `residue_output`, `contaminant_profile`, `destination`, `quality_status`, `evidence_uri`, and `uncertainty`.

**Food distribution hierarchy:** prevented waste → edible rescue → allowable feed uses → digestion/HTL or compost after suitability screening → residual safe treatment. Grocery stores, restaurants, hotels and farmers maintain distinct baselines; historically landfilled waste cannot be counted again as an incremental farm/grocery stream.

**Wet biosolids comparison:** baseline digestion / co-digestion vs HTL vs hybrid with *mutually exclusive* input allocation. Consider moisture/dry solids, achievable oil yield, HTL heat/pressure and process water, upgrading cost, biogas electricity/heat, contaminant fate (PFAS/metals), qualified fuel market and final waste disposal.

**Energy coupling:** Distributed PV plus vegetated roofs/canopies/bioswales ('biosolar' = conventional photovoltaic electricity plus ecological co-design); batteries; optional dispatchable biogas CHP; metered purchased/recovered heat; industrial flexible demand. The modular inference data center is **a net electric load** with only conditional recoverable heat, not a power source. It must satisfy workload value, PUE, water use, heat off-take and hourly dispatch tests. Never count battery discharge as energy generation.

**Micro-haul:** Short routes and source-segregated containers with generator-specific pickup frequency; regional densification; long-haul only for materials whose treatment economies outweigh transport. Measure loaded/empty miles, labor, payload utilization, refrigeration and odor controls, kWh/mile, contamination, avoided hauls, and routing effects near schools and sanctuary.

## Public dashboard status codes

- **MEASURED** — instrument/source-backed outcome with reporting period and boundary.
- **MODELED** — scenario with assumptions, confidence intervals, sensitivity analysis.
- **PROPOSED** — design idea without verified viability.
- **QUARANTINED** — inconsistent, harmful, insufficiently evidenced, or infeasible claim.
- **RECEIPTS** — original measurements, contracts, manifests, assays and studies traceable to each claimed result.

Claims of net benefit always show `baseline`, `project`, `difference`, `scope`, `uncertainty`, and `verification_status`.

## Scenario set for engineering and finance

1. Baseline: current collection/disposal, grid generation, imported fuels, water extraction, wastewater reuse, restoration commitments.
2. A: existing-asset-only optimization—reuse water, improve sorting, micro-haul, targeted grid/solar upgrades.
3. B: distributed digestion/compost and native PV/battery microgrids without HTL/data center.
4. C: hybrid with centralized pilot-scale HTL, controlled sludge and suitable organics, specific offtake.
5. D: hybrid plus limited compute, waste-heat recovery and dynamic power control; compute included as an incremental load.
6. Stress cases: drought, wildfire, fuel-shipping interruption, grid outage, strong storms, tourism changes, low recycling commodity prices, technology underperformance, and 30-year replacement cycles.

Annual scenario outputs: incremental water delivered and potable demand reduced; waste diverted; mass of products placed; energy in/out and grid net; displaced fuel imports; emissions lifecycle; ecological response; truck miles; cash flows; project cost; resident savings; robustness under multi-week emergency.

## Provisional acceptance gates

- All environmental permits, sanitary standards and independent safeguards passed.
- Every domain separately reports 'net improved', 'neutral', 'worse', or 'unverified' against an independently approved baseline. Unknown is never labeled net positive.
- The capital portfolio must demonstrate **positive 30-year risk-adjusted net present value** or make a transparent case for noncommercial public benefits; the community does not subsidize opaque margins.
- Grid exports, carbon removal, potable displacement, waste diversions, nutrient sales, jobs and savings verified individually—no circular cross-subsidization or double counting.
- At every planned phase: disclose what is measurable today, what remains model-only, and what conditions trigger redesign or shutdown.

## Local alignment and initial baseline sources

1. Maui County Climate Action and Resiliency Plan: https://www.mauicounty.gov/3242/Ka-Papa-Hooll-Holu-ina-Climate-Action-Re
2. Maui County ordinance, Title 20, climate mitigation goals including circular economy, net-negative emissions, equity, indigenous and ecological knowledge, and quarterly public dashboard: https://library.municode.com/hi/county_of_maui/codes/code_of_ordinances?nodeId=TIT20ENPR_CH20.40AMOSAMICEMAINSA
3. County GHG inventory (2019): BASIC 1,512,220 tCO2e; BASIC+ 2,410,670 tCO2e, **countywide**, not Maui-island-only and not updated to 2026: https://storymaps.arcgis.com/stories/970ec836fd7f4881aeca768ca6d05fae
4. 2025 County State of the County: One Water for Lahaina, recycled R-1 water investments and restoration priorities: https://www.mauicounty.gov/2829/2025-State-of-the-County-Address
5. County FY2026 wastewater performance budget; includes actual/forecast regulatory compliance and reuse metrics: https://www.mauicounty.gov/DocumentCenter/View/152301/000---FY-2026-Program-Budget-Combined

**Data still needed before claiming net-positive performance:** site-specific 2024–2026 inflows and biosolids dry solids; generator-level grocery/restaurant/hotel/farm waste tonnages; current hauling and landfill invoices; grid half-hour/hourly loads and tariffs; thermal curves at generation stations; all water demands and existing rights; salt/brine and marine discharge assessments; fuel/offtake specifications; native habitat baseline and Kanahā management approval; construction and financing offers; workforce impacts and community preferences.

## Governance / final instruction

Do not optimize one headline scalar. Optimize the feasible **Pareto frontier** of measured gains subject to absolute environmental and social boundaries. The project's success is the verified incremental wellbeing of Maui and its ecosystems over 30 years, not the size of the infrastructure or its gross production figures.
