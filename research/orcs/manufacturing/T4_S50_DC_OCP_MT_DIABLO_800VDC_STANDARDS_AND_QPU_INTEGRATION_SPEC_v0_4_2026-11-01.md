# ORCS Transformer 4.0 — T4-S50-DC v0.4: OCP Mt. Diablo / LVDC Standards-Aligned Power Tile and Cloud-First QPU Integration
> **2026-11-01 commercial benchmarking correction — read this first:** The [actual OCP Mt. Diablo Table 10 vendor benchmark and T4-MD30 26–30 kW PSU decision](T4_MT_DIABLO_VENDOR_BENCHMARK_30KW_PSU_DECISION_AND_RFQ_v0_1_2026-11-01.md) finds **three different 1OU reference PSU solutions (30/27/26 kW at 480 VAC)**, NOT a 50 kW standard PSU. **§8.2.1 specifies a 400 VDC PSU output feeding a shelf delivering differential ±400 VDC or an isolated two-wire 800 VDC option**. The 50-kW tile below remains a **CUSTOM R&D branch**, not a drop-in OCP shelf part or known mechanically acceptable rack unit; its 17/21/23-module scaling arithmetic is not a compliant rack implementation. **For first standards-fit supplier dialogue select T4-MD30** and freeze an actual OCP Table 10 mechanical variant, electrical pinout, grounding, PDU and qualified protection before any hardware. No 30-kW PSU is claimed to be designed, built or quoted.

**Date:** 2026-11-01  
**Status:** SUPPLIER-DIALOGUE-READY / DESIGN TARGET / NO PROTOTYPE / NO CERTIFICATION / NO ENDORSEMENT / NO ORDERS.  
**Technology scope:** 480 VAC three-phase → differential 800 VDC power conversion tile for an OCP-inspired sidecar rack, **not** the OCP 5–10 MW medium-voltage SST product. A separate, intentionally isolated compute architecture permits **remote cloud QPUs first** and co-located real-time QPU control later. No QPU is declared operational within Stargate or any ORCS campus.

**Preserved earlier designs:** [T4-S50-DC v0.3 (250 kW reference, cost and topology)](T4_S50_DC_800V_AI_FACTORY_SST_RETROFIT_AND_TOPOLOGY_SPEC_v0_3_2026-11-01.md); [T4-S50-AC 480→120/240 V v0.2](T4_S50_SIC_SOLID_STATE_TRANSFORMER_ADVANCED_BRANCH_v0_2_2026-11-01.md); [T4-P25-L utility transformer](T4_P25_L_MODULAR_DISTRIBUTION_TRANSFORMER_PRODUCT_DECISION_AND_SPEC_v0_2_2026-11-01.md); [shared AHD/DISH research platform](T4_COMMON_AHD_DISH_DUAL_MATERIAL_ROBOTIC_PLATFORM_AND_COST_MODEL_v0_2_2026-11-01.md). This specification supersedes v0.3 for **standards crosswalk and scaling** while retaining its assumption-only cost model as historical screening, not vendor prices.

## 0. PRODUCT DECISION

**Near-term beachhead:** provide a *candidate* isolated **50 kW nominal AC/DC modular power shelf/tile** supplying the existing **differential 800 VDC (±400 VDC relative to a midpoint where selected)** data center power rack architecture, with all safety and AC/DC PDU interfaces designed against **OCP Mt. Diablo Disaggregated Power Rack Specification v1.0.0, effective October 8, 2026**.

**Why:** OCP's October 2026 specification already describes a **480/415/400 VAC three-phase sidecar** targeting **800 kW–1.1 MW+**. It is a much closer commercial specification for our LVAC retrofit module than the **OCP MVAC SST Specification v0.3.0 (June 22, 2026)**, which defines **13.8/34.5 kV three-phase input and 5/10 MW direct-to-800 VDC output**. The two scopes must not be conflated.

**Critical geometry:** ±400 VDC *differential* means a potential 800 V between +400 and −400 conductors, potentially with a physical midpoint/common under an approved protection/earthing scheme. **A unipolar 0-to-800 VDC output is a different pole, earthing and connector design** even when both show 800 V across terminals; require separately qualified interface configurations. All terminal labels, conductor insulation, neutral/midpoint, PE connection, touch safety and site protection coordination are **frozen per variant**. Do not silently bolt together unipolar and bipolar power supplies.

