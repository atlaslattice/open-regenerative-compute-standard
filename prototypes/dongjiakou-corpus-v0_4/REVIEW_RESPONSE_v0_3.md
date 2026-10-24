# v0.3 reviewer response and attachment guide

24 October 2026 • Research screening, not an executable procurement budget.

The tables are supplied directly for inspection. Empty CSV fields mean unknown/not supplied, not zero. JSON nulls retain the same meaning. Scenario numbers explicitly labeled assumed are neither quotations nor measured results.

## 1. Equipment savings as a percentage

`results/equipment_leverage.csv` computes the narrow price-reduction test requested by the reviewer, on **matched July2025 scope**:

| Boundary | Process-equipment share | Total reduction if this line is halved |
|---|---:|---:|
| Construction total | 15.45% | 7.73% |
| Construction plus planning/design/admin | 12.96% | 6.48% |

The underlying process-equipment amount is $154.13m. These are historical categories, not a breakdown of the2026 $978.77m GMP. Source CC25DETAIL was downloaded and visually checked; see the cost hierarchy CSV. The $542.96m claim remains unverified. The broad treatment category includes equipment; it is not labor alone.

A single-digit result limits the savings demonstrated by **halving one equipment line**. It does not establish that adapting a different whole-plant design, simplifying buildings/piping, changing intake, or procurement scope has no leverage. Those require engineering quantities and separate proof. Other categories can contain internationally sourceable components; their foreign/domestic split is unknown. The raw13.89×/9.61× comparison remains only a screening signal.

## 2. Break-even before long-horizon claims

`results/mineral_break_even_sensitivity.csv` now states the required product price as:

variable cost per sold tonne + (annualized recovery CAPEX + fixed OPEX + allocated shared residual cost − net coproduct contribution) / sold tonnes.

Actual inputs and actual break-even remain null. The illustrative grid assumes $50m module CAPEX, $5m/year fixed OPEX, $400/t variable cost,6% capital recovery over20years, and sales of25/50/75/100% of the modeled annual Mg(OH)2 quantity. Shared residual-cost scenarios are $0/$10m/$25m per year. Zero here explicitly excludes that shared obligation; it is not evidence that disposal is free.

At full modeled sales, illustrative break-even prices are approximately $474/t before shared residual costs, $552/t with $10m/year allocated, and $670/t with $25m/year allocated. At50% sales, the corresponding values are $547/$704/$940 per tonne. No market quotation or validated production cost supports these assumed inputs; replace them with quotes and buyer capacity.

`results/discount_horizon_sensitivity.csv` separately tests3/6/10% discount rates and10/20/30-year horizons. No terminal value is included. A constant30-year annuity at6% receives about53.5% of its present value from the first10years, so the assertion that most NPV necessarily comes from distant years is not generally true. Price paths, ramp-up and financing still require analysis. Actual recovery CAPEX/variable costs must not be charged again on a net-margin series that already deducts them: the break-even grid and the prior net-margin grid are **alternative views, not additive benefits**.

## 3. Fallback is still unquoted

`fallback_pricing_status.csv` says **NO QUOTE** for every proposed route. No named receiver, accepted chemistry, capacity or fee has been established. `residual_routes.csv` retains those open fields. No order-of-magnitude shipping or gate fee is invented. Geographic arguments from Hawaiʻi do not establish a Corpus permit or price.

A viable no-ocean configuration still requires a qualified route, capacity and operational containment, including feed stop if those conditions are unavailable. This is a procurement dependency, not a priced or approved fallback.

## 4. Two different chloride constraints

The earlier `test_chloride_limiting_inventory` checks **stoichiometric inventory conservation**: one chloride inventory cannot feed unlimited NaCl/KCl/MgCl2 products. It does not test construction safety, crop response or buyer acceptance.

`chloride_acceptance_gates.csv` now separately records use-specific analysis, units, documented specification and other tests. No universal chloride threshold is invented. A declared maximum exceeded means failure for that use; passing it alone does not approve a product. In NaCl, chloride is a desired constituent; purity includes unwanted ions and other contaminants. For water or building materials, chloride may instead be a limiting constituent.

## 5. Chloride is a resource candidate

`chloride_pathways.csv` adds salt recovery, bipolar-membrane acid/base production, chlor-alkali, other chloride salts and qualified construction incorporation. Separation-only operations retain their concentrated or regeneration residuals.

`results/chloride_allocation_sensitivity.csv` allocates only the Na/Cl remaining after the hydroxide/gypsum scenario. Each alternative competes for that same inventory. It displays pure-active theoretical quantities, not solution volumes, saleable tonnes, current yield or product value. An explicit internal-acid-return case prevents reagent reuse being miscounted as chloride destruction. Other ions and the bulk-water obligation remain outside that stage model.

## Attachments to inspect first

1. `cost_category_alignment.csv` and `results/equipment_leverage.csv`
2. `results/mineral_break_even_sensitivity.csv` and `results/discount_horizon_sensitivity.csv`
3. `fallback_pricing_status.csv` and `residual_routes.csv`
4. `chloride_pathways.csv`, `chloride_acceptance_gates.csv`, and `results/chloride_allocation_sensitivity.csv`
5. `resource_status.csv` and `RESIDUE_POLICY_AND_CHLORIDE.md`

Twenty-eight software tests cover the new arithmetic and gates. **Passing software tests validates bookkeeping, not treatment performance.** There are no confirmed product sales, downstream receiver quotes or realized environmental credits.
