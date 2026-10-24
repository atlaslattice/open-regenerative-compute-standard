# Atlas Lattice Corpus Christi
## Networked retrofit, desalination, landfill-mining and compute nodes

**Version 0.8 | 24 October 2026 | Public screening white paper**

Prepared for Dave Sheldon's Atlas Lattice / Open Regenerative Compute Standard research. This is a reproducible opportunity assessment, not a feasibility certification, supplier quotation, construction design or financing offer. Chinese equipment and process references are used for the proposed supply packages. Existing Corpus assets are retained as the service baseline. Imported comparison prices are preserved in the appendix but excluded from the proposed Chinese-supply package.

## 1. Executive assessment

The proposed system links four operating domains: an existing municipal/industrial reclaimed-water network; a new desalination and brine-products plant; a Desen-based landfill-mining and materials-remediation branch; and an optional compute campus. Biological processing is central to the architecture, with different bioreactors matched to clean organic wastes, wastewater and nutrient-release duties. It is not assumed that one biological process treats every stream.

The useful near-term question is whether selective extraction and polishing can be retrofitted around existing infrastructure while preserving its contracted water service. Water earmarked for industry remains a potential extraction feed: an upstream sidecar can remove selected constituents and return compliant water, subject to losses, chemistry, ownership and delivery obligations. That is different from claiming the water is unallocated or counting its reuse a second time.

The project is compared at zero additional large compute, 100 MW IT, 500 MW IT and a deliberately exploratory 1.21 GW IT case requested during preparation. The larger cases are illustrative hyperscale or "Stargate-scale" comparisons, not a proposed affiliation with Stargate or evidence of a committed customer. At assumed 90% average IT load and PUE 1.15, the 100/500 MW compute-only sites draw average 103.5/517.5 MW and consume 0.907/4.533 TWh/year. At an assumed $0.10/kWh, electricity alone is $90.7/$453.3 million/year. The 1.21 GW case reaches 10.971 TWh/year and about $1.097 billion/year in compute electricity. Compute can provide useful services and recoverable heat, but those revenues and benefits have not been established.

A 30 MGD desalination product block remains the reference water scale. At the retained screening recoveries, it produces 153,643 m3/day of combined RO and pretreatment residual liquid on operating days. No routine marine process-liquid release is permitted in the proposed design. Mineral extraction, further water recovery, chemical conversion, dewatering and qualified solid uses are candidates; they do not yet constitute a cleared final residual route.

Desen screening scenarios of 50 and 200 metric t/h give 96,000 and 384,000 metric tonnes/year of campaign feed at 8 hours/day, 300 days/year and 80% effective availability. These are screen-throughput sensitivities, not demonstrated complete-line performance. Current Desen specifications differ from earlier articles, and washing modules may bottleneck the line. No Corpus waste assay, net diversion percentage or approved recovered-fines use has been established.

The current evidence supports designing and quoting this network in modules. It does not support an all-in project price, guaranteed payback, zero final residuals, or a claim that either compute scale is net positive. Those fields remain explicitly unresolved.

## 2. Research boundary and evidence rules

This paper extends the published v0.7 model, frozen at Git commit f0914a5b9f5be1febcdde30d52455b582c97bdd3 [S1]. It preserves historical Chinese price anchors and Corpus comparators without treating them as executable budgets. The new scenario script is self-contained and requires only Python's standard library.

Evidence is distinguished as: official reported asset or program; manufacturer-stated product capability; primary research or pilot result; user-supplied price needing original sourcing; analyst scenario; and unknown. An unresolved gate is neither a demonstrated failure nor a pass. Passing software tests validates bookkeeping, not treatment performance.

"Chinese supply reference" is not a certificate that every motor, membrane, electronic component or alloy is Chinese-made. For several pump, evaporation and biological packages, the original vendor and bill of materials remain unknown. Proposed packages use Chinese candidates where identified; missing suppliers stay TBD. Actual U.S. installation, engineering, commissioning, import, certification and service costs remain null. A China-market price for an imported brand is not relabeled Chinese manufacture.

The paper uses MGD for million U.S. gallons/day, metric tonnes for model solids and salts, and 1 MGD = 3,785.412 m3/day. U.S. municipal reports using "tons" must be checked for short-ton conventions before comparison. MW IT nameplate, instantaneous site power, annual average power and recoverable thermal MW are separate quantities. All currency conversions use an assumed CNY7.25/USD, not a current FX quotation.

## 3. Corpus infrastructure that can be reused

### 3.1 Municipal water and existing industrial reuse

The city's wastewater service document reports an average 28 MGD across six plants and explicitly includes residential, commercial and industrial sewer sources [S2]. Separately permitted industrial discharges may provide additional opportunities, but measured flow, internal/outfall overlap, existing reuse and rights remain unverified. A partial sum of permit limits is not a regional resource ceiling.

On June 30, 2026, the city announced a $107.5 million Phase 2 construction contract for Oso-to-Greenwood reclaimed-water conveyance, pumping and associated works. The stated addition is 11 MGD, bringing the program to as much as 16 MGD; completion is scheduled for May 2027 [S3]. This is a project under delivery, not proof of present 16 MGD flow. The engineering provider also identifies storage and an industrial-reuse connection [S4].

