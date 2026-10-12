# US raw-material imports, exports, reserve allowance and circular replacement — v0.4
**2026-10-12 · REPORTED / DERIVED / SIMULATED / PROPOSED / UNKNOWN · NON-CANON · ZERO REALIZED CREDIT**

## Purpose and boundary
Continue v0.3 with the user's clarified objective: ALL raw-material families, rather than finished goods or detailed crop-by-crop work. Primary metric is grade-matched import displacement. Consumption data does not block initial screening. This release populates 25 broad raw-material/material-input families from a downloaded federal annual trade table. All nine SITC crude-material subgroups are included, along with fuels, oils, bulk chemicals, fertilizer and upstream metals. Electric current is a replacement comparator, not raw material. Iron/steel, nonferrous metals and some chemical groups contain intermediates; retain them to screen the raw-to-refined bottleneck, without claiming they are pure raw-only groups. Machinery, vehicles, medicines, finished plastics and consumer products are excluded.

**This is broad family coverage, not a complete HS-coded raw-only census.** Minerals are bundled inside crude fertilizers/minerals, ores/scrap and metal families. Specialty grades, nuclear fuel and unresolved mixed groups need separate detail before claiming every raw-material line has been modeled. Dollar rows cannot establish tonnes, domestic surplus or an actual export gate.

## Source and revision
Downloaded Census **June 9, 2026 annual revision**, final_2025.pdf. Exhibit 14, printed PDF pages 37–38, gives 2025 total exports and general imports, million USD, unadjusted. It warns that its exhibit is not additive: do not sum summary categories, alternative classifications and child rows. The selected rows below are a screen; no nationwide raw-material total is claimed. The source PDF SHA-256 is recorded in JSON and the extracted table text is preserved. This supersedes reliance on the February 2026 first-release numbers for these specific rows; prior papers remain preserved.

## Reserve interpretation and screening equations
For a first pass independent of consumption metrics, use the **PROPOSED import-exposure reserve target = 20% of one year's gross matching imports**, about 73 days at average import pace. This is not 20% of all domestic requirements. Import-value-equivalent figures below are provisional budget/exposure markers, not certified reserve valuations or procurement prices.

- Trade deficit = max(imports − exports, 0).
- Deficit + reserve allowance = deficit + 0.20 × imports.
- Strict zero-import replacement exposure + initial reserve = 1.20 × imports, before crediting certified existing reserves.
- Trade-value surplus after reserve screen = exports − imports − 0.20 × imports.

The second formula is the user's ballpark deficit-plus-reserve screen. It assumes zero credited reserves for the displayed allowance, while actual holdings remain UNKNOWN. It is **not** the actual replacement quantity: exported and imported grades may differ. Export retention and waste-derived output must not both be credited for the same tonnes. Reserve build is a one-time stock acquisition, possibly staged; recurring import replacement is annual. Inventory maintenance/replenishment is separate. For a domestic-use reserve later, target=0.20×annual domestic requirement; that denominator remains UNKNOWN here.

## Populated matched family ledger
| Material family | Exports $B | Imports $B | Deficit $B | Deficit + reserve proxy $B |
|---|---:|---:|---:|---:|
| Hides, skins, and furskins, raw | 0.692 | 0.028 | 0.000 | 0.006 |
| Oil seeds and oleaginuos fruits | 18.263 | 1.137 | 0.000 | 0.227 |
| Crude rubber | 2.596 | 3.137 | 0.541 | 1.168 |
| Cork and wood | 6.480 | 8.467 | 1.987 | 3.680 |
| Pulp and waste paper | 7.633 | 3.966 | 0.000 | 0.793 |
| Textile fibers including waste | 6.924 | 1.174 | 0.000 | 0.235 |
| Crude fertilizers | 3.096 | 3.394 | 0.298 | 0.977 |
| Metalliferous ores and metal scrap | 29.650 | 11.156 | 0.000 | 2.231 |
| Crude animal and vegetable materials | 3.227 | 7.609 | 4.382 | 5.904 |
| Coal, coke, and briquettes | 10.323 | 0.894 | 0.000 | 0.179 |
| Petroleum products and preparations | 208.615 | 191.537 | 0.000 | 38.307 |
| Gas, natural, and manufactured | 80.876 | 11.100 | 0.000 | 2.220 |
| Electric current | 1.049 | 2.175 | 1.126 | 1.561 |
| Animal oil and fat | 0.419 | 1.637 | 1.218 | 1.545 |
| Fixed vegetable fats and oil, crude | 1.790 | 10.681 | 8.891 | 11.027 |
| Animal or vegetable fats, processed | 0.261 | 2.817 | 2.556 | 3.119 |
| Organic chemicals | 43.526 | 44.345 | 0.819 | 9.688 |
| Inorganic chemicals | 13.598 | 17.979 | 4.381 | 7.977 |
| Dyeing, tanning and coloring materials | 7.527 | 4.866 | 0.000 | 0.973 |
| Essential oil and reinoids | 18.454 | 24.436 | 5.982 | 10.869 |
| Fertilizers | 3.460 | 8.334 | 4.874 | 6.541 |
| Plastics in primary forms | 40.349 | 17.095 | 0.000 | 3.419 |
| Chemical materials and products | 41.024 | 26.076 | 0.000 | 5.215 |
| Iron and steel | 14.574 | 33.615 | 19.041 | 25.764 |
| Nonferrous metals | 19.384 | 69.108 | 49.724 | 63.546 |

