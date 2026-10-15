# Maui Biosolar & Circular Water–Energy–Agriculture Model v0.2

**Atlas Lattice / Open Regenerative Compute Standard (ORCS)**  
**Date:** 2026-10-15  
**Status:** PROPOSED · NON-CANON WHERE UNVERIFIED · ZERO REALIZED CREDIT  
**Scope:** Island of Maui, with Maui County source data explicitly labeled where island-only data are unavailable.  
**Versioning:** New document; preserve preceding v0.1 discussion and all existing repository files.

## Executive summary

Propose a regenerative island-scale infrastructure architecture combining (1) brackish/saline-groundwater desalination; (2) wastewater reuse; (3) native-landscape-integrated solar photovoltaics, agrivoltaics and distributed batteries (collectively *biosolar*); (4) small, dispatchable inference-compute capacity where it provides a demonstrable public benefit; (5) stormwater and drainage restoration; (6) scientifically tested soil rehabilitation and selective mineral recovery; and (7) reef, watershed, and whale habitat protection.

**No facilities, savings, credits, or partnerships are claimed to exist as a result of this research.** Project sites require local landowner/community consent, regulatory authorization, ecological studies, and procurement analysis. The public-led Lahaina rebuilding context does not imply blanket local approval for proposed designs.

## 1. Verified baselines and explicit uncertainties

- Maui County's **2024 Desalination Feasibility Study** evaluates Central/South and West Maui supplies. The 2022 Water Use and Development Plan cited therein projects **up to 8 MGD additional source water for the Central Water System and 4 MGD for West Maui through 2035**. These are planning needs, not current shortages.
- County April 2026 correspondence reports *preliminary total capital-improvement budgets*: **$119M for 0.5 MGD brackish**, expandable to **$261M for 2 MGD**, and **$328M for 4 MGD saltwater-quality groundwater**, with annual operating costs around **$2M, $3M and $10M**, respectively. These are not costs for the biosolar-integrated design.
- Source-water chemistry must be measured separately for seawater, saltwater-quality groundwater, brackish groundwater and treated wastewater. Never apply open-ocean mineral inventories directly to an untested inland aquifer.
- Mahi Pono's 2025 report says it acquired **41,000 acres of former sugarcane land in 2018** and had **12,585 cultivated acres by June 30, 2025**. Fallow appearance is not itself evidence of soil contamination, sodicity, misuse, or legal availability.
- Existing Maui/Hawaiʻi agricultural land-use and special-permit provisions constrain PV conversion, with conditions for compatible farming. Confirm project-specific law and status rather than assuming agrivoltaics are automatically permitted.
- Maui County water-quality and reclaimed-water records, wastewater volume, power generation and island import/export statistics need independent time- and geography-matched validation. Avoid double-counting water reused or electricity displaced.