The Valero agreement provides initially up to 3 MGD and later up to 8 MGD following infrastructure improvements. It includes treatment-related and O&M reimbursement provisions [S5]. The full 16 MGD program should not be equated with this one customer's contractual allocation. Nor does 28 minus 16 prove that 12 MGD is available to Atlas.

**Retrofit interpretation:** nutrients or other compounds can potentially be recovered before industrial delivery, with water returned to the existing service chain. Existing water supply, committed customer value and planned pollution reductions remain in the counterfactual. Atlas credits only independently verified additional performance, net of added burdens.

### 3.2 Greenwood biology and nutrient access

The v0.7 source register records historical Greenwood activated-sludge treatment and anaerobic digestion alongside a city rehabilitation plan explicitly describing elimination of primary treatment and anaerobic digestion [S6, S7]. Current configuration and implementation status require confirmation. A retrofit dependent on digester centrate cannot assume the source survives the rehabilitation.

Bioreactor integration is broader than retaining a particular digester: mainline biological polishing, dedicated organic-waste digestion, biological phosphorus release and selected algal/fungal research routes can be evaluated independently. The design must say which existing or proposed vessel, feed and operating regime supports each route.

### 3.3 Existing solid-waste resource systems

Corpus has its own solid-waste assets, rather than an empty starting point. In July 2025, the city announced a $5.48 million compost-yard construction contract at Cefe Valenzuela, planned capacity of 120,000 tons/year, and a landfill-gas-to-energy operation reported to have started in April 2024 [S8]. Present compost throughput and available capacity require confirmation. Existing composting, gas revenues and diversion are baseline benefits, not new Atlas outputs.

The landfill is geographically separate from the proposed water network [S9]. No shared parcel has been selected. The regional network can integrate material products, reagents, suitable water, data and selected thermal duties without transporting raw garbage or sewage to a drinking-water or compute building. A site-specific layout must evaluate traffic, odors, dust, flood/storm surge, fire access, utility routing and ecological buffers.

## 4. Architecture: one ledger, several protected process circuits

| Node | Main duty | Candidate exchanges | Boundary that must remain explicit |
|---|---|---|---|
| Oso/Greenwood and industrial reuse network | Retain compliant reclaimed-water delivery | Nutrient sidecars, selective polishing, industrial makeup | Existing deliveries and quality cannot be silently reduced |
| Desalination node | Produce qualified water; concentrate seawater salts | Mg reagent, salts, water, acid/base candidates | Intake effects and all residuals remain accounted for |
| Landfill/materials node | Mine selected cells; sort and remediate qualified fractions | Metals, aggregates, clean organics, wash-water recovery | Excavation is not net diversion; hazardous fractions remain controlled |
| Biological node(s) | Treat organics; selected energy/nutrient recovery | Biogas, nutrient-rich liquor, qualified compost/biomass | Nitrification or digestion is not complete material recovery |
| Compute node | Useful inference/training, metering and process support | Temperature-matched heat, data, verified services | Independent power, cooling, reliability and demand case |
| Product/finishing node | Purify, dry and qualify products | Industrial reagents, construction and agricultural inputs | Buyer specifications, finite demand and end-of-life fate |

**All participating retrofit nodes belong to the network; they do not need to be co-located.** A node can participate through data, product/reagent exchange, coordinated maintenance, research or procurement without receiving every other node's waste. Physical co-location is an optional optimization that must earn its own cost and environmental case. Shared laboratories, training, maintenance, procurement, spares and data can produce benefits without shared wetted equipment. Seawater, reclaimed water, oily wastewater, leachate and potable water require appropriate separation. Chemical compatibility, pressure duty and contamination risks determine whether any equipment family can be reused.

There is no universal 30 MGD pump. A 30 MGD wastewater-feed block is a reasonable screening envelope around a 28 MGD average, with about 7% headroom before peak-flow and storage assessment. At 90% RO recovery, 28 MGD feed would yield 25.2 MGD product; a 30 MGD product target instead requires 33.33 MGD feed. Actual pump counts and pressure/flow specifications remain TBD.

## 5. Chinese-reference equipment and process packages

### 5.1 Desalination, polishing and controls

The Dongjiakou government casebook reports 100,000 m3/day, CNY450 million investment and 2.2 kWh/m3 for its stated UF/RO case boundary [S10]. The manufacturer project description independently identifies the phase-one capacity [S11]. At the assumed exchange rate the investment reference is $62.07 million. It is about 26.4 MGD, not 30 MGD. Historical investment figures conflict, and the matched original cost breakdown is unavailable in the present corpus. A separate Lubei brine-to-bromine/salt case is not proof that the CNY450 million Dongjiakou scope includes mineral recovery or ZLD.

Candidate Chinese packages comprise intake screening and pretreatment; UF or equivalent feed conditioning; RO membranes and pressure vessels; high-pressure/booster pumps; ERDs; post-treatment; and data/control instrumentation. OriginWater and Jiangsu Longmo membrane references, Tangshan project pump packages and a Harbin ERD reference are retained, with prices still NEEDS SOURCING URLS. NF and BWRO packages do not automatically match SWRO duties.

