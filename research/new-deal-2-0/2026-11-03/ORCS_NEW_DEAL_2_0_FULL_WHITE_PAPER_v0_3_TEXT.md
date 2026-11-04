# ORCS / New Deal 2.0 — Original v0.3 White Paper (Complete Readable Text)

**November 3, 2026 | Source-document text edition.** Extracted from the complete 10-page Word source (the independently rendered PDF may paginate differently). Table spacing, charts and typography may be altered by extraction. The underlying claims, source boundaries and model limitations are preserved. For convenient cross-reading, consult the [structured public research digest](./ORCS_NEW_DEAL_2_0_EVIDENCE_MODEL_v0_3_PUBLIC.md) and [CSV scenarios](./three_sector_scenarios_v0_3.csv). *Not a substitute for the original editable Excel workbook.*

---

## Original document page 1

                             ORCS / NEW DEAL 2.0        |   RESEARCH WORKING PAPER           |   NOVEMBER 2026

RESEARCH & RECONCILIATION SERIES

ORCS / NEW DEAL 2.0
National Industrial Capacity, Workforce and County-Benefit Model
Evidence-backed update • Model version 0.3 • 3 November 2026
Three priority sectors: materials recovery, water/wastewater modernization, and grid fieldwork. Integrated
dependencies: county factories, housing, agriculture, training, community-positive computing nodes and 30-year
financing.

Prepared for cross-model technical review, including DeepSeek. Scenario calculations are illustrative and
distinguish public-source evidence from program assumptions.




               Figure 1. Three-sector 2030 workforce sensitivity (NOT a validated projection).

PROVENANCE KEY
 Class                                 Meaning                               What this release contains

 PUBLISHED                             Data reported by public agencies or   EPA, BLS, DOE, USDA, EEI and
                                       original industry organizations       Census benchmarks
 DERIVED                               Reproducible arithmetic with          Scenario workbook and annual
                                       disclosed inputs                      debt-service calculations
 ASSUMED                               Chosen scenario inputs requiring      Labor intensity, unit prices, new-
                                       empirical calibration                 hire rates, investment pace
 TARGET                                Program objective that is not yet     3M paid jobs, 3M homes, county
                                       economically supported                participation
 OPEN                                  Missing datasets, verification or     County inventory, procurement,
                                       financing closure                     pilot measurements




                              Research scenario — not independently validated • 1

## Original document page 2

                                ORCS / NEW DEAL 2.0         |    RESEARCH WORKING PAPER           |   NOVEMBER 2026

Executive findings
The national program is wider than transformers or grid construction. The three previously underrepresented
sectors have independently measurable physical and investment baselines: approximately 600.3 million U.S. short
tons of 2018 construction/demolition debris, $630.1 billion in EPA 2022 water-quality infrastructure needs over 20
years, and substantial electric-utility capital investment. None of these quantities is equivalent to addressable,
funded, incremental ORCS demand. [S1–S4, S7]

    Finding                     Conservative                    Central                     Accelerated

    Three-sector gross          54,139                          190,208                     488,750
    annual roles/job-years
    Potentially net-new         15,667                          86,229                      288,250
    roles (assumed shares)
    Waste-processing            179                             363                         645
    modules
    Waste margin after          $-2.31B                         $-0.38B                     $+8.08B
    capital charge



The central case supports about 190,000 annual operating roles/construction job-years in these three sectors; about
86,000 are potentially net-new under explicitly assumed hiring fractions. These are not measured new jobs. They
do not justify extrapolating to a three-million-worker national workforce. The waste model fails to cover its
illustrative financed capital charge in the central case.

The companion spreadsheet provides editable assumptions and traceable formulas. It intentionally does not
fabricate county-by-county results: the full BLS QCEW and Census CBP county records, local permits, feedstock
compositions, utility project portfolios and site surveys have not been ingested.


Decision register
     Keep three million active paid jobs by 31 December 2030 as a TARGET, not a base-case forecast. Do not report
      3M as verified output.
     Treat every county as entitled to a measurable benefit assessment, not necessarily a 100,000 sq. ft. factory.
     Do not count the same recycled ton, construction worker, utility contract or AI-saved hour in multiple ledgers.
     Advance pilots only after qualification, unit-economics, funding and community-benefit gates pass; major
      national scale-up is conditional.


