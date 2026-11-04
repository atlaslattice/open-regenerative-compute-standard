# ORCS / New Deal 2.0 — Workbook v0.3 All 13 Tabs (Readable Data Extract)

**Public reference archive of the 13-sheet XLSX text**, generated directly from the accompanying source workbook. It preserves the extracted sheet rows and original source URLs, but flattened export **does not preserve editable Excel formulas, workbook styling, charts or data validation**. Use [source inputs CSV](./three_sector_assumptions_v0_3.csv), [scenario results CSV](./three_sector_scenarios_v0_3.csv), and [reproduction script](./reproduce_three_sector_v0_3.py) for reproducible computational checks. No claim of completed county-by-county ingestion or validated commercial deployment.

---



## Workbook extract: 1 / 13 TABS
TAB NAME: README


index,ORCS / NEW DEAL 2.0  |  Research workbook v0.3,Unnamed: 1,Unnamed: 2,Unnamed: 3
0,,,,
1,Section,How to use / boundary,Status,Supporting file
2,Purpose,"Bottom-up 2030 material recovery, water infrastructure, and grid workforce sensitivity model; NOT a validated jobs forecast",MODEL,ORCS_white_paper_v03.docx
3,Published data,Primary-source national physical/employment data in Evidence + Sources; retain years and units,SOURCED,Evidence
4,Assumptions,Edit BLUE numbers in Scenario_Inputs C:E. Conservative/Central/Accelerated are illustrative combinations.,EDITABLE,Scenario_Inputs
5,Model formulas,"Materials, Water, Grid and Dashboard formulas reference Scenario_Inputs",DYNAMIC,Materials / Water / Grid
6,Geography,"No county-level CBP/QCEW files were ingested; County_Schema is an intake specification, not county output",NOT MODELED,County_Schema
7,Finance,No financing closure shown for the whole $1.5T program. Waste pilot economics include a capital charge.,UNRESOLVED,Finance
8,Employment,Gross supported job-years/roles must NOT be counted as net-new or double-counted across sectors,CAUTION,Dashboard
9,Source vintage,2018 EPA waste data and 2022 EPA wastewater needs are historical; not updated to 2026,HISTORICAL,Evidence
10,Field verification,"Labor coefficients, qualification yields, processing prices and county site requirements await engineering validation",UNVERIFIED,Pilot_Gates
11,Outputs,A separate report and a source register accompany this workbook,COMPLETE,Sources



## Workbook extract: 2 / 13 TABS
TAB NAME: Sources