Jinke Environment's NewaterHouse/WateRobot provides an additional manufacturer-described Chinese modular water-treatment and AI-operations candidate [S12]. The published 2,000-50,000 tonne/day product-scale range is a lead for modular assessment, not a verified match to either entire Corpus flow. Claimed reductions in footprint, delivery time, staffing and lifecycle cost are not credited. Existing biological treatment need not be replaced to add advanced polishing. Plant operation must remain safe without a remote AI or internet connection.

### 5.2 Full Desen integration surface

The Desen catalogue identifies fixed washing/remediation and mobile screening, scrubbing, multistage classification, solid-liquid separation and wash-water treatment [S13-S15]. These form a conditional solids-remediation branch, not a seawater-desalination EPC package. Relevant application categories include contaminated soil, oily soil, dredged/ditch sludge, sewer or industrial solids, aggregate and C&D materials. Feed-specific tests determine applicability.

The current screening product page lists DS260 and DS15SE at 30-150 t/h, 28.5 kW and 15,200 kg, with 8.4 x 3.1 x 3.4 m outline dimensions [S13]. Earlier supplied articles listed different capacity, weight and dimensions. Both records remain visible; the RFI must obtain a dated model-specific package and sustained performance on the proposed waste. The mobile scrubbing listing describes 15-30 t/h [S14], so a high-capacity screen cannot establish the throughput of a full washing line.

The process chain is: controlled excavation and inspection; removal of batteries/cylinders/hazardous items; suitable screening; metal separation; material-specific sorting; fines characterization; washing/scrubbing where useful; classification; dewatering; wash-water treatment and reuse; then qualified product delivery or final residual treatment. Magnets, eddy-current, optical sorting, shredders and combustible preparation require explicitly quoted modules. They are not proven included in the screen reference price.

The CNY2 million listing previously supplied for a generic aged-waste screening product converts to about $275,862 before any separately priced delivery costs. It is not a model-bound DS15SE quotation or the price of the full Desen suite [S16]. No combination of these catalogue modules automatically produces agricultural soil, accepted fuel or saleable aggregate.

### 5.3 Bioreactors and nutrient-recovery sidecars

Biological modules include wastewater mainline or side-stream bioreactors, clean-organic digestion/co-digestion, phosphorus release, and candidate biomass polishing. Shanghai JADE is a Chinese AD supplier lead for food-waste/sludge applications [S17]; commercial scope and costs need direct confirmation. The proposed domestic struvite and ammonia-recovery package prices remain user-supplied leads. An imported Pearl-type installation is process background, not the selected Chinese package.

Struvite crystallization is a chemical step downstream of appropriate nutrient preparation. Reactive phosphate, ammonium and qualified magnesium must be present simultaneously. Total phosphorus is not automatically reactive phosphate; nitrate cannot simply be counted as ammonium. Optional imported ammonia is a separately costed input, not recovered nitrogen. Brine-derived Mg allocated to fertilizer is deducted from the same finite Mg inventory available for sale or binders.

The prior final-effluent example yielding about 42 kg/day ideal struvite at 8 MGD was a demonstration that dilute, nitrified final effluent is an unattractive recovery point. It was not the plant's nutrient potential. The new 100/200/500 m3/day sidecar scenarios use assumed reactive P 35 mg/L, ammonium-N 100 mg/L and P capture 85%, giving approximately 23.6/47.1/117.9 kg/day of pure struvite. These are illustrative chemistry cases, not Greenwood measurements.

### 5.4 Brine products, chloride and residual closure

The candidate portfolio retains NaCl; Mg hydroxide/oxide/carbonate/chloride; gypsum or CaCO3; KCl/K2SO4; bromine; acid/base and disinfectant feedstocks; and conditional construction binders. Boron, lithium, strontium, rubidium/cesium/iodine, uranium/trace metals and deuterium remain research leads without base revenue. Actual assay and selectivity must precede product forecasts.

Bipolar-membrane electrodialysis has a published Chinese engineering-case lead [S18]; it still requires clean feed, membranes, electricity and product specifications. Chlor-alkali is a separate industrial chemical route requiring purified brine, power, gas handling and suitable users. The same Na/Cl cannot support full NaCl sales plus full BMED plus full chlor-alkali production. Internally used HCl can return chloride to water, so acid manufacture alone is not final chloride removal.

MVR evaporation, crystallization, dewatering, drying and residual stabilization remain candidate Chinese-supply packages. Plasma/vitrification is an optional compatible-solid treatment, not a bulk-brine evaporator. A Chinese experimental paper reports secondary fly ash as well as vitrified material [S19]. Volatile metals, salts, offgas capture, scrubber water and secondary residues remain in the ledger. No molten-slag or mortar route is credited without actual composition, leaching, durability, use approval and a receiving market.

## 6. Retrofit scenarios and water balances

The network should first preserve fit-for-use water. Full-stream RO is an option, not a prerequisite for every nutrient or solid-recovery sidecar. Assumed split routing illustrates the penalty of unnecessarily treating all water to a stricter specification.

| Feed available to scenario | All qualified direct reuse | Half feed through 90%-recovery RO | All feed through 90%-recovery RO |
|---|---:|---:|---:|
| 8 MGD | Up to 8.0 MGD product | 7.6 product; 0.4 reject | 7.2 product; 0.8 reject |
| 16 MGD | Up to 16.0 MGD product | 15.2 product; 0.8 reject | 14.4 product; 1.6 reject |
| 28 MGD | Up to 28.0 MGD product | 26.6 product; 1.4 reject | 25.2 product; 2.8 reject |
| 30 MGD | Up to 30.0 MGD product | 28.5 product; 1.5 reject | 27.0 product; 3.0 reject |

