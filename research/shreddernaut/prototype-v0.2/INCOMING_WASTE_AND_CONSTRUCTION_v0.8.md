# Shreddernaut v0.8 — Five years of incoming waste, including construction and demolition

**Status: source-based national inventory plus illustrative capacity and recovery scenarios. Not a waste forecast, verified mineral reserve, engineered throughput guarantee or investment return.**

## What changed

The v0.6 national model did not explicitly inventory five years of incoming municipal solid waste (MSW) and construction/demolition debris (C&D). Its selected metal-rich feed case was conditional, not a representative national waste composition. This addition inventories fresh flows separately, excludes existing recovery from the incremental feed pool, and makes fresh streams compete with legacy material for the same fleet capacity. Original models remain historical scenarios; their returns and copper-rich outputs do not automatically carry over.

C&D is included here as a separate account. EPA explicitly excludes it from MSW. C&D covers construction, renovation and demolition of buildings, roads, bridges and other structures. Industrial process wastes, mine tailings, sewage sludge and separate vehicle streams remain outside this inventory.

## Projection basis and national flows

EPA's national Facts and Figures series is current through 2018. These are **five future planning years at 2018 annual rates**, with optional 1% and 2% annual growth sensitivities; they are not observed 2026 rates or an extrapolation of measured growth through 2026. Disposal shares and composition are held constant. Update the baseline with current state/local scale records before procurement.

All displayed quantities below are **million metric tonnes (Mt)**. EPA's U.S. short tons are converted at 0.90718474 metric tonnes per short ton. Table 1's precise MSW generation total, 292.36 million short tons, is used rather than the overview's rounded 292.4.

| Stream | Annual generated | Five-year generated | Five-year baseline landfill destination |
|---|---:|---:|---:|
| MSW | 265.22 | 1,326.12 | 662.79 |
| C&D | 544.61 | 2,723.05 | 652.18 |
| Combined | 809.83 | 4,049.17 | 1,314.96 |

The distinction matters: 4.05 billion tonnes are generated, but only about 1.315 billion tonnes are assigned to landfills in this baseline. Material already going to recycling, aggregate, compost, fuel and other management cannot all be claimed as new recovery by Shreddernaut. EPA's C&D “next use” includes fuel and aggregate; it does not mean every tonne returns to an equivalent manufactured product.

| Annual growth sensitivity, beginning after planning year 1 | Five-year generated, Mt | Five-year baseline landfill destination, Mt |
|---|---:|---:|
| 0% | 4,049.17 | 1,314.96 |
| 1% | 4,130.97 | 1,341.53 |
| 2% | 4,214.41 | 1,368.63 |

Under the user's equal-50-state arithmetic, the flat case adds **26.30 Mt of landfill-bound material per state over five years**, before additional intervention. Actual state flows differ substantially; these numbers are not Maui estimates.

## Material opportunity in fresh landfill-bound streams

This table is **material present before collection, sorting losses, contamination, buyer acceptance or refining**, not finished output or a commercially recoverable reserve.

| Five-year material pool | MSW, Mt | C&D, Mt |
|---|---:|---:|
| Ferrous / reported C&D metal proxy | 47.76 | 4.99 |
| Aluminum | 12.07 | Not separately quantified |
| Other nonferrous, including lead; not all copper | 3.36 | Not separately quantified |
| Concrete | — | 322.91 |
| Brick/clay | — | 48.98 |
| Asphalt pavement | — | 22.22 |
| Asphalt shingles | — | 58.96 |
| Gypsum drywall | — | 59.87 |
| Wood | — | 134.24 |

EPA's C&D management table reports “metal”; this model uses the corresponding generation table's steel category as a ferrous proxy. Aluminum and copper are **unknown**, not physically absent. Rounded C&D category figures total 143.8 million short tons/year; their shares are normalized to the more precise 143.78 summary total. This small adjustment prevents a rounding discrepancy in the mass ledger.

MSW copper is not isolated in the EPA table. Sensitivities assign 0%, 25% or 50% of the landfilled “other nonferrous” category to copper. These are deliberately hypothetical shares; 0% means no recovery credit, not proof of no copper. EPA's aluminum material page also cautions that its recycling quantity represents cans only; broader aluminum recovery is not fully reported. These inventories therefore remain screening inputs needing local characterization and additionality checks.

## Integrating fresh feed without adding free capacity

Keep the previous central deployment assumption: 5,000 target units, 20 tonnes/day, 300 operating days/year, with average active fleet fractions of 10%, 25%, 50%, 75% and 100%. The same fleet processes **78 Mt over five years** and 30 Mt/year in year 5. The operating-day assumption is retained; no additional availability multiplier or unproved speed increase is applied.

Three capacity-allocation scenarios are included in the script: all legacy; 40% legacy / 30% fresh MSW / 30% fresh C&D; and 50% fresh MSW / 50% fresh C&D. These shares are illustrations, not an optimized deployment recommendation. The C&D scenarios require suitable handling/preparation to sustain the carried-over throughput assumption; no crusher performance is established.

| Intake in the illustrative 40/30/30 scenario | Five-year Mt |
|---|---:|
| Legacy | 31.20 |
| Fresh landfill-bound MSW | 23.40 |
| Fresh landfill-bound C&D | 23.40 |
| Total | 78.00 |

