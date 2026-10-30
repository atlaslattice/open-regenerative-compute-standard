# Beyond Q — Maintenance, Manufacturability & Local Replacement Ledger
**v0.1 · 2026-10-30 · Proposed 20-year testbed accounting schema**
**Provenance:** User's proposal for mature on-site 3D-printed manufacturing of tooling and modular spares; Copilot independent Oct 30 analysis of HTS, vendor dependencies and twenty-year whole-campus boundaries. Related: [full-stack campus mission](BQ_20_YEAR_FULL_STACK_AUTARKY_AND_SURPLUS_CAMPUS_GOAL_v0_1_2026-10-30.md) and [Moon/Mars testbed](BQ_MOON_MARS_CLOSED_LOOP_HABITAT_TESTBED_MISSION_AND_LEDGER_v0_1_2026-10-30.md).
## Core question
Can the campus keep its productive systems working under limited resupply, and which replacement items can be **actually qualified** for local manufacture rather than simply 3D printed?
## Proposed per-component ledger schema
`subsystem_id,component_id,component_description,manufacturer,material_grade,criticality,operating_environment,life_distribution,inspection_interval,MTTR,spare_stock,annual_quantity,supplier_count,supplier_geography,lead_time_days,imported_mass_kg,imported_embodied_energy_kWh,manufacturing_route,required_machine_tools,required_feedstock,feedstock_source,local_process_step,metrology_requirement,qualification_test,code_or_certification,local_replacement_lead_time,local_replacement_yield,repair_success_rate,local_cost,import_cost,unplanned_outage_effect,personnel_safety_effect,environmental_risk,habitat_transferability,evidence_status,source_uri`.
**Candidate sectors:** pumps, seals, bearings, impellers, filters, water-treatment housings, modular piping, fixtures, tools, containment, fermentation equipment, packaging, agricultural components, spare electrical enclosures and non-safety-critical structures. Nuclear, cryogenic, tritium/chemical containment and safety-critical replacements require independent qualifications; some parts need precision machining, heat treatment, alloy control and certified inspection, not additive manufacturing alone.
## Manufacturing decision paths
Import finished component; repair existing; remanufacture/recoat; local conventional machine; qualified additive manufacture + postprocess; redesign for substitute; multi-source and safety reserve. Score technical function and safety separately from economic return.
## Maturity ladder
Concept geometry → bench sample → verified materials → life-cycle test → component qualification → witnessed integration trial → approved use for specified operating envelope. No automatic promotion to safety-critical production.
## Nightmare Lab challenges
- Can a facility make the bearing but not the lubricant or metrology calibration standard?
- Does an onsite pump part depend on imported laser powder, power semiconductor, or oxygen?
- What happens if two identical locally printed parts fail from the same material defect?
- Can inspection catch dimensional faults and chemical incompatibility in seals and membranes?
- Are components repairable during 150-day isolation without vendor firmware/cloud license?
- Does printing one spare consume more scarce electrical energy than a safe stored imported spare?
## Tests and metrics
Internal replaceability %, qualified vs merely printable, average/95th percentile repair time, expected downtime, spare coverage under isolation, embodied inputs, imported tooling and feedstock, on-site production scrap, certification, total lifecycle cost, local product export after reserves.
## Evidence anchors
CFS / Fujikura Sept 30, 2026 HTS agreement https://www.fujikura.co.jp/en/news/pressrelease/20260930cfsarc1km.html ; Proxima / Kyoto Fusioneering Oct 28 2026 MOU https://www.proximafusion.com/press-news/proxima-fusion-kyoto-fusioneering-mou . These show industrial supply-chain focus, **not** on-site manufacture capability in Beyond Q.
**Invariant:** Reactor B stays 1.13 GW D-T fusion power, Reactor A stays hypothetical 20 MW primary D-D; these are research configurations, not proven hardware.