Direct-use cases exclude separately unquantified wash, sampling, product-moisture and other process losses. They are water-routing envelopes, not promises of zero loss or universal suitability. Added extraction may alter hardness, alkalinity, scaling, nutrient levels, disinfectant demand and corrosion. Industrial cooling makeup, boiler feed, crop irrigation and potable water have different requirements.

Three retrofit packages should be quoted separately: (R1) nutrient/solids sidecars at the biological source; (R2) selective polishing at the existing delivery hub; and (R3) industrial process or blowdown recovery at the customer's facility. R1 need not transport a concentrated nutrient stream through the entire reclaimed-water pipeline. R3 may see higher salt concentrations but also more treatment chemicals and contaminants. Their nutrient and salt inventories cannot be counted repeatedly as they circulate.

## 7. Desalination and mineral inventory

The base water calculation uses 30 MGD online product, 42.5% whole-plant recovery, 47.5% RO recovery, 35 kg/m3 feed salinity and 90% annual water availability. It gives about 267,206 m3/day intake, 239,079 m3/day RO feed, 125,516 m3/day RO reject and 28,127 m3/day other pretreatment residual. Annual product is 37.31 million m3, equivalent to 27 MGD annual average. Firm delivery requires redundancy and reliability analysis beyond this calculation.

The dissolved-feed inventory is approximately 9,352 tonnes/day; about 8,368 tonnes/day enters the idealized RO feed and the rest is assigned to pretreatment residual in this envelope. That split is not a detailed salt-rejection model. Representative RO-feed inventories include Mg 322.8 t/day, Ca 98.0, K 93.2, Br 16.0, and Li 0.043. These are assumed elemental inventories, not recovered product quantities or net revenues. Actual product mass can include added reagents and bound water; it cannot be compared with feed inventory without chemical accounting.

Potential industrial/agricultural substitution includes qualified magnesium reagents, gypsum, potash, salt and manufactured acid/base. Replacing purchases is measurable; replacing international imports additionally requires the displaced procurement's origin. Gulf Coast purchases may already be domestic. Revenue is limited by accepted grade, contamination, market capacity, transport radius and competing product allocations.

Water recovery and extraction require a coupled optimization: residual volume, salt inventory, energy, reagents, purity and final fate must change together. Removing some Mg or Ca does not eliminate the remaining water or sodium/chloride. Inorganic mineral residue is not biofuel. Source-separated organics and eligible organic sludge have different biological/energy pathways.

## 8. Landfill-mining throughput and final material fate

| Screening sensitivity | Campaign feed/day | Campaign feed/year | Complete-line sustained throughput |
|---|---:|---:|---|
| 50 metric t/h | 320 metric t | 96,000 metric t | Unknown |
| 200 metric t/h stretch | 1,280 metric t | 384,000 metric t | Unknown; above current 150 t/h catalogue ceiling |

Both cases assume 8 hours/day, 300 days/year and 80% effective availability applied once. The 200 t/h case preserves an earlier discussion as a stretch sensitivity; it is not the current confirmed model rating. A 15-30 t/h washing module could accept only part of the screened material, require parallel modules or limit the campaign. Procurement must specify the bottleneck duty rather than summing module advertisements.

For transparent material handling only, the script partitions hypothetical feed into 50% soil/fines, 20% combustibles, 10% mineral aggregate, 5% ferrous, 1% nonferrous, 4% glass and 10% other. These fractions are analyst assumptions, not Corpus sampling. At the 50 t/h screen case, that creates 160 t/day of fines and 64 t/day of combustibles needing characterization; neither is automatically a product. Every qualified output and final disposal quantity remains null until tested. No overall diversion percentage is forecast.

Metals require acceptance and net freight pricing. Combustibles need fuel qualification, a permitted receiver and residue accounting; Oahu's H-POWER is not a Corpus outlet. Recyclable plastics require polymer/contaminant separation. Batteries and e-waste need dedicated approved handling. Clean organics may be digested or composted; aged mixed landfill fines cannot be relabeled clean organic feed. Washed aggregate needs performance and leaching acceptance. Hazardous fines, spent media and washing cakes need further recovery or permitted final treatment.

Mining can also disturb gas collection, liners, leachate systems and existing closure obligations. Excavated tonnage is not airspace recovery: reburied residual volume, compaction, cover and stability must be measured. Corpus landfill-life benefits must be established locally rather than imported from the Oahu siting argument. Any avoided-disposal and new material revenues are separate from existing tipping-fee and gas-contract effects.

## 9. Compute comparison: 100 MW, 500 MW and 1.21 GW IT

Compute is a separable service business and infrastructure load, not a reagent that must be added for recycling to work. The 0 MW comparison means zero additional large compute campus, not an absence of plant controls. Chinese hardware/integration candidates, including an Ascend-class architecture if legally and commercially available, are an RFI option; no specific chip exportability, server capability, price, training performance or U.S. service arrangement is assumed.

