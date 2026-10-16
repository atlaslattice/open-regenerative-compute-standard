# Maui BioSolar + AI Living Landscape + Resident-First Virtual Power Plant — v0.2
**Atlas Lattice / Open Regenerative Compute Standard (ORCS)**  
**Date:** 2026-10-16 · **Status: PROPOSED / SIMULATED / NON-CANON / ZERO REALIZED CREDIT**  
**Provenance:** New, separately versioned companion to [Olowalu–Launiupoko Living Landscape and Mandatory Lahaina BioSolar v0.1](maui-olowalu-launiupoko-living-landscape-lahaina-mandatory-biosolar-v0.1-2026-10-16.md) and [standalone land/desal microgrid calculator v0.1](maui_olowalu_biosolar_v01.py). Neither original is modified.  
**Executable companion:** [Maui resident-first VPP / BioSolar model v0.2](maui_biosolar_vpp_v02.py).  
**IMPORTANT:** Source documents demonstrate real grid dispatch and actual Hawaiian Electric programs; this Maui project is **not** installed, approved, funded, or endorsed.

## 1. Reframing the engineering objective

**BioSolar is supplemental to the utility grid and firm resilient generation, not an assumed fully self-sufficient power supply for a building, neighborhood or ZLD desalination plant.** Treat integrated vegetation + PV as co-designed land use providing a locally testable generation benefit, cooling/shade, stormwater infiltration, landscape beauty, plant growth, resident amenity, and diversified resilience. New mandatory Lahaina construction standards should specify an eligible-building PV/storage/greenery/microgrid-ready **performance requirement** with code-safe equivalencies, historic rights, permits, lawful legislative approval and funded affordability pathways.

For water and ZLD: preserve the earlier 1-MGD hypothetical RO/ZLD model of **~18.46 GWh/year** at assumed 85% duty, compared with **8-MWp** site PV at **12.8 GWh/year** before 1–2% BioSolar test uplift. The shortfall is **not a design failure**: supplement with utility service, negotiated firm energy and emergency backup. Always include hourly load, electrical islanding and process continuity, and never treat annual kilowatt-hours as a resilience guarantee. Resilient critical loads differ from full continuously running ZLD processes; if uninterrupted production is required, separately procure and validate firm capacity.

## 2. Real October 2026 virtual power plant precedent

Electrek (Fred Lambert, 14 October 2026) reports that California's residential battery systems supplied **745 MW peak** in a coordinated October 6 response to a heat wave. A Tesla disclosure cited **more than 85,000 Powerwall owners exporting more than 600 MW** within that **combined 745-MW figure**: do not add them. Sunrun's original release reports **669 MW peak on October 5** and **745 MW October 6**. Sunrun and Tesla share underlying assets and reporting; this was not two separate 745-MW power plants.

**745 MW = instantaneous power at the recorded peak, not 745 MWh or a demonstrated number of hours at full output**. Neither press release gives full October 6 dispatch MWh or detailed duration. The broader September 2026 580-MW event did include a three-hour dispatch window, but that does not prove October 6's actual duration. Customer compensation is a regulated program feature rather than an assumed profit per Maui battery. California's reported event is evidence of coordinated distributed dispatch *technology*, not evidence those companies were using a particular AI architecture or that Maui can reproduce the fleet size.

Sources: https://electrek.co/2026/10/14/tesla-powerwall-sunrun-record-745-mw-california-grid-dispatch/ and https://investors.sunrun.com/news-events/press-releases/detail/384/sunrun-leads-record-grid-dispatch-delivering-enough-energy

## 3. More important: Hawaiʻi has a currently operational entry point

**Hawaiian Electric BYOD Plus**, Rule 33, already enrolls eligible batteries paired with rooftop solar and has a **two-hour daily dispatch window**. Households serve their own load first and participate with surplus output, with suitable reserve management. Utility-published BYOD Plus incentives (as viewed 2026-10-16) are **$400 per contracted kW upfront**, with an additional **$400 per contracted kW** for eligible low/moderate-income accounts, plus program-specific export credits. Eligibility, advanced meters, approved interconnection, committed capacity verification, selected windows and **five-year commitments** apply. This is a conditional program estimate, *not an award or revenue stream already secured*. For ownership/leases, the entity that actually receives the incentive can differ; ensure resident economic benefits under contract. Official links: https://www.hawaiianelectric.com/products-and-services/customer-incentive-programs/bring-your-own-device-plus ; https://www.tesla.com/support/energy/virtual-power-plant/heco-byodplus .

The Hawaiʻi PUC opened Docket **2026-0084 on April 22, 2026** to consider improved VPP dispatch and performance compensation, particularly with lower-income access: https://puc.hawaii.gov/news-release/puc-opens-docket-on-virtual-power-plant-program-and-invites-participation/ .