**First physical deliverable:** one 50 kW isolated converter using purchased qualified SiC and magnetic/electrical components; validated conventional insulation. **AHD/DISH dielectric parts remain an independently gated optional manufacturing study** and are not in the first critical electrical BOM.

**Decision gate:** can the tile contribute to a qualified rack that beats actual commercial competitors on ***AC PDU input → DC PDU output*** efficiency at required loading, transient performance, DC safety/fault clearing, field service, modularity, and full installed/lifetime cost? If not, redirect to component subcontracting or mature rack products.

## 1. PUBLISHED STANDARDS REGISTER — hierarchy and applicability

| Source | Published status / numbers | Applies to T4-S50-DC? | Compliance boundary |
|---|---|---|---|
| **OCP Mt. Diablo Disaggregated Power Rack v1.0.0** | Effective **2026-10-08**; Microsoft/Meta/Google; 480/415/400 VAC 3φ sidecar, differential ±400 VDC/800 V; ~800 kW–1.1 MW+ rack | **PRIMARY** sidecar rack target and subsystem qualification | Rack-level published requirements are **not automatically proven** by a 50 kW tile; design for compliant integration and measure at actual rack boundaries |
| **OCP Data Center Facility LVDC Distribution white paper v1.1.0** | OCP lists Sept 2026 release; architecture covering ≤1500 VDC | **SYSTEM design guidance**, earthing, coordination, DC protection and storage | White paper is architecture guidance, not automatic product certification; verify final text in procurement/compliance phase |
| **OCP SST Specification v0.3.0** | Effective **2026-06-22**; Google/Microsoft/NVIDIA; **5 MW at 13.8 kVAC**, **5 or 10 MW at 34.5 kVAC**, 800 VDC output | **FUTURE MV-SST class only**, informative consistency check | **Not a binding 50 kW 480 VAC product specification**; do not claim OCP-SST-v0.3 conformance |
| OCP Rack & Power / applicable interconnect specifications | Includes separate connector/cable, shelf, busway and DC power equipment work | Applicable once exact rack integration is chosen | Must verify each SKU and version in controlled configuration register |
| NFPA/UL/IEEE/IEC/electrical installation and safety | Applicable scopes vary by equipment, site, utility, rack and DC earthing | Regulatory engineer to establish **actual** matrix | Do not pick a standard by similar acronym alone; require independent appropriately accredited testing |

**Primary documents:**
1. OCP Mt. Diablo final PDF: https://www.opencompute.org/wp-content/uploads/2026/10/OCP-Specification-Mt.-Diablo-Disaggregated-Power-Rack-Specification-v1.0.0.pdf
2. OCP SST v0.3: https://www.opencompute.org/documents/ocp-sst-design-specification-v0-3-final-pdf
3. OCP LVDC project / v1.1.0 listing: https://www.opencompute.org/projects/data-center-facility/power-distribution/
4. OCP industry explanation of LVAC-sidecar vs direct medium voltage: https://www.opencompute.org/news/powering-the-next-era-of-ai-how-google-microsoft-and-nvidia-are-standardizing-and-accelerating-the-industry-transition-to-lvdc/
5. OCP Rack & Power current contributions: https://www.opencompute.org/projects/rack-and-power/

**Version control:** 2026-11-01 is the standards snapshot. Future OCP releases and supplemental voltage/connector specs require their own dated change-control review. OCP Mt. Diablo v1.0.0 explicitly refers to "differential 800 Vdc" and ±400 VDC distribution; its future native-800 V standard is not automatically embodied here.

## 2. INPUT/OUTPUT AND RACK IMPLEMENTATION TARGETS

