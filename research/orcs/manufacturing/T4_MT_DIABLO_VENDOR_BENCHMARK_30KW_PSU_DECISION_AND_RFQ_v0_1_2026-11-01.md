# ORCS Transformer 4.0 — OCP Mt. Diablo Supplier Benchmark, 30 kW PSU Decision and Bounded Indicative RFQ
## Verified commercial hardware comparison and immediate product decision · v0.1 · 2026-11-01

**Status:** SOURCE-TRACED RESEARCH / ENGINEERING SCOPE / SUPPLIER-DIALOGUE-READY, NOT PROTOTYPED, QUALIFIED, ORDERED, FUNDED OR ENDORSED. **No commercial vendor prices, confidential detailed BOMs or physical performance test data have been obtained**. "Comparable" means *similar application or system level*, NOT certified pin-compatible or OCP-conformant.

**This file is the next decision gate for** [Transformer 4.0 T4-S50-DC v0.4 OCP Mt. Diablo crosswalk](T4_S50_DC_OCP_MT_DIABLO_800VDC_STANDARDS_AND_QPU_INTEGRATION_SPEC_v0_4_2026-11-01.md). It **corrects** that document's implied positioning of 50 kW as a candidate *first* OCP PSU module. Original 50 kW three-phase 480 VAC → 800 VDC **continues as a separate custom product hypothesis**, but must not be represented as drop-in compatible with OCP Mt. Diablo Table 10.

## 0. Executive manufacturing decision

**Recommended first engineering target:** **T4-MD30** — a **proposed 1OU (~40–45 mm-high), 480 VAC three-phase input, galvanically isolated, up-to-30 kW PSU**, with **400 VDC floating output at the module level** and qualified rack/shelf circuitry producing **differential 800 VDC (three-wire ±400/common or specified isolated two-wire option)**. Precisely select one of OCP's three **different Table 10 physical solutions** before mechanical design; the headline "30 kW" is Solution 1 at 480 VAC, **not a universal 415/400 VAC rating**.

**Stop/redirect rule:** If an integrator's actual module dimensions, connection/midpoint, power-sharing, protection, cooling and qualification requirements cannot be met competitively with a complete independently engineered PSU, **do not launch a new converter**, and instead offer **module-forming, thermal, sensor, fixture, busbar accessory or test-automation manufacturing** where approved. Existing product test lab access and incumbent contracts are major barriers. AHD/DISH components are *optional* research and have not been qualified as critical dielectric parts.

**First engagement package:** obtain **two or more supplier/integrator feedback responses** on (1) the exact OCP variant and safety requirements, (2) real 26/27/30 kW module cost and availability at 1/10/100 units, (3) shelf/rack integration and testing, and (4) which noncritical manufacturing subparts are open to third-party manufacture. Do not promise 800 kW delivered from a pile of untested PSUs.

## 1. Primary standard: OCP Mt. Diablo v1.0.0, effective October 8, 2026

Official PDF: https://www.opencompute.org/wp-content/uploads/2026/10/OCP-Specification-Mt.-Diablo-Disaggregated-Power-Rack-Specification-v1.0.0.pdf

**Section 8.2.1, Table 10 (source PDF printed pp. 23–24):** published module reference solutions at:

| PSU physical solution | 480 VAC 3φ | 415 VAC 3φ | 400 VAC 3φ | Mechanical envelope without handle (printed p. 24) |
|---|---:|---:|---:|---|
| **Solution 1** | **30 kW** | **26 kW** | **25 kW** | Variant A **848 × 40 × 170 mm**; variant B **875 × 42.2 × 163 mm** |
| **Solution 2** | **27 kW** | **27 kW** | **27 kW** | **945 × 45 × 134 mm** (length 933 mm without handle also separately shown; drawing ambiguity must be resolved) |
| **Solution 3** | **26 kW** | **26 kW** | **26 kW** | **898.8 × 40 × 170 mm** |

**Never confuse** these with a single universal "30 kW specification". They are alternative component envelopes/ratings in one **shared system-level standard**, and do **not** certify any presently available supplier item. Original v1.0 table also lists different handle/non-handle dimensions, so any production mechanical drawing requires vendor-fit validation rather than reading these values as complete fabrication tolerances.

**Electrical topology nuance:** Per §8.2.1 the AC/DC **PSU module outputs 400 VDC**, connected into the shelf as a floating output with **+400, −400, common/midpoint/return** at the shelf, while an alternative **two-wire differential 800 VDC** distribution output is described. Individual 400-V PSU and 800-V shelf output are **not** the same connector, grounding, insulation or power-conversion stage. Select the published variant and its approved shelf-level interconnect/series or parallel topology explicitly; no arbitrary joining of PSU outputs.

