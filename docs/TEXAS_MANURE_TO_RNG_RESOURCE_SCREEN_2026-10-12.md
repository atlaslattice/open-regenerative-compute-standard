# Texas manure-to-biogas/RNG screening ledger — October 12, 2026

**Status: DERIVED scenario from REPORTED USDA livestock counts + PROPOSED unverified manure and collection parameters. No current project, power export, carbon savings, revenues or verified feedstock ownership is claimed.** This is a forkable first-pass spreadsheet-style model, not a BMP-tested plant feasibility study.

## Source anchors

- USDA/NASS Texas 2025 State Agriculture Overview (published source inventory dated Jan 1 2026 for cattle and Dec 1 2025 for pigs): https://www.nass.usda.gov/Quick_Stats/Ag_Overview/stateOverview.php?state=texas — all cattle/calves 12.1 million; beef cows 4.045 million; milk cows 705,000; **cattle on feed 2.54 million**; hogs 1.13 million; **broilers production 731.8 million annually**, NOT simultaneous poultry standing population.
- EPA AgSTAR candidate feasibility guidelines: https://www.epa.gov/agstar/anaerobic-digestion-right-your-farm ; screens manure collections, large dairies and hog units; 90% manure routinely collected is a recommended eligibility signal, not demonstrated Texas fraction.
- EPA AgSTAR national potential: https://www.epa.gov/agstar/agstar-market-opportunities-report and https://www.epa.gov/agstar/agstar-data-and-trends . Published national **technical** categories are not state-specific verified outputs.
- EPA project development and feedstock/credit criteria: https://www.epa.gov/agstar/frequent-questions-about-livestock-biogas-projects.

## Scope and anti-double-counting decisions

Texas total cattle includes beef cows, dairy cattle and feedlot stock. **Do not add 12.1m cattle to 2.54m feedlot and 705k dairy counts.** This screening ledger deliberately includes only dairy cattle, cattle currently on feed and hogs as partially collectable cohorts, and excludes other beef grazing cattle, slaughter waste, poultry litter and undifferentiated livestock manure. Annualized point-in-time feedlot inventories assume a typical occupied inventory throughout the year; animal movements and seasonal stock are not added again. Hog inventory is a headcount not annual throughput. Poultry annual production is not an inventory: no chicken litter estimate without birds in-house durations, litter cleanout frequency, reuse and housing count.

## Explicit scenario parameters (not field measurements)

- Days/year 365; wet manure kg/head/day illustrative dairy 55, feedlot beef 25, hog 5. These can be inconsistent with water added via flush, animal weight and feeding ration: require site samples.
- Collectable share of gross wet manure scenarios: 75% dairy, 55% cattle on feed, 65% hog. **All are invented screening assumptions and not measured TX percentages**; do not confuse these with EPA's farm eligibility rule suggesting 90% regularly collected.
- Yield low/mid/high in **m³ CH4 per wet metric tonne COLLECTED**: dairy 10/18/25; beef 8/13/20; hog 5/12/20. No digestion or upgrading uptime penalties included in these gross methane potentials. Numeric limits depend on volatile solids, feed moisture and BMP.
- 35.3147 ft³ per m³ CH4; 0.0353 MMBtu lower heating value per m³ CH4 approximate using 35.8 MJ/m³ and 1055 MJ/MMBtu? Correct energy: 35.8 MJ/m³ / 1055.056 MJ/MMBtu = 0.03393 MMBtu/m³. Use **0.03393 MMBtu/m³ CH4 LHV**, not 0.0353. For RNG pipeline sales use HHV, gas specification and dry standard temperature/pressure explicitly, not this energy figure.
- Upgrading methane recovery sensitivity 90%/95%/98% and downtime 5%; no carbon credits, tipping fees, digestate product sales or environmental benefit monetize unless verified.

## Cohort volumes (three select confined cohorts only)

| Cohort | USDA animals (head) | Assumed wet kg/head/day | Gross wet metric tons/year | Screening collectable % | Collected metric tons/year | Low–high methane m³/t collected | Middle methane m³/year |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Dairy cows | 705,000 | 55 | 14,152,875 | 75% | 10,614,656 | 10–25 | 191,063,813 |
| Beef cattle on feed | 2,540,000 | 25 | 23,177,500 | 55% | 12,747,625 | 8–20 | 165,719,125 |
| Hogs | 1,130,000 | 5 | 2,062,250 | 65% | 1,340,463 | 5–20 | 16,085,550 |
| **3 cohorts** | | | **39,392,625** | | **24,702,744** | | **372,868,488** |