**Distinguish VPP versus physical microgrid**:
- VPP = coordinated permitted injection or load relief while connected to a functioning utility grid. Communications and market rules govern it.
- Customer microgrid = certified local islandable system supplying a customer's own load during outage.
- Hybrid neighborhood microgrid = separate interconnection, real protection and restoration/islanding rights. Hawaiian Electric's **Phase 1 Rule 30 excludes Maui hybrid microgrids with >1 MW peak demand**, routine nonemergency island operation, and virtual microgrids under that particular tariff. BYOD participation does *not* mean a neighborhood can energize dead public feeders. Large shared systems require another utility/PUC-approved structure.
Reference: https://www.hawaiianelectric.com/about-us/our-vision-and-commitment/resilience/microgrid-services-tariff .

Hawaiian Electric also posts Smart Renewable Energy export rates for Maui: **6.6¢/kWh daytime, 18.2¢/kWh evening peak, 13.1¢/kWh overnight** for the 2024–2026 published rate table. Actual BYOD incentives/credits depend on tariff and contract; the cited rates are **not** a single all-in value or a guaranteed 2027 price. Do not multiply peak MW by these credit rates without MWh and eligibility. Source: https://www.hawaiianelectric.com/products-and-services/smart-renewable-energy-programs/smart-renewable-energy-export .

## 4. Illustrative 500-home Botanical Village VPP screen

Under the previous **613-acre historical planning-envelope hypothesis**, assume *for comparison only*:
- **500** long-term homes; **60%** choose and qualify for enrollment = **300 hypothetical participant homes**.
- Each participating home has **20 kWh usable storage**, including a **50% resident backup reserve**; its home's two-hour demand is assumed **2 kWh**.
- Each enrolled home commits **3 kW over two hours**, yielding **6 kWh AC dispatched per event** if hardware, grid acceptance and battery SOC allow.
- **90% assumed battery-to-export delivery efficiency**: available AC after protecting the 10-kWh reserve and 2-kWh household demand = (20 − 10 − 2) × 90% = **7.2 kWh/home**. This idealized energy test supports the 6-kWh commitment on a nominal full-battery start, **not actual field availability**.
- **300 homes × 3 kW = 0.90 MW peak export**, and **0.90 MW × 2 h = 1.80 MWh per full successful event**; no guarantee every day's dispatch is full, and real export limits may be lower.
- Installed total fleet at **500 × 20 kWh = 10 MWh usable residential capacity**; participating fleet 6 MWh. **These kWh values are distinct from the 0.90-MW VPP power.**
- Conditional upfront programs for **300×3 kW = 900 committed kW**: general $400/kW => **$360,000** *hypothetical aggregate one-time awards*, not annual revenue. Assuming half participating households are individually qualified LMI => additional **$180,000**, for **$540,000 aggregate upfront conditional scenario**. Application approval, enrollment capacities, verification, recipient rights and actual LMI eligibility must be established. Neither figure finances the whole village, and it must not also be counted in the islandwide ORCS enterprise as fresh revenue. Export credits are not modeled without actual dispatch/tariffs/contracts.
- Households with ~**10 kWh in reserve** and a hypothesized **5 kWh/day critical load** have an ideal **two days backup without solar** at that reserve; real usable duration may be less and higher-reserve preferences can lower VPP dispatch. The prior **72-hour 0.4-MW campus** backup reference needs its own **36 MWh rated** energy system at 80% delivery assumption, distinct from household backup and distinct from any grid-connected VPP commitment.

Scale bands for the **same committed 3 kW/home**, without claiming enrollment feasibility: 100 enrolled = 0.3 MW/0.6 MWh per two-hour full dispatch; 300 enrolled = 0.9 MW/1.8 MWh; 500 enrolled = 1.5 MW/3.0 MWh. These are mathematical nameplate dispatch screens, not firm accredited grid capacity or islands-mode neighborhood supply. The source article's California per-home average (~7 kW Powerwall peak) should **not** be copied as Maui contract sizing.

**Energy production**: for all 500 homes at 7-kW rooftop PV, **3.5 MWp** and assumed 1,600 annual kWh/kWp => **5.60 GWh/year** PV. The **1.5% BioSolar test hypothesis** corresponds to **0.084 GWh/year (= 84 MWh/year)** incremental; the separate 8-MW campus adds **0.192 GWh/year (=192 MWh/year)**. Total **276 MWh/year** hypothetical incremental solar production is *not* incremental firm battery energy or revenue. Must distinguish exports from self-consumption, non-electric benefits, and irrigation load.

The new [v0.2 script](maui_biosolar_vpp_v02.py) calculates the basic power, energy and conditional incentive sensitivity with explicit resident reserve constraints.

