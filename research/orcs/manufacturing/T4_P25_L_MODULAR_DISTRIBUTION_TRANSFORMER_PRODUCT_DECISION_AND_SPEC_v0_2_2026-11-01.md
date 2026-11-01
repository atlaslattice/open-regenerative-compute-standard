# ORCS Transformer 4.0 — T4-P25-L Modular Distribution Transformer
## Product decision, bounded supplier dialogue and test specification · v0.2 · 2026-11-01

**Status:** **SUPPLIER-DIALOGUE-READY / CONCEPT DESIGN / UNPROTOTYPED / UNCERTIFIED / UNFUNDED.** Not a certified commercial product, formal build-to-print RFQ, vendor quote, utility-approved design, project procurement award or claim that AHD-D1 meets electrical standards.

**Scope boundary:** This file describes the **near-term passive** 25 kVA liquid-immersed product and its first differentiating component, the two-material acoustically patterned/DISH-cured **AHD-D1 dielectric spacer**. The 50 kVA SiC SST is **a different product**: [T4-S50 separate specification](T4_S50_SIC_SOLID_STATE_TRANSFORMER_ADVANCED_BRANCH_v0_2_2026-11-01.md). Shared production concepts, evidence ladder and cost-model definitions are in the [AHD/DISH common manufacturing appendix](T4_COMMON_AHD_DISH_DUAL_MATERIAL_ROBOTIC_PLATFORM_AND_COST_MODEL_v0_2_2026-11-01.md). This reorganizes but does **not erase** [the original broad v0.1 research program](TRANSFORMER_4_0_AHD_DISH_MODULAR_ROBOTIC_SPEC_v0_1_2026-11-01.md).

# ONE-PAGE PRODUCT DECISION SUMMARY

| Question | Decision or explicit unknown |
|---|---|
| **What are we selling first?** | Proposed **T4-P25-L**, single-phase 25 kVA, 60 Hz, overhead, liquid-immersed distribution transformer; 7.62 kV line-neutral on 13.2 kV grounded-wye nominal primary, 120/240 V center-tapped secondary. The utility/OEM must approve all ratings, taps, insulation/impulse class, impedance, fuse/surge protection, mechanical design and purchase conditions. |
| **Why would a buyer care?** | Potentially fewer custom insulating pieces, faster robotic placement, better provenance/repairability and a modular catalog. These are **hypotheses**, not demonstrated savings, electrical superiority or market demand. |
| **What is the first fabricated item?** | **AHD-D1-SP01**, a preliminary **8 × 8 × 4 mm** two-feedstock dielectric spacer/geometry coupon; **100 inspected candidate pieces** across controlled batches, with matched conventional and DISH-only references and separate destructive test coupons. Geometry is a proposed lab datum, **not a final transformer component drawing**. |
| **What is the first decisive gate?** | **G3: independently evaluated dielectric/thermal/fluid-aging noninferiority** to a qualified reference. G0–G2 (source/physical process proof) precede G3. A G3 failure kills the **AHD route into critical insulation**; it does not kill the conventional modular-transformer program. |
| **What is the first economic question?** | Can AHD-D1 deliver an accepted, tested part at a rational premium to an equivalent conventional part? A transparent **illustrative** 100-attempt model is **$43.13/AHD accepted part vs $14.74/conventional accepted part**; **+$28.39 premium**, **2.93×**. Neither is a vendor price or empirical performance. Full assumptions below. |
| **Who must act next?** | One transformer OEM/utility design authority; one university/accredited high-voltage lab; one DISH/acoustic research team; at least two independent prototype-part fabricators. Request **indicative pricing and lead times only** for a 100-part research batch and a conventional-insulation **1–5 kVA bench reference**. |
| **Why not a factory-wide RFQ?** | No locked transformer drawing, no qualified photocurable dielectric recipe, no successful AHD-D1 sample, no utility approval, no certified test report and no realized production takt. A full-product fixed-price quotation would be misleading. |
| **Go/no-go** | Proceed to 1–5 kVA paired experimental assemblies only after G3 plus part-handling/fit checks; only pursue a 25 kVA medium-voltage engineering article after the OEM/utility freezes its actual requirements. No grid deployment until all mandatory independent approvals. |

