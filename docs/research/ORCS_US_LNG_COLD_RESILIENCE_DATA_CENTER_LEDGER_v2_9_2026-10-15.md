# ORCS v2.9 — United States LNG cold recovery + industrial edge AI + battery resilience

**15 October 2026. NEW US-ONLY DATA MODEL. RESEARCH/PROPOSED. ZERO REALIZED PRODUCTION/SAVINGS. Append-only.**

## Executive finding
The U.S. has sizable LNG receiving vaporizer nameplate but 2025 annual marine LNG imports were just **13.786 Bcf** according to EIA, versus exporting about **15 Bcf PER DAY** (exports liquefy gas and do not supply free regas cold). An EIA-import-limited throughput basis yields only roughly **0.283 Mt imported LNG**, at a screening conversion of 48.7 Bcf per Mt LNG (gas composition sensitivity). Using peer-reviewed reference **830 kJ/kg = 230.56 kWh/t** theoretical cold thermal energy results in **~65.3 GWh/year thermal cold**, annual average 7.45 MW thermal, NOT GW-scale electricity. This is theoretical cold of the import stream, not actually measured wasted cold. Existing cold use, operating modes, truck vs ship, site split, cargo schedules and vaporizer inefficiencies are not reconciled.

## Sources
- EIA U.S. LNG imports by point of entry 2025, 13,786 million cubic feet total; https://www.eia.gov/dnav/ng/ng_move_poe1_a_EPG0_IML_Mmcf_a.htm
- EIA 2026 LNG exports grew from 0.5 Bcf/d 2016 to 15 Bcf/d 2025, eight LNG export terminals as of Feb 2026; https://www.eia.gov/TodayinEnergy/detail.php?id=67224
- FERC Jan2025 LNG import map: **10 onshore import-designated terminals, plus 2 offshore deepwater LNG facilities**, including Peñuelas, Puerto Rico, and legacy dual-mode export sites. Map categories **not proof imported volume or accessible cold today**: https://www.ferc.gov/sites/default/files/2025-01/LNG%20Maps%20for%20the%20Web%20%281-28-2025%29%20-%20Imports.pdf
- PHMSA release Oct7 2026 reports 186 LNG facilities in service among 191 reported 2025 records (all types, not 186 regas imports); https://www.phmsa.dot.gov/data-and-statistics/pipeline/liquefied-natural-gas-lng-facilities-and-total-storage-capacities
- FERC: >170 LNG facilities including peak-shaving local storage and service, not additive to PHMSA 186 (overlapping universe); https://www.ferc.gov/natural-gas/lng
- 2019 thermodynamics review 830 kJ/kg LNG cold: https://doi.org/10.1016/j.energy.2018.12.170
- 2022 LNG/data-center combined power + cooling peer-reviewed case modeling: https://doi.org/10.1016/j.energy.2022.124397
- 2026 high-efficiency conceptual study models terminals 10-30 Mtpa showing 12-198 MW power and 273-1075 MW thermal cooling, case-specific modeled systems **not operating U.S. or Dongjiakou measurements**: https://doi.org/10.1016/j.rineng.2026.111031

## The actual-import baseline and sensitivity
Mass basis ~0.283 Mt LNG/y ×230.56 kWh cold/t = **65.27 GWh/y of ideal thermal cold**; average **7.45 MWth**, if smoothed 8760 hours. LNG unloading and regional seasonal operations are NOT constant, so site-level firm cold duty can be zero between cargoes if tanks aren't regasified; no 7.45 MW continuous SLA.

**Electrical generation**: assumed 5%, 10%, 20% of this thermal cold potential as net electricity = **3.26, 6.53, 13.05 GWh electric/year** = 0.37, 0.75, 1.49 MW average across national imports. NOT simultaneously allocating identical cold to chilled-water cooling; these are reference independent all-to-power comparisons; a thermodynamic exergy analysis is mandatory before using efficiency as a forecast.

**Cooling displacement**: assumed cold reserved to cooling 50-100%, useful cold captured after temperature/pinch losses 65%, conventional chiller COP=4. At 50% cooling share electric chiller avoided **5.30 GWh/year**; at 100% **10.60 GWh/year**. This is **electricity avoided**, NOT cold-electric power generated. Multi-commodity heat exchanger parasitics and geographic suitability ignored. If full cold is instead considered directly usable (100%) and COP=4, maximum idealized displaceable cooling electricity is 16.32 GWh/y, before pumps and storage. Never combine 100% electricity generation and 100% cooling credit; model splits.

**Illustrative split 10% electric power / 50% cooling cold / 40% unallocated loss/other** ×65.27 GWhth/y: generated **6.53 GWhe/y** plus displaced chiller use 5.30 GWhe/y (50% *65%/COP4) = **11.83 GWhe/y electricity equivalent benefit**, with major location, interstage and market uncertainty.

## U.S. wider scope beyond imports: PRIMARY RESEARCH GAP
The national full vaporization universe includes **domestic LNG peak-shaver facilities**, LNG fuel and utility storage, possible truck delivery and on-site gas-grid applications. PHMSA 186 facilities includes many that actually *liquefy* LNG or hold tanks without significant re-vaporization. **NEVER multiply 186 plants × import terminal ratings or assign all 186 a continuous cold flow**. Demand peaks are episodic. Need FERC/PHMSA state permit, operator and pipeline telemetry by plant, actual annual tonnes vaporized, temperature, pressure, hours, and already-used cold. No source-backed comprehensive national domestic LNG vaporization total was retrieved. Therefore TOTAL AMERICAN WASTED COLD IS UNKNOWN; 65.3 GWhth/y is a marine-import-only gross chemical baseline, not full wasted nationwide cold.

