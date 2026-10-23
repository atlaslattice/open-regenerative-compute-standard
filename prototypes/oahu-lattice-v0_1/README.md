# Oʻahu Atlas Lattice — daily screening model v0.1

```text
STATUS: CANDIDATE / EXECUTED SCREENING SENSITIVITY
CANON: no
DEPLOYMENT: no
AUTHORITY: none
PROOF: no
PUBLIC_RELEASE: reviewed
DATE: 2026-10-23 (America/Chicago)
REALIZED_CREDIT: zero
```

This is the first runnable Oʻahu-specific daily model in this investigation, not the first Atlas landfill concept ever written. It explores current waste screening, conditional fuel and manufacturing outlets, conditional additional reclaimed water, a compute load, and a future desalination hydraulic boundary. It does not establish project feasibility, a supplier recommendation, full-system benefits or ROI.

## Run and inspect

Python 3; standard library only:

```bash
python model.py
python -m unittest -v
```

The model produces seven 365-row daily CSVs and JSON/CSV summaries in `results/`. Published summaries are included; the daily files regenerate locally. Change `inputs.json` to test assumptions. Units are metric tonnes, m³, kWh and USD unless explicitly marked U.S. short tons or MGD. 1 U.S. short ton = 0.90718474 metric tonnes.

## Evidence and boundary

Source URLs, retrieval dates, published anchors, analyst assumptions and unresolved inputs are separated in [inputs.json](inputs.json). A reported design capacity is not available spare capacity. A published program is not an Atlas achievement. This is a prospective one-year sensitivity using 2024 disposal as a reference profile, not a reconstruction of daily 2024 operations or a calendar-2026 forecast.

- City-reported WGSL 2024 disposal: 155,030 U.S. tons other MSW plus 145,029 U.S. tons ash/residue. The separate C&D landfill's 233,835 U.S. tons are excluded from simulated feed and denominator.
- All other-MSW intake is hypothetically eligible for screening; that eligibility, safety review, preparation, contracts and permits are UNVERIFIED. Ash bypasses the unit. Legacy excavation is NOT modeled; the prior 11-million-tonne sensitivity is not a surveyed reserve and is not used.
- Offered feed is evenly distributed over 365 days. There are 300 evenly distributed eight-hour shifts, with 80% assumed availability. Unprocessed same-day incoming feed is disposed; no incoming-feed buffer or overtime is assumed.
- Desen's 50/200 metric t/h cases are planning scenarios, not validated complete-line performance. The price/configuration relationship remains unresolved. A required pre-treatment step, including any size reduction to satisfy manufacturer feed limits, is not supplied by this model.
- Modeled feed fractions, recovery, prices, power, water use, outlets, buffer size and operating allowance are assumptions, not assays, quotes or guarantees.

## Executed example results — assumptions, not forecasts

Rounded values from [results/summary.json](results/summary.json):

| Scenario | Screened metric t/year | Modeled disposal avoided, metric t/year | Share of WGSL reference disposal |
|---|---:|---:|---:|
| Incumbent reference | 0 | 0 incremental | 0% incremental |
| 50 t/h, assumed accepted metals only | 96,000 | 1,805 | 0.66% |
| 200 t/h, assumed accepted metals only | 115,595 | 2,173 | 0.80% |
| Conditional 50 t/h integrated outlets | 96,000 | 39,917 | 14.66% |
| Conditional 200 t/h integrated outlets | 115,595 | 48,064 | 17.66% |
| Conditional 200 t/h + outage stress | 115,595 | 46,409 | 17.05% |
| Future conditional 200 t/h + desal online | 115,595 | 48,064 | 17.66% |

Why these differ from the earlier arithmetic: earlier examples assumed enough material to fill every operating shift and swept net diversion yields. This version caps daily processing at offered current other-MSW intake. A large machine cannot manufacture feed, and screening is not diversion. Legacy campaigns, feed storage, more shifts or other authorized feed streams require explicit additional scenarios.

The conditional integrated cases assume: 80% acceptance of a 55%-by-mass combustible fraction, 200 metric t/day of additional H-POWER receiving capacity, 20% fuel ash returned to disposal, and 2,000 tonnes of allowable fuel storage. They also assume 25% of the mineral/fines fraction qualifies for manufacturing and that 90% of this qualified input becomes accepted product, limited by an assumed 50 t/day input capacity. NONE of these are established Oʻahu acceptance conditions. The stress case adds a 30-day H-POWER outage and a 10-day reclaimed-water outage. It does not simulate additional raw-MSW arrivals caused by that H-POWER outage, so it is a limited dependency test, not island-wide outage resilience analysis.

