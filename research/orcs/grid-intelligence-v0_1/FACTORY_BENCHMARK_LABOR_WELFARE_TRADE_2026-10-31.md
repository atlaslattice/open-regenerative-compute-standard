# ORCS — Transformer Factory-Cell Benchmark + US Labor, Safety-Net and Trade Ledger

**2026-10-31 | Economic/factory screening v0.1 | SOURCE-TRACED public statistics / ASSUMED simulated processes / NOT REAL FACTORY TESTS.**

Related projects: [national grid AI model](WHITE_PAPER.md) · [five-year national mobilization](FIVE_YEAR_STANDARDIZATION_TRAINING_AND_POWER_CONDITIONING_2026-10-31.md) · [fully/partly printed robotics research](ADDITIVE_FACTORY_MILLION_WORKER_DOMESTIC_PIVOT_2026-10-31.md) · [reproducible benchmark script](factory_cell_fiscal_trade_benchmark.py).

## 1. US people potentially available for work — as of Oct 31 2026

U.S. BLS Sept 2026, released October 2:
- Labor force **170.262M**, officially unemployed **7.109M**, U-3 **4.2%**.
- **5.790M** people outside labor force **currently want a job**; not BLS unemployed due to job-seeking or current availability definitions. **12.899M** = 7.109M + 5.790M, mutually exclusive groups, NOT automatically employable/available for ORCS.
- **4.5M** already employed part-time for economic reasons, wanting full-time hours; **1.9M** long-term unemployed are SUBSET of 7.109M. Distinct part-timers may benefit from new/full-time jobs but cannot be reclassified unemployed.
- **105.292M** people not in labor force, but mostly **DO NOT** self-report wanting a job. They cannot be treated as an idle labor reserve.
Source: https://www.bls.gov/news.release/archives/empsit_10022026.htm .

## 2. Budget and safety-net baseline (not cash freely available)

| Program / measure | Year | Amount | Accounting boundary |
|---|---|---:|---|
| Regular state UI benefits | Calendar 2025 | $34.4B | DOL ~5.3M *annual beneficiaries*, not 5.3M concurrent; employers' UI payroll taxes fund regular benefits |
| Federal SNAP | Fiscal 2025 | $101.7B | USDA; many recipients are children or employed-household members |
| SSI federally administered payments incl state-administered supplement | Calendar 2025 | ~$65B | SSA 7.4M recipients in Dec 2025; age and disability benefits not unemployment subsidy |
| Medicaid federal government | Fiscal 2025 | ~$668B | CBO, acute/long-term health program, many children/older adults/disabled/working adults |
| **Federal income-security category** | Fiscal 2025 | **$397B** | CBO includes SNAP, unemployment insurance, SSI, refundable tax credits, families; NEVER ADD constituent lines to this total |
| Federal Medicaid, projected | Fiscal 2026 | $708B | CBO outlook (not FY25) |

Sources: https://oui.doleta.gov/unemploy/DataDashboard.asp ; https://www.ers.usda.gov/data-products/charts-of-note/115611 ; https://www.ssa.gov/policy/docs/statcomps/ssi_asr/2025/index.html ; https://www.cbo.gov/publication/62105 .

**Core economic constraint:** 7.1M BLS unemployed != UI recipients, and many low-income recipients are already employed. Wage gains, reduced benefit payouts, employer UI premiums, employer/employee tax receipts and net value added are DIFFERENT measures, with different budget/government beneficiaries. Reduced benefits may also be reduced household income, not pure economic gains. Preserve SNAP/SSI/Medicaid as ZERO assumed savings until individual/household eligibility models and the counterfactual are established.

## 3. US trade baseline (2025 actual, 2026 latest monthly)

BEA 2025: goods **imports $3.4384T**, goods exports $2.1975T => **goods deficit $1.2409T**; services surplus $339.5B => combined **goods/services deficit $901.5B**. Goods/services total imports $4.3338T. **$1.9T is NOT the documented 2025 international trade deficit**: the Congressional Budget Office forecast a **~$1.9T federal FY2026 budget deficit**, which is a different accounting concept. August 2026 BEA/Census provisional monthly combined trade deficit $105.6B ($136.6B goods less ~$31B services surplus), NOT an annual final result. Sources: https://www.bea.gov/news/2026/us-international-trade-goods-and-services-december-and-annual-2025 ; https://www.census.gov/foreign-trade/current/ ; https://www.cbo.gov/publication/61882 .

**Industrial demand is huge but not a guaranteed domestic order book**: BEA reports about $1.1T **capital-goods imports** in 2025. High-potential ORCS transition lanes: certified transformer cores and windings, electrical steel, copper/aluminum, motors, pumps, water treatment hardware, robotics parts/servos/controllers, switchgear, inverters/rectifiers, industrial cooling, selected mechanical parts. For each product use verified customs HTS 8–10 digit category, current U.S. production capacity, domestic full BOM, imported input leakages, costs, warranty and replacement output. No policy preference is asserted.

## 4. Three factory-cell architectures: INVENTED input assumptions, reproducible arithmetic

**The physical proof gate is the SAME for all 3:** specified identical primary/secondary voltage, kVA, phase, impedance, dielectric impulse, partial discharge, thermal and short-circuit, repairability, modern DOE equipment-type efficiency, fault/arc safety and field acceptance. **No actual unit is manufactured or tested by this script.** Product physical performance is intentionally held as **UNKNOWN**, not an assumed 97/99% figure.