## 1. Product boundary and owner requirements

### 1.1 Proposed reference nameplate — not yet design-locked

| Parameter | Reference proposal | Open design control |
|---|---|---|
| Product identifier | T4-P25-L | Revision and country-of-origin BOM required |
| Power class | 25 kVA continuous | Actual load/ambient/temperature-rise conditions |
| Phase/frequency | Single-phase / 60 Hz | Utility service specification |
| HV | 7.62 kV line-neutral, reference 13.2 kV grounded-wye source | Correct feeder nominal, permissible taps, isolation and BIL |
| LV | 120/240 V split-phase | Neutral bonding, terminal ratings, regulation |
| Mounting | Pole/overhead | Bracket, center of gravity, service clearances and environmental exposure |
| Insulation and cooling | Liquid-immersed mineral oil **or** qualified ester variant | No fluid interchange without all-material aging test |
| Core | Qualified GOES/amorphous lamination packets | B-H, measured no-load losses, core joints, short-circuit forces |
| Conductors | Qualified refined copper or aluminum | Actual winding resistance, joints, flux geometry, class, winding constraints |
| Dielectric insert | Conventional certified part **baseline**; AHD-D1 **experimental substitution only** | Positioning, wall stress, PD, creepage/clearance, aging |
| Electrical losses | Equipment-class-specific DOE compliance at required test load | Full electrical testing; no invented universal efficiency % |
| Optional data | Noncritical monitored temperature/asset status, separated from HV | Offline-safe; no control authority or exposed sensor HV hazard |

Checks, **not winding designs**: at 25 kVA, 7.62 kV input ≈3.28 A nominal and 240 V output ≈104.17 A nominal. Core design needs measured flux, lamination steel, voltage taps, thermal margin and qualified fault withstand; simple nameplate arithmetic does not constitute electrical engineering.

**Compatibility:** The T4-P25-L is **not** electrically interchangeable with a 480 V-input SST, a padmounted three-phase transformer, a dry-type transformer or any medium-voltage unit with different taps, impedances, surge protection, BIL or fault duty.

### 1.2 What is actually modular

- **M01 core**: qualified cut/stacked GOES or amorphous-metal lamination packet with controlled mechanical datum and clamp; no claim of polymer-printed magnetic steel.
- **M02/M03 windings**: automated or semi-automated conductor winding/foil manufacture with certified winding insulation and factory-joined terminals; no claim of DISH printing bulk copper.
- **M04 insert**: AHD-D1 dielectric spacer/guide once proven, else legacy approved spacer/pressboard. AHD-D1 is a **drop-in design candidate**, not approved interchange.
- **M05 cooling insert**: conventional qualified oil-flow guide initially; AHD-D2 contingent on later testing.
- **M06–M12**: sensor carrier, certified tank/radiator, external bushings, LV terminals, fluid/seals, mounting/guards and optional isolated telemetry.

Interfaces: **L0** low-energy sensor/accessory (per permitted isolation policy), **L1** structural/insulating mechanical keyed locating features plus qualified retention, **L2** all power conductors/magnetic/high-field dielectric interfaces with certified factory permanent or specified service joints, inspection and HV test. **No energized hot-swapping.** Snap/slot is a positioning technique, never the sole justification for a live high-voltage joint.

## 2. First component — AHD-D1-SP01

**Objective:** Produce measurable, distinguishable two-material micropatterned dielectric spacers; demonstrate a controlled physical improvement (if any) over controls **and** no deterioration in safety-critical dielectric performance.

**Preliminary geometric lab coupon:** 8.0 mm × 8.0 mm × 4.0 mm envelope, target ±0.10 mm final dimensions; uncomplicated rounded-edge rectangular body with a deliberately measurable spatial filler pattern. Do **not** claim this coupon is appropriate for a particular transformer location; final shape, dimensions, creepage and stress concentration can be established only by an OEM electrical/materials design and CAD package. Surface-quality and porosity acceptance require measurement methods and numeric limits agreed before the trial; reject loose, undocumented visual-only acceptance.

