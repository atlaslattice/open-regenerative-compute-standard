# What the15% figure actually means — and v0.4 review response

24 October 2026 • Atlas Lattice research • No procurement estimate or verified profitability.

## Correct interpretation of the Corpus budget

The historical2025 table labels one line **process equipment**. It does not divide the whole project into equipment versus labor/admin. Other categories include physical assets, construction labor, installation and other costs. Their internal splits are not reported.

| Grouped construction scope | USD million | Share |
|---|---:|---:|
| Named process-equipment line | 154.13 | 15.45% |
| Other physical works: marine, civil, structural, plant piping, electrical/instrumentation, buildings, product pipeline, pump/storage | 674.30 | 67.61% |
| Escalation, contingency, bonds/insurance, general conditions | 168.86 | 16.93% |
| Construction total | 997.29 | 100% |

Planning/design/admin is a separate $192.13m category, bringing that broader historical boundary to $1,189.42m. It includes technical engineering and other services; it is not all administrative waste. These are the2025 source categories, not the2026 GMP. [CC25DETAIL]

**Making only the named process-equipment line free reduces this historical construction total by15.45%. It does not imply that85% is labor/admin or that all hardware/design-related savings are capped at15.45%.** Halving that line produces the familiar7.73% reduction. That is a narrowly defined line-item sensitivity. Even this line's supply-versus-installation boundary needs confirmation; halving it is not a verified vendor-price opportunity.

A different integrated design could also change piping, structural loads, buildings, electrical systems, intake works, installation effort and schedule. Those opportunities need quantities, duty, code-compliant alternatives and quotations. The cost table neither proves such savings nor rules them out. It also does not identify a pure labor total or support ranking governance as the dominant cause of the China/U.S. gap.

The appropriate challenge is a **complete functional-scope comparison**: factory scope, shipping, site works, American installation, distribution, performance guarantees and residual closure. Avoid comparing bare equipment prices with fully installed categories. Request labor-hours/rates, material quantities/unit prices, equipment scope, overhead/profit, contingency, schedule and risk allocation separately. No displayed budget is assumed efficient simply because it has a line item.

## Suggestion1: Dongjiakou cost categories

The original matched equipment/civil/labor allocation was **not located in the reviewed public sources**. The cells remain numeric null, with an explicit status column explaining why. This is not a declaration that no public breakdown exists. `dongjiakou_search_status.csv` records the gap and the needed original feasibility/EPC/BOQ/completion-account records.

New primary evidence provides a **separate later intake project**, not a substitute original-build breakdown: a2025 notice identifies a selected consortium bid of ¥85.696m for1565m of intake relocation. Its tender lists ¥158.81m total project investment and a ¥102.023m construction ceiling. It serves an840,000t/day intake design supporting a planned300,000t/day desalination scale. [DJKINTAKE25; DJKINTAKETENDER25]

These prices and scopes stay separate from the historic ¥450m/¥650m100,000m³/day reference. They are not added to it, used to fill its original intake cost, or normalized against the Corpus line without a common engineering boundary. They demonstrate that public physical-infrastructure pricing can be located beyond membrane replacement notices.

## Suggestion2: Sourceable fraction

`equipment_leverage.csv` now explicitly retains `internationally_sourceable_fraction=null` and unknown actual savings. `equipment_sourcing_sensitivity.csv` tests assumed fractions0/25/50/75/100%, applied to an assumed50% net price reduction in the named line.

At40% and60% hypothetical addressability, the arithmetic would give3.09% and4.64% of historical construction, respectively. This is not an estimated achievable range. National import-dependence and patent percentages do not establish this project's bill of materials, legal eligibility, competing bids, supplier manufacturing location or net landed savings. A Chinese-integrated plant may use U.S./European components; that is a procurement choice to price, not an automatic exclusion.

## Suggestion3: Explicit margin-to-price bridge

