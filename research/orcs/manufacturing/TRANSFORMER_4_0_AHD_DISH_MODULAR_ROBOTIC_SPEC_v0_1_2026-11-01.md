# ORCS Transformer 4.0 — Acoustic-Holographic/DISH Two-Material Modular Manufacturing and Robotic Assembly
> **November 1, 2026 packaging update:** This **v0.1 is the preserved integrated research program**, not a supplier-ready product specification or binding RFQ. The operational documents are now **[T4-P25-L product decision / passive transformer v0.2](T4_P25_L_MODULAR_DISTRIBUTION_TRANSFORMER_PRODUCT_DECISION_AND_SPEC_v0_2_2026-11-01.md)**, **[T4-S50 advanced SiC SST v0.2](T4_S50_SIC_SOLID_STATE_TRANSFORMER_ADVANCED_BRANCH_v0_2_2026-11-01.md)**, and **[shared AHD/DISH platform / cost-class appendix v0.2](T4_COMMON_AHD_DISH_DUAL_MATERIAL_ROBOTIC_PLATFORM_AND_COST_MODEL_v0_2_2026-11-01.md)**. All v0.1 technical material is retained for provenance; the earlier phrase "RFQ-READY" is superseded by **SUPPLIER-DIALOGUE-READY** for bounded indicative enquiries only. DOE's April 2024 final rule remains binding for 2029 unless formally amended; the 2026 RFI does not itself change that rule. The DOE 80,000 figure is potential configuration combinations, not an order-frequency distribution. No lab or prototype validation is claimed.

**Specification:** T4-AHD-R v0.1 · **Date:** 2026-11-01 · **Status:** PRESERVED INTEGRATED RESEARCH PROGRAM / SUPERSEDED FOR SUPPLIER-FACING USE BY FOCUSED v0.2 PACKETS; NOT PROTOTYPED, CERTIFIED, OR FUNDED  
**Program:** ORCS / New Deal 2.0 / Atlas Lattice Everywhere Factory / HTAM  
**Design maxim:** **Sound positions. Light locks. Robots assemble. Certified conductors carry.**  
**Primary objective:** Maximize the share of transformer components made from locally recovered, certified feedstock by programmable **two-feedstock** manufacturing cells and robotic, keyed modular assembly, without relaxing electrical safety, electromagnetic efficiency, reliability, or field-service standards.

## 0. Executive decisions

1. **Two complementary product families:** **T4-P** passive 60 Hz distribution transformers for utility deployment and **T4-S** SiC-enabled solid-state/hybrid transformers for independently qualified power-conditioning applications. These have distinct performance, costs, standards, and certification gates. A 480 V / 50 kVA SST is *not* a 7.62 kV medium-voltage service transformer.
2. **Two-material means two independently controlled primary feedstock streams per fabrication cartridge**, not a claim that a complete transformer needs only two chemical substances. Different production modules can use different validated material pairs; purchased qualified semiconductor, fastener, safety and bearing assemblies are precision components, not printer feedstock.
3. **Most viable near-term application:** Acoustic-aligned recycled-polymer/recovered-ceramic **dielectric guides, spacers, bobbins, terminal barriers, oil/ester-compatible guides, sensor capsules, ducts**; DISH locks photoreactive matrices **after imaging confirms placement**. **DISH cannot currently print dense transformer-grade steel cores or highly conductive solid copper windings.** Those are produced by separate qualified metal machines then robotically assembled into the same keyed system.
4. **Modularity is strongest at the factory**, not through live medium-voltage plug-and-play. Robots may slot, locate, clamp and fixture modules, but primary/secondary electrical connections need rated factory joints; magnetic circuits need controlled air gaps and matched laminations; dielectric boundaries require qualified continuous barriers. No energized hot-swapping of transformer internals.
5. **Upscaled DISH/HTAM is an R&D track.** Original DISH supports ~19 µm overall features over ~1 cm optical depth and 0.6 s *small transparent resin object exposures*, not meter-scale mixed-metal parts or sustained factory takt. Heavy scatterers, opaque metal fillers and chemical-cure rates may defeat DISH entirely.
6. **Standardize interfaces, not one national voltage ratio.** Family-specific kVA, primary and secondary voltages, phase, taps, impedance, BIL, thermal fluid, protection, mounting, utility purchasing requirements and regulation all require distinct qualification.

## 1. Product requirements and reference equipment

### 1.1 T4-P25-L: initial grid product (design **target**, not existing hardware)

