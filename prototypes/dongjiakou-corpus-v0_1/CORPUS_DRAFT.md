# Corpus Christi water–mineral–industry lattice: draft v0.1

24 October 2026. Independent research by the Atlas Lattice project, prepared with AI assistance. This is an auditable screening model, not an engineering estimate, regulatory determination or vendor offer. Source IDs below resolve in [sources.json](sources.json). Calculations are reproducible with [model.py](model.py).

## 1. Objective and environmental boundary

Evaluate a 30-MGD nominal water plant using Dongjiakou as an operating reference, with American engineering/construction, open component procurement, selective mineral recovery, and explicit community/ecological obligations. The project should supply useful water and industrial inputs while avoiding routine process-brine discharge into marine habitat.

**No routine marine process-liquid discharge is the candidate acceptance constraint. Full ZLD is the preferred aspiration, not an assumed achieved capability.** A route that treats a residual elsewhere may qualify only if its complete downstream fate satisfies the same constraint. Sending liquid to a contractor who ultimately discharges it to the ocean does not qualify.

Mineral extraction does not destroy the remaining salt. Dewatering does not destroy contaminants. Plasma does not erase off-gas residues. A dry residual can still require permitted stabilization, containment or disposal. Intake impacts, thermal effects, air emissions, land impacts and trucking must pass independently; eliminating an outfall does not itself demonstrate ecosystem protection or agency approval.

The [residual-route register](residual_routes.csv) includes RO reject, backwash, cleaning liquids, off-spec condensate, mineral mother liquors, scrubber purges, wet cake, filtrate, spent media and contaminated contact water. Every destination and receiving capacity is currently unconfirmed.

Historical outfall configurations may be retained as counterfactuals for costs and impacts. They are excluded from the proposed no-ocean baseline. The design objective protects marine habitat generally; this draft does not assert a site-specific whale exposure assessment.

## 2. What the Dongjiakou evidence establishes

The ministry casebook reports a 100,000-m³/day Dongjiakou UF–RO plant, ¥450m investment and 2.2 kWh/m³ electricity use. Its technology discussion distinguishes 45–50% RO recovery from 40–45% whole-plant recovery. A separate Lubei case describes brine sent to bromine extraction and solar salt production. **That integrated precedent is not proof that Dongjiakou's ¥450m includes a mineral/ZLD train.** [MIIT25, printed pp64–67]

Historical reporting describes Dongjiakou at ¥450m and 3.52 kWh/m³, using warmed power-station cooling seawater. A later company environmental assessment reports ¥650m for the plant and related facilities. These differences require reconciliation of date, metering boundary, operating conditions and investment scope. They are not a statistical confidence interval. [DJK16; DJK65]

The model uses 2.2, 3.0, 3.52 and 4.32 kWh/m³ as a sensitivity grid. The last is a stress assumption. No claimed pump, ERD or control-system saving is added to an already achieved SEC without a common measured baseline. No historical capital figure is treated as a 2026 equipment quotation.

## 3. Granular costs actually found

| Item | Reported tax-inclusive CNY | Quantity | Evidence and scope |
|---|---:|---:|---|
| First-stage RO replacement | 15,381,311.40 | 4,914 elements | Primary ranked-candidate notice; includes replacement work; not final executed contract [RO26] |
| UF replacement | 5,727,346.24 | 952 elements | Provisional mirror; includes installation works; primary not located [UF26] |
| Self-cleaning filters | 2,350,000 | 10 units | Provisional mirror; supply/installation/commissioning [FILTER26] |
| Air-source heat-pump package | Unknown | 4 units plus three 30-m³ tanks | Primary tender; no verified award price [HP26] |

These lots are useful price anchors for defined replacement scopes. They are **not** an original-build bill of materials and cannot be added to the historical investment total or scaled into complete Corpus plant CAPEX. A larger UF lot is quarantined because of potential overlap. The UF mirror's identifier did not reconcile to the expected primary record; this is an explicit evidence defect, not a verified award.

Still unpriced: intake, complete UF/RO trains, vessels, high-pressure pumps, ERDs, civil works, corrosion protection, product pipelines/storage, grid connection, mineral purification, residual closure, local labor, certification, engineering, permits, contingency and financing. Every such Corpus slot remains `null`. No numeric installed-cost total is issued.

## 4. Normalize before interpreting the gap

The city's February 2026 preliminary GMP was $978.77m for Inner Harbor. An indexed city attachment provisionally separates $78.61m phase 1 and $900.16m phase 2; the direct attachment could not be retrieved, and these are not equipment/civil-work categories. [CCGMP; CCPHASE]

At an **assumed**, non-market-quoted exchange rate of ¥7.25/$:

