# United States Industrial and Agricultural Import Supply Chain Atlas — v0.1
**Date:** 2026-10-12 | **Status:** SOURCE-ANCHORED TAXONOMY / PARTIAL QUANTIFICATION / NO REALIZED IMPORT SUBSTITUTION | **New version; prior studies preserved.**

## Purpose
Trace the United States' foreign industrial and agricultural commodity supply chains, from original raw-material producer through refiners, international transit, US ports, interstate delivery, consuming industries, end-of-life recovery, and domestic substitute. Goal is resilience and circular economic opportunity, not indiscriminate elimination of useful foreign trade.

**Important limitation:** This is a comprehensive **coverage schema and initial sector register**, not a fully populated HS10, company or facility-level census of the entire import supply chain. A complete quantitative ledger requires millions of product/country/port records and the subsequent domestic industrial purchase flows that customs data do not publish directly.

## Verified scale and source controls
- US BEA *Annual 2025 International Trade in Goods and Services* reports **2025 US goods imports $3,438.4 billion on a balance-of-payments basis**; this is not the customs-statistics value and includes many consumer goods beyond industrial/agricultural inputs. https://bea.gov/news/2026/us-international-trade-goods-and-services-december-and-annual-2025
- USDA ERS reports **$212 billion US agricultural imports in 2025**, of which **$136 billion** were processed products; high-value products dominate the value. This is USDA agricultural definition and **is not an additive separate category to total goods imports**. https://www.ers.usda.gov/data-products/ag-and-food-statistics-charting-the-essentials/agricultural-trade
- Complete **2025** USITC DataWeb imports available; as of 2026-10-12 query system shows through **August 2026** with 2023–25 revisions. Obtain 2025 import-for-consumption values and quantities by HTS10, origin country and district. https://dataweb.usitc.gov/ ; methodology https://www.usitc.gov/applications/dataweb/about ; underlying Census merchandise imports https://www.census.gov/foreign-trade/data/IMDB.html
- USGS *Mineral Commodity Summaries 2026* provides 2025 net import-reliance and source countries for critical/mineral inputs; distinguish net reliance from gross imported value and from upstream embedded imports. https://pubs.usgs.gov/publication/mcs2026
- USDA ERS food imports data updated April 2026 includes time-series annual country, food group and volume. https://ers.usda.gov/data-products/us-food-imports
- USDA Agricultural Transportation fertilizer imports/exports nutrient-equivalent database revised July 2026 can be filtered by N/P2O5/K2O and country. https://agtransport.usda.gov/Fertilizer/Fertilizer-Imports-and-Exports-Nutrient/tpd5-muue
- USGS 2026 *Indirect mineral import reliance and provenance* warns that shipment origin or intermediary can differ from producer origin; preserve both and original production provenance. https://www.usgs.gov/publications/indirect-mineral-import-reliance-and-provenance
- EIA April 2026 report notes **6.2 million barrels/day US crude imports in 2025**, 8% originating from Middle East Gulf; crude grade/refinery fit and regional pipeline topology matter, rather than assuming all imported crude is replaceable by US output. https://www.eia.gov/Todayinenergy/detail.php?id=67407

## System boundaries — avoid double counting
1. **Goods imports ≠ imports of domestic industries.** Split imported intermediate/raw goods, imported capital equipment, imported final consumer goods. USDA agricultural categories already lie inside goods trade.
2. US production can require imported machinery or refined precursors; characterize **direct** and **embodied** exposure separately. Material origin, last-exporting country, refining nation, port, destination and corporate supplier are different fields.
3. Gross physical imports, net reliance, and value-at-port are different metrics. Net import reliance must account for domestic production, exports, inventory adjustment and recycling in comparable units.
4. Regional self-sufficiency does not imply zero imports: optimize reliability, lifecycle economics, ecological constraints, diversified sourcing and relations with allies/trading partners.
5. Circular outputs are credited only once. Waste already reused, crop residues needed for soil, food suitable for rescue, and manure already land-applied are not available as new recovered imports.

## Coverage taxonomy: industrial and agricultural supply chains