index,Primary source register and limitations,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
0,,,,,,
1,ID,Publisher / series,Vintage,Source URL,Model use,Limitations
2,EPA_CWNS,EPA Clean Watersheds Needs Survey,2022,https://www.epa.gov/cwns,Water funding denominator,"Needs != appropriations; includes wastewater, stormwater, NPS, decentralized"
3,EPA_CND,EPA C&D material flows,2018,https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/construction-and-demolition-debris-material,Waste material baseline,Historical; 455M tons already next use
4,EPA_MSW,EPA MSW national overview,2018,https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/national-overview-facts-and-figures-materials,MSW generated/landfilled,Historical; material classification distinct from C&D
5,EPA_REI,EPA Recycling Economic Information,"2012, report 2020",https://www.epa.gov/smm/recycling-economic-information-rei-report,1.17 jobs/1000 tons comparison,"Value-chain jobs incl IO effects, not new direct processing jobs"
6,EPA_BIOS,EPA Biosolids Annual Reports,2024,https://www.epa.gov/biosolids/basic-information-about-sewage-sludge-and-biosolids,Sludge baseline,"Reporting subset, dry metric tons"
7,DOE_USEER,DOE U.S. Energy & Employment Report,2026/2025 jobs,https://www.energy.gov/policy/2026-us-energy-employment-report-useer,TDS employment benchmark,TDS includes non-electric fuel subsectors
8,EEI,Edison Electric Institute capital spending,Sept 2025 projection,https://www.eei.org/-/media/Project/EEI/Documents/Issues-and-Policy/Finance-And-Tax/Industry-Capital-Expenditures.pdf,Industry existing capex comparison,All IOU capex; not all grid nor incremental ORCS demand
9,BLS_WATER,BLS Water/wastewater treatment operators,2025/2035,https://www.bls.gov/ooh/production/water-and-wastewater-treatment-plant-and-system-operators.htm,Occupational baseline,"Operators only, excludes construction and engineering"
10,BLS_LINES,BLS Electric line installers,2025/2035,https://www.bls.gov/ooh/installation-maintenance-and-repair/line-installers-and-repairers.htm,Occupational baseline,Projected jobs not realized jobs
11,BLS_ELECT,BLS Electricians,2025/2035,https://www.bls.gov/ooh/construction-and-extraction/electricians.htm,Occupational baseline,Projected jobs not realized jobs
12,BLS_WASTE,BLS NAICS 562 workforce,Sept 2026,https://www.bls.gov/iag/tgs/iag562.htm,Existing waste-sector employment,Includes remediation/collection/disposal; not all recycling
13,USDA,USDA ERS Farm labor,2024,https://www.ers.usda.gov/topics/farm-economy/farm-labor,Agriculture baseline,QCEW covered employees; not all farm work
14,CENSUS_HOUSE,Census New Residential Construction,2025/2026,https://www.census.gov/construction/nrc/index.html,Housing output benchmark,Private completions; excludes some manufactured homes
15,CENSUS_CBP,Census County Business Patterns County File,2023,https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23co.zip,County intake for future optimization,Full county data NOT ingested in this release
16,BLS_QCEW,BLS county employment/wages,2025/2026,https://www.bls.gov/cew/downloadable-data-files.htm,"County employment, wages",Full county data NOT ingested in this release
17,BEA,BEA input-output accounts,Various,https://www.bea.gov/data/industries/input-output-accounts-data,Indirect job accounting follow-up,Do not use IO coefficients for direct net-new employment
18,USA_SPEND,USAspending,Rolling,https://www.usaspending.gov,Procurement contracts follow-up,Award values != paid invoices
19,NREL,NREL REopt,Various,https://www.nrel.gov/analysis/reopt/,Energy site optimization follow-up,Site-specific input required
20,GREET,Argonne GREET,Various,https://greet.anl.gov/,Lifecycle environmental impacts follow-up,Requires per-process verified input



## Workbook extract: 3 / 13 TABS
TAB NAME: Evidence