| Reference | Capacity m³/day | Capital intensity $/(m³/day) |
|---|---:|---:|
| Dongjiakou ¥450m | 100,000 | 621 |
| Dongjiakou ¥650m broader scope | 100,000 | 897 |
| Corpus $978.77m proposal / 30 MGD | 113,562 | 8,619 |

The raw ratios are 13.89× and 9.61×. Similar output capacities make scale alone an insufficient explanation. Mixed price years, seawater source, intake/outfall arrangements, water standards, distribution works, labor, procurement, risk allocation and finance remain unresolved explanations. The ratio is a research signal, **not** verified transferable savings, a current U.S. budget or domestic-content waiver eligibility.

The model publishes an explicit grid of assumed escalation (1.0/1.3/1.6), localization multipliers (2/3/5), exchange rates (7/7.25/7.5), and the two historical scopes. Those are sensitivity axes, not fitted cost forecasts. Any apparent headroom must pay for missing scope, including the no-ocean treatment obligation.

The friend's $260m expenditure figure remains an attributed, unverified lead. A city snapshot through June 2025 distinguishes $34.28m spent from $38.79m encumbered; it cannot establish later cumulative spending. Borrowing, authorization, encumbrance and expenditure must remain separate. [CCSPENT]

## 5. Draft physical system

**Stage A — demand and reuse.** Establish industrial demand, conservation, existing reuse commitments and backup supply before sizing seawater capacity. The city's Oso–Greenwood program is an existing counterfactual, not an Atlas invention: the city announced a $107.5m construction phase adding 11 MGD availability within a 16-MGD program. Do not claim announced delivery as current operation. [REUSE]

**Stage B — U.S.-engineered intake, pretreatment and RO.** Assess seasonal intake chemistry and biological impacts, then UF or an alternative pretreatment selected by trials. Size high-pressure pumps, ERDs, redundant trains, potable post-treatment, industrial branches and product storage. Chinese reference engineering can inform procurement, while the responsible U.S. design team establishes site-specific code compliance, guarantees and interface responsibility. Desen is a candidate for suitable auxiliary soil/residual modules, not the default seawater desalination EPC.

**Stage C — selective minerals.** Prefer the lanes with credible feed concentration, selectivity, reagents, qualified use and buyers. Chemical sequence must be trialed because one recovery can contaminate or starve another. Reserve capacity for unsold or out-of-spec material.

**Stage D — residual water recovery and final fate.** Compare additional membranes where chemically feasible, selective electrodialysis, thermal or membrane concentration, mechanical-vapor-recompression/evaporation, crystallization and dewatering. Freeze concentration is an optional tested branch with its own electricity/refrigeration duty; it receives no free LNG cold credit. Select technology from salinity, scaling, organic content, temperature, corrosion, energy, footprint and disposal tests. Do not assume any one technology accepts all reject.

**Stage E — compatible sludge treatment.** Test solids for contaminants and leachability. Compare metal recovery, stabilization/solidification, authorized industrial use and permitted containment. Treat compatible organic contamination separately. Vitrification/plasma is an optional route for characterized, suitably dewatered material; capture volatile metals, acid gases and secondary dust. Its energy use and secondary residues remain in the ledger. Fly-ash plasma research reports chloride-promoted volatilization; that supports an off-gas gate, not a brine-treatment performance claim. [PLASMA] It is not the default solution for thousands of tonnes/day of dissolved seawater salts.

**Stage F — metering and control.** Locally owned/exportable time-series data for flows, quality, energy, chemicals, product acceptance, downtime and every residue. Separate industrial control safety from AI experiments. Meter parasitic loads and maintain manual operation, isolation, bypass to contained storage and a controlled feed stop. Bypass must not mean an unrecorded ocean outfall.

## 6. Water, salt and recovery envelope

Base screening assumptions: 30 MGD product, 42.5% whole-plant recovery, 47.5% RO recovery, 35 kg/m³ feed salinity, 90% annual availability. These are editable assumptions anchored to a reference range, not Corpus feed measurements. Daily flows are online-day nameplate values; availability is applied once to annual output.

| Stream | m³/day |
|---|---:|
| Raw intake | 267,206 |
| RO feed | 239,079 |
| Product water | 113,562 |
| Pretreatment residual/loss envelope | 28,127 |
| RO reject | 125,516 |
| Combined nonproduct liquid | 153,643 |

The idealized salt-rejection balance contains **9,352 t/day feed salt**, of which about 8,368 t/day enters the RO-reject inventory and 984 t/day the pretreatment envelope. Complete rejection is a simplifying approximation; real permeate salt, suspended solids, cleaning chemicals, recycles and speciation require a process balance. The representative ion list is not a complete assay and does not exactly sum to the salinity assumption.

| Additional recovery from combined residual | Remaining liquid m³/day | Overall volume recovery |
|---|---:|---:|
| 0% | 153,643 | 42.50% |
| 50% | 76,822 | 71.25% |
| 80% | 30,729 | 88.50% |
| 100% mathematical closure | 0 | 100% |