## Named shortlist for LNG-powered distributed local data-center suitability
1. **Everett LNG receiving terminal, Everett/Charlestown MA**: EIA confirmed continued operation under supply contracts through 2029-30; 2025 imported 6,093 MMcf and 2026 Jan/Feb import cargoes. Strongest *present throughput*-backed marine cold case in this dataset. Dense urban safety/buffer zones; investigate industrial cooling customers, existing chilled-water assets and proximity, high resilience value, not assume practical IT co-location.
2. **Cove Point MD**: 2025 1,156 MMcf imports, dual LNG liquefaction/export operating status; import evidence not enough for year-round free cold, need actual imported stream scheduling and operator approval.
3. **Golden Pass TX**: 2025 3,525 MMcf imports, terminal shifting toward export liquefaction; import-era cooling potential is historical 2025 throughput, NOT guaranteed future LNG cold after conversion.
4. **Elba Island GA**: historic LNG import facility but no recorded 2025 imported LNG through Elba under EIA annual; also LNG export; no imported cold credit in 2025.
5. **Lake Charles LA / Gulf LNG Pascagoula MS / Freeport TX / Cheniere Sabine LA / Cameron LA**: import-designated facilities on FERC map, export conversion/idle import status requiring checks; **zero actual import cold credited from inactive import mode**, not proof physical impossibility.
6. **EcoEléctrica Peñuelas Puerto Rico**: FERC mapped import facility. EIA lower-48 import table likely excludes Puerto Rico territorial LNG receipts or reports in a different channel; require independent PR terminal fuel vaporization before U.S.-jurisdiction rollup. Do not attribute 0 based on continental EIA table.
7. **Domestic peak-shaver subset**: FERC March2026 mapping identifies Chattanooga TN, Chesapeake VA, Kingsport TN, Hopkinton MA, Providence RI, Garner IA, Wrenshall MN, Plymouth WA, Stokesdale NC and Lovelock NV under FERC jurisdiction, among others outside FERC mapping. These are **candidate sites**, actual vaporization throughput/seasonality unverified.
No national plant count of thermally feasible co-location established.

## Data center co-siting under operator safety and thermodynamics
A modest **0.25–5 MW IT industrial edge node** for optimization (not training) is more defensible than assigning 100MW hyperscale centers to small winter-only LNG receipt flows. Cooling load rough range 10–40% of IT rated electricity depending cooling design, and actual PUE. At peak regas may absorb available cold, but safety buffer, redundancy and legal process separation constrain co-location. Cold-storage heat transfer can shift hours/days but not whole seasons cheaply. Metered site-specific cold MW by temperature band is mandatory. Remote/cooled liquid loop may outperform literally placing servers next to LNG hazards.

## Resilience pack
For industrial supervisory compute, **BESS energy = IT MW × facility PUE × autonomous hours / usable fraction**. At 1MW IT, PUE=1.2 and 4 h, minimum delivered energy=4.8MWh, nameplate **~6MWh at 80% usable fraction**, plus AC power PCS rating **>=1.2MW** and additional pump/chiller/Cooling BESS loads, UPS/transfer/reserve, 25% engineering headroom. **Battery is NOT a generation source.** It time-shifts power and can provide instantaneous UPS/ride through, arbitrage, black-start assistance or reserve energy, subject to electrical one-line design; no supply beyond battery duration without generator/islandable upstream power.
Cooling thermal storage example: at ~25K chilled-water delta-T and 1MWth×4h duty, ideal water volume = 4MWhth/(1.163kWh/m³-K ×25K)~138m³, neglect losses and usable temp band; standard chilled-water systems may operate lower delta-T and require larger tanks. For cryogenic/freezing process use compatible phase-change/media, not assumed directly stored 'cold' in electrical BESS.
Pair long-term resilience with redundant feeds, proven diesel/gas gensets subject to emissions and fuel limits, independently certified microgrid controller and tested transfer time. OT airgaps/segmentation, signed advisory AI and manual override; protection is mechanical and deterministic rather than autonomous.
Do not assume on-site LNG storage provides free extra gas supply; contractual off-take, permits and safety classification required.

## Scenarios not to add
- No 15 Bcf/d U.S. LNG exports × 830 kJ/kg as WASTED regas cold; exports take purchased refrigeration to liquefy. May have process heat/cold coupling opportunities, but energetics must debit compression.
- No PHMSA 186 × LNG import terminal cold output.
- No global 200+ terminal population applied to U.S.
- No full thermal GWh added to electric GWh without COP/power conversion and conservation.
- No BESS MW entered in electricity-generation tally.
- No claim that 2025 imports equal LNG throughput across territorial/peak-shaving systems.

## Formal next steps
(1) EIA LNG point of entry 2025/2026, separate Everett/Cove Point/Golden Pass and 2026 dual modes; (2) PHMSA operator registry with annual LNG stored, vaporized, liquefied by plant, 2025 data (if publicly accessible); (3) islanded electric resiliency model with 1/4/8-hour batteries and site specific safety; (4) physical co-location/offtaker spatial assessment; (5) equal-source thermal and cashflow alternatives: ORC generation, data-center process cooling, chilled-water district load, freeze-desal, no recovery. Deliver source receipts, code and sensitivity ranges. 
