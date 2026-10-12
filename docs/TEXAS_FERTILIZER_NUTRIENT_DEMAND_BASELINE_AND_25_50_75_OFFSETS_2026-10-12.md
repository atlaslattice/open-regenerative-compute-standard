# Texas Commercial-Fertilizer Nutrient Baseline and 25/50/75% Food-Waste Offset — 2026-10-12

**Evidence: REPORTED 2017 N/P fertilizer purchasing volumes, DERIVED scenario ratios, UNKNOWN 2026 statewide demand and all actual import substitution. NON-CANON, ZERO REALIZED CREDIT.**

## Key finding

The U.S. EPA state commercial fertilizer purchased dataset supplies a **Texas-specific historical physical demand proxy** instead of dividing Texas recovered nutrients by all U.S. imports. In the **2017** reporting column, Texas purchased **608,141 thousand kg nitrogen** (608.141 million kg N) and **143,232 thousand kg phosphate** as P2O5 (143.232 million kg P2O5). This is **2017 reported commercial fertilizer purchases, not current 2026 agronomic demand**, not total nutrient use including manure, not imports, and not a state self-sufficiency measure.

Primary cited public table: https://www.epa.gov/nutrientpollution/commercial-fertilizer-purchased . EPA notes AAPFCO fertilizer sales/shipments reporting, Texas September–August fertilizer-year basis, and exclusion of livestock manure, amendments and liming material. EPA labels a separate 2022 fertilizer report in its metadata but **the visible Texas N/P columns end in 2017**. Do not misread that reference as a Texas 2022 nutrient observation.

## Assumed food-waste resource and reactor nutrient output

Source [previous TX 25/50/75 study](./TEXAS_STATE_FERTILIZER_SELF_SUFFICIENCY_RECOVERY_25_50_75_2026-10-12.md). Total food waste **5–8 million US short tons/year** remains a provisional, unverified Texas scenario. Conversion: 0.90718474 metric tonnes/US short ton. Capture 25, 50, or 75 percent of this envelope. Recovered crop-available nutrient yields per original wet metric ton are **assumed**, NOT laboratory-verified: 2–6 kg N, 0.5–2 kg P2O5, 1–3 kg K2O. No digestion efficiency is separately credited or measured. Existing food rescue and other material uses must not be displaced.

## Texas-specific arithmetic (comparison with 2017 commercial-fertilizer purchase proxy)

| Hypothetical collection | Recovered N (million kg/year) | % of 2017 TX commercial N purchases | Recovered P2O5 (million kg/year) | % of 2017 TX commercial P2O5 purchases | K2O (million kg/year) | K % |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 25% | 2.27–10.89 | **0.37–1.79%** | 0.57–3.63 | **0.40–2.53%** | 1.13–5.44 | **UNKNOWN** |
| 50% | 4.54–21.77 | **0.75–3.58%** | 1.13–7.26 | **0.79–5.07%** | 2.27–10.89 | **UNKNOWN** |
| 75% | 6.80–32.66 | **1.12–5.37%** | 1.70–10.89 | **1.19–7.60%** | 3.40–16.33 | **UNKNOWN** |

The EPA page supplies N and phosphate (P2O5), **not potassium purchase mass**, so Texas K2O market-offset percentage remains UNKNOWN rather than using a fictitious denominator. Different vintage: 2017 fertilizer purchase data contrasted with 2026 scenario waste inputs; percentages illustrate **scale only**. Actual effective nutrient substitution requires verified crop access, digestate regulations, nutrient equivalence, and logistics; it is not measured displacement.

## Texas-state self-sufficiency balance (still requires measurements)

- `TX_total_agronomic_demand_N/P2O5/K2O`: 2024–2026 crop application by grade and county, horticultural and other uses. 2017 fertilizer purchase is an *incomplete, older proxy*.
- `TX_current_domestic_chemical_production_N/P2O5/K2O`: actual Texas-origin sales usable by Texas agriculture; plant nameplate capacities are not physical supply.
- `TX_existing_manure_nutrients`: farm baseline nutrient reapplication measured separately, with only **incremental** recovered nutrients counted as new import displacement.
- `TX_new_food_waste_recovery`: collected non-food-rescue fraction, lab-verified and product certified.
- `TX_wastewater_recovery`: measured WRRF inputs, contract restrictions and recovered phosphate/ammonia; exclude food/manure already entering wastewater totals.
- `TX_crop_residues`: subtract current soil-retained, grazing/feed and field fertility inputs to avoid degradation or double counting.
- `TX_intrastate_recycled_total`: must be compared with agronomically accessible nutrient needs near destination farms (distance, salinity, nutrient timing and local overload).
- `TX_foreign_imports`: US Census state-of-destination customs series are an imperfect proxy for ultimate Texas use; don't equate with demand.
- `TX_interstate_commodity_receipts`: purchased fertilizer from Louisiana, Oklahoma and other US states is *not a foreign import*; requires shipment/accounting data.

## Source-access and reconciliation plan

1. Texas Office of the State Chemist / AAPFCO latest fertilizer consumption **mass and guaranteed analyses** by product/year: derive 2024/25/26 N/P2O5/K2O. Note blended products must be apportioned by mass fraction; not simply count NPK product tonnage.
2. USDA NASS/Texas 2022 census commodity/county acres, annual application rates from Agriculture Chemical Use surveys and state statistics: independent nutrient-demand cross-check. Missing data should remain UNKNOWN, not interpolated as verified.
3. US Census import state of destination by HS 3102/3103/3104/3105, convert products to nutrient masses, separate transshipments, then identify actual TX users; likewise domestic interstate supplies and native production.
4. ReFED/TCEQ current TX food waste by origin/destination; inspect commercial packaging residues and contamination.
5. Manure and WWTP sludges: establish **baseline already used as fertilizer**, site BMP/total N/P/K analysis, nutrient conversion and bioreactor recovery mass closure; build scenario 25/50/75% separately for each source, not apply assumed food-waste yields to manure.
6. Assign circular material flows by origin and final use, accounting for struvite/ammonium sulfate alongside wet digestate without dual credits.

## Model equations

```python
SHORT_TON_TO_METRIC = 0.90718474
TX_2017_N_KG = 608_141_000
TX_2017_P2O5_KG = 143_232_000
for capture in (0.25,0.5,0.75):
    lo = 5e6 * SHORT_TON_TO_METRIC * capture
    hi = 8e6 * SHORT_TON_TO_METRIC * capture
    print(capture, 'N percentage',lo*2/TX_2017_N_KG*100,hi*6/TX_2017_N_KG*100,
          'P percentage',lo*.5/TX_2017_P2O5_KG*100,hi*2/TX_2017_P2O5_KG*100)
```

**No actual Texas foreign fertilizer import share can be inferred from this result.** Actual 2026 physical nutrient demand, K consumption, current TX-origin production, interstate/foreign imports and all certified realized recovery are not yet established.