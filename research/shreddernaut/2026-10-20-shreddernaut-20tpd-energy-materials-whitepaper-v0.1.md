# Shreddernaut 20 t/day — Energy Reconciliation, Materials Recovery and Pilot White Paper v0.1
**Date:** 2026-10-20 | **Status:** PROPOSED / NON-CANON / NOT DEPLOYED / NOT VALIDATED | **Owners:** Atlas Lattice research discussion / Tidal Lantern handoff

## Executive findings
This review repairs the original Shreddernaut energy assumption by explicitly separating **20 metric tonnes/day incoming presorted feed** from the tonnes actually washed, dried or pelletized. It does **not** assume that every incoming tonne must traverse all processing stages. Prior historical Shreddernaut concepts claimed 15–25 t/day or 50–150 t/day at approximately 1,800 kWh/day (in some drafts) and USD 1.2–2.8m capex. The independent archive assessments found the full-chain energy/throughput claims unsubstantiated, financial estimates unverified, and complete 40-foot-container industrial scope unsupported.

**Decision for research:** Favor a grid-connected, modular, selective-processing, 20-t/day **presort → hazard isolation → screening/sensor sorting → selective shredding → concentrate/flake offtake** pilot. Treat wet washing, pelletizing, advanced refining and all high-temperature recovery as external/offsite or separately powered modules. A roof-only photovoltaic supply is not a credible sole source of energy. Presort **before landfilling** wherever possible; source-segregated recovery is often preferable to mining old mixed waste. Old landfills and WTE ashfills require distinct models.

