# Atlas Lattice / ORCS — Kapalua Resort + West Maui Community Micro-Hauler Pilot v0.7

**Date:** 2026-10-15  
**Status:** PROPOSED / MODEL-SCENARIO / ZERO REALIZED CREDIT  
**Geography:** Kapalua, Nāpili, Honokōwai, Kāʻanapali, Lahaina (West Maui).  
**Versioning:** Additive to [Maui v0.6 micro-haulers](maui-community-microhaulers-large-generator-v0.6-2026-10-15.md) and [v0.5 distributed collection](maui-distributed-collection-bioreactors-polygone-v0.5-2026-10-15.md). None of the preceding sources is overwritten.  
**Companion scenario script:** [maui_kapalua_westmaui_pilot_v07.py](maui_kapalua_westmaui_pilot_v07.py).  
**Governance:** no agreement, endorsement, project approval, property access, installed-system claim, verified savings, or realized earnings attributed to any resort or community.

## 0. Executive decision

Select **The Ritz-Carlton Maui, Kapalua** as a specific, *unaffiliated* first resort for a public-information-only comparison; select a **1,400-household weekly collection catchment** as an initial hypothetical West Maui customer base. These are two distinct accounting boundaries connected to a possible local hub, not 1,400 real customers or resort-approved service.

**Most useful finding:** an attractive, code-checked rooftop/parking-canopy **biosolar** system could plausibly cover a material but not complete part of a luxury hotel's modeled annual electricity, while household pickup revenue supports resident-paid work and a clean materials/compost stream. A single resort plus 1,400 subscribed homes, **under conservative shared-hub assumptions, do not finance a standalone $1.5 million treatment hub alone**. Thus model shared incumbent processors, modular hubs, broader commercial procurement, and phased capital investment before announcing a profitable 5-to-10-year payback.

**Primary targets:** beautiful, ecologically respectful landscapes; affordable local service; nutrient/microplastic runoff avoidance; soil restoration; safe local manufacturing; marine health and jobs that remain on island. Hotel satisfaction is an *additional testable output*, not license to assume higher booking rates.

## 1. Resort identity and evidenced current efforts

**The Ritz-Carlton Maui, Kapalua**, 1 Ritz Carlton Drive, Kapalua, on 54 tropical acres.

- The **official Marriott page** says **468 rooms and suites**, six dining experiences, two nearby golf courses (not automatically hotel-controlled acreage), an organic garden, meeting/event facilities, spa and pools. A separately run resort marketing site uses **466 rooms**, so **468** is the v0.7 model default, and room count must be confirmed before any quote.
- Marriott's official sustainability disclosure states **Green Key Eco-Rating certification**, **26.25 kg CO₂e/room-night**, **1,962.08 liters water footprint per room-night**. These are hotel-reported figures, not a published 12-month water-meter dataset, and do not prove site-specific energy emissions or green certification scoring boundaries. The official Marriott site documents community conservation projects, including Puʻu Kukui watershed and Hui O Waʻa Kaulua support.
- A separate resort booking/marketing site states 80% LED lighting and electricity sourced entirely from renewable energy; this claim is **not the same as documented on-site generation, grid independence or proof of new savings**. Require Marriott/utility evidence on contracts, existing rooftop systems and REC ownership.
- The region's February 2026 **hotel occupancy 76.3%** was officially reported, and is **one month regional performance, not the Ritz's 2026 annual occupancy**. Use **72% annual assumed** baseline, 60–85% sensitivity.

Primary references:
- Marriott official hotel: https://www.ritzcarlton.com/en/hotels/jhmrz-the-ritz-carlton-maui-kapalua/overview/
- Marketing FAQ (room discrepancy and renewable energy claim): https://theritzcarltonmaui.com/rooms-and-suites/
- Hawaiʻi DBEDT February 2026 regional occupancy: https://dbedt.hawaii.gov/blog/26-12/

## 2. Electricity: room-scale reference and rooftop-area-constrained biosolar

**Important boundary:** Do not assume a 54-acre hotel parcel is available for photovoltaics; ecological/cultural buffers, resort vistas, beach environment and golf stewardship limit usable area. No aerial CAD, scanned roof polygon or solar installation inventory was available for this iteration.

### 2.1 Hotel electricity load: modeled, not billed