| Metric | 100 MW IT case | 500 MW IT case |
|---|---:|---:|
| Peak compute-site load at PUE 1.15 | 115 MW | 575 MW |
| Average compute-site load at 90% IT load | 103.5 MW | 517.5 MW |
| Annual compute electricity | 906.66 GWh | 4,533.30 GWh |
| Electricity at assumed $0.10/kWh | $90.67m/year | $453.33m/year |
| Captured IT heat at assumed 70% of average IT power | 63 MW thermal | 315 MW thermal |
| Compute installed capital and contracted revenues | Unknown | Unknown |

### Exploratory 1.21 GW case

Dave requested a 1.21 GW case as a deliberately expansive sensitivity. It is defined here as 1,210 MW IT nameplate to preserve a consistent comparison. If 1.21 GW instead refers to total compute-site capacity, its IT capacity at PUE 1.15 would be about 1,052 MW, requiring a different run.

| Metric | 1.21 GW IT sensitivity |
|---|---:|
| Peak compute-site load, before process loads | 1,391.5 MW |
| Average compute-site load at 90% average IT load | 1,252.35 MW |
| Annual compute electricity | 10,970.59 GWh |
| Compute electricity at assumed $0.10/kWh | $1,097.06m/year |
| Captured IT heat at the assumed 70% fraction | 762.3 MW thermal |
| Cooling consumption / makeup at 0.2 L/kWh and five cycles | 1.381 / 1.726 MGD |
| Cooling consumption / makeup at 1.8 L/kWh and five cycles | 12.428 / 15.535 MGD |

The high-water case's 15.535 MGD makeup is almost the entire nominal 16 MGD existing reuse program. That arithmetic is not an allocation: existing industrial service cannot be reassigned to compute without explicit agreement and a defensible community comparison. A dry-rejection case avoids modeled cooling evaporation but still needs heat-rejection equipment, power, initial fill and ancillary water. No cooling technology has been selected.

At the same illustrative latent duty, the captured heat has a 29,040 m3/day single-effect energy equivalent, about 21.0% of the average residual envelope. At hypothetical heating COP 3 or 5, upgrading all that source heat would add 381.15 or 190.575 MW of electricity. These are process-independent algebraic sensitivities, not an MVR design or credited energy savings. This scale needs a separate credible power-system and useful-workload case; it does not make the smaller recovery nodes dependent on a gigawatt campus.

Water production alone adds roughly 9.37-18.40 MW average, or 82.07-161.16 GWh/year, across the 2.2-4.32 kWh/m3 screening range. Thus compute plus water production is about 112.9-121.9 MW average for the 100 MW IT case, and 526.9-535.9 MW for 500 MW IT. These exclude mineral recovery, wastewater retrofit loads, landfill machinery, final residual closure, additional heat pumps and many network services.

The assumed electricity tariff range $0.05-$0.15/kWh gives compute-only energy bills of approximately $45.3-$136.0 million/year or $226.7-$680.0 million/year. These are arithmetic sensitivities, not utility offers; demand charges, capacity contracts, grid works and backup fuel are not included.

### 9.1 Cooling water and closed-loop meaning

Chip-level closed loops still need heat rejection. Dry/mechanical rejection may avoid cooling evaporation; an evaporative tower consumes water and creates blowdown. A manufacturer's non-Chinese zero-evaporation design is cited only as a boundary example, not as the proposed supplier or a Corpus WUE guarantee [S20]. This paper's WUE numbers are explicitly analyst assumptions, not fleet averages.

At 90% average IT load and five cycles of concentration:

| Assumed cooling consumption per IT kWh | 100 MW: consumed / makeup MGD | 500 MW: consumed / makeup MGD |
|---|---:|---:|
| 0 L/kWh, dry rejection case | 0 / 0 | 0 / 0 |
| 0.2 L/kWh | 0.114 / 0.143 | 0.571 / 0.713 |
| 1.8 L/kWh | 1.027 / 1.284 | 5.136 / 6.419 |

Makeup includes simplified blowdown replacement, excluding drift, domestic demand and other uses. Consumption is evaporated water and cannot be recovered merely by treating blowdown. Using reclaimed water changes the source; it does not erase consumption. Net-positive water accounting must compare actual community supply, aquifer withdrawals, water quality and seasonal reliability against the baseline, without counting repeated circulation as new supply.

### 9.2 Thermal match and residual-treatment limits

The screening heat-source temperatures are 45 and 60 C, not measured hardware specifications. With an assumed 5 C heat-exchanger approach, the sink supply ceiling is approximately 40 or 55 C. Biology, certain preheating/drying duties and suitably designed low-temperature processes may be candidates. Heat exchangers, pumps, fouling, insulation, seasonal demand and backup add costs. No MED or crystallizer duty is cleared by a generic heat label.

Using an illustrative latent duty of 630 kWh/m3, 63 or 315 MW of captured heat corresponds to an ideal energy-only single-effect evaporation equivalent of 2,400 or 12,000 m3/day. That is about 1.7% or 8.7% of the annual-average desalination residual envelope. It is not a real evaporator prediction, an upper bound on all multi-effect designs, or a statement that MVR needs single-effect thermal energy. MVR recycles latent heat and consumes compressor electricity; its actual energy balance must be modeled separately.