**Materials A/B and controls:**
- **A**: optically compatible 405-nm-curable insulating formulation, potentially chemically recycled-derived if the chemistry and purification are verifiable. Virgin certified-like development resin allowed in G0–G2; *do not* relabel it recovered.
- **B**: measured, electrically insulating silica/alumina/glass-ceramic particle grade with full particle-size, density, impurities, optical attenuation and acoustic contrast controls. Recycled source only when chemically qualified and source/lot traceable.
- **C0**: transparent DISH-only A, no B and no acoustics; **C1**: DISH-only A+B; **C2**: A+B acoustically positioned before cure; **C3**: A+B with acoustic field active during cure; **C4**: conventional molded/machined/reference part. Equal nominal geometry, cure, aging and sampling matrix wherever scientifically comparable.
- No assumption that metallic/opaque filler is compatible with volumetric optical cure. If optics fail, abort or switch to a separate candidate manufacturing method; do not silently claim DISH.

**First production run target:** 100 dimensionally inspected AHD parts (e.g., 3 lots over ≥3 days where batch planning permits), plus *additional* retained destructive/aging coupons. **100 acceptable finished parts** is not equal to 100 attempted; count both. Monitor first-pass acceptance and all reject reasons. Blind lab assessor to fabrication arm where feasible; randomize sample order.

**DISH/acoustic:** 405 nm DISH-compatible light field, independently phased acoustic transducers and transparent vessel; primary controlled geometry first, levitation as separate exploratory variant. Image actual filler map before cure, and after cure with microscopy or micro-CT; electronics phase stability alone does not prove material position.

**Mechanical fit:** datum A/B/C, keyed robot-safe grasp, positive retention and dimensional record after cure/aging. The printed spacer is not a completed high-voltage component until installed stress/aging is proven.

## 3. Qualification / decision gate

**G0 source and materials** — Reproduce DISH baseline on its published compatible resin, prove two-stream material metrology, reconcile prior contradictory HTAM array figures and photochemistry; record optical dose and particle loading.

**G1 acoustic positioning** — Reproducible target separation or geometric localization with measured 3D map and no-acoustic control. Must rule out co-clustering, hidden bubbles and uncontrolled acoustic heating.

**G2 optical cure** — Actual cured 3D structural integrity, transparency/attenuation, postcure and dimensional statistics; report *accepted parts/hour* inclusive of handling instead of copying the Nature 0.6-second exposure number.

**G3 decisive dielectric noninferiority** — A qualified independent test authority pre-registers appropriate methods and margins for breakdown voltage **distribution** (Weibull or justified equivalent), partial discharge **in the actual test geometry**, insulation resistance, dielectric loss, accelerated thermal aging and oil/ester fluid aging (extractables, moisture, gassing, dimensional swelling, cracks and mechanical retention). The conventional part/coupon must be a physically appropriate qualified reference. An initial good-looking dielectric number is **not** 20–30 year field reliability. **Fail on catastrophic dielectric, contamination or aging behavior even if printed shape is perfect.**

**G4 assembly fit** — Robot alignment/interlock testing, locked-in torque/compression, vibration and disassembly only as authorized. Cannot substitute for G3.

**G5 1–5 kVA controlled bench** — Supervised low-voltage prototype with conventional insulation, followed by only a G3-passing AHD-substituted twin. Compare winding resistance, losses, temperature rise, noise and electrical safety under equivalent conditions.

**G6 25 kVA engineering article** — Freeze utility/OEM procurement specification; independently specify the 7.62 kV/120-240 V transformer and all requisite high-voltage insulation, surge protection and performance tests.

**G7 accepted-part economics + qualified factory rate** — Validated scrap, optical cycle including recovery, process bottlenecks, traceability, yield/OEE and warranty reserves.