An external 2025 tropical luxury-hotel study reports roughly **22,184 kWh per AVAILABLE room per year** for a sample of upscale hotels; this is a cross-country analogy, not a Maui meter. Model 12k / 20k / 28k kWh per available room-year including attributed common areas, kitchens, cooling, pumps and amenities; **do not add an additional occupancy energy multiplier to these room-year values**.

| Resort electricity scenario | kWh per available room-year | 468 rooms annual electricity |
|---|---:|---:|
| Lean | 12,000 | **5.616 GWh** |
| Reference | 20,000 | **9.360 GWh** |
| Intensive | 28,000 | **13.104 GWh** |

Observed Maui resort load, demand peaks, hot water fuel and grid electricity share remain **UNKNOWN**. Use 12–24 months of actual utility bills, half-hour interval data, and any fuel/renewable contract disclosure to close the baseline.

Source for analog: https://www.mdpi.com/1996-1073/18/11/2788

### 2.2 Roof-plus-shade-canopy model (square footage, not arbitrary land coverage)

US NREL planning guidance suggests roughly **15 W of DC panels per square foot of panel-covered surface**, with **50–70% of many non-flat roof surfaces** potentially coverable. Local design must independently consider roof material, equipment, setbacks, wind uplift, fire access, corrosion, historic/cultural vistas and shading. **Square footage below is an UNMEASURED hypothesis, not architectural property data**.

| Design surface | Gross area assumed | Net panel-covered fraction | Panel area | Rated solar |
|---|---:|---:|---:|---:|
| Building rooftops | **90,000 ft²** | **60%** | 54,000 ft² | **810 kWdc** |
| Parking/service canopies | **60,000 ft²** | **65%** | 39,000 ft² | **585 kWdc** |
| **Combined** | 150,000 ft² | — | 93,000 ft² | **1,395 kWdc** |

Calculate:

`PV kWdc = gross sq ft × usable fraction × 0.015 kW/sq ft`.

**Maui sun resource vs generation:** Hawaii State GIS provides mapped annual/daily **GHI** from 10-km cells, measured in **kWh/m²/day**. NREL PVWatts uses roof orientation, weather, system design and loss to derive **kWh/kWdc/year**. These are not the same quantity. No precise Kapalua grid cell or PVWatts run was independently obtained, and wetter/windier Kapalua may differ from sunny Lahaina/Kīhei. Model **1,400 / 1,600 / 1,750 kWh/kWdc/year**, explicitly as a *sensitivity range*, not a verified Kapalua sunshine statistic.

At **1,600 kWh/kWdc-year**:
- Rooftop: **1.296 GWh/year**.
- Canopies: **0.936 GWh/year**.
- Combined: **2.232 GWh/year**, equivalent to **23.85%** of hypothetical 9.360 GWh hotel load before hourly consumption timing, shading and output curtailment.
- At assumed **85% on-site self-use**, **1.897 GWh/year** avoids purchased power, conditional on current tariff and actual meter.
- At illustrative **$0.338/kWh**, gross avoided volumetric electricity charges ≈ **$641k/year**, not verified savings. DBEDT reported Hawaiʻi statewide **2025 non-residential average ~33.8¢/kWh**; Ritz tariff/energy contract and demand charges unknown.
- At hypothetical **$3.00/Wdc**, PV CAPEX ≈ **$4.185M**, annual PV operating allowance 1.5% = **$62.8k**, PV-only simple payback **~7.23 years** *if* full assumed value is realized. No incentive, interconnection, financing, degradation, replacement, insurance or roof reinforcement modeled; battery optional.
- Optional **2 MWh** storage at assumed **$500/kWh** adds **$1M** upfront and may improve resiliency, but no extra battery revenue or lower grid charges is credited until hourly dispatch modeling.
- HSEO, NREL and HECO hosting-capacity documentation must guide feasible site-specific PV; locally installed PV and renewable procurement are unknown.

Relevant technical sources:
- NREL PV roof-area guidance: https://www.nrel.gov/docs/fy24osti/90582.pdf
- Hawaii solar radiation layer: https://geodata.hawaii.gov/arcgis/rest/services/Climate/MapServer/29
- NREL PVWatts: https://pvwatts.nlr.gov/pvwatts.php/
- HECO Maui hosting-capacity map: https://www.hawaiianelectric.com/products-and-services/smart-renewable-energy-programs/locational-value-maps/maui-county-locational-value-map-%28lvm%29
- Hawaiʻi statewide 2025 non-residential retail electricity average: https://governor.hawaii.gov/newsroom/news-release-dbedt-releases-2025-state-of-hawaii-data-book/