**Integration requirements:** front accessible 1OU PSU, hot-swap/hot-plug **as part of a qualified shelf**, galvanic isolation of AC and chassis, rack shelf up to 2OU, three-phase AC PDU and output channel count matching actual PSU ports, droop/active current sharing, safety thermal sensor at bus clip, rack manager/telemetry, protection and earthing/midpoint engineering. **No exposed 800 VDC hot-plug or bench DIY handling**. Hot-swap is an engineered system capability, not a property of an isolated electronics card.

**OCP Table 9 rack efficiency** measures **AC PDU input → DC PDU output**, includes cooling, control, distribution, backup losses. At 480 VAC: >95% at 20% rack load, **>98% at 50%**, **>97% at 100%**. Vendor PSU peak efficiency cannot satisfy this requirement on its own. The separate OCP MV SST specification 5/10 MW at 13.8/34.5 kV is a **different electrical product**, not direct applicability to T4-MD30.

## 2. Verified announced competing hardware, as of November 1, 2026

### A. Delta Electronics — strongest detailed benchmark

Sources:
- Delta April 2026 product announcement: https://www.delta-americas.com/en-US/news/40116
- Delta Oct 2026 OCP Summit announcement: https://www.delta-americas.com/en-US/news/40272
- Delta Oct 2026 rack/shelf exhibition: https://www.delta-americas.com/en-US/landing/2026-OCP-Summit

**Vendor-published architecture**: **18.5 kW** AC/DC PSU module (up to 98% claimed peak efficiency) within an **110 kW** AC/DC shelf. Six nominal 110-kW power shelves, each with an **80-kW** battery backup subsystem, form a vendor-announced **660 kW** in-row rack with **480 kW** short-duration backup power. A distinct **800-kW** in-row rack without BBU is offered/shown. Delta displays 800-VDC infrastructure, a 90-kW DC/DC shelf converting downstream to ~50–54 V and 2.4–3MW cooling units.

**Important**: the Delta **18.5 kW module** is not the OCP Mt. Diablo Table 10 **26/27/30 kW module**. Their physical and electrical interchangeability has **not** been demonstrated. "110 kW shelf" is a shelf assembly, not an 110-kW 1OU PSU. Delta's Oct landing page separately describes a 110-kW 380–480 VAC AC/DC shelf **>97% efficiency with PMBus and hot-swap**; that is a *vendor claim and at the shelf-level*, not a measured Mt. Diablo ≥98% full-rack-at-50%-load test report.

**Benchmark tests to request from Delta or independent integrator:** actual SKU/datasheet; 800 V two-/three-wire architecture, PSU module size and power, actual 480/415/400 V derating, full-rack efficiency by OCP boundary, AC PDU/DC PDU/BBU inclusion, energy storage runtime at rated power, load step, current sharing, fault clearing, per-unit/whole-rack price, NRE, qualification, source country and warranty. None are public price quotes in current sources.

### B. LITEON — second announced hardware platform, limited numerical disclosure

Company's OCP 2026 newsroom: https://www.liteon.com/en/news/press-center/content/liteon-ocp-2026

LITEON's Oct 2026 materials describe **800-VDC power shelves**, **BBU**, **CBU**, Grid-to-Chip power distribution and high-density AI data-center systems; a **95-kW DC/DC shelf** and 280-kW CDU for NVIDIA Vera Rubin are separately mentioned. It does **not**, in the public article reviewed, uniquely identify an independently certified Mt. Diablo **Table 10 30-kW 1OU PSU with published electrical and mechanical pinout**. **Do not compare a 95-kW 800→50 V DC/DC shelf with a 30-kW 480VAC→400VDC AC/DC PSU** as though they perform the same conversion.

**Procurement question:** request a real AC/DC PSU shelf/PSU engineering datasheet, OCP Mt. Diablo v1.0 statement plus which solution variant and certificate/report, measured powertrain/rack efficiencies, service procedures, lead times and indicative pricing.

### C. Broader credible ecosystem, not yet exact product benchmarks

Dell'Oro's late-Oct 2026 OCP Summit observer report: https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/

Names additional 800V architecture participants: AcBel, Advanced Energy, Murata, Flex/Axiom, Eaton, Vertiv, Megmeet, xFusion, Bosch/Rittal. Some announced systems scale hundreds of kW or more but **not all have public component-level, version-specific ratings, pricing or confirmed interchangeability**. Create RFQ contacts only for vendors who can return an actual relevant **AC/DC** supply data sheet.

