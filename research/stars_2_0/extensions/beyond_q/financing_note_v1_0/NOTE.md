# Beyond Q: whole-campus financing sensitivity v1.0

Prepared 2026-11-01. Research direction: Dave / Atlas Lattice. Financing and market-price inputs explicitly supplied by the originator. Calculation implementation: GPT Work. Prior analytical contributions by GPT-6, DeepSeek and Gemini Argon remain attributed to their respective review records. No institutional endorsement or experimental validation is implied.

## Purpose and limits

Evaluate the integrated D-D isotope factory / D-T power plant / optional GPU or QPU campus over a financing horizon, rather than require A to sell electricity independently. Grid-powered A remains a separate comparison. This note adds financial sensitivities without changing earlier physical scenarios or their assumed 90% capture input. The newly preferred 75% overall recovery has NOT been silently substituted into the dynamic model. Source birth, plasma survival, capture and qualification must remain distinct.

Long-term fuel-cycle autonomy, electrical autonomy, isotope surplus and commercial profitability are separate acceptance criteria. The proposed 1.10 GW D-D operating point and its whole-plant electrical output are unresolved. B's public ARC comparator is about 400 MWe net for its published D-T design, not a demonstrated 400 MWe output of this campus. Neither 500 MWe campus availability nor perpetual component life is established.

Continued operation requires deuterium and, with B's lithium blanket, consumed lithium feedstock or an explicit replacement tritium source. Components, coolant, maintenance and heat rejection remain necessary. Dilution refrigerators already recirculate their He3/He4 working fluid; alternatives must not be categorized wholesale as once-through consumption systems.

## Financing convention

30 annual end-of-year, level debt-service payments; nominal 5% fixed annual interest; 100% of scenario capital financed. Principal C gives annual payment C * r / [1-(1+r)^(-30)]. Capital recovery factor = 0.06505143508027657. This assumes financing at operations start; construction interest, fees, equity, taxes, inflation, decommissioning, working capital and replacement financing are not included. The 5% rate is a user scenario, not a lender offer.

| Financed capital | Annual debt service |
|---|---:|
| Historical corrected ledger: $5.67B | $368.842M |
| Alternate two-chassis + gross adaptation: $5.90B | $383.803M |
| Stress case: $8B | $520.411M |
| Stress case: $12B | $780.617M |

Historical local source: ../reserve_dispatch_v1_8/sources/ARC_CANONICAL_2026-10-31.md. The $5.67B value sums $2.8B + $2.8B + $150M - $200M + $120M. The previously written $5.87B is preserved there as an arithmetic discrepancy. $5.90B uses the same assumed chassis values plus the originator's approximate $300M adaptation, without turbine credits. These are alternative unreconciled scopes, not independent vendor quotes or additive estimates. Potential overlap between adaptation and separation equipment remains unresolved. Stress cases are not estimates.

## Market-price correction scenarios

Assumed He3 price: $1,500 per gaseous STP liter (0 C, 1 atm). Assumed T price: $1,500 per gram = $1.5M/kg. Neither is a firm offtake quote or equilibrium price forecast. Sellable quantities require independent qualification and buyer demand. No internal allocation is also sold.

350,000 L/year qualified He3 SOLD gives $525M gross annual revenue. If total captured He3 is 350,000 L and 50% is retained internally, the maximum sale allocation before further qualification losses is 175,000 L, or $262.5M gross revenue. Five kilograms of qualified EXPORT tritium adds $7.5M; 20 kg adds $30M. These export masses are financial sensitivities, NOT qualified surplus predictions from the dynamic model. Gross T births, stock growth and B breeding do not automatically qualify for sale. He4 revenue remains uncredited pending purity, availability and price evidence.

At $5.67B financing, 350,000 L qualified He3 sales and 20 kg qualified T exports produce $186.158M/year after initial debt service BEFORE all operating costs, replacement allowances, tax and other financing. This is not profit. With 175,000 L sales, the corresponding result is -$76.342M/year before those costs. Electricity or compute contribution must be evaluated separately.

## Electricity and compute boundary

P_site_available = P_B_net + P_A_net - incremental_shared_processing_and_site_load. Ensure A/B net definitions include each plant's own auxiliaries, and subtract common loads only once. P_IT = P_site_available / PUE if available power is at the facility boundary. Annual energy also requires the operating schedule and any grid exchanges. Do not assume that 400 MW plant export equals 400 MW GPU chip load.

Example only: B net 400 MWe, A net draw 100 MWe and zero additional shared load gives 300 MWe facility power; PUE 1.2 gives 250 MW IT. These are independent sensitivity assumptions, not an established A draw or site PUE.

IREN's 2026 primary announcements provide a contemporary gross revenue comparison: a $3.4B five-year managed GPU services agreement serviced within approximately 60 MW of existing data centers, giving an undiscounted contract-average ~$680M/year or ~$11.33M per stated MW-year. Do not equate this boundary with GPU-only or IT MW without reconciliation. A separate approximately $1.6B Dell equipment purchase supports that deployment. Scaling these figures to Beyond Q is an extrapolation, not a profit prediction. GPUs, networking, buildings, refresh, software, staff, utilization, service obligations and financing remain separate from the reactor hardware loan. Historical or 2026 GPU contract prices are not assumed to persist for 30 years.

