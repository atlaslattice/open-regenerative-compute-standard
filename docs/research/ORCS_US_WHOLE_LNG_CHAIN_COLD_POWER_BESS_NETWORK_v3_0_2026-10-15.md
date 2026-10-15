# ORCS v3.0 — U.S. entire LNG facility fleet: vaporization cold, electric, cooling and resilience scenarios

**2026-10-15 | U.S.-ONLY · ASSUMPTION-DRIVEN NATIONAL SCALE SCREEN · ADDITIVE · ZERO REALIZED CREDIT**

## Why change the denominator
Prior v2.9 intentionally modeled only foreign LNG **imports** to the U.S., 2025 EIA annual 13.786 Bcf. That omits domestic **peak-shaving LNG vaporizers**, which can be charged from U.S. pipeline gas and regasified into U.S. utility systems in winter. EIA describes the domestic peak-shaving cycle here: https://www.eia.gov/energyexplained/natural-gas/liquefied-natural-gas.php .

As of PHMSA's October 7 2026 publication, 2025 U.S. regulatory returns include **186 LNG facility records in-service** from 191 total (PHMSA). The source's capacity in service is **63,834,468 [unit not shown in main webpage table]**; it is a **STORAGE CAPACITY**, not annual regasification LNG flow. It is inappropriate to multiply by every site's number of cargoes or continuously run it without actual vaporization volumes. https://www.phmsa.dot.gov/data-and-statistics/pipeline/liquefied-natural-gas-lng-facilities-and-total-storage-capacities ; downloadable 2010–present annual reports at https://www.phmsa.dot.gov/data-and-statistics/pipeline/gas-distribution-gas-gathering-gas-transmission-hazardous-liquids .

EIA explains most current US mega LNG infrastructure **exports**: LNG liquefaction consumes refrigeration, gas, and electricity. PHMSA facility counts include exporters, LNG production/holding, and peak shavers; **186 is the total screening universe, NOT 186 operating LNG cold recovery plants**. No averaged real world 2025 domestic vaporization TONNAGE is established by facility count. These ranges are *assumed tonnage per active vaporizer*, not a documented historical mean.

## Global physics / U.S. sample modeling basis
830 kJ/kg of LNG vaporized theoretical cryogenic energy/exergy reference (IEEE 2025 study on LNG ORC cold electricity): https://ieeexplore.ieee.org/abstract/document/11041205 . ≈230.56 kWh-thermal per metric tonne LNG. Thermodynamic exergy and heat quantities are not identical; treating the entire value as freely recoverable cold-duty is a simplifying **upper screen**, not actual on-site recoverable electricity. Losses, pressure, thermal approach, temperature glide and ambient-air pumping all matter.

### Three DIFFERENT assumed U.S. peak-shaver/receiving fleets (do not add together)
| Fleet | Hypothesized vaporizing sites out of 186 | Hypothetical annual tonnes vaporized/site | Total tonnes/year | Cold potential GWh-thermal/year | Generated electric GWhe/y at 10% assumed conversion | Chiller avoided GWhe/y (50% cold allocation ×65% capture /COP4) | Combined useful-electric equivalent GWhe/y | Example BESS capacity at all nodes |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Low | 25 | 25,000 | 625,000 | **144** | **14.4** | **11.7** | **26.1** | **150 MWh** |
| Mid | 75 | 50,000 | 3,750,000 | **865** | **86.5** | **70.2** | **156.7** | **450 MWh** |
| High | 150 | 100,000 | 15,000,000 | **3,458** | **345.8** | **281.0** | **626.8** | **900 MWh** |

Assumptions: model assigns **10%** gross cold energy to Rankine electric conversion, **50%** to physical useful cooling (65% of that delivered), **40%** to residual/unutilized or other. COP4 electric displacement only for useful cooling. These branches cannot claim 100% electricity and 100% cooling simultaneously; waste cold does not equal generated electricity. Cold generation available only when LNG vaporized, particularly peak-shaver dispatch windows. Annual mean power equivalents are **3.0/17.9/71.6 MW** across low/mid/high for generated electricity **plus avoided chiller load** (not all is electric generation). Separate power generation annual average = **1.65/9.87/39.48 MW**.

