# ORCS Transformer 4.0 — T4-S50 SiC Solid-State Transformer (Advanced Branch)
## Independently scoped R&D product specification · v0.2 · 2026-11-01
> **November 1, 2026 v0.3 application split:** The v0.2 **single-phase 480 VAC → 120/240 VAC** design remains this advanced industrial AC research branch. For the distinct AI data-center **three-phase 480 VAC → 800 VDC, 50 kW power tile**, OCP standards crosswalk, 5+1 synthetic 250 kW rack, explicit AFE/DAB/matrix/partial-power alternatives and assumption-only $16k–$70k per-tile cost class, use the [new T4-S50-DC v0.3 application-specific spec](T4_S50_DC_800V_AI_FACTORY_SST_RETROFIT_AND_TOPOLOGY_SPEC_v0_3_2026-11-01.md). OCP's 5–10 MW MV input specification is a **different product class**; neither branch is a qualified product or commercial RFQ.

**Status:** ADVANCED R&D / SYSTEM-ARCHITECTURE AND SUPPLIER-DIALOGUE-READY ONLY / UNBUILT / UNVALIDATED / UNCERTIFIED / UNFUNDED. **Not a utility distribution transformer replacement**, not a commercially validated data-center product, not an assertion of 97% measured efficiency. The candidate is not ready for a binding production RFQ.

**Document split:** The **near-term distribution-transformer product** is [T4-P25-L](T4_P25_L_MODULAR_DISTRIBUTION_TRANSFORMER_PRODUCT_DECISION_AND_SPEC_v0_2_2026-11-01.md). Shared acoustic/DISH/manufacturing architecture is [the common platform appendix](T4_COMMON_AHD_DISH_DUAL_MATERIAL_ROBOTIC_PLATFORM_AND_COST_MODEL_v0_2_2026-11-01.md). Preserve [Transformer 3.0 historical source](TRANSFORMER_3_0_FULLY_ADDITIVE_SIC_SST_RFQ_COST_GATES_2026-10-31.md) and [Transformer 4.0 v0.1 integrated research program](TRANSFORMER_4_0_AHD_DISH_MODULAR_ROBOTIC_SPEC_v0_1_2026-11-01.md).

# Product decision summary

| Item | Specific bounded decision |
|---|---|
| **Who is this for?** | Prospective industrial, microgrid, data-center **auxiliary/edge loads** requiring active conversion/regulation, power quality or AC/DC interfaces **where functions are worth their cost**. It is not presumed to serve a standard medium-voltage utility feeder or the main high-voltage data-center electrical distribution. |
| **Prototype target** | 50 kVA continuous **reference objective**, single-phase **480 V AC input → 120/240 V AC split-phase output**, 60 Hz, 3-stage AC/DC → isolated high-frequency DC/DC → AC inverter candidate, with alternatives to be studied. |
| **Proposed differentiator** | Keyed **de-energized replaceable** SiC electronics and control/cooling subassemblies, efficient high-frequency magnetic modules, independent testing, optional acoustically patterned/DISH insulation **only if qualified**. |
| **What is real?** | Published electronics/components and conventional machining/winding; not a fully printed 50 kVA SST, not a completed field unit. Texas Instruments TIDA-011012 is a **different-voltage, three-phase reference design**, not a ready-made 480 V/120-240 V product. |
| **First decision gate** | Written system function/value case: compared against equivalent conventional transformer **plus actual necessary inverter/UPS/conditioning stages**, can this architecture win on full-chain energy, availability, cost and protection? Without such a case, **stop the SST product** and use conventional transformers. |
| **First supplier dialogue** | Indicative prices/specifications for commercially available SiC modules, magnetic-core materials, isolated gate drivers, DC-link capacitors, thermal hardware and qualified electromagnetic/EMI testing. No full SST unit quote or promised launch date. |
| **Relationship to AHD-D1** | **Optional R&D transfer after G3**. Neither SiC topology nor its revenue case is gated on experimental DISH spacer development; standard insulation remains baseline. |

## 1. Functional engineering envelope

