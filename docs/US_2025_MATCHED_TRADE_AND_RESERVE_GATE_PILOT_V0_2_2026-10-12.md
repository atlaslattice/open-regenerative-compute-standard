# US 2025 matched import/export and reserve-first pilot — v0.2
**2026-10-12 | MEASURED FEDERAL FLOWS + DERIVED RATIOS + UNVERIFIED RESERVE SUFFICIENCY | zero realized import substitution or export restrictions.** Additive to v0.1; no overwrite.

## Case A: 2025 US DISTILLATE fuel (EIA; physical thousand barrels converted to million barrels)
| Metric | 2025 million bbl | Authoritative data |
|---|---:|---|
| Refinery/blender net production | 1,822.486 | https://www.eia.gov/dnav/pet/pet_pnp_refp_a_epd0_ypr_mbbl_a.htm |
| Imports | 57.989 | https://www.eia.gov/dnav/pet/pet_move_imp_a_epd0_im0_mbbl_a.htm |
| Exports | 456.168 | https://www.eia.gov/dnav/pet/PET_MOVE_EXP_A_EPD0_EEX_MBBL_A.htm |
| Product supplied (proxy for domestic demand) | 1,426.504 | https://www.eia.gov/dnav/pet/PET_CONS_PSUP_A_EPD0_VPP_MBBL_A.htm |
| East Coast imports | 45.424 | EIA imports by PADD link above |
| Gulf Coast exports | 411.180 | EIA exports by PADD link above |