`discount_horizon_sensitivity.csv` adds `implied_selling_price_usd_t` and the cost basis. **$623.58/t is a conditional bridge**, obtained by adding the independent$150/t net-contribution assumption to the specific illustrative$473.58/t full-sales recovery cost. It is not a unique price implied by a free-standing margin assumption or a market quotation.

That recovery cost uses assumed$50m module CAPEX,$5m/year fixed OPEX,$400/t variable cost,6%/20-year capital recovery and full modeled sales, before shared final residual costs. Change any of those and the price bridge changes. A hypothetical$500/t sale price gives roughly$26.42/t contribution on that same cost basis only; it is not an observed project margin. The claims register retains both limitations. The levelized break-even and net-contribution views remain alternatives and are not added together.

## Suggestion4: Separate chloride summaries and route rows

`chloride_scenario_summary.csv` has one row per scenario with total consumption and residuals. `chloride_allocation_sensitivity.csv` now contains route-level quantities only. Final residual totals are not repeated in route rows. The split scenario's three allocations can be summed; the one scenario residual is then read once from the summary. Both tables remain theoretical inventory calculations, not accepted products.

## Suggestion5: External chloride references

`external_chloride_screening.csv` provides FAO screening categories: surface-irrigation chloride below4,4–10 and above10meq/L; the sprinkler boundary is3meq/L. Converted chloride concentrations are approximately142,355 and106mg/L, respectively. These are crop/method/context guidelines, not universal pass/fail limits or permission to discharge saline irrigation drainage. Other salts, soil, crops, climate and drainage still matter. [FAO29]

For construction, the register points to ASTM C1602 for mixing water, ACI318 for the applicable concrete mixture/exposure requirements, and ASTM C1218 for water-soluble chloride testing. ASTM C33 remains an aggregate-qualification reference; the claim that its designation alone supplies a universal recycled-aggregate chloride limit is not adopted. Confirm the edition adopted by the project and responsible engineer. NRMCA's2026 guidance describes C1602's optional chemical limits and use-specific application. [NRMCA26; ACI_CRC94]

External references have their own columns; actual measurements, adopted buyer limits and approvals remain unresolved. A screening category does not automatically activate or clear the project's acceptance gate.

## Suggestion6: External disposal costs, without inventing a fallback

`external_disposal_benchmarks.csv` converts a primary Argonne2005–2006 survey of produced-water injection fees,$0.30–10/bbl, to approximately$1.89–62.90/m³ **in those historical survey dollars**. It is a different waste stream/regulatory context, excludes transport and is not a current desalination-brine quotation. It does not establish a current minimum or maximum cost for Corpus. [ANL2006]

The Bureau of Reclamation's2006 report also supplies a historical deep-well capital example of$4.497m, on2001 cost curves, excluding pretreatment and pump. A capital example is not an all-in$/m³ gate fee. Its Florida-based geology and pressure assumptions are not established for Corpus. [USBR123]

Fallback tables link to these external references while keeping every actual facility, accepted chemistry, capacity, fee and permit unconfirmed. Historical E&P facilities are not presumed authorized to take desalination residuals. A shipping quote also needs chemical classification, density, payload, packaging and receiving capacity; a container freight headline cannot be silently converted to a bulk-brine treatment cost.

The benchmark provides context; it does **not** turn the executable downside case from unknown into known. That requires an applicable receiver/design and quote. No external benchmark clears the no-routine-marine-process-discharge gate or enters the operator cash baseline as an actual fee.

## Attachments for independent review

Start with `results/historical_construction_groups.csv`, `cost_category_alignment.csv`, `dongjiakou_search_status.csv`, `results/equipment_sourcing_sensitivity.csv`, `results/discount_horizon_sensitivity.csv`, the two chloride output tables, `external_chloride_screening.csv`, and `results/external_disposal_benchmarks.csv`. Remaining tables preserve the prior recovery and twelve-domain registers.

Thirty-five software tests pass. **Passing software tests validates bookkeeping, not treatment performance.** All-in costs, actual sales, original matched Dongjiakou categories and final residual routes remain unresolved.