**Design preference:** roof-first; tasteful screened utility/storage areas; solar-covered dropoff, loading docks and staff parking where physically feasible; storm-rated shaded service spaces integrated with native, fire-safe planting. Guard existing solar and shade-grown ecology; refuse canopy locations that harm historic character or sacred sites.

## 3. Water and reclaimed-water opportunity

Marriott water footprint **1,962.08 liters per room-night** × 468 rooms × 72% occupancy × 365 ≈ **241.3M liters (63.75M US gallons)/year**, or ~**0.175 MGD annual-average equivalent**, under *assumed* occupancy and uniform footprint.

**This is extrapolation of a resort-published footprint, NOT a measured annual meter record.** Do not label all water as potable; identify water source and category separately.

Scenario reuse 25% of the proxy annual amount → ~**15.94M gallons/year**, **only if** sufficiently treated, permitted, safely distributed and matched to actual nonpotable cooling/irrigation/toilet/landscaping demand. Account for saline irrigation soil injury, reclaimed-water regulation and water quality. Keep golf-course water consumption OUT unless measured contracts show resort ownership/use. Count gallons reused only once as avoided purchased or abstracted water.

## 4. Waste and organics — reconcile FULL resort streams and existing diversion

For 122,990 modeled annual occupied room-nights, assume **2.5 kg of hotel operational mixed waste per occupied room-night** = **307.5 metric t/year**, of which **0.9 kg food-related subset** = **110.7 metric t/year**. This scenario is **not Ritz waste data**, and the food fraction is **included**, not added, in the 307.5 tonnes. Add *separately collected* landscaping/green waste **100 t/year** assumption for a combined waste reference **407.5 metric t/year**. No golf course or public park waste included unless under a signed separate service boundary.

External hotel waste studies give order-of-magnitude analogs but vary sharply by property type, guest count and convention/festival volume. Empirical Ritz sorting/hauler tickets, kitchen inventory, packaging, glass, paper, metals and resort landscaping volumes are required. Any existing resort recycling or on-site recovery is subtracted before *incremental* diversion is credited.

| Material fraction | Annual midpoint scenario (metric t) | Candidate fate |
|---|---:|---|
| Food/restaurant organics within operational waste | **110.7** | Food prevention/donation first; enclosed bioreactor or legally compliant compost |
| Other operational mixed waste | **196.8** | Glass/PET/HDPE/cardboard/metal separated by weighed sort; fraction recoverable UNKNOWN |
| Separate grounds vegetation | **100** | Mulch and compost where appropriate, no diseased/invasive plant relocation without controls |
| **Total assumed** | **407.5** | Clean residuals identified, zero implicit full diversion |

**Potential compost mass:** (110.7 + 100) t organics × 35% assumed finished wet compost yield ≈ **73.7 t/year**, not nutrient tonnes or marketable product without testing. Do not also claim complete biogas energy from the same mass. Plastic/PFAS fragments must be removed before agricultural application; verify local soil and nutrient offtake.

**Corrects prior v0.5 modeling:** its resort assumption 350 kg per stop × 156 stops/year = **54.6 tonnes/year per resort**. That is unlikely to describe *all* streams at a 468-room full-service hotel, so v0.7 uses **weights per actual ton and adequate commercial collection vehicles**, not residential truckbeds. At 5 visits/week, 407.5 t/year implies ~**1.57 t/visit**, which could require dedicated commercial vehicles, roll-offs and multiple segregated streams.

Analog studies:
- Hotel waste quantity and food fractions: https://pmc.ncbi.nlm.nih.gov/articles/PMC11564243/
- Hotel guest-room+restaurants solid waste: https://research.polyu.edu.hk/en/publications/environmental-accounting-of-municipal-solid-waste-originating-fro/

## 5. West Maui residential local-truck pilot