1. Boundaries, units and source vintage
EPA reports 600.33M short tons of construction and demolition (C&D) debris generated in 2018, including 143.78M
short tons landfilled and about 455M directed to next use. EPA separately reports 292.4M short tons of municipal
solid waste (MSW) generated and 146.2M landfilled in 2018. These totals produce a historical combined generation
of 892.73M short tons, but this is not current 2026 waste supply, not all diverted material, and not all accessible for
ORCS. [S1–S2]

EPA reported $630.1B in January-2022-dollar water-quality infrastructure needs over a 20-year window, including
wastewater treatment, pipe conveyance, stormwater, nonpoint-source control and decentralized systems. Calling
the full figure wastewater-only spending would be incorrect. [S3]

The 2026 DOE USEER describes about 1.5M workers in transmission, distribution and storage in 2025, but this
broad category includes pipelines and fuels. The 2025 USEER reported 732,500 workers specifically in traditional

                                 Research scenario — not independently validated • 2

## Original document page 3

                              ORCS / NEW DEAL 2.0         |    RESEARCH WORKING PAPER              |   NOVEMBER 2026

electric transmission/distribution in its earlier snapshot. EEI projected approximately $1.1T in 2025–2029 investor-
owned utility capital expenditure; this includes generation and other uses, not a dedicated ORCS grid spending
pool. [S7–S8]


2. Methods and employment definitions
Three-sector modeling uses a 2030 annual snapshot. Conservative, central, and accelerated scenarios vary both the
amount of activity and operational parameters. They are alternative assumptions, not statistical confidence
intervals or model posterior predictions. No national probability weights are assigned.

Materials direct processing FTE = annual inbound short tons × productive labor hours per ton ÷ 1,800 annual
productive hours. Water and grid construction FTE/job-years = annual executed project dollars (in millions) ×
assumed direct job-years per $1M. Incremental O&M is added separately. Potentially net-new hires apply a
separate assumed fraction to construction/processing labor; existing employment is not automatically new.

A continuing series of temporary projects can sustain a long-lived construction workforce. We therefore
distinguish project job-years, annual job-year occupancy, continuing employment, permanent O&M roles, and
demonstrated net-new national labor demand. A 2029 construction job-year and a 2030 job-year may be held by
the same worker; they cannot be counted as two simultaneous jobs.

All labor coefficients, material prices and recovery yields used in this report are scenario inputs awaiting field
calibration. Historic EPA value-chain job multipliers are presented only as a cross-check, not added to direct ORCS
FTEs.


3. Materials recovery and legacy landfill mining
The recovered ORCS concept targeted 145M short tons/year of annual material interception at mature deployment,
or the nameplate equivalent of 580 modules each processing 250,000 tons/year at 100% utilization. Once
uptime/utilization is modeled, the required module count is higher: 645 modules at 90% utilization for 145M actual
annual tons. The 145M figure is a capacity TARGET, not a measured net incremental diversion. [ORCS internal
scenario]

 2030 input / result           Conservative                   Central                      Accelerated

 Inbound throughput (M         29.0                           72.5                         145.0
 short tons)
 Operating modules             179                            363                          645
 Direct process labor          1.25                           0.75                         0.45
 (hours/ton)
 Direct processing FTE         20,139                         30,208                       36,250
 Gross product + fee           $0.8B                          $4.6B                        $15.9B
 revenue
 Module capital                $10.7B                         $16.3B                       $25.8B
 Post-financed-capital         $-2.31B/yr                     $-0.38B/yr                   $+8.08B/yr
 result



The accelerated case is financially positive only because it assumes relatively high qualified-material prices, high
yields, faster automated sorting, substantially better contracted tipping revenue, and lower capital cost per
module. These assumptions cannot be considered verified. The central case generates positive pre-capital
operating contribution but fails after annualizing module capex under the illustrative 7%/20-year capital charge.

                               Research scenario — not independently validated • 3

## Original document page 4

                              ORCS / NEW DEAL 2.0        |    RESEARCH WORKING PAPER             |   NOVEMBER 2026




 Figure 2. Waste recovery annual contribution after illustrative financed module capital charge; dollars in
                                                 billions.
Materials throughput is divided among new landfill diversion, upgraded existing recovery streams and legacy
landfill mining. The three streams are mutually exclusive in the workbook; only the first should be credited as new
ongoing landfill diversion. Environmental credit for mining legacy landfill material must be site-specific.