| Attribute | Proposed reference | Qualification status |
|---|---|---|
| Application | Single-phase, overhead, liquid-immersed residential distribution | Target family |
| Rated apparent power | 25 kVA continuous; scalable named variants 10 / 15 / 25 / 37.5 / 50 / 75 / 100 kVA | Target, dependent on cooling |
| Primary service | 7.62 kV line-neutral on 13.2 kV grounded-wye feeder; other utilities need separately specified HV windings | Nominal reference; not universal |
| Secondary | 120/240 V split phase, 60 Hz | Reference |
| Insulation class / BIL / impedance | As required by selected utility and relevant IEEE/ANSI standards; **must be established by qualified electrical design** | OPEN |
| Magnetic circuit | Qualified grain-oriented electrical-steel or amorphous-metal laminations with measured no-load losses, not DISH resin | Baseline technology |
| Winding circuit | Recovered-content, certified copper or aluminum with rated insulation, welded/brazed/qualified terminals | Baseline engineering, supplier quote required |
| Cooling | Sealed mineral oil or suitable ester, independent variant and fluid-material qualification | Both candidate paths |
| Mechanical | Rated weatherproof tank, mounting bracket, corrosion protection, surge provision, tank grounding | Independently qualified |
| Sensors | Optional low-power external/magnetic or temperature-health sensing; removable only under approved isolation | Noncritical initial option |
| Minimum efficiency | At least **equipment-class-specific** applicable DOE requirement; design for requirements effective **2029-04-23** unless rule changes | Must be certified; no invented universal percent |
| Useful life | LCCA horizon 30 years (financial comparison, **not demonstrated warranted service life**) | Target only |

At 25 kVA: nominal primary current ≈3.28 A at 7.62 kV; nominal 240 V secondary full-load current ≈104.17 A. These are simple nameplate checks, not conductor, fuse, transient or terminal design.

**First electrical prototype should be a controlled low-voltage 1–5 kVA bench transformer**, before a utility medium-voltage engineering article. A lab-rated article is not a utility product.

### 1.2 T4-S50: retained advanced branch from 2026-10-31 Transformer 3.0

- Reference candidate: **50 kVA**, single-phase **480 V AC in → 120/240 V split phase**, SiC rectifier / isolated high-frequency DC/DC / inverter stages; >=97% full-system efficiency, +/-1% regulation, <3% output THD were **previous owner targets, unverified** and must be measured at specified load points.
- Electronics, magnetic design, thermal and insulation system must be engineered as one converter. Replaceable controls/semiconductor cassettes may be fitted with keyed service connectors while de-energized; DC bus discharge verification and safe isolation are mandatory.
- Do **not** substitute this topology for the T4-P 7.62 kV distribution transformer. Competing against a 99%+ passive transformer requires explicitly valued extra power-conditioning functions and a full-chain energy-loss comparison.

### 1.3 Other qualified catalog families (planned, not one common BOM)

- **T4-P-O** single-phase polemount utility class.
- **T4-P-P** single-/three-phase padmount and vault; independent HV, phase and fluid ratings.
- **T4-P-D** commercial dry-type; alternate thermal and fire systems, no oil/ester assumptions.
- **T4-S** optional SiC/hybrid conversion for bidirectional DER/DC/industrial systems; independent power-electronics certification and EMI/fault requirements.

## 2. Two-feedstock module architecture

**Rule T4-MAT-001:** Every *experimental material-forming cell* receives two independently metered, traceable primary feedstock streams A and B, optionally executed as sequential locked layers/cycles. It must record their source, lot, composition, rheology, contamination, acoustics, spectral attenuation, cure profile and post-process quality. Conventional nonprinting manufacturing units may also carry two primary functional materials (e.g., metal + insulation) but use suitable joining/lamination rather than pretending DISH cures metal.

| Module family | A (recovered, qualified) | B (recovered, qualified) | Production route | Intended use / hard limitation |
|---|---|---|---|---|
| **D1 dielectric spacer** | Chemically recycled-content UV-curable insulating polymer formulation | Nonconductive recovered silica/alumina/glass ceramic, dielectric-qualified | Acoustic spatial orientation + DISH matrix cure; optional separate postcure | Spacers and bobbins; prove PD, fluid aging, creepage, dielectric strength |
| **D2 thermal/dielectric guide** | Photocurable insulating polymer | Recovered electrically insulating thermally conducting ceramic (e.g., qualified alumina / BN **if certifiably recovered and chemically suitable**) | Acoustic/DISH only if optical transparency permits; otherwise hybrid casting | Thermal guides; particles cannot form unintended electrical paths |
| **D3 sensor capsule** | Recycled-derived insulating transparent polymer | Qualified recoverable glass/ceramic or passive sensor carrier | DISH overmold around separately inspected sensor | Sensors outside primary barrier; chips are purchased components |
| **C1 conductor former** | Recycled and conductor-grade refined Cu/Al | Certified conductor insulation film/coating | Automated bending/foil winding + dielectric application, robot placement; **not** DISH metal curing | Winding assemblies; verify resistance, AC loss and termination integrity |
| **M1 core lamination packet** | Reprocessed/qualified electrical-steel or amorphous alloy | Rated interlaminar dielectric coating | Slit/anneal/punch/stack/bond with robotic handling | Core packets; no DISH claim for magnetic performance |
| **H1 thermal/mechanical package** | Certified recycled Al or steel | Qualified electrically insulating/corrosion-barrier coating | Metal forming/print/machining + surface finishing | Heat sinks, tank brackets, mounting, fluid interfaces |
| **E1 enclosure/sensor shell** | Qualified recycled thermoplastic | Nonconductive recovered reinforcement/filler | Extrusion/injection/additive + robotic finishing | Noncritical housing features. **No conductive graphene/carbon in HV dielectric surfaces** without evidence |

