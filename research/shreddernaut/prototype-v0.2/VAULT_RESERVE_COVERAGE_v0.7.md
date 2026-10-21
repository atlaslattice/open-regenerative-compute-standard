# Shreddernaut v0.7 — Vault comparison and consumption-equivalent reserve coverage

2026-10-20 | REPORTED IMPORT DELIVERY / CONDITIONAL DOMESTIC RECOVERY MODEL

## Comparison judgment

The recovery network could provide a domestic replenishment capability plus environmental benefits. It is not yet established as a cheaper or more reliable purchase than delivered copper. The 12,000-t Vault shipment is reported as delivered; Shreddernaut's national quantities depend on unverified enriched feed supply, capture, product grades, refinery access and five-year rollout.

[Reuters, October 15, 2026](https://www.kitco.com/news/off-the-wire/2026-10-15/mercuria-delivers-12000-tons-drc-copper-us-project-vault) reports 12,000 metric tonnes of DRC copper delivered through Mercuria and a separate $500m commitment to Vault. That commitment is NOT stated as the price of the shipment; the report reviewed does not disclose shipment purchase terms. Do not calculate $500m/12,000t as copper cost.

## Consumption denominators

Use 2025 estimated consumption from USGS MCS 2026, held constant for comparison, not forecasts of demand five years from now:

| Material | Baseline t/year | Definition/source |
|---|---:|---|
| Copper | 2,200,000 | Apparent primary refined copper + copper from old scrap; [USGS copper](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-copper.pdf) |
| Aluminum | 5,700,000 | Apparent consumption, excludes new-scrap circular flows; [USGS aluminum](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-aluminum.pdf) |
| Ferrous product comparison | 95,000,000 | Apparent steel mill product consumption; [USGS iron/steel](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-iron-steel.pdf) |

These are mass-equivalent comparisons with different commodity definitions, not a claim that every alloy/product grade can substitute for every other. Steel intermediate production may require rolling/fabrication not separately priced in our simple conversion scenario. Aluminum alloy/primary purity requirements and copper cathode specifications need confirmation. National operations also require many materials not covered by this three-metal model.

## If all five-year output is accumulated for reserve

Assume zero withdrawals during buildup, 100% of modeled finished output qualified and delivered to domestic reserve, constant baseline consumption, and no inventory loss. Formula: stored tonnes / (annual consumption/365).

| Material | Selected metal-rich national output over five years | Gross national consumption-equivalent days | Mixed 80%-legacy/20%-selected days |
|---|---:|---:|---:|
| Copper | 1,293,786 t | **214.7 days** | 64.6 days |
| Aluminum | 2,534,220 t | **162.3 days** | 51.6 days |
| Ferrous | 5,068,440 t | **19.5 days** | 8.8 days |

The 12,000-t copper shipment is approximately **2.0 days** on the same broad copper-consumption basis. Selected-case five-year copper output is about 108 such shipments. This compares scale only, not cost or delivery readiness. Against the narrower 1.7m-t/year reported refined-copper-use series, the modeled reserve would equal about 278 days and the shipment about 2.6 days; use the same denominator for both.

These inventories would be accumulated over five years, not available at launch. If 20% rather than 100% of output is reserved, gross coverage becomes about 43 copper days, 32 aluminum days and 3.9 ferrous days. Withdrawals reduce the stored quantity. At 50% additionality, the attributable INCREMENTAL reserve contribution halves; diverting already-recycled supply into a stockpile does not create new national supply.

## Ongoing replenishment at year-five fleet scale

At 5,000 active units:

| Material | Year-five production t/year | Share of annual baseline use | Consumption-equivalent days produced each year |
|---|---:|---:|---:|
| Copper | 497,610 | 22.6% | 82.6 |
| Aluminum | 974,700 | 17.1% | 62.4 |
| Ferrous | 1,949,400 | 2.05% | 7.5 |

This is replenishment rate, not additional coverage to add to the five-year stock without accounting for time. Each percentage requires continued qualified feed, capacity, staffing and operating performance. For a disruption affecting only an imported share, available stocks may cover the shortfall longer than total-consumption coverage; actual drawdown must use disrupted product-specific supply and operating domestic production, not simply divide by headline net import reliance.

## Cost of producing versus buying and holding the reserve

The $2.75bn national build investment does NOT buy the entire five-year metal stockpile. Our commercial ROI assumed finished output was sold, paying processing and operating costs.

Using existing synthetic prices and conversion fees:

- Five-year modeled gross finished-product value: $21.808bn across all three metals.
- Five-year resource cash cost (initial investment + local/shared operation + assumed downstream conversion/freight/assay/selling deductions): $18.202bn.
- Their difference reconciles to the earlier $3.606bn commercial net value.
- If aluminum and ferrous coproducts are SOLD at assumed values, crediting $8.870bn against costs leaves an indicative copper cost of about **$7,213/t**. This is a co-product allocation sensitivity, not a binding delivered copper quote. Those same coproducts cannot also be retained in Vault while counting their sale proceeds as cash.
- If all metals are retained by a public owner, operating and downstream cash costs need funding; metal inventory is an asset rather than sale revenue. If Vault purchases from operators instead, it needs a separate acquisition budget and negotiated prices. Storage/insurance/financing and extra refinery investment are not included.

This supports testing a domestic-recovery procurement route alongside near-term reserve purchases. It does not justify calling a synthetic $7,213/t case an actual saving against an undisclosed shipment price.

## Reproduce

`python3 reserve_coverage.py`

Reads national-summary.json and payback-assumptions.json; writes reserve-coverage-results.json. Checks reconcile gross modeled product value less total modeled cost to national commercial net cash. Baselines above were retrieved from USGS's indexed primary tables; direct PDF fetch was unavailable. Original v0.3-v0.6 files remain unchanged.