Thus 46.8 Mt of incoming material is screened, about **3.56% of baseline new landfill-bound tonnage**. The 78 Mt is throughput, not total waste eliminated. At full deployment the fleet's entire 30 Mt/year is only about 11.4% of the baseline 263 Mt/year incoming landfill flow, even if all units were assigned to fresh material.

Fresh MSW fractions come from its landfill destination: ferrous 10.53/146.12, aluminum 2.66/146.12, and other nonferrous 0.74/146.12. Fresh C&D uses the normalized landfill category shares. Legacy feed retains the old synthetic 3% ferrous, 0.7% aluminum and 0.3% copper. All lanes assume 80% capture, 90% buyer acceptance and downstream yields of 95% for ferrous/aluminum and 97% for copper. None is a demonstrated Shreddernaut yield.

| Modeled finished output, all three lanes combined | Five-year tonnes | Gross national consumption-equivalent days if all stored |
|---|---:|---:|
| Ferrous | 1,916,088 | 7.36 |
| Aluminum | 440,755 | 28.22 |
| Copper, no fresh copper credited | 65,370 | 10.85 |
| Copper, hypothetical 25% share of MSW other nonferrous | 86,061 | 14.28 |
| Copper, hypothetical 50% share | 106,752 | 17.71 |

Copper rows are alternative cases, not additive. C&D aluminum/copper receive no quantified credit. The first copper row still includes synthetic legacy copper. Coverage uses v0.7's held-constant 2025 USGS demand bases: 95 Mt/year steel mill products, 5.7 Mt/year aluminum excluding new scrap, and 2.2 Mt/year broad copper consumption. These are different product bases. All output would need suitable domestic conversion, grade qualification and storage; no withdrawals are assumed. These are consumption equivalents, not proof of Vault eligibility or supply for a particular defense industry.

The materially lower copper yield than the earlier enriched case follows from changing the feed assumption. A qualified wiring/equipment recovery lane could outperform average waste, but its available tonnes must be established separately; one cannot apply 2% copper to ordinary national waste by default.

## Stock and flow: screening is not remediation

Using the 25% copper sensitivity, finished products total **2.443 Mt**, consisting of approximately 0.855 Mt recovered from legacy material and 1.588 Mt diverted from fresh disposal. In the closed metal-only ledger, all other material and refining losses return to landfill. No other product, mineral reuse, biodegradation or change in existing recovery is credited.

Consequently, incoming landfill additions remain approximately **1,313.38 Mt**, and buried mass across the modeled streams grows by about **1,312.52 Mt after subtracting legacy product removal**. This is an accounting illustration, not a forecast of actual site mass changes. Some real residues may take other routes, and safe remediation involves more than mass removal.

The earlier rounded 10-billion-tonne legacy assumption is not a verified combined MSW+C&D stock. Historical C&D stock is still unknown. Do not add new C&D to an MSW-only historical inventory and call the result a complete national landfill reserve. A complete-remediation date cannot be established from this model.

## Design and economics implications

Use separate operating lanes. Recover accessible equipment, wire and reusable components before mixing or crushing; send qualified metals to contracted refiners. Direct concrete, masonry and asphalt to regional bulk processors with appropriate crushers, screening, contamination controls and product testing. Segregate gypsum, wood, hazardous items and other specialist fractions. The prototype's metal separation line does not establish the capacity, cost or suitability of any of those additional processes.

Concrete reuse is primarily a local aggregate opportunity; tonnes are not copper-equivalent strategic inventory. Shipping heavy low-value minerals from Maui needs its own cost assessment. Appropriate local use may matter more than mainland shipment. No aggregate revenue, avoided mining value, carbon credit or plastic-processing return is booked here.

**v0.8 does not assign a new ROI.** Different feeds require different loading, separation, treatment, residue handling and partner costs. The prior metal-rich 131% national financial ROI remains conditional on its prior enriched feed and cost assumptions. It is not the return of these source-based mixed-waste scenarios. Refiner capacity, local feed assays and binding acceptance terms are still needed.

## Reproducibility and sources

Run `python3 incoming_waste.py` beside the earlier files. It writes detailed annual results and a compact summary, and checks capacity conservation, product-plus-residue mass balance, inventory bounds, category normalization and the five-year baseline sum. `incoming-waste-summary.json` is the published compact output; full annual results regenerate locally.

Primary sources, accessed October 21, 2026:

- [EPA national overview](https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/national-overview-facts-and-figures-materials): dataset date, national generation and scope exclusions.
- [EPA C&D material-specific data](https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/construction-and-demolition-debris-material): precise annual summary totals and definitions of next use.
- [EPA 2018 Fact Sheet, Tables 1, 6 and 8](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P1019BN2.TXT): MSW disposal/material totals and C&D generation/disposal composition.
- [EPA aluminum data](https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/aluminum-material-specific-data): recycling-data coverage limitation.
- [v0.7 reserve coverage](VAULT_RESERVE_COVERAGE_v0.7.md): USGS consumption sources and qualifications.
- [v0.6 national assumptions](national-assumptions.json): prior ramp and fleet context; historical feed and financial scenarios are not replaced with unverified new return estimates.