| Attribute | Published OCP Mt. Diablo v1.0 | ORCS proposed requirement / verification |
|---|---|---|
| AC entrance | 3-phase 480/415/400 VAC, 50/60 Hz, WYE or delta configurations; nominal tolerances ±10%, other conditions per spec | First target **480 VAC 3φ**, with earth/neutral variant-specific protection. No claim of 415/400 compliance until tested |
| DC entrance to IT racks | Differential **800 VDC** with ±400/common options per configuration, connector-level protection | Two **separate interface variants** considered: bipolar ±400 V/common or 2-wire differential; 0→800 unipolar **separately engineered**, not presumed interchangeable |
| Sidecar output power | **800 kW to 1.1 MW+** depending on AC input/system | **50 kW power tile** is ORCS module concept, not OCP-specified PSU rating |
| Output cable options | **50 kW or 100 kW** per DC output cable in protection module configurations | A 50-kW tile **need not equal one cable**. Current sharing and protection PDU require separate rack engineering |
| Dynamic loading | Fast pulse profiles, including 10 kHz and **up to 175% short pulse** examples; ~**3 ms settling** and ±3% transient in specified test | Exact test fixture and safe power ceiling by *tile and rack*; no promise a 50 kW tile can deliver 175% without qualification |
| PSU no-storage hold-up | Up to **20 ms** at full load, per spec boundary | Design and test ride-through or approved partition with downstream hold-up; real source and definition recorded |
| With BBU | **45–90 seconds** at full load (when chosen) | Storage is **rack/system option**, not assumed inside 50-kW tile |
| Efficiency, **full sidecar AC PDU → DC PDU** | At **480 VAC**, >95% @20% load, **>98% @50% load**, >97% @100% load, including cooling/control/distribution/backup losses | Target in **assembled rack**, not claim achieved or derived from each module's peak efficiency |
| Redundancy | Distributed/parallel racks with load-sharing; AC input may have N+N supply | Demonstrate isolated failure, shared-bus protection, independent rack PDU failure cases and reconfiguration |
| Grounding | Midpoint resistive or solid options and alternative 800V earthing schemes | Final site topology requires insulation monitor and fault/grounding design; do not hardcode a universal neutral or PE mapping |
| Instrumentation | Rack management, telemetry, communication, measured power and fault | Independent deterministic controls, serial/lot history, authenticated read-only data access by AI; software cannot defeat safety PLC |
| Safety/service | Segregated AC/DC PDU, protected disconnect before cable unplugging | **No energized connector handling** unless the specifically qualified protection system expressly supports the service procedure |

**Efficiency must be reported with the same boundaries as OCP Mt. Diablo**. OCP's MV SST **≥98% power-train only at 50–100% utilization** is **NOT equivalent** to the sidecar's >98% ***end-to-end including auxiliaries*** at 50% load.

## 3. Proposed MODULE / RACK scalability

