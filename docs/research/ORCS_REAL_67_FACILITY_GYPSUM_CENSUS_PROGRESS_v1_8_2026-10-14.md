# ORCS v1.8 — 100-facility census: first reproducible evidence tranche

**2026-10-14 | COMMITTED ACTUAL-NAME REGISTRY / NO FABRICATED SITES OR YIELDS / NON-DEPLOYABLE**

## Outcome
- **67 unique named plant/site records** committed to `data/desal_gypsum/orcs_named_facility_register_v1_8_2026-10-14.json`. Includes all **59 names** shown in the public Texas Water Development Board desalination plant database (two explicitly labeled idle) plus **8** additional real named facilities/projects from previous official-source registers across California, Florida, and Texas.
- **14 additional named federal feasibility-study projects** in `data/desal_gypsum/orcs_usbr_feasibility_projects_v1_8_2026-10-14.json`, *not counted as plant records*, because a listed study does not verify an existing physical desalination plant or distinct operating facility. Even if all 14 later qualify, those lead records cannot be blindly added without deduplication and status checks.
- **100 independently verified named physical sites NOT YET ACHIEVED**. Remaining **33 named physical plant records**, with independent evidence, are still required. Do not populate count from business names, projects, or invented facilities.
- TWDB primary 59-name source: https://www3.twdb.texas.gov/apps/desal/DesalPlants.aspx (public list retrieved 2026-10-14). Note the state database has had several survey updates and may contain outdated statuses. The listing is a named census source, **not a fresh current plant-operation check**. https://www.twdb.texas.gov/innovativewater/desal/maps.asp
- USBR public feasibility project source, updated Sep 2026: https://www.usbr.gov/watersmart/title/desal_eligible.html

## Source and status distinctions
`LISTED_IN_TWDB_DATABASE` = government public record of a facility; **not** evidence of a gypsum recovery plant or still active on a specific day. `IDLE_LISTED` means agency list specifically marks it idle. `OPERATING` for Carlsbad, Tampa Bay and Santa Barbara derives from official water utility sources, but **no reject assay was obtained** in this tranche. `PROPOSED` for Harbor Island, Doheny, Monterey/CalAm and Laguna Madre is **not current mineral production**.

The original Harbor Island model's **0.733 Mt/year gypsum equivalent at proposed 100 MGD** is a chemical-equivalent ceiling only, not a validated yield rate per MGD transferable to other plants. All named plant entries have `recoverable_gypsum_tpy = null`. The broader brackish-water population absolutely **cannot** inherit seawater chemical assumptions.

## Industrial gypsum joining lane (no invented excess)
The national 2025 USGS gypsum baseline counts **~17 Mt/y of synthetic gypsum ALREADY used**; it cannot be incrementally credited. Industrial options:
1. Unutilized FGD gypsum: real stacks/generators, quantity, chemical grade, radionuclide/trace measurements, EPA/State approvals and existing use must be identified by site; a positive inventory, landfill or power-plant capacity alone cannot prove recoverable excess.
2. Phosphogypsum stacks: EPA rules and required radionuclide controls are binding; status as *possible industrial or acid feed* does not establish legal agronomic supply.
3. Wallboard/cement plant gypsum scrap: existing recycled tonnes are baseline, requiring verified additional diversion from discard to qualified use.
4. Desalination brine gypsum precipitation: requires Ca and SO4 assays, reject mass, recovery process and actual segregated process feed.

## Next data engineering
- Source another 33 **operating or otherwise clearly identified physical plants** from state databases with exact names, status and canonical source IDs. Exclude feasibility-study proposals from confirmed-plant counts.
- Upgrade the 59 TWDB entries with the detailed database's `source water, rated capacity, operations status` fields and dates; independently verify larger plants first.
- Retrieve actual historical facility-by-facility unutilized calcium-sulfate streams from public plant documents/EPA byproduct disclosures where available, and preserve **unknown** for unpublished quantities.
- Cross-check first-year target (6.8 Mt 2025 crude imports + an additional 8.8 Mt proposed 20%-of-annual-consumption reserve) **15.6 Mt** against qualified physical supply, not hypothetical mineral inventories. Actual need and existing private stock levels need assessment. Human and regulator review required for any retrofits/allocations.

This stage is an **evidence-connected 67-row published ledger and 14 study leads**, not the completed 100-name register or 15.6 Mt activation solution. Earlier branch artifacts and drafts preserved.
