# ORCS v3.1 — October 15, 2026 PJM emergency: peak-MW vs LNG cold and industrial resilience

**15 October 2026 | ADDITIVE | PRIMARY-SOURCE CHECK | NO REALIZED CREDIT | NOT A VERIFIED ROLLING BLACKOUT IN 13 STATES**

## Status: user '13 states rolling blackouts' language corrected
PJM interconnection supplies all/parts of thirteen states and D.C., not necessarily 13 states under actual rolling curtailments. DOE Oct 12 order 202-26-50 based on PJM Oct 11 application authorizes backup generators and dispatch through Oct 16 to avert blackouts amidst heat, planned power plant maintenance and transmission outages. PJM Oct13 Maximum Generation/Load Management alerts do **not** mean controlled blackouts ordered or executed; alert said no customer action necessary. Reporting of a national crisis may misread PJM *jurisdiction* as 13 independently blacked-out states.
Sources:
https://www.energy.gov/articles/energy-secretary-secures-mid-atlantic-grid-ahead-anticipated-stressed-system-conditions
https://www.energy.gov/ceser/federal-power-act-section-202c-pjm-interconnection-llc-pjm-order-no-202-26-50
https://insidelines.pjm.com/operations-update-extends-maximum-generation-alert-calls-on-demand-response/
https://www.axios.com/local/richmond/2026/10/14/richmond-dominion-pjm-energy-emergency-order-blackouts

## Grid sizing metric
PJM regional capacity shortfall of **~6.8 GW** referenced in Reuters Oct 12 FERC data-center filing, an anticipated future adequacy gap, not independently measured Oct15 deficit. PJM 2026/27 outlook anticipated data center load to potentially reach 29GW in 2030; new PJM data-center register approved and demand-curtailment proposal rejected by FERC as submitted.
Source: https://www.reuters.com/business/energy/us-panel-approves-pjms-registry-data-centers-rejects-plan-curtail-power-them-2026-10-12/
DOE Oct12 says **>35GW unused U.S. backup generation**, not all physically firm, permit-ready, fuel-backed or located at risk nodes. DOE temporary order exposes a much larger near-term reliability instrument than cryogenic recapture.
NERC 2025 long term assessment projects summed system peak demands may increase **>224GW summer, >245GW winter** through 2035 (various assessment areas, not single-ISO instantaneous shortage and no assertion of rolling blackouts). Source: https://prod.nerc.com/globalassets/our-work/assessments/nerc_ltra_2025.pdf
NERC 2026 Summer Reliability Assessment said abnormal-condition risk at three regions and one sub-area, improved from six at 2025, rising grid peak load 11 GW y/y; do not recast as 13 states rolling blackouts. Source: https://www.nerc.com/events/industry-webinar--2026-summer-reliability-assessment

## Same-day October 15 industrial AI power announcement — NOT LNG cold waste
**Venture Global** announces FRAME agreements with GE Vernova and Baker Hughes Energy Services for **up to sixteen 720-MW gas-powered island-mode power units**, a nameplate ceiling of **11.52 GW (16×720MW)** at property controlled by Venture Global, intended for adjacent behind-the-meter LNG and AI data centers. Commercial proposed procurement, NOT commissioned 11.52GW, NOT available to PJM grid, NOT LNG cold recovery. It might *reduce future new data-center load on public grid* if actual stations built, connected to new loads, fueled, and operated, but it can also add aggregate gas demand/air impacts and not cure legacy line congestion.
Source: https://ventureglobal.com/2026/10/15/venture-global-secures-new-agreements-to-support-expansion-of-existing-grid-independent-power-network/
Reuters same day: https://www.reuters.com/business/energy/venture-global-inks-deals-with-ge-vernova-baker-hughes-power-expansion-2026-10-15/

