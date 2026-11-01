# ORCS Transformer 4.0 — T4-S50-DC / 800 VDC AI-Factory Power Tile
## Market-specific engineering decision, topology trades, cost-class and reproducible load case · v0.3 · 2026-11-01

**Status:** ENGINEERING RESEARCH / STANDARDS-ALIGNED DESIGN TARGET / SUPPLIER-DIALOGUE-READY / NOT PROTOTYPED, CERTIFIED, FUNDED, PRICE-QUOTED, ORDERED OR ENDORSED. This document does NOT state that OpenAI/Stargate, NVIDIA, Google, Microsoft, OCP or any power-system vendor has adopted ORCS equipment. All "T4" marks are working project names, not a recognized industry standard.

**Direct lineage:** [T4-S50 original 480 VAC → 120/240 VAC advanced branch v0.2](T4_S50_SIC_SOLID_STATE_TRANSFORMER_ADVANCED_BRANCH_v0_2_2026-11-01.md) is preserved as **T4-S50-AC legacy product candidate**; [T4-P25-L utility product](T4_P25_L_MODULAR_DISTRIBUTION_TRANSFORMER_PRODUCT_DECISION_AND_SPEC_v0_2_2026-11-01.md) remains separate; [AHD/DISH shared manufacturing platform](T4_COMMON_AHD_DISH_DUAL_MATERIAL_ROBOTIC_PLATFORM_AND_COST_MODEL_v0_2_2026-11-01.md) remains independently experimental. This v0.3 creates a **NEW**, distinct **three-phase 480 VAC → 800 VDC** candidate; no electrically invalid substitution of old one-phase designs. The broad [Transformer 4.0 v0.1](TRANSFORMER_4_0_AHD_DISH_MODULAR_ROBOTIC_SPEC_v0_1_2026-11-01.md) is preserved.

**Critical standards discovery:** OCP published **Solid State Transformer (SST) Specification v0.3.0**, effective June 22, 2026, authored by Google, Microsoft and NVIDIA. Its **medium-voltage** SST product SKUs are **13.8 kVAC 3φ → 800 VDC, 5 MW**, and **34.5 kVAC 3φ → 800 VDC, 5/10 MW**. The **≥98% at 50–100% loading** goal is **power-train-only**. **A 50 kW 480-VAC side-rack converter is NOT the 5 MW medium-voltage SST defined by that specification.** Our 50 kW tile targets the *separately described near-term LVAC retrofit side-power-rack architecture*, with independent relevant OCP power rack, DC busway, system safety and interconnection validation. An eventual 5 MW MV converter would be a **separate product with a completely different insulation, fault, transformer and certification design**, not 100 unqualified 50 kW 480-V tiles wired directly to 13.8 kV.

Primary sources:
- OCP v0.3 original PDF: https://www.opencompute.org/documents/ocp-sst-design-specification-v0-3-final-pdf (especially pp. 9–10 and 14)
- OCP co-authored industry rollout article and retrofit/direct-MV distinction: https://www.opencompute.org/news/powering-the-next-era-of-ai-how-google-microsoft-and-nvidia-are-standardizing-and-accelerating-the-industry-transition-to-lvdc/
- NVIDIA Aug 11, 2026 architecture: https://blogs.nvidia.com/blog/800-vdc-power-architecture-ai-factory/
- NVIDIA 2025 engineering context: https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories

# ONE-PAGE COMMERCIAL / ENGINEERING DECISION