This is a **volume/salt envelope**, not evidence of clean-water yield or achievable membrane performance. At high concentration, phase change/crystallization and bound water prevent interpreting the arithmetic as an all-liquid solution. Salt remains even at zero liquid volume; condensate must be tested; real ZLD has wet solids and other losses. No treatment energy or cost is inferred from these fractions.

At 90% availability, annual output is 37.31m m³ (27 MGD annual average). A 30-MGD firm obligation requires separately sized redundancy/storage/backup, not a silent assumption of continuous nameplate delivery.

## 7. Full brine-recovery portfolio and competing allocations

The [pathway register](mineral_pathways.csv) retains the prior Maui and Corpus research: sodium chloride; magnesium hydroxide/oxide/chloride/carbonate; gypsum/calcium carbonate; potassium chloride/sulfate; bromine; boron; strontium; lithium; trace rubidium/cesium/iodine and assay-dependent trace metals; reagent manufacturing; and research-only isotope recovery. Unknown or poor economics does not remove a discovery lead; it prevents that lead from being booked as revenue.

One illustrative allocation takes **50% of selected RO-reject ions**, with no pretreatment inventory credited. It is deliberately a bookkeeping scenario, not a vendor yield claim:

| Theoretical product | t/online day | Important external input or condition |
|---|---:|---|
| NaCl | 3,191 | Selective crystallization, purity, market capacity |
| Mg(OH)₂ | 387 | External hydroxide; cannot also sell the same Mg as MgO/MgCl₂ |
| Gypsum | 211 | Uses Ca and sulfate; bound water included |
| KCl | 89 | Competes for chloride; difficult selective recovery |
| Bromine elemental equivalent | 8.0 | Oxidant/containment/speciation and process yield unmodeled |

These product masses must not be subtracted wholesale from feed-salt mass: some include external reagents or bound water. The code deducts each consumed feed ion exactly once and retains the unused inventory. The alternative MgCl₂/CaCO₃ case is **mutually exclusive**, not additive. Calcining hydroxide to MgO requires an extra energy/reaction balance. Selling Mg versus consuming it to recover nutrients from a separate wastewater stream requires a decision on net margin, nutrient demand, purity, supply reliability and residual fate.

Boron, lithium and strontium inventories are displayed in the output without product recovery. Deuterium is a water-isotope research lane, not ordinary RO enrichment or a salt product; no isotope revenue is assumed. Sulfate-derived acid, alkali, hypochlorite and fertilizer reagents are manufactured products requiring extra processes, inputs and power. Chloride feedstock is not nuclear fuel.

Qualified industrial supply is preferred where contracts support it; resilience and import replacement require actual displaced purchases. The model's **accepted product tonnes, realized mineral revenue and import-displacement credits remain zero**. Market depth matters: bulk salts cannot be priced as if every tonne commands specialty retail value.

## 8. Thermal, LNG, wastewater and compute integrations

Corpus's LNG liquefaction/export setting does not provide the regasification cold resource available at an LNG import terminal. Candidate exchanges are measured compressor/turbine/refinery residual heat, compatible shared water treatment, and specific pressure-reduction duties. Existing heat recovery and contractual uses must be subtracted first.

For each thermal connection record source/return temperatures, flow, availability, fouling, exchanger approach, pumping, distance, backup and owner. Test heat-pump boosting where justified. MED and other thermal processes must be matched to actual supply temperatures; generic liquid-cooling return temperatures do not automatically support them. Drying and water recovery have separate mass-transfer constraints.

An on-site industrial data/AI node can consolidate process telemetry and test optimization without requiring a speculative hyperscale data center. The energy grid compares zero, 100-kW and 1-MW additional IT loads at an assumed PUE 1.15 against assumed 0/5/10% water-plant energy savings. **No AI saving is established.** At 2.2 kWh/m³ and 90% availability, a 5% assumed saving is 4.10 GWh/year; a continuously operating 1-MW IT node consumes 10.07 GWh/year including the assumed overhead. Heat credits remain zero. A real compute service may have independent value, but that value requires its own customers and ledger.

The 1+M+N architecture, model–data iterative learning, and WED assessment provide distinct discovery/evaluation contexts; they do not make an AI optimization commercially proven or impose a WED procurement standard. The twelve-domain ORCS lens adds community, ecology and other opportunity/obligation surfaces.

## 9. Cost effectiveness and portfolio accounting

Base water-only electricity sensitivity is 2.2–4.32 kWh/m³ at assumed tariffs $0.07–0.15/kWh, or $0.154–0.648/m³. This excludes extra mineral/residual treatment and most non-electric operating costs. The ministry reference reports chemical costs below ¥0.15/m³ (about $0.0207/m³ at the assumed exchange rate); that reference bound excludes proof of Corpus chemical pricing and mineral-recovery reagents. [MIIT25] At 2.2 kWh/m³ the online-day average electrical load is approximately 10.4 MW; ZLD or substantial additional compute increases it.