A hypothetical heating COP of 3 would require an additional 31.5 or 157.5 MW electricity to upgrade all the modeled source heat, delivering 94.5 or 472.5 MW thermal. At COP 5, additional electricity is 15.75 or 78.75 MW. These algebraic cases do not establish achievable COP at a chosen temperature lift. Neither is booked as avoided MVR electricity.

Corpus LNG facilities are liquefaction/export operations, not a source of free regasification cold. Candidate exchanges include verified compressor/turbine heat, qualified reclaimed-water supply and specific utility services. Pressure-reduction recovery, refinery heat and any existing thermal allocation need equipment-level evidence. This case cannot inherit Dongjiakou's LNG cold cascade without a matching process.

## 10. Costs: what can be priced and what cannot

The appendix carries all 27 prior price anchors with original CNY and converted USD, source status and scope. They are not newly obtained quotations. Examples of potentially relevant Chinese-supply leads are:

| Package/reference | Converted USD reference | Scope limitation |
|---|---:|---|
| OriginWater / Longmo membrane elements | $628 / $539 per element | Claimed procurement ceilings; vessel, quantity and current original notice missing |
| RO high-pressure/booster package | $2.445m per reported package | Head, count, phases, materials and duties not matched |
| Harbin ERD | $270,345 per reported unit | Capacity basis and redundancy unknown |
| 5.5 t/h MVR project budget | $1.620m | Feed versus evaporation duty and project inclusions unresolved |
| Chinese 200 m3/day struvite package | $154,483 | Supplied claim, not current installed quote |
| Stripping/recovery equipment | $24,828-$38,621 | Not ammonia storage/dosing, not matched feed duty |
| Food-waste digestion capacity reference | $8,000 per t/day capacity | Different feed and boundary from sewage sludge |
| Generic Desen screen listing | $275,862 | Model/modules, Incoterm, 60 Hz and freight not bound |

All listed prices retain NEEDS SOURCING URLS or their separately described platform-reference status. The alleged sludge-digestion price of CNY180,000 per tonne has an unresolved capacity denominator and is not multiplied into a budget. Imported membrane/struvite comparisons remain outside the proposed Chinese-supply subtotal. No total is formed by adding unit prices, OPEX rates, project budgets and market selling prices.

Retrofit installed costs must include process modules, demolition/tie-ins, bypass, shutdowns, foundations, pressure/electrical compliance, imported delivery, U.S. engineering and labor, commissioning, operator training, spares, cybersecurity and lifecycle residual obligations. Existing conveyance can reduce duplicated work but is not proof of a cheap tie-in. A cost at the industrial endpoint may differ from a WWTP sidestream package of the same flow.

The small nutrient sidecar is a useful negative screening result. At 200 m3/day, 35 mg/L reactive P and 85% capture, the theoretical struvite is only 47.1 kg/day. At the supplied CNY2,800-3,500/t selling-price reference, gross sales are about $18-$23/day before reagents, operations and capital. Product sales alone do not establish an attractive case against a $154,483 equipment anchor. Avoided scaling, reduced nutrient-treatment burden or higher-concentration feed may matter, but must be measured and priced separately.

**Community-use struvite is an explicit alternative to commercial sales.** A module may be funded at a financial loss to provide suitable fertilizer to local agriculture and deliver verified treatment or resilience benefits. Report annualized capital, O&M, reagents, testing, packaging and transport; deduct actual cash receipts and independently verified avoided costs; disclose the remaining public or network subsidy. Compare with buying an agronomically suitable fertilizer and providing equivalent nutrient treatment separately. Donation is not sale revenue, and the same product cannot also earn a second full market-value credit. Document recipients, application needs, contaminant/pathogen acceptance, phosphorus availability and avoided purchases. A subsidized service may pass a public-benefit decision without being labeled commercially profitable; the 47.1 kg/day example does not by itself establish community demand or value.

Likewise, linear scaling of the supplied small MVR budget to the full residual envelope previously yielded about $1.89 billion. That is a warning about unresolved scope and scaling, not a valid installed quote, lower bound or proof that ZLD is impossible. Mineral net margins remain zero in the actual baseline until qualified quantities, costs and buyers exist. Thirty-year gross mineral values cannot be used as cash available today without discounting, market absorption, replacements, downtime and financing.

The rejected Corpus proposals remain a separately dated comparator [S21]. The 2025 named process-equipment line is not all hardware, and halving it is not a cap on layout, construction or procurement redesign savings. This paper does not fill missing American component values with generic allocations. Competitive whole-facility comparison still requires scope-matched quantities and a reference design. Historical U.S. cost, construction duration and community concerns motivate inquiry; they do not prove a particular category is unnecessary.

## 11. Products, agricultural use and community benefit

Qualified outputs may support industrial inputs, construction, agriculture, restoration and local manufacturing. Candidate magnesium reagents may serve nutrient recovery or appropriate binders; gypsum and potash require soil-specific need and salinity assessment. Qualified compost/biomass comes from eligible feed and treatment, not an assumption that contaminated fines become fertilizer. Construction uses must address chloride, corrosion, strength, curing, leaching and end-of-life behavior. Product demand constrains the amount accepted: concrete is not an unlimited sink for mixed salts or sludge.

