# Shreddernaut v0.3 — prototype cost and operating-day payback

2026-10-20 | EXECUTED SCREENING CALCULATION | NOT A QUOTE, INVESTMENT FORECAST OR VALIDATED PLANT

## Answer

The initial planning allowance is approximately $270,000–$654,000 for the installed modular dry-recovery line including 20% contingency, at an existing permitted mainland host. Adding a $50,000 illustrative development campaign gives $320,000–$704,000 before working cash. Use $450,000 installed equipment plus $50,000 development ($500,000 total) as a central scenario; a further $160,000 cash reserve gives a $660,000 initial funding envelope. These are analyst allowances anchored only partly to advertised equipment prices; unforeseen site requirements can exceed them.

At 20 metric tonnes/day, the synthetic metal-rich toll-processing case repays the central $500,000 in about 284 operating days without a service fee. The synthetic ordinary legacy-feed case has NO payback without a contracted service fee. It repays in about 521 operating days at $150 per incoming tonne, or 255 days at $200/t. No such contracts, feed composition or refinery terms are established.

## What is and is not purchased

The budget covers feeding/screening, magnetic and eddy-current separation, conveyors/bins/frames, electrical integration, limited site safety controls, printed fixtures/tooling and mobilization/commissioning. It does not buy a refinery, plastic-processing line, shredder, loader, land or new building. Loader/excavator access is represented as daily rental in operating costs. No automatic cost savings are assigned to 3D printing.

| Component | Low allowance | High allowance | Evidence classification |
|---|---:|---:|---|
| Screening/feeding | $53,000 | $150,000 | Low point anchored to advertised static screen; suitability not confirmed |
| Magnetic separation | $15,000 | $35,000 | ASSUMED allowance |
| Eddy-current separation | $35,000 | $70,000 | Low point anchored to ended used listing; no availability claim |
| Conveyors/bins/frames | $25,000 | $60,000 | ASSUMED allowance |
| Electrical/controls/integration | $40,000 | $90,000 | ASSUMED allowance |
| Safety/dust/drainage | $30,000 | $70,000 | ASSUMED allowance, site dependent |
| Printed fixtures/tooling | $2,000 | $10,000 | ASSUMED allowance, no purchased printer |
| Mobilization/commissioning | $25,000 | $60,000 | ASSUMED allowance |
| Subtotal | $225,000 | $545,000 | Screening budget, not a binding estimate |
| Contingency (20%) | $45,000 | $109,000 | ASSUMED |
| Installed line | **$270,000** | **$654,000** | Excludes working cash and development |

Additional exclusions: taxes, duties, major site civil works, new permit-driven treatment systems, legacy excavation remediation works beyond the simple operating allowance, groundwater cleanup, closure/restoration, unusual hazardous waste, ocean freight and financing costs. Equipment transport and commissioning allowances require quotes. No calendar deployment commitment is made.

## Public price anchors and their limits