All recycled-content claims require mass-balance traceability, composition and impurity analysis, same-lot coupons, incoming-acceptance criteria and repeat production approval. Feedstock acquisition may be modeled **$0 or a tipping-fee credit** only if a real supply contract supports it; washing, sorting, mechanical/chemical conversion, binder, energy, transport, qualification, reject disposal and hazardous recovery are always costed. **No unqualified waste-derived polymer is permitted in a critical dielectric barrier.** BAETA is a carbon-capture sorbent in historical work, not a certified magnet alloy or dielectric resin; never assume its use in structural/electrical components. When recovered feedstock cannot meet certification, **hold that part rather than substituting unverified materials**; precision certified purchased equipment is a distinct program exception.

## 3. Physical plug-and-slot interface specification

**T4-IF-001 — Mechanical datum:** Each module carries a digitally defined datum A/B/C, a robot-facing grasp face, two independent keyed locating features, anti-misassembly polarization, lead-in chamfers and positive retention mechanism. Choose pitch, exact ± tolerances and load paths in CAD after vibration/thermal creep study; **no universal fixed 25-mm grid for all voltage classes**. Allow rework without breaking adjacent healthy modules.

**T4-IF-002 — Three interface classes:**

- **L0:** low-energy sensor/data/cooling accessory—keyed removable only within an authorized isolated service boundary.
- **L1:** structural insulator/duct/coil former—robotic snap/slot **for alignment**, then qualified bolt, compression fixture, weld or encapsulation as needed; engagement proof by force/vision.
- **L2:** core/winding and high-energy dielectric connection—**factory-finished joints only** with specified contact area, torque/weld/braze resistance, insulation coordination, thermal/vibration/fault withstand. Never interpret "slots together" as unprotected live conductive plug contacts.

**T4-IF-003 — Dielectric:** Continuous rated barriers, creepage/clearance and radii designed from the highest local stresses, voltage class, pollution, liquid and thermal profile; interfaces must not create long-term trapped-air PD sites or capillary moisture paths. Two-layer interlocks do not compensate for poor bulk dielectric.

**T4-IF-004 — Magnetic:** Core packet alignment and compression maintain required flux path, lamination orientation, joint gaps, noise and mechanical clamping. Modular segments may increase no-load loss; require A/B core-loss measurement against uninterrupted control steel.

**T4-IF-005 — Fluids/thermal:** Seals, ducts and fluid-contacting polymers have explicit swelling, extracts, gas generation, aging and maintenance acceptance. No unjustified microchannels that clog or impair cooling under aging; compare conventional paper/pressboard, wood and tested polymer references.

**T4-IF-006 — Traceable identity:** Each part is marked (external barcode/etched/optional RFID) with serial, CAD revision, feedstock lot(s), source waste origin, cure/heat-history batch, test record, installation location and independent release signature. No item moves to high-voltage assembly without validated acceptance record.

## 4. Acoustic + DISH precision material-forming cell (AHD-C01)

### 4.1 Hardware (laboratory **starting architecture**, not purchased turnkey specification)

- **Material streams:** two independently dosed, filtered and measured feedstock cartridges with cleanable delivery and return loops; resin reuse allowed only after spectroscopy/viscosity/contamination check.
- **Containment:** closed transparent resin vessel or microfluidic window; assess **supported stationary-basin** as baseline. **Levitated droplets** are a separate small-part experimental variant; not required for large-scale transformer manufacturing.
- **Acoustics:** independently phased, calibrated ultrasound array with **64 controlled channels** as an initial engineering candidate (e.g., **8×8**, not the legacy contradictory “16×16, 64 elements”); investigate frequency across 0.1–4 MHz depending on resin, particle radius and attenuation, not one guaranteed 4-MHz recipe; measure sound speed, pressure, standing-wave map and acoustic streaming. Multi-wall array optional after simulation.
- **Optics:** reimplement the actual Nature DISH **405 nm coherent source, DMD, rotating periscope and optimized multi-angle exposures** where licensing allows; published DMD pattern rates up to 17,000/s, up to 10 rotations/s, ~19 µm overall feature resolution across ~1 cm; 0.6 s optical exposure only **for compatible mm-scale specimens**, never treat as actual factory cycle time.
- **Measurement:** dual-angle cameras, optional OCT/confocal/fluorescent imaging, photodiode dosimetry, hydrophones/acoustic pingers, viscosity and temperature, IR, post-cure micro-CT coupon sampling. Conductor and ceramic inclusions may require X-ray microscopy ex situ.
- **Safety:** fail-safe laser gate + independent chamber and acoustic overpressure controls, extraction for resin chemicals, enclosure door interlock, reactive materials handling, emergency stop, optical stray-beam limits, pressure/temperature cutoffs, and manual rearm after faults. Safety PLC separate from GRACE/AI planner; no model-overridden interlocks.