**Non-comparable trap:** Delta's OCP marketplace **33-kW Open Rack v3** shelf https://www.opencompute.org/marketplace/facilities-physical-infrastructure/delta-33kw-1ou-open-rack-v3-power-shelf/ outputs **48/50 VDC**, not differential 800 VDC, and should not be counted as an 800-VDC PSU competitor merely because its wattage is nearby.

## 3. Transparent technical comparison

| Metric | ORCS old S50-DC v0.3/v0.4 | New proposed **T4-MD30** | OCP Mt. Diablo v1.0 | Delta's publicly described hardware |
|---|---|---|---|---|
| Function | 480VAC→800VDC 50-kW **custom converter** | 480VAC→400VDC PSU into **±400 differential shelf** | Three physical reference PSU solutions then shelf/rack assembly | 18.5-kW PSU → 110-kW AC/DC shelf → 660/800-kW rack families |
| PSU rating | 50 kW **hypothetical** | up to 30 kW @480VAC, derate per selected variant | 30/27/26 kW @480; 25–27 kW @400/415 | 18.5 kW vendor announcement |
| PSU physical reference | Not selected | 1OU; pick **exact Solution 1 A/B envelope** | 1OU, 3 variants plus shelf ≤2OU | Contact supplier; public press does not give pinout/measurements |
| DC output distinction | v0.4 treats 800 differential as tile-level | Source-check 400 PSU vs shelf 800 differential | explicitly describes 400V PSU and differential 800 shelf | Confirm actual vendor rack/shelf architecture |
| Safety and uptime | Proposed | Needs independent qualification | System-level hotplug, earthing, isolation, current sharing and PDU | Vendor advertises hotswap and redundant BBU; system test not provided |
| Rack efficiency | No measurements | **No measurements** | At 480 VAC >95/98/97% @20/50/100% rack load | Vendor efficiency claims at PSU/shelf/system boundaries differ |
| Real supplier pricing | None | **None** | Specification, not a product price | None published in reviewed sources |
| Market claim | "AI rack" is opportunity | supplier-dialogue concept | Published interoperability requirements | Actual publicly showcased vendor architecture; procurement availability to be confirmed |

**Engineering decision:** **T4-MD30 wins the standards-fit screening over S50-DC as the first 1OU module candidate** only because it matches OCP's *documented reference power/size category*, **not** because ORCS has a better efficiency/cost/module design or a real purchase contract.

## 4. Quantity arithmetic and packing constraints — not a finished rack BOM

