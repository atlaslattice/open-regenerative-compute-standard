# ORCS Manufacturing Diversification — Modular Liquid Cooling and Heat Exchanger Platform
**October 31, 2026 | Candidate product, not certified or procured | Evidence-graded proposal**

## Decision
The first **non-transformer** product candidate for common additive/robotic manufacturing lines is **modular liquid-cooling distribution hardware**: replaceable cold plates, 500 kW-class liquid/liquid heat exchanger modules, manifolds and robotically assembled pump/CDU skids. Keep all ratings illustrative until commercially verified. Related product lanes: modular switchgear and power panels, industrial water pumps and electrical motors. An approximately $7B **global** data-center liquid-cooling maker revenue market projected in 2029 cannot alone sustain a million national factory workers: diversify across end markets and track actual orders.

## Current references and independent evidence
- Dell'Oro **Jan 8 2026**: data-center liquid-cooling global factory revenue approaching **$7B/year in 2029**, forecast (not actual U.S. purchase orders). https://www.delloro.com/news/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate/
- UC Davis **Aug 25 2026**: laboratory-validated modular high-power chip cooling using printed electrochemical copper cold plates and low-water modeled architecture; facility performance still a model. https://energy.ucdavis.edu/no-chiller-no-water-no-problem-a-new-way-to-cool-ais-hottest-chips/
- Journal of Heat and Mass Transfer **March 2026** printed topology optimized liquid heat sinks: up to **50% lower pumping power** than a straight-channel comparison in selected tests, **not** 50% less facility electricity. DOI:10.1016/j.ijheatmasstransfer.2025.128106
- HRL Laboratories (ARPA-E COOLERCHIPS) developed **3D-printed manifold** single-phase water-cooling approach. Its comparative thermal/density claims are supplier-reported, not validated nationwide. https://lowchill.hrl.com/
- Phasic company demo: 500kW liquid/liquid **one-piece printed** SS316L heat exchanger, compared with ~180-plate brazed assembly, company reports same duty in matched reference volumes with approach temperature 2.5C vs 3.6C. **Vendor technical claim**; independent tests and qualifying lifetime are needed. https://phasic.com/
- ACT announced expansion of **50k sqft** in Lancaster PA for single/two-phase cold plates in May 2026, real U.S. manufacturing activity, not evidence of nationwide unmet supply. https://www.prnewswire.com/news-releases/act-expands-us-manufacturing-to-scale-cold-plate-production-for-ai-data-center-cooling-302776037.html
- JLL 2026 Global Data Center Outlook notes U.S. data-center equipment average lead time **42 weeks**, but cooling-device categories have different lead times than transformers and switchgear. https://www.jll.com/content/dam/jllcom/en/global/documents/reports/research-reports/26-research-global-data-center-outlook-new.pdf

## Trade and demand by broad HS commodity (Sep 2025-Aug 2026, Census API via CK Economics)
| Broad basket | Imports | Exports | Goods balance | Correct constraint |
|---|---:|---:|---:|---|
| HS8419 thermal-treatment equipment inc. heat-exchange units | $11.4B | $5.3B | -$6.1B | NOT all cooling-CDU heat exchangers |
| HS8413 pumps and parts | $12.8B | $9.2B | -$3.6B | NOT all coolant pumps |
| HS8537 electrical boards/control panels | $24.1B | $9.1B | -$15B | Much broader than distribution-grid switchgear |
| HS8501 electrical motors and generators excluding sets | $13.3B | $5.0B | -$8.3B | Many unrelated end uses |
Sources: https://www.ckeconomics.com/data/trade/products/8419 ; https://www.ckeconomics.com/data/trade/products/8413 ; https://www.ckeconomics.com/data/trade/products/8537 ; https://www.ckeconomics.com/data/trade/products/8501 . **Never call HS import volumes fully addressable data-center markets; verify HTS6/8/10 for target SKUs.**