### 4.2 Experimental process sequence

1. **Specify part**: voltage/fluid/thermal qualification class; multimaterial voxel map; target particle type/region; acoustic field simulation and optical attenuation simulation; data provenance.
2. **Prepare A/B**: certify upcycled feedstocks and binder; record rheology, refractive index, particle size distribution, conductivity, density and 405-nm effective attenuation.
3. **Dose sequentially**: position A, then B at bounded concentration, or suspend B selectively in A; use different acoustic contrast and/or staged dosing for segregation. Do **not** presume arbitrary dense mixtures spontaneously split into predefined regions.
4. **Acoustic phase**: ramp fields; hold for a measured stable material-position state (not merely electronics phase lock). Candidate dwell sweep 0 / 2 / 10 / 30 / 60 s; compare no acoustics and pretreatment and concurrent-acoustics conditions.
5. **Close-loop verification**: reconstruct 3D particle field and confidence interval; measure optical penetration. Hard-stop if target morphology unattained, bubbly, unstable, or optically inaccessible.
6. **DISH lock**: timed angle-resolved exposure only after hardware interlocks and measured optical/acoustic go/no-go, optimize dose against scattering and initiator kinetics. Dynamic acoustic field during exposure is experimental and must be compared with field-off after shape lock.
7. **Recover**: separate uncured resin, clean, postcure (if chemically needed), inspect dimensions, pores, filler distribution and surface; contamination-controlled rework/scrap loop.
8. **Qualify**: machine test coupons from same lot; destructive dielectric, thermal, immersion and mechanical samples; release only by independently configured acceptance gates.

### 4.3 Physical unknowns and necessary modeling

- Acoustic manipulation acts on **particles/interfaces through radiation forces and streaming** and is not a general-purpose bulk-solid-mass mold. Force scales with particle size, acoustic contrast and field gradients; hydrodynamics and sedimentation compete.
- For a uniform pressure node/antinode design, a *mixed* formulation may co-cluster; distinct materials may not separate. Program time-staged dosing or differential acoustic contrast and verify actual segmentation.
- Metal and dense ceramic powder strongly scatter/absorb 405-nm light, reducing curing depth. Measure Beer–Lambert effective optical depth \alpha before claiming sub-second cure; where no sufficient transmission, print open lattices/scaffolds or use alternate postprocess.
- Optically cured polymer loaded with metallic powder remains polymer composite, **not bulk copper conductor or grain-oriented silicon steel**. To make an electrical pathway, prove resistivity, contact stability, current density and heat generation under service conditions; metallic paste sintering requires separate engineered process.
- DISH's ~1 cm depth limit means **tile and join**, not magical meter-scale cure. Every join must survive thermal/fault/aging loads.

### 4.4 Experimental matrix and criteria

| Variant | Acoustic | Material | DISH | Priority metric |
|---|---|---|---|---|
| C0 baseline | OFF | A transparent qualified-like control resin | ON | Cure/dimensional baseline |
| C1 | Pretreatment | A + trace nonconductive B | ON | Particle positioning and optical depth |
| C2 | During cure | A + B | ON | Net precision vs C1 and cavitation |
| C3 | Sequential A then B | Differing contrast | ON | Interface leakage/mixing |
| C4 | Droplet levitation | A + B | ON | Unsupported small-shape geometry |
| C5 | High filler fraction | A + dielectric B | ON or alternative cure | Optical feasibility cutoff |

**AHD-C01 proposed advancement gates:** >95% of independently mapped target A/B spatial occupancy in a simple geometry (research target, based on validated imaging, **not a published capability**); matched-control no extra trapped voids; printed optical feature accuracy and cured dimensions meeting drawing; zero uncontrolled shorts; dielectric and fluid-aging noninferiority versus matched commercially qualified reference; repeat across ≥3 material lots, ≥3 production days and independently validated operators. Reject candidate if material/electrical performance fails even if the shape looks correct.

## 5. Transformer 4.0 complete module library