## 5. AI-driven living landscape monitoring and optimization architecture

**Three distinct control domains:** (1) plant and hydrology monitoring; (2) power and battery measurement/forecasting; (3) public safety and human-licensed utility operations. AI is supervisory decision support, not unverified direct access to safety-critical battery protection, chemical dosing or potable water systems.

### 5.1 Sensor and data plane
| Layer | Suggested measured inputs | Outputs and guardrails |
|---|---|---|
| Solar arrays | String-level DC/AC power, inverter temperature, panel rear temperature, plane-of-array irradiance, tilt, wind, soiling and shade | Expected-vs-actual yield, faults, temperature-normalized uplift; shading and salt corrosion alerts |
| Botanical garden | Soil moisture/tension by depth, root-zone EC/salinity, evapotranspiration, air humidity, plant leaf temperature, rain capture, runoff, soil stability | Species-appropriate irrigation suggestions; no invasive exotics introductions; cap water by lawful available reclaimed supply |
| Native dry forest | Seedling survival, canopy cover, wildfire fuel load, invasive plant observations, erosion/sediment and seasonal soil moisture | Native practitioner-approved restoration timing; water conservation; manual human review for vegetation removal |
| Battery and grid | Revenue meter, grid voltage/frequency, breaker state, inverter output, BMS SOC/SOH/temp, critical circuits, fire/smoke, utility dispatch limits | VPP availability and forecast; SOC reserve never below resident-set safety floor; certified EMS/BMS owns electrical protections |
| Water plant | Source salinity, feed/potable conductivity and permitted QA, tank levels, membrane pressures, RO specific energy, ZLD energy and residual mass | Maintenance scheduling, operator alerts and non-safety load-shifting proposals; regulatory-rated PLC/SCADA retains authority |
| Coastal protection | Measured turbidity, sediment/nutrient/microplastic sampling and collection receipts | Reef-protection monitoring, not unvalidated remote actuation or assertions of cleanup credit |

**Example logic:** early-morning vegetation moisture forecast predicts drought stress under PV; edge AI proposes targeted irrigation from **lawfully available reclaimed water**, checks reservoir reserves, salinity, native plant needs and human-approved watering windows, and then sends a *bounded recommendation* to a conventional irrigation controller. It also predicts potential panel cooling and power changes from a temperature-corrected control array. If the marginal irrigation water is needed for resident essentials, streams or critical crops, the flowerbeds receive none. Growing plants is a project benefit; the **1–2% energy increase** remains experimentally unproved until site A/B data support it.

### 5.2 Day-ahead scheduler and event-response hierarchy

Proposed objectives: minimize household energy burden and ecological harm while maintaining water service; reduce peak grid stress when contracted; preserve emergency reserves; prevent excessive cycling and expensive premature battery replacements. Explicit prioritized constraints:

1. Life safety, fire/chemical safety, critical healthcare devices, grid protection and emergency public services.
2. Resident-defined backup energy, outage/evacuation readiness, allowed irrigation hierarchy, protected water demand and lawful water rights.
3. Rooftop/garden thermal balance, plant survival, public shade and native ecological stewardship.
4. Optional approved BYOD/VPP event dispatch only with **resident consent**, utility rules and remaining surplus.
5. Revenue/cost arbitrage and aesthetic effects never bypass gates 1–4.

Operating modes:
- **Normal:** predict household and garden loads, 24–72 h weather, solar, plant conditions and battery availability; propose a verified export commitment and operational schedule under contracts.
- **Hot afternoon / evening peak:** respect critical circuits and backup reserves; deliver only approved excess battery power, and measure MW *and* MWh with time stamps.
- **Hurricane, extreme wildfire threat, scheduled fire management or impending outage:** increase reserve policy under resident/operator preferences and applicable contracts; preferentially precharge critical batteries, suspend discretionary export where legally/contractually allowed; preserve emergency water/communications/pumps and irrigation appropriate for fire readiness.
- **Blackout:** approved protective isolation/islanding takes over; no attempt to energize dead utility lines; only certified local microgrid circuits serve priority loads, with offline operation independent of cloud access.
- **Sensor failure or cyber incident:** revert to conservative deterministic control, not open-ended agent action. Human operator can lock out all optimizer-driven suggestions.

**Security and privacy:** edge inference where practical; segregate residential consumption from public garden and OT logs; publish consented *aggregated* community metrics, not individual household occupancy or location patterns. Hardware-enforced battery reserves, signed updates, audit trails, MFA and zero-trust segmentation. AI may not modify certified relays, safety PLCs, discharge limits, water sanitation set points or utility dispatch obligations outside explicitly engineered envelopes. No algorithmic autonomy over chemically dangerous processes.