At nominal 800 V **differential rack bus**, a **30-kW successfully delivered module-equivalent** corresponds to \`30,000/800 = 37.5 A differential bus\`, after engineering proper shelf arrangements; if the PSU output port is 400 V at module level, **30 kW/400 V=75 A** nominal port current before conversion/series sharing interpretation. **These are circuit checks, not connector specifications**.

Minimum arithmetic (one equivalent module redundancy, no other derating, exactly rated usable output):
- 250 kW load at 30 kW-equivalent requires ceil(250/30)=9 active plus 1 spare → **10 modules, nominal 300 kW installed**.
- 800 kW at 30 kW-equivalent requires ceil(800/30)=27 active plus 1 spare → **28 modules, nominal 840 kW installed**.
- 800 kW at 27 kW-equivalent requires ceil(800/27)=30 active plus 1 spare → **31 modules, nominal 837 kW installed**.
- 800 kW at 26 kW-equivalent requires ceil(800/26)=31 active plus 1 spare → **32 modules, nominal 832 kW installed**.
- 1,100 kW at 30 kW-equivalent requires ceil(1100/30)=37 active plus 1 spare → **38 modules, nominal 1,140 kW installed**.

**All require real shelves, AC PDU connector counts, 2OU shelf limits, wiring, common bus, fault isolation, 800-V feed architecture, 800kW–1.1MW cooling, BBU/CBU and physical fit tests**. N+1 "one module" is not necessarily a valid failure/redundancy unit when a shelf, source or DC PDU fails. In particular, 28 1OU PSUs may not fit within OCP's available rack spaces using the required shelves; do not take arithmetic quantity as physical feasibility.

**Why size matters:** designing a 50-kW tile would require a **different physical, thermal, power-dense and interconnect architecture** than OCP Table 10 reference solutions. Retain as customized converter R&D, but not as the first standard-equivalent 1OU hot-plug PSU.

## 5. Risk-ranked product/manufacturing strategy

**Route R0 — Fastest practical industrial engagement:** target the **shelf and rack manufacturing supply chain**, not instant hyperscaler direct orders: qualified busbar mechanical components/insulating covers, sheet-metal enclosures, cooling manifold subassemblies, brackets, robotic fixture and test automation, traceable recovered Al/Cu/steel **only when specification-compliant**. Buy rated protection and semiconductors; do not claim direct customer relationship from public OCP news. Some critical insulating components require much longer proof than neutral mechanical parts.

**Route R1 — Bounded PSU feasibility:** only after an integrator shares a **real product requirement and variant** pursue T4-MD30: 480VAC, 1OU, 26–30kW family, safe galvanic isolation, correct 400V module/shelf ±400V arrangement, measured rack-level efficiency and 10-kHz pulse behavior where applicable, independently validated fault and transient tests. Evaluate actual module shelf fit with a 3D printed *noncritical* handling mockup first; never energize an unverified 800V rack.

**Route R2 — AHD/DISH research:** proceed on **noncritical sensor carriers/fixture details** and separate dielectric coupons. None is a certified energy-transformer primary insulation barrier without G3 pass. Do not tie acceptance of conventional power shelf to feasibility of UV optical processing of opaque composites.

**Route R3 — Custom S50-DC:** only if a named use case values 50kW per tile more than a compliant 26–30kW PSU, and can fund a distinct mechanical and electrical design + full qualification. Preserve research separate.

**Decision rule after quotes:** show *total tested rack cost per delivered kW*, full-rack efficiency incl auxiliaries, independent safety/short-circuit test scope, true accepted throughput, expected service outage, upstream source and DC protection, OEM licensing and supply rights. No investor claim from manufacturer marketing efficiency or from the 0.6-second DISH exposure time.

## 6. Bounded outreach / request for information template (not formal binding RFQ)

**Subject:** Indicative engineering dialogue — 480VAC 3φ / 26–30kW isolated PSU and Mt. Diablo rack component supply

We are conducting source-traced exploratory research on domestic, automated manufacture of power conversion subassemblies under an open interface approach. We request only **nonbinding** information:

1. Which **OCP Mt. Diablo v1.0.0, §8.2.1 Table 10** (or alternate customer-specific specification) module, shelf and DC pole/earthing arrangement do you actually support? Provide exact SKU, drawing, isolation and pinout and rated 480/415/400VAC derating.
2. What are the **published test boundary** and third-party evidence for 20/50/100% rack efficiency, transient response, DC fault/ground-fault interruption, current sharing and BBU options?
3. Which subassemblies (enclosure, thermal manifold, busbar insulator, noncritical composite mount, automation fixture, acceptance-test fixture) can be quoted separately and sourced from new suppliers? Provide material/drawing/compliance data and industrial IP/license rules.
4. Quote **indicative** nonrecurring engineering/setup, 1/10/100 modules and 1/10/100 compatible components, delivery windows, country of origin/recycled feedstock certifications, sample inspection and acceptance/test fees.
5. Do you permit a safety-reviewed **non-electrified physical mockup** for robotic assembly benchmarking, then a jointly defined qualified electrical lab plan? Do not request voltage energization or purchase.

**No factual claim that any vendor has agreed to participate.**

## 7. Facts, unknowns and first decisive experiment

**PUBLISHED**: OCP Mt. Diablo Table 10 three 1OU power classes 26–30kW; 400V PSU vs 800 differential shelf; efficiency boundaries; vendor Delta/LITEON announcements.

**DERIVED**: nominal kW-to-A arithmetic and module-count stress cases.

**PROPOSED**: T4-MD30 alternative, manufacturing routes R0–R3, conditional connector/mechanical qualification experiments.

**NOT VERIFIED**: exact cross-vendor mechanical/pin interchangeability, actually purchasable 30kW SKU, per-unit prices, end-to-end compliant PSU, supplier interest, 800kW packaging, guaranteed uptime, AHD/DISH qualification or project funding.

**Immediate work package:** obtain source **dimensional CAD and pinout for one specific OCP variant**, build an *unpowered* module/shelf robotic-handling and insulation-clearance fit mockup, estimate internal noncritical manufacturing cost with real component quotes, and independently test route to compliance. If unable to obtain product drawings, the honest outcome is **gap open**, not "product-ready".

**Publication source status:** This document is a public research/engineering design recommendation based on published material. It is not a standards-body implementation, manufacturing release, supplier endorsement or shipment.
