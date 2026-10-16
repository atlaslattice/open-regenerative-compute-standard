# Atlas Smart Water Spine — Maui Residents-First Circular Water, Fiber Sensing & Co-located AI Inference
**ORCS research white paper v0.1 | 2026-10-16**
**Status:** PROPOSED / SIMULATED / CITED; NOT a permitted design, endorsed project, proven savings forecast, or investment recommendation.
**Provenance:** New companion paper; prior Maui versions preserved. No realized environmental or financial credit.

## Plain-English objective
1. Deliver dependable, high-quality water **to residents first**, including affordable household water, essential services, reserve storage, and fire protection.
2. Collect wastewater from **residential, commercial, hotel and other connected sources** islandwide where environmentally and economically viable, including currently separate private systems; document real influent and capture rates.
3. Reclaim wastewater for **agricultural irrigation, eligible industry, landscape irrigation and other approved non-potable uses**, while protecting crops, workers, aquifers, coastal ecosystems and freshwater-dependent natural systems.
4. Minimize leaks and excavation via **accessible, modular aboveground pipe corridors where appropriate** plus rehabilitated buried assets elsewhere; include fiber communications and distributed sensing.
5. Equip all three initial treatment campuses with **on-site inference computing**, solar and bioenergy integration, human-supervised optimization, and a physically separate, safety-rated operational-control layer.
6. Require **no routine liquid waste disposal** for proposed ORCS process streams, microplastics interception and verified management of salts, ash and hazardous residues. ZLD is not zero solids/emissions.
7. Measure *actual* freshwater withdrawal and East Maui stream-diversion reductions, rather than counting infrastructure capacity as ecological recovery.

## Quantitative starting ledger: DON'T DOUBLE COUNT
- **22.5 MGD** = historical Maui County Department of Water Supply (DWS) household-metered baseline (17.5 MGD single-family + 5.0 multifamily), **not Maui Island-only 2026 flow**, excluding private suppliers. Treat as sizing target subject to reconciliation.
- **Household circular target**: 70% collected for centralized/local advanced reclamation × 90% treatment recovery × 22.5 = **14.175 MGD** reclaimed second-use service. This is SIMULATED; actual public plant flows do NOT substantiate 14.175 MGD household-only recovery today.
- **Known public Maui Island wastewater plants** historical: Lahaina 3.41 MGD, Kīhei 3.93 MGD, Wailuku–Kahului 5.54 MGD; combined 12.88 MGD *from all sectors*. At hypothetical 90% recovery yields 11.592 MGD **total public-plant output**; historic already reused 4.37 MGD. Not additive with household-only recovery, and no double counting of private/municipal transfers.
- **Residential water supply nameplate** at 85% dependable annual output: 22.5/0.85=**26.47 MGD** if ALL historical DWS household demand were newly desal-supplied. This is not additional to retained municipal freshwater nor a demand forecast.
- **Household cascade**: 22.5 MGD first use + 14.175 MGD reclaimed second use = **36.675 MGD sequential service** (NOT 36.675 MGD new water). Additional commercial/resort sewage can increase recoverable flow only when measured separately and not already included in public plant influent.
- **Agriculture:** recoverable municipal wastewater alone does not meet ~41.46 MGD midpoint Mahi Pono future irrigation scenario (development scenario, not actual diversion). Measure farm demand after efficiency, water rights and environmental-flow requirements; match recovered volumes to source-specific diversion retirement.
- **Non-revenue water** ~18% of DWS supply in historic county plan includes physical leakage plus meter/accounting/unbilled categories, NOT demonstrated 18% farm water loss. Meter supply, billing and district-night-flow separately.
- Do not assume all captured wastewater can be used on crops: verify pathogen, nutrients, salinity, SAR, boron, trace organics, PFAS as relevant, and micro/nanoplastic performance; preserve adequate environmental flows.

