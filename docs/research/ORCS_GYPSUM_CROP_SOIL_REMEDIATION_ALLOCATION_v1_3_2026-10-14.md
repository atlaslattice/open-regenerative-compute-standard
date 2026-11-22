# ORCS v1.3 — Gypsum: crop yield, soil remediation and competing sulfuric-acid uses

**2026-10-14 · ADDITIVE EVIDENCE UPDATE · NON-OPERATIONAL · ZERO REALIZED CREDIT**

## Research question
For each **assayed and agronomically qualified** tonne of recovered gypsum-equivalent calcium sulfate from desalination, what are the relative benefits of (A) soil amendment for a documented soil/crop need, (B) industrial sulfuric-acid route when verified economic and chemical feasibility exists, (C) industrial gypsum use, (D) accessible strategic reserve, vs (E) no recovery? Preserve the U.S. domestic supply → resilience → affordability → residual export evaluation policy hierarchy. No double-counting.

## Evidence: genuine but condition-dependent agronomic effects

**NRCS 2024 Conservation Practice Standard 333**, gypsum amendments, addresses improved infiltration, soil-aggregate stability, reduced phosphorus loss and subsoil aluminum toxicity, alongside calcium/sulfur agronomic value. **NRCS CPS 610** governs saline/sodic soil management. These are practice standards; state Field Office Technical Guides, laboratory soil testing and site-specific prescriptions are needed.
- https://www.nrcs.usda.gov/resources/guides-and-instructions/amending-soil-properties-with-gypsum-products-ac-333-conservation
- https://www.nrcs.usda.gov/resources/guides-and-instructions/saline-and-sodic-soil-management-ac-610-conservation-practice

**de Castro Pias et al., 2020**, Agronomy Journal meta-analysis (129 harvests, 930 observation pairs) in no-till acid soils: cereals (maize, wheat, oats, barley, rice) on soils with >5% Al saturation at 20–40 cm depth had 77–97% likelihood of positive grain-yield response; mean gains ~14% under water deficiency, ~7% without. Soybean under both water deficiency and >10% Al saturation had 88% likelihood of positive response, mean increase ~12%. **These are conditional study-group responses, not universal gains or projections for U.S. fields.**
- https://doi.org/10.1002/agj2.20125

**Kost et al., 2018**, Journal of Environmental Quality meta-analysis of 10 U.S. experimental sites shows **no significant overall mean crop-yield increase** from gypsum across the sampled treatments (mined gypsum ratio 0.987; FGD gypsum 1.00). Some sites benefit, others do not. Soil/plant nutrient and vadose water chemistry can change even without yield improvements.
- https://doi.org/10.2134/jeq2018.04.0163

**USDA ARS** explains calcium/sulfur contribution, infiltration and erosion improvements, dissolved P loss reduction, subsoil aluminum toxicity and pathogen transport effects:
- https://www.ars.usda.gov/research/publications/publication/?seqNo115=336218

## Provenance and environmental constraints
- Salt and trace contaminants in **marine brine precipitate** may differ substantially from mined and flue-gas-desulfurization gypsum. None of the studies establish that Harbor Island brine gypsum is automatically safe for application. It requires composition and contaminant assays, chloride washing, moisture/sulfate content, harmful trace metal testing, product designation, permitted agronomic use and responsible residual discharge assessment.
- Soil pH, sodium adsorption ratio (SAR)/exchangeable sodium percentage (ESP), drainage and leaching water availability, cation exchange, aluminum saturation, organic matter, sulfur sufficiency, field response and regional regulation must be measured.
- In saline-only soils, gypsum does not remove salt and can worsen salts without adequate drainage; in sodic soils replacing sodium is ineffective without leaching/drainage; for nutrient-replete soil crop yields may not respond. Overapplication can alter Mg/K balance, and additional sulfate leaching requires water-quality review.
- Gypsum supplies Ca and S; **not nitrogen, phosphorus or potassium**. It is a soil amendment/crop complement, not replacement for major macronutrients.
- Sometimes gypsum supports cover crops, diversified rotations and co-cultivation under stress by improving the soil environment, but no quantified companion-planting synergy is assumed without actual trials for named crop combinations. Research title “cohabitation” interpreted as applying gypsum within multi-crop agronomic systems, not as a separate established mechanism.

## Existing source ledgers (preserve)
- Harbor Island **proposed** desalination: prior upper-bound seawater composition gives **0.733 Mt/year gypsum-equivalent theoretical inventory**, NOT recovered certified agricultural gypsum.
- Dongjiakou modeled gypsum ceiling **62.7–76.9 kt/y per node**, not measured qualified plant output.
- Earlier Chinese sulfuric-acid project design comparison ~0.4 t acid/t gypsum feed **not actual conversion yield**; transforming gypsum to acid requires proven plant/energy/grade and environmental accounting.
- National comparison of 100 identical Harbor Island designs **73.3 Mt/y hypothetical gypsum inventory ceiling** only, not actual U.S. installed plants or usable amendment quantity.

## Ledger and allocation rules
Represent each field/project opportunity with: source gypsum batch_ID, dry-product mass and CaSO4·2H2O purity, available mass after processing, ion/contaminant assays and certification, regional soil category/crop/rotation, NRCS CPS applicability, farmer field-test yield response and uncertainty, crop price and yield, avoided fertilizer Ca/S expenditure, water/runoff and phosphorus impacts, sodium/Al or salinity changes, transport and application cost, environmental protections, regional emergency availability, industrial acid use qualification and price.

Track **same-batch exclusive allocation**: `agricultural_tonnes + acid_feed_tonnes + industrial_tonnes + reserve_tonnes <= qualified_available_tonnes`. Any feed assigned to acid cannot simultaneously increase field yields. For field-level scenarios, a yield improvement is contingent on validated condition and source-specific trial; do **not** multiply study percentage by national acreage indiscriminately.

## Practical next implementation
Import USDA NRCS soils (SSURGO/gSSURGO) and NASS planted acreage/crop patterns with region-specific data-access receipts; join NRCS 333/610 standards and USDA soil laboratory recommendations to land eligibility. Couple to documented mine/FGD/desal qualified gypsum availability and geographically reachable freight costs. In parallel maintain USGS/Census sulfur/acid import and fertilizer producer/reserve ledgers. Present Pareto tradeoff between agronomic outcomes and sulfuric-acid security before export candidacy. No invented farm results or realized mineral credits.