A time-sensitive, independently reported **switchgear** shortage is also credible: Reuters, Jul 9 2026: U.S. grid/data-center construction demand pressures transformers, circuit breakers, switchgear, some lead times in years. https://www.reuters.com/business/energy/us-power-companies-scramble-secure-equipment-surging-data-center-demand-strains-2026-07-09/ . It is an attractive SECOND product on the panel/electronics line, but its high-voltage safety devices and certified interrupters are not suitable for arbitrary printing.

## 500kW modular CDU product exploration

**Uniform field-replaceable standard interface, not a one-design-fits-every-chip assertion.**
- **Print-first parts:** monolithic liquid/liquid heat exchanger core, manifold geometry, brackets, selectively shaped cold plates and integrated cooling channels if independent pressure/thermal/corrosion testing validates the print method.
- **Use high-throughput conventional where justified:** high-volume plate/fin heat exchangers, commodity tubes, sheet metal cabinets, filters, hose, pumps, motors, valves, seals, connectors, sensors and electronics. Robotically install standard purchased qualified components. No fantasy that a single printer fabricates SiC dies or a complete motor.
- **Candidate flexible production line:** certified recovered Al/Cu/SS316L raw material -> controlled powder/wire/extrusion -> 24/7 automated print/cast/machine operation -> depowder and clean internal passages -> heat treat -> machine/seal contact faces -> robotic assemble with certified pump/valve/connector modules -> hydrostatic proof, leakage/pressure loss, flow curves, thermal approach, endurance, coolant compatibility, electrical grounding -> serial QA trace.
- **Non-print fabrication choice:** brazed plate / machined-channel / stamped fins, evaluated against printed core at **identical** duty, pressure, volume, thermal approach, flow and 10-year life.
- **Site system boundary:** liquid cooling moves heat; **does not erase it**. Track 500kW heat duty, pump electricity, HVAC/water use, dry-cooling performance and heat reuse separately. Full site economizers, redundancies, service and water availability matter.

**Scale illustration only**: if an AI campus has 100 MW of thermal rejection actually served by these **500kW devices**, it requires 200 working modules (plus engineering redundancy and spares). 1GW of heat would require 2,000. No customer orders and no procurement prices assumed.

**Factory reuse:** printing/casting CNC/robot cells and calibrated leak testing share additive machine/tooling/operator skills with ORCS Transformer 3.0, but cooling's pressure, corrosion, microbial cleanliness and service requirements differ from transformer dielectric/fault qualification. Retool with documented machine utilization and worker qualifications.

## Screening and economic gates
1. **Demand** — customer letter of intent + annual needed MW cooling, load profile, cost/kW and order book, eligible domestic procurement and verified service network.
2. **Performance** — identical exchanger duty and rated thermal approach/pressure drop/flow, corrosion/water chemistry, freeze and fatigue, leak cycles, safety, 10-year expected reliability.
3. **Print productivity** — net quality/yield, occupied machine hours/core, material mass and powder recirculation, robot and human labor, depowder time, machining, seals, pressure and flow test cost.
4. **Domestic BOM** — U.S. origin for qualified metallic feedstock, printers, robots, pumps, motors, sealing and sensors; test zero-import ambition as supplier portfolio, not assumed existing fact.
5. **Full plant economics** — conditioned cost per certified kW of cooling and lifecycle pump kWh, inclusive of downtime, field replacement, spare units, throughput and capital amortization.
6. **Training** — task-specific paid AI-assisted supervised factory work, human practical evaluation, powder safety, process QA, pressure systems and water chemistry. Do not invent universal 3–4-year lineworker requirements for factory assembly.
7. **Diversification** — after data-center ramp, qualify products for wastewater, industrial heat recovery, district energy, refrigeration and desalination with verified demand. Do not book future permanent jobs until signed orders/factory conversion are established.

## Status and next step
**Industrial opportunity / sourcing hypothesis.** Obtain three independent quote sets: (A) stamped/brazed/machined baseline, (B) selected additive/robotic assembly, (C) nearly all-additive core. Start same functional 500kW heat exchanger lab proof and robot workcell time study. Compare component tests rather than company marketing claims. Parallel RFQs for automated switchgear panels and industrial pump skids would diversify equipment utilization.