| Requirement | Starting objective | Pass criterion / uncertainty |
|---|---|---|
| Apparent power | 50 kVA continuously | Thermal/electrical qualification across real duty cycle |
| Input | 480 V RMS single-phase nominal 60 Hz | Decide tolerance, line sag, fault, surge and source impedance before topology freeze |
| Output | 120/240 V split phase 60 Hz | Nominal 240 V 208.33 A at 50 kVA PF=1; neutral/load imbalance requirements TBD |
| Nominal input current | ~104.17 A at 480 V, ignoring losses | Actual current higher with conversion loss and power factor |
| Whole-system efficiency | ≥97% **proposed owner goal** | Measured inclusive of controls, drivers, auxiliary pumps/fans, switching and all stages at **specified load points** |
| Output regulation | ±1% proposed | Test across specified loads, load steps and grid conditions |
| Output THD | <3% proposed | Define load/measurement method; no universal claim of applicability |
| Electrical isolation | Galvanic isolation by qualified HF transformer | Actual creepage, clearances, barriers, impulse, PD and fault withholding |
| Power direction | Initial one-way; bidirectional **separate option** | Not implied by SiC devices; requires independently designed controls and protection |
| Cooling | Modular metal spreaders, heat sinks, approved air/liquid interface | Heat-flux, leak, overtemp and serviceability qualification |
| Controller | DSP/MCU protection and deterministic interlocks | Independent hardware overcurrent, overtemp, disconnect, precharge and anti-restart |
| EMI, harmonics, grid interaction | Must be designed and tested | Exact standard and service interconnection class by product compliance engineer |
| Mechanical | Keyed cassette, controlled heat-sink contact | **No energized field swap**; discharge/LOTO/prove-dead protocol |
| Warranty/lifetime | Unknown | Capacitor, thermal cycling, magnetics, power module, fans, service availability and duty |

**Architecture is not final:** 3-stage rectifier → isolated DC/DC → inverter is one feasible category. Compare a single isolated direct converter, a partial-power conditioner, modular UPS/active filter or passive transformer + existing electronics. Switching frequency, bus voltage, SiC device ratings, HF topology and insulation system are **engineering trade studies**; no copied schematic is suitable for production without requalification.

## 2. Electrical and life-cycle economics

For idealized 50 kW real output at PF=1 (only a comparison point):

- At **97% end-to-end efficiency**, estimated input power = 50/0.97 = **51.546 kW**, total loss ≈ **1.546 kW**.
- At **99% end-to-end efficiency**, estimated input power = 50/0.99 = **50.505 kW**, total loss ≈ **0.505 kW**.
- Difference ≈ **1.041 kW** continuously. At 8,760 hours and 100% illustrative load factor this corresponds to **~9.12 MWh/year** of *extra input energy* in the 97%-versus-99% **end-to-end-equivalent** comparison, before demand charges, cooling energy, actual variable-load efficiency and required power conditioning benefits.

**This comparison is a warning, not a claim that every passive unit has exactly 99% efficiency**. An SST can make sense when it replaces existing lossy conversion stages, supports valued fast voltage regulation or enables necessary AC/DC and bidirectional functions. Compare the actual chain **passive transformer + all necessary converters** vs **SST chain serving the identical output service**. Do not compare the SST's 97% to one passive component's efficiency if auxiliary conversion has been omitted on one side.

A product P&L requires validated semiconductor BOM cost, magnetic core losses at real *switching* frequency and flux density (not 60-Hz coefficients), measured electrical thermal rise, reliability/spares, grid interaction, production yield, warranty, service and system operational value.

## 3. Subsystem manufacturing breakdown

| System | Preferred build route | Two-material modular role | Limit |
|---|---|---|---|
| S01 SiC switching module | Qualified purchased modules, thermal packaging and robot assembly | Semiconductor + isolated substrate/cooling interface | No DISH printing of SiC dies |
| S02 HF magnetics | Suitable ferrite/nanocrystalline/amorphous/Fe-Si based on frequency-loss trade | Certified core material + insulation; separate manufacturing line | Do not transplant mains-frequency GOES claims to HF core |
| S03 Primary/secondary HF winding | Precision copper/litz/foil automated winding | Refined Cu/Al + verified dielectric film/coating | Skin/proximity losses and high-frequency insulation govern |
| S04 DC link/filter | Commercial rated capacitors, snubbers and magnetics | Replaceable qualified passive assemblies | Capacitor aging/ripple; not laser-printed |
| S05 Cooling | Certified Al/Cu thermal spreader and cooling manifold | Metal A + suitable coating/barrier B | Fluid leaks, isolation, pump failure, corrosion |
| S06 D1 dielectric holders | Conventional insulators initially; AHD-D1 **after independent G3** | Qualified photopolymer + nonconductive ceramic filler | Optical attenuation, PD, thermal class, aging |
| S07 Controller/telemetry | Commercial DSP/MCU/gate drivers/isolation and deterministic firmware | Sensor carrier from qualified modular material | Human-authorized; non-override safety |
| S08 Housing/shield | Certified enclosure/metal barrier, polymer panel where safe | Metal + rated coating, or polymer + filler | EMI, bonding, touch safety, environmental exposure |
| S09 Protection | Rated breaker/fuses, surge, protective relays, disconnects | Purchased independently qualified safety components | Protection never replaced by a software promise |