**1,400 subscribing HOUSEHOLDS are assumed, not counted subscribers or the island's full residential market**. Census-based prefire/ACS place approximations: Lahaina CDP **2,960 households 2020–24 ACS** and Nāpili–Honokōwai CDP **2,536**; these are not guaranteed current occupied/accessibly served households after the fires. The University of Hawaiʻi 2026 recovery panel confirms ongoing displacement. No conversion rate derived from those figures.

Reference weekly plan:
- **1,400 participating homes**, one pickup per week → **72,800 household visits/year**.
- Resident fee **$15/visit** → **$65/month equivalent** (52 weeks/12).
- **$14 direct visit cost** comprising $8 gross local operator labor, $4 reimbursed truck fuel/insurance/wear, $2 depot receipt (assumed, must verify).
- Annual collections: **$1.092M revenue** vs **$1.0192M direct costs** → **$72,800 route margin before dispatch administration, enterprise overhead, processor cost and capital**.
- **9 kg of dry + organics per residential collection** → **655.2 metric tonnes/year** (not verified).
- **72,800 household stops / 8 stops/hour** → **9,100 route-hours/year**, equivalent to **5.06 full-time-equivalent route jobs** at 1,800 hours/year or ~**7 five-hour truck shifts per workday**, Monday–Friday.
- Operator gross pay envelope in this example: **$582,400/year**, corresponding to $64 per productive route hour if every hour truly achieves 8 delivered stops. Neither hourly pay nor 5 FTE is a guaranteed job contract; gig classification, insurance, payroll, labor standards, qualification and transfer duties must be verified.
- For informal pickup trucks: use sealed, anchored, leakproof containers and load securement; do NOT transport mixed oils, wildfire debris, untreated medical waste, industrial brine or unpermitted hazardous material; high-volume hotels require suitable commercial trucks.

The household subscriber base may expand only when actual route prices, resident affordability, accessibility, route density, safe depot use and preservation of existing local hauler livelihood have been demonstrated.

Sources: https://www.census.gov/quickfacts/fact/table/lahainacdphawaii/HSD410223
https://www.census.gov/quickfacts/fact/table/napilihonokowaicdphawaii/RHI725224
https://uhero.hawaii.edu/economic-and-housing-recovery-three-years-after-the-maui-wildfires-findings-from-the-maui-recovery-survey/

## 6. One-resort + households: conservative integrated financial test

**Separate clean streams; no hidden subsidies or grants:**
- Resort 5 visits/week × $500/visit = **$130,000/year service income**, with assumed $250/visit fully loaded collection cost = **$65,000/year route contribution**.
- Homes route contribution = **$72,800/year**.
- Combined material **407.5 t resort + 655.2 t homes = 1,062.7 t/year**. At assumed **$80 per metric tonne of NET material/compost contributions after each processor's full incremental operating costs**, contributes **$85,014/year**. Absolutely **NOT** market price or verified material sales.
- Shared hub/admin operating cost **$120,000/year** (assumed separate from processor costs) → annual cash before hub capital **~$102,814**.
- Hub CAPEX **$1.5M**; 7% financing/recovery assumption, 10-year CRF ~0.142378 → **~$213,566/year** capital recovery.
- **Annual financial deficit ~−$110,752 after a 10-year annuitized capital recovery**, before any additional excluded costs. This **does NOT** support a claim that one resort+1,400 homes alone pays for a new hub.
- Existing permitted hubs and bioreactor/metal-plastic processing equipment may reduce capital; 2–3 more comparable hotels or signed institutional waste contracts could increase revenue, but their cost, supply and environmental performance must be recomputed, not simply multiplied optimistically.
- Critically, a resort's electricity and water benefits belong to its own energy investment cash flow and cannot subsidize the separate local pickup firm unless a signed service/financing arrangement transfers some value.

**Sensitivity levers:** measured resort waste tickets; separate compost sales vs import displacement without double counting; nonhazardous polymer-grade yields; existing permits and local hauler agreements; grant-backed resident subsidies only if awarded; consumer willingness to pay; delivery and freight for island materials; 100% utilization from Year 1 is unrealistic.

## 7. Guest satisfaction, perceived green value and resident legitimacy

### Verified external baselines — *different populations, not Ritz-specific outcomes*

