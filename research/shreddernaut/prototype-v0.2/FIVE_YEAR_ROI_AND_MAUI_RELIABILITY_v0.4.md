# Shreddernaut v0.4 — five-year ROI and Maui maintainability

2026-10-20 | EXECUTED SYNTHETIC SENSITIVITY / PROPOSED HARDWARE REQUIREMENTS

## Financial definition

Five-year simple cash ROI = (five full years of operating cash surplus − initial installed equipment/development investment) / initial investment. Pre-tax, unlevered and undiscounted. No salvage, grants, carbon credits or terminal value. Five years start with operations; development/construction delays are not included. Base investment is $500,000, with a separate $160,000 working reserve excluded from the main ROI denominator. If reserve is returned in full at year five, the enriched toll case's return on total $660,000 funding is about 325%, compared with 429% on equipment/development. No reserve recovery is guaranteed.

Inputs remain the synthetic feed, prices, fees, costs and capacity assumptions documented in COST_AND_PAYBACK_v0.3.md. One richer stream assumes 8% ferrous, 4% aluminum and 2% copper in incoming mass; this is NOT a typical Maui landfill composition. At 300 days/year and 20 t/day, each five-year base case processes 30,000 tonnes. No actual continuous feed supply, refinery contract or site quote exists.

## Base results: 300 operating days annually

| Feed / route | Hypothetical service fee per input t | Five-year operating cash surplus | Net cash after $500k initial investment | Cumulative five-year ROI |
|---|---:|---:|---:|---:|
| Legacy / toll | $0 | -$3.061m | -$3.561m | -712% |
| Legacy / toll | $150 | $1.439m | $0.939m | 188% |
| Legacy / toll | $200 | $2.939m | $2.439m | 488% |
| Selected metal-rich / scrap | $0 | $1.063m | $0.563m | 113% |
| Selected metal-rich / toll | $0 | $2.643m | $2.143m | 429% |

Negative ROI below -100% means continued operating losses require additional cash beyond initial investment; a real operator would need to stop, reconfigure or secure compensation. It is not a prediction that an unfunded plant could run for five years.

Service fees are conditional contractual revenue, not automatically received tipping charges. Paying a public remediation fee can deliver public benefit but does not make that payment a free system-wide profit. Actual imported-material displacement and ecosystem gains are not monetized here.

## Stress tests: selected metal-rich toll case, no service fee

| Change from base | Five-year ROI |
|---|---:|
| Base: 300 days/year | 429% |
| 240 days/year, retain planned staff/rental/overhead | 229% |
| Finished metal prices down 20%, conversion charges unchanged | 100% |
| Cash operating costs up 15% | 310% |
| 240 days + prices down 20% + costs up 15% + extra $100k year-3 overhaul | -163% |
| Illustrative Maui overlay | 149% |

Reduced operating days do not eliminate committed annual staff, rental or overhead in this model. Model holds $468,000/year of those base costs while throughput-dependent costs vary. This is more conservative than multiplying every expense by fewer days. Actual retention and rentals require contracts. Extra overhaul is a downside allowance ABOVE existing maintenance, not a claim of a known failure or routine expense.

The Maui overlay is an analyst sensitivity, NOT a quote: add $100,000 initial shipping/adaptation/spares allowance, $50,000/year added overhead, and $250/accepted metal tonne extra toll-route freight on top of the base freight assumption. Enriched toll investment becomes $600,000 excluding working reserve; five-year operating cash falls to $1.495m and net cash after investment to $0.895m, giving 149% ROI. Base $160k reserve is not automatically adequate after island changes.

Do not combine any of these percentages with the earlier daily payback without using the matching case. The overlay's payback is about 602 operating days, or two operating years at 300 days/year. Island freight, receiving-port access, storage and mainland processing capacity need binding bids. Scrap-route net prices in the base are already net prices; for a real Maui scrap quote they must be replaced with island-specific net terms rather than assuming unchanged freight.

## Dependability: reasonable architecture, unproven performance

The design uses established equipment types, but no Shreddernaut hardware has been assembled or tested. The 80% within-shift availability in example.json is an assumption, not an observed reliability rate. The 300-day schedule is also an assumption. Throughput, maintainability and safe operations must be established independently; passing Python checks validates arithmetic only.

Commercial precedent: [REMEX mobile IBA processing](https://www.remex-processing.com/iba-processing/mobile-iba-processing/) describes coordinated mobile modules for screening, magnetic/eddy-current separation and sorting. Its scope is incinerator bottom ash, not evidence of mixed-landfill yields or our availability. [Eriez service](https://www.eriez.com/Service/Service-Repair) and [manuals](https://www.eriez.com/Resources/Manuals) provide equipment-specific repair and maintenance routes. These are prospective technology references, not project partners.

## Proposed Maui configuration

- Receiving and hazard-isolation bay on an approved working surface, separate from clean service/control space.
- Trailer/skid screen and feed module; replaceable screen panels and accessible wear surfaces.
- Ferrous separation module with independent drive/control interfaces.
- Nonferrous module selected for measured size/moisture/metal content; aggregate small metal lots for shipping.
- Labeled output and residual bins with covered storage where needed.
- Containerized clean controls, tools, qualified spares and workbench; local manual operation and interlocks remain available without internet. Container thermal management must be sized.
- Common bolt patterns and documented electrical/mechanical interfaces where vendors allow; access clearances and designed lifting points. No assumption that all modules fit inside a single container.
- Coastal corrosion specification: appropriate materials/coatings, dissimilar-metal isolation, weather protection, sealed electronics and inspection/cleaning plan. Final specifications by qualified designer after site survey.

The reliability goal is rapid safe replacement using available parts. A shipping container alone provides transportability/protection, not maintainability; service access, extraction routes and spare inventory must be designed.

## Manufacture each component by the best qualified route

| Part class | Initial route | Qualification / spare strategy |
|---|---|---|
| Sensor mounts, labels, cable guides, assembly fixtures | Locally printable polymer where suitable | Stored CAD, specified material/process and fit/UV/temperature checks |
| Guides and low-load custom chutes | Print trial pieces or fabricate sheet metal | Impact/abrasion tests; replaceable wear surfaces |
| Frames, hopper, structural screen supports | Conventional fabricated steel initially | Structural design, coating and local repair drawings |
| Motors, gearboxes, bearings, belts, VFDs | Standard purchased parts | Minimize unique types; stock critical spares on island |
| Magnetic/eddy-current rotor assemblies | Qualified vendor equipment | Vendor service route, condition monitoring and replacement plan |
| Wear plates, shafts, high-load/high-speed parts | Qualified fabrication/machining initially | Material certificates and balance/fatigue requirements as applicable |

Printing the whole machine is not established as the cheapest or most reliable route. Additive manufacturing itself needs part qualification; [ORNL research on residual stress](https://www.ornl.gov/news/dealing-stress-large-scale-additive-manufacturing/) explains possible cracking and fatigue implications in large printed metal parts. Printed parts may still need heat treatment, machining, inspection and finishing. Ordinary recycled feed is not automatically suitable printer feedstock. No printed-content percentage or replacement-time guarantee is claimed.

## Proposed dependability acceptance plan

1. Vendor sample tests for real feedstock, including wet and entangled material. Eriez advertises a [recycling test center](https://www.eriez.com/Service); access and fees need agreement.
2. Identify failure modes per module: screen plugging, belt tracking/tear, bearing/drive failure, separator fouling, corrosion, sensor contamination and power loss. Measure consequence, repair time, cost and spare lead time.
3. Demonstrate safe access and a timed replacement of a representative wear part and drive module with local staff. Record actual total restoration time, including diagnosis and recommissioning; do not count only wrench time.
4. Track planned shift hours, run hours, unplanned stops, intake tonnes, quality acceptance and repair hours separately over 30/60/90-day trials. No reliability prediction without enough representative exposure.
5. Keep critical spares, offline manuals/CAD, tool lists and training on island. Set quantities from measured failure frequency and replenishment time; an initial inventory is only a provisional allowance.
6. Use buffers and an accepted offsite route where feasible. Safe bypass is permitted only when product quality and hazard controls remain satisfied; a separator cannot simply be bypassed while claiming unchanged recovery.
7. Re-run ROI with measured availability, maintenance, freight, salaries, acceptance and sustained feedstock supply before deciding to replicate.

## Reproduce

`python3 five_year.py --output five-year-results.json`

The script executes six variants for all 16 existing feed/route/service-fee combinations (96 results). Embedded checks reconcile base five-year cash to v0.3 daily cash and verify downtime sensitivity. All source assumptions remain visible. New files are additive; earlier calculations and source documents remain intact.