Compute revenue includes the use of internal electricity: do not also book an external electricity sale for those same MWh. Campus consolidated cash flow = external isotope receipts + compute receipts + actual grid export receipts - grid imports - all operating costs - replacement capital - debt service - cash taxes. Avoid depreciation plus the same capital expenditure as duplicate cash charges; accounting net income is a separate output. Internal isotope allocation may have a documented avoided-purchase benefit, but cannot simultaneously generate external sales receipts.

## After the initial 30-year loan

Debt service on that loan becomes zero only if it is fully repaid. It improves cash flow by that loan's payment, all else equal; it does not eliminate maintenance, vessel replacement, refurbishment, isotope processing, GPU refresh or new debt. A 30-year viable service life and post-payoff margin are open research questions. Actual net profit remains null in results.json until operating, replacement, site and compute costs are supplied.

## Existing-campus addition and reactor housing scope

Originator clarification, 2026-11-01: evaluate the two-reactor/isotope package as an addition to an existing or independently financed compute campus, including a Stargate-type campus as a conceptual example. This does not assert a partnership, permission, site suitability, available capacity or an approved integration plan. GPU financing remains a separate ledger.

The reactor project must explicitly account for BOTH A and B housing and supporting site works: reactor buildings and foundations; shielding and confinement provisions; maintenance/hot-cell and component-handling facilities; isotope processing and storage buildings; electrical switchgear and campus/grid interconnection; heat-rejection and cooling infrastructure; civil works, installation, engineering and contingency. Costs and dimensions remain unresolved until supported by scope-specific evidence. Shared facilities are allocated once, not charged in full to both plants.

Before adding housing/site allowances, reconcile each historical chassis estimate's installed scope. If an estimate already contains a building or balance-of-plant item, disclose its allocation rather than adding that item again. The earlier $5.67B/$5.90B examples are NOT established complete installed campus budgets. No new housing allowance has been invented or silently embedded in those examples.

Report three separate ledgers: (1) reactor/isotope project capital, financing, operating costs and external receipts; (2) compute-campus GPU/server/network capital, financing, refresh and compute receipts; (3) consolidated campus cash flow, eliminating internal electricity/isotope charges. For a separately owned existing campus, an electricity supply contract can be real reactor revenue and real campus expense; it cancels only in consolidated reporting. Incremental compute revenue requires evidence of additional contracted throughput; it is not automatically attributable to replacing the site's electricity supplier.

Footprint comparison must include the complete installed reactor/isotope package: buildings, maintenance access, cooling/heat rejection, electrical equipment, storage, required separation and construction space. Tokamak size alone is not site area. Compact integration is a design objective; relatively minimal footprint is not yet a quantified result. Existing-campus power, cooling, civil and transmission capacity can reduce incremental scope only when demonstrably reusable without double counting.

## Sources retrieved 2026-11-01

- CFS, ARC overview: https://cfs.energy/technology/arc/ . Public approximately 400 MWe design comparator; not the D-D retrofit or a capital quotation.
- CFS, How LIBRTI will help CFS verify our fusion fuel production technology, July 1 2026: https://blog.cfs.energy/how-librti-will-help-cfs-verify-our-fusion-fuel-production-technology/ . Breeding/extraction research remains relevant to fuel autonomy.
- IREN, IREN Secures $3.4bn AI Cloud Contract with NVIDIA, May 7 2026: https://irisenergy.gcs-web.com/news-releases/news-release-details/iren-secures-34bn-ai-cloud-contract-nvidia . Contract value, duration and stated 60 MW deployment scope.
- IREN, IREN Targets $4.4bn in ARR with Blackwell Deployment at Childress, May 26 2026: https://iren.gcs-web.com/news-releases/news-release-details/iren-targets-44bn-arr-blackwell-deployment-childress . Approximately $1.6B Dell equipment scope and deployment plan.
- IREN, FY26 results, August 27 2026: https://iren.gcs-web.com/news-releases/news-release-details/iren-reports-fy26-results . Reports recent contracts above $20M per IT MW; a different boundary/product mix from the simple contract average above, not a universal margin.
- Bluefors, dilution refrigerator systems: https://bluefors.com/products/dilution-refrigerator-measurement-systems/ . Closed-loop He3/He4 cooling.

## Evidence labels and reproduction

SOURCE-TRACED: cited design and commercial announcements (not independently validated performance). VERIFIED-DERIVED: loan arithmetic and explicit price-times-quantity calculations. POTENTIAL-DERIVED: scenario revenues and extrapolations. UNRESOLVED: reactor performance, qualified sale volumes, full CAPEX/OPEX, long-term prices, compute margin and actual profit.

Run `python calculate.py` with Python 3; results.json is regenerated. Internal checks verify the amortized residual and zero-interest boundary. These software checks provide no reactor validation. No prior release is overwritten. This local note has not been committed or published to GitHub.
