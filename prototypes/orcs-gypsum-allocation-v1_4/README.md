# ORCS gypsum allocation v1.4 — empirical-only interface

The first executable crosswalk between the **already published** Dongjiakou/Harbor Island physical-equivalent ceilings and future official USDA soil/crop evidence. It deliberately makes **no national yield estimates, acreage rankings, recovery claims or operator decisions** until agency data are acquired and product assays certified.

## Official data connectors (documentation verified, extraction not performed)
- USDA NRCS SSURGO: https://www.nrcs.usda.gov/resources/data-and-reports/soil-survey-geographic-database-ssurgo . Download/web services. Use per-state and survey-area metadata, soils properties, component percent and soil test; available map-unit descriptions are not an individual farm prescription.
- USDA NASS Quick Stats: https://www.nass.usda.gov/Quick_Stats/ . Public interactive/bulk data; API key may be required. Connect year, state/county FIPS, commodity, harvested/planted acres; avoid suppressed counts and conflicting boundaries.
- USGS Mineral Commodity Summaries 2026 gypsum: https://www.usgs.gov/data/mineral-commodity-summaries-2026-data-release . Official CC0 CSV 2026 release, not yet ingested. Prior U.S. 2025 gypsum **estimated 20 Mt crude production and 44 Mt consumption**, which are *not* agronomic gypsum use in isolation. Distinguish mined and synthetic product.
- USDA NRCS CPS 333 gypsum amendments and CPS 610 saline/sodic soils. Field testing of product purity/contaminants, sodium, chloride, soil chemistry and drainage is required.

Existing model source: Harbor Island **proposed** 0.733 million t/year gypsum-equivalent *chemical inventory*; Dongjiakou **modeled** 62.7–76.9 thousand t/year gypsum-equivalent. These values are not commercial production nor agronomically suitable product. Never promote this ledger into physical supply without qualified assays and demonstrated recovery.

## Run

`python3 -m unittest discover -v`
`python3 allocation.py`

The module accepts **real, independently sourced** and qualified inventory as input. The user-supplied allocation must satisfy material conservation across soil, acid, industrial and resilience reserve uses. Missing qualifiers and missing baseline sources are UNKNOWN, not zero. No synthetic fields/crops/hazards are used in any empirical result. Test fixtures exercise arithmetic only and never imply real field outcomes.

Draft PR #7; append-only. Human and legal review required for actual facility, farmer, industrial/acid, environmental or trade decisions.