Exports/imports = **7.866**. Exports / product supplied = **31.98%**. Net exports = **398.179 million bbl**. Refinery net production + imports − exports − product supplied = **−2.197 million barrels**. The residual is not evidence of data error: EIA comprehensive supply/disposition includes stock changes, blending adjustments and other components; do not force a simplistic identity to zero without the actual whole-system reconciliation. **National net exported barrels do NOT imply grade-matched regional reserves.** 2025 published year-end US distillate marketing stocks = **100.195 million barrels** (different accounting boundary and last-in-year stock, source https://www.eia.gov/dnav/pet/PET_SUM_MKT_A_EPD0_STR_MBBL_A.htm). This represents **~25.6 days** at annual average 2025 domestic product supplied ~3.908 million bbl/day, but this figure is NOT full working emergency coverage, not a strategic stockpile, not a proven shortage, and is not a valid PADD-level reserve target. Compare daily 2026 East Coast winter vulnerability separately. Other EIA weekly Oct 2, 2026 stocks ~105.1 million barrels national, reported Reuters https://www.reuters.com/business/energy/us-crude-stocks-distillate-inventories-fall-gasoline-inventories-rise-eia-says-2026-10-07/ ; not an emergency reserve in itself.

### Strict user-design surplus gate
Target: cover all US essential + commercial grade-specific seasonal demand, put resilient reserve in correct place, actual imports zero for relevant grade and horizon, then allow exports only from measured regional deliverable margin with human lawful authorization. **This is a proposed national policy and/or voluntary producer contract, not an existing law or authority held by this project.** Energy liquids are grade-, geography-, and time-specific. Inventory includes quality qualification, accessibility, capacity at ports/pipelines/trucks, demand spikes and replenishment time. Provisional **diesel gate = NOT VERIFIED / exports not authorized under synthetic proposed rule**, not a recommendation for immediate enforceable stop.

## Case B: strategic nonfuel MINERALS and old scrap (USGS MCS 2026)
USGS 2026 report https://pubs.usgs.gov/publication/mcs2026 and machine-readable 2026 statistical data release https://www.usgs.gov/data/mineral-commodity-summaries-2026-data-release (released September 18, 2026). The release contains production, imports, exports, stocks, consumption and net import reliance by commodity but values haven't yet been downloaded or normalized into a fully matched national mineral table.

**Cross-check already published in USGS MCS 2026 overview**: ~**$21 billion** old mineral scrap exports, **$8 billion** old scrap imports and **$45 billion** old scrap domestically recycled in 2025; approximate **net scrap export value ~$13 billion**, but this is NOT $13 billion of available refined domestic metal and dollar netting across unlike material forms is not a physical balance. USGS narrative contains one rounded inconsistency ($45 vs $46B domestic old scrap recycled in differently written summary paragraphs); use the explicit year-labelled source table and provenance for any strict accounting. High scrap-export-share categories: copper, silver, aluminum, chromium and titanium; priority audit is **exported scrap grade vs imported virgin/refined form**, not automatic scrap retention. New secondary copper smelter operated by 2025; others under construction do not count as current capacity.

Priority mineral rows pending 2025 data normalization: potash, copper, aluminum/bauxite, antimony, rare earths, graphite, fluorspar, nickel, tin, iron/ferroalloys, lithium/cobalt. **UNKNOWN != ZERO**.

## Case C: FOOD/AG trade (USDA ERS)
2025 US ag exports approx **$171B**, ag imports approx **$212B**. This is a nominal trade-value aggregate of non-fungible products and cannot become a physical commodity reserve gate. Need FATUS 2025 equivalent product/grade/country/mass and annual domestic availability and food inventories before output per commodity. Use https://www.ers.usda.gov/data-products/foreign-agricultural-trade-of-the-united-states-fatus/calendar-year and https://www.ers.usda.gov/data-products/ag-and-food-statistics-charting-the-essentials/agricultural-trade ; importer/exporter aggregates should be reconciled to product identity and period.

## Commodity-level data engineering contract
**Period:** annual 2025 = full year, 2026 monthly separate. **Flow:** US-origin exports separately from reexports, imports-for-consumption separately from general imports. **Granularity:** HTS10 imports, Schedule B exports matched carefully at HS6, then physical product/form/grade and unit. USITC 2025 complete records and June 20 2026 revisions: https://dataweb.usitc.gov/ . DataWeb API requires a Login.gov-linked account and API key (source https://www.usitc.gov/applications/dataweb/api/dataweb_query_api.html); public queries may be made manually without account https://www.usitc.gov/faq/question/how_do_i_use_sitequery_data.htm . Do not fabricate line-level downloads.

For each matching physically fungible commodity, reconcile:
`domestic_use = domestic_production + imports - exports - stock_build + stock_draw +/- adjustments`.
`reserve_gap = verified_reserve_target_by_grade_region − accessible_certified_inventories`.
`export_unlocked = actual_imports_zero AND current_domestic_demand_fully_met AND reserve_gap<=0 AND verified_dynamic_surplus>0 AND legal_human_authority`.
A zero-import gate is *user's deliberately strict proposed goal*, which may remain unattainable for geographically scarce grades; import diversity or cooperative trading may still reduce vulnerability. For demand shocks, use per-grade Monte Carlo/seasonal stress tests with explicit public assumptions.

## Economic and material recovery ranking
1. **Scrap vs imported refined metal:** copper and aluminum, magnet recycling, battery black mass. USGS ~$13B *net exported scrap value* is a directional screening marker only, NOT additional profit or import substitution; existing domestic recycling ~$45B cannot also be called new.
2. **Potash/soil nutrients:** manure, food waste, wastewater, processing residuals, source separated urine; subtract fertilizer nutrients already field-applied and prevent soil depletion.
3. **Sulfur/industrial acids/gypsum:** refinery offgas, FGD gypsum, spent acids. Purity permits and industrial energy needed; hazardous waste is not food-grade nutrient.
4. **Energy:** used cooking oil and separated food waste, landfill gas, sewage gas, refinery waste heat. Some streams are already valorized; avoid double counting RNG and its feedstock energy.
5. **Industrial water/thermal:** avoided domestic resource costs, not automatically customs import offsets; locate customers adjacent to source.

## Outcome
Pilot has a **real quantified matched 2025 distillate import/export/production/use** comparison and USGS **scrap value-flow opportunity screen**. It does **NOT** supply complete commodity-level matched 2025 USITC dataset or verified strategic reserve targets/holdings. Next iteration should ingest USGS 2026 CSV entries and USDA 2025 FATUS exports/imports; full USITC DataWeb HTS10 download needs user-available API key or public query exports. Maintain receipts and label unknown gates unknown.
