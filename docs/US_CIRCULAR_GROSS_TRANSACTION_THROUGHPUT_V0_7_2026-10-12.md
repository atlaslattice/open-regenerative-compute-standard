# Circular economy: unrestricted transaction throughput and production flows — v0.7
**October 12, 2026 · SIMULATED / DERIVED / REPORTED / UNKNOWN · NON-CANON · ZERO REALIZED CREDIT**

## Scope and result
User requests gross throughput including repeated transactions, without restricting the metric to GDP or final sales. This version therefore reports **three separate layers**: production gross output, domestic value added/GDP, and gross payment/financial-transaction turnover. Repeated transactions count as events in the third layer. They are not excluded because they repeat.

Using the user's **$1.6 quadrillion/year working gross-transaction benchmark**, the middle-case proportional-turnover scenario gives **+$3.271 trillion/year gross transactions**, reaching **$1.603271 quadrillion/year total**. Expanded case gives **+$8.328 trillion/year**, reaching **$1.608328 quadrillion/year**. These results are **conditional scale mappings, not empirically estimated payment responses or tax bases**. The unrestricted scope does not remove the need to label assumptions.

## Refined production-side calculation
Keep v0.6's same23-family478.512B import basket and its eligibility/deployment cases, but replace arbitrary directVA fractions and VA multipliers with a geometric supply-chain proxy using observed2025BEA sector input shares.

| Broad producer sector | Intermediate inputs/gross output | Value-added/gross output |
|---|---:|---:|
| Manufacturing | 59.4733% | 40.5267% |
| Mining | 43.4432% | 56.5568% |
| Agriculture/forestry/fishing | 60.6822% | 39.3178% |

Sources: the directly downloaded BEA annual GrossOutput/IntermediateInputs workbooks frozen in v0.6. These are industry-wide2025ratios, **not circular-plant engineering costs or a complete BEA domestic requirements matrix**.

Coarse proposed assignments:
- Hides, oilseeds, natural rubber, cork/wood, textile fibers and crude animal/vegetable materials → agriculture/forestry/fishing proxy.
- Crude fertilizer/minerals, coal/coke and natural/manufactured gas → mining proxy.
- Remaining recovery/refining/material conversion groups → manufacturing proxy.
These mixed classifications require refinement; recycled metals differ from ore mining and renewable gas differs from extraction. The model does not infer plant feasibility from the mapping.

For each family i:
- B_i = imported-value-equivalent output replaced domestically, assuming parity pricing.
- a_i = observed broad-sector intermediate-input/output ratio.
- h = assumed domestically sourced fraction of intermediate inputs.
- X_i = B_i / (1 − a_i×h): direct output plus the geometric series of upstream domestic production.
- V_i = (1 − a_i)×X_i: value added under the **same broad-sector coefficient for each round**.
- Incremental X/V after displacement = sums×(1 − assumed displacement fraction).

This is a scalar proxy, **not a full interindustry Leontief inverse**. Imported supplier inputs leak from the domestic loop; hypothetical domestic-input fractions are60/80/95%. Displacement fractions15/15/20% remain uncalibrated assumptions. No household-induced multiplier is added; the earlier v0.6VA multiplier is not applied again. Additional production and direct imported substitution must be truly incremental; existing domestic recovery is in the baseline.

| Case | Imports replaced $B/year | Production gross output increase $B/year | GDP level increase $B/year |
|---|---:|---:|---:|
| Limited | 23.926 | 31.504 | 12.892 |
| Middle | 95.702 | 154.330 | 63.101 |
| Expanded | 215.330 | 393.188 | 160.637 |

Gross production flows are ~2.44–2.45times the modeledGDP gain. That difference is expected because gross output includes intermediate sales; it is not an additionalGDP credit. Earlier v0.6outputs remain a separate heuristic sensitivity. v0.7refines the production coefficient model rather than announcing measured effects.

## Unrestricted gross transaction layer
Let T0=1,600,000B/year (user working benchmark) and GDP0=30,861.3B/year (BEA2025):
- Gross transaction/GDP scale ratio r=T0/GDP0=**51.844867**.
- Conditional change in turnover ΔT=ΔGDP×r×response factor f.
- Conditional total turnover T1=T0+ΔT.

For f=1, turnover grows proportionally with modeledGDP; this is a **PROPOSED scaling assumption**, not money-stock velocity, a causal financial multiplier or evidence that the circular sector generates the national average amount of securities/repo/loan settlement.

| Case | Added gross transactions, $T/year | Total working gross transactions, $Q/year | Added share of working baseline |
|---|---:|---:|---:|
| Limited | 0.668 | 1.600668 | 0.0418% |
| Middle | 3.271 | 1.603271 | 0.2045% |
| Expanded | 8.328 | 1.608328 | 0.5205% |

**This answers the requested unrestricted turnover scenario.** It does not establish that3.271T or8.328T are additional income, resources or economic welfare. These are repeated gross events valued in dollars.