| Chain / linked HTS chapters | Core upstream imported inputs | Typical source/source hubs (NON-EXHAUSTIVE, validate commodity specific) | US transformations/end users | Candidate domestic/circular routes | Evidence needed for quantitative impact |
|---|---|---|---|---|---|
| Agricultural fertilizer, 31 | Potash salts/KCl, N fertilizers, phosphates, blends | Canada potash; other suppliers vary | Blending, fertilizer distribution, crops | N/P nutrient recovery, domestic N/P factories, targeted K recycling, fertilizer precision | HTS10 quantity, N/P2O5/K2O assays, domestic supply and crop application |
| Farm input chemicals, 28-30/38 | Agrochemical intermediates, herbicides, fungicides, specialty chemical feedstocks | Country/product specific | Active ingredient synthesis, formulation, farming | Domestic chemical loops, precision pest control and proven biological alternatives | Product vs active ingredient, registrations and residual constraints |
| Seeds/feed/animal input, 10-12/23 | Oilseeds, protein meals, feed additives, seeds | Canada/Mexico/South America and others | Animal feed, seed, crop/food production | Low-waste feed, domestic protein fermentation where tested | Feed nutrients/quality/animal health and land use |
| Food, produce and processing, 01-24 | Fruits, vegetables, cocoa, coffee, sugar, fats/oils, meat, seafood, processed foods | Mexico, Canada, EU, South America, tropics | Mills/food processors, retailers, households | Food rescue, local food/CEAs for suitable crops, residual AD/fiber/nutrient recovery | Edible vs unavoidable waste, seasonal marginal import value |
| Forestry, timber, pulp, paper, packaging, 44/47/48 | Wood, wood products, pulp, paper | Canada and commodity specific | Building, pulp/paper, packaging | Recycled fiber, regenerative forestry, reuse | Recycled fractions, product grade, energy/water requirements |
| Textile fibers/chemicals and apparel, 50-63 | Natural/synthetic fibers, yarn, fabric, apparel | Asia/Americas and others | Textile finishing, construction, consumers | Fiber-to-fiber recycling, repair, renewable fibers | Fiber composition, contamination, manufacturing capacity |
| Crude oil, gas and fuels, 27 | Refinery-grade crude oil, LPG, refined products | Canada/Latin America/Middle East by grade | Refineries, plastics, transport | Efficiency, biogas/RNG, electrical substitutions and petrochemical material recycling | Refiner grade and actual region-specific energy flows |
| Industrial chemical precursors, 28-29 | Ammonia derivatives, sulfuric intermediates, methanol, caustic products, acids | Commodity-specific | Refining, resins, fertilizers, manufacturing | Sulfur recovery, waste-heat integration, recovery of spent industrial chemicals | Purity/capacity, process LCA and chemical permits |
| Polymers/plastics/rubber, 39-40 | Resin, monomers, additives, rubber | Commodity-specific | Packaging, auto, construction | Mechanical recycling, verified chemical recovery where net-positive, redesign | Functional equivalence, lifecycle losses |
| Stone/cement/glass/ceramics, 25/68-70 | Industrial minerals, specialty glass, cement/clinker | Canada/Mexico/other countries | Construction, electronics, refractory materials | Industrial byproduct gypsum/slag/ash, glass cullet and clinker substitutes | Material standards, leachate safety and transportation |
| Ferrous metallurgy, 26/72-73 | Iron units, ferroalloys, special steels, finished steel articles | Varies by grade and alloy | Mills, foundries, vehicles, infrastructure | High-grade scrap, electric arc mills, ferroalloy circularity | Impurity tolerance/metal losses, end-use and domestic process capacity |
| Aluminum/bauxite/alumina, 26/76 | Bauxite, alumina, primary aluminum, scrap and wrought products | Canada primary aluminum; other ore/refiner origins differ | Smelters, rolling mills, transport | Aluminum scrap remelting, manufacturing yield and domestic refining | Energy demand, alloys and embodied input source |
| Copper and conductive metals, 74/75/79-81 | Copper products, zinc, nickel, tin, cobalt/lithium intermediates | Canada, Chile and commodity-specific | Grid, batteries, wiring, industrial equipment | E-waste, transformer/scrap and battery recycling | Metal by grade, battery chemistry and process recovery efficiency |
| Strategic/critical minerals, multiple 25-28/71/81 | Rare earths/magnets, graphite, gallium, germanium, antimony, tungsten, niobium, fluorspar | Concentrated in different producers/refiners, potential Chinese refining exposure | EV/power electronics, catalysts, defense/aerospace, magnets, metallurgy | Scrap magnets, E-waste, slag/tailings extraction, US processing and diversified imports | Mineral-form inventory, producer vs reexport intermediary; USGS net reliance |
| Machinery, 84 | Machine tools, pumps, industrial robots, engines, HVAC | Globally diversified | Manufacturing/industrial plants/farms | Domestic precision machining, repair, remanufacturing | BOM and domestic vendor capability |
| Electrical and electronics, 85 | Chips, integrated circuits, batteries, generators, motors, panels | East Asia and global | Industrial controls, AI compute, grid, appliances | Chip packaging, battery refining/reuse, repair, rare-metal reclaim | Multi-tier BOM, fab location, critical tooling and wafers |
| Transport and logistics equipment, 86-89 | Auto and aviation parts, ship components, rolling stock | Mexico/Canada/EU/Asia and others | Vehicle, logistics, agriculture | Remanufacture, localized parts manufacture | OEM part compatibility and qualifying supplier list |
| Medical and laboratory industrial supplies, 30/90 | Pharma precursors, biotech inputs, imaging/lab devices | Multiple | Health and bioprocessing | Domestic sterile production, process recovery and reliable diversified sourcing | Quality, supply-risk and regulatory compliance |