Agricultural reuse must account for crop demand, soil salinity/sodicity, boron, pathogens, metals, microplastics, drainage and downstream salt fate. Microplastic capture media, filtration and monitoring are retained as a performance slot; a Chinese supplier and verified duty are TBD. Drinking-water or food/feed claims require their own authorization. All captured contaminants remain an obligation unless actually destroyed or placed in a qualified product/sink.

The twelve-domain lens records agriculture, ecology, education, employment, chemistry, research, manufacturing, governance, AI, water, energy and data. Each candidate exchange needs an owner, evidence status, finite resource allocation, costs, acceptance criteria and residual fate. AI/data are both enabling infrastructure and resource consumers. Training and public data can be outcomes, but delivery, beneficiaries and measurement must be specified rather than presumed.

Community measures should include resident water reliability and affordability; industrial potable-demand displacement; local hiring/training; air, water, odor and traffic burdens; access to usable products; ecological condition; and public reporting. Industrial earmarking does not disqualify an ecological gain. The gain must be measured relative to what the existing industrial-reuse project would already do, including the customer's subsequent blowdown and emissions.

## 12. Footprint, resilience and delivery incentives

Total land area remains unknown. Preliminary geometry can size tanks, not whole campuses: for 16 MGD, eight hours of storage is about 20,189 m3; at assumed 5 m depth and a 1.5 layout factor it is about 1.50 acres. Twenty-four hours is about 4.49 acres. Neither includes roads, biological vessels, minerals finishing, enclosed waste handling, compute halls, electrical yards, backup equipment or storm buffers. No percentage footprint saving is credited from modular marketing claims.

A regional arrangement should compare a landfill-adjacent materials yard, WWTP source sidecars, the existing industrial pipeline and a suitable coastal desalination site. Heat moves only when distance and temperature preserve value; reagents and data can travel more readily. Water treatment must continue during compute outages, and compute may not consume emergency resident reserves. Common-cause failures, utility outages, hurricane/flood exposure, cyber incidents, odors, noise and maintenance access require independent safeguards.

The alternative management model retains zero automatic expenditure-linked management fee, with reasonable salaries, verified expenses and capped benchmark awards still TBD costs. It does not erase legitimate project supervision or assert that Corpus used prohibited fees. Awards should depend on independent commissioning, reliable service, product quality, net lifecycle savings and verified additional material value. Sales and internal avoided purchases are alternatives for the same tonne; imported reagents are deducted; independent reviewers set baselines. AI anomalies enter human review and do not automatically cause payment penalties.

Reported Dongjiakou construction-to-first-water timing and a two-times-duration scenario are useful research comparisons, not binding U.S. total-delivery guarantees. Necessary permissions, public participation, testing and reliability cannot be traded for an early first-water date. Chinese equipment, remote support, public funding requirements and U.S. construction compliance require project-specific review; no legal clearance is claimed here.

## 13. Staged evaluation and decisions

1. **Inventory and assay:** confirm city flows, existing reuse commitments, Greenwood rehabilitation status, independent industrial streams, landfill cell composition, organics contracts, local product demand and exact candidate sites. Obtain recent operating data, not only permits.
2. **Source-based retrofit trials:** test one or more concentrated nutrient/solids streams and industrial blowdown loops while preserving existing service. Add metering, sampling and human-reviewed process analytics. Determine product acceptance and all residual destinations.
3. **Desen campaign:** obtain written full-line configurations and factory trials; run a controlled local materials campaign, logging excavation, products, process water, secondary residuals and true net airspace. Separate clean-organic digestion from contaminated fines.
4. **Desal/mineral pilot:** test actual source water and product routes. Select one finite chloride allocation and a quantified residual closure strategy. Obtain package quotes and American installation/tie-in estimates.
5. **100 MW comparison:** proceed to a compute design only with useful workload demand, power delivery, cooling and thermal offtake evidence. A smaller inference node can precede it. Water and recovery modules need not wait for hyperscale compute.
6. **500 MW expansion test:** require independently credible grid/generation, reliability, land, cooling, service and community cases. Increase water and recovery capacity because feed and customer demand support it, not merely because a larger campus appears on a drawing.

At each stage compare service-equivalent lifecycle costs and performance with the baseline and with smaller modular alternatives. A single financial ledger may cross-subsidize a necessary stream, but profit elsewhere does not clear an environmental or safety veto. No current lane has earned realized Atlas mineral revenue, confirmed import substitution or net ecological credit.

## 14. Reproducibility and files

Run `python scenarios.py` to regenerate CSVs and `python -m unittest discover -s . -p 'test_*.py' -v` for the nine new boundary/conservation tests. These are additional to the 86 tests in the frozen v0.7 package, not a claim that a new 95-test combined physical simulator exists. The appendix includes the complete prior 27-anchor price register, the new module register, explicit inputs, separate compute/water/heat/landfill/nutrient outputs and a source register. Blank numeric CSV cells mean unknown; zero actual revenue means no qualified realized credit, not an estimate of eventual profitability.

This version produces a coherent testable network and explicit comparisons. It does not produce a site-selected engineering design, complete bill of quantities, priced procurement package, validated AI optimization, qualified recovered product or approved residual route.

## References and provenance

