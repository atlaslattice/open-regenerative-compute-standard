# Shreddernaut Dry Recovery Prototype v0.2

> **October 23, 2026 update:** The [Hawaiʻi commercial recovery research package](../hawaii-commercial-recovery-2026-10-23/README.md) moves the proposed next step toward deploying and characterizing commercial equipment, with purchase preferred if scope, price and performance are validated. This earlier 20-tonne/day package remains a historical proposed design and synthetic model; it is not a production-capacity limit. See the new package for the supplier RFI, attributed DeepSeek claims, explicit corrections and land-preservation comparison.

2026-10-20 | PROPOSED design / EXECUTABLE screening model / NOT hardware-validated

## Purpose
A relocatable 20 metric tonne/day sorting and concentration pilot supplies existing domestic scrap processors, specialist electronics/battery recyclers and, where specifications permit, mills/refineries. Start with leased conventional equipment at an existing permitted host. Onboard plastic washing, drying and pelletizing are omitted. Bulk shredding is also omitted from the first configuration; size reduction is added only after demonstrated buyer need and hazard review.

This package implements the next research step from the [v0.1 white paper](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/main/research/shreddernaut/2026-10-20-shreddernaut-20tpd-energy-materials-whitepaper-v0.1.md). It does not establish manufacturing cost, grant eligibility, site permission, deployment or commodity acceptance. All example model inputs are synthetic. Funders and prospective buyers listed in FUNDING_AND_PARTNERS.md have not endorsed or joined this project.

## Prototype boundary and sequence

1. Host supplies permitted receiving area, controlled working surface, loader/excavator, drainage/leachate management, power and lawful residual destination. Availability must be established, not assumed free.
2. Weigh and identify batches; maintain separate source-separated and legacy excavation trials.
3. Trained personnel isolate batteries, electronics, cylinders, drums and suspect materials before mechanical processing. Unknown hazards stop the batch. An excavator is not a method for certifying safe feed.
4. Feed hopper and metering conveyor with guarded inspection station; coarse screen removes oversize items for separate handling.
5. Size screening separates fines from coarser material. Screen aperture and moisture envelope are trial variables. Both fines and coarse fractions need metals assays; screening is not decontamination.
6. Magnets recover ferrous material; eddy-current separation acts on appropriately sized nonmagnetic fractions after ferrous removal. Dirty, wet, entangled or fine material may require different equipment or offsite treatment.
7. Inspect and grade output; record contamination, metal content and buyer acceptance. Ship only approved grades in labeled bins. A scrap processor will often be the first buyer rather than a refinery accepting mixed concentrates directly.
8. Fines, unrecovered materials and quarantined hazards remain individually tracked through their approved management routes. No agriculture, soil or construction reuse is assumed.

Transport as separate trailer/skid modules plus bins and site equipment. A container can house controls, tools and telemetry; the complete plant is not claimed to fit inside one 40-foot container. Required footprint, trailer weights, turning access, foundations and electrical/fire design need vendor layouts and professional engineering.

## Functional procurement requirements (proposals)

| Module | Requirement for vendor response | Acceptance evidence |
|---|---|---|
| Feeding/inspection | Net 20 t/day with actual bulk density, moisture and oversize envelope | Weighed sustained trial, documented stoppages and safe access |
| Screening | Adjustable size cuts; access for wet-feed blockage clearing under isolation | Mass/size balance and contaminants by fraction |
| Ferrous separation | Target capture and product grade independently measured | Input/output assay and buyer deductions |
| Nonferrous separation | Representative feed trial by size class | Accepted commodity shipments, not detector accuracy alone |
| Controls/power | Interlocks, emergency stops, lockout provisions and stage metering | Qualified commissioning and metered operating/idle loads |
| Dust/water/fire | Site-specific engineered controls | Host/regulator acceptance and inspection |
| Output logistics | Labeled bins, grade segregation, shipment custody | Written buyer specifications and settlement receipts |

One 8-hour shift needs 2.5 t/hour net average. At an assumed 80% within-shift availability, operating throughput must exceed 3.125 t/hour on full-feed stages. Model defaults of 5 t/hour and 80% availability are synthetic, not equipment guarantees. A four-person crew is also only a cost scenario, not a staffing/safety determination.

## Run the model

Python 3; no third-party dependencies:

```bash
python3 model.py example.json --output results.json
python3 verify.py
```