## 6. True BioSolar measurement protocol (avoid claiming 1–2% guaranteed)

Controlled paired plots: same PV model, azimuth, tilt, ventilation, wind exposure, shade, cleaning and estimated irradiance; randomized or crossover vegetated/control modules and separate species groups. Instrument kWh/kWp, voltage and temperature, local weather, root-zone soil moisture, annual rainfall, irrigation liters, plant health, cleaning frequency, biomass carbon, runoff, soil nutrient and wildfire fuel. Normalize yield by irradiation and temperature. Pre-register 0%, +1%, +2% sensitivity hypotheses, including possibility of **negative** results from shading, corrosion or maintenance.

Peer-reviewed national-lab evidence demonstrates soil and vegetation co-benefits but warns PV cooling uplift is climate/site-specific. A multi-year temperate-climate study found **no statistically significant vegetated-array electricity uplift**, so do not use 1–2% as a bankable forecast. Relevant references:
- https://research-hub.nlr.gov/en/publications/environmental-co-benefits-of-maintaining-native-vegetation-with-s/
- https://research-hub.nlr.gov/en/publications/multi-year-analysis-of-physical-interactions-between-solar-pv-arr/
- https://doi.org/10.1088/1748-9326/ad2ab8

The vegetation and resident benefits count even if measured PV uplift is 0%, subject to maintaining a sustainable irrigation, roof-fire and water budget. Never design a mandatory planted roof if its fire-risk or maintenance burdens exceed viable alternatives.

## 7. Architecture cohesion, governance and value capture

**Lahaina mandatory new-build standard proposal** continues from v0.1, requiring site-appropriate PV, approved green integration, critical-load backup, and grid-service/microgrid readiness with safe equivalencies. Not all buildings can join a VPP; voluntary grid *market participation* remains contract-based even if installing capable devices becomes an adopted code requirement. Homeowners, tenants and resident cooperatives must know who owns the equipment, pays for batteries and degradation, receives program incentives, sets reserve minimums, and can opt out under contract. Avoid shifting program benefits to third-party landlords without resident protections.

**Olowalu botanical village**, Launiupoko coastal research and county water campus should use consistent beautiful architectural elements: integrated planted solar canopies, native dry forest continuity, public gardens with limited exotic rainforest display, shaded walkable courtyards, visually screened but accessible utility buildings, and non-extractive cultural leadership. PV may be supplementary to conventional reliable energy. Garden irrigation and mineral-processing power compete for real resources and are not assumed to be free.

**Economic ledger** must separately display resident-owned avoided bills, utility dispatch compensation actually earned, verified self-consumed energy, PV incremental yield, offset building cooling, measured plant performance and maintenance, reduced irrigation where proven, import substitution without double counting, 10–15-year battery replacement reserves where warranted by lifetime model, cyber/software costs, and ecological improvements (nonmonetized unless independently valued). No automated economic credits without records.

**Thirty-year experimental design:** baseline year 0 power/plant measurements, 12–24-month paired BioSolar pilot, yearly certified power and ecological audits, fifth-year battery degradation/replacement review and community opt-in renewal, separate 8,760-hour grid dispatch and 72-hour islanded-resilience test. Require Native Hawaiian and resident-led governance and stewardship.

## 8. Immediate next build artifacts

1. Import **actual Maui BYOD tariff terms and eligible enrollment capacity**; identify which roof owners/residents can legally receive the incentives.
2. Extend the [Maui Front Street v0.4 dispatch model](maui_circular_ocean_microgrid_v04.py) to hourly battery SOC and storm reserves; **do not** mistake v0.2 algebraic event capacity for dynamic dispatch validation.
3. Define a **non-intrusive digital twin** for native forest, ornamental plants, reclaimed-water irrigation and PV; seasonally compare alternative horticultural regimes.
4. Site-policy and legal study before mandating equipment: fire code, Class A roof vegetation equivalents, historic Lahaina restrictions, utility incentives, consumer ownership and hardship funding.
5. Gather actual TMK/GIS buildable areas and consent. The historical **613-acre** Olowalu planning envelope remains **illustrative**, not a developable titled parcel. The separate restored **19.4-acre former debris quarry** is not presumed available.

**Bottom line:** use the proven California VPP event as evidence that distributed home storage can support a grid at scale; use Hawaiʻi's existing BYOD Plus and PUC docket as realistic pathways; and build an AI-supervised, resident-protective, habitat-positive BioSolar system that supplements—not falsely replaces—firm electricity, emergency backup and native ecological stewardship.

**Provenance:** no systems installed or dispatched for this ORCS proposal, no regulatory authorization, no earned utility incentives, no verified 1–2% uplift, no existing cultural endorsement, no realized housing or ecosystem benefit.
