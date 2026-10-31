# ORCS Grid Intelligence 1.0 — U.S. Workforce and Job-Year Scenario, 2026-10-31

**Status:** RESEARCH SENSITIVITY ONLY. Not federal workforce forecast, approved funding, contracts, vacancies, union commitments, or guaranteed net-new employment. **No jobs have been created by the scenario itself.**

## 1. Employment baseline and comparison

- DOE 2026 U.S. Energy and Employment Report: 2025 **825,000** people working in electric-power transmission and distribution; **744,000** traditional electric T&D, **32,000** smart grid, **24,100** other grid modernization and **21,800** microgrids. These are existing employment stocks, not new project hiring. Source: https://www.energy.gov/documents/2026-useer-national-report .
- BLS 2025 electric line installers/repairers: **131,900** employed, median annual cash wage **$95,320**, projected **13,600 net additional jobs** 2025–2035 in baseline projections. Wages alone do not include benefits, employer taxes, per diem, training, indirect labor overhead or the compensation of engineers/software developers. Source: https://www.bls.gov/ooh/installation-maintenance-and-repair/line-installers-and-repairers.htm .
- NREL JEDI convention: construction employment is an FTE **job-year**, not a permanent position; operations FTEs are counted annually. Supply-chain and induced jobs must be defined separately. Source: https://www.nrel.gov/analysis/jedi/results.html .

## 2. Reproducible explicit labor arithmetic

For each **capital program**:

```
domestic_supported_job_years = capex_USD * domestic_labor_compensation_share / fully_loaded_employment_cost_USD_per_year
average_FTE_during_buildout = domestic_supported_job_years / construction_years
```

This method allocates a *share of all purchased project goods and services* to **domestic worker labor costs across onsite + domestic supplier and engineering workers**. It is **not** BLS net job additions, a JEDI input-output multiplier, a payroll audit or a claim every dollar of domestic factory procurement is wages. Reject double counting if procurement quotes already include labor under another program.

Digital systems, same physical scope as [national digital-grid model](national_grid_ai_scenarios.py):

| Digital track | Capital | Domestic labor share (assumed) | Loaded $/FTE-y (assumed) | Capital job-years | Average capital-supported FTE/y, 10-y build |
|---|---:|---:|---:|---:|---:|
| Conservative | $12.49B | 25% | $150,000 | ~20,814 | ~2,081 |
| Reference | $38.77B | 35% | $130,000 | ~104,369 | ~10,437 |
| Upper | $65.70B | 45% | $120,000 | ~246,361 | ~24,636 |

These are alternate programs, NOT additive alternatives. Differences in labor-share and compensation are sensitivity settings, not validated supplier estimates. Includes software engineering, local field installation/retrofit, data science, grid sensing, cybersecurity, equipment/sensor manufacturing and integration *only to extent already financed within this CAPEX*.

**Digital ongoing operations:** Existing [national economic model](national_grid_ai_scenarios.py) assumes annual OPEX equal to **5% of program capital**, i.e. $0.624B / $1.938B / $3.285B at full deployment. If **60%** of OPEX is domestic payroll + burden (assumed) and the same loaded costs apply, ongoing annual supported FTEs would be ~**2,500 / 8,950 / 16,425** once fully rolled out. These are gross **operational roles supported**, not necessarily permanent new hires; maintenance, vendors, software and cyber staffing must avoid double counting. OPEX is **already counted in financial model** and must not be booked a second time as independent capital.

Separate possible physical capital tranches (not included in the $38.77B digital-grid CAPEX):

| Physical track | Capital | Assumed domestic labor share | Assumed fully loaded $/job-y | Supported job-years | Build period; annual average |
|---|---:|---:|---:|---:|---:|
| Replace oldest 55% of 70M distribution transformers | **$308B** | 30% | $140,000 | **660,000** | 20y; **33,000** |
| Underground 25,000 critical miles + harden 100,000 overhead miles | **$158.3B** | 30% | $140,000 | **339,214** | 20y; **16,961** |
| Replace **all** 70M transformers **instead of** oldest 55% | **$560B** | 30% | $140,000 | **1,200,000** | 20y; **60,000** |

Physical prices ($8k/unit installed, $3.25M/mile underground, $770k/mile hardening) are previous **illustrative screening prices** rather than nationwide procurement quotes. In particular, 25,000 miles may not be the most hazard-effective selection; and 70M in 20y is **3.5M/yr**, a demanding industrial ramp. Compare with actual natural fleet renewals: baseline activity is not all incremental. Undergound vs hardened line mileage counts cannot overlap; exclude any sensor and controller costs already included in those physical contracts from digital CAPEX.