**Results are scenario arithmetic, NOT USDA annual manure tonnage estimates**. Across these three populations, middle gross potential is **0.373 billion m³ CH4/year** = **13.17 Bcf/year**. Crude low/high yield-only band: **7.59–19.32 Bcf/year**; this band does not include uncertainty in herd-size distributions, collectability, site access, BMP or avoided baseline methane. Middle example with 95% upgrader recovery, 95% uptime: **11.88 Bcf/year** of cleaned methane equivalent (not verified gas-grid injection and not guaranteed sales).

## Unit economics as a *sensitivity* calculation

Gas sales revenue, before CAPEX, OPEX, electricity, transport, leak mitigation, nutrient management, taxes, contracts and gas tariffs, at a hypothetical **$3, $6, $10/MMBtu** realized value and using gross methane LHV energy (not market standard) are **$37,954,283, $75,908,567, and $126,514,278 per year, respectively**. These synthetic calculations are not bids, tariffs or bankable revenue; delivered RNG volume is lower after losses/downtime, upgrading HHV conversion differs, and not all screened operations qualify.

Net profit cannot be inferred without cost and environmental baseline. For RNG, quantify: farm-gate manure handling, digesters, biogas upgrading, compression/pipeline interconnect, O2/H2S/H2O cleanup, lagoon covers, labor, financing and energy, nutrient export, transport distances, avoided baseline lagoon methane, and emissions leakage. Avoid claiming digestate is automatically a commercially saleable fertilizer or safe for fields; nutrient constraints, salts, pharmaceuticals, pathogen control and application timing are essential.

## Atlas Lattice / ORCS system integration

Model small clusters where municipal food-processing organics or documented industrial byproducts can be *co-digested* without bypassing food safety or accepting hazardous feedstocks; reallocate waste heat, water treatment energy, RNG offtake, and nutrient recycling only when infrastructure distance and rights are known. Environmental accounting must be relative to manure's **actual baseline handling** (e.g. anaerobic lagoon vs dry pasture), not assume all avoided manure methane would otherwise be vented.

## Critical corrections to preceding chat

An earlier 100 wet metric-ton/day dairy example at 18 m³/t yields 1,800 m³/day, or **~23.2 million ft³/year** of methane. It yields **~6.5 GWh/year of methane lower-heating-value fuel energy**; if converted to electricity at 30% conversion, ~1.95 GWh/year **gross electrical**, prior to parasitics. It is not 6.5 GWh electrical, and no grid deliverability is implied. Percent shares must not be compared across theoretical manure and feasible capture without consistent assumptions. No guarantee Texas statewide livestock stock can be captured at the screen percentages.

## Missing primary data / how to upgrade model

1. 2026 Texas county-level dairy operations and actual head at barns; feedlot operators and manure handling; hog farm distribution; poultry litter tons by cleanout cycle.
2. Animal-specific dry matter/volatile solids, biogas/CH4 BMP at representative farms; seasonal management.
3. Actual farm-level daily collection fraction, economics and permitted farm-digester locations.
4. Methane leakage from lagoons and upgrading, feedstock contracts, nutrient/soil testing, off-site disposal/land rights.
5. Pipeline proximity, utility interconnect cost, RNG gas quality, tariffs, RNG certification and payment contracts; realistic avoided emissions.
6. Source-neutral independent engineering validation. **REALIZED CREDIT = ZERO.**

## Reproducible formulas

```python
days=365
cohorts=[
 {"head":705000, "kg_day":55, "collection":.75, "m3_t":18},
 {"head":2540000,"kg_day":25, "collection":.55, "m3_t":13},
 {"head":1130000,"kg_day":5,  "collection":.65, "m3_t":12},
]
wet_tonnes=sum(x["head"]*x["kg_day"]*days/1000 for x in cohorts)
collected_tonnes=sum(x["head"]*x["kg_day"]*days/1000*x["collection"] for x in cohorts)
methane_m3=sum(x["head"]*x["kg_day"]*days/1000*x["collection"]*x["m3_t"] for x in cohorts)
rng_bcf=methane_m3*0.95*0.95*35.3147/1e9
print(wet_tonnes,collected_tonnes,methane_m3,rng_bcf)
```
