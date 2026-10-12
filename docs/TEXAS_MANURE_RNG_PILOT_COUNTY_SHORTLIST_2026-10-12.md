# Texas livestock manure → RNG | county-first pilot screen
**Date:** 2026-10-12 · **Status: PRE-FEASIBILITY / REPORTED + MODELED + UNKNOWN · NO VERIFIED PROJECT OFFTAKE OR REALIZED CREDIT**

## Executive assessment
**First target: the Moore–Hartley dairy corridor; alternative: Castro–Parmer; comparator: Erath.** These are *county clusters for field diligence*, not confirmed project sites, not a comparison of individual farms, and not an operational digester proposal. Dairy concentration is evidenced by federal milk-market records; manure production/capture fractions, pipelines and site permitting have *not* been verified at farm level.

## Primary datasets and evidentiary constraints
1. USDA NASS [Texas 2025 Agriculture Overview](https://www.nass.usda.gov/Quick_Stats/Ag_Overview/stateOverview.php?state=texas), showing **705,000 Texas milk cows** (Jan 1 2026), **2.54 million cattle on feed** (Jan 1 2026), and **1.13 million hogs** (Dec 1 2025). Cattle on feed already included in total 12.1m head of cattle; do not double-count.
2. USDA Federal Milk Market Administrator's [October 2025 bulletin](https://www.dallasma.com/file_map/order/2025/OCT25BUL.pdf) lists September 2025 Texas milk receipts by county. These are marketed milk pounds/producer counts, **not herd counts or manure generation**. It identifies Moore (270,984,277 lb; 16 producers), Hartley (263,633,553 lb; 19), Castro (163,029,912 lb; 15), Parmer (126,512,533 lb; 15), Erath (119,327,550 lb; 37), and Deaf Smith (107,199,925 lb; 15).
3. USDA NASS [April 2025 Cattle on Feed report](https://www.nass.usda.gov/Statistics_by_State/Texas/Publications/Current_News_Release/2025_Rls/spr-cattle-on-feed-04-2025.pdf) reports 2.38m cattle on feed in the Northern High Plains then, ~89% of Texas feedlot inventory. That is 2025 geography, not a measured October 2026 farm location list.
4. EPA [AgSTAR projects](https://www.epa.gov/agstar/projects-and-opportunities), [farm digester case histories](https://www.epa.gov/agstar/anaerobic-digester-project-profiles), and [design / permitting guidance](https://www.epa.gov/agstar/building-operating-biogas-recovery-systems): existing digesters, methane handling, historical operational successes and failures.
5. [EPA-derived July 2025 state project count compiled by EFI](https://efiusa.com/digester-atlas) lists Texas **9 operating, 6 under construction, 3 shut down**. This count is secondary and time-bound, **not independently refreshed for Oct 2026**. EPA profiles include **Huckabay Ridge (Texas), shut down**, illustrating that feedstock aggregation, plant operations and economics can fail. Avoid promising bankability just because cattle concentration is high.
6. Railroad Commission of Texas [GIS pipeline viewer](https://www.rrc.texas.gov/resource-center/research/gis-viewer) and [pipeline permits/mapping](https://www.rrc.texas.gov/pipeline-safety/permitting-and-mapping/). The GIS is approximate, not an interconnection feasibility certificate or a substitute for 811 or site engineering.

## County-cluster shortlist with explicit ranking basis

| Screening order | County/cluster | Documented evidence | Why screen | Main unresolved veto |
| --- | --- | --- | --- | --- |
| **1A** | **Moore + Hartley**, northern Panhandle | USDA September 2025 combined **534.62 million lb of marketed milk** / 35 producers | Highest two-county reported milk concentration; compact region for comparing dairy co-digestion and multiple farm capture options | Unknown herd/manure management, lagoon baseline, gas line pressure and distances; Ogallala water stress; nutrient loading |
| **1B** | **Castro + Parmer**, southern Panhandle | USDA combined **289.54 million lb** / 30 producers | Dairy plus broader feedlot/crop symbiosis hypothesis; digestate nutrient destination and adjacent manure handling worth screening | Collection solids, water rights, transport miles, soil salt/P balances and existing offtakes |
| **2** | **Deaf Smith + surrounding feedlots**, Panhandle | USDA **107.20 million lb** dairy receipts; Northern High Plains feedlot concentration reported by NASS | Candidate for *separate feedlot manure processing*, noting dry scraped manure behaves differently from dairy slurry | Digester feedstock moisture/process economics may favor compost/pyrolysis over AD; no assumed collection fraction |
| **3** | **Erath**, North-Central Texas | USDA **119.33 million lb milk** / 37 producers; EPA Huckabay Ridge TX historical failure | Research comparator for smaller-scale facilities and transport; investigate why former project shut down before any new hub | Existing contracted feedstock; farm distribution and prior project failure modes unknown |

**Not a claim about farm readiness, zoning, gas-line adjacency, county-by-county total manure or rankings on net profitability.** Dairy milk receipts strongly correlate with economic dairy activity but cannot be converted to cows at individual farms without yield and marketing-system adjustments.

## Corrected statewide synthetic mass balance
Inherited public screening assumptions from [Texas RNG resource screen](./TEXAS_MANURE_TO_RNG_RESOURCE_SCREEN_2026-10-12.md): dairy 705k head × 55 kg wet manure/day × 75% collection × **18 m3 CH4/t wet collectable**; feedlot 2.54m × 25 kg/day × 55% × 13; hogs 1.13m × 5 kg/day × 65% × 12. Those 75%/55%/65% collection assumptions **are not measured Texas fractions**; methane yields also unvalidated. Results:
- Dairy: gross wet **14.153m metric tons/yr**, screening collected **10.615m t/yr**, methane **191.1m m3/yr ≈ 6.75 Bcf/yr**.
- Feedlot: gross wet **23.178m metric tons/yr**, collected **12.748m t/yr**, methane **165.7m m3/yr ≈ 5.85 Bcf/yr**.
- Hogs: gross wet **2.062m metric tons/yr**, collected **1.34m t/yr**, methane **16.1m m3/yr ≈ 0.57 Bcf/yr**.
- Sum: **~39.39m t gross wet**, **~24.70m t assumed collectable**, **~372.9m m3/yr**, **~13.17 Bcf gross methane/yr**. At **95% methane recovery × 95% annual uptime**, illustrative clean methane becomes **~11.88 Bcf/yr**. Not metered feedstock or actual pipeline RNG.
- Earlier conversation/chart reported dairy ~7.96 Bcf and hog ~0.13 Bcf, inconsistent with the stated assumptions. **These are corrections, not revised livestock statistics.** See executable values in the underlying cohort model; round discrepancies to 2 decimal places.

## Hypothetical single-site dairy module (not a farm census)
A screened farm/cluster with **5,000 dairy cows**, 55 kg/head/day, 75% recovered manure, 18 m3 CH4 per wet tonne:
- 206.25 wet metric tons/day entering digester; **3,712.5 m3 CH4/day**; **~47.9 million ft3/year** gross methane (0.0479 Bcf/y).
- After 95% recovery and 95% uptime: **~43.2 million ft3/y** delivered-clean-methane equivalent (0.0432 Bcf/y), **before pipeline gas specification, interconnection pressure restrictions and regulatory certification**.
- At 0.03393 MMBtu/m3 CH4 lower heating value, ~41,494 MMBtu per year after losses, **approximately**; a hypothetical $6/MMBtu suggests **~$249k/year gross commodity value**, not revenues under a signed tariff nor ROI. Clean methane sales conventionally use HHV, so this is simply a consistent LHV engineering screen. It *excludes* any environmental/renewable-fuel credit value and avoided costs. No tipping, nutrient, water or carbon credits assumed.
- **Core reality:** methane commodity value alone may not justify capital/operating costs. Farmer avoided manure handling costs, genuine lagoon methane mitigation, credit eligibility, co-digestion, and contracted energy offtake would need independent validation.

## Candidate decision gates — stop before commercial promises
1. **Feedstock:** obtain **farm/operator consent** and anonymized producer cluster data, herd inventory, collection method, hydraulic load and volatile solids; verify 90%+ regular collection if using EPA suitability screen, rather than treating 75% hypothetical capture as a guaranteed farm yield.
2. **Methane emissions counterfactual:** document uncovered lagoon, stockpile, pasture, or dry stack management and measured baseline emissions; if original manure is aerobic/dry, avoided methane credit may be far smaller; control digester / upgrader leakage.
3. **Logistics:** calculate feedstock movement distances, water additions, fiber/bedding, pump energy, onsite heat balances, seasonal shutdown and pipeline/compressor/interconnect pressure; **no pipeline distance asserted here**.
4. **Digestate:** nutrients remain; conduct nitrogen, phosphorus, salts, pathogens, residual contaminants tests; legal land application capacity/seasonality and discharge restrictions; avoid double-sale of gas and digestate benefits.
5. **Contracts/economics:** secure feedstock, long-term qualified RNG buyer, credit eligibility, utility interconnection tariff and independent construction quote. Stress test zero environmental credits, -25% gas yield, +30% CAPEX, and leakage.
6. **Community:** air/water odor controls, environmental justice, water drawdown, transparency to neighbors, public benefit and stop-work triggers.
7. **Credibility:** name qualified independent engineering reviewer; publish calibrated source receipts and permissioned redacted project data before describing anything as bankable.

## Proposed 90-day study (no funding secured)
**First 30 days:** obtain county-level Texas dairy/feeding facility inventories and actual operator handling sample; ask EPA AgSTAR for dated Texas digester database and failure-case history; map public infrastructure only at general area scale, no presumed connection.
**Days 31–60:** sample 3–5 voluntary facilities for volatile solids / BMP / nutrient chemistry, assess baseline manure treatment and project consent; route to AD vs compost vs thermal alternatives according to actual feed.
**Days 61–90:** compare 3 alternatives for one consenting cluster—covered lagoon or on-farm digestion, manure aggregation with common upgrading, and non-AD nutrient/fiber/compost option—using owner bids, gas-quality constraints, water, local soil capacities and independent engineering sign-off.

**NEXT DECISION: perform a consenting-site screen starting Moore/Hartley, not pitch national supply estimates to investors.** A named site cannot be selected from published county data alone.

## Public repository status
Purely desktop/browser reproducible research at this stage. Related tracked blocker: [GitHub #5](https://github.com/atlaslattice/open-regenerative-compute-standard/issues/5). **NO realized commercial credits, operational claim, official partnership or field access.**


## Unsubsidized single-module breakeven sensitivity — purely illustrative
For the 5,000-head screening farm, ~41,494 MMBtu LHV/year is the hypothetical **clean methane energy after assumed 95% upgrader recovery and 95% uptime**. At illustrative $6/MMBtu LHV, energy commodity revenue is ~$249k/year, not a buyer bid. To demonstrate why commodity value alone can be inadequate, assume a **12% annualized capital charge** (hypothetical capital recovery inclusive of return and amortization; not a real financing offer) plus synthetic annual OPEX:

| Hypothetical CAPEX | Hypothetical annual OPEX | Annual cash requirement | Breakeven commodity value ($/MMBtu LHV) |
| ---: | ---: | ---: | ---: |
| $5 million | $250,000 | $850,000 | ~$20.49 |
| $10 million | $500,000 | $1,700,000 | ~$40.97 |
| $20 million | $1,000,000 | $3,400,000 | ~$81.94 |

These numbers are **not estimates of actual Texas digester construction or operating cost**. They omit all tax, depreciation, environmental credit/LCFS/RIN qualification, nutrient co-product and avoided manure-handling cashflows. The sole purpose is to reveal the required verified contracting/credits or lower-cost shared infrastructure for bankability. Do not combine renewable-energy certificate, RIN, LCFS and avoided-methane claims without checking eligibility, ownership and additionality.

Executable (standard-library only) model: [Texas manure RNG calculator](../tools/texas_manure_rng_screen.py), including explicit livestock inventory cohort assumptions and self-checks. To test in an appropriately configured Python 3 environment: `python tools/texas_manure_rng_screen.py --self-test`. **The code has been published and read back but has not been confirmed as executed through GitHub CI.**
