# Texas food-waste nutrient recovery vs US fertilizer imports
**2026-10-12 · DERIVED / HYPOTHETICAL · NON-CANON · ZERO REALIZED CREDIT**

## Comparison scope
This models Texas **food waste only** (not manure, sewage biosolids or other co-feedstocks) relative to gross 2024 **United States** imported nutrient equivalents. It does not imply nutrients become certified retail fertilizer, or that equivalent import shipments are displaced. Statewide Texas waste supply is not verified and 25% diversion is assumed, not contracted.

## Import baseline
USDA AMS Grain Transportation Report, April 10 2025, quoting US Census fertilizer trade: 2024 imports in short tons of nutrient equivalents: **5.8 million short tons N, 1.6 million short tons P2O5, 9.6 million short tons K2O**. Source https://www.ams.usda.gov/sites/default/files/media/GTR04102025.pdf page 4.
Denominator converted with 907.18474 kg/short ton, yielding **5.2617 billion kg N**, **1.4515 billion kg P2O5**, **8.7090 billion kg K2O**. These are **gross** imports before reexports; they are not 2026 imports, Texas-only imports, or national consumption.
For updated series see USDA nutrient-equivalent dashboard https://agtransport.usda.gov/Fertilizer/Fertilizer-Imports-and-Exports-Nutrient/tpd5-muue .
USGS 2026 MCS potassium also indicates **92% net potash import reliance in 2025**, though the USGS table is a distinct nutrient/commodity definition and historical period: https://pubs.usgs.gov/periodicals/mcs2026/mcs2026.pdf .

## Texas food-waste assumption and nutrient ranges
See [Texas food waste bioreactor market screen](./TEXAS_FOOD_WASTE_BIOREACTOR_FERTILIZER_MARKET_SCREEN_2026-10-12.md). Unverified Texas food waste **5–8 million short tons/year**, with 25% AD/recovery collection; at 0.90718474 metric ton/short ton this gives **1.134–1.814 million metric tons/year** of captured feedstock. Plant-available **nutrient recovered per wet input metric ton** is screening assumption: N **2–6 kg/t**, P2O5 **0.5–2 kg/t**, K2O **1–3 kg/t**. Actual assays, nitrogen loss, phosphorus speciation, land-application feasibility, fertilizer registration and crop uptake are all unresolved.
The assumed nutrient recovery is not inferred from wet digestate weight, avoiding a common false equivalence.

| Nutrient | Hypothetical recovered kg/year | 2024 US gross imports kg nutrient | Arithmetic equivalent |
| --- | ---: | ---: | ---: |
| N | 2.268–10.886 million kg | 5,261.7 million kg | **0.043–0.207%** |
| P2O5 | 0.567–3.629 million kg | 1,451.5 million kg | **0.039–0.250%** |
| K2O | 1.134–5.443 million kg | 8,709.0 million kg | **0.013–0.063%** |

The lower bound combines minimum waste generated and minimum nutrient yield; upper bound max/max. Fractions are ratios of *potential recovered crop-available nutrient* / national historical gross import nutrient, **not literal forecast import substitution**. Regional Texas imports, local agricultural demand, plant nutrient use efficiencies, contaminants and products quality may reduce achievable actual substitution further.

## Upside / scale questions
- At 100% (hypothetically) recoverable Texas food waste, arithmetic ratios are fourfold: N 0.17–0.83%, P2O5 0.16–1.00%, K2O 0.05–0.25%. This is NOT physically attainable without avoiding food rescue, existing diversion and collectability limits; never promote as policy target.
- A national food-waste and livestock-manure coordinated program must use separate national data sets, prevent manure/food double counts (especially co-digestion), and quantify crop nutrient partitioning. A national extrapolation from Texas alone would be invalid.
- The US gross import denominator for K can differ markedly from US net consumption due to fertilizer reexports. An energy/fertilizer policy should evaluate import displacement by region and use net import reliance separately.

## Reproducible formulas
```python
short_to_metric=0.90718474
imports_kg={"N":5.8e6*907.18474, "P2O5":1.6e6*907.18474, "K2O":9.6e6*907.18474}
captured_metric_t=[5e6*short_to_metric*.25,8e6*short_to_metric*.25]
nutrient_kg_per_t={"N":[2,6],"P2O5":[.5,2],"K2O":[1,3]}
for label, (lo,hi) in nutrient_kg_per_t.items():
    low=captured_metric_t[0]*lo
    high=captured_metric_t[1]*hi
    print(label,low/imports_kg[label]*100,high/imports_kg[label]*100)
```

## Work remaining
Source a rigorous Texas annual **food waste mass by sector and fate**; replace preliminary plant-availability yields with feedstock-specific and reactor-specific sampled nutrient assays and recovery chemistry; check digestate contaminants/market approval; compare with Texas farm nutrient demand rather than only US trade; simulate collectability and transport distance; preserve no realized credits.