index,Published U.S. reference observations | preserve units & vintage,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
0,,,,,,
1,Measure,Value,Unit,Year / population,Source,Interpretation / caution
2,C&D generated,600.33,million US short tons,2018,https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/construction-and-demolition-debris-material,"Historical, NOT all landfill"
3,C&D directed to landfill,143.78,million US short tons,2018,https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/construction-and-demolition-debris-material,"Possible interception stream, not all accessible"
4,C&D next-use,455,million US short tons,2018,https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/construction-and-demolition-debris-material,Already directed to reuse/next use
5,MSW generated,292.4,million US short tons,2018,https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/national-overview-facts-and-figures-materials,Separate from C&D; historical
6,MSW landfilled,146.2,million US short tons,2018,https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/national-overview-facts-and-figures-materials,Separate from C&D
7,EPA recycling value-chain jobs per 1000 tons,1.17,jobs per 1000 short tons,2012 observed; 2020 report,https://www.epa.gov/smm/recycling-economic-information-rei-report,"National IO footprint, not marginal direct hires"
8,EPA recycling and reuse jobs,681000,jobs,2012 observed; 2020 report,https://www.epa.gov/smm/recycling-economic-information-rei-report,Existing value-chain jobs
9,EPA Clean Watersheds Needs,630.1,USD billions Jan 2022,2022 needs / 20 year,https://www.epa.gov/cwns,Includes stormwater & nonpoint sources
10,CWNS secondary treatment,66.6,USD billions,2022 needs / 20yr,https://www.epa.gov/cwns,Category of full 630.1B
11,CWNS advanced treatment,83.6,USD billions,2022 needs / 20yr,https://www.epa.gov/cwns,Category of full 630.1B
12,CWNS conveyance systems,151.1,USD billions,2022 needs / 20yr,https://www.epa.gov/cwns,Category of full 630.1B
13,CWNS CSO correction,36.5,USD billions,2022 needs / 20yr,https://www.epa.gov/cwns,Category of full 630.1B
14,CWNS stormwater management,115.3,USD billions,2022 needs / 20yr,https://www.epa.gov/cwns,Category of full 630.1B
15,CWNS nonpoint-source control,94.4,USD billions,2022 needs / 20yr,https://www.epa.gov/cwns,Category of full 630.1B
16,CWNS water reuse,7.7,USD billions,2022 needs / 20yr,https://www.epa.gov/cwns,Category of full 630.1B
17,CWNS decentralized treatment,74.7,USD billions,2022 needs / 20yr,https://www.epa.gov/cwns,Category of full 630.1B
18,CWNS desalination,0.2,USD billions,2022 needs / 20yr,https://www.epa.gov/cwns,Category of full 630.1B
19,Publicly owned treatment works,17544,facilities,2022,https://www.epa.gov/cwns,No uniform facility size
20,U.S. sewage sludge generated,4,million dry metric tons,2024 reported subset,https://www.epa.gov/biosolids/basic-information-about-sewage-sludge-and-biosolids,Different units from waste short tons
21,BLS water/wastewater operators,131000,employees,2025,https://www.bls.gov/ooh/production/water-and-wastewater-treatment-plant-and-system-operators.htm,O&M occupation; -6% projected to 2035
22,EEI utility capex 2025-2029,1100,USD billions,Sept 2025 forecast,https://www.eei.org/-/media/Project/EEI/Documents/Issues-and-Policy/Finance-And-Tax/Industry-Capital-Expenditures.pdf,Includes all IOU capital expenditures
23,2025 USEER TDS jobs (including pipelines),1500000,employees approximate,2025 jobs; 2026 report,https://www.energy.gov/policy/2026-us-energy-employment-report-useer,Not all electricity T&D
24,2025 electric power line installers,131900,employees,2025,https://www.bls.gov/ooh/installation-maintenance-and-repair/line-installers-and-repairers.htm,10% projected 2025-35
25,2025 electricians,821000,employees,2025,https://www.bls.gov/ooh/construction-and-extraction/electricians.htm,9% projected 2025-35
26,Waste management NAICS 562 employment,528000,employees,Sep 2026 provisional,https://www.bls.gov/iag/tgs/iag562.htm,"Existing waste management, not all materials refining"
27,Agriculture/support wage jobs,1180000,jobs,2024,https://www.ers.usda.gov/topics/farm-economy/farm-labor,Existing employment
28,2025 housing completions,1491000,units approx,2025 FRED/Census,https://www.census.gov/construction/nrc/index.html,Annual rate from 2025 mean; rough comparison



## Workbook extract: 4 / 13 TABS
TAB NAME: Scenario_Inputs