## Findings across supply chains
- **Nonferrous metals:** imports 69.108B, exports 19.384B, deficit 49.724B; deficit-plus-import-reserve marker 63.546B. Meanwhile **ores and scrap** exports 29.650B vs imports 11.156B yield an 18.494B broad surplus. This is a cross-stage processing signal, not fungible metal or 18.494B of recoverable profit. Use v0.3 aluminum mass scenarios as a working example; copper, rare earths and batteries need separate grade/capacity filters.
- **Iron and steel:** 19.041B trade deficit; 25.764B marker. Scrap recovery, alloy sorting, electric-arc processing and qualified domestic steel manufacture are candidates. Coking coal cannot simply be replaced with intermittent electricity at an unchanged blast furnace.
- **Fertilizers:** 4.874B deficit; 6.541B marker. Crude fertilizer/mineral inputs separately show a 0.298B deficit. Do not add nutrients, mineral rock and downstream fertilizer as if they were independent recoverable atoms. Food/manure/wastewater N/P/K recovery applies broadly, with existing land application subtracted. Renewable-powered ammonia can address nitrogen feedstock but does not create phosphorus or potassium.
- **Inorganic chemicals:** 4.381B deficit; 7.977B marker. Spent-acid recovery, sulfur byproducts, brines and segregated industrial residuals need chemical identity and purity checks.
- **Cork/wood:** 1.987B deficit; 3.680B marker. Construction timber, wood residues, regenerated forestry and qualified fiber replacement are candidates. Pulp/waste-paper surplus does not establish interchangeable structural timber.
- **Oils:** crude vegetable-oil deficit 8.891B. Used cooking oil/fats can replace compatible industrial or fuel uses after purification. Waste-derived oil is not automatically edible food-grade oil or a substitute for every imported tropical oil.
- **Crude rubber:** 0.541B deficit. Tire recovery/devulcanization and renewable feedstocks are candidates; recovered rubber is not universally equivalent to virgin natural latex.
- **Fibers/pulp:** broad export surpluses coexist with imports, making grade sorting and domestic conversion relevant. Do not count existing exported recycling as landfill diversion.
- **Organic chemicals/primary plastics:** solvent recovery, qualified polymer recycling, biogenic carbon feedstocks and renewable hydrogen warrant screening. Chemical materials/products and essential oils contain mixed products; replacement ratios remain UNKNOWN.

## Oil/gas screen: useful national pattern, not certified export controls
Broad gas exports 80.876B vs imports 11.100B: 69.776B value surplus; after a 2.220B import-exposure reserve allowance, 67.556B value margin remains. Broad petroleum exports 208.615B vs imports 191.537B: 17.078B surplus, smaller than the 38.307B reserve allowance, giving −21.229B on this value screen. **Crude oil separately**: exports 98.710B, imports 139.990B, deficit 41.280B, deficit-plus-reserve marker 69.278B (Exhibits 6/7); this is already included in petroleum and must not be added.

Grade-matched reallocation, reserves and renewable demand replacement can therefore be studied across these families. Dollar surpluses are not physical sufficiency: petroleum refinery configuration, crude gravity/sulfur, gas pipelines, seasonal demand and storage deliverability remain constraints. Coast-to-coast delivery is explicitly UNKNOWN. No actual restriction is enacted or recommended from these aggregates; lawful human review remains mandatory. The user's strict zero-import gate cannot be satisfied by a positive net-export balance while imports continue.

## Waste processing versus shipping: reproducible economic frontier
Actual shipment charges by material are UNKNOWN. Census customs value excludes international freight/insurance; CIF−customs is the appropriate import-charge measure when available. Imports here are customs values, not landed delivered prices. The API attempt did not produce usable charges; do not disguise scenario rates as researched quotes.

The runner supplies:
- 2%, 5%, 10% of import value **SIMULATED shipping/insurance sensitivities** for every family.
- 324 normalized cases: 25/50/75% capture of 100 wet tonnes of eligible additional feedstock; 50/80/95% yield; 50/80/100% grade acceptance; processing 10/30/60/100 USD per feed tonne; avoided shipping 10/30/60 USD per qualified product tonne.
These ranges are engineering sensitivities, not market estimates. They are not added to trade values as realized benefits.

Processing cost per qualified tonne = processing cost / (yield × grade acceptance). At 10 USD/feed tonne, 80% yield and 80% acceptance, this is **15.625 USD/usable tonne**. Against assumed shipping of 30 USD/usable tonne, narrow freight-minus-processing margin is +14.375 USD/usable tonne; against 10 USD it is −5.625. At 30 USD/feed tonne the processing cost is 46.875 and exceeds the 30 USD shipping case. Every stream requires its own actual yields/costs.