EPA’s Recycling Economic Information Report estimates 681,000 recycling/reuse jobs in 2012, or 1.17 jobs per 1,000
recycled tons. Applied mechanically to 145M tons, this is 169,650 jobs supported across the value chain—but the
coefficient is based on national historical input–output accounting and must NOT be interpreted as 169,650 new
ORCS direct processing jobs. [S4]


4. Water and wastewater: construction and operations
The EPA 2022 CWNS sum is $630.1B, reported over 20 years, or an arithmetic average of $31.505B/year in January
2022 dollars. It is a statement of needs, not a confirmed 2030 appropriation. The report models $5B/$15B/$30B of
annual ORCS-addressable executed projects in 2030. [S3]

 2030 water variable          Conservative                   Central                     Accelerated

 Annual executed              $5B                            $15B                        $30B
 projects
 Direct job-years per $1M     2.0                            3.5                         5.0
 Annual direct                10,000                         52,500                      150,000
 construction job-years
 Incremental permanent        500                            2,500                       7,500
 O&M
 Potentially net-new          3,000                          26,125                      97,500
 positions



These construction job-year intensities are assumptions, not validated water-sector estimates. The central case
implies approximately 24.5% of capital outlay goes to the modeled directly employed construction workforce at
$70,000 fully loaded per job-year; other capital pays for materials, equipment, subcontracted functions and
margins. Labor coefficients must be replaced with bid and payroll evidence before pilot authorization.




                               Research scenario — not independently validated • 4

## Original document page 5

                               ORCS / NEW DEAL 2.0         |    RESEARCH WORKING PAPER            |   NOVEMBER 2026

BLS counted about 131,000 water/wastewater treatment operators in 2025 and projected a 6% decline through
2035. This does not establish declining water-construction employment; it does caution against claiming large
permanent gains solely from new plant operators. [S5]

EPA biosolids reporting covering applicable facilities estimated about 4M dry metric tons of sludge in 2024. These
quantities must not be directly added to MSW/C&D short tons without preventing overlap and converting units.
[S6]


5. Grid infrastructure: distinct from transformer fabrication
Grid fieldwork includes utility construction, line installation, substations, protection/control systems, resilience
improvements, inspections and operations. It should not be derived from transformer factory staffing. The
scenarios apply 1.5/2.5/3.5 assumed direct construction job-years per $1M of 2030 field spending to $15B/$40B/$80B
annual executed spending. These intensities are not empirical industry averages.

 2030 grid variable            Conservative                    Central                     Accelerated

 Annual executed field         $15B                            $40B                        $80B
 projects
 Direct construction job-      22,500                          100,000                     280,000
 years
 Added maintenance             1,000                           5,000                       15,000
 positions
 Potentially net-new           6,625                           45,000                      169,000
 positions



BLS counted about 131,900 electrical power-line installers/repairers and 821,000 electricians in 2025. The proposed
gross grid labor exceeds the existing specialized line-worker occupation in the accelerated case and therefore
requires a defensible occupational mix, apprenticeship capacity, labor mobility and import-substitution test. [S9–
S10]

The EEI $1.1T projection over 2025–2029 includes expenditures that utilities already intend to make. It is a
financing-market indicator, not evidence of an additional $1.1T available for ORCS. The model must identify which
contracts are incremental, accelerated, cheaper to deliver, or otherwise attributable to the program. [S8]


6. Combined employment bridge: what is and is not supported
Three separate sector ledgers produce the following results. Annual construction job-years and O&M positions are
comparable only after careful definition; this model expresses annual job-year occupancy, not the sum of distinct
individuals hired over the period.

                                                                                                  3M remaining
                                                 Potentially net-        Full factory target      after optimistic
 Scenario                Three-sector gross
                                                 new                     if activated             new factory
                                                                                                  additions

 Conservative            54,139                  15,667                  188,640                  2,795,693
 Central                 190,208                 86,229                  452,736                  2,461,035
 Accelerated             488,750                 288,250                 754,560                  1,957,190




                                  Research scenario — not independently validated • 5

## Original document page 6

                              ORCS / NEW DEAL 2.0         |   RESEARCH WORKING PAPER             |   NOVEMBER 2026

The 3,144-site manufacturing concept produces 754,560 total factory jobs at 240 workers per fully active site and
1,037,520 at 330 workers per site. Neither estimate proves that the factories have customers, meet gross margins,
can be commissioned by 2030, or employ only net-new workers. Our central scenario assumes only 60% of
facilities are active by 2030, implying about 452,736 factory positions at 240 workers/site.