| ID | Module / fixture | Fabrication | Installation | Nonnegotiable tests |
|---|---|---|---|---|
| T4-M01 | Core leg/yoke packets | Metal slit/laser cut + anneal + rated coatings; scrap re-refined to certified electrical steel | Robot stack and clamp | B-H, no-load watts, gap, noise, short-circuit forces |
| T4-M02 | Primary winding packet | Recycled-grade conductor winding/foil forming + verified insulation | Robot onto bobbin/core fixture; factory terminal joins | DC R, dielectric, impulse, thermal, joint R |
| T4-M03 | Secondary winding packet | As M02, relevant conductor cross-section | Robotic positioning, controlled isolation and leads | AC losses, fault forces, hotspot, joints |
| T4-M04 | Dielectric spacer tiles | AHD-D1 where proven; fallback approved conventional forming | Keyed auto insertion | PD, breakdown, creep, oil/ester aging |
| T4-M05 | Cooling/flow insert | AHD-D2 or conventional | Robot slot in oil/ester winding package | Flow, blockage, aging, extractables, heating |
| T4-M06 | Sensor carrier | AHD-D3 where optically feasible | Snap only at low energy isolated points | Hermeticity, accuracy, EMI, useful life |
| T4-M07 | Tank/radiator | Recycled certified steel/aluminum pressed/welded | Robot seam welding, leak testing | Pressure/leak, corrosion, thermal, grounding |
| T4-M08 | HV terminals/bushings | Qualified purchased or certified specialized manufacturing | Torque/vision controlled installation | Dielectric, BIL, impulse, leak, tracking |
| T4-M09 | LV terminals/connection bus | Formed conductive metal + rated dielectric | Robot weld/braze/bolt to approved drawing | Joint resistance, heating, fault |
| T4-M10 | Fluid and seal kit | Qualified fluid, gaskets/seals | Dry/degas/fill/close through clean system | Water, particles, dielectric fluid, leak |
| T4-M11 | Mounting/guard | Recycled structural metal/polymer | Robotic bolt/torque | Mechanical/static/vibration/environment |
| T4-M12 | Controller/telemetry | Purchased qualified electronic kit + recycled shell | Plug in only isolated signal compartment | Cybersecurity, EMC, environment, offline-safe |
| T4-M13 | Optional active converter | SiC modules + cooling passives + control | Bolted replaceable cassette, *de-energized only* | All stage losses, EMI, faults, firmware safety |
| T4-M14 | Final product | Integrated modules | Robotic assembly; human hold-points | Full IEEE/DOE/utility factory acceptance |

**Proportion manufactured by DISH is unknown** and may be a small fraction of unit **mass** even if it meaningfully reduces component count, fixture count and labor. The heavy magnetic and conducting parts will dominate many transformers. Count **qualified materials by mass, part count, process-hours, defect rate and cost**, separately; avoid claiming 80–100% DISH by weight.

## 6. Robotic assembly architecture and sequence

**Cell R0—receipt/segregation:** recycled streams fingerprinted, chemically separated, contamination threshold lot acceptance, dual witness for electrical inputs; material route traceability.

**R1—metal core:** CNC/slitting, annealing, magnetic test, robot stack to design airgap, clamp, verify gap/profile and mass.

**R2—conductors:** automated winding/foil forming, controlled insulation application, in-process tension and resistance measurement, CT/vision on suspect voids, terminal weld/braze.

**R3—AHD microfactory:** parallel transparent-material DISH cells for qualified insulator/sensor/duct tiles, machine vision/GRACE quality monitor, destructive sample panel, separate reject recycle; **AI advises, quality sign-off is rule-based and human-auditable**.

**R4—coil/core integration:** keyed assembly fixtures, machine-verified engagement, compressed stack, assembled winding-to-core clearances, welded conductors, thermal path verification.

**R5—enclosure:** certified tank fabrication, grounding lugs, seals, bushings/terminals, fluid fill or dry-type potting process, full leak control. **No press-fit alone for high-energy contacts.**

**R6—EOL:** polarity/ratio, resistance, insulation power factor (if specified), induced/applied dielectric, impulse where required, excitation/no-load loss, load loss, impedance, temperature, PD and sound as applicable, short-circuit type design verification, fluid/water/particle tests, mechanical and safety release; run under applicable standards and design-lab oversight.

**R7—label/service:** serialized machine-readable digital twin and immutable BOM/recovered content proof, factory electrical test result, safety/certification evidence, spare part route, field manual and installation limits. Shipment requires independent release signature. Grid commissioning by qualified licensed personnel only.

Robots run 24/7 where industrial safety allows; crews work staggered **five-day/40-hour weeks**. For 60 human posts occupied continuously at a site, the arithmetic minimum is **252 FTE** at 40 h/wk (10,080 staffed hours / 40), and ≈**315 FTE** with a 1.25 relief factor—not 240 FTE across four crews. This is a workforce-scheduling sensitivity, not a fixed staffing proposal. Each multi-product county node should specialize by capability; do not assume every county performs full MV high-potential testing onsite.

## 7. Controls, manufacturing model and digital thread

