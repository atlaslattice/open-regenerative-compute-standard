# ORCS v3.4 — Measured U.S. Solar Baseline, Biosolar Eligible Upgrades, Industrial Inference Value
2026-10-15 | APPEND-ONLY | PUBLIC WORKING RESEARCH | ZERO REALIZED CREDIT

## Correct all previous technical vs measured baseline ambiguity
EIA March 20 2026 statement confirms *ACTUAL 2025 generated solar electricity* 296 TWh US utility-scale + 93 TWh small-scale = **389 TWh/year**. Source https://www.eia.gov/TODAYINENERGY/detail.php?id=67367 . These are 2025 measured/estimated actual U.S. generation figures, not potential.
NREL 2016 technical potential is **1,432 TWh/year if all suitable U.S. rooftops were equipped**, from 1,118 GW of PV and 8.13 billion m² suitable roofs; genuinely published detailed engineering estimates, **NOT ACTUAL generated electricity**. Source https://www.nrel.gov/grid/news/press/2016/24662 , dataset https://data.nlr.gov/submissions/121 . Existing PV fleet should not be double-counted inside technical potential.

## Biosolar technology
UTS/Bradfield 2026 field data: vegetated roof under actual photovoltaic solar arrays produced **+11.1% PV electricity on average during four-month Australian summer** and up to 23.25% in extremely hot intervals. NOT verified yearly U.S. uplift or ground-mounted plant benefit. Meaning of 'bio-solar' here is rooftop PV over rooftop vegetation, not a new photosynthetic electric cell. Source https://bradfield.city/news/first-buildings-biosolar-roof-sets-new-standard-climate-resilient-cities .

## Retrofit sensitivity applied to actual 389TWh baseline
Formula: incremental_TWh = 389 TWh (measured annual U.S. solar generation) × fraction of generation coming from physically eligible biosolar retrofits × hypothesized full-year performance uplift. This is a valid SCENARIO formula, not evidence of actual retrofits.
At 10% eligible: assumed 5%, 8%, 11.1% uplift -> **1.945, 3.112, 4.318 TWh annual extra**.
At 25% eligible: **4.863, 7.780, 10.795 TWh**.
At 50% eligible: **9.725, 15.560, 21.590 TWh**.
At 100% eligible: **19.450, 31.120, 43.179 TWh**, mathematical-only overreach; most utility solar is ground-mounted, not biosolar roof eligible. **Small-scale solar only 93TWh** baseline × 5–11.1% = 4.65–10.32 TWh/year if 100% eligible, which it is not. If retrofitted eligible fraction is 25% ×8% -> **1.86TWh** extra.
Long-run 10% NREL roof technical potential *new build*: 143.2TWh conventional PV plus a conditional 15.90TWh uplift at hypothetical 11.1% annual biosolar; do not present the full 159.1TWh as retrofit uplift to existing PV. For roofs not equipped with PV, most energy gain is **new solar panel generation**, not biosolar enhancement.

## Industrial solar-site inference: measured use and limitations
2026 peer-reviewed field study with one year data from two Korean grid-connected PV arrays used SVR with data preprocessing; detected **11.6% first-year power loss due to potential-induced degradation**, confirmed by IR/electroluminescence. This is measurable *loss discovered*, not a proven 11.6% energy recovery after AI intervention. https://doi.org/10.1016/j.seta.2026.105030
2026 peer-reviewed review confirms solar forecasting, maximum power-point tracking, fault classification, predictive maintenance and SCADA as AI use-cases but urges real-world cost/outcome benchmarking, not automatic uplift. https://doi.org/10.1016/j.meadig.2026.100027
At photovoltaic plants inference nodes can be **rack, edge appliance or shared regional cluster**; proof should compare local energy draw vs additional electricity delivered, net of telemetry and WAN. Existing MPPT/inverter/cloud-monitoring baseline matters. 'Inference increases efficiency' means reducing preventable outages, soiling, mismatch/curtailment and storage dispatch losses, NOT making panels fundamentally more efficient in the thermodynamic photovoltaic conversion sense. Plant must be allowed to act on recommendations, maintain inverter OEM warranties and dispatch rights.
USER THESIS: ROI of distributed industrial inference may exceed ROI of hyperscale training *in near-term at the margin* if process savings/avoided costs per kWh of local compute outweigh deployment; cannot universally assert inference > training without matched capital, benefit and workload comparisons.

## Industrial AI evidence from China
MIIT 2025 released results for 230 designated excellence smart factories: **22.3% higher average production efficiency, 50.2% lower defect rates, 20.4% lower carbon emissions, 28.4% shorter development cycles** in reported program. These are operator/government aggregated program metrics, not causal attributable only to AI or on-site inference and not directly electricity savings. https://www.miit.gov.cn/xwfb/gxdt/sjdt/art/2025/art_70c95052e16e44eb9bb49eae85f71e70.html .
Early 2026 China MIIT reports 35,000+ basic, 8,200+ advanced, 500+ excellence, 15 pioneer-level smart factories, >70% of pilot/factory operational scenarios using AI in the pioneer set, average 29% improved productivity and 47% fewer defects in selected pilot group. Selected top performers have strong selection effects and no per-site kWh savings receipt. https://www.miit.gov.cn/xwfb/bldhd/art/2026/art_4ba01aa6d2f54ced8ba3490ea4fb52c4.html .
Oct 9 2026 China policy includes further industrial AI pilot bases, risk controls and an explicit warning against capital bubbles; announcement is a policy direction not quantified savings. Reuters https://www.reuters.com/world/asia-pacific/china-issues-guidelines-new-productive-forces-including-ai-2026-10-09/ .
May 2026 Nature Communications Sustainability paper modeled AI deployment on China's power system, potential **5.8–15.6% of 2060 nationwide electricity**, research forecast not current measured AI energy savings. https://www.nature.com/articles/s44458-026-00080-4 .

## Operational edge solar + BESS proposal
PV/vegetation on eligible roof (site selection & structural load), local weather/panel sensor data, edge inference for maintenance and irradiance forecast, battery forecast/dispatch optimization human-approved and grid-operator coordinated, 4/8h BESS, flexible industrial demand, reliable mains/gas for long-duration resilience. PV generation improvements (biosolar), uptime restoration (AI), and load shifting (BESS) must be measured in **separate mutually exclusive value ledgers**. Reserve safety controllers outside LLM autonomy.
Capacity adequacy depends location/hours: real annual +TWh does not guarantee +MW during evening PJM scarcity. Use PJM-region rooftop subset rather than all 389 TWh U.S. solar, weather/horizon, interconnection, BESS MW, MWh, usable capacity and net round-trip losses.

## Actions & evidence gates
1. From EIA small-scale + utility-level generation, decompose facility types and roofs by state/ZIP. Ground arrays are not green roofs.
2. Measure 12-month comparative PV performance by climatic zone before adopting 11.1% annual uplift.
3. Audit existing PUE/controller software, edge energy consumption, cybersecurity & third-party OT approval.
4. Simulate 1,4,8,72 hour reliability and require hard battery/electrical interconnect evidence.
5. No implied deployment, public program adoption or realized revenue; draft PR not merged.