The central three-sector scenario plus activated factory jobs supports about 643,000 gross positions/job-years; even
assuming every factory position is net-new, the combined optimistic net-new tally is about 539,000. The shortfall
against the 3M target is 2.46M jobs. Housing, agriculture, logistics, training, data services and other streams could
narrow it—but they remain unqualified and cannot yet be assigned jobs to close the gap.


7. Integrated program dependencies that remain to be qualified
7.1 Housing
A 3M-unit goal at a $200,000 selling price corresponds to $600B gross housing sales value, not net profit or public
cost. An even four-year deployment from 2027 to 2030 would require 750,000 completions annually. The Census
estimated approximately 1.49M privately owned housing completions at the annualized 2025 rate, so the implied
incremental production is of major national scale. Housing capacity requires land, infrastructure, building code,
permit, financing, skilled trades, and distribution of actual buyers—not only factory printers. [S11]


7.2 Agriculture, food processing and nutrient recovery
Earlier ORCS county-bioprocessing planning calculated approximately 5.87 TWh/year of net electricity, 76,455
metric tons nitrogen, 19,066 tons phosphorus and 78,412 tons potassium expressed as K2O under a conditional 50%
recovery scenario. A $248M/year nutrient reference value was also modeled. These figures are recovered internal
scenarios, not independently reproduced field results. Prior scenario analysis showed negative annual finance
balances for some county-sized sites, so net product revenues and local feedstock availability remain critical.

USDA reports approximately 1.18M agricultural wage-and-salary jobs in 2024. This is an existing workforce
reference and cannot be counted as new ORCS employment. [S12]


7.3 Other sectors
Cooling equipment, transformer fabrication, AI/data-center operations, logistics, site remediation, healthcare
administration, education, auditing, and maintenance remain components of the proposed national portfolio. The
original employment allocations are preserved in the workbook Sector_Targets sheet, clearly labeled TARGET /
UNMODELED rather than derived outputs.


8. County-level deployment is a benefit guarantee, not a site allocation
shortcut
County-by-county participation is foundational to the proposed political-economic structure. Each county should
have a measurable benefit commitment—industrial jobs, qualified training, maintenance capacity, affordable
housing, water improvements, grid reliability, waste recovery, or accessible inference/digital services. A benefit
package is not automatically a factory.

Allocation should minimize delivered industrial/logistics costs subject to environmental permitting, skilled-worker
supply, capital availability, utility capacity, contractual demand, and an auditable local-benefit floor. Inter-county
commuting, utility service territories and watershed boundaries must be represented explicitly; none necessarily
match a county border.



                                Research scenario — not independently validated • 6

## Original document page 7

                               ORCS / NEW DEAL 2.0         |   RESEARCH WORKING PAPER             |   NOVEMBER 2026

County optimization was not executed here. The dataset intake schema identifies Census 2023 County Business
Patterns, BLS QCEW, local property records, EPA CWNS project data, EIA/utility investment plans, and local
permits. Because the raw county files and site audits were not ingested, this revision does not rank or promise
actual county projects. Source URLs and required fields are in the workbook.

The integrated data-center ledger maintains three separate boundaries: facility resource draw; integrated
industrial-site physical performance; and independently demonstrated community benefit. The program cannot
net community goodwill against electricity or water meters and claim that the data center itself produces power or
water.


9. Finance: 2030 jobs vs 30-year capital envelope
At 5% fixed interest and a fully drawn $1.5T principal amortized over 30 years, annual debt service would be
approximately $97.58B. This is a scale comparison—not a financing schedule: a real program would draw capital
over years, have multiple rates/tenors, and could have guarantees rather than cash disbursement.

Three million jobs at a $70,000 loaded annual cost require $210B/year of payroll alone. This recurring labor
obligation must be supported by qualified sales, services, contracted public procurements, tariffs, sustainable
appropriations or other explicit sources of funding, not by casually amortizing the original capital envelope.

The earlier $180B federal liquidity/risk facility and $20B standards/audit/workforce authority remain unallocated
against the $1.5T envelope. They are not automatically additional, nor automatically included. The previously
discussed refinery modernization authority at $100B/year for 30 years would total $3T and therefore cannot fit in
the current package without narrowing its duration, reducing the amount or creating separate authorization.

