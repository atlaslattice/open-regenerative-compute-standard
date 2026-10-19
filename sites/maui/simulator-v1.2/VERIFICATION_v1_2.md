# Maui ORCS v1.2 — execution and limitations record

Verified at 2026-10-19T13:57:42.484926+00:00. Status: runnable advisory prototype; simulated physical outcomes; no realized project benefit.

## Verified execution

- Original v1.1: nine existing unit tests passed before changes.
- v1.2: 19 unit tests passed, covering input rejection, food allocation, battery state/energy balance across all eleven scenarios, islanded export prohibition, critical-load priority, annual CHP energy normalization, forecast time/unit/freshness rejection and provider failure fallback.
- Eleven scenarios each produced 30 annual rows and 168 hourly rows.
- Eleven local HTTP checks passed: dashboard HTML, catalog, feed status, comparisons, annual and hourly endpoints, bad scenarios/allocations, negative inputs, and POST rejection.
- Dashboard JavaScript passed Node syntax check. Browser rendering/interaction was not verified because no browser executable is installed.
- All five adapters completed successful public requests; raw bytes, URLs, retrieval times, HTTP codes, byte lengths and SHA-256 digests are preserved in live/raw. Normalized records have separate receipts and hashes.
- The weather-connected hybrid example used 165 forecast irradiance hours and 3 synthetic fallback hours. Electrical loads, conversion yields and plant sizes remain hypothetical in both cases.

## Corrections relative to v1.1

1. An islanded grid can neither accept exports nor supply imports; excess onsite production is curtailed after battery charging.
2. Constant representative-week CHP power now uses annual electricity divided by 8760 hours. The previous 7500-hour divisor overstated continuous-week output.
3. Critical demand receives available power first. Remaining critical and flexible shortfalls are reported separately; no reliability certification is implied.
4. CLI and HTTP use the same forecast freshness/schema/unit/time gate. Cached LIVE_RETRIEVED labels age to STALE_CACHE on read.
5. Forecast rows start at the current HST hour. Synthetic fallback follows the same local clock. No seven-day forecast is projected through the 30-year cashflow.
6. Core model validation rejects negative sizes, nonfinite values and impossible feedstock allocations across CLI and HTTP.
7. Dashboard controls now derive defaults from the actual resolved scenario instead of duplicating hardcoded numbers.
8. Financial incompleteness is explicitly returned in annual-model responses and shown on the dashboard.

## What these runs say

The storm scenario retains unmet critical demand even with the hypothetical PV/battery system. Battery size alone does not demonstrate disaster sufficiency; verified load shedding, reserve policy, backup generation, fuel availability and storage would need modeling.

Default financial screening remains negative. It excludes unverified fuel/compost sales, compute revenue, grid export remuneration and public benefits. It also omits important costs and uses annual power netting, so it cannot rank investment options defensibly. Negative results do not establish that an optimized Maui network is infeasible.

## Outstanding accounting/engineering work

- Replace annual netted electricity costs with calibrated 8760-hour imports, exports, curtailment and interconnect constraints.
- Split reuse, desal, HTL, AD, sorting, hauling, land, pipe, grid, finance, insurance, taxes, maintenance and replacement costs; resolve the unused maintenance-capex assumption.
- Model approved seasonal water demand, treatment and RO losses, brine chemistry, nutrient/pollutant residuals and critical water storage.
- Track AD digestate, HTL gas/aqueous/char, moisture and ash; current food-allocation conservation is not full elemental conservation.
- Validate parcels, distances and hazards for Central Maui, Waikapū, Mā‘alaea, Lahaina, North Shore and Kīhei. No current site approvals or utility interconnections are asserted.
- Expand beyond five connected public feeds; utility meters, FIRMS, stream/aquifer conditions, road/port/fuel telemetry, ecological observations and long-term climate ensembles remain unwired.
- Complete a 2056 terminal checkpoint. Current annual cashflow ends in 2055.
- Live provider content and licenses were not independently re-audited; receipt success is evidence of retrieval and schema compatibility only.

## Reproduction and provenance

Run `python -m unittest discover -s tests -v` and `python verify.py`. The latter overwrites generated local results only. Raw receipts remain unchanged unless a new feed refresh is explicitly requested. Verify hashes in results/model_input_hashes.json and live/raw/*.receipt.json. Time-dependent labels and forecast selection naturally change when rerun later; offline physical scenario values are deterministic under the same inputs.