**50 kW module**: nominal 800 V × 62.5 A DC; input AC line current at **assumed** 98% power-train efficiency and PF 0.99 = \`50,000/(sqrt(3)×480×0.98×0.99) ≈ 62.0 A\` per phase (not an engineering wire size). Bus and input harmonic loads depend on measured whole-chain performance.

**Three levels of demonstrator:**

| Stage | Installed tile count | Available nameplate after one tile fails | Intended status |
|---|---:|---:|---|
| One power tile | 1×50 kW | 0 if that one fails | First engineering model |
| **250-kW study** | **6×50 kW (5+1)** | **250 kW** | **Synthetic lab/engineering system only**; not a complete Mt. Diablo sidecar |
| **800-kW rack proposal** | **17×50 kW (16+1)** | **800 kW** | Industrial scale hypothesis; not known to fit specified rack footprint or thermal distribution |
| **1.0-MW rack proposal** | **21×50 kW (20+1)** | **1.0 MW** | Industrial scale hypothesis; not known to fit specified rack footprint or meet OCP AC/PDU limits |
| **1.1-MW rack proposal** | **23×50 kW (22+1)** | **1.1 MW** | Industrial scale hypothesis; only after confirmed site, PDU and cabinet |

The table is **arithmetic modular count** and nothing more. OCP Mt. Diablo specifies real rack envelope, 6,000-lb load target, PSU/shelf dimensions, cable routing and thermal management. **Do not assume 17–23 tile cassettes physically fit** or that AC PDU / busbar / cooling can survive the corresponding current. Design for ***rack-level 800–1,100 kW with a feasible mechanical module size***; a smaller/larger rated tile may be the better standard after OEM consultation. Absolute "plug and play" of electrical power internals is forbidden.

### 3.1 250-kW test rig — keep synthetic waveform, add published OCP impulses

Retain v0.3 study as a **synthetic** 250 kW maximum load: 2,000 h ×100 kW +4,000 h ×175 kW +2,760 h ×250 kW = **1,590 MWh/year** delivered. This is *not* customer-metered demand and does **not** test the 10-kHz transients.

Add **independent** hardware-in-the-loop transient suites grounded in OCP Mt. Diablo Tables 6–8: 20, 100, 500 Hz, 1 kHz, 4 kHz, 5 kHz, 6.5 kHz and 10 kHz patterns and bounded short-term pulse magnitudes up to 175% TDP, with load bank and qualified test stand capable of handling the transient. **Do not demand 175% from an unvalidated bench converter**. Exact device/cable/bus ratings and protection always win over an attempted stress test.

### 3.2 DC protection and power sharing

- Verify exact grounding/earthing version (differential ±400/common vs unipolar 0/800 with return), polarity, continuous insulation monitor, rack common mode and fault detection.
- Protect each AC input, AFE and DC tile; precharge power bus safely; enforce no DC cable exposure during unplug; approved emergency stop and lockout.
- Demonstrate measured overcurrent, DC arcing/ground-fault isolation, short/bus fault, false-trip stability and protection coordination with BBU and rack DC/DC.
- Select droop/current-sharing architecture and reproduce faulted-tile reallocation without collapsing 800 VDC voltage tolerance. Confirm failure of common DC PDU is not misrepresented as solved by N+1 converter modules.
- Define **machine safety lifecycle and cybersecurity**; telemetry/AI are supervisory only and cannot close unsafe power contactors.

### 3.3 Energy storage / backup accounting

BBU optional **45–90 s full-load** rack supply (per source when BBU used) is a separate rack-BBU specification. At **800 kW**, lossless DC energy alone is **10–20 kWh** for 45–90 s, before conversion losses, temperature, aging, depth of discharge, surge or redundancy. At 1 MW, 12.5–25 kWh DC ideal. Do not confuse the energy number with the **much harder 800-kW–1-MW power delivery and fault management** requirement. Specify tested battery chemistry, BMS, fire containment, cooling, AC interruption response and independently compliant BBU. Capacitor bank (CBU) option is a separate power/energy trade.

## 4. Power conversion topology and cost model

Four v0.3 candidate topologies are retained:
A. Three-phase active front end (AFE)/PFC → high-voltage DC intermediate → **isolated dual-active bridge** to the protected differential 800 VDC bus (**first candidate**).
B. Direct matrix-derived AC-to-high-frequency-link with isolated DC rectification (**challenger**).
C. Certified industrial-frequency passive isolation, rectifier/PFC and **partial-power** regulation where it can meet exactly the same 800 VDC envelope, isolation and protection (**must-beat comparator**).
D. **Real commercially available** OCP-oriented sidecar PSU/shelf/rack (**must-beat product comparator**).

No claim of final 50-kW topology, switching frequency, SiC ratings, closed-loop stability, full-power insulation or service life. Preserve original v0.3 ***assumption-only*** per 50-kW lab tile **$16k / $29.5k / $70k** cost scenarios. These were **illustrative budget stress tests**, not verified vendor price bands. A 17-module nominal 800-kW rack would imply $272k / $501.5k / $1.19M of these **notional module-only values**, before AC/DC PDU, transformer/site interface, rack structure, cable/bus/BBU, qualified cooling, field installation, certification and profit. **Do not report as rack price.** First supplier RFQ is still bounded indicative.

**New cost comparison boundary**: all-in cost per **qualified kW of DC output at actual rack DC PDU**, external AC distribution, energy loss at measured dynamic load, tested redundancy, cooling water, warranty, replacement time and ten-year service model. Do not compare a bare SiC switching board to a commercial complete power rack.

## 5. Standards crosswalk deliverables before any prototype RFQ

**OC-01** *OCP/Mt Diablo scope*: signed matrix mapping every relevant v1.0.0 item (nominal and transient voltage/current, PF/harmonics, grounding, BBU/CBU, efficiency test boundary, redundancy, connector/PDU, EMI, safety, controls) to one of **in-scope**, **rack-integrator-owned**, **conditional**, **not applicable** or **not yet evaluated**. Cite exact PDF page and clause; never write "OCP compliant" prematurely.

**OC-02** *Operational interfaces*: selected AC connector/whip and actual 480 WYE/delta and 3-phase configuration; DC connector/pole arrangement; no-mate/no-energize protections; terminal isolation; interlock state charts; network isolation.

**OC-03** *Electrical test matrix*: 20/50/100% full-rack **end-to-end** efficiency plus relevant 10/25/75% intermediate data, 10-kHz impulse response, DC ripple and droop, 45–90 s BBU hold-up if equipped, no-storage 20 ms, staged failover, ride-through and utility harmonic checks with actual standards.

**OC-04** *Mechanical fit*: reconcile module enclosure volume, rack height/width/depth, weight, PSU shelf/BBU clearance and DC PDU barriers. OCP typical rack dimensions vary by operator; no claim the historic factory tile is physically compliant.

**OC-05** *Safety and accreditation*: independent compliance engineering for final product classification; any UL/NFPA/IEEE/IEC law/standard selected by actual scope. Hardware electrical protection independent of supervisory AI.

**OC-06** *Industrial procurement*: 1/10/100 tile cost and build-time with supplied real BOM and material origin, and a separate **actual 800-kW site/rack bill of materials**. Record R&D NRE, tests, service obligations and 24/7 staffing explicitly. No field deployment without approval.

## 6. Quantum processing architecture — CLOUD FIRST, REAL-TIME LOCAL OPTIONAL

**No QPU installation is needed to build an AI factory or T4-S50-DC power sidecar.** Quantum processors are optional *application services*; the energy conversion product should not advertise quantum-performance gains merely because a customer can call a QPU API.

The compute program consists of **three physically and operationally distinct tiers**, after the IBM QCSC and NVIDIA NVQLink architectures:

| Tier | QPU + GPU/HPC relationship | Network / latency posture | Use | Infrastructure commitment |
|---|---|---|---|---|
| **Q0 — cloud QPU API** | CPU/GPU/HPC hosts submit circuits to provider's QPU via managed APIs and retrieve results | Public/private WAN; queue + transfer + job overhead; **not deterministic real-time** | Chemistry/materials, batched QAOA/VQE-like experiments, benchmarking, model research | No owned QPU or on-prem cryostat; provider maintains **its own local QPU controls** |
| **Q1 — colocated/nearby QPU** | QPU with nearby deterministic classical runtime, plus same-campus GPUs / near-time networking | Deterministic host-to-QPU controller where needed, e.g. RoCE/RDMA; validated service-specific latency | Faster hybrid loops, calibration/error-mitigation experiments, reduced queue and data movement in certain cases | Dedicated isolation, cryogenics/lasers depending on modality, EM/vibration controls, reserved GPUs |
| **Q2 — tightly coupled quantum/classical realtime** | Real-time GPU host + Quantum System Controller (FPGAs/RFSoCs) + QPU in same QPU system/network | **Microsecond-to-millisecond** functions depending on QPU; NVIDIA NVQLink has a published **<4 microsecond reference callback** example, **not a guaranteed universal requirement** | Real-time feedback, QEC decoding, autocalibration and eventual fault-tolerant workloads | Specialized deterministic control; cloud WAN cannot close required microsecond feedback loop |

**Important nuance:** A QPU **accessed via cloud** still has real physical qubits and specialized colocated control/readout hardware at the provider. We are choosing **where the user-facing hybrid HPC and science workflow runs**, not eliminating classical controllers.

**IBM QCSC tiers:** QPU + local classical runtime (FPGA/ASIC/CPU) → colocated partner GPU/CPU "scale-up" via near-time network → more remote/cloud "scale-out" CPU/GPU. IBM specifically states cloud and on-prem integration work. NVIDIA NVQLink emphasizes GPU↔QSC realtime connections using RoCE, ConnectX and host/controller coordination. Neither requires every AI campus to own a QPU.

**Sources:**
- IBM March 2026 reference: https://research.ibm.com/blog/quantum-centric-supercomputing-system-reference-architecture
- NVIDIA technical architecture: https://developer.nvidia.com/blog/nvidia-nvqlink-architecture-integrates-accelerated-computing-with-quantum-processors/
- NVIDIA FAQ: https://www.nvidia.com/en-us/solutions/quantum-computing/nvqlink/

### 6.1 Beyond Q / Stellar Forge deployment recipe

**Phase Q0 (first):** pluggable QuantumService adapter implementing:
- \`list_backends()\`: provider, device family, current queue estimate, credential/data residency/price and retention scope;
- \`submit(circuit, shots, constraints)\`: explicit permitted user authorization and budget ceiling; no implied execution on every simulation;
- \`status(job_id)\`, \`results(job_id)\`, \`cancel(job_id)\` where supported;
- provenance record: complete circuit representation, backend calibration/version, compilation/transpilation parameters, physical/software metadata, price/queue/run time, seeds, shot uncertainty and result checksums;
- independent **classical baseline** and no claimed advantage until observed speed/quality/cost on equivalent scientific task;
- data-security/Export Control/licensing for controlled scientific materials; HIPAA or other sensitive data needs its own lawful requirements and access boundaries.

**Phase Q1 (conditional):** when a specific subroutine's measured *locality penalty* (WAN queue/transfer/iteration latency, restricted data or billing) dominates, research on-site QPU systems. Define **physical modality and OEM** before booking cryo, vibration, EMI, shield, temperature, contamination, 480/800-VDC isolation and safety requirements. QPU chip is **never** connected directly to an 800 VDC rack bus; use approved multistage conversion/power quality to its actual instrument specification.

**Phase Q2 (research-only):** QEC/real-time host and QSC vendor integration after deterministic benchmark and safety review. A software scheduler cannot satisfy hardware-real-time QEC simply by moving cloud endpoint closer in logical topology.

**Stargate case:** OpenAI/Stargate's published data-center builds have **no publicly substantiated QPU-node deployment or quantum-hybrid purchase commitment** in the sources checked 2026-11-01. No partnership or plan is implied. Stargate could be a *potential* AI infrastructure buyer class, not the reference client and not a known QPU customer.

## 7. Three highest-value experiments

**E1 — supplier standard crosswalk / no high-voltage energization**: compare one actual OCP-derived compatible converter/PSU quote with hypothetical 50-kW tile; extract true mechanical PDU/connector/power profiles; produce signed gap table and source-referenced test plan. Result: "viable component SKU?" with fail/pass on real interface.

**E2 — full-chain time-dependent hardware-in-the-loop**: simulated 250-kW 5+1 load with **OCP Mt. Diablo documented pulse suites** and protection faults, independent 480 VAC→DC measured efficiency and transient logs in safe qualified equipment. Result: can the architecture be scaled to an actual 800-kW rack while meeting spec without unqualified stress or bad physical packing? Do not call a controller-only sim certified.

**E3 — cloud QPU benchmark**: three candidate **small quantum-compatible subproblems** from materials/chemistry/optimization; compare provider QPU jobs against reproducible classical alternatives with end-to-end wall-time, queue, uncertainty, spend and result quality. A QPU result is **not** an end-to-end WarpX/OpenMC acceleration claim. Only after actual benefits or real-time feedback requirements should QPU hardware procurement be scoped.

## 8. Evidence register / prohibited extrapolations

| Claim | Evidence level |
|---|---|
| OCP Mt. Diablo v1.0.0 800kW–1MW+ at 480 VAC; ±400 differential 800 V; test boundaries | **PUBLISHED** OCP October 2026 |
| OCP SST v0.3 5/10 MW MV conversion, nominal 800 VDC and ≥98% *power-train-only* efficiency | **PUBLISHED** OCP June 2026 |
| OCP LVDC v1.1.0 Sept 2026 release | **PUBLISHED version listing**; detail needs controlled source document in conformity matrix |
| 50-kW ORCS tile, modular 17/21/23 tile count and 250-kW 5+1 bench | **PROPOSED / DERIVED COUNT**, not an OCP qualified tile |
| $16k/$29.5k/$70k per 50-kW tile | **ASSUMED V0.3 COST SENSITIVITY**, not procurement |
| Cloud-accessible QPU and QCSC hybrid orchestration | **PUBLISHED architecture**, but no ORCS implementation |
| NVQLink real-time callback architecture and QEC usage | **PUBLISHED example**, QPU-specific timing required |
| Stargate QPU node, ORCS provider commitments, whole-rack 98%-at-half-load, fully printed converter | **NOT VERIFIED / NOT CLAIMED** |

**Release authority:** product compliance authority for 480/800-V power; quantum vendor for quantum controller latency; operator for real data center load contract; independent materials lab for any AHD/DISH high-voltage insulation. No autonomous energization or L2 field connector switching and no use of human-unreviewed AI output as a grid safety control.

**Next funded engineering decision, not yet approved:** obtain independent supplier/OCP connector and rack integrator feedback on exact Mt. Diablo v1.0.0 480 VAC/800 VDC interface **before** refining a production BOM; in parallel perform **cloud-QPU software-only experiments** if the user chooses those workloads.