At assumed 6% capital recovery over 30 years and 90% availability, illustrative installed CAPEX of $150m/$250m/$500m/$978.77m produces capital-only charges of $0.292/$0.487/$0.974/$1.906 per m³. These are **hypothetical budgets**, not quotations or complete water tariffs. The model also annualizes one known RO replacement lot over assumed 5/7/10-year lives, clearly excluding all other membrane/equipment replacement.

Net operator cash must include capital, energy, chemicals, labor, maintenance, testing, certification, residual transport/disposal, shutdown reserves and finance, less actual water/product payments. Additional modules may operate at a loss if the whole permitted portfolio is worthwhile. That cross-subsidy must identify payer, recipient, allocation and contract; it cannot turn a failed environmental gate into a pass.

Maintain parallel ledgers for operator cash, buyer savings, public water reliability, import substitution, ecological outcomes, local employment/skills and community governance. A buyer's avoided purchase and the operator's sales revenue are two views of the same transaction, not automatically additive social gains. An avoided outfall or landfill cost needs a credible baseline, attributable marginal reduction and responsible owner. No assumed government payment or environmental credit is used to close an operating deficit.

## 10. Twelve-domain test and attribution

The [lattice register](lattice_couplings.csv) treats agriculture, ecology, education, employment, chemistry, research, manufacturing, governance, AI, water, energy and data as search domains. It does not require all possible pairings or credit every promising linkage. Each candidate needs transfer conditions, losses, owner, counterfactual, monitoring, residual fate and a veto.

For ecology, select controls/reference sites and a pre-intervention baseline, record seasonal currents/weather/other discharges, then predefine indicators and observation duration with independent experts. Intake mortality, pollutant loads, salinity/temperature exposure and benthic response are different metrics. A permit or lower discharge is not proof of a population-level habitat improvement.

For education, use competency tests, operator certification, retention and comparison with ordinary training. For governance, measure response/resolution of documented concerns and meaningful participation, with privacy and independent reporting. For AI, compare against conventional control using staged, safety-bounded trials and net energy. Do not classify hard-to-attribute outcomes as worthless; assign an appropriate design and retain unresolved status until evidence supports credit.

## 11. Procurement, compliance and acceptance

Separate seawater core technology, auxiliary residual modules and controls. Ask each supplier for a dated scope, guaranteed sustained rate on specified feed, expected availability, product quality, measured mass balance, complete load list, itemized EXW/FOB/delivered price, commissioning and U.S. references. Obtain separate prices for minerals and final residual closure, including all consumables, off-gas and disposal.

U.S. engineering must establish applicable pressure, electrical, drinking-water, structural, environmental and labor requirements. Origin-based funding/procurement rules and access restrictions require project-specific review. U.S. assembly alone does not settle domestic component compliance. The code's component-share arithmetic excludes final assembly labor; it is not a legal eligibility determination. No current tariff percentage, exemption, domestic-content waiver or regulatory approval is assumed in CAPEX. Customs classification and shipment-date landed pricing need written confirmation.

Intake permitting is site/duty-specific; a generic 2-MGD desalination-module threshold is not assumed. Local acceptance, water rights, operator qualifications, training, spares, cyber/data ownership and service access remain independent gates.

Acceptance sequence:

1. Characterize seasonal feed and all proposed sinks; reconcile reference costs and meters.
2. Obtain normalized vendor scopes and actual receiving-facility capacity/quotes.
3. Bench/pilot the mineral sequence and residual chemistry; retain unfavorable results.
4. Demonstrate water quality, source-safe intake, containment, offline/manual control and residual transport/final fate under normal and upset conditions.
5. Obtain independent cost/performance/permit review and community decision before scale-up.

`fate_gate` returns **FAIL** for a declared routine marine release, **UNRESOLVED** for missing permits/final fate, and a boundary-limited pass only when all declared streams meet the conditions. The caller must establish a complete stream inventory; the function cannot discover omitted waste. It does not replace the other legal, safety, ecological and commercial gates. At present, overall clearance remains unresolved and every realized benefit stays zero.

## 12. Practical next decision

Proceed to a scoped pre-feasibility request, not a deployment or profitability claim. Ask qualified desalination engineers and U.S. constructors to price a common 30-MGD boundary, with separate mineral and no-ocean residual options and explicit firm-supply requirements. In parallel, ask buyers and residual receivers for binding specifications and capacity.

The actionable finding is that an operating reference justifies a serious component-level challenge to the U.S. cost structure. The unresolved question is how much of that advantage survives site adaptation, community obligations and the much wider material-closure boundary. This package makes that question measurable while preserving all earlier recovery lanes.