index,"Scenario inputs  |  blue cells = editable, not observed",Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
0,,,,,,
1,Assumption,Units,Conservative,Central,Accelerated,Status / rationale
2,Annual productive labor hours,hours/FTE,1800,1800,1800,ASSUMED; may differ by shift / paid vs productive
3,Fully loaded annual labor cost,USD/FTE,70000,70000,70000,"ASSUMED, excludes capital and some contracted overhead"
4,Materials module annual nameplate,short tons/year,250000,250000,250000,"ORCS HISTORICAL planning module capacity, not validated"
5,Waste capital financing rate,annual,0.07,0.07,0.07,ASSUMED project capital pricing
6,Waste capital repayment term,years,20,20,20,ASSUMED project life for annual capital charge
7,Materials throughput in 2030,million short tons/yr,29,72.5,145,ORCS DESIGN scenarios; not measured incremental recovery
8,Materials module utilization,fraction,0.65,0.8,0.9,ASSUMED; module count = ceil(throughput/capacity)
9,Processing direct labor intensity,productive hours/short ton,1.25,0.75,0.45,ASSUMED; NOT measured facility norms
10,Share of processing FTEs net-new,fraction,0.3,0.5,0.6,ASSUMED net addition vs existing recycling workers
11,Qualified output yield,fraction,0.45,0.6,0.7,ASSUMED; high material-dependence
12,Qualified material sale price,USD/qualified short ton,50,85,125,ASSUMED blended revenue; not commodity quote
13,Share of material eligible for tipping,fraction,0.25,0.35,0.5,ASSUMED contract eligibility
14,Tipping fee realized,USD/eligible inbound short ton,25,35,45,ASSUMED not guaranteed revenue
15,Non-labor operating cost,USD/inbound short ton,25,18,20,ASSUMED excludes direct wages and capital charge
16,Capex per materials module,million USD/module,60,45,40,"ASSUMED; includes systems, not land/site acquisition"
17,Water capital expenditure in 2030,USD billions/year,5,15,30,"ILLUSTRATIVE ORCS annual project pace, not appropriated"
18,Water direct construction job-years,jobs per USD million invested,2,3.5,5,ASSUMED; no verified national direct coefficient
19,Water construction jobs net-new share,fraction,0.25,0.45,0.6,"ASSUMED, includes substitution adjustment proxy"
20,Water incremental permanent O&M,FTE,500,2500,7500,"ASSUMED, compare BLS 131k existing operators"
21,Grid field capital expenditure in 2030,USD billions/year,15,40,80,ILLUSTRATIVE annual addressable project pace
22,Grid field construction job-years,jobs per USD million invested,1.5,2.5,3.5,ASSUMED; excludes equipment mfg counted separately
23,Grid construction jobs net-new share,fraction,0.25,0.4,0.55,ASSUMED incrementality
24,Grid incremental permanent O&M,FTE,1000,5000,15000,ASSUMED
25,County industrial facilities,sites,3144,3144,3144,ORCS target; no individual site validation
26,Workers per fully activated factory,people/site,240,240,240,ORCS earlier scenario 4 teams; 330 sensitivity elsewhere
27,2030 activated factory fraction,fraction,0.25,0.6,1,"ASSUMED rollout, not completed sites"
28,Housing units by 2030,units,3000000,3000000,3000000,"ORCS program TARGET, not delivery forecast"
29,Housing selling price,USD/home,200000,200000,200000,ORCS TARGET scope not yet reconciled
30,Core program financing,USD,1500000000000,1500000000000,1500000000000,ORCS 30-year envelope; cash availability schedule unresolved
31,Core financing illustrative rate,annual,0.05,0.05,0.05,ILLUSTRATIVE fixed amortization rate
32,Core financing term,years,30,30,30,ORCS financing planning term
33,Materials new-diversion share,fraction,0.15,0.25,0.35,"ASSUMED, distinct from upgraded existing streams"
34,Materials existing-stream upgrade share,fraction,0.65,0.55,0.5,ASSUMED; no new landfill diversion credit
35,Materials legacy landfill mining share,fraction,0.2,0.2,0.15,ASSUMED; physical availability unproven
36,EPA REI value-chain coefficient,jobs per 1000 tons,1.17,1.17,1.17,PUBLISHED EPA benchmark; NOT direct new jobs
37,CWNS nationwide need,USD billions,630.1,630.1,630.1,PUBLISHED 2022 national 20yr estimate
38,CWNS years,years,20,20,20,PUBLISHED EPA planning period
39,EEI existing industry annual capex,USD billions/year,220,220,220,"DERIVED 1100/5, includes all IOU capex; not ORCS incremental"
40,Jobs goal in 2030,paid jobs,3000000,3000000,3000000,ORCS TARGET; not inferred from model



## Workbook extract: 5 / 13 TABS
TAB NAME: Materials


