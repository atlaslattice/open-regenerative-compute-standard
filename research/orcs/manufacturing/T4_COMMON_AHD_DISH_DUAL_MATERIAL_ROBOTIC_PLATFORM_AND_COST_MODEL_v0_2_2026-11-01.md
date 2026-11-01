# ORCS Transformer 4.0 — Common AHD/DISH Dual-Material Manufacturing Platform
## Shared engineering appendix, cost model, evidence rules and factory interfaces · v0.2 · 2026-11-01

**Status:** SHARED RESEARCH MODULE / SUPPLIER-DIALOGUE-READY SUBCOMPONENT CONCEPT / NOT A MANUFACTURED, CERTIFIED OR COMMERCIAL TURNKEY FACTORY. No vendor quotes or accredited dielectric results have been obtained.

**Child product decisions:**
- **First near-term utility product:** [T4-P25-L Modular 25 kVA Distribution Transformer](T4_P25_L_MODULAR_DISTRIBUTION_TRANSFORMER_PRODUCT_DECISION_AND_SPEC_v0_2_2026-11-01.md)
- **Separate R&D advanced branch:** [T4-S50 SiC SST for industrial and edge power conversion](T4_S50_SIC_SOLID_STATE_TRANSFORMER_ADVANCED_BRANCH_v0_2_2026-11-01.md)
- **Historical consolidated baseline (preserved):** [Transformer 4.0 v0.1 integrated research program](TRANSFORMER_4_0_AHD_DISH_MODULAR_ROBOTIC_SPEC_v0_1_2026-11-01.md)
- **Original parent manufacturing system:** [March 2026 HTAM](https://github.com/atlaslattice/atlas-lattice-foundation/blob/main/docs/Holographic_Trashium_Acoustic_Spec_v1.0.md); [April 2026 consolidated HTAM module](https://github.com/atlaslattice/atlas-lattice-foundation/blob/main/spec_modules/18_volumetric_acoustic_printing_spec.md)

> **Sound positions. Light locks. Robots assemble. Certified conductors carry.**

## A. Scope and physical constraints

The Everywhere Factory / HTAM concept couples **acoustic particle organization** with **DISH-type volumetric optical photopolymerization** to produce **small, geometrically complex candidate composite components**, with automated transfer to industrial assembly. Two independent feedstock cartridges per *material-forming cell* enable A/B dosing or staged layering. They do **not** make a whole transformer out of just two elements.

**Observed versus extrapolated:**
- **PUBLISHED:** DISH demonstrated 0.6-second curing of **millimeter-scale** compatible optical resin structures, roughly 19 µm stable printing resolution, 405 nm laser/light-field control in a 1 cm range; 0.6 s is exposure-only, not an industrial cell time. Source: https://www.nature.com/articles/s41586-026-10114-5
- **PUBLISHED:** Research exists on acoustic particle structuring within volumetric/polymer additive methods and on different polymer dielectric compatibility in transformer environments; **that is not a demonstrated combined commercial process**.
- **RECOVERED_SOURCE, NOT INDEPENDENTLY VERIFIED:** Earlier HTAM design gave <120-second production, ~$180k cell cost and rapid direct curing of recycled HDPE/PET/ABS melt; these are **targets/historical assertions**, not manufacturing achievements. Hot thermoplastic cannot generally be 405 nm light cured without a new chemically active formulation.
- **NOT CURRENTLY DEMONSTRATED:** arbitrary two-material separation in a dense opaque mixture, all-metal DISH copper windings or grain-oriented steel cores, meter-scale complete transformer cure, oil-immersed high-voltage-qualified DISH photopolymers, field-reliable self-assembling medium-voltage connections or end-to-end qualified multi-cell factory.

### One manufacturing principle, several distinct production cells

| Cell | Stream A | Stream B | Physics | Producible candidate |
|---|---|---|---|---|
| AHD-D1 | Verifiably recycled-derived 405-nm-curable insulating polymer **if achieved** | Certified nonconductive silica/alumina/glass filler | Independently phased ultrasound + patterned optical cure | Small spacers, holders, bobbin guides |
| AHD-D2 | Photocurable dielectric polymer | Thermally conductive **electrically insulating** recovered ceramic | Acoustic orientation + optical or alternate curing | Fluid guides and thermal inserts |
| AHD-D3 | Transparent insulating resin | Qualified glass/polymer reinforcement | Optical/DISH and limited acoustic field | Noncritical sensor shells |
| C1 | Qualified recovered copper/aluminum | Rated dielectric film/layer | CNC/forming/automated winding/foil process | High-current windings |
| M1 | Qualified electrical steel/amorphous alloy | Interlaminar dielectric | Slitting/annealing/stacking with robot clamps | 60-Hz core packets |
| H1 | Qualified steel/aluminum | Certified corrosion/insulation barrier | Sheet forming, welding, machining, coating | Tank/heat exchanger/mounting |
| E1 | Certified recycled thermoplastic | Nonconductive mechanical filler | Injection/large-format extrusion/hybrid tooling | Secondary casing/sensor cover |

No unqualified raw waste enters a safety-critical insulation part. A $0 waste purchase scenario may still incur collection, sorting, washing, chemical treatment, binder, power, qualification, rejects and disposal. No unsupported claims of full import independence.

## B. AHD-C01 laboratory cell — candidate hardware / not a finalized BOM

**Acoustic:** initial **64 independently controlled channels** (e.g. 8×8), with frequency sweeps from approximately 0.1–4 MHz **according to measured acoustic contrast, propagation and viscosity**. This corrects the legacy '16×16 / 64 elements' arithmetic error, and does not claim 8×8 is optimal. Acoustic stabilization must measure *actual 3D particle distribution*, not just electronic phase alignment.

**DISH:** start by reproducing the primary Nature **405 nm laser, digital micromirror device, rotating periscope, model-based multi-angle light-field optimization**, with enclosure, optics calibration and appropriate rights. No guarantee the two-feedstock slurry transmits light sufficiently. Flow-supported resin basin baseline; levitated droplet or free-form suspended multi-material geometries are *separate experiments*, not necessary for first product.

**Two material streams:** metered A/B reservoir, filtrations, defined mixing/staged dosing, independent mass/flow meters, particle-size and refractive-index controls, temperature/viscosity, quantitative source/impurity logs; reclaim unused resin only after qualification.

**Sensing:** 3D optical or fluorescence/micro-CT position map, acoustic hydrophones, thermometry and attenuation measurement, UV irradiance and photochemical dose tracking, end-of-cycle dimensional metrology, QC tags.

**Interlocks:** independent safety PLC, chamber door UV laser gate, optical hazard control, acoustic overpressure shutoff, chemical ventilation, E-stop, temperature and electrical interlocks; no software-agent override. Laser curing gated until stable target *material* field and measured acceptable attenuation, not an arbitrarily inherited numeric opacity threshold.

**Control formulation:** optimize both ultrasound actuator complex amplitudes and DISH light-field exposures against target two-material 3D distribution, observed particle trajectories, scattering and cure dose. Keep separate uncertainty bounds for positional error, acoustic heating, field collapse, cure shrinkage, absorption and suspended-particle sedimentation. G0 control = optically cured resin with **no acoustic activation**.

**No unproven 100% sorting assertion:** particles with similar acoustic contrast can occupy the same nodes. Staged dosing, carrier-media choice and validated imaging remain required. If particles scatter light, return to transparent matrix/control or a different technology. No cure means no release.

## C. Shared mechanical, electrical and digital interfaces

- **L0 — low-energy/signal/service:** mechanically keyed and service-documented only under applicable isolation, grounding and personnel controls.
- **L1 — structural/insulation/duct:** datum A/B/C, positive grasp locations, robot orientation feature, insertion lead-in, independent retention, geometry and joint aging tests.
- **L2 — high-energy/core-winding/dielectric:** robot locator only, then engineered permanent or rated mechanical/electrical connection, required creepage and clearances, inspected contact resistance, impulse/PD design and fault withstand. **No energized hot-swap of power connections**.
- Module BOM includes all constituent materials, serial, lot, recovered-source documentation, resin optical/thermal process, test status, final assembler release, service location, approved installation rules and rejection/rework history.
- Electric-field edge rounding, pressure-sensitive cracks, trapped air bubbles and oil-capillary moisture paths are independent dielectric risk modes; good ±0.1 mm dimensions do **not** prove low PD.
- Magnetic joins/stacking must be compared to uninterrupted reference lamination for increased air-gap and no-load loss.
- Cooling/fluid inserts require leak, swelling, gassing, dielectric fluid cleanliness and blockage tests.

## D. Cost-class model and reproducible arithmetic

**The following is an internally assumed cost-class example, not vendor research, a supplier quote, procurement price or an observed discount.** It is intended to force the first economic decision into a testable conversation. The selected geometric prototype is **8×8×4 mm AHD-D1-SP01**, not necessarily the field part.

### D1 illustrative 100 *attempts* (not 100 accepted)

| Input | AHD prototype | Conventional custom control |
|---|---:|---:|
| Material/consumables per attempted piece | $1.00 | $1.00 |
| Machine/process time and rate | 0.15 h × $70 = $10.50 | 0.08 h × $50 = $4.00 |
| Handling/prep per attempt | $3.00 | $2.00 |
| Routine inspection per attempt | $5.00 | $3.00 |
| Batch setup for 100 attempted | $1,500 | $400 |
| Yield of accepted pieces | 80% assumed | 95% assumed |
| Variable per attempt before fixed setup | $19.50 | $10.00 |
| Total 100-attempt batch | $3,450 | $1,400 |
| Expected accepted pieces | 80 | 95 |
| **Cost per accepted piece** | **$43.125 → $43.13** | **$14.73684 → $14.74** |
| **AHD premium** | **+$28.39/accepted part** | **2.93× accepted unit cost** |

Direct formula:

\`batch_cost = attempts*(material + machine_hours*machine_rate + handling + inspection) + fixed_setup\`

\`accepted_count = attempts * measured_first_pass_yield\`

\`accepted_part_cost = batch_cost/accepted_count\`

The difference is positive *against AHD* in this placeholder. At an identical required component count, AHD has **no demonstrated savings**; the hypothesis is that a precision two-material design could eliminate other parts, reduce assembly minutes, improve test yield or change service economics. These benefits must be proven through measured **installed and electrically accepted device cost**, not asserted from printing speed or superior looking micrographs.

**Sensitivity:** Use independent vendor rates for machine/hour, automatic handling minutes, three-lot yield, optical rework, secondary postcure, process downtime, material provenance and independent test. Report costs at **1 / 10 / 100 / 1,000 accepted pieces**, a separately clearly stated amount for setup/NRE, and 10,000 if the supplier can credibly quote capacity. Do not translate 0.6 s DISH optical exposure to 0.6 s complete qualified part or factory. No valid data exist yet for one $X–$Y empirical AHD price range.

**Exclusions that require separate budget:** experimental print-head capital, optical safety fit-out, resin chemistry/R&D, high-voltage laboratory tests, aging, accreditation/certification, equipment depreciation outside stated machine rates, utility design consulting, engineering CAD, warranty/field liability, building/land/financing, and end-of-life disposal. Do not double count later additions.

**Decision test:** If a $43.13 printed part replaces 3 conventional parts at $14.74 each, raw pieces alone total $43.13 vs $44.22; **potential gross delta ≈ $1.08**, *only if geometries and qualification are interchangeable and installation labor and safety test remain comparable*. More compelling savings would need actual assembly savings, fewer failure modes or scaled yield. If acoustic alignment demonstrates no physical or electric advantage, drop the acoustic step from the first production path and keep the broader HTAM research as a parallel experiment.

### NRE and first pilot budget bookkeeping

Budget categories for vendor request, **NO MONEY COMMITTED**: CAD and tooling; resin/powder synthesis and cleanliness; acoustic and optical system rentals/commissioning; 100 candidate parts + destructively tested controls; third-party dielectric/PD/fluid-aging lab; conventional low-voltage bench transformer; robotic fixture and independent industrial-safety review. The historic <$180k HTAM printer and <120 s print figures are explicitly **unverified** and must not become a purchase ceiling or Gantt baseline without quotes.

## E. Factory routing and parallel specialization

County/regional industrial sites can specialize in **AHD resin/ceramic precision cells**, **qualified magnetic-core processing**, **automated conductor winding**, **sheet-metal fabrication**, **final assembly** and **accredited high-voltage testing**. The cost model must compare a networked supply chain against complete vertical integration instead of claiming all ~3,144 county-equivalent nodes have high-potential labs or magnetic-metallurgy capability.

**R0:** certified incoming metal and resin streams → **R1:** metal slit, stamp, anneal and robot stack → **R2:** certified winding/insulation/termination → **R3:** optional AHD acoustic/optical pilot → **R4:** robot keyed mechanical alignment, inspected retention and rated joints → **R5:** enclosure/cooling/fluid/seals → **R6:** independent electrical/thermal/quality hold and acceptance → **R7:** serialized shipment, warranty and field-service records. Purchased critical semiconductor/safety hardware remains separate.

Machine-hours: \`qualified output = available machine hours * performance fraction * yield / cycle hours per attempted item\`. If **OEE already includes quality**, do **not** multiply by separate quality yield again. At 8,760 possible annual machine-hours, an *assumed* 70% availability/performance and 90% first-pass yield gives 5,518.8 equivalent accepted processing-hours *before* dividing by measured cycle time; not 5,519 transformers.

For hypothetical 60 human posts occupied 24/7, 60×168/40 = **252 FTE** mathematical minimum before time off; ×1.25 relief factor gives **315 FTE**. Four 60-person ×40-hour crews provide only 9,600 h vs 10,080 h required. This is a personnel-planning sensitivity, not a site headcount decision.

## F. Standardized catalog concentration — hypothesis not verified sales claim

DOE identified roughly **80,000 possible transformer configurations** across attributes and legacy utility specifications. That number does **not** mean 80,000 equally purchased commercial SKUs. DOE's March 2026 webinar explicitly discusses the combinations of attributes. **Do not repeat 'top 5–10 configurations cover most sold units' as verified**, because the DOE source does not provide supporting purchase-frequency data.

**Required Pareto study:** acquire actual year-specific order counts, dollar volume and customer/region/voltage/phase/unit-kVA segmentation from willing utilities and OEMs, deduplicate custom accessories and group core design-equivalent builds. Publish top-5/top-10/top-20 share **with geography, confidence and exceptions**, then select the demand-weighted modular catalog. Standardization must preserve utility safety approvals and local installation needs, not create a blanket one-rating product.

Sources:
- https://stage.energy.gov/oe/supply-chain-and-market-analysis
- https://www.energy.gov/sites/default/files/2026-03/Distribution-Transformer-Convening-Webinar-Transcript.pdf

## G. Compliance gates and deliverables

- **April 2024 DOE final rule** (distribution-transformer class-specific energy conservation) effective as issued, with **April 23, 2029** compliance date. **June 2026 RFI** asked for information; absent a later final amendment, an RFI does **not** postpone an adopted obligation. https://www.govinfo.gov/app/details/FR-2024-04-22/2024-07480 and https://content.govdelivery.com/accounts/USEERE/bulletins/41b58d7
- **Passive liquid transformers**: relevant IEEE C57.12.00-2021 requirements and C57.12.90-2026 test code, plus purchasing-utility and installation requirements. https://standards.ieee.org/ieee/C57.12.00/6962/ and https://standards.ieee.org/ieee/C57.12.90/10944/
- **SST and converter-specific** grid/product safety and EMI requirements must be separately selected by an appropriately qualified compliance engineer, not inferred automatically from passive transformer standards.
- **Stage evidence:** RECOVERED_SOURCE → PUBLISHED → DERIVED → ASSUMED/PROPOSED → SOURCE_REPRODUCED → TESTED → INDEPENDENTLY VALIDATED → PRODUCT QUALIFIED. Label all assumptions and independent outcomes by actual record. Multi-model textual agreement is **not** prototype or accredited material validation.
- **No bypass:** any failed safety-critical dielectric, thermal or fault test stops insertion of candidate AHD modules into energised devices. An alternate conventional material route can continue independently.

## H. Immediate supplier dialogue requests and success criteria

1. AHD material/optics facility: can it **print** a reproducible 8×8×4 mm A/B pattern in 100 inspected parts at measured cost, yield and postcure quality? Provide sample coupons and lot records.
2. Conventional molding/machining shop: what is equivalent part cost, tolerance and lead time at identical geometry, including tool setup?
3. Independent HV materials lab: what tests and physically meaningful, pre-registered noninferiority margins would establish G3 before selecting an actual transformer insulation application?
4. Transformer OEM and customer utility: what relevant part geometry, voltage stress, required dielectric design, oil/ester compatibility, product variants and utility selection data must be specified before any field component is permitted?
5. Robotic integrator: what datum/fixture and torque/force inspection architecture is appropriate for mechanically slotting and permanently securing insulation, core and winding assemblies?

**First acceptance criterion:** 100 accepted parts plus honest total attempted, real run costs, actual mapped spatial material separation, matched controls and independent G3 test report. **A failure is a useful result.** Preserve the broader Transformer 4.0 vision without calling a research cell commercial factory.

## Provenance

This v0.2 appendix and its child product specifications reflect the November 1 owner-directed acceptance of a DeepSeek critique of [the preserved v0.1 original](TRANSFORMER_4_0_AHD_DISH_MODULAR_ROBOTIC_SPEC_v0_1_2026-11-01.md). Corrections incorporated: supplier-dialogue label, product split, an explicit bottom-up **assumption-only** cost-class comparator, DOI/DOE primary-source verification, and a falsifiable first product decision. No lab data or external endorsement is claimed.


## November 1, 2026 — BattMan and battery R&D boundary (dated addendum)

[DOE's October 28 Battery Manufacturing Accelerator (BattMan) launch](https://www.energy.gov/cmei/ammto/articles/doe-launches-battery-manufacturing-accelerator-strengthen-us-competitiveness) names PNNL, Argonne, ORNL and the National Laboratory of the Rockies; program focus is AI-assisted manufacturing-process sensing, digital twins and closed-loop experimentation. **E1 program launch**, not an ORCS partnership or demonstration of AHD/DISH battery production.

**Separate experimental route BATT-AHD-01:** establish one transparent polymer/filler sample that can be manufactured by staged acoustics and photopolymerization; then only *if relevant electrochemical compatibility is independently established* investigate a real battery subpart. Controls: no acoustic vs acoustic-before-cure vs acoustic-during-cure; conventional cast/laminated control; measure particle concentration/geometry, UV cure completion, porosity, mechanical properties, bulk/interface electronic/ionic transport, electrolyte compatibility, thermal stability and cycling where applicable. Resistive printed photopolymer composites cannot be assumed to replace Cu/Al current collectors, active electrodes, separators or electrolyte. Reject on capacity fade, self-heating, contamination, dendrites or safety failure. Record direct process power, acoustic dwell and accepted unit cost; omit claimed Watt-hours and battery cycle life absent tests.

**Priority unchanged:** AHD-D1 dielectric spacer G3 first. Battery pathway is a non-blocking research watch. [All November 1 sources and next actions](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/main/research/ORCS_2026_11_01_CROSS_PROGRAM_NEWS_EVIDENCE_AND_IMPLEMENTATION_REGISTER.md).