The model reconciles each material into buyer-accepted output and managed residual; calculates stage electricity, separately reports mobile-equipment diesel, checks assumed capacity, and calculates a break-even contracted service fee. Product net prices must already subtract offsite freight, treatment/refining charges and buyer deductions. Fines can be counted as accepted output only after an authorized use and acceptance are established; acceptance can still have a zero net price.

The example uses a same-basis wet incoming mass balance with no drying or moisture loss. Feed composition, capture and buyer acceptance are separate inputs. Purity is an external assay/contract requirement, not something this simple model predicts. Residual costs must cover actual disposal/treatment and transport. Purchased capital excludes equipment already in the rental charge; fixed costs include insurance, permitting, testing and utility demand charges as applicable. Site acquisition, groundwater treatment, financing fees/taxes, escalation, ramp-up and restoration are not independently calculated: add allowances or a dedicated project model before investment. Do not treat these missing scopes as zero-cost real work.

The synthetic legacy-waste example produces 0.576 t/day accepted metals (2.88% of intake), 203.6 kWh/day sorting electricity plus 20 L/day diesel, and a roughly $138/t break-even service fee after annualized capital recovery. These figures demonstrate arithmetic only. They are NOT measured energy, market quotations or an estimate of the proposed system's costs. In particular the 203.6 kWh/day figure must not replace the retired full-chain energy claim as a new performance promise.

The example fails a scrap-sales-only business case under its assumptions. Low-cost replication must be earned through trials, shared crews/host assets, higher utilization, higher-grade feed and reduced residual costs. Compare a larger regional line against thousands of small lines. Grants support development; they are not recurring product revenue.

## National stock and deployment

The 2016 [Waste Informatics study](https://pubmed.ncbi.nlm.nih.gov/27651028/) estimated 8.5 billion metric tonnes of U.S. municipal waste stocks. The 10 billion tonnes in example.json is a rounded planning assumption, not a current national census. Equal division gives 200 million tonnes per state and is not a claim of equal actual distribution.

At achieved 20 t/day and 300 days/year, annual throughput is 6,000 t/unit. A fleet of 50,000 units processes the assumed legacy stock once in 33.3 years; a 30-year target needs 55,556 units nationally before ramp-up. New waste, repeat processing, downstream bottlenecks and restoration are excluded. Processing is not complete remediation. National output multiplication is a sensitivity calculation, not a reserve or import-displacement estimate. Grade-adjusted domestic offtake must be measured before substitution can be booked.

## Two pilots, different evidence

A. Source-separated/bulky waste at a collection or recycling site: establish safe operations, product quality, power and genuine logistics costs on fresh feed. This is the priority first host route.

B. Separately permitted legacy-waste campaign: characterize cells, moisture, contamination, excavation stability and gas/leachate implications; establish accepted fractions and lawful residual routes. A's results do not validate B's yields or economics.

## Proposed execution sequence (time allowances, not promises)

- Days 0–30: confirm applicant/operator, public host and process boundary; obtain representative samples and buyer specifications; map permits and liability; request rental/vendor quotes. Gate: legal site access and documented scope.
- Days 31–60, only after approvals: temporary leased line and representative batch trials. Gate: reconciled weights, qualified controls, accepted shipment and actual labor/power/residual costs.
- Days 61–90 or longer as needed: sustained 20 t/day campaign and independent technical/economic review. Gate: safe throughput, acceptable mass closure agreed with reviewer, paid shipments and a funded service contract or demonstrated margin.
- Replicate at a second unlike site before proposing fleet procurement. Decide whether a 100–500 t/day regional line wins on costs; those capacities remain alternatives for study, not verified designs.

## Quote and partner request packet

For hosts: feed source and annual tonnage, cell/site records, existing permits, surface/drainage/utilities, available equipment, fees and residual destinations.
For equipment vendors: sample envelope, required throughput, rental/purchase/maintenance terms, connected and measured power, trial plan, controls and transport layout.
For buyers: exact grades, contamination/moisture limits, required size, minimum lot, available receiving capacity, freight responsibility, rejection terms and settlement formula. Damaged/unknown batteries and contaminated electronics need express specialist acceptance.
For funding sponsors: eligible legal entity, scope and innovation, work packages, itemized quotes, match sources, procurement route and measurable outcomes. Do not charge the same equipment/hour to two awards. No applications or communications are submitted by this package.

## Evidence upgrades required

Every synthetic input should be replaced with site records, vendor quotes, meters, laboratory results or buyer settlements. Preserve the v0.1 documents and current SolBrain pointers. Never reclassify this model as an operating prototype or verified remediation result.