## Three-campus architecture and capacity decision
**West / Lahaina:** resident and essential potable priority; advanced wastewater capture from homes, hotels and businesses; odor elimination, sewer overflow prevention, reef and coastal-groundwater protection; non-potable agricultural and landscaping off-take.
**Central / Wailuku–Kahului:** largest potential potable load and irrigation delivery; wastewater R-1 upgrade; agricultural storage/pumping and nutrient recovery; airport-area siting, hazards and land tenure review. Central freshwater nameplate is a design variable, NOT assumed 5 MGD.
**North Shore / Pāʻia–Haʻikū:** resident-first local potable resilience; local sewer/private-system catchment audit and suitable agricultural reuse; terrain, uphill pumping, storm and flood considerations.
**Cross-cutting:** South Maui (Kīhei), Upcountry, Hāna and privately served communities require explicit catchment and supply integration. Three campuses cannot be presumed to represent the entire island. No fixed final 3×5 MGD specification until **Maui Island customer-metered household demand by source and pressure zone** is acquired. Test total freshwater nameplate 15/25/30/40/50 MGD, with each campus variable; reserve interties, backup and phased delivery. Separate fresh desal production and wastewater-treatment capacity.

## Accessible aboveground water spine: precedents and limits
1. **Aboveground utilidors and accessible common utility corridors** are established in permafrost and industrial settings, carrying water/wastewater and other services. Alaska use does not itself prove Maui cost or resilience superiority. Example background: https://alaskaplumbingauthority.com/insulated-utilidor-systems-in-alaska/
2. **Fiber-optic distributed acoustic sensing (DAS)** can identify pipe vibration/leaks and monitor corridors; a 2026 *Applied Acoustics* article demonstrates research advances in leak localization: https://www.sciencedirect.com/science/article/pii/S0003682X25005286 . Application to specific Maui pipe and sensor geometry needs trials.
3. **Smart sewers**: EPA describes online monitoring, machine learning, real-time control and South Bend, IN case studies with documented overflow reductions: https://www.epa.gov/npdes/smart-sewers and https://www.epa.gov/npdes/smart-sewer-technologies . Not evidence of automatic equivalence between South Bend and Maui.
4. **Comparison modes**: (A) retained/rehabilitated buried lines including cured-in-place rehabilitation where eligible, (B) fully buried new lines, (C) protected at-grade/abovegrade modular corridor, (D) elevated bridge/pipe-rack routing. Include easement acquisition, right-of-way, clearance, crossing access, viewshed, corrosion, UV, earthquake, wind, wildfire, vandalism, tsunami/flood debris, water hammer, pressure loss, sediment, temperature and maintenance.
5. **Design safeguards**: aboveground shields cannot guarantee zero leaks; instrument pressure + acoustic + distributed temperature + fiber strain + flow plus district metering. Dedicated fiber strands for DAS may not be interchangeable with traffic-carrying telecom fibers; use engineered cable and optical budget. Separate communications cabinets from potable/reuse mains. Do not run sewage and potable side-by-side without compliant separation, labeling, cross-connection/backflow prevention, robust leak interception and permit approval.
6. **Do not dig up intact legacy infrastructure by default**. Replace only on lifecycle evidence, contamination/cross-connection risk or inadequate hydraulic capacity.

## Every campus gets a co-located AI inference node
**Mandatory proposed functional modules:** compute room (initially sizing by instrument count and model workload, NOT an arbitrary hyperscale data center); redundant networking and power; storage for SCADA historian, GIS asset register, metered withdrawals and provenance logs; edge vision/acoustic anomaly models; water-demand forecasting; membrane scaling/cleaning prediction; crop soil/water monitoring; nutrient mass balance; microplastic mass balance; predictive leak detection; coastal water-quality trend modeling; public read-only dashboards. Schedule noncritical inference based on renewables and compute heat reuse.
**Hard boundaries:** conventional validated PLC/SCADA and protective controls remain operable offline; AI cannot autonomously change drinking-water disinfection levels, make unsafe valve operations, or bypass permits; human operators authorize consequential setpoint changes. Independent cybersecurity segmentation of OT and inference/IT; signed updates, hardware secure boot, offline recovery, audited model versions, incident response, and failsafe plant states.
**Physical infrastructure:** climate-, salt-, cyclone- and flood-resilient equipment rooms; backups, batteries, and fire suppression; no underwater or flood-exposed critical electrical rooms. Quantify compute load including PUE; transparent WUE and water use; closed-loop/low-consumption cooling as first screening choice. Any process-heat reuse must match actual temperatures and not reduce drinking-water reliability.
**Framework:** NIST SP 800-82 Rev 3 https://csrc.nist.gov/pubs/sp/800/82/r3/final ; EPA Smart Sewer program https://www.epa.gov/npdes/smart-sewers . September 2026 NIST Rev 4 is draft, not final https://csrc.nist.gov/pubs/sp/800/82/r4/ipd .