Water and grid scenarios describe annual executed construction/project expenditure, not new government
spending commitments. They may be funded by utilities or project owners; existing utility capital programs must
not be claimed as federally financed ORCS benefits.


10. AI augmentation and productivity verification
The program’s intended mechanism is human–AI tandem productivity: consent-governed personal agents, role-
bound enterprise integrations, local production support, audit trails, and specialized on-the-job training. Time
saved is an intermediate outcome, not a new job or automatically realized profit.

Run matched or randomized pilot cohorts comparing conventional tools, generic AI assistance, and persistent
agents connected to authorized work systems. Measure quality-adjusted output per paid hour, task errors,
supervision time, retention, wages, training completion, accessibility, and net program cost. Do not promote
employee productivity as a simultaneous direct employment increment.

Underwriting should explicitly model potential hiring avoidance or displacement; the program’s augmentation
preference must be translated into employment monitoring, retraining, due-process and contractual governance,
not simply assumed from technology choice.


11. 2030 ramp: physical schedule before political claims
The workbook contains a four-year illustrative activity ramp of 15%, 35%, 65%, and 100% of 2030 scenario levels
for 2027–2030. These are artificial activity fractions to expose sequencing requirements, not a construction plan.
Raw material availability, equipment lead times, qualified labor and permitting will likely produce non-linear
deployment.

A serious deployment model requires procurement lead-time distributions and crew-throughput schedules linking
materials facilities to product qualification, electrical upgrades to factories/housing sites, wastewater reuse to site

                                Research scenario — not independently validated • 7

## Original document page 8

                                   ORCS / NEW DEAL 2.0         |   RESEARCH WORKING PAPER            |   NOVEMBER 2026

operations, and housing completion to workforce attraction. Benefits must be evaluated by county and by year; the
program should not assume that all workstreams can expand simultaneously without competing for crews, steel,
copper, transformers, grid capacity or financing.


12. Pilot validation and binding stop criteria
    Gate                                      Required evidence                      Fail / redesign condition

    Data                                      Primary source register,               Untraceable or overlapping
                                              unit/vintage reconciliation, mass      national baselines
                                              flow checks
    Feedstock                                 Contracts, contaminants, actual        Material loss or unknown
                                              accessible volumes                     contamination outside design
                                                                                     range
    Qualification                             Third-party certified products,        Safety/structural/electrical
                                              buyer acceptance                       certification failed
    Finance                                   Contracted offtake, funded service,    Negative bankable coverage absent
                                              project capital coverage               explicit subsidy
    Labor                                     Measured site/task labor hours,        Employment inferred only from
                                              payroll baseline                       target multipliers
    Net new                                   Employer and worker baseline plus      Existing transferred workers
                                              comparable controls                    counted as new
    Environment                               Verified utility meters, waste,        Material environmental
                                              pollution, water accounting            noncompliance
    AI                                        Randomized/control outcomes and        No meaningful verified gain or
                                              retention                              harmful workforce effect
    Community                                 Published realized county benefits     Benefit floor repeatedly missed
                                              and public audit
    Scaling                                   Permits, crews, machines,              2030 delivery impossibility under
                                              construction critical paths            credible schedule
    Budget                                    Authorization reconciliation,          Unfunded overlap of refinancing
                                              public/private capital schedule        and refinery commitments



Suggested initial design: 10–20 heterogeneous pilot counties, supported by non-pilot comparison areas. This pilot
can identify feasibility and common risks but cannot validate 3,144 separate county economies. National scale-up
requires a second stratified expansion and independent approval of repeatable site economics.


13. Priority technical work orders
        A. Ingest actual 2023 CBP and current QCEW county records; build FIPS join and industry employment
         baseline; document suppressed data handling.
        B. Materials: measure hours/ton, quality yield, route costs, contaminated residue, signed tip and product-
         offtake agreements at multiple facilities.
        C. Water: link CWNS project categories to actual grant/utility financing, contractor payroll hours, construction
         schedule, permanent O&M and cross-county sewersheds.
        D. Grid: reconstruct utility capex by project type, isolate incremental ORCS contracts, calculate
         lineworker/electrician/other trade mix and utility qualification.


                                    Research scenario — not independently validated • 8