- **Architect:** chooses certified part family, revisions, optical/acoustic inverse-solver targets and robot job recipes from a controlled library.
- **Physicist/digital twin:** electromagnetic finite element magnetics (loss and saturation), electrostatic insulation field/PD, thermal/CFD oil or air, structural/fault/short-circuit force, acoustic wave and slurry dynamics, optical wave/dose/cure chemistry. Require mesh independence, parameter ranges and documented calibration; software is not empirical validation.
- **GRACE/Critic:** camera and sensor diagnostics, yield, anomaly detection, failed mold/cure, feedstock cross-contamination, reconciliation. Model outputs tagged *observed, published, derived, assumed or speculative*.
- **Asha safety linter/hardware interlocks:** independently fail-safe industrial system. Never allow machine-learning confidence to bypass hardwired interlock, qualified production hold point, or human lockout/tagout.
- **HITL:** material substitutions, electrical core revisions, production-rule changes and shipment release require qualified humans; D-119 dual signature if required by project governance.
- **Common contract** per module: `module_id, physical_revision, certified_family, source_lot_a, source_lot_b, fraction_recovered, process_recipe_hash, acoustic_field_hash, exposure_hash, tensile/dielectric/PD_test_refs, electrical_design_refs, assembly_joint_ids, release_signatures, installed_serial`.
- **Supply chain:** recorded shortages, qualified dual-source suppliers, no arbitrary substitutions, true commercial RFQs with delivered-cost and proof-of-delivery.

## 8. Electrical design calculations and efficiency ledger

For passive transformers, foundational calculations include:

- **Voltage:** \(V_1/V_2 \approx N_1/N_2\) ideal turns relation, with actual regulation, winding impedance and taps accounted separately.
- **Sinusoidal EMF:** \(E_{\mathrm{rms}} \approx 4.44 f N A B_{\mathrm{max}}\) for the selected core geometry/material under sinusoidal flux; cannot use 60-Hz magnetic-loss coefficients for SST switching frequencies.
- **Copper loss:** \(P_{\mathrm{Cu}}=\sum I_{\mathrm{rms}}^2 R(T)\) including winding AC and joint effects as required.
- **Total passive loss:** \(P_{\mathrm{total}} = P_{\mathrm{no-load}}+P_{\mathrm{load}}(x,T)+P_{\mathrm{stray}}+P_{\mathrm{aux}}\) with no double-counted components; regulated efficiency at prescribed test load point.
- **SST stage efficiency:** \(\eta_{\mathrm{wall}}=\eta_{\mathrm{rectifier}}\eta_{\mathrm{DC/DC}}\eta_{\mathrm{inverter}}-\text{auxiliary-loss correction}\) only under consistent power/efficiency definitions. Validate each stage and converter cooling.
- **Reliability:** track MTBF/MTTR/warranty in life-cycle economics; no fictional 30-year experimental reliability demonstration.

**Mandatory comparative ledger:** A conventional certified transformer of the same kVA/voltage/phase/impedance/cooling and tested at same loading; T4-P conventional core with printed noncritical components; T4-P with qualified AHD insulating modules; T4-S where the extra conversion functions are actually needed. Analyze no-load/loaded kWh annually at measured load curves, outage effects, field maintenance, purchase plus install cost, embodied carbon and net recovered content.

## 9. Safety, regulation and qualification