Whole-system incremental benefit = avoided baseline import procurement and external freight + avoided disposal + additional distinct outputs − recovery OPEX − annualized CAPEX − collection/delivery − residual handling − foregone existing reuse/export value. Do not add output sales and avoided purchase of that same product. A national welfare analysis must also separate real costs from transfer payments; customs purchase value is an exposure/buyer-cost marker, not proof of social gain. UNKNOWN coast-to-coast freight is not imputed to zero. Narrow positive margins do not prove full feasibility.

## Renewable replacement matrix
| Material/use | Circular route | Renewable route | Accounting constraint |
|---|---|---|---|
| Gas/coal for heat/power | Biogas, waste heat | Electrified heat; renewable electricity plus firming | Match delivered service, temperature, seasonal reliability; no automatic tonne-for-tonne swap |
| Petroleum fuels | Qualified waste fats/oils and residues | Electrified transport; renewable fuel pathways where required | Separate fuel substitution from petrochemical feedstock |
| Ammonia/nitrogen inputs | Manure/food/WWTP nitrogen | Renewable-powered hydrogen + nitrogen-to-ammonia | Include hydrogen/plant electricity, water and delivered cost; P/K need material sources |
| Steel/metals | Scrap sorting, remelt/refine | Renewable-powered furnaces; hydrogen where suitable | Power supplies processing; it does not create missing metal atoms or alloy purity |
| Chemicals/plastic resins | Solvent/acid/polymer recovery | Qualified biogenic feedstock and renewable H2 | Reaction pathway, carbon source, purity and process capacity required |
| Timber/fibers/rubber | Demolition wood, paper/textile/tire recovery | Regenerative forestry/fibers and suitable bio-feedstocks | Growth time, land/water and material performance required |
| Minerals/gypsum/cement inputs | Slag, ash, gypsum and suitable residuals | Renewable process heat | Contaminant/structural qualification; climate benefits are separate from import credits |

DOE supports exploring electrification, low-carbon feedstocks, hydrogen and recycling across industrial sectors. This matrix records candidates, not independently verified substitution fractions.

## Physical examples and limits
v0.3 potash gross imports 5.60 Mt K2O imply an initial import-exposure reserve 1.12 Mt K2O and gross replacement-plus-build target 6.72 Mt; net-import-deficit-plus-build marker 6.55 Mt. v0.3 refined copper imports 1.70 Mt imply 0.34 Mt reserve allowance; gross replacement-plus-build 2.04 Mt versus net-deficit-plus-build 1.93 Mt. Aluminum crude/semi imports 4.40 Mt imply 0.88 Mt allowance; grade-matched zero-import-plus-build 5.28 Mt. These are derived allowance calculations, not available recovery or procurement commitments. Certified holdings/stock credit are UNKNOWN.

The broad agricultural comparator is exports 171.486B/imports 212.944B, 41.458B deficit, 84.047B deficit-plus-reserve marker. It is mixed raw/processed and overlaps this ledger; it is included only to demonstrate the common framework, not granular crop analysis or a raw-agriculture total.

## Reproduction and deliverables
Run `python3 tools/raw_material_supply_screen_v0_4.py` from repository root. Standard library only; arithmetic, 25-family count, 324-case count and UNKNOWN transport checks passed.
- [Frozen trade/source metadata](../data/raw_materials_v0_4/trade_2025.json)
- [Matched trade/reserve CSV](../data/raw_materials_v0_4/raw_material_trade_reserve_screen.csv)
- [Processing/freight sensitivity](../data/raw_materials_v0_4/processing_vs_freight_sensitivity.json)
- [Federal source table receipt](../data/raw_materials_v0_4/census_exhibit14_source_2026-06-09.txt)
- [Runner](../tools/raw_material_supply_screen_v0_4.py)
- [Previous physical pilot](US_NATIONAL_SUPPLY_SECURITY_LEDGER_V0_3_2026-10-12.md)

Sources: [Census annual revision](https://www.census.gov/foreign-trade/Press-Release/final_revisions/index.html), [downloaded federal report](https://www.census.gov/foreign-trade/Press-Release/ft900/final_2025.pdf), [Census value/freight definitions](https://www.census.gov/foreign-trade/reference/definitions/index.html), [DOE low-carbon feedstocks](https://www.energy.gov/cmei/ito/low-carbon-fuels-feedstocks-and-energy-sources), [DOE industrial roadmap](https://www.energy.gov/documents/industrial-decarbonization-roadmap-fact-sheet).

Next data gap is **quantity/grade/charges inside these populated families**, not more crop detail. Actual incremental waste inventories, material assays, domestic processing capacity, renewable delivered costs and existing reserves are UNKNOWN. Financial deficit signals and cost-frontier math establish where replacement is worth testing; they do not prove the full deficit can be closed.