## Compare ORCS v3.0 annual energy against regional peak
v3.0 LNG regasification cold scenarios (NATIONWIDE, FLEET STATUS HYPOTHETICAL):
Low 25 hypothetical vaporizers×25kt/y -> 144GWh thermal/y; power-only 14.4GWhe/y / 8760h=**1.64MW** annual mean; cooling chiller avoided 11.7GWhe/y/8760h = **1.34MW** annual mean; combined 3MW.
Mid 75×50kt/y -> 865GWh thermal/y; 86.5GWhe generated / 8760h=**9.87MW** average, 70.2GWhe cooling avoided ≈ **8.02MW** average, combined **17.89MW**.
High 150×100kt/y -> 3,458GWh thermal/y; 345.8GWhe generated / 8760h=**39.48MW**, 281GWhe chiller avoided=**32.08MW**, combined **71.56MW**.
These are annual average **electrical generation plus power avoided by data center chillers** and are NOT deliverable at particular peak interval. Against a referenced 6.8GW future PJM gap, even an implausibly perfectly co-located/high-case constant **71.56MW** = **~1.05%**; against DOE nationwide backup 35GW ~0.20% (not meaningful direct comparables due geography/time). The estimated full U.S. LNG cooling opportunity may be larger if PHMSA peaks measured; 2025 domestic LNG vaporization fleet actual annual tonnage is still UNKNOWN. Old 13.786Bcf imports figure alone captures only marine LNG import, not domestic peakshavers. No LNG export process refrigeration credit as if free waste regasification energy.
IMPORTANT possible seasonal positive correlation: gas distribution LNG peak-shaver boil/vaporization peaks during winter grid stress, so **peak deliverable MW from small units could exceed annual mean for a few hours/days**—only physical time series can establish. Thermal storage and BESS provide bridging, not additional net generation.

## Complementary storage architectures
- **BESS** four-hour 1MW IT×PUE1.2 /80% usable => **6MWh nameplate** per industrial edge node; cannot cover whole PJM 6.8GW deficit. To bridge 6.8GW for 4 hours would need **27.2GWh discharged** / 0.8 usable = **34GWh nameplate** ignoring reserve/PCS/network delivery, and **6.8GW+ power capacity** where load actually needs it. This is a rough sizing reference not policy cost recommendation. Grid-scale BESS only helps where permitted interconnection and charging energy available.
- **LAES** March 2026 study by Xu Zheng et al. doi:10.1016/j.tsep.2026.104554 integrates LNG cold, waste heat, power generation, wastewater ice-making and liquid-air energy storage, with algorithmic load scheduling; **1.371MW net modeled output**, 52.1% exergy efficiency, reported **190.1% combined-energy round-trip efficiency** due attribution of external waste heat and cold; NOT ordinary electrical battery efficiency >100% and NOT a field demonstration. Use separate exergy input boundaries when comparing to BESS.
https://www.sciencedirect.com/science/article/pii/S2451904926000806
- 2026 Energy article 'Liquefied natural gas cold energy recovery through Organic Rankine Cycle for power generation and cold storage applications' online record ahead of Nov1 publication, doi:10.1016/j.energy.2026.142316. Research models serial ORC ~17.5% net work improvement with ~7.8% extra cost and optimal cold at −40/−20/+4°C, NOT U.S. operating plant. https://www.sciencedirect.com/science/article/abs/pii/S0360544226024230
- For reliability, prioritize dispatchable local low-capex flexibility/backup already in region plus microgrids, targeted 1/4/8hr BESS, then opportunistic cold-cascade with data center and process heat, not invert causality.

## Quantification to perform before mapping 13-state/peak gaps
Obtain current PJM load forecast, capacity margin, emergency dispatch MW requested/actual on **Oct13/14/15** and EEA status. Extract NERC balancing authority adequacy MW not state counts. Geocode PHMSA true LNG vaporizing plants by BA/ZIP, rated LNG t/h, actual annual LNG vaporized and frequency, known cold users; overlay with balancing area need and data-center permitted megawatt demand. For each plant assign thermal/electric kW for **particular emergency hours**, guaranteed 4-hr battery kW and MWh, local interconnection capability, and actual refrigerant opportunity costs; any unverified site remains UNKNOWN.
## Price/policy status
No proof Venture Global 11.52GW is existing or connected to public grid; no proof user ORCS design adopted; nothing merged, no economics realized. Existing v2.9 and v3.0 docs retained.