## 1. Source archaeology and prior errors
- Original draft: [Shreddernaut v1.0](https://github.com/atlaslattice/atlas-lattice-foundation/blob/main/infrastructure/SHREDDERNAUT.md): 40-foot high-cube; claims 50–150 tons/day, 95% uptime, 85% product yield, USD 1.2–2.8m capex, unusually short payback and 98% classification. These claims are proposed, NOT independently measured.
- [Shreddernaut model validation](https://github.com/atlaslattice/manus-artifacts/blob/main/public_candidate_bundle_0001/china_research/notion_archive/089-3f20c1de73d981c6aa6cdd254fb449da.md): reports competing 15–25 and 50–150 t/day versions; 1,800 kWh/day insufficient for integrated throughput; inconsistent energy/power calculations, unit economics, throughput/day-versus-year and missing meter/commissioning data. Appendix has source table and method.
- [Six-agent assessment](https://github.com/atlaslattice/manus-artifacts/blob/main/public_candidate_bundle_0001/china_research/notion_archive/050-3f20c1de73d9814f95e9c070bb8dc3ec.md): rejects claims of validated deployment, product certificates and full-chain profitability.
- Important scope correction: the independent review's plant energy comparators normalize to different process stages and output mass bases; therefore numbers below are *bounds/scenarios*, not a validated process simulation or direct measured machine load.
- All past national fleet projections, 4–6 month payback, special construction “Trashium” outputs, 95% all-resin purity, and full-chain 100 t/day energy assumptions must be marked **UNVERIFIED / DO NOT PROPAGATE**.

## 2. Twenty metric tonnes/day energy screening
Assume 20,000 kg incoming material every 24 h. This is **20 metric tonnes input**, not guaranteed saleable output. Use kWh per metric tonne as a provisional normalisation while noting that published datasets use differing feed/input-product denominators.

| Comparator / boundary | Reference specific electric intensity | 20-t/day screen | 24-hour average | Classification |
|---|---:|---:|---:|---|
| Favorable rigid-polymer pre-extrusion engineering model | 256.9 kWh/t | 5,138 kWh/day | 214 kW | MODELED comparator |
| Weighted HDPE bale→flake and flake→pellet components | 193.6 + 332.9 = 526.5 kWh/t normalized | 10,530 kWh/day | 439 kW | REPORTED stage figures, illustrative total |
| Operating plant pre-pellet electricity | ~715.6 kWh/t | ~14,312 kWh/day | ~596 kW | REPORTED inventory |
| Operating plant complete pellet chain | 1,073.4 kWh/t | 21,468 kWh/day | ~895 kW | REPORTED inventory |

**Existing proposed supply:** 1,800 kWh/day = 75 kW daily average. **Illustrative electric deficit**: ~3.34 / 8.73 / 12.51 / 19.67 MWh/day against the respective 20-t/day benchmarks. All entries are **before reliable plant-specific downtime, auxiliary loads, thermal vs electrical allocation, conversion yields and startup transients**. They are therefore *not* validated utility requirements. Do not use plant input and product-output denominators interchangeably in a final design.

**Critical distinction:** mechanical pre-sorting of mixed materials, recovering metals/glass and shipping concentrates is *not* equivalent in energy or output to full plastic recycling. The 256.9–1,073.4 kWh/t cases do not directly predict a metals-first dry sorting line. Until vendor metering/representative pilot exists, energy for the proposed reduced-scope line is **UNKNOWN**.

### Selective-processing mass balance (illustrative only)
Define:
- Q = 20 t/day incoming material.
- p = fraction sent to energy-intensive wet polymer line; e.g., **p=0.25**, a *scenario*, not expected site composition.
- q = fraction of that line converted to saleable product (must be measured).
- E = E_intake_and_dry_sort + (Q*p*e_wet_line) + E_aux + E_treatment; never subtract stages that are necessary for hygiene/product specification.
- Example 5 t/day chosen for wet treatment at illustrative 526.5 kWh/t => ~2.63 MWh/day **for that selected processing chain alone**; dry sort, hazards, conveying, dewatering, dust extraction and rejects still need a separate metered budget.
- Residual 15 t/day is NOT automatically a recovered commodity; reconcile source-separated ferrous, nonferrous, glass, aggregates, clean plastics, organics, rejects and quarantined hazardous fractions so input mass equals all outputs (including moisture changes).
- Scenario bounds: 0%, 25%, 50%, 100% of incoming material subjected to intensive processing; separately calculate local service cost and product grades.

## 3. How to close the gap, in priority order
1. **Avoid processing entirely where possible:** source segregation and pre-landfill presort; take reusable electronics, cables, motors and repairable parts out intact; recover clean steel/aluminum/copper with magnetic/eddy-current/sensor sorting before shredding; keep banned/hazardous material out.
2. **Mechanical front-end with bypass lanes:** screen out soil-like fines/inerts, separate ferrous and non-ferrous materials, use optical/spectral sorting selectively, shred only material requiring size reduction, and avoid commingling clean feedstock with waste.
3. **Modular stage gates:** initial output graded scrap/concentrates/flakes; offsite partner pelletizes, smelts, refines, recovers batteries/e-waste. Add wash/dry only where offtake price premiums beat energy/water/treatment and reject costs.
4. **Recover existing site energy:** grid or contracted industrial power first; use landfill gas/biogas or recovered heat **only** if a demonstrably available source exists and environmental permits/engineered controls are satisfied; no imaginary thermal credits. Heat can offset drying thermal duty, not one-for-one electrical motor energy.
5. **Solar canopies and distributed generation:** PV useful for daytime energy offset and shade; grid connection / microgrid remains required. Battery sized for short ride-through, controlled shutdown and fire-safe isolation, not automatically 24-hour off-grid throughput. Any solar-only claim needs meteorological/site resource, acreage, inverter/downtime, storage, load shapes and reliability accounting.
6. **Equipment efficiencies:** variable-frequency drives, high-efficiency motors, no-load shutoff, feed-rate control, minimized pressure drop, mechanical dewatering before thermal drying, recoverable low-grade heat, preventive maintenance, demand scheduling.
7. **If site economics fail:** cut modules, restrict feedstock to high-value sorted streams, reduce duty cycle, or send bulk fractions to existing regional MRFs rather than pretending efficiency gains alone solve the discrepancy.

**PV sanity check**: illustrative yield 4 kWh/kWp/day delivered gives ~1,285 kWp to match 5,138 kWh/day, ~2,633 kWp for 10,530, ~3,578 kWp for 14,312, ~5,367 kWp for 21,468. These are simple annual-average equivalent arithmetic, **not a location-calibrated solar engineering design**, and exclude storage for nighttime, losses in a battery cycle and peak-load considerations. 40-foot container roof cannot host utility-scale array. For a solar offset fraction f, nameplate ~ f*E_daily/4. Source for site-specific PV later: [NREL PVWatts](https://pvwatts.nrel.gov/).

## 4. ecomaine benchmark: what it proves and does not
A peer-reviewed case study of the **ecomaine waste-to-energy ashfill** found 34,352 metric tonnes of ferrous and nonferrous metals recovered and shipped to recyclers between December 2011 and March 2015, with conservative estimated metal value USD 7.42m, an additional 10,194 m³ ashfill airspace and associated USD 267k value. Peer-reviewed case abstract: [Waste Management DOI 10.1016/j.wasman.2015.06.034](https://doi.org/10.1016/j.wasman.2015.06.034); [PubMed](https://pubmed.ncbi.nlm.nih.gov/26152366/). This was an **ashfill metals project**, not direct evidence that excavated mixed municipal waste produces clean plastic products at attractive cost, or that metals yields generalize to all landfills.
**Transferable engineering:** metal-rich targeting, ferrous/non-ferrous separation, sieving by size, verified material shipments, site-airspace value, contamination monitoring and detailed accounting.
**Non-transferable:** recovery rate for unsorted old MSW, same profitability, same material distribution, energy intensity or permitted downstream uses.

## 5. All major prospective landfill outputs / usability gates
Inventory must be assayed by age, cell, layer, weathering and waste type; theoretical presence != saleable recovered commodity.
- **Bulk metals:** ferrous iron/steel; aluminum; copper; brass (Cu/Zn); stainless (Fe/Cr/Ni); zinc; tin, lead; nickel; manganese; precious-metal-bearing items. Separate by existing scrap grades; check lead/contaminant limits.
- **Discarded batteries and electronics (do not bulk-shred):** lithium, cobalt, nickel, manganese, iron/phosphate, copper/aluminum foils; gold, silver, palladium in selected circuit boards; rare-earth magnets (Nd/Pr/Dy/Tb) in select motors and devices. Product-specific variability is enormous; approved e-waste/battery processors only.
- **Glass / mineral / construction:** clear/mixed glass, concrete, brick, asphalt, ceramics, gypsum, excavated coarse aggregate, slags; need leaching, asbestos, contamination and product-grade tests. Soil-like fines cannot be declared clean topsoil or cement input without assays.
- **Plastics:** PET, HDPE, LDPE, PP, PS/EPS, select engineered resins; identify polymer, additives, halogens, age/contamination and quality. PVC, multilayer films, mixed old plastics often need dedicated handling rather than an automatic conversion-to-building-block assumption.
- **Biological/combustibles:** paper/cardboard, wood, organics, textiles and residues; may be degraded or contaminated after burial; options depend on compost, digestion, specialty manufacturing or regulated energy recovery; no universal nutrient recovery.
- **Hazards and exclusions:** pressurized containers, lithium batteries, asbestos, medical/sharps, mercury lamps, pesticides, solvents, PFAS-bearing material, contaminated sludge and unknown drums. Quarantine and licensed specialists; no routine shredding, thermal processing or agricultural reuse without approval.

OSHA notes lithium-ion batteries may undergo thermal runaway and should be separated into designated recycling routes, not mixed in municipal trash/recycling: [OSHA hazards](https://www.osha.gov/lithium-ion-battery-safety/hazards) / [controls](https://www.osha.gov/lithium-ion-battery-safety/control).

## 6. Economics and national resilience
Primary functional unit: **dollars and kWh per incoming metric tonne** and **dollars/kWh/tonne per specification-grade product**. Three ledgers: (a) operator cash flow (gate fees when contracted, product offtake, power/labor/maintenance/reject handling, permits, transport, capex), (b) system-wide avoided disposal/infrastructure benefit **without double-counting** gate fees, and (c) domestic import-displacement and strategic-reserve value by actual product grade. No inference that earlier illustrative $10/t processing and $55/t product value are measured averages for landfill mining. Capital recovery and uptime dominate return.
At 20 t/day and 300 operating days, gross accepted feed = 6,000 t/year. Input ≠ saleable commodities; yield, grade, cost and buyer price await assays, pilots and signed contracts. Keep 51% worker-equity concept as a governance proposal, not a revenue/profit fact.

## 7. Pilot design, testing and validation gates
**Phase 0:** select feedstock, exclude legacy remediation hazards until permitted. Characterize 50–100 representative batches including wet/dry variation; quantify fractions, assay metals, polymers, batteries, fines, contaminant/leachate and existing site disposal path. This sample size is a provisional study proposal, not a statistical assurance.
**Phase 1:** modular manual/automated presort and commodity-grade separation. Track counts/weights with calibrated scales, product grades and reject destination. Measure kWh per distinct line including idle/peak, compressed air, dust handling and auxiliaries.
**Phase 2:** integrate selective shredder; test whether 20 t/day can be handled without routing all 20 t/day through wet wash/thermal dry. Independent fire/electrical safety review.
**Phase 3:** compare local processing vs offsite processors; commission PV and backup only with documented generation and net load; perform economics with genuine vendor quotes.
**Phase 4:** independently verify 30/60/90-day sustained operations and product offtake; then consider duplicating.

**Stop/go:** compliant safety system, verified mass balance (including moisture), metered power and peak demand, qualified commodities, signed offtake, lawful residual disposal, audited capex/opex, ecological baselines and financial downside case. No broad claim about "profitable landfill mining" without these.

## 8. Open issues / corrections for the next Tidal Lantern
1. Original **1,800 kWh/day** and sometimes 80–120 kW cited inconsistently; retire as full-process design supply.
2. Do not equate 20 t/day **dry-sorting input** with 20 t/day **saleable pellets**.
3. Need true motor/PFD/P&ID line list, vendor capacity/energy quotes, thermal heat balances, water and wastewater balance, dust/fire code, local permit constraints.
4. Need site-specific incoming fraction sample and destination contracts before estimating metal yield, gold/lithium recovered, or product prices.
5. Do not transplant ecomaine ashfill grade/ROI to aged mixed landfill waste.
6. No climate/carbon credit until site-specific baseline/methane lifecycle evaluation.
7. Comparison needs grade-adjusted import substitution, transport cost, reserves, domestic refining capacity, and separate economic value to affected parties.
8. Compare grid-tied solar roof only, expanded canopy PV, biogas/CHP if available and full offsite processing; exclude conjectural zero-energy tech.
9. No unverified deployment, simulations, government adoption, AI self-ratification or canonical status.
10. Next executable model: process-stage ledger by feedstock and actual meters, PV/dispatch sensitivities, CAPEX/OPEX, product mass balance and Monte Carlo scenario validation.

## Reference index
- [Original Shreddernaut concept](https://github.com/atlaslattice/atlas-lattice-foundation/blob/main/infrastructure/SHREDDERNAUT.md)
- [2026 detailed independent model-validation archive](https://github.com/atlaslattice/manus-artifacts/blob/main/public_candidate_bundle_0001/china_research/notion_archive/089-3f20c1de73d981c6aa6cdd254fb449da.md)
- [Six-agent comparison and engineering summary](https://github.com/atlaslattice/manus-artifacts/blob/main/public_candidate_bundle_0001/china_research/notion_archive/050-3f20c1de73d9814f95e9c070bb8dc3ec.md)
- [Detailed enhanced landfill mining review](https://github.com/atlaslattice/manus-artifacts/blob/main/public_candidate_bundle_0001/china_research/notion_archive/081-3f20c1de73d981febc74f28ba486676d.md)
- [ecomaine peer-reviewed research](https://pubmed.ncbi.nlm.nih.gov/26152366/)
- [OSHA lithium battery safety](https://www.osha.gov/lithium-ion-battery-safety/hazards)
- [NREL PVWatts model](https://pvwatts.nrel.gov/)
- [ORCS resurrection checkpoint](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/main/docs/handoffs/SOLGPT_TIDAL_LANTERN_RESURRECTION_2026-10-14.md)

**Final evidence classification:** historic source design PROPOSED; peer-reviewed ecomaine operation REPORTED; process energy comparators REPORTED/MODELED; 20 t/day modified system, PV configuration and economics PROPOSED/UNKNOWN; deployable prototype NOT VERIFIED.