index,Materials recovery | independent physical / financial ledger,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
0,,,,,,
1,Measure,Unit,Conservative,Central,Accelerated,Interpretation
2,Gross inbound throughput,short tons/year,29000000,72500000,145000000,All 3 streams combined; not net new diversion
3,New waste diverted,short tons/year,4350000,18125000,50750000,Credit landfill diversion only for this volume
4,Existing recovery upgraded,short tons/year,18850000,39875000,72500000,Qualified upgrade is not newly diverted from landfill
5,Legacy landfill mining,short tons/year,5800000,14500000,21750000,"Site-specific risk, contaminant and recovery cost"
6,Flow balance (should be zero),short tons,0,0,0,Zero indicates allocation sum 100%
7,Required operating modules,sites,179,363,645,"250k/yr nameplate, corrected for assumed utilization"
8,Direct processing labor hours,hours/year,36250000,54375000,65250000,Excludes separately modeled transport/installation
9,Direct processing FTEs,FTE,20138.88888888889,30208.333333333332,36250,Gross supported operating roles; assumes throughput exists
10,Potentially net-new FTEs,FTE,6041.666666666667,15104.166666666666,21750,Fraction is an assumption; verification via payroll
11,EPA REI job value-chain comparison,"supported jobs, NOT direct",33930,84825,169650,"Historical economy-wide REI attribution, do not add"
12,Qualified material produced,short tons/year,13050000,43500000,101500000,Must pass independent product test and contaminant screens
13,Gross qualified material revenue,USD/year,652500000,3697500000,12687500000,ASSUMED sale pricing and full offtake
14,Gross tipping-fee revenue,USD/year,181250000,888125000,3262500000,Only contracted eligible stream should generate fees
15,Total gross revenue,USD/year,833750000,4585625000,15950000000,Excludes public benefits/carbon offsets
16,Non-labor operating cost,USD/year,725000000,1305000000,2900000000,Excludes direct payroll and capex
17,Direct processing payroll,USD/year,1409722222.2222223,2114583333.3333333,2537500000,Only direct waste-processing workforce
18,Operating contribution / EBITDA proxy,USD/year,-1300972222.2222223,1166041666.6666667,10512500000,"Before financed capital charge, taxes, site/land and some overhead"
19,Capital cost of required modules,USD,10740000000,16335000000,25800000000,ASSUMED per-module capex; no existing plant reuse
20,Illustrative annual capital charge,USD/year,1013780022.4825659,1541908442.016081,2435337484.1759963,Equivalent annualized 20yr cost at 7%
21,Operating contribution after capital charge,USD/year,-2314752244.704788,-375866775.34941435,8077162515.824003,Not equity IRR or net income; key cash test
22,Post-charge value per inbound ton,USD/inbound ton,-79.81904292085477,-5.184369315164336,55.7045690746483,Negative => sensitivity case does not close financially



## Workbook extract: 6 / 13 TABS
TAB NAME: Water


index,Water & wastewater | project job-years vs permanent operations,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
0,,,,,,
1,Measure,Unit,Conservative,Central,Accelerated,Interpretation
2,Annual water capital execution,USD/year,5000000000,15000000000,30000000000,"Modeled 2030 project expenditure, not guaranteed funding"
3,Share of EPA 20yr average annual need,fraction,0.15870496746548168,0.476114902396445,0.95222980479289,Comparison ONLY; EPA needs do not equal appropriations
4,Direct construction job-years / annual FTE,job-years/year,10000,52500,150000,"Assumed direct coefficient, not empirical"
5,Potentially net-new construction jobs,FTE/year,2500,23625,90000,Reallocation/displacement adjustment assumed
6,Added permanent O&M positions,FTE,500,2500,7500,Contrast with 131k existing BLS operators
7,Total supported positions,FTE/year,10500,55000,157500,Construction job-year occupancy + added O&M
8,Potentially net-new positions,FTE/year,3000,26125,97500,Not equal to net national employment effect
9,Direct construction payroll proxy,USD/year,700000000,3675000000,10500000000,"Wages are within capital spend, not additional to it"
10,Direct construction labor share of spend,fraction,0.14,0.245,0.35,Implausible values signal model failure
11,O&M addition / BLS operator baseline,fraction,0.003816793893129771,0.019083969465648856,0.05725190839694656,"BLS projection is declining, so requires evidence"
12,4-year capital pace relative to EPA needs,fraction,0.03174099349309634,0.095222980479289,0.190445960958578,Not investment delivered by the program yet



## Workbook extract: 7 / 13 TABS
TAB NAME: Grid