## Reclaimed water, sludge, plastics and ZLD
- Apply applicable Hawaiʻi DOH R-1 categories and project-specific requirements (rather than importing Texas Corpus Christi Type I standards as controlling law): https://health.hawaii.gov/wastewater/home/reuse/ ; https://www.epa.gov/waterreuse/summary-hawaiis-water-reuse-guideline-or-regulation-agriculture ; https://www.epa.gov/waterreuse/summary-hawaiis-water-reuse-guideline-or-regulation-industry .
- Catch coarse and fine plastics in sewer, storm and sediment pathways, verify particle size distributions and transport to sludges; proposed Polygone filtration requires validation. Never spread mixed sewage sludge on agricultural soils based solely on fertilizer value.
- Segregate saline desal brine from biosolids. Recover nutrients and commercial minerals selectively; industrial residues remain hazardous until tested; thermal treatment/incineration requires pollutant destruction evidence, air permitting and management of salts/ash.
- Net aquifer/stream offsets require **measured retirement or reduction of specific withdrawals** and audit of induced new demand and return flows.

## Pilot sequence and gates
**0 (0–6 mo conceptual):** reconcile county DWS household bills/island pressure zones/private supply; all public/private wastewater inflows; map East Maui ditch diversions and recipient farms; GIS existing rights-of-way and utility conditions; grid/PV siting and compute workloads. Engage Native Hawaiian rights holders, residents, county utilities and regulators.
**1 (6–18 mo conditional):** 1–3 km accessible corridor pilot in suitable easement; fiber DAS vs pressure meter/hydrophone and conventional trench lifecycle comparative test; constrained inference with cyber-safety review; R-1 polishing microplastics test; no claim of automatic regulatory approval.
**2 (18–48 mo conditional):** optimize campus-by-campus modular wastewater upgrades, expanded R-1 delivery, ag storage, North Shore capture; measure leak repairs and actual retired freshwater withdrawals.
**3 (conditional later):** scale regionally based on validated 10/20/30-year cost and environmental performance; full ZLD residuals and geothermal/biosolar resource integration.
**Metrics:** household outage hours, liters/kWh and kWh/m3, non-revenue-water components, verified leakage, MGD actual reclaimed and delivered, freshwater well/stream diversion reductions, crop kg/m3, Enterococcus/coral nutrient indicators, odor complaints, microplastics size distribution in water and solids, CO2e, capital/operating cost, compute WUE/PUE and human authorization logs.

## Source appendix / evidence register
- Maui DWS Water Shortage and Conservation Plan entry: https://waterresources.mauicounty.gov/210/Water-Shortage-and-Conservation-Plan
- Maui County DWS sources and 2024 desal feasibility: https://www.mauicounty.gov/3096/About-Us
- EPA smart sewers: https://www.epa.gov/npdes/smart-sewers
- EPA smart sewer tech: https://www.epa.gov/npdes/smart-sewer-technologies
- Water-pipeline DAS experiment: https://www.sciencedirect.com/science/article/pii/S0003682X25005286
- Alaska utilidor precedent (background, secondary): https://alaskaplumbingauthority.com/insulated-utilidor-systems-in-alaska/
- Hawaiʻi DOH wastewater reuse: https://health.hawaii.gov/wastewater/home/reuse/
- EPA summary of Hawaiʻi reuse requirements: https://www.epa.gov/waterreuse/summary-hawaiis-water-reuse-guideline-or-regulation-agriculture
- NIST OT guide: https://csrc.nist.gov/pubs/sp/800/82/r3/final
- NIST 2026 draft: https://csrc.nist.gov/pubs/sp/800/82/r4/ipd

**Open verification gates:** 2026 Maui Island-only residential billing and pressure zones; all decentralized wastewater generation; West/North/Central facility real catchments and permits; actual pipe routing + soil/environmental impact; proof of projected ag 20% field-use reduction without yield harm; validated microplastic reduction and fate; levelized full ZLD costs and renewable heat; compute energy and WUE. No claim of funded, approved, built or operating system.