[S1] Frozen v0.7 public model, sources and receipts: https://github.com/atlaslattice/open-regenerative-compute-standard/tree/f0914a5b9f5be1febcdde30d52455b582c97bdd3/prototypes/dongjiakou-corpus-v0_7

[S2] City wastewater service and pretreatment overview, undated, accessed 24 Oct 2026: https://www.corpuschristitx.gov/media/y54dmdsz/wastewater-service-area-and-pretreatment.pdf

[S3] City Phase 2 announcement, 30 Jun 2026: https://www.corpuschristitx.gov/news/posts/news-post-no-banner-2/

[S4] Ardurra project description; engineer-reported scope, not independent performance audit: https://ardurra.com/projects/corpus-christi-reclaimed-water

[S5] City Valero agreement announcement, 13 Jan 2026: https://www.corpuschristitx.gov/news/posts/city-council-approves-30-year-recycled-water-agreement-with-valero-refining/

[S6] TCEQ Greenwood technical package; historical sample and plant description, source receipts in v0.7: https://www.tceq.texas.gov/downloads/permitting/wastewater/title-iv/tpdes/wq0010401003-cityofcorpuschristi-greenwoodplant-nueces-tpdes-technicalpackage.pdf/@@download/file/wq0010401003-cityofcorpuschristi-greenwoodplant-nueces-tpdes-technicalpackage.pdf

[S7] City FY25 Q3 budget/performance report; planned asset change, not proof of completed removal: https://www.corpuschristitx.gov/media/cxxj4v45/fy25-quarter-3-budget-and-performance-report.pdf

[S8] City compost-yard and landfill-gas announcement, 22 Jul 2025: https://www.corpuschristitx.gov/news/posts/construction-contract-awarded-for-solid-waste-compost-yard-at-cefe-valenzuela-landfill/

[S9] City landfill locations: https://www.corpuschristitx.gov/department-directory/solid-waste-services/landfill-and-collection-centers/

[S10] Government-hosted 2025 industrial-water casebook, Dongjiakou and separate Lubei cases; source receipt in v0.7: https://jxj.ezhou.gov.cn/xwzx/tzgg/202510/P020251031656176156731.pdf

[S11] Beijing OriginWater Membrane Technology project description; indexed text retrieved, full fetch timed out on 24 Oct 2026: https://www.bsyflm.com/use_84/167.html

[S12] Jinke Environment NewaterHouse and WateRobot manufacturer description, accessed 24 Oct 2026: https://greentech.com.cn/Island . Related company report dated 22 Oct 2026: https://www.greentech.com.cn/News/Detail/3204

[S13] Desen screening catalogue, current accessed specification, not performance guarantee: https://www.materialwashing.com/Mobile-Screening-Plant/281.html

[S14] Desen mobile washing family: https://www.materialwashing.com/Mobile-Washing-Plant/

[S15] Desen fixed washing family: https://www.materialwashing.com/Fixed-Washing-Plant/79.html

[S16] Previously supplied B2B reference-price listing; original model/configuration linkage remains unresolved, not reverified as a current quotation in this paper: https://www.hbzhan.com/chanpin/25410123.html

[S17] Shanghai JADE AD manufacturer lead; indexed text retrieved, full fetch timed out, price not sourced: https://en.jade-cn.com/technology_show.aspx?id=625

[S18] Bipolar membrane electrodialysis: Industrial application in Bohai Sea, China. Prior abstract-level source, full package financial scope unverified: https://doi.org/10.1016/j.jwpe.2025.108266

[S19] Zhang et al., Experimental on plasma melting of fly ash from hazardous waste incineration, 2023, DOI 10.13732/j.issn.1008-5548.2023.02.014; 80 kg/h experimental platform, not Corpus package: https://ftjs.ujn.edu.cn/info/1045/3722.htm

[S20] Microsoft zero-evaporation design announcement, 9 Dec 2024; boundary illustration only, not proposed equipment supplier: https://www.microsoft.com/en-us/microsoft-cloud/blog/2024/12/09/sustainable-by-design-next-generation-datacenters-consume-zero-water-for-cooling/

[S21] Corpus dated proposal tables and action record. February 2026 presentation: https://corpuschristi.legistar.com/View.ashx?GUID=4C308273-7546-4BF4-8960-1AC483DFDC0E&ID=15269350&M=F . September action: https://corpuschristi.legistar.com/LegislationDetail.aspx?GUID=63C2D0EE-6B8A-4EAE-9144-C93B0DCDF65B&ID=8038548

[S22] Earlier Atlas thermal-water-mineral white paper; research intent, not independent verification: https://github.com/atlaslattice/open-regenerative-compute-standard/blob/f0914a5b9f5be1febcdde30d52455b582c97bdd3/docs/whitepapers/ORCS_CORPUS_THERMAL_WATER_MINERAL_WP_v1_2_2026-10-14.md

[S23] Product-use research retained from v0.7: brine-related mortar study https://pmc.ncbi.nlm.nih.gov/articles/PMC7665687/ ; Mg cement abstract https://doi.org/10.1016/j.desal.2025.118928 . These establish research leads, not approved Corpus construction materials.

The 27 equipment, OPEX and market-price anchors were supplied by DeepSeek through the user on 24 Oct 2026. Original sourcing URLs remain missing in that register. They must not be attributed to the official sources above unless a matching original record is subsequently retrieved.