index,Grid modernization | field construction & long-term maintenance,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
0,,,,,,
1,Measure,Unit,Conservative,Central,Accelerated,Interpretation
2,Annual grid construction program spend,USD/year,15000000000,40000000000,80000000000,Hypothetical addressable annual executed projects
3,Share of EEI projected industry-wide capex,fraction,0.06818181818181818,0.18181818181818182,0.36363636363636365,EEI includes generation too; NOT incremental opportunity
4,Direct field-construction job-years,job-years/year,22500,100000,280000,Assumed direct; excludes transformer factory positions
5,Potentially net-new construction FTE,FTE/year,5625,40000,154000,"Fraction assumed, not measured"
6,Additional ongoing maintenance FTE,FTE,1000,5000,15000,New long-run positions only
7,Total supported positions,FTE/year,23500,105000,295000,Annual site/construction activity + O&M
8,Potentially net-new positions,FTE/year,6625,45000,169000,Subject to county/occupational constraints
9,Direct construction payroll proxy,USD/year,1575000000,7000000000,19600000000,Within construction spend
10,Direct payroll share of contract spend,fraction,0.105,0.175,0.245,Coefficient should be qualified by contractor bids
11,New site workers as share of 2025 line workers,fraction,0.04264594389689159,0.3032600454890068,1.1675511751326764,Not same exact occupational mix; stress test only



## Workbook extract: 8 / 13 TABS
TAB NAME: Dashboard


index,ORCS Model v0.3 | Illustrative 2030 employment bridge,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
0,,,,,,
1,Result,Units,Conservative,Central,Accelerated,Evidence / important qualification
2,Materials gross operating FTE,FTE/year,20138.88888888889,30208.333333333332,36250,Modeled direct processing only
3,Water gross supported positions,FTE/year,10500,55000,157500,Annual construction job-years + O&M
4,Grid gross supported positions,FTE/year,23500,105000,295000,Annual construction job-years + O&M
5,THREE SECTORS | gross supported,FTE/year,54138.88888888889,190208.3333333333,488750,Gross annual roles/job-years not newly created jobs
6,Materials potentially net-new,FTE/year,6041.666666666667,15104.166666666666,21750,New share assumed
7,Water potentially net-new,FTE/year,3000,26125,97500,New share assumed
8,Grid potentially net-new,FTE/year,6625,45000,169000,New share assumed
9,THREE SECTORS | potentially net-new,FTE/year,15666.666666666668,86229.16666666666,288250,Still not a verified national employment effect
10,County facilities activated by 2030,sites,786,1886.3999999999999,3144,Target deployment not site specific
11,Factory workforce at assumed staffing,FTE,188640,452735.99999999994,754560,Unverified staffing and financing; not net-new qualified
12,Gross sector roles + factory work,positions,242778.88888888888,642944.3333333333,1243310,Combines construction job-years and factory positions
13,Upper bound net-new + ALL factory new,positions,204306.66666666666,538965.1666666666,1042810,Only as bounding assumption; no factory demand modeled
14,Remaining jobs to reach 3M (optimistic),jobs,2795693.3333333335,2461034.8333333335,1957190,Remaining workstreams must be separately modeled
15,Waste finance surplus / shortfall,USD/year,-2314752244.704788,-375866775.34941435,8077162515.824003,Excludes some overhead and land
16,Annual water + grid construction spend,USD/year,20000000000,55000000000,110000000000,Annual gross projects; not all new program financing
17,County industrial network gross payroll,USD/year,13204800000,31691519999.999996,52819200000,Without revenue proof and before other sectors



## Workbook extract: 9 / 13 TABS
TAB NAME: Finance


index,Financing / housing constraints | NOT a solved 30-year cash flow,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
0,,,,,,
1,Test,Unit,Conservative,Central,Accelerated,Caveat
2,Core 30-year financing envelope,USD,1500000000000,1500000000000,1500000000000,Envelope not cumulative project revenues
3,Illustrative fully drawn annual debt service,USD/year,97577152620.41484,97577152620.41484,97577152620.41484,"Assumes entire sum drawn at start, simplifying unrealistic draw schedule"
4,Annual full 3M payroll at $70k loaded,USD/year,210000000000,210000000000,210000000000,Recurring cost not financed permanently by construction loans
5,Housing gross sales value at target price,USD,600000000000,600000000000,600000000000,Sales != profit; excludes site work definition & working capital
6,Average housing completions over 2027-30,homes/year,750000,750000,750000,Assumes uniform completions; realistic ramp would be backloaded
7,Annual 2025 Census housing completions,homes/year,1491000,1491000,1491000,"Published housing output benchmark, excludes HUD-code homes"
8,ORCS housing pace / 2025 nationwide,fraction,0.5030181086519114,0.5030181086519114,0.5030181086519114,New production demands large new regional workforce
9,Proposed enabling authority (not additive),USD,200000000000,200000000000,200000000000,180B liquidity/risk + 20B standards; allocation unresolved
10,Refinery $100B/year x30 years conflict,USD,3000000000000,3000000000000,3000000000000,Shows $3T > 1.5T; requires separate authority/period
11,Financing remaining after 4yrs grid+water spend,USD,1420000000000,1280000000000,1060000000000,"Not finance closure: excludes factories, housing, procurement etc."