| Decision | T4-S50-DC v0.3 |
|---|---|
| **Specific beachhead** | Existing or under-construction **AI data centers retaining a 480 VAC three-phase distribution system** and upgrading to **800 VDC rack/row delivery** via modular side-power-rack equipment. Not a direct 13.8 kV-to-800 VDC medium-voltage SST sale. |
| **First prototype product** | One **50 kW real output**, ~50 kVA-class **three-phase 480 VAC input, isolated 800 VDC output** power-conversion tile; SiC AFE / isolated DC-DC candidate. Nameplate kW, kVA and PF must be quoted separately. |
| **Initial system reference** | **250 kW peak 800 VDC hypothetical AI compute load** with **five 50 kW delivering tiles + one redundant 50 kW spare (5+1)**. This is a synthetic *study case*, NOT a real load contract, measured 2026 data-center trace or OCP-mandated exact rack rating. |
| **Competitive alternatives** | (A) Three-phase active-front-end + isolated dual-active-bridge; (B) direct AC/HF link or matrix-derived topology with suitable rectification/isolation; (C) conventional 50/60 Hz transformer + commercial rectifier/PFC and **selective partial-power** conditioning; (D) commercially available integrated power rack. Compare **identical 800 VDC output and protection**, not the old 120/240 VAC output. |
| **First deciding experiment** | DC bus regulation, efficiency-vs-load, variable AI load ramp, thermal, harmonics, protection, short-circuit fault clearing, isolation, modular droop/current sharing and hot standby in a qualified lab; compare total **installed $/qualified kW, $/delivered MWh and availability**. |
| **Cost-class study** | At 1–10 laboratory units, **assumed nonrecurring-engineering-excluded per 50-kW tile $16k–$70k**, with a transparent low/base/high work-breakdown below. These are **scenario envelopes**, NOT sourced SiC pricing, production cost, market quotes, purchase offers or validated economics. NRE and independent certification outside envelope. |
| **Supplier-dialogue objective** | Lock which supplier can quote 480 VAC three-phase input, voltage/current/output, safety and duty; get actual commercially current 50 kW module/system prices, cooling and independent test budgets before any funding commitment. |
| **Absolute stop rule** | If the 480 VAC retrofit path does not win against an OEM-standard 800 VDC power rack/rectifier on **full-chain energy, reliable fault protection, serviceability and lifetime installed price**, do not produce an SST on novelty alone. |

## 1. Exactly what does "solid-state transformer" mean here?

Three separate product **classes** must not be conflated:

**Class S50-AC (preserved v0.2):** 480 VAC **single phase** → 120/240 VAC 60 Hz, 50 kVA AC-output reference, rectifier + isolated converter + inverter. Candidate for specialty industrial AC power regulation. **Not appropriate** as an 800 VDC AI factory feeder. Keep its efficiency target **≥97% inclusive of auxiliaries** as an untested legacy target.

**Class S50-DC (new beachhead):** 480 VAC **three phase**, via suitable input breaker, sensing, AFE/PFC, isolated HF DC/DC and protection, to 800 VDC bus. May omit **output inverter** entirely. The product is **a high-frequency isolated AC-to-DC power module / side-rack building block**, not necessarily an SST under utility equipment definitions. Do not use the term SST as a substitution for legal product classification or qualification. Baseline with commercially qualified isolation and **no AHD/DISH**.

**Class MV-SST (future, wholly separate scope):** OCP-defined 13.8/34.5 kV input, 5/10 MW output SST / transformer rectifier skid, with medium-voltage insulation, BIL, fault current, cooling, busbar and load-management architecture. **This is not T4-S50-DC**; any future ORCS product must complete its own engineering, standard, grid interconnect and test design. OCP spec ≥98% 50–100% rated loading refers to **power-train loss only** and may exclude externally distributed cooling/auxiliary loads.

## 2. Reference electrical envelope — NOT a certified nameplate

