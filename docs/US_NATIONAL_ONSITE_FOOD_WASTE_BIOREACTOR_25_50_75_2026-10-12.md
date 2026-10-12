# USA onsite bioreactor food-waste diversion — national 25/50/75% scenarios

**2026-10-12 · MODELLED, not contracted or demonstrated · ZERO REALIZED CREDIT**

## National input: protect the resource denominator
[ReFED 2026 US Food Waste Report](https://refed.org/food-waste/refed-us-food-waste-report-2026/) gives **70 million US short tons surplus food in 2024**, which contains material still edible or already beneficially managed. [ReFED 2024 statistical fact sheet](https://refed.org/downloads/food-waste-in-the-united-states-2025.pdf) states **nearly 60 million US tons became food waste**. For a conservative transparent *gross food-waste envelope*, this paper assumes **60 million US short tons** nationwide; that is **not** 60 million newly available tons and is NOT equivalent to current landfilled mass. EPA historic 2019 account uses different sectors and method: https://www.epa.gov/facts-and-figures-about-materials-waste-and-recycling/food-material-specific-data ; do not add its 40m food-manufacturing tons atop ReFED 60m without reconciliation.

## Deployment premise
**At least one biological processing unit onsite at each qualifying participating large waste generation or consolidation facility.** This is a deployment hypothesis, not an asserted feasibility for every grocery, restaurant, home, farm or transfer station. Larger sites can use multiple modules; small sources can use shared transfer-site units. Sizing should follow independently measured wet tonnes/day and uptime. An onsite unit may save outbound freight but still incur organics segregation, processing product transport, feedstock contaminants, energy and staff/maintenance.
- Processing cost **$20 per US short ton** = **$22.05 per wet metric tonne** — is the explicit 'half as costly as trash' scenario. Separate user's previous **$10/wet metric ton** aspirational process target (not the same normalized assumption).
- Disposal cost **$40 per US short ton** for strict 2:1 demonstration, or **$62.63 per US short ton** as published **2024 nationwide tonnage-weighted landfill tip fee**: [EREF 2024 report](https://erefdn.org/product/2024-analysis-of-municipal-solid-waste-msw-landfill-tipping-fees/). Applying an overall MSW fee to all organic material is an **illustrative price proxy, not actual food-waste contract fees** and assumes displaced volumes would otherwise pay that fee.
- Gas and NPK are credited **separately** only to a realized offtake, never additionally counting digestate product and nutrient value for the same material. No credit for existing reuse, rescue or composting as avoided landfill unless it was in fact landfill-bound.

## Strict disposal-vs-process annual arithmetic, before all other charges
| Scenario | Food waste processed, US short tons/y | National landfill disposal avoided @$62.63/short t | Process @$20/short t | Direct nominal avoided gate minus process | Methane Bcf/year gross potential |
|---:|---:|---:|---:|---:|---:|
| 25% | 15.0M | $0.939B | $0.300B | **$0.639B** | 28.8–72.1 |
| 50% | 30.0M | $1.879B | $0.600B | **$1.279B** | 57.7–144.2 |
| 75% | 45.0M | $2.818B | $0.900B | **$1.918B** | 86.5–216.2 |

For the exact **2:1 $40 vs $20** case the direct waste-handling margin is **$300M / $600M / $900M per year** at 25/50/75% capture. With published 2024 weighted **$62.63 landfill tip** and hypothetical $20 processing, direct nominal margins are **$639M / $1.279B / $1.918B per year**. None are audited net benefit after financing, sorting, residual handling, collection or market fulfillment.

## Additional potential recoverable nutrients, NOT included in direct savings
Reuse Texas food-waste **assumed** yields, not national BMP: per original wet metric tonne of food waste **2–6 kg crop-accessible nitrogen, 0.5–2 kg P₂O₅ equivalent, 1–3 kg K₂O equivalent**, completely dependent on assays, chemistry and agronomic access. A short ton is 0.90718474 metric tonnes.
| Captured waste | Recoverable N million kg/y | P₂O₅ million kg/y | K₂O million kg/y |
|---:|---:|---:|---:|
| 25% | 27.2–81.6 | 6.8–27.2 | 13.6–40.8 |
| 50% | 54.4–163.3 | 13.6–54.4 | 27.2–81.6 |
| 75% | 81.6–244.9 | 20.4–81.6 | 40.8–122.5 |

These numbers are **screening nutrient-potential** and do not establish retail fertilizer tonnage, net new national fertilizer supply, registered end product or import displacement. Food rescue and existing reuse take priority.

## Gas coproduct potential, not pipeline output
Per wet metric tonne source-separated suitable food waste, gross methane **60–150 m³ CH4**, *assumed*, without collection contamination or methane-upgrading/downtime. Bcf computed as `US_short_tonnes × 0.90718474 × assumed_m3_ch4_per_metric_t × 35.3147 / 1e9`. No value from gas has been added to disposal savings above. Methane leaks, process energy and whether onsite power/heat is superior to RNG injection remain to be evaluated.

## Facility minimum / deployment count caveat
'One facility onsite' means one eligible industrial/farm/municipal collection node, **not one single reactor sufficient for a city**, and not an estimate of how many sites exist. A hypothetical 100 wet metric tonne/day module at 365 utilization would treat 36,500 wet tonnes/year, or 40,234 US short tons/year; thus captured 15m/30m/45m US short tons requires **about 373 / 746 / 1,119 fully utilized 100 metric-tonne/day reactor equivalents**. This is a *capacity-equivalence*, not actual number of operating plants or eligible site count; lower uptime implies more capacity, and smaller distributed reactors multiply facility count. Avoid counting onsite modules and shared collection hub reactors twice for the same waste.

## Reproducible scenario formula
```python
WASTE_SHORT_TONS=60e6
LANDFILL_USD_PER_SHORT_TON=62.63
PROCESS_USD_PER_SHORT_TON=20.00
for recovery in (0.25,0.50,0.75):
    tons=WASTE_SHORT_TONS*recovery
    print(recovery, tons,
          tons*(LANDFILL_USD_PER_SHORT_TON-PROCESS_USD_PER_SHORT_TON))
```

## Financial systems: stop double counting
- Local government/generator **avoided landfill cost** and processor **collected tipping fee** represent the same economic transfer stream under different contracts, not two independent system benefits.
- No new reactor output product value can be added to historical wasted **food retail value** (ReFED's $380B+); this is the original food's opportunity loss, not digester feedstock's sale value.
- Actual capital, labor, de-packaging, solids treatment, hauling, methane cleanup, product registration and sales, energy/heat integrations, water, salt, environmental externalities, operator feedstock rights and subsidies remain site-dependent.
- **National half-cost claims are a conditional target, not a demonstrated all-in cost advantage.** National feasibility requires region-level waste allocation by actual baseline treatment and competing beneficial pathways.

## Next evidence
Confirm regional ReFED resource by sector/fate, cite on-site bioreactor vendor guarantees ($/ton and residence time), site sample/BMP and product maturity, local municipal rate contracts, power/gas offtake, actual residual and truck route costs, and one qualified facility inventory. Build county/metro allocation and prohibit processing edible food diverted from donation.


## 2026-10-12 correction: user's $10 per WET METRIC TON processing target (authoritative requested sensitivity)
The preceding document's **$20 per US short ton** model was a distinct half-cost scenario, not the user's **$10 per wet metric ton** cost target. The $10/wet-metric-ton case must be shown prominently and not silently conflated with the $20/US-short-ton scenario. Conversion: **$10/metric tonne = $9.0718474/US short ton**. National 60,000,000 US-short-ton food-waste envelope and EREF 2024 landfill benchmark $62.63/US-short-ton unchanged. Modeled avoided tipping less reactor processing cost:

| Captured resource | US short tons/year | Baseline tipping avoided | $10/wet metric ton processing | Corrected direct delta |
|---:|---:|---:|---:|---:|
| 25% | 15,000,000 | $939,450,000 | $136,077,711 | **$803,372,289/year** |
| 50% | 30,000,000 | $1,878,900,000 | $272,155,422 | **$1,606,744,578/year** |
| 75% | 45,000,000 | $2,818,350,000 | $408,233,133 | **$2,410,116,867/year** |

Difference in USD/US-short-ton: $62.63 − $9.0718474 ≈ **$53.56**. Gross tipping avoided is **not** a guaranteed avoided expense if diversion includes waste not previously landfilled, and onsite equipment often requires a product/offtake and sorting network. Excludes onsite CAPEX, maintenance not counted in $10, sorting/depackaging, power, transport of residues/outputs, marketing, and existing beneficial reuse. Earlier $20/US-short-ton results remain archived in preceding sections, labeled an alternate stress case, rather than deleted. No assertion that the $10/wet-metric-ton commercial cost is verified; this is an unvalidated engineering target, not a vendor quote.
