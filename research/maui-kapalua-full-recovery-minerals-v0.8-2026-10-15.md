# Maui / Kapalua Comprehensive Resource Recovery and Mineral Ledger v0.8

**Atlas Lattice / Open Regenerative Compute Standard (ORCS)**  
**Date:** 2026-10-15  
**Status:** DERIVED + SCENARIO, NON-CANON UNTIL VERIFIED, ZERO REALIZED CREDIT  
**Geographic boundaries:** (A) hypothetical one-resort source-sorted material balance at The Ritz-Carlton Maui, Kapalua; (B) conditional resort water/wastewater proxy; (C) **separate** hypothetical 5-MGD seawater desalination reference serving West Maui, not belonging to the hotel. **NEVER add these capacities or credit a mineral stream to the resort.**  
**Versioning:** supplements and corrects [v0.7](maui-kapalua-resort-westmaui-biosolar-microhaulers-v0.7-2026-10-15.md); v0.7 remains intact. Also preserves all previous v0.2–v0.6 work.  
**Executable source:** [maui_kapalua_full_material_mineral_balance_v08.py](maui_kapalua_full_material_mineral_balance_v08.py).

## Executive correction: 74 tonnes did NOT derive from 410 tonnes of food

The v0.7 resort scenario assumes **468 rooms**, **72% occupancy**, **122,990 occupied room-nights/year** and **2.5 kg/occupied room-night of TOTAL solid waste** (a scenario, not actual resort weighing). That yields **307.48 metric tonnes of hotel operational waste**, within which **110.69 tonnes** are food. Another **100 tonnes of landscaping/green waste** is separate, yielding **407.48 tonnes of all waste**.

Prior compost estimate: **(110.69 food + 100 green) × 35% finished wet compost = 73.74 t/year**. It does NOT claim 410 tonnes of food or a full 410-tonne input to compost.

A published U.S. food-waste life-cycle dataset (2024) uses ~**48% average mass loss**, with **22–70%** range depending on operations and source, corresponding to a **52% default wet compost yield** with a wide **30–78%** sensitivity range. Those food-waste-derived factors are only provisional for food-plus-green blends; local moisture, bulking agents, curing and screening must be measured.

**Revised 210.69-t organic feed:**
- 35% yield: **73.74 t/year** original
- 52% yield: **109.56 t/year** working reference
- 78% upper sensitivity: **164.34 t/year**
- If **410 t/year were actually ALL compostable food waste** (contrary to v0.7), 52% gives **213.2 t/year** finished wet compost, before added amendments/contamination.