Each factory figure counts direct estimated purchased BOM, machine activity/printing, robots, labor, postprocess and factory QA per attempt, divided by assumed accepted yield; not utility installation, factory initial capex, data center capacity or policy incentives.

| Assumed architecture | Per-unit qualified yield | Effective additive occupancy | Invented direct factory cost per accepted unit | Stations at 7.7M qualified units/y |
|---|---:|---:|---:|---:|
| Automated conventional lamination/winding | 98% | 0h | **$2,918** | No additive cells |
| Hybrid robotic/additive (selected shapes) | 94% | 4h | **$3,298** | **5,344** additive cells |
| Maximum-additive research concept | 85% | 18h | **$5,847** | **26,592** additive cells |

At assumed $100/print-hour, base hybrid needs print time to fall to **~0.43 hours per accepted attempt equivalent** to match conventional cost with all else held unchanged. Alternatively achieve lower material/assembly cost, better yield, lower print cost or materially greater life/functional system value. **This is a hypothesis-sensitivity, not proof additive cannot win**. Count 365-day 24/7 machines with assumed 70% OEE and process yield, stagger five-day human schedules with ~5.25 FTE per round-the-clock post. Quote six independent suppliers and 100/1,000/10,000 qualifying units before committing to million-unit claims.

**Validation plan**: A0 same functional spec/BOM and hazardous-process site permits; A1 printed vs stamped/cast/wound test coupons with comparable conductivity, magnetic core loss under actual flux/frequency, tensile/fatigue, insulation withstand, partial discharge; A2 100 50-kVA lab product builds for repeatable process and quality, qualification yield with independent failures; A3 1k units multi-vendor with accelerated electrical/thermal aging; A4 10k unit factory pilot with uptime, OSHA safety, customer sites and full life-cycle loss; A5 full cost per certified operational kVA, actual installed price and warranties. Operators trained, competent and human accountable. **Can't claim actual benchmark measurement without physical vendors, devices and labs.**

## 5. Net additional employment vs public fiscal return sensitivity

At **$60,000 annual cash wage per NET NEW worker** and 15.3% employer + employee statutory Social Security/Medicare payroll taxes, *subject to wage/coverage law*, 1M genuine net additional workers create ~$60B gross wages and up to **$9.18B/year combined employer/employee payroll tax collections** (transfer between private accounts/governments, not an incremental social benefit to add again to wages).

Use latest regular UI total **$34.4B / 5.3M annual beneficiaries = $6,490/year per annual recipient**. If 25% of NET NEW workers would otherwise receive UI and the program averts 50% of their expected baseline annual UI spell benefits, illustrative UI savings **$811M/year per 1M jobs**. This is not $34.4B available or a forecast, and states' UI experience/premiums may change.

For net-new **manufacturing** employees only, use ASSUMED **$300,000 annual factory gross sales output per worker**, 35% of that output replacing imported finished products and incremental imported raw/intermediate inputs equal 25% of displaced gross value; *conditional static trade-balance change* is **$78,750 per new manufacturing worker/year**. Factory output and value added are not the same; trade balance may respond via exchange rates, consumption and exports; no GDP gain asserted.

| Hypothetical net new workers economy-wide | Of which new manufacturing | Annual wage bill | Combined payroll receipts | UI saved if assumed counterfactual | Conditional direct goods-balance change |
|---|---:|---:|---:|---:|---:|
| 300,000 | 100,000 | $18B | $2.75B | $0.24B | $7.88B |
| 1,000,000 | 300,000 | $60B | $9.18B | $0.81B | $23.63B |
| 2,000,000 | 800,000 | $120B | $18.36B | $1.62B | $63B |

**No savings from SNAP/SSI/Medicaid in base model; no income taxes or corporate taxes credited.** These are conditional illustrative sensitivities, not claims the grid program can add 1–2M *net new* jobs. Prior 299k/year gross FTE supported by a hypothetical 5-year capital rollout includes existing/reallocated jobs and must NOT be added to an assumed 1M net new. The 1M unique trainee target does not establish 1M employed FTE or 1M extra jobs.

## 6. Testable national factory pivot rule

The original grid contract creates startup sales, but a permanent manufacturing market must be won independently. After the initial 5-year peak, require a continuously refreshed 10-year order book by class, residual grid replacements, export opportunity, domestic industrial demand, volume-dependent qualification and tool changeover losses. A factory line becomes a new robotics, pump, motor or power-electronics line only after separate equipment-cost, reliability and product demand tests. Avoid claiming zero imports during transition if robot semiconductors, sensors, machine tools or feedstocks remain foreign.

**Policy design is an alternate institutional structure for public-benefit financing; it isn't an announcement of new federal nationalized assets or a stance on a political party.** Independent procurement and physical verification determine social/fiscal cost effectiveness.

## 7. Reporting and falsification

Always show **(1)** newly trained people, **(2)** actual qualified entrants, **(3)** gross job-years supported, **(4)** demonstrably net additional employment, **(5)** domestic worker earnings and net value added, **(6)** reduced UI payments by counterfactual, **(7)** social service benefits preserved, **(8)** merchandise import substitution **net** of imported content, and **(9)** public/utility lifecycle cash flow. Do not add wages, benefits, payroll tax revenue, factory output and GDP as if independent national surplus. If certified units don't lower cost or improve performance, or domestic factories can't meet demand profitably, the claimed benefit must be zeroed until validated.

**Next evidence gate:** RFQs and test-lab plans from actual automated-conventional, hybrid additive/robotic and maximum additive factories, alongside specific HTS trade categories and state registered-apprenticeship partners.