For comparison, use verified2025Fedwire Funds turnover1.148267Q instead of the unverified all-flow1.6Q benchmark: the corresponding proportional **Fedwire-reference** changes are .480T /2.348T /5.977T. This is a separate rail/reference mapping, not a lower bound or a confidence interval for total national payments. Do not add it to the1.6Q-based scenarios.

### Response sensitivity
| Case | No aggregate turnover growth, f=0 | Half proportional, f=.5 | Proportional, f=1 | Twice proportional, f=2 |
|---|---:|---:|---:|---:|
| Limited, $T/year added | 0 | .334 | .668 | 1.337 |
| Middle | 0 | 1.636 | 3.271 | 6.543 |
| Expanded | 0 | 4.164 | 8.328 | 16.656 |

The range is an assumed sensitivity, **not a statistical uncertainty interval**. Actual payment turnover could decline if there are fewer settlement steps, import financing/trading flows shrink or payment systems consolidate. No positive lower bound is demonstrated.

Import purchase payments may already originate in the US and appear in US settlement data. Switching the recipient domestically does not necessarily create another first payment. Extra supplier/payroll/financing flows need transaction-level measurement. Financial market turnover depends heavily on interest rates, securities trading and repo activity; it need not track incremental industrialGDP proportionally.

Where the user intentionally counts repeated rail events, overlapping events can be included with a consistent definition. Such an event-throughput sum must not be described as unique underlying spending. Current exact all-rail annualT0 remains unverified; the working1.6Q is preserved as an assumption, not promoted to observed data.

## Tax interpretation
Repeated **taxable** sales, wages, fees, interest or realized gains can contribute tax bases at multiple stages. However, **gross payment turnover is not automatically taxable income**. IRS asset-sale accounting measures gain relative to adjusted basis; installment payments can include taxable interest/gain and a non-income return of basis. A transfer of principal cannot be counted wholesale as an income-tax base.

Under a separately proposed broad transaction levy, an eligible share of gross events could form the policy tax base. This analysis does not assume such a law exists or choose a rate. Collectible revenue requires a specified tax, eligible transactions, exemptions, credits, incidence, compliance and behavioral response.
- Hypothetical gross-event levy arithmetic: revenue=ΔT×eligible share×rate.
- Existing-law incremental taxes: estimate wages/profits/value added/gains and apply relevant taxes, without taxing every dollar of settlement as income.

Tax rate, eligible fraction, actual taxable base and revenue remain **UNKNOWN** in the structured outputs. No national revenue projection is asserted. A broad levy would likely change the throughput it taxes; static gross-flow arithmetic alone cannot establish receipts.

## Interpretation for the programme
The domestic circular-production case still concerns qualified material supply, affordable delivered cost and resilience. Export retention and stocked reserves reallocate existing goods; they do not create financial wealth merely by adding recorded transfers. Renewable replacement can reduce commodity demand and sometimes reduce payment churn while improving welfare.

The **much larger throughput number is possible as a conditional accounting scenario**. The more grounded operating screen remains31.5–393.2B/year production gross output under the stated assumptions. Gross financial-event throughput.668–8.328T/year is the less grounded proportional mapping. Keep them separate from each other and from GDP; never sum the three layers.

## Reproduce
Run `python3 tools/circular_throughput_v0_7.py`, standard library.
- [Assumptions and23-family sector mapping](../data/throughput_v0_7/assumptions.json)
- [Scenario summary including unrestricted turnover](../data/throughput_v0_7/summary.json)
- [Scenario CSV](../data/throughput_v0_7/scenario_results.csv)
- [69 family/case production calculations](../data/throughput_v0_7/sector_calculations.csv)
- [Runner](../tools/circular_throughput_v0_7.py)
- [v0.6macro sources and GDP context](US_CIRCULAR_ECONOMY_CONSUMPTION_THROUGHPUT_GDP_V0_6_2026-10-12.md)

Checks passed:69family/case rows;95.7024B middle replacement; gross output exceeds value added; UNKNOWN tax base preserved; total turnover reconciles to working baseline plus simulated change. ZERO REALIZED CREDIT.

Primary references: [BEA gross output/value added](https://www.bea.gov/help/faq/1197); [BEA total-requirements definitions](https://www.bea.gov/help/glossary/total-requirements-table); [BEA input-output methods](https://bea.gov/resources/methodologies/concepts-methods-io-accounts); [Fedwire annual2025](https://www.frbservices.org/resources/financial-services/wires/volume-value-stats/fedwire-funds-service-annual-statistics/); [IRS Publication544](https://www.irs.gov/publications/p544); [IRS Publication537](https://www.irs.gov/publications/p537). BEA ratios/GDP/43mineral receipts remain frozen in v0.6. A sector matrix and observed industrial payment chains would be required to estimate actual transaction response.