Source: [2024 Food waste end-of-life management: parameterized datasets](https://doi.org/10.1016/j.dib.2024.111174); [EPA composting](https://www.epa.gov/sustainable-management-food/composting).

## 1. Resort source-to-product full solid-waste ledger

### 1.1 Explicitly assumed intake composition

| Disjoint intake category | Tonnes/year | Grounding |
|---|---:|---|
| Kitchen/restaurant food scraps | **110.69** | 0.9 kg per occupied room-night, entirely SCENARIO |
| Separately generated landscape organics | **100.00** | SCENARIO; excludes independent golf-course operations |
| Paper and cardboard | **70.00** | Allocated portion of remaining hotel solid waste; NOT sampled |
| Glass | **45.00** | Allocated portion; NOT sampled |
| Plastics (mixed grades) | **40.00** | Allocated portion; NOT sampled |
| Metals (mixed Fe/Al/others) | **14.00** | Allocated portion; NOT sampled |
| Textiles | **10.00** | Allocated portion; NOT sampled |
| Residual mixed/unrecoverable | **17.78** | Reconciliation remainder; NOT sampled |
| **TOTAL** | **407.48** | Sum matches resort scenario |

**Note:** 2.5 kg per occupied room-night is a hypothetical *property operations allocation*, not the actual branded resort's weighed receipts. Existing recycled/donated amounts and third-party service streams must be subtracted in an incremental study; the hotel has documented existing conservation practices. Water, wastewater, solar energy and seawater minerals are separate ledgers, not components of 407.48 t solid waste.

### 1.2 Conversion pathways (52% compost mass yield)

| Input | Input tonnes | Hypothetical physical output | Output t | Loss/residue t |
|---|---:|---|---:|---:|
| Food + green | **210.69** | Finished screened wet compost | **109.56** | **101.13** evaporation, biogenic CO2, other gases and process loss (not zero emissions) |
| Paper/cardboard | 70.0 | Recovered fiber @ 85% | **59.50** | **10.50** |
| Glass | 45.0 | Clean cullet/graded glass @ 90% | **40.50** | **4.50** |
| Plastics | 40.0 | Sortable polymer flake/pellets @ 60% | **24.00** | **16.00** |
| Metals | 14.0 | Graded recyclable Fe/Al/other scrap @ 90% | **12.60** | **1.40** |
| Textiles | 10.0 | Unassayed, no product booked | **0** | **10.00** |
| Mixed residual | 17.78 | No product booked | **0** | **17.78** |
| **TOTAL** | **407.48** | **Recovered direct product** | **246.16** | **161.32** (101.13 organic mass loss + 60.18 dry rejects) |

**Wet-mass** recovery = **60.4%** physical recovered products divided by initial incoming mass. That percentage is not a GHG reduction score and understates organic conversion to non-solid streams; does NOT imply 39.6% landfill disposal. Screened rejects can contain some future recoverables, but none should be counted without actual proof. Safe processing, export/buyers, contamination and pickup logistics remain essential.

### 1.3 Candidate local products

**Compost** for Kula, West Maui and Central Maui farms/landscaping once tested for crop-compatible EC, pH, NPK, C:N, maturity, pathogens, microplastic particles, perfluoroalkyl chemicals as relevant, metals and herbicide residues. **Fiber** repulped or baled and exported if island manufacturing is uneconomic. **Glass** cullet, tested sand/pozzolan substitute, mosaic or ceramic products where standards allow. **PET/HDPE and qualified other polymers** wash/extrude to nonstructural 3D-print components, tested panels or durable utility parts. **Aluminum/steel/copper** graded, reused/remanufactured under appropriate standards, not random mixed-metal reinforcement for load-bearing homes. **Textiles** prioritized for laundering/repair/resale where sanitary.

Environmental QC: capture processing-water microplastics and airborne shredding fibers; clean fire debris/hazardous waste not introduced into building feedstock; discharge and residual disposal governed by permits. Count actual import substitution only after matching the local buyer's product specification and price.

## 2. Food/green bio-resource routes: mutually exclusive baseline alternatives

### Route A — In-vessel aerobic composting (v0.8 default)

- Total input **210.69 metric wet tonnes/year**.
- Finished compost reference **109.56 wet tonnes/year**, range **63.21–164.34 t/year** using 30–78% yield.
- Biochemical losses ~**101.13 tonnes wet mass** at 52% output; split into water/CO2/leachate and trace gases only after actual measurements.
- Total elemental N/P/K **in compost from FOOD INPUT ONLY**, modeled from the 2024 U.S. LCI: **N ~1.097 t, P ~0.156 t, K ~0.308 t**. These are product nutrient content estimates, NOT fertilizer-grade product mass. Green waste contributes additional yet-unsampled nutrients and stable organic matter.
- Compost value is often as important as **soil carbon, infiltration, water retention, erosion control, landscape resilience and reduced nutrient runoff** as fertilizer substitution. Those environmental outcomes need measurements; do not price them automatically as credits.
- **If all 410 tonnes were food instead**, 2024 food-only per-input-tonne LCI gives compost nutrient equivalents ~**4.06 tonnes N, 0.58 tonnes P, 1.14 tonnes K**; in the actual baseline, food is only 110.69t.

### Route B — Anaerobic digestion of FOOD fraction only, remaining green waste composted

- **Food feed 110.69 wet tonnes/year**. EPA / EBMUD wet-food study reports roughly **75–135 m³ of methane per wet metric tonne** under specific digester conditions; scenario methane production **~8,300–14,900 m³/year**, approximately **83–149 MWh/y thermal LHV** at ~9.94 kWh/m³ methane.
- At assumed **30–35%** gross electrical conversion, **~25–52 MWh/year GROSS electricity** before reactor electricity/heat demand, maintenance, methane leaks and engine economics; inadequate to power the resort's ~9.36 GWh hypothetical annual electricity, but useful to compare local hub co-digestion.
- **AD produces digestate, NOT finished compost.** Post-treatment digestate can supply separated nutrients and composted solids if permitted; its actual wet/dry quantity and quality require analysis. Some wastewater nutrients may be recovered as struvite or ammonium concentrate.
- **Green waste 100 tonnes** may instead compost separately to approximately **52 t finished wet compost**, with unknown additional nutrient content. That compost is *not* 109.56 t if 110.69 t food is diverted to AD. Any finished digestate compost requires its own mass-balance assay.
- Never count complete compost output for the 110.69 t food **and** all of its methane output.

Sources: [EPA 2008 EBMUD wet-food digestion pilot](https://www.epa.gov/system/files/documents/2024-08/ebmud-final-report-anaerobic-digestion-of-food-waste-2008-03.pdf), [EPA AD basic](https://www.epa.gov/anaerobic-digestion/basic-information-about-anaerobic-digestion).

## 3. Resort water footprint and CONDITIONAL nutrient reclamation

Official Marriott hotel webpage discloses a **1,962.08 liters water footprint per room-night**, not independently verified metered wastewater. At assumed **122,990.4 annual occupied room-nights**: **241.32 million liters = 63.75 million gallons/year**, of which **25% treated nonpotable beneficial reuse** would hypothetically displace **15.94 million gal/year** if safely permitted, with actual demand and seasonal storage.

For an illustrative nutrient screen only, **75% of footprint is hypothetically sent to a recoverable wastewater stream**: **181,000 m³/year** / **47.81 million gallons/year**. Those flows are not verified resort sewer meters or owned reclamation assets; the effluent may enter shared county systems.

**Hypothetical wastewater influent concentration assumptions, NOT samples:** total nitrogen **30 mg/L**, phosphorus **5 mg/L**, Mg/phosphate speciation unknown.

| Species / resource | Gross hypothetical flow | Assumed processing | Feasible upper scenario output before purity/permits |
|---|---:|---|---:|
| Water | 63.75M gal water footprint | 25% beneficial nonpotable substitution | **15.94M gal/year** if legal and useful |
| Wastewater total N | **5.43 t N/year** | 50% modeled net nutrient recovery | **2.71 t elemental N/year** across ALL N products |
| Wastewater total P | **0.905 t P/year** | 60% to recoverable orthophosphate and crystallization, unrealistically generous unless speciation allows | **0.543 t elemental P/year** in struvite |
| Struvite MgNH4PO4·6H2O | — | 1:1:1 Mg–NH4–PO4 molar balance | **4.30 t product/year**, requires magnesium supply and product quality |
| Nitrogen INSIDE that struvite | — | ~5.7% by mass | **~0.245 t N**, **included** in the 2.71 t total N (not additional) |
| Magnesium INSIDE struvite | — | ~9.9% by mass | **~0.426 t Mg**, sourced from wastewater or separate reagent; not automatic local recovery |
| Other hypothetical N product | — | rest of 2.71t N recoverable | **~2.47 t N** in e.g. ammonium concentrate (NO mass of formulated product credited) |
| Secondary recycled graywater | included within total water flows | Need separate safe plumbing and permit | Not counted twice with total 15.94M gal |

**Scientific controls:** not all total P is orthophosphate or chemically available for struvite, and not all N is ammonium. Municipal treatment has nutrient removal options that may discharge N2 without selling a fertilizer. For marine health, nutrient pollutants **avoided reaching the reef** must be independently measured and separately labeled, not assumed equal to nutrient recovered.

If a resort sewer stream is combined with Lahaina municipal wastewater, nutrient recovery belongs to the shared plant ledger only, with resort attribution based on measured source shares; no double-counting between resort and municipal water.

Source: [2026 struvite recovery review](https://www.sciencedirect.com/science/article/abs/pii/S221471442502327X), [Marriott disclosures](https://www.ritzcarlton.com/en/hotels/jhmrz-the-ritz-carlton-maui-kapalua/overview/).

## 4. Standalone West Maui / Maui island reference desalination mineral refinery

**VERY IMPORTANT:** All mineral quantities in this section refer to an independent hypothetical **5 million gallons/day finished seawater desalination reference case**, not the Ritz-Carlton, its organics, or its own wastewater. Source chemistry uses representative ocean seawater from USGS, **not assayed Maui well water**. Candidate Maui groundwater, brackish or ocean intake may have very different mineral grades.

At **45% reverse osmosis recovery**, estimated **42,060 m³/day intake**, **18,927 m³/day water product**, **23,133 m³/day concentrate**. Electricity at **3.5 kWh/m³ finished freshwater** is **24.18 GWh/year**, BEFORE auxiliary distribution, mineral refining or final concentrate management.

Representative **theoretical elemental/ionic inventories entering seawater plant** (not saleable production):

| Element / ion | Concentration mg/L | Input elemental/ion tonnes/year | Potential distinct products |
|---|---:|---:|---|
| Sodium (Na) | 10,500 | **161,200** | NaCl, NaOH or carbonates where reagent balance allows |
| Chloride (Cl) | 19,000 | **291,700** | NaCl, KCl, MgCl2; competing for the same chloride |
| Magnesium (Mg) | 1,350 | **20,725** | Mg(OH)2, MgCO3, Mg salts |
| Calcium (Ca) | 410 | **6,294** | Gypsum OR CaCO3 OR other calcium salts |
| Sulfate (SO4) | 2,700 | **41,450** | Gypsum or sulfate product, with competing divalent-ion use |
| Potassium (K) | 390 | **5,987** | KCl, K2SO4, other salts |
| Bromide (Br−) | 67 | **1,029** | Bromine derivatives; reagent and hazardous-handling constraints |
| Bicarbonate (HCO3−) | 142 | **2,180** | Carbonate and buffering chemistry; carbon balance required |
| Boron (B) | 4.6 | **71** | Borates, subject to process economics |
| Strontium (Sr) | 8 (typical scenario) | **123** | Specialized compounds only if demand/purity established |
| Lithium (Li) | 0.18 (typical scenario) | **2.76** | Trace research only; very low grades |
| Deuterium (D) | natural seawater isotopic abundance | ~**530 t/year elemental-D-equivalent in the WHOLE feedwater** | Research inventory only, mostly in water, not available brine solids; zero financial credit |

Representative salt mass: **~537,300 t/year** dissolved salts entering seawater feed at 35 g/L; with 0.5 g/L in finished water, **~533,900 t/year** salts remain in the concentrate. This is a mass inventory, not a demonstrated 534k-ton saleable-product refinery. Multiply recovery efficiencies only **after** ion-by-ion balances and pilot process results.

**Stoichiometric upper product alternatives (do NOT add as simultaneous attainable outputs):**
- Ca-limited **gypsum CaSO4·2H2O: ~27,000 t/year** theoretical, consuming recovered Ca and matching sulfate; needs product purity and soil-specific agronomic evidence.
- If Ca goes instead to **CaCO3: ~15,700 t/year** theoretical, not additionally the full gypsum.
- Mg-limited **Mg(OH)2: ~49,700 t/year** theoretical, requires OH/reagents and energy, not 49,700 t of metallic magnesium.
- K-limited **KCl: ~11,400 t/year** theoretical, requires chloride and extraction.
- Na-limited **NaCl: ~409,800 t/year** theoretical, competes for chloride with other chlorides and requires evaporative/reagent processing.
- Sulfate-derived **ammonium sulfate or sulfuric acid** could be explored only with nitrogen/reagent inputs and an independently validated chemical and thermal process; sulfates in seawater cannot be priced as free sulfuric acid.
- Lithium, bromine, strontium and deuterium may have high commodity prices in certain product grades, but extraction may be uneconomic; **zero booked revenue** without yields, grade, buyers, product transport and full lifecycle treatment.

**Zero liquid discharge:** the additional hypothetical **10 kWh/m³ of concentrate** stress test at 23,133 m³/day yields **~84.4 GWh/year** above RO, or about **$16.9M/year of electricity alone at $0.20/kWh**. This is neither a vendor estimate nor inevitable cost; selective mineral recovery, pretreatment, thermal integration, MLD alternatives, brine mineral streams and reclaimed-water reuse must be co-optimized. A ZLD plant creates solid residuals requiring custody and leachate prevention; ocean-first means minimum total ecological damage, not just removing a pipe from the seafloor.

Sources: [USGS average seawater composition](https://pubs.usgs.gov/circ/2003/circ1262/), [NOAA minor seawater species](https://repository.library.noaa.gov/view/noaa/39136), [Maui County desalination feasibility](https://www.mauicounty.gov/DocumentCenter/View/154964/Maui-Desalination-Feasibility-Study-ES-2024), [2025 brine-valorization research overview](https://www.nature.com/articles/s44359-025-00036-2).

## 5. Local-first agriculture and interisland circular supply

Prioritize **actual recoverable N, P, K, Ca, Mg, sulfur and organic carbon** from food scraps, agricultural crop residues, livestock manure, municipal effluent, aquaculture and source-segregated organics. Keep mineral ions from saline plant in separate material ledger; connect for product production only where real transfers and processing have occurred.

**Land-based product priority:** clean compost + mulch to improve Kula/Central/West Maui field infiltration/soil cover; test K, Mg and boron soil deficiency before adding saline salts; only apply gypsum to Ca/S-deficient or sodic soils where agricultural tests show benefit and leaching capacity exists. Test any reuse solution for sodium and chloride buildup and food safety.

**Interisland surplus:** Maui measured agronomic demand + resilient reserve → neighbor island demand and legally compliant freight → optional external sales. Shipping bulk moist compost or diluted digestate may destroy margin; dry concentrated fertilizers and purified salts can be more freight-efficient. Each product requires import displacement and product price independently. No speculative interisland contracts counted.

## 6. Financial sensitivity: resort feedstock value alone does not build the refinery

**Illustrative, NON-MARKET, gross product prices, not contemporary Maui quotations:**

| Recovered solid | Scenario t/yr | Hypothetical realized $/t | Gross annual product value range |
|---|---:|---:|---:|
| Finished compost | 109.6 | $100–250 | **$11.0k–27.4k** |
| Paper/cardboard | 59.5 | $30–150 | **$1.8k–8.9k** |
| Glass | 40.5 | $0–80 | **$0–3.2k** |
| Polymer fractions | 24.0 | $100–600 | **$2.4k–14.4k** |
| Metals (mixed) | 12.6 | $100–1,000 | **$1.3k–12.6k** |
| **Subtotal** | **246.2** | — | **~$16.5k–66.5k/year GROSS** |

**These prices are user-adjustable placeholders**, not verified product markets, actual incremental revenue or profit. Product certification, recycling handling costs, transport/export, bioreactor CAPEX, odor/leachate controls, worker wages, additional equipment and existing resort contracts may exceed gross sales. Disposal-cost avoidance may also matter if current contracted avoided costs are documented. No double-counting of material product sale and avoided imported replacement if only one economic transaction occurs.

**Separate resource effects, not cash for material processor without contract:**
- Marriott footprint proxy ~**63.75M gal/year**; if reuse could displace 25% legally and practically, **15.94M gal/year** water purchases/abstraction as a maximum scenario (at illustrative $0.01/gal marginal utility avoided cost = **$159k/year**, treatment costs not deducted). Resort tariffs, source and reclaimed equipment unknown.
- v0.7 assumes biosolar ~**2.232 GWh/year** gross. At 85% self-use and a hypothetical $0.338/kWh volumetric retail offset ≈**$641k/year** of gross avoided utility charges, excluding solar financing/capex and existing renewable contracts. **This energy benefit belongs to hotel's solar project only**, not automatically to compost, hauling, mineral recovery or community utility.
- Food-only AD **~25–52 MWh gross electricity/year** is only **~0.27–0.56%** of the hypothetical 9.36 GWh hotel load; scaling AD economically likely needs shared hub and additional organics, not a one-resort standalone grid solution.
- Mineral revenue cannot be assigned until assays, pilot recoveries, yields, chemical supplies, ZLD waste custody, buyer contracts, island demand, full energy and coastal environmental outcome evaluation. ZLD power penalty can outweigh bulk mineral values.

**Financial boundary invariant:** Commercial material recovery value = actual net cash product sales + separately verifiable avoided handling/landfill costs + separately verifiable imported material spending genuinely substituted (no overlap) − collection, processing, finishing, testing, distribution, residual and financing costs. Utility reduction and ecosystem gains are tracked with separate ownership and baselines.

## 7. Recommended receipt hunt / pilot and explicit next versions

1. Resort operator/hauler voluntarily supplies 4–8 weeks of scales by food, green, cardboard, glass, PET, HDPE, metal and remaining waste; count already diverted material so incremental outcomes aren't invented.
2. Test input food/landscape moisture %, total solids, volatile solids, N/P/K, salts, metals, microplastics, PFAS where relevant and compost maturity and pathogen screens.
3. Test three realistic routes (a) compost, (b) food AD + garden compost and digestate fractionation, (c) food waste prevention / edible donation + remainder compost; no overlapping chemistry or tonnage.
4. Source 12-month water flow and wastewater permit logs; measure ammonium, organic N, phosphate-P, Mg, Ca, chloride, pathogen and contaminant loads for feasible struvite/safe reuse.
5. Confirm clean local material pricing and actual packaging grades, landfill/tip fees, shipping, high-volume glass and EPS conversion opportunities.
6. Test actual **separate Maui desal feed** chemistry by source and sensitivity; produce independent zero/minimal liquid discharge process simulation and environmental life-cycle assessment.
7. Join resident local-truck pickup, resort hotel and public collection without falsely assuming service contracts or county grant ownership; quantify pay, haul hours, operator protections, waste cleanliness and community satisfaction.
8. Maintain reef pH, alkalinity, dissolved inorganic carbon, aragonite saturation, nutrients, microplastics and reef health monitoring **before** any experimental chemistry intervention.
9. Update v0.9 only after actual feedstock assays, bills, pilot runs and confirmed product off-take; preserve all source traces and prior versions.

**Conclusion:** The original 74-ton figure was not a calculation from 410 tonnes of food waste. A corrected 52% reference suggests ~110 tonnes of compost from ~211 tonnes of organics in an ~407.5-ton TOTAL waste stream. A complete local economy combines that compost with sorted fiber, glass, metals, polymers, measured nutrient recovery, beneficial reuse, biosolar energy, and a **separately scoped** seawater mineral-recovery refinery. Every stream must obey conservation of matter, chemistry and cash.