This coverage is a **working ontology**, not a claim that each row represents positive net dependence. Some US sectors export more than they import or import grades that domestic producers do not make.

## Multistage trade graph
`deposit / farm / well → extraction/harvest → separation/beneficiation → refining/chemical synthesis → component manufacturing → original-producer export or international transfer → US customs port / district → warehouses / rail / barge / pipeline / truck → US plant / farm / retail → material waste / byproducts → recovery loop / export / disposal`.
Record *both* original-production and immediate-export countries. A country of import is not necessarily the producer, as USGS documents. For intermediate inputs, map multiple processing countries and suppliers before US border.

## Data model (one canonical row per commodity-year-partner-port-form)
Required fields:
`year, hs10, hts_version, commodity_label, import_flow, partner_origin, shipment_country, true_producer_origin_status, customs_district, mode, customs_value_usd, landed_cost_usd, declared_quantity, declared_unit, normalized_metric_tonnes_if_valid, physical_input_grade, processing_stage, source_dataset_url, timestamp, provenance_state, us_downstream_naics, us_domestic_production, us_consumption, net_import_reliance, supply_concentration_hhi, criticality, substitutability, current_reuse, baseline_disposal_cost, recoverable_qty, product_spec, co_product, capex, opex, avoided_transport, avoided_import_value, water_footprint, energy_footprint, waste_emissions, project_site, confidence, review_gate`.
Data units vary: for machinery count and value matter more than weight; value-based prioritization must not drown out small but critical mass of semiconductor materials.

## First data collection / ranking workflow
1. **USITC 2025 census imports-for-consumption**: pull HTS10 by value, quantity, country and customs district. For 2026 use Jan-Aug YTD only, explicitly dated (not annualized to a verified full year). Build HS→ sector→ NAICS bridge.
2. **USGS 2026**: join direct and indirect mineral reliance by mineral form and producer/refiner. Mark 100%-reliant, high-reliant or strategic supply even when dollars modest.
3. **USDA ERS food imports 2025 + USDA nutrient fertilizer trade**: join 2025 dollars, volume, destination and forms; prioritize K import reliance and suitable N/P circularity.
4. **EIA energy imports**: origin, refinery grade, PADD, pipeline and tank capacity; compare gross crude import to energy exports with distinct grades/regions.
5. **Domestic transformation**: Census Annual Survey of Manufactures/County Business Patterns, USGS production, USDA crop/livestock geography, EPA TRI/ECHO, EIA power, USGS water; plant BOL and contracts may not be public and must remain UNKNOWN.
6. **Recovery network**: EPA waste generation, RCRA, AgSTAR, MSW, WRRF, e-scrap, scrap metals and spent industrial inputs; certify material balance and current baseline before claiming import offset.
7. **Rank** by (import concentration × criticality × shortfall risk × recoverable domestic resource × verified economic margin × water/ecology/community fitness); weights and tradeoffs publicly specified. Include 25/50/75 collection or yield sensitivities, not assume 100% physically attainable.
8. Issue exact per-row citations and run negative/uncertain controls. No numbers should be copied from national aggregate to product/port without data.

## Phase-one candidate chains for Atlas Lattice research
A. Fertilizer potassium and phosphorus/nitrogen streams; domestic closed-loop manure, food waste, wastewater and gypsum industrial integration. **K cannot be created in a reactor** and P must enter the waste feed; scarcity and collection matter.
B. Copper/aluminum/steel material looping and regional refining; quantify scrap already collected, grade and avoided imports.
C. Battery/electronics mineral recycling, especially magnets and strategic minor metals; account for contamination and manufacturing bottlenecks.
D. Sulfuric, ammonia and industrial chemical process chains; avoid hazardous sludge in fertilizer and secure permits.
E. Agricultural specialty feed/inputs and food-processing losses; food security and manufacturing resilience separate from trade deficit.
F. Heat, water and wastewater coupling at co-located industrial nodes; **local avoided costs rather than nominal imports** can dominate economics.

## Critical data gaps
Not a full 2025 line-level import extraction yet. No exact national per-commodity 2025 dollars/tons by partner and port imported here; no buyer-level BOM; no 2026 full-year data; no verified import displacement, financed projects or contracted supply. Don't declare any category wholly dependent on China, or recoverability independent of market grade. Consumer-electronics imports and farm machinery belong in the atlas as enabling supply, but a food-waste bioreactor cannot substitute them directly.

## Existing Atlas references
- [US onsite food-waste bioreactor scenarios](./US_NATIONAL_ONSITE_FOOD_WASTE_BIOREACTOR_25_50_75_2026-10-12.md)
- [Texas fertilizer demand and 25/50/75 circular recovery](./TEXAS_FERTILIZER_NUTRIENT_DEMAND_BASELINE_AND_25_50_75_OFFSETS_2026-10-12.md)
- [Texas landfill baseline economics](./TEXAS_FOOD_WASTE_BASELINE_AVOIDED_DISPOSAL_CHINA_COMPARISON_2026-10-12.md)