- Hawaiʻi Tourism Authority's Maui 2026–28 Destination Management Action Plan reports **70.8% of Maui visitors in 2025 rated visits excellent**. Maui residents in the 2025 sentiment survey: **45% said tourism benefits exceeded problems**, **37% felt they had a voice in tourism decisions**. These measure broad visitor/resident experience, **not Ritz guest satisfaction or green-property uplift**.
- Booking.com's 2026 global research reports **85% of travelers say sustainability is important** and **36% plan to choose sustainability-certified accommodation**, with 2025 >100 million certified-accommodation room-nights booked on its platform. Survey intent and platform statistics are **not** evidence a specific Kapalua resort earns a rate premium or improved occupancy.

Sources:
- HTA Maui D-MAP: https://hta.hawaii.gov/what-we-do/plans-reports/dmaps/maui-dmap-2026-2028/
- Booking.com 2026 report: https://news.booking.com/bookingcoms-latest-travel-and-sustainability-research-reveals-unexpected-generational-paradox/

### Proposed independently testable KPIs

| Stakeholder | KPI and instrument | Baseline/status | Direction |
|---|---|---|---|
| Resort guests | Post-stay overall satisfaction / NPS; question specifically on visible native biosolar landscape | **Not yet measured**; guest survey and CRM | Improve vs control hotel and historical seasonality |
| Resort guests | % selecting sustainability-certified stay, and verified booked-rate difference from randomized comparable listing experiments | **Unknown Ritz effect** | Positive only if measured in observed booking behavior |
| Resort guests | Beach/reef cleanliness perception, scenic views, shade/heat comfort; accessibility | Baseline site survey required | Improve without disturbing beach ecology |
| Local residents | Affordability: average voluntary pickup charge, missed pickups, recorded litter complaints, heavy-truck movements | Baseline required | Low burden, accessible service |
| Local residents | % saying tourism benefits exceed costs / meaningful local voice in tourism development | HTA 2025 **45% / 37% Maui-wide**, not pilot baseline | Positive changes, community-led measurement |
| Ecology | Nutrient/particle load intercepted *before* coast, reef/pH trends, beach bacteria | Before/after paired field measurements | Net pollutant reduction; ecological veto |
| Local employment | Paid wages, driver hours, full-time equivalent jobs, retention and benefits, operators' ownership | **0 VERIFIED PROJECT JOBS** | Positive demonstrated payroll |

**Prevent fake guest-satisfaction credit:** hotel ratings are sensitive to price, staffing, weather, airline access, wildfire recovery and room quality. Use comparison properties, matched seasonality, guest A/B tests and independently verified local spending. Do not assign a dollar value to 85% survey intent, and do not count marketing claims as clean-water outcomes.

## 8. Priority data requests and 60–90-day pilot concept

1. **Property energy:** operator-permitted 24 months electricity and fuel invoices, hourly or half-hour interval loads, solar/REC procurement, backup and outage records, separate adjacent golf operations.
2. **Physical roofs:** current aerial GIS polygons + structural roof schedules + electrical as-builts; PVWatts (Kapalua coordinates) with monthly NSRDB weather, shading, hurricane uplift, salt corrosion and coastal glare checks; model canopy area from actually available legal parking/servicing space, not resort land area.
3. **Water:** resort meter totals / hotel vs golf split, swimming pools, irrigation, laundry, restaurant, sewage output and treated reuse permits.
4. **Waste:** 2–4 weeks per stream of weighed hauler tickets, organics composition lab, glass/cardboard/aluminum/resin records, kitchen reuse and existing diversion contracts; zero assumption of resort partnership.
5. **Residential:** 150–300 voluntary subscribers in two neighborhoods with several locally owned/insured pickup routes; record stop-hours, failed pickups, vehicle costs, wages, weights, landfill and certified downstream destinations, material contamination and resident satisfaction.
6. **Shared hub:** partner with permitted local facilities before new construction, test bioreactor organics product for food-soil safety and actual agriculture offtake.
7. **Community:** Native Hawaiian and West Maui resident stakeholders and existing haulers must be included in governance before regulatory proposals, public branding or siting; prioritise local families and sustainable wage protections.
8. **Funding:** federal or island resilience grant as conditional external funding only, not booked project revenue; independently priced solar/building investment separate from hauling cash flow.

**End state:** a verifiable, attractive, culturally grounded commercial-residential loop whose actual meter readings, tickets, resident jobs, and ecological outcomes can support cost recovery and gradual scaling across Maui without unsupported promises of free resort utility service.