| Item | Candidate specification | Needed engineering verification |
|---|---|---|
| Input | 480 V L-L RMS, three-phase, 60 Hz; input tolerances TBD | Grounding, neutral if any, transient, harmonics, protection, upstream transformer, actual site |
| Rated output | **50 kW at 800 VDC nominal**, nominal **62.5 A DC** | Define allowed DC voltage window, polarity, upstream source impedance and bus protection |
| Approx nominal input current | At 50 kW real DC, **~61.4 A/phase** at assumed 98% efficiency and PF=0.99 | \`50,000/(sqrt(3)*480*0.98*0.99) ≈ 61.4 A\` (rounded), not a cable-sizing instruction |
| Isolation | Galvanic with HF magnetic stage in A/B, or qualifying alternate | Rated impulse, barriers, creepage/clearance, continuous insulation monitor where applicable |
| Conversion | Option A: 3φ AFE/PFC → HVDC link → isolated DAB to 800 V | Actual DC link voltage, SiC ratings, thermal and controller topology **TBD** |
| Efficiency | Compete on **measured full-system** curve at 10/25/50/75/100% including coolant, fans and controllers | Do **not** quote 98% OCP MV SST power-train as proof T4-S50 achieved it |
| Power factor and harmonic current | Target PF >0.99 at rated, distortion to applicable current standard | Precisely identify service/load applicability; characterize faults and voltage sag |
| Modular system | 5 delivering + 1 spare for an assumed 250 kW peak bus; shared protected 800 VDC output | N+1 **capacity** does not automatically equal 99.9% or any uptime SLA |
| Service | Cassettes may be changed only via approved shutdown/isolation/discharge process | No unqualified "live hot-swap" of 800 VDC and no self-energized DC bus |
| Controls | Hardware safety PLC/gate, deterministic protections, digital twin and telemetry | No AI agent to override physical interlocks |
| AHD/DISH | Optional **noncritical** composite insulator/sensor/cooling part after its own G3 | No dependency of commercial S50-DC on speculative photocurable dielectric |

**Arithmetic:** at 250 kW, nominal total DC current = **312.5 A** at 800 V; if 5 tiles each supply 50 kW, each carries **62.5 A** nominal. If any one of six fully rated modules is offline, remaining five retain rated *aggregate capacity* only if the bus, upstream supply, thermal equipment, fault isolation and control permit. The six-module assembly has **300 kW installed conversion nameplate**, not 300 kW guaranteed delivered after fault in all conditions. No 50 kVA module should be silently treated as 50 kW real power without converter PF and thermal scope.

## 3. Engineering topology trade study

| Candidate | Isolating path / mechanism | Main advantage | Principal risks | Decision role |
|---|---|---|---|---|
| **A: 3φ active front end + DAB** | AFE/PFC and galvanic isolated high-frequency **dual-active bridge** DC/DC | Relatively well-understood SiC modularity, controllable PF, energy flow option, DC regulation | Two conversion functions, HF magnetic losses, DAB reactive circulating current, DC protection and losses | **Baseline first design study** |
| **B: direct/matrix-derived AC to HF link + rectification** | Controlled AC link with HF transformer, rectified to DC | Potential reduction of bulky DC link or conversion stages | Commutation, fault interruption, capacitor/EMI requirements, output regulation, difficult practical maturity | Research challenger; not automatically more efficient |
| **C: passive transformer + rectifier/PFC + partial-power conditioning** | Certified 50/60 Hz isolation handles bulk path; converter handles selected power fraction where possible | Lower cost/mature safety and potentially lower active processed power | Cannot pretend partial-power regulation supplies total galvanic isolation; voltage/load limits, harmonic, grid compliance and control complexity | **Must-beat system comparator** |
| **D: already commercially offered integrated 800 VDC side-power rack** | OEM equipment, full purchased interface and safety controls | Lower qualification risk, partner supply, actual warranty/service | Vendor lock-in, integration/fee and space limits | **Must-beat real supplier competitor** |

Important: a DAB is an isolated DC/DC *stage*; not a complete three-phase grid interface by itself. A matrix/direct AC-AC converter needs an appropriate rectification and DC output strategy to qualify for a DC rack. Partial-power paths must still satisfy **total** protection, isolation and delivery at actual loading. Topology ranking uses **measured** performance, not a paper-only "3 stages = worse".

**Weighted design scorecard (proposed selection rubric, no actual scores yet)**:
- End-to-end energy including controls/cooling and actual measured annual load profile — **25%**
- Fully allocated 1/10/100-unit manufacturing plus installed and 10-year service costs — **25%**
- Isolation, fault response, DC arc management, protection and independent compliance readiness — **25%**
- Achievable delivered power density, repair time, supply chain and reliability — **15%**
- Interoperable OCP interfaces and control/monitoring openness — **10%**

Any **fail** in isolation, fault control or test-stand safety is an absolute gate regardless of score. Customer-specific weights may supersede only via written agreed test plan.

## 4. Explicit prototype cost-class — assumptions, NOT vendor pricing

Estimates below are **internally selected order-of-magnitude budget placeholders** for a **50 kW, 480 VAC three-phase → 800 VDC isolated lab development tile**, at 1–10 prototype units. **Not a research-cited component cost survey, certified hardware bill of materials or commercial price.** They are chosen to trigger vendor responses and must be replaced by supplier-provided itemized offers. Costs per module USD:

| Budget category | Low scenario | Base scenario | High scenario |
|---|---:|---:|---:|
| SiC AFE switches/drivers and controller/sensing | $2,500 | $5,000 | $12,000 |
| HF isolated DAB power stage, transformer/magnetics | $3,000 | $6,000 | $15,000 |
| Input EMI/PFC filtering, DC bus passives and protection | $2,500 | $4,500 | $10,000 |
| Cooling, enclosure, thermal interface, bus hardware | $2,500 | $4,500 | $10,000 |
| Bench integration, QA, instrumentation and build labor | $5,500 | $9,500 | $23,000 |
| **Per-unit provisional total** | **$16,000** | **$29,500** | **$70,000** |
| **Per rated kW** | **$320/kW** | **$590/kW** | **$1,400/kW** |
| **Five delivering tiles / 250 kW load (no redundancy)** | **$80,000** | **$147,500** | **$350,000** |
| **Six tiles / 5+1 (300 kW installed nameplate)** | **$96,000** | **$177,000** | **$420,000** |

**Excluded:** NRE engineering/firmware, tooling/test fixtures, facilities and site construction, independent laboratory certification, fault/EMI type testing, OCP/customer qualification, product liability, sustained factory scaling, spare parts, markup, installation labor and building bus/UPS/BESS/short-circuit protection. A **hypothetical additional $250,000–$2,000,000 development NRE range** could be set aside for exploration; this range is merely a capital-planning stress case, not source-derived or a turnkey budget. **Do not sum costs without confirming which work a supplier's quote already includes.**

**Useful real-world but NON-EQUIVALENT anchors:**
- Public surplus EV charging listing offers a **50 kW rated power cabinet at $7,500** and other 100–360 kW used/surplus systems at different prices; these are **surplus offerings**, not current new SiC 800 VDC data-center rack products, not evidence our lab tile costs $7,500. https://provenperformer.com/btc-power-surplus
- Tritium Power describes a **50 kW liquid-cooled SiC AFE power module** with claimed peak efficiency **98.5%**, and a separate 25 kW isolated DAB module with claimed **99.1% peak**; their architectures, requirements, available supply, operating range and per-unit pricing must be independently checked. **Peak individual module efficiency cannot establish whole-chain efficiency**. https://www.tritiumcharging.com/technology/
- A listed **300 kW SiC inverter evaluation kit** at approximately **$18.5k** is not an isolated 50 kW three-phase AC→800 VDC conversion tile and cannot be substituted for a quote. https://store.nacsemi.com/products/detail?part=EVK-PLA1050B-96

**Supplier enquiry:** ask 3 power-module/cabinet companies and 2 independent test/integrator facilities for 1/10/100 **INDICATIVE** units, heat dissipation at 25–100% load, current ripple, isolation ratings, fault dynamics, recovery behavior, PF, input harmonics, warranty and total loaded/installed cost. Reject false whole-system efficiency comparisons and vendor claims without independent measurements.

## 5. Customer-independent fallback S0: reproducible **synthetic** 250 kW study load

No customer access is required to run a **publicly specified synthetic reference study**; however, no such simulation establishes a real operator's demand, revenue or measured workload. We must not invent a measured annual curve from "a named source" when sources do not publish one.

**Evidence anchors:** NVIDIA publishes a design range from ~100 kW to >1 MW rack scale and rollout to 800 VDC; OCP SST v0.3 establishes an 800 VDC interface and says actual detailed simulated load curves will arrive in future versions. It **does not publish a measured 250 kW workload curve here**. The following is **owner-program-assumed**, not endorsed or based on an actual rack meter.

**Full year at a 250 kW peak capacity:**
| Hours/year | Applied 800 VDC DC load | Annual delivered energy |
|---:|---:|---:|
| 2,000 h | 100 kW | 200 MWh |
| 4,000 h | 175 kW | 700 MWh |
| 2,760 h | 250 kW | 690 MWh |
| **8,760 h** | — | **1,590 MWh/year** |

Equivalent average delivered power = **181.51 kW** and load factor = **72.60%** relative to 250 kW maximum. **Not a real demand profile or financeable PPA.** Before HIL tests, specify time-series ordering, step/ramp magnitude, 10 ms–seconds transient waveforms, 24-h acceptance/dispatch patterns, upstream battery or UPS response, voltage sag, source trip, module outage, DC faults, a cyber-isolated safety override and thermal ambient. The 3-state table is sufficient for *aggregate energy*, not for dynamic protection validation.

**Energy sensitivity (illustrative):** if actual matched full-chain conversion efficiencies are **98%** vs **97%** constant over the same 1,590 MWh annual DC load:
- 98% chain requires **1,590/0.98 = 1,622.45 MWh** input.
- 97% chain requires **1,590/0.97 = 1,639.18 MWh** input.
- Annual difference = **~16.72 MWh** at this load. At an **assumed** $0.10/kWh energy rate, gross energy value ≈**$1,672/year** before cooling, peak demand/charges, reliability and real varying efficiency. A 1% conversion gain **alone** is unlikely to justify expensive prototype qualification at this small single-system scale. For a 5-MW and national-scale installed base the energy case could be materially larger; validate actual duty and costs.

**Availability scenario:** require demonstration that adding a nominally N+1 tile removes only **one module as a single failure point**, not a common bus, controls, cooling, upstream supply or software failure. A proposed **99.9%** system availability corresponds to at most **8.76 h annual downtime** mathematically, but **is not demonstrated** and may be inadequate for customer contractual AI infrastructure. No claimed reliability from a redundant schematic.

**S0 checkpoint:** seek 2–3 real customer/operator load curves, utility service specifications, facility cooling and fault data, and vendor system quotes. If unavailable after an **owner-chosen 30-day research interval**, proceed **only with this labeled synthetic study**; do **not** describe it as a named customer's actual 250 kW installation. This is a study workflow decision, not a promise to perform work in background.

## 6. Engineering test and procurement decision sequence

**D0 source and specification crosswalk:** Map OCP 800 VDC input compatibility, data-center retrofit power rack interface, common bus protection and approved grounding, applicable electrical safety codes. Show which OCP v0.3 requirements apply to **MV megawatt-class SST only**, versus which are transferable as *engineering guidance* to LVAC S50-DC. **No automatic OCP conformity claim.**

**D1 match architectures:** For A/B/C/D, publish same 480 VAC three-phase and 800 VDC regulated output, battery/UPS handling, load trace, protective functions, safe fault shutdown, isolation, same installed capacity and service boundaries. Record vendor and simulation input files.

**D2 stage emulation:** SPICE/PSIM/PLECS or appropriately validated controls simulator for AFE, DAB, direct link, passive+rectifier+partial-power; switching and magnetics thermal losses, EMI and gate-drive faults. Establish material and component availability before topology selection.

**D3 hardware at safe ratings:** Independently supervised low-energy bench power stages; qualify protection and controller behavior before rating escalation. Required faults include short-to-ground/bus, insulation monitor failure, thermal runaway and bus contactor failure.

**D4 first true 50 kW tile:** NRTL/compliance-oriented lab with appropriate site licenses and lockout/tagout; hardware E-stop, fusing, arc flash and supply isolation, DC bus discharge, cooling failure and third-party witness tests. No request for a makerspace to energize 800 VDC.

**D5 5+1 power rack integration:** Six independent tiles, nominal 300 kW installed rating, test to **250 kW delivered** and one unit out, bus/cable fault interruption, distributed current share, operation with one failed cooling pump/fan, power quality and fail-safe shutdown. No actual 99.9% SLA until MTBF and common-mode failures are modeled with data.

**D6 supplier price and go/no-go:** Independent quotations and test reports replace the $16–70k/tile placeholder and peak module efficiency brochure; compute cost of accepted qualified kW, installed thermal/electric, 10-year maintenance and DC delivered energy. Compare production 1/10/100 units to actual commercially available power rack systems.

**D7 independent customer pilot:** End-user signs actual scope and operating envelope, maintains existing protection and service alternatives, runs supervised site qualification. No utility/OpenAI/OCP/NVIDIA partnership claim until documentary evidence.

## 7. Opportunity landscape is not an order book

**Potential demand:** AI factory construction and the 800 VDC transition are documented trends, with OCP's Google/Microsoft/NVIDIA common specifications and NVIDIA's 80+ ecosystem companies. **Stargate** is a plausible *prospect class*, not an expressed customer, validated switchgear order, committed 800 VDC adopter or documented QPU installer. OpenAI's public Stargate announcements emphasize GPU/NVIDIA computing infrastructure, not a disclosed facility QPU plan.

**Competitive reality:** Eaton, Schneider, Vertiv, TI, Tritium/EV-industrial suppliers and other power manufacturers are active or relevant. Entry could be via **certified part and industrial subcontracting**, value-added converters, cooling/insulation and data-controlled commissioning, rather than claiming a new small company can outsell system-qualified incumbent hyperscale suppliers.

**Quantum extension:** NVIDIA's NVQLink is a *real* public QPU↔GPU integration architecture used at research centers; IBM has public quantum-centric supercomputing reference design. **No publicly verified Stargate QPU-node plan was found as of 2026-11-01.** A QPU service module needs an *independent* facility-level power quality, EMI/vibration, cryogenic plant thermal and real-time control qualification; 800 VDC power tile does **not** directly power superconducting quantum chips.

Sources:
- OpenAI Stargate infrastructure April 29: https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/
- NVIDIA NVQLink: https://nvidianews.nvidia.com/news/nvidia-nvqlink-quantum-gpu-computing
- IBM 2026 reference: https://newsroom.ibm.com/2026-03-12-ibm-releases-a-new-blueprint-for-quantum-centric-supercomputing
- Korean hybrid facility news: https://www.datacenterdynamics.com/en/news/south-koreas-sdt-opens-quantum-ai-data-center-deploys-20-qubit-quantum-computer-integrated-with-nvidia-dgx-b200-hardware/

## 8. Provenance, owner decisions and prohibitions

**RECOVERED_SOURCE:** ORCS T4-S50-AC v0.2, prior T4-S50 under Transformer 3.0. **PUBLISHED:** OCP 800 VDC v0.3, NVIDIA rack power transitions, cited public comparable product descriptions. **DERIVED:** 50 kW/800 VDC current, 250 kW rack current, 5+1 total capacity, exact budget-scenario sums, synthetic 1,590 MWh energy arithmetic. **ASSUMED:** cost bracket inputs and yields, 250 kW capacity and load bins, 99.9% availability aspiration, development NRE. **UNVERIFIED:** utility equipment classification, A/B/C/D weighted scores, physical converter, cost/performance outcomes and real customer adoption. **GATE_PASSED:** none for new T4-S50-DC.

**Never claim**: OCP's 5 MW MV SST specification is directly met by a 50 kW LVAC tile; a 0.6-second DISH optics demonstration prints power SiC/magnetics; peak efficiency of independent components multiplies into a certified rack; NVIDIA/OpenAI/Microsoft/Google endorsed the ORCS prototype; any Stargate site has publicly confirmed quantum processors; synthetic demand is metered demand; $16k–$70k is a supplier price or audited BOM; 5+1 nominal capacity guarantees a 99.9% SLA.

**Immediate action:** Pursue **real OCP ecosystem power-conversion requirements and bounded indicative quotes** for a 480 VAC three-phase to 800 VDC **50 kW isolated tile**, comparing an actually purchasable side-power-rack reference product. Use the reproducible 250 kW scenario only until an authentic measured deployment/load case is available. Preserve T4-P25-L and the research SiC AC product as separate branches.