The model closes tracked waste-origin mass daily. Combustion non-ash mass leaves this solids ledger, not the environment: emissions, oxygen, moisture and carbon chemistry are NOT modeled. New H-POWER ash is explicitly returned to disposal. End-of-year fuel inventory is reserved as a disposal liability, never counted as diversion. This is a mass screen; net permitted landfill airspace stays UNKNOWN without excavation, reburial, cover and density measurements.

## Financial boundary

The user-provided $2,800/operating-day allowance is not an all-in cost quote. Metal netbacks are illustrative: $243/t ferrous and $1,500/t blended nonferrous, with assumed recovery and buyer acceptance. The partial metal-netback-minus-allowance balance is approximately -$63,552/year at 50 t/h and +$94,934/year at 200 t/h. These are NOT profit estimates or evidence of break-even. They exclude unspecified capex, mobilization, disposal, additional process costs, environmental management, finance, water/power costs and other omitted items. No RDF, aggregate, water, carbon, resilience or AI revenue is invented. Integrated cases have extra costs that remain unpriced. Full profit, payback and ROI remain `null`.

## Water, brine, agriculture and compute

- Honouliuli's published 12-MGD recycling design is baseline infrastructure. Conditional cases assume only 100 m³/day of ADDITIONAL available reclaimed water, not the whole design capacity. Dust control has first priority; the balance serves an assumed existing irrigation demand. Landfill water and agricultural water are kept separate; no landfill washwater is applied to crops. No food-yield or import-displacement benefit is inferred.
- Kalaeloa is NOT online. The developer's October 21 SEC exhibit expects construction in H1 2027. Only the explicitly future case assumes 1.7 MGD product output all year. At an assumed 45% recovery and 4 kWh/product-m³, it gives about 2.35 million m³/year product, 2.87 million m³/year concentrate and 9.40 GWh/year desal energy. These are hydraulic/energy sensitivities, not the plant's guaranteed recovery or SEC. It is not a commissioning-year forecast. Well-water and concentrate assays are missing, so no Mg, gypsum, salt or trace-product tonnes/revenue are assigned.
- Organics composting, existing wastewater treatment and Honouliuli gas recovery are incumbent pathways. Their tonnages and benefits are not assigned anew to Atlas. Incremental digestion, nutrient recovery and crop responses remain uncalibrated interfaces in [couplings.csv](couplings.csv).
- The integrated example adds an assumed continuous 10-kW data/AI load (87.6 MWh/year), with no automatic energy savings or service-value credit. The model runs deterministic routing and state updates; it does not train a neural network, implement online learning or recreate Atlas Prime. The corpus/knowledge layer should retrieve evidence and propose scenarios; validated physical calculations remain independently inspectable.
- Local repair, additive manufacturing of spare parts, industrial reagents, refined metals and qualified polymer products are tracked as candidate interfaces; no manufacturing yield, certified part, uptime improvement or import offset is invented beyond the explicitly conditional mineral-product example.

## How this tests integration

This version demonstrates state propagation: receiving outages alter storage and disposal, manufacturing acceptance bounds outputs, dust water competes with irrigation for a bounded new supply, compute adds a burden, and later desal adds both product water and a concentrate liability. It is a small coupled process model, not a complete twelve-layer evaluator or a claim that a neural architecture is necessary. The current routing policy is fixed; adaptive dispatch is a next experiment against this reproducible benchmark.

Next calibration priorities: measured feed characterization and authorized streams; supplier model/configuration and sustained trial; buyer specifications and delivered prices; H-POWER actual acceptance, time profile and capacity; full handling/residual cost; water commitments, connection costs and crop demand; source-well/concentrate assays; actual industrial-input and fabrication demand; ecological baseline and local community evaluation design.

All physical benefit claims remain UNRESOLVED. Software validation does not clear site permits, product acceptance or ecological gates.

## Execution receipt

Executed `python model.py` and `python -m unittest -v` on October 23, 2026. Nine tests passed: conservation and end-inventory liability, exact shift schedule, loss of metal outlets, loss of fuel acceptance, outage blocking, bounded water/manufacturing, future water balance and invalid composition rejection. This tests implementation logic, not real-world performance.

## Related work

- [Commercial recovery research and RFI](../../research/shreddernaut/hawaii-commercial-recovery-2026-10-23/README.md)
- [WED / cross-site methodological bridge](../../research/2026-10-23-wed-dongjiakou-corpus-maui-oahu-crosswalk.md)
- [SolBrain continuity archive](https://github.com/atlaslattice/manus-artifacts/tree/master/archive/boot/gptbrain/SolBrain)

The existing source archive and all earlier scenarios remain intact. Notion can contain fuller originals than GitHub mirror stubs.