### Integrated reference and 20-year workforce shape

**Reference digital ($38.77B) + oldest 55% transformers ($308B) + 125,000 priority line miles ($158.3B)** = **$505.07B combined capital** over distinct scopes, before tax/finance, manufacturing capital, training programs and common-cost reconciliation.

Capital-associated gross job-years: **104,369 + 660,000 + 339,214 = 1,103,583**. Twenty-year average = **~55,179** FTE/y, although digital installation finishes after first ten years. On top, digital operations jobs ramp linearly with commissioning over first ten years to ~8,950 FTE/y then remain at that level. Approximating first-ten-year OPEX employment at 55% mature level and second-ten-year at 100%, 20-year average gross operations FTE ~= **6,930**. Thus **roughly 62,000 gross full-time equivalents per year averaged over 20 years**, or **~1.24 million job-years across capital and ongoing operations**, subject to the overlap controls.

**Full replacement instead of oldest tranche:** replace $308B / 660k job-years with $560B / 1.2M job-years, keeping same 20y schedule. Total initial capital = **$757.07B**, gross 20-year average = ~**89,000 FTE/y** including phased digital OPEX. This is a larger hypothetical program, not a recommended national schedule or incremental number of jobs. **Do not add** full-fleet and oldest 55% tranches.

With domestic labor compensation assumptions, $505B reference CAPEX implies **~$153.5B in fully-loaded domestic labor cost over phased buildout**, *not* pure take-home wages, local net value added or tax revenue. Wage portion is substantially lower than loaded cost after benefits/overhead. For a geographically credible county-level estimate, use actual eligible local contractors, union agreements, state labor rates, suppliers, apprenticeship capacity and import shares.

## 3. What job categories and how to preserve gain

**Construction and electric trades:** lineworkers, qualified electricians, relay technicians, substation builders, underground civil crews, fiber technicians, fiber splicers, thermal-monitoring installers, inspection crews, traffic management and safety professionals.

**Domestic supply and manufacture:** distribution transformers, cores, electrical steel, copper/aluminum conductor, sensors, meters, reclosers, SiC devices, switchgear, fiber, enclosures, precision machining, power-electronics test, repair/remanufacturing. **Transformer 3.0 remains experimental**; no assumed fabrication jobs from an uncertified product.

**Professional and software:** power-systems and protection engineers, dispatch analysts, OT security, NERC compliance, distributed resource integration, grid simulation, digital-twin and AI forecasting, utility data stewardship, independent auditors, QA, environmental and fire-risk specialists.

**Continuing positions:** after initial build, operations include field repair, calibration, resilience drills, OT cybersecurity, asset analytics and scheduled technology refresh. But some automation replaces existing manual meter-reading and inspection tasks; report gross positions separately from workforce displacement and actual counterfactual employment.

**Training and labor constraint:** electrical-worker apprenticeships and qualified journeymen, certification testing, field safety, HV switching and licensing are gating constraints. A higher project job-year number is NOT automatically feasible without scaling training and domestic supply capacity.

## 4. Employment reporting rules

1. Disclose **job-years / average FTE during a specified build period / steady operational FTE / actual net job change** separately; no permanent-job claim from a temporary construction headcount.
2. Distinguish **on-site direct**, **domestic equipment and other supply-chain**, and **induced household-consumption** employment; current figures include only first two via labor-share arithmetic and exclude induced jobs.
3. Show **incremental hiring over baseline** and worker reallocation separately. Existing maintenance and scheduled replacement jobs do not become newly created simply because the same work is in a national plan.
4. Explicitly disclose **domestic versus imported content**; shifting supply-chain manufacturing into U.S. plants can create domestic employment while potentially changing costs.
5. Apply state/county-specific wage scales and procurement instead of a universal flat 50-state multiplier; compare with NREL JEDI / state input-output model only after contracts and sourcing are known.
6. Protect workforce: certified training, safe fatigue limits, prevailing-wage / collective bargaining as applicable, independent whistleblowing and auditing, no unsupervised AI disabling certified protection.
7. No additive public financing/job credit from DOE SPARK, DPA declarations, or unrelated grants unless actual funded scopes are identified and net of overlap.

**Evidence gate:** Replace labor compensation shares, average employment cost, unit prices and phasing with vendor and union/local workforce quotes. Monitor worker retention, time-to-credential, trainee graduation, domestic manufacturing output, labor productivity, injuries and actual jobs by project and state.