Sources:  
[2024 Maui desal study executive summary](https://www.mauicounty.gov/DocumentCenter/View/154964/Maui-Desalination-Feasibility-Study-ES-2024)  
[April 2026 Maui County water-cost correspondence](https://mauicounty.legistar.com/View.ashx?GUID=64C847A9-470B-42AD-B0E5-6B90F1742E14&ID=15364404&M=F)  
[Mahi Pono water-efficiency report 2025](https://www.mauicounty.gov/DocumentCenter/View/155515/26-SEPT_Item-No-4dii_-Water-Efficiency-Report-Q2-2025-BLNR-Report)  
[Hawaii agricultural land-use provisions](https://law.justia.com/codes/hawaii/2024/title-13/chapter-205/section-205-4-5/)

## 2. Biosolar architectural invariant

**Every new facility is evaluated first for ecological fit, landscape beauty, public access, disaster resilience, and useful co-production.** Biosolar means a *designed integration*, not covering land indiscriminately with panels and vegetation.

- **Lahaina construction:** roof-integrated solar, shaded walkways, solar carports, rainwater management, native drought-adapted landscapes, accessible green spaces, battery-backed cooling and critical services. Use fire-safe defensible space and nonflammable construction detailing; vegetated roofs require structure, water and fire review.
- **Water-treatment sites:** buried/screened tanks where practical, landscaped setbacks, quiet equipment, bioswales and native planting; rooftop/carport PV; controlled access and glare review.
- **Central Maui agriculture:** photovoltaic canopies only where crop species, light, irrigation, soil, zoning, farm economics and food output justify them; protect productive farmland and local farming opportunities.
- **Resilience:** modular electrical islands, emergency-water storage, physical hardening, cyber segmentation and manual fallback.
- **Social license:** Native Hawaiian cultural and water-rights consultation, resident-led design, transparent project finances, affordable water, ecological monitoring, and consent. Do not presume tourism aesthetics outweigh Hawaiian community priorities.

## 3. Computation + desal co-location

Candidate *small-scale* edge AI/inference nodes could assist leak detection, predictive equipment maintenance, crop-water scheduling, fire/flood alerts, rainfall-runoff modeling and marine monitoring. A 2026 Applied Energy research paper co-optimizes flexible compute, waste heat and desalination, but its financial percentages are **not** Maui forecasts.

In a reverse-osmosis plant, waste-heat use is contingent on feed temperature, membrane tolerance, scaling/biofouling, heat exchangers, pumping and economics. Compare against a control case **without compute**. High-temperature thermal desal processes require distinct thermal/electrical balances. Co-location is not inherently net-energy-positive.

**First-pass incremental compute load scenarios (assumptions, not selected designs):**

| Incremental average IT power | Annual IT electricity | Total facility electricity at PUE 1.2 | Annual extra electricity at $0.20/kWh |
|---:|---:|---:|---:|
| 50 kW | 0.438 GWh | 0.526 GWh | $105,120 |
| 250 kW | 2.190 GWh | 2.628 GWh | $525,600 |
| 1 MW | 8.760 GWh | 10.512 GWh | $2,102,400 |

Compare workload revenue/service value, recovered heat use and local resilience benefits against equipment cost, network reliability, cooling water, noise, coastal risk and opportunity cost of electricity. Do not confuse inference revenue with verified local savings.

Source: [2026 Applied Energy heat/computing/desal paper](https://www.sciencedirect.com/science/article/abs/pii/S0306261926000802).

## 4. Desal mass-energy baseline (illustrative open-seawater reference only)

Assume **5 MGD fresh water production**, **45% reverse-osmosis water recovery**, **3.5 kWh/m³ product**, 35 kg/m³ seawater salinity and 0.5 kg/m³ product salinity.

- Fresh water: **18,927 m³/day** = 5.0 MGD.
- Feed: **42,060 m³/day**; concentrate: **23,133 m³/day**.
- Electricity: **66.25 MWh/day**, **24.18 GWh/year**, excluding incremental off-site distribution and associated storage.
- Salt mass in concentrate: **about 1,462 metric tonnes/day** (feed salt ~1,472 t/day less product salt ~9.5 t/day); **~533,600 tonnes/year**. This is dissolved mineral inventory, **not** recovered saleable material.

**Critical correction:** Any earlier lower salt-total estimate at this production/recovery rate should be superseded by this explicit balance. Seawater feed minerals are not free: all inventory, extraction, purity, disposal and transport must be costed.

Use sensitivity ranges for water recovery 35–55%, treatment SEC 2.5–5.0 kWh/m³, source salinity and actual plant duty cycles. The real Maui preferred-source study is largely brackish/saline groundwater, not necessarily ocean intake.

## 5. Gypsum and soil restoration: gated research

**Hypothesis:** Some Maui saline concentrate chemistry or separate waste streams may yield calcium-sulfate (gypsum) products suitable for *certain* soil amendments. Gypsum is CaSO4·2H2O; obtaining it requires a validated calcium/sulfate mass balance and crystallization/separation/purity process. Do not claim all brine can convert into gypsum, or that gypsum can fix all former sugarcane soils.

**Soil diagnostics before any application:** pH, electrical conductivity, sodium adsorption ratio (SAR), exchangeable sodium percentage (ESP), CEC, soil texture, compaction, infiltration, organic carbon, nutrients, chloride/boron, metals, background groundwater, and crop-specific salinity sensitivity. Compare gypsum with compost, mulch, cover crops, biochar, irrigation/drainage improvements, and no-amendment controls.

**Stoichiometric audit ceiling:** 1 mole CaSO4·2H2O weighs 172.17 g, of which Ca ~40.08 g and sulfate ~96.06 g. For any process, theoretical gypsum <= min(moles recoverable Ca, moles recoverable sulfate) × 172.17 g/mol. Adjust for competing chemistry and process recovery. No gypsum tonnage or sales credit is warranted without site samples.

A pilot should measure crop yield, soil infiltration, salinity leaching, stream effects, ecology, cost per treated acre and avoided imported amendments. Concentrates should never be applied unprocessed to farmland.

## 6. Hāna drainage, watershed function and fire/flood resilience

The Maui Infrastructure Assessment reports Hāna drainage ditches that have overtopped roads and damaged stream lining. A 2026 Hāna Highway/Waikina Loop project calls for culvert and swale works. **Confirm which Hāna drainage issue and watershed the resident considers primary; do not presume a specific site or redirect stream flows.**

Design treatment train: upstream land stabilization, appropriate restored riparian buffers, sediment interception, maintained culverts, nature-based detention/infiltration where geology permits, real-time rainfall/flood sensors and watershed water-quality sampling. Maintain traditional water rights and avoid converting natural streamflow into unrestricted industrial supply.

Sources: [Maui infrastructure assessment](https://www.mauicounty.gov/DocumentCenter/View/10486/Maui-Infrastructure-Assessment-Update-condensed?bidId=) and [Hāna Highway drainage project](https://govtribe.com/file/government-file/specifications-final-specifications-w-ntb-36b-01-26-dot-pdf).

## 7. Wastewater, reefs and marine protection

Prioritize pollutant removal *before* discharge: microplastics, sediment, nutrients, pathogens and trace contaminants as site permits require. Distinguish **potable water** from **R-1 recycled water**; recycled water can displace potable irrigation demand but is not equivalent to unrestricted drinking water.

Include Lahaina and Kīhei wastewater reclamation constraints, injection-well migration and nutrient impacts, and coastal monitoring. Desal concentrate injection/discharge needs aquifer and marine modeling. Protect coral habitat and humpback migration/breeding environments; use passive marine acoustic sensing and reef-friendly construction practices.

Source: [Maui wastewater reports and studies](https://www.mauicounty.gov/1027/Current-Wastewater-Reports-and-Notificat).

## 8. Island import/export and recoverables ledger

Build an **island-only** ledger by HS/SCTG freight categories where attainable: petroleum and fuels, electricity fuel inputs, fertilizer/gypsum, food/feed, aggregates and cement, membrane and treatment consumables, metals, plastic products, agricultural imports, recovered wastes, export tonnages, and waste exported for disposal. For each stream record physical tons, source, destination, landed unit cost, local substitute, achievable recovery, energy and water needed, customer, CAPEX, OPEX, regulatory status, reserves, and provenance.

**Material candidates, without revenue credit:** NaCl and mixed salts; Mg and Ca derivatives; potassium salts; bromine; trace lithium; deuterium; recovered N/P from wastewater; biogas and organic amendments; reusable construction aggregate and metals. Trace high-unit-price materials are not necessarily economic at ocean concentrations.

Accounting equation:

Annual attributable net value = avoidable imported *landed* purchases + avoided local disposal + verified net resource sales + avoided outage losses (separately evidence-rated) − incremental operating expense − capital carrying costs − ecosystem mitigation/monitoring costs.

No double-counting: a produced kWh or gallon cannot be credited simultaneously as revenue, avoided purchases and reserve capacity. Net import substitution requires local demand and purchaser documentation; export is unlocked only after modeled local demand and appropriate reserves.

## 9. Scenario matrix and go/no-go gates

| Scenario | Water | Energy | Land | Compute | Mining | Minimum gates |
|---|---|---|---|---|---|---|
| A: Water resilience | Targeted brackish/desal + reuse | Efficiency, existing grid | Site landscaping | No new compute | None | Permits, water quality, ecology, tariffs |
| B: Biosolar circular pilot | Modular desal/reuse | Rooftop PV, batteries | Native shade/agrivoltaics | 50–250 kW optional | Gypsum process lab-only | Agricultural baseline and full LCA/TEA |
| C: Island-scale optimization | Multi-system reserves | Distributed solar+storage | Land capability zoning | Only profitable/public-service nodes | Only verified saleable streams | Freight ledger, grid modeling, consent, watershed cumulative assessment |

**Deliverables for v0.3:** source-specific water chemistry; 2025–26 island freight flows and import prices; parcel/soil maps and land tenure; wastewater plant volume and pollutants; fire and flood basin overlays; monthly hourly solar and storage dispatch; fertilizer demand; gypsum proof-of-process; ecological and resident consultation record; alternatives analysis and Monte Carlo break-even analysis.

## 10. Evidence and provenance rule

Label each claim **MEASURED / REPORTED / DERIVED / SCENARIO / PROPOSED / QUARANTINED**; version updates rather than overwriting the original; prohibit realized-cost, yield, mineral-sales, carbon-credit or social-license claims until verified. Work should be locally led and designed to complement, not replace, Hawaiʻi agencies and community planning.

Additional sources:
- [Maui DWS projects and reports](https://www.mauicounty.gov/3096/About-Us)
- [2025 Mahi Pono agricultural context](https://www.mauicounty.gov/DocumentCenter/View/155515/26-SEPT_Item-No-4dii_-Water-Efficiency-Report-Q2-2025-BLNR-Report)
- [UH research on data-center cooling in Hawaiian climate](https://www.hawaii.edu/news/2026/07/13/ai-data-center-cooling/)
- [Maui County landscape-water requirements](https://library.municode.com/hi/county_of_maui/codes/code_of_ordinances?nodeId=TIT14PUSE_ART1WA_CH14.12WAAV)
