# ORCS v2.1 — Seawater versus brackish annual brine volume (91-site evidence register)

**2026-10-14 · ADDITIVE · NOTHING OVERWRITTEN · USER-APPROVED SOURCE SEGREGATION · NO CLAIM OF AN OPERATING BRINE MINE**

## Categories
All 91 named facility or project entries across v1.8 and v1.9 have been classified in new data file `data/desal_gypsum/orcs_seawater_brackish_separated_network_v2_1_2026-10-14.json`:
- 3 operating documented seawater (78 MGD nameplate product water)
- 4 proposed seawater (114.8 MGD nameplate, **not current brine output**)
- 1 reported opened 2025 seawater with no capacity in register (Stock Island)
- 1 brackish operating reported (6 MGD)
- 21 brackish historical or current status needing independent checks (164.3 MGD from 17 published capacities; 4 records unknown capacity)
- 61 source unclassified TWDB and California entries (all capacity unknown in current registry).

Counts = 3 + 4 + 1 + 1 + 21 + 61 = 91. None of the excluded sources is assigned a zero measured flow. Note that TWDB listed facilities include two designated idle.

## Flow law
Use only product-water nameplate capacities `P` and explicit scenario assumptions. For reverse osmosis first-pass simplification, feed `F=P/R`, reject `B=F-P=P(1/R-1)`; 1 MGD = 3,785.411784 m³/d, and annual model `B_y=B×365×utilization`. Actual pretreatment bypasses, concentrate stages, recycle, pilot uses, operational capacity and blending may violate the simple identity, so never call the resulting number a measured brine supply.

### Modeled reject brine:
| Cohort | Rated product MGD | Source status | Recovery scenario | Utilization | Annual reject million m³ |
|---|---:|---|---:|---:|---:|
| Seawater existing named | 78.0 | 3 operating | 50% | 90% | **96.99** |
| Seawater proposals | 114.8 | 4 projects, exclude from present | 50% | 90% | **142.75 FUTURE-ONLY** |
| Brackish recently reported existing | 6.0 | 1 Antioch CA, other status unverified | 70/80/90% | 90% | **3.20 / 1.87 / 0.83** |
| Brackish plus older rated sites | 170.3 | historical/status-uncertain capacity, NOT all presently operating | 70/80/90% | 90% | **90.76 / 52.94 / 23.53** |

A full nameplate hypothetical **seawater-existing plus all known-capacity brackish** equals **120.52 to 187.75 million m³/y** (corresponding brackish recovery 90 to 70%). This is a conditional scenario mixing current and **unverified historical facilities**, NOT a claim of 2026 national output, and omits **62 sites with unknown source/capacity as well as 4 brackish records missing capacity**.

If proposed seawater projects are also included, a much less grounded *eventual capacity planning screen* would be approximately **263.27 to 330.51 million m³/y**, contingent on construction and all older brackish capacities. Again not a measured forecast.

## Brine mining feed versus physical outfall
The volume of rejected concentrate is not the same as the volume a plant can separately intercept economically before seawater cooling-water dilution. Brackish groundwater may be dominated by carbonates, sulfates or other ions; chemistry cannot be copied from USGS seawater profiles. Distinguish water volume, dissolved dry TDS mass, target-ion mass, recoverability, usable product, actual revenue and marine or terrestrial disposal risk.

## What is needed to calculate an actual 91-site total
For each named active operator: permitted and metered annual *feed* and *concentrate* m³, time stamps, blending/interception point, pretreatment reject/RO reject split, salinity/TDS and ions (Mg, Ca, K, SO4, Na, Cl, Br, trace D Li B I), actual recovery, product grade/market, regional rights and environmental permits. Only then compute gross and net mineral production and import displacement. No live operating telemetry was accessed.

## Code and source
- Registry: [ORCS seawater/brackish v2.1](../../data/desal_gypsum/orcs_seawater_brackish_separated_network_v2_1_2026-10-14.json)
- Calculator: [flow_categories_v2_1.py](../../prototypes/orcs-brine-portfolio-v2_0/flow_categories_v2_1.py)
- Previous source registries [v1.8](../../data/desal_gypsum/orcs_named_facility_register_v1_8_2026-10-14.json) and [v1.9](../../data/desal_gypsum/orcs_source_verified_additional_24_named_sites_v1_9_2026-10-14.json)
- Existing multispecies seawater inventory model [v2.0a](../../prototypes/orcs-brine-portfolio-v2_0/portfolio_v2_0a.py)

**All hypothetical mining, financial and mineral import offsets remain modeled sensitivities and zero realized credit.**