## Original document page 9

                                ORCS / NEW DEAL 2.0         |    RESEARCH WORKING PAPER              |   NOVEMBER 2026

     E. Agriculture: rerun original 3,144-county resource model using current feedstock composition, realistic plant
      capex/OPEX and nutrient sale contracts.
     F. Housing: validate all-in site-delivered cost and schedule (including land, foundation, utilities, permitting,
      finance and insurance); reconcile scale with national construction capacity.
     G. Finance: reconcile $180B + $20B authorities, refinery work, amortization/grants and public/private capital
      by year, with debt-service and sources-uses roll-forward.
     H. AI: pre-register controlled productivity trials and an explicit employee-retention / expansion policy before
      claiming employment contributions.

Completion criterion for “validated 3M jobs” is a reconciled, county-linked, industry-by-industry source of funded
labor demand and paid employment through 2030; no projection in this paper meets that standard. The work is
nevertheless substantially more testable than an unsupported aggregate macro multiplier.


Appendix A — Scenario assumptions (all ASSUMED unless stated)
    Input                        Conservative                   Central                      Accelerated

    Waste throughput, M          29.0                           72.5                         145.0
    short tons/year
    Waste processing h/t         1.25                           0.75                         0.45
    Waste direct new hire        30%                            50%                          60%
    fraction
    Waste qualified yield        45%                            60%                          70%
    Blended product price,       $50                            $85                          $125
    $/qualified ton
    Waste module capex,          $60                            $45                          $40
    $M
    Waste module                 65%                            80%                          90%
    utilization
    Water capex, $B/yr           5                              15                           30
    Water direct                 2.0                            3.5                          5.0
    jobyears/$1M
    Grid capex, $B/yr            15                             40                           80
    Grid field jobyears/$1M      1.5                            2.5                          3.5
    Grid new hire fraction       25%                            40%                          55%
    Annual productive            1,800                          1,800                        1,800
    hours / FTE
    Loaded labor cost / FTE      $70,000                        $70,000                      $70,000




Appendix B — Primary-source register
[S1] EPA 2018 C&D generation, landfill and next-use paths
https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/construction-and-demolition-debris-
material




                                 Research scenario — not independently validated • 9

## Original document page 10

                             ORCS / NEW DEAL 2.0        |   RESEARCH WORKING PAPER           |   NOVEMBER 2026

[S2] EPA MSW national overview, 2018 physical flows
https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/national-overview-facts-and-figures-
materials

[S3] EPA 2022 Clean Watersheds Needs Survey, categories and 20-year needs
https://www.epa.gov/cwns

[S4] EPA Recycling Economic Information (2020 report; 2012 jobs)
https://www.epa.gov/smm/recycling-economic-information-rei-report

[S5] BLS water and wastewater plant and system operators, 2025/2035
https://www.bls.gov/ooh/production/water-and-wastewater-treatment-plant-and-system-operators.htm

[S6] EPA Biosolids 2024 reporting
https://www.epa.gov/biosolids/basic-information-about-sewage-sludge-and-biosolids

[S7] DOE 2026 U.S. Energy & Employment Report
https://www.energy.gov/policy/2026-us-energy-employment-report-useer

[S8] EEI September 2025 IOU capital expenditure projections
https://www.eei.org/-/media/Project/EEI/Documents/Issues-and-Policy/Finance-And-Tax/Industry-Capital-
Expenditures.pdf

[S9] BLS electrical power line installers/repairers, 2025/2035
https://www.bls.gov/ooh/installation-maintenance-and-repair/line-installers-and-repairers.htm

[S10] BLS electricians 2025/2035
https://www.bls.gov/ooh/construction-and-extraction/electricians.htm

[S11] Census New Residential Construction
https://www.census.gov/construction/nrc/index.html

[S12] USDA ERS farm labor series
https://www.ers.usda.gov/topics/farm-economy/farm-labor

[S13] Census 2023 County Business Patterns county CSV/ZIP (not ingested)
https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23co.zip

[S14] BLS QCEW downloadable county datasets (not ingested)
https://www.bls.gov/cew/downloadable-data-files.htm

[S15] BEA input-output accounts for later indirect employment validation
https://www.bea.gov/data/industries/input-output-accounts-data

Internal ORCS recovered scenarios cited in this paper are historical conversation-derived planning calculations,
not independently verified GitHub-source runs in this release. The companion workbook labels them accordingly.




                              Research scenario — not independently validated • 10