**G8 external approval** — Applicable third-party/accredited tests and actual utility/OEM/NRTL requirements; no field deployment before approval.

**Parallel route allowed:** A conventional-insulation T4-P transformer can progress through OEM design and factory testing while AHD is held at G3. The experimental spacer must **not** be installed in energised utility equipment until approved.

## 4. Transparent 100-attempt cost-class screening — not a quote

**These numbers are explicit negotiating placeholders, NOT research-measured costs, supplier prices, credible market ranges, or actual production margin.** They are intentionally disputable to set the information needed for a first vendor call.

| Per attempted part or batch | AHD prototype (ASSUMED) | Conventional custom baseline (ASSUMED) |
|---|---:|---:|
| Consumables/material per attempt | $1.00 | $1.00 |
| Machine/process time | 0.15 h at $70/h = $10.50 | 0.08 h at $50/h = $4.00 |
| Handling/prep | $3.00 | $2.00 |
| Routine inspection | $5.00 | $3.00 |
| One-batch fixed setup | $1,500 for 100 attempts = $15.00/attempt | $400 for 100 = $4.00/attempt |
| Assumed first-pass yield | 80% | 95% |
| **Total per 100 attempted** | **$3,450** | **$1,400** |
| **Expected accepted quantity** | **80** | **95** |
| **Cost per accepted piece** | **$43.13** | **$14.74** |
| **Nominal precision premium** | **+$28.39/AHD accepted piece** | Baseline |