- **2029 U.S. efficiency requirements:** DOE's **April 22, 2024 final rule** currently specifies compliance from **April 23, 2029**, with applicable class-level requirements; DOE opened a further RFI in June 2026. Recheck final regulation before launch. [DOE source](https://www.energy.gov/cmei/buildings/distribution-transformers).
- **Liquid transformers:** IEEE C57.12.00 requirements and **IEEE C57.12.90-2026** test code as applicable to equipment class; utility-specific ANSI/NEMA/IEEE accessories, clearances, BIL, short-circuit tests and environment. [IEEE source](https://standards.ieee.org/ieee/C57.12.90/10944/).
- **Dry-type:** IEEE C57.12.01 and **IEEE C57.12.91-2026** (applicability check), plus UL 1561 only when the product actually lies inside its scoped voltage/equipment class. **UL 1561 explicitly excludes many higher-voltage and liquid-filled transformer products.** [IEEE scope](https://ieeexplore.ieee.org/abstract/document/11711423) · [UL scope](https://www.shopulstandards.com/ProductDetail.aspx?productId=UL1561).
- **Fluids:** IEC 60296:2020 covers specified mineral insulating oils, including qualifying recycled oils; IEC 62770:2024 for specified natural esters where applicable; use fluid and transformer OEM test requirements, including contamination, moisture, gas generation and thermal aging. [IEC 60296](https://webstore.iec.ch/en/publication/61025).
- **Controls/industrial:** OSHA/machine safeguarding, laser safety, chemical hygiene, environmental disposal, electrical OSHA/NFPA/NEC, LOTO, correct local jurisdiction, industrial cybersecurity and supply chain security.
- **High-voltage prohibition:** No unsupervised energized assembly, connector exchange, or laboratory high-voltage demonstration; qualified test lab and trained personnel required.

## 10. Verification and evidence gates

| Gate | Required deliverable | Stop if |
|---|---|---|
| **G0 source audit** | Reconcile historic HTAM math and material physics; reproduce DISH baseline on **actual compatible resin** | Original contradictory spec used as hardware fact |
| **G1 two-material acoustic geometry** | Three-dimensional imaged A/B placement with 3 batch/3 day repeat and field-off controls | Co-clustering, drift, heating or voids uncontrolled |
| **G2 DISH optical locking** | Spatial cure/feature accuracy and real build cycle including recovery/postcure | Filled mixture optically opaque or undercured |
| **G3 dielectric coupon** | Noninferiority in aging, breakdown distribution, PD, dielectric loss, thermal and immersion vs certified reference | Any catastrophic dielectric or extraction failure |
| **G4 robot assembly** | Repeatable keyed placement, engagement proofs, measured qualified electrical joints, zero-misassembly fixtures | Contact resistance, creepage/clearance, airgap or vibration unqualified |
| **G5 1–5 kVA bench** | Complete equivalent-transformer loss, temperature, dielectric and fault-safety comparisons with conventional reference | No validated net performance/safety |
| **G6 25 kVA preproduction** | Signed OEM/utility design requirements, MV type testing, high-voltage lab approvals | No demonstrated DOE/utility compliance |
| **G7 factory repeatability** | 1/10/100/1000 accepted unit RFQ, yield/OEE bottleneck, per-unit and tooling CAPEX independent quotes | Manufacturing costs/exceptions exceed comparator without proven value |
| **G8 external qualification** | Independent NRTL/OEM/utility acceptance and safe field trials under approved supervision | Lab product called commercial/grid-approved |

## 11. Economics, throughput and factory BOM/RFQ

**Every vendor quote** shall cover 1 / 10 / 100 / 1,000 units and annual capacity at candidate national scale. Quote **base conventional**, **AHD hybrid**, **T4-P**, and **T4-S** in matched duty classes. Price and report:

- mass and certified source percentage of core alloy, Cu/Al, insulation, ceramic, oil/ester, tank, electronics, seals and packaging;
- separate $0 / gate-fee **incoming waste acquisition** from positive collection, washing, sorting, refining, chemical conversion, binder, energy, lab certification, rejects and waste-hazard liability;
- coil winding/metal finishing/annealing/bonding hours, DISH **true accepted parts per hour** after handling, assembly seconds, high-voltage test/minute bottleneck, staffing and annual maintenance;
- equipment purchase, support/consumables, protective infrastructure, ERP/MES + quality, calibration, training, factory safety, financing, insurance and depreciation;
- measured electrical losses and cost of lifetime energy, installed cost per **qualified kVA**, field-repair frequency and actual embodied carbon;
- revenue **only from orders**, savings **only from measured equivalent outcomes**. Local community dividend **only from auditable distributable surplus**, never from savings counted twice.

**Throughput equation** (each work cell): `qualified units/year = scheduled operating hours × OEE × first-pass yield / verified bottleneck machine-hours per attempted unit` (**yield must not already be embedded within OEE quality factor**). If OEE includes quality, use `hours × performance/availability × first-pass yield` to avoid double penalty. E.g., 8,760 h/year × 0.70 availability/performance × 0.90 first-pass yield = **5,518.8 qualified-equivalent hours/year**, before actual product takt; that's not 5,518 transformers without a full hour/unit production and test bottleneck. **0.6 s DISH exposure cannot determine transformer takt.**

**Candidate $ model:** `C_accepted = (annualized equipment+facility+lab+tooling+overhead + purchased qualified BOM + recovered-material refining + resin & consumables + utilities + labor + scrappage + testing + field-warranty allowance) / accepted qualified units`. Compare T4-P with a current commodity passive unit independently quoted, not the historical illustrative $5–8k SST speculation. A national county factory is a portfolio of standardized cells; do not assume all 3,144 sites each have molten steel foundries and certified MV labs.

## 12. Deltas from previous research, evidence reconciliation

| Earlier program artifact | Retained | Correction or updated implementation |
|---|---|---|
| **Everywhere Factory** | Recursive manufacturing node: local waste → qualified material → factory outputs and new spare components | No verified full self-replication. Motors, semiconductors, optics, precision bearings still may be purchased and source-country tracked. |
| **HTAM v1.1 March 29** | Acoustic patterning, programmable optical locking, dual-modality sensors, resonance-first laser gate, safety philosophy | 0.6 s DISH applies to limited transparent mm objects. Acrylic UV cure cannot directly convert hot HDPE/PET/ABS melt; acoustic force not a general bulk mold. Original “melt 250°C + UV cure” line is unvalidated chemically. |
| **April 1 consolidated HTAM module** | Acoustic field modeling, 2-stage waste-to-feedstock, proposed array, GRACE defect AI, reusable print cells | Historical **16×16 grid / 64 elements** contradiction corrected; exact array frequencies/power/tolerances only experimentally tuned. Its < $180k/cell, <120 s print and competitive-cooling claims are **targets**, not verified. |
| **Transformer 3.0 Oct 31** | Recovered Cu/Al and Fe, SiC SST, additive cooling, modular electronics, 50 kVA 480→120/240 research RFQ | Keep as **T4-S**, not automatically the primary T4-P utility product. No validated 97% efficiency, BOM cost or 3D-printed conductive and magnetic circuit. |
| **ORCS grid standardization Oct 31** | DOE 80,000 utility variants and shared interface mandate, multiple kVA/voltage/phase product families | Standardize tested modules/accessories and procurement, NOT all utility service ratings into one universal unit. |

**No false validation:** prior multi-model statements (e.g., “council validated”) are editorial provenance, not accredited dielectric/life-cycle testing. HTAM/DISH + acoustics + transformer-grade two-material interfaces has **not yet been built and certified** in the researched sources.

## 13. Work packages, milestones and decision request

**WP01 — Source reconciliation:** reproduce original DISH and acoustic controls; spectroscopy of recovered polymer/ceramics; publish independent facts vs prior claims. Deliver two-supply recipes + error budgets.

**WP02 — 100-part AHD-D1 spacer run:** 100 physically printed, metrologically inspected parts (goal, not current result) with independent nonacoustic controls; three material lots and independently retained coupons; design-for-robotics features.

**WP03 — Qualified dielectric + fluid study:** retention after prescribed aging, electrical and mechanical tests; approve/reject resin/ceramic recipe before integration.

**WP04 — Low-voltage transformer demonstration:** two identical 1–5 kVA articles, one conventional insulation, one AHD printed modules; compare electromagnetic, thermal, dielectric and assembly time under controlled conditions.

**WP05 — 25 kVA utility reference:** engage accredited lab/OEM/utility, lock complete drawing/BOM, build manufacturing-only prototype (not field install), type-test to agreed standard.

**WP06 — Factory automated pilot:** parallel AHD stations and metal/winding cells, robotic assembly, qualification lab, real 1/10/100/1,000 unit cost quotes, live waste feedstock receipts and yields. Field deployment only after required approval.

**Immediate proposed decision:** Accept **T4-P25-L** as main utility reference, **T4-S50** as R&D branch, and **AHD-D1 dielectric spacer** as first two-material DISH/acoustic part. A complete modular transformer must *not* be gated on achieving a physically implausible one-shot all-material DISH print.

## 14. Source and provenance register

**Recovered existing owner program**
1. [Atlas Lattice HTAM v1.1 — March 29, 2026](https://github.com/atlaslattice/atlas-lattice-foundation/blob/main/docs/Holographic_Trashium_Acoustic_Spec_v1.0.md).
2. [HTAM System Architecture](https://github.com/atlaslattice/atlas-lattice-foundation/blob/main/docs/HTAM_System_Architecture_v1.0.md).
3. [Consolidated volumetric acoustic printing module — April 1, 2026](https://github.com/atlaslattice/atlas-lattice-foundation/blob/main/spec_modules/18_volumetric_acoustic_printing_spec.md).
4. [ORCS Transformer 3.0 — October 31, 2026](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/main/research/orcs/manufacturing/TRANSFORMER_3_0_FULLY_ADDITIVE_SIC_SST_RFQ_COST_GATES_2026-10-31.md).
5. [ORCS national standardized grid manufacturing — October 31, 2026](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/main/research/orcs/grid-intelligence-v0_1/FIVE_YEAR_STANDARDIZATION_TRAINING_AND_POWER_CONDITIONING_2026-10-31.md).

**Independent scientific and normative anchors**
6. Wang et al., [Nature (2026), DISH](https://www.nature.com/articles/s41586-026-10114-5). Optical process only; not metal-core evidence.
7. Agrawal et al., [Advanced Materials (2024), SonoPrint](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202408374). Particle-acoustic plus volumetric resin patterning and strength comparison, not certified transformer insulation.
8. [3D printing on levitated droplets (2025)](https://www.sciencedirect.com/science/article/pii/S2950431725000164). Small-object multimaterial feasibility, not high-voltage equipment.
9. [US DOE distribution transformer standards](https://www.energy.gov/cmei/buildings/distribution-transformers). 2029 rule effective 2024, further 2026 RFI.
10. [DOE: Over 80,000 distribution transformer variants](https://www.energy.gov/oe/supply-chain-and-market-analysis).
11. [IEEE C57.12.90-2026 active standard](https://standards.ieee.org/ieee/C57.12.90/10944/) and [IEEE C57.12.91-2026 dry-type standard](https://ieeexplore.ieee.org/abstract/document/11711423).
12. [UL 1561 scope limitations](https://www.shopulstandards.com/ProductDetail.aspx?productId=UL1561).
13. [IEC 60296:2020 recycled and unused mineral transformer oils](https://webstore.iec.ch/en/publication/61025).

**Evidence grades:** `RECOVERED_SOURCE`, `PUBLISHED`, `DERIVED`, `PROPOSED`, `UNVERIFIED`, `GATE_PASSED` (only with a retained lab report). Avoid expressing aspirational equipment and throughput as demonstrated.

---

**Disposition:** Proposal drafted for owner review. Existing GitHub source documents were read but **not overwritten or amended** by this local specification. All product ratings, dimensions, feedstock recipes, quote values, throughput and field service practices require engineering design and independent utility acceptance before use.