**Sensitivity challenge:** national 15Mt annual LNG vaporization in high case is about **53 times** the 2025 imported-LNG tonnage, which is physically possible for hypothetical domestic pipeline-sourced peak-shaving flow but *not evidenced*. It might exceed actual U.S. peak-shaving annual turnover by a wide margin, because these facilities are seasonal. DO NOT cite these assumed cases as an estimate of measured 2025 unused cold, probability distribution or industry average. Data extraction from PHMSA is needed; 2025 volume receipts may have only annual LNG **storage inventory**, not vaporizations; if missing ask operators or EIA surveys.

## Compute and resilience equivalent, separately costed
For EACH assumed active site, example modest **1MW IT edge AI** for optimization (not training), PUE=1.2 gives 1.2MW entire node. At 4h backup, delivered energy 4.8MWh, BESS minimum nameplate **6 MWh** at 80% usable. Low/mid/high assumed site installation = **25/75/150 on-site 1MW IT nodes** and total nameplate **150/450/900 MWh batteries**. This is NOT naturally obtainable from annual waste-cold inventory or economical at all these sites, and cannot supply LNG facility's full industrial loads. Grid islanding needs independent generation and a 1.2MW+ inverter per IT node, cooling/pump/UPS and safety systems, fuel and winter load plans. BESS provides *storage*, not extra electricity; reserve electricity can be charged from grid or qualified local power under measured terms.

## Data-center duty reality check
An LNG power-generation fleet generating a total **86.5 GWh/year** under mid case would, if flawlessly delivered and firm, power 75 nodes ×1.2MW each for only **~960 hours of aggregate full-load year-equivalent**, far less than 8760 hours/year. To support all 75 1MW IT nodes at 80% IT utilization for year: 75×1.2MW×8760×0.8=**630.72 GWh/year**. Thus the mid-case power generated is ~13.7% of those node demands on an annual energy basis, and chronologically much less without supply scheduling. Cold cooling savings can reduce extra HVAC energy, but cannot substitute for IT kWh. This directly answers need for batteries: 6MWh per node covers 4 hours of rated node facility power, NOT seasonal peak-shaving gaps.

## Real-world source classes + priority
1. LNG import receivers: Everett MA documented active U.S. import stream; 2025 EIA import receipts in v2.9. Opportunity credible but owner contracts, facility safety buffers, year-round vaporization and co-siting unknown.
2. Domestic peak shavers: PHMSA facility-type-specific records and utility annual reports, linepack and storage; high value **cold coincidence with winter demand**, but backup electricity and chillers unavoidable.
3. LNG export liquefiers: major energy flow but refrigerant cold is an **input** and cannot be counted as wasted vaporization cold; optimize existing compressors/heat rejection/edge AI instead, in separate ORCS ledger.
4. LNG fueling/satellite LNG terminals and storage-only sites: candidate after verifying genuine LNG vaporization, annual tonnage, distance and safety constraints. Do not give an energy-per-facility averaged across all 186.

## Next real-data extraction 
PHMSA 2025 LNG annual record microdata: unique site/operator identifiers, facility type, storage, installed vaporizers, annual tonnage **actually vaporized if present**; EIA LNG peak-day utility withdrawal and city-gas data, import receipts and territory sources; gas utility filings and permit records. Then compute site mean tonnage, annual vaporization hours, recoverable and already used cold, cold temperature exergy, viable data center location and BESS hours/capacity; use county and electrical tariffs. National demand-driven fleet operating annual average may be orders of magnitude below high case because facilities mainly serve winter peaks.

## Existing papers preserved 
- Prior imports-only bottom baseline: docs/research/ORCS_US_LNG_COLD_RESILIENCE_DATA_CENTER_LEDGER_v2_9_2026-10-15.md
- Co-siting Corpus export v2.6 and v2.7 research remain unmodified.
- New runnable example: prototypes/orcs-lng-cold-us-v3_0/us_fleet_vaporization_scenarios.py

**All figures are explicitly conditional engineering scenarios with NOTIONAL operating population and utilization, not measured national average power production or operator business case; zero realized credit.**