Formula: \`C_accepted = (N_attempt*(material + process + handling + inspection) + setup + allocated calibration, if any) / (N_attempt*FPY)\`; material/processing entries above assume **all attempts** incur their stated process costs. Rounding after division. This screening excludes **full development CAPEX, professional CAD, independent destructive dielectric qualification, long-term aging, facility overhead not in rates, licensing, warranty, insurance and certification**. Neither option's fixture/geometry has a real supplier quote. Avoid inventing a universal 'market price' for spacers.

**Economics decision:** Under these deliberately unfavorable prototype assumptions, AHD requires roughly **2.93× per accepted part**. To win, demonstrate **fewer required pieces, lower assembly/test hours, superior validated dielectric service performance or a credible scaled unit-cost reduction**. For example, if one AHD part replaces three conventional parts, benchmark total *installed, qualified* system cost, **including joint risk and failure warranty**, not nominal part price alone. Do not assume this benefit exists.

**Sensitivity requirements:** Recompute per accepted part using actual equipment quote, setup, average machine-hour and accepted yield from at least 3 lots. Quote 100/1,000/10,000 parts as **indicative supplier dialogue**, with separate nonrecurring engineering (NRE) and type-testing. If acoustic patterning adds no verified advantage, prefer simple molding or established 3D printing.

## 5. Bounded initial supplier enquiry — what can actually be priced

**Enquiry A: 100 candidate spacers, laboratory-only.** Ask for material-compatibility assessment, sample CAD feasibility, high-level 405 nm attenuation limit, two-feedstock handling, three-batch opportunity, dimensional/particle imaging, finish, expected reject rates, postcure safety, NRE and setup hours, provisional accepted-unit price, safety controls, and lead-time **range**. Mark **INDICATIVE / R&D** and request a list of missing finalized drawings before any binding quotation. No HV claim.

**Enquiry B: 1–5 kVA conventional-insulation bench comparator.** Ask a qualified transformer lab/OEM for an independently safe low-voltage design, selected nameplate and test plan, two matched assemblies, BOM and lead-time estimate, instrumental monitoring and labor. **Do not ask them to quote a nonexistent completed AHD transformer.**

**Enquiry C: utility/OEM design consultation.** Ask what geometry, BIL, insulation fluid and test methods a spacer would need to be evaluated as a candidate for a real 25 kVA distribution transformer; collect commercially important common-voltage and size combinations from *actual customer demand*.

**Documentation before binding RFQ:** frozen CAD and drawings, tolerances, material standards, statistical acceptance plan, tests and responsibility matrix, service conditions, legal/insurance boundaries, rights to supplied data, factory quality plan, approval path and detailed quantity schedule. Without these, supplier dialogues are not fabrication orders.

## 6. Manufacturing and robotic assembly — limited to this product

Plant sequence: incoming certified steel, copper/aluminum, resin/ceramic and purchased accessories → independent magnetic-core and winding modules → AHD-D1 validated lab cell (or conventional approved insulator) → keyed robotic physical assembly → rated winding joints and insulation → sealed tank/radiator, bushings, grounding, fluids → approved factory high-voltage testing → serialized release. Safety PLC and independent human authority interlock all critical operations; **no live energized manipulation of primary HV connections**.

Record per-device metal, recycled content, insulating-lot IDs, leakage, dielectric tests, losses, certified first-pass yield, OEE **without double counting quality**, direct factory cost, inspection cost and life-cycle energy. To compute US-wide demand, query utility procurement **actual unit volumes by configuration**, not just count combinatorial possible variants.

## 7. Standards and external evidence

**Regulation is already adopted:** the April 22, 2024 DOE **final rule** established equipment-class standards with compliance required **April 23, 2029**. A **June 2026 request for information** solicited feedback and **does not itself vacate or replace the 2024 final rule**. Recheck any formally published later amendment before quoting an approved product:
- DOE/Federal Register 2024 final: https://www.govinfo.gov/app/details/FR-2024-04-22/2024-07480
- DOE June 2026 RFI: https://content.govdelivery.com/accounts/USEERE/bulletins/41b58d7

**Liquid-immersed transformer standards:** IEEE C57.12.00-2021 general requirements and currently active IEEE C57.12.90-2026 test code, subject to exact equipment class and further utility requirements:
- https://standards.ieee.org/ieee/C57.12.00/6962/
- https://standards.ieee.org/ieee/C57.12.90/10944/

**80,000 variants scope:** DOE reports >80,000 possible combinations/varieties, including requirements resulting from many attributes and accessories. **This is not a census of equally demanded sold SKUs**. DeepSeek's proposed 'top five to ten cover most sales' is a plausible **concentration hypothesis**, **not established by the cited DOE statistic**. Obtain aggregate utility/OEM order frequency distribution and calculate top-N share before making a quantified standardization promise.
- DOE supply-chain: https://stage.energy.gov/oe/supply-chain-and-market-analysis
- DOE 2026 industry webinar transcript: https://www.energy.gov/sites/default/files/2026-03/Distribution-Transformer-Convening-Webinar-Transcript.pdf

**Scientific guardrails:** original DISH demonstrated millimeter-scale photocurable printing with approximately 0.6 s exposure, not commercial oil/ester-safe dielectric resin nor transformer parts: https://www.nature.com/articles/s41586-026-10114-5 . Work on FFF polymer compatibility illustrates the existence of material/immersion research, but **PPSU/PEEK/ULTEM compatibility cannot be transferred to a different DISH-curable resin**: https://link.springer.com/article/10.1007/s40964-024-00614-z .

## 8. Evidence / release status

- **RECOVERED_SOURCE:** earlier owner specifications and HTAM hardware architecture.
- **PUBLISHED:** DOE regulations, IEEE standard scopes, DISH optical demonstration, cited dielectric literature.
- **DERIVED:** nameplate current estimates and the arithmetic in the scenario table.
- **ASSUMED/PROPOSED:** specific prototype geometry, component material pairing, 100-unit run, batch yields, rates, economics and production roadmap.
- **UNVERIFIED:** complete AHD-D1 electrical noninferiority, real robot cycle, commercial demand concentration, component cost advantage.
- **GATE_PASSED:** none for T4-P25-L or AHD-D1 as of this version.

**Decision requested:** authorize **research scoping and supplier dialogue**, **not utility procurement**. Proceed sequentially from a real 100-part AHD sample and matched conventional comparator to an evidence-based G3 decision, then a supervised bench transformer, then a separately qualified 25 kVA product.
