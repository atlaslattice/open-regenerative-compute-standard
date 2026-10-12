# Texas fertilizer self-sufficiency: 25/50/75% food-waste recovery
**Dated October 12, 2026 · ADDITIVE correction to earlier US-import denominator · DERIVED / PROPOSED / UNKNOWN · ZERO REALIZED CREDIT**

## Objective
**Texas fertilizer supply security and physical nutrient self-sufficiency** rather than offsetting a fraction of all US fertilizer imports. Separate three different metrics: (i) share of annual Texas agronomic nutrient demand supplied by Texas recovered sources, (ii) Texas international fertilizer imports by country/commodity, and (iii) domestic interstate shipments into Texas. These do not share a common observable denominator; never equate Texas demand with foreign imports.

## Sources and evidence gates
- Texas total *food waste* 5–8M US short tons/year remains a **UNVERIFIED scenario envelope** taken from the prior food-waste note; not an established 2026 TCEQ statewide inventory: [base model](./TEXAS_FOOD_WASTE_BIOREACTOR_FERTILIZER_MARKET_SCREEN_2026-10-12.md).
- Historical Texas farm fertilizer/lime/soil-conditioner spending of **~$1.3B in 2022** is **combined spending in dollars**, not nutrient-specific physical demand, state import value, or direct 2026 fertilizer costs. Product grades and delivered fertilizer value vary.
- USDA NASS has Texas cropped-acreage and crop-specific nutrient applications; an actual Texas demand ledger must sum county/crop nutrient use and adjust animal feed, horticulture and inventory changes. [Texas agricultural statistics](https://www.nass.usda.gov/Statistics_by_State/Texas/).
- US Census publishes [international imports by state of ultimate destination and HS6](https://www.census.gov/foreign-trade/data/ISTHSM.html) and [state destination import series](https://www.census.gov/foreign-trade/statistics/state/destination_state/index.html). International shipments coded to Texas do not automatically equal Texas final use; industrial products might be transshipped, and customs HS products are not direct crop-available N/P2O5/K2O equivalents.
- Domestic interstate fertilizer deliveries into Texas are NOT in foreign-import series; obtain state fertilizer sales/tonnage, port manifests, supplier shipments and inventories. **Texas-specific import-displacement % is not yet measurable.**

## Defined capture / nutrient outcomes
Raw hypothetical Texas statewide food waste: **5–8 million US short tons/year** × 0.90718474 = 4.536–7.257 million wet metric tons/year.

Collection/recovery scenarios refer to fraction of this **food-waste resource routed to a qualified treatment system**: **25%, 50%, 75%**. These do **NOT** assert digestion or nutrient mineral-extraction efficiency. Existing prevention, food rescue, animal feed, composting and disposal fate have to be reconciled; 75% is a high-diversion stress case, not a forecast.

For each metric tonne of input food waste, unverified screening yields:
- crop-accessible recovered nitrogen N **2–6 kg**;
- phosphate as P₂O₅ equivalent **0.5–2 kg**;
- potash as K₂O equivalent **1–3 kg**;
- gross methane **60–150 m³ CH₄**, with 35.3147 standard-ish ft³/m³ approximate physical conversion before gas standard-condition accounting, pipeline qualification and losses.
These ranges need waste composition, BMP, nutrient assay, process chemistry and crop-availability validation. Nitrogen can volatilize, potassium and phosphorus may be co-products of diluted digestate, and transport can nullify fertilizer substitution.

## Reproducible 25/50/75 scenarios

| Capture of assumed TX food waste | Collected wet metric t/year | Available N kg/year | Available P₂O₅ kg/year | Available K₂O kg/year | Gross CH₄ Bcf/year |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 25% | 1.13M–1.81M | 2.27M–10.89M | 0.57M–3.63M | 1.13M–5.44M | 2.40–9.61 |
| 50% | 2.27M–3.63M | 4.54M–21.77M | 1.13M–7.26M | 2.27M–10.89M | 4.81–19.22 |
| 75% | 3.40M–5.44M | 6.80M–32.66M | 1.70M–10.89M | 3.40M–16.33M | 7.21–28.83 |

**Do not sum wet digestate and finished compost from the same original feedstock.** Do not double credit co-digested manure already counted in the separate statewide manure ledger. Prioritise food rescue/prevention and robust contamination screening ahead of RNG credits.

## Real Texas denominator: formulas and missing values
Define physical annual Texas demand by crop/use (tonnes nutrients) as `D_TX_N, D_TX_P2O5, D_TX_K2O`. These are **UNKNOWN, not zero** pending verified aggregation.

For independently verified accessible recovered fertilizer nutrient streams, `T_TX_N, T_TX_P2O5, T_TX_K2O`, compute:
- `Texas demand offset per nutrient = min(1, T_TX_nutrient / D_TX_nutrient)`, not a claim all Texas fertilizer is imported.
- `Texas remaining gap per nutrient = max(0, D_TX_nutrient - T_TX_nutrient - secured other in-state production)`, plus soil, timing, storage and land-application constraints.
- `International fertilizer-import substitution = independently validated canceled international import nutrient by commodity / true TX-bound international imports of that nutrient`. No reliable percentage without HS customs detail and end-use mapping.
- `Interstate fertilizer displacement = independently validated reduction in purchases from other US states / interstate nutrient receipts`. Don't treat interstate trade as foreign-import dependence.
- `Texas self-sufficiency ratio = validated within-Texas supply / TX annual nutrient requirements`. In-state production, current reuse, inventory and crop-soil legacy nutrient availability must be separately entered.

## Resource integration expansion, not yet quantified
Food waste only underlies the displayed numbers. Atlas full in-state self-sufficiency model should include **non-overlapping** streams of dairy / feedlot / hog / poultry manure, source-separated municipal food waste, wastewater treatment sludge/liquid nutrients, harvest residues and industrial nutrient streams. Maintain elemental N/P/K mass closure, process loss, salinity, contaminant, producer baseline and the feedstock's existing use, before calculating usable net new replacement.

## Current evidentiary conclusion
**No defensible actual percentage of Texas fertilizer imports displaced** can be supplied from current Texas food-waste hypotheses and USDA US-wide import figures alone. The table provides transparent physical recovered nutrient potential at 25%, 50% and 75% capture, and the data schema needed to measure whether Texas could achieve local or statewide nutrient self-sufficiency. Current economic savings, actual import cancellations and realized environmental credit = **0 established**.

## Next dataset tasks
1. Get TX 2024/2025 commercial fertilizer tonnage/sales by nutrient grade, plus USDA Texas county crop-acreage and annual fertilizer application rates.
2. Retrieve international fertilizer imports into Texas by HS6 and country, convert each product to N/P₂O₅/K₂O; remove through-shipments and establish final end users.
3. Estimate interstate arrivals and existing native Texas industrial fertilizer production by actual plant output (not merely nameplate).
4. Identify county-specific recoverable organics and nutrient use, validating 25/50/75% capture feasibility, food-rescue baseline and digester/compost product quality.
5. Run full resource-closure scenarios and environmental/economic sensitivity, keeping P and K, manure and food streams non-overlapping.

## Previous publications retained
[US import comparison, a different denominator](./TEXAS_FOOD_WASTE_US_FERTILIZER_IMPORT_OFFSET_2026-10-12.md) is preserved for historical context; the **Texas statewide self-sufficiency ledger** is the primary decision frame for this research. Do not erase either version.