**L0/L1/L2 interfaces:** L0 low-energy isolated data/auxiliaries; L1 structural mounts and dielectric alignment; L2 high-energy electrical, magnetic and dielectric interfaces, fixed at factory under engineering controls. Cassette modules only replaced **after shutdown, discharge verification and lockout/tagout**.

## 4. Proof sequence and deliverables

**S0 — Customer functional RFQ / no product claim:** Obtain one authentic industrial/edge microgrid load case with voltage, power quality, availability, DC interfaces, existing equipment, measured loss curves and annual economics. A general reference to data centers is not a validated customer.

**S1 — Baseline alternatives:** Price and engineer passive transformer + existing converter, UPS/active power quality and medium-voltage equipment if applicable. Identify incremental features and full system duty.

**S2 — Safe low-energy stages:** Simulation and low-energy hardware emulation for each converter stage, controller and isolation; demonstrate faults, PWM, EMI strategy and deterministic interlocks under qualified lab oversight.

**S3 — Selected topology and thermal mock-up:** Device stress, short circuit, overvoltage, magnetic-core-loss map, switching thermal model, dielectric test plan, heatsink/pump tests, root-cause instrumentation.

**S4 — Power-stage qualified laboratory prototype:** Rigorous protective enclosure, appropriate site/technician safety, qualification of each stage before integration at rated voltage/power. No presumption that full 50 kVA may be safely energized in a general makerspace.

**S5 — Full-chain measured comparison:** Power analyzer records 10–100% load curve, idle/standby, switching and transformer losses, THD, fault clearing, thermal, acoustic, EMI and dynamic response. Equivalent-output, equivalent-function comparator.

**S6 — Hardware service validation:** Cycle stress and maintainability; keyed cassette fit, isolation/grounding, safe discharge, parts availability and digital traceability; report failure/repair rates with proper confidence intervals.

**S7 — Independent certification pathway and pilot:** Compliance engineers determine product-category standards and grid interconnection requirements. Obtain external reviews/approvals and controlled customer trial; no field sales or unattended deployment before acceptance.

**AHD/DISH transfer:** Test a separate coupon/cassette family only after dielectric G3 for its **own frequency, peak stress, temperature and fluids**. Passing 60-Hz mineral-oil requirements does not automatically qualify a high-frequency SiC insulation system.

## 5. Supplier dialogue package — limited to measurable items

Send to at least two independent electronics/magnetics suppliers:
- permitted SiC module ratings/availability/lead times **for a TBD architecture**, isolated gate drivers, DC-link capacitor specs and costs at 1/10/100 indicative quantities;
- magnetic core candidates with **frequency-dependent core-loss curves** and availability, wire/foil insulation, machining/stacking labor and thermal interface data;
- closed-loop cooling interface and environmental qualification scope;
- test-house availability and indicative charges for EMI, fault, dielectric, temperature-rise, short-circuit and operational safety reviews;
- licensing/IP boundaries and documentation deliverables.

**Do not request a fixed-price 50 kVA system quotation** until topology, drawings, safety case, load function, BOM and test conditions exist. Keep NRE separate from recurring BOM and warranty. Show explicit high/low uncertainty and vendor-controlled performance.

## 6. External source and regulatory guardrails

- Original owner program: [Transformer 3.0 SiC SST research / RFQ cost gates](TRANSFORMER_3_0_FULLY_ADDITIVE_SIC_SST_RFQ_COST_GATES_2026-10-31.md)
- TI TIDA-011012 reference, **not** 480 V single-phase product: https://www.ti.com/tool/TIDA-011012
- Actual DISH paper (mm-scale optical cure, not photonic manufacture of SiC/copper): https://www.nature.com/articles/s41586-026-10114-5
- IEEE and other required electronic product standards vary by installation type; do not claim automatic qualification by UL 1561, IEC 60076, IEEE C57.12.90 or a utility standard that does not actually cover the final assembled **power-conversion system**.
- DOE 2029 passive distribution-transformer rule may not apply to a particular SST design as presumed; get an **explicit regulatory applicability finding** for each equipment class before quoting standards compliance.
- None of the owner-proposed 97% efficiency, cost, service life or volumetric manufacturing claims has a verified test report in these source docs.

## 7. Independent branch decision

Proceed only if a real customer functionality case and a measured architecture comparison justify **why active conversion is needed**. Treat **T4-P25-L** as the first utility transformer program, and **T4-S50** as a distinct advanced industrial converter program with its own economics, test lab, safety/legal classification and readiness level. Retain modular acoustic/DISH components solely where they can be **independently qualified**, not as a prerequisite for the entire SST.