## Workbook extract: 10 / 13 TABS
TAB NAME: 2030_Ramp


index,Annual ramp / deployment dependencies | proportions are assumptions,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5,Unnamed: 6
0,,,,,,,
1,Year,Ramp fraction,Conservative gross 3,Central gross 3,Accelerated gross 3,Central potentially net-new,Cumulative facility activations central
2,2027,0.15,8120.833333333333,28531.249999999996,73312.5,12934.374999999998,282.96
3,2028,0.35,18948.61111111111,66572.91666666666,171062.5,30180.20833333333,660.2399999999999
4,2029,0.65,35190.27777777778,123635.41666666666,317687.5,56048.95833333333,1226.1599999999999
5,2030,1,54138.88888888889,190208.3333333333,488750,86229.16666666666,1886.3999999999999



## Workbook extract: 11 / 13 TABS
TAB NAME: Sector_Targets


index,Original sector target ledger | not forecasts,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4
0,,,,,
1,Sector,Original 2030 jobs target,Derivation status,Current finding / next task,Job overlap risk
2,Distributed manufacturing / factory operations,1000000,Not demand-validated,"3144 sites x 240 workers = 754,560 at full activation; 330/site = 1,037,520.",Factory production workers vs recycling equipment manufacturing
3,"Grid construction, line work & field modernization",400000,Partial scenario only,Grid direct field supported roles modeled in Grid; net-new still assumed.,"Electricians in housing, wastewater and other sectors"
4,"Waste mining, collection, sorting, refining",350000,Partial scenario only,Material processing direct FTE modeled; value-chain benchmark not additive.,"Waste logistics, downstream manufacturing and materials upgrading"
5,Housing construction and installation,350000,Dependency only,3M units by 2030 requires 750k units/year 2027-2030 average; costs incomplete.,Factory printed components vs site labor
6,Wastewater and water recovery,225000,Partial scenario only,CWNS includes categories beyond wastewater and no procurement schedule.,"General civil construction, shared operators"
7,"Agriculture, nutrient recovery, food systems",225000,Legacy ORCS physical model,Conditional 5.87TWh and nutrient recovery require feedstock/cost validation.,Organic feedstock from waste ledger
8,"Logistics, maintenance and equipment services",200000,Unmodeled,Must de-duplicate logistics embedded in each modeled sector.,"Materials tonnage transport, grid field contractors"
9,"Training, specialized teaching and certification",100000,Unmodeled,Need trade-by-trade instruction hours and legally qualified staff.,Already counted operational supervisors
10,"Independent auditing, compliance, oversight",75000,Unmodeled,"Need audit evidence schedule, sampling plan, credible fees/funding.",Procurement QA under other categories
11,Program management and digital operations,75000,Unmodeled,"Need county-level task volume, privacy, cyber, support budgets.",Corporate overhead in modeled sector OPEX



## Workbook extract: 12 / 13 TABS
TAB NAME: County_Schema


index,"County data schema | intake specification, NOT filled county estimates",Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4,Unnamed: 5
0,,,,,,
1,Field,Units / datatype,Best source,Required for county benefit gate,Coverage status,Use / validation
2,county_fips,5-character string,2023 Census CBP + TIGER,Yes,NOT IMPORTED,Stable administrative key incl county-equivalents
3,county_name / state,text,Census CBP,Yes,NOT IMPORTED,Not a location claim without source file
4,existing_manufacturing_jobs,"workers, NAICS31-33",Census CBP / BLS QCEW,Yes,NOT IMPORTED,Establishment disclosure and suppression caution
5,existing_waste_jobs,"workers, NAICS562",BLS QCEW,Yes,NOT IMPORTED,Avoid assuming capacity from count alone
6,industrial_available_sqft,qualified vacant sq ft,Local property / permits,Yes,FIELD SURVEY,Factory rehabilitation feasibility
7,water_capital_need,2022 USD,EPA CWNS local project records,Yes,NOT IMPORTED,Sewershed often crosses county boundary
8,grid_verified_projects,USD with geospatial location,Utility IRP/PUC / projects,Yes,NOT IMPORTED,Utility jurisdiction not equivalent to county
9,accessible_waste_tons,short tons/year by material,County/state waste authority,Yes,FIELD SURVEY,Net new landfill diversion vs upgraded flows separate
10,available_labor_pool,qualified FTE and apprentices,BLS LAUS/QCEW/ACS,Yes,NOT IMPORTED,Commuting cross-county flows needed
11,housing_units_needed,"units, size, tenure",ACS + local permitting,Yes,NOT IMPORTED,Avoid conflating need with buyer demand
12,water_stress,source-specific index,USGS + state water data,Yes,NOT IMPORTED,No assumed water offsets
13,grid_capacity,MW available / outage stats,EIA + utility,Yes,NOT IMPORTED,Net site power balance and load interconnection
14,industrial_access,freight distance and cost,USDOT & engineering,Yes,FIELD SURVEY,Logistics economics
15,local_benefit_commitment,audited USD / annual output,Project contract + county ledger,Yes,PROPOSED,Requirement to deliver something concrete
16,community_consent,public record id / process,Local consultation,Yes,PROPOSED,Cannot replace actual zoning/permits
17,contractual_demand,annual offtake volume and price,Executed contracts,Yes,NOT IMPORTED,No revenue credit without counterparty
18,environmental_permits,license ids / expiration,EPA and state permit portals,Yes,NOT IMPORTED,Stop gate for non-compliance



## Workbook extract: 13 / 13 TABS
TAB NAME: Pilot_Gates


index,Validation gates | proposed test program,Unnamed: 1,Unnamed: 2,Unnamed: 3,Unnamed: 4
0,,,,,
1,Gate,Pass evidence,Reject / redesign trigger,Owner / source,Status
2,G0 Data quality,"Traceable units, vintages and primary source links; county joins and duplicates audited",Major untraceable inputs or overlapping waste volumes,Independent data audit,OPEN
3,G1 Feedstock availability,"Signed collection agreements, tested contamination/quality and monthly volume",Unavailable compatible feedstock or >20% uncontrolled mass discrepancy,Materials / regulators,OPEN
4,G2 Qualification,Third-party qualified materials and end-product acceptance,"Failed safety, chemistry, structural or product certification",Testing / NIST / buyers,OPEN
5,G3 Financial closure,Contracted revenues and auditable 20-30yr source-of-funds,No debt coverage or funded public-service operating appropriation,Independent underwriter,OPEN
6,G4 Labor calibration,"Measured hands-on hours by task, contractor payroll and hours by NAICS/SOC",Job claims based only on hypothetical multipliers,Labor statistician,OPEN
7,G5 Net-new hiring,Matched establishment/worker baseline + comparable control counties,Displacement or transfer counted as net-new jobs,Payroll review,OPEN
8,G6 Environmental,"Verified water, power, emissions and contaminated material disposal",Permit violation or externalized damage exceeds safeguards,Environmental auditor,OPEN
9,G7 AI RCT,"AI-agent pilot vs conventional tool with output quality, hours and retention",No incremental value or measurable negative safety/retention,Labor research team,OPEN
10,G8 Community benefit,"County-signed benefits, published meter and realized service data",No county-level realized benefit for funded project,Community benefit board,OPEN
11,G9 Scaling dependency,"2027-2030 skilled trade, housing, factory equipment and utility capacity reconciled",Delayed critical path makes 2030 delivery infeasible,Program PMO,OPEN
12,G10 Financing conflicts,$200B enabling allocation and refinery modernization authority reconciled,Unfunded overlapping commitments exceed financing envelope,Treasury/capital markets,OPEN