- [Machinery Partner Gremac eZero](https://www.machinerypartner.com/heavy-equipment/gremac-eZero-static-trommel-screener): advertised new from $53,000; excludes taxes, transportation and parts packages. Published throughput is NOT a demonstrated mixed-landfill rating.
- [DADE 2006 SGM VIS 300 separator](https://www.dadeauctions.com/Listing/Details/1597963/2006-SGM-VIS-300-Eddy-Current-Separator): listed $35,000, ended/no longer available; sold as-is. Historical asking-price anchor only.
- [DADE HOAT system](https://www.dadeauctions.com/Listing/Details/1740781/Screens_Separators): page shows a $150,000 asking price for a used metals-from-dirt system with conveyors/magnet/eddy-current equipment, but also states no longer available. Exact included equipment/condition, buyer premium and actual sale price require verification. This is a reason to investigate existing used lines, not a $150,000 installed Shreddernaut quotation.

## Model and feed assumptions

Run `python3 payback.py --output payback-results.json` in this folder. Inputs are in payback-assumptions.json; underlying operating costs and stage ratings come from example.json/model.py. `python3 verify_payback.py` checks accounting invariants. Original v0.2 files remain unchanged.

| Input | Legacy sensitivity | Selected metal-rich sensitivity |
|---|---:|---:|
| Input/day | 20 t | 20 t |
| Ferrous fraction of input | 3% | 8% |
| Aluminum fraction | 0.7% | 4% |
| Copper fraction | 0.3% | 2% |
| Total metal content | 4% | 14% |
| Capture of each metal | 80% | 90% |
| Buyer acceptance of captured metal | 90% | 95% |
| Accepted metals/day | 0.576 t | 2.394 t |
| Cash operating cost/day | $2,654 | $2,643 |

The selected case is deliberately enriched, including **2% copper in total incoming mass**. It is not a claim about normal fresh MSW, an average landfill, or West Maui feed. Qualification must assay metal content within recovered streams; metal-bearing items are not treated as 100% metal. The assumption here is metal-equivalent fractions, with refining losses applied later. No gold, lithium, fines, plastics, carbon credits or land-value revenue is booked.

Operating costs include four staff at $30 loaded/hour for eight hours ($960/day), $400/day mobile equipment rental, $100/day other costs, $100/day fixed-cost allocation at 300 operating days/year, $100/day maintenance, assumed electricity and diesel, plus residual management. Legacy residual management alone is about $941/day. At an existing landfill, lawful onsite residual management may cost less than the assumed re-disposal charges; obtain incremental site costs instead of automatically paying a second full gate fee. Conversely contamination can raise costs substantially. There is no receipt supporting $10/t all-in processing in this model.

## Scrap versus toll-processing economics

Synthetic round price sensitivities, NOT current market prices or offered contracts:

| Metal | Scrap net receipt per accepted tonne | Finished-product price per tonne | Metallurgical yield | Conversion fee per accepted feed tonne |
|---|---:|---:|---:|---:|
| Ferrous | $250 | $500 | 95% | $250 |
| Aluminum | $1,400 | $2,500 | 95% | $500 |
| Copper | $6,000 | $10,000 | 97% | $500 |

Toll route also subtracts freight ($80/accepted t), assay allocation ($12/accepted t), and selling charge (2% of gross finished-product value). Conversion fees are assumed to include processor energy and downstream residue handling. Actual minimum lots, minimum batch charges, alloy/grade requirements, acceptance, payable-metal deductions, impurity penalties, settlements, logistics and losses may be worse or better. Ferrous remelting and aluminum remelting are different processes from copper refining; the model uses a common accounting interface, not one universal refinery. 60-day settlement is only a working-capital sensitivity.

No gross-up of scrap revenue to finished value without those deductions. Source chain ownership and product credits need explicit contracts. A downstream partner has not offered any terms. A joint venture is not separately modeled because no revenue share or cost allocation exists; inventing one would add false precision.

## Executed outcomes

All values rounded; cash surplus excludes financing, taxes and annualized capital charges. Service fees below are hypothetical paid contracts, not assumed grants or automatically received tipping fees.

| Feed/route | Service fee/input t | Daily cash surplus | Payback operating days | Years at 300 operating days |
|---|---:|---:|---:|---:|
| Legacy / scrap | $0 | -$2,145 | None | None |
| Legacy / toll | $0 | -$2,040 | None | None |
| Legacy / toll | $100 | -$40 | None | None |
| Legacy / toll | $150 | $960 | 521 | 1.74 |
| Legacy / toll | $200 | $1,960 | 255 | 0.85 |
| Selected metal-rich / scrap | $0 | $709 | 705 | 2.35 |
| Selected metal-rich / toll | $0 | $1,762 | 284 | 0.95 |

The legacy toll case needs about $102/input t in service revenue merely to cover modeled operating costs, before recovering initial investment. The equivalent scrap threshold is about $107/t. Toll improves the legacy result by only about $105/day; it improves the enriched result by about $1,053/day. Refinery participation does not automatically fix a poor feedstock.

## Payback and liquidity definitions

Simple payback operating days = ($450,000 installed capital + $50,000 one-time development) / positive daily cash surplus. Cash surplus = net product receipts + actually contracted service revenue − cash operating expenses. Negative/zero surplus gives no payback. No depreciation, capital-recovery charge, principal repayment or grants are subtracted again in this unlevered simple-payback calculation. This is not discounted cash flow, IRR or a financing approval.

The $160,000 initial reserve is liquidity, not another expense to be charged against every operating day or a grant. At roughly $2,654/day, 60 fully operating days before any customer settlement would require about $159,000. Actual calendar work schedules, deposits, service-payment timing and ramp losses determine the real bridge. It may not cover prolonged commissioning losses. Payback is shown in operating days and normalized years; initial development, idle days, commissioning and payment delays make calendar cash recovery later.

A funding award can lower the owner's initial outlay, but does not improve the underlying operating margin. Taxpayer/system costs remain visible. Material revenue plus gate fees plus avoided disposal savings must not be counted as three independent benefits to the same operator.

## Economic design decision

For fastest plausible self-financed recovery, select assayed metal-rich feed first, aggregate enough volume for competitive conversion terms, share existing host infrastructure, and obtain paid product settlements. For low-grade legacy remediation, structure a public/environmental service contract and evaluate the full remediation benefit separately. Compare larger sorting lines to the 20-t/day pilot before fleet procurement. Printing fixtures may shorten iterations, but no measured savings support claiming a lower whole-line price yet.

Next evidence: representative batch assays; written toll and scrap bids on identical samples; minimum-lot freight quotations; vendor compatibility trials; itemized installed quotes; incremental residual-management price; and a sustained metered campaign. These decide whether any of the modeled paybacks is achievable.
