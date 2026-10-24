# Oʻahu Atlas Lattice v0.2 — remediation modules and portfolio economics

**October 24, 2026. Research extension; no equipment purchased, no cleanup authorization, no measured Oʻahu recovery yield and zero realized benefit credit.**

This adds **62 catalog entries, 19 candidate process recipes, a runnable fines-washing ledger, capacity tests, a full-cost interface, and portfolio accounting** to the [unchanged daily v0.1 model](../oahu-lattice-v0_1/README.md). The catalog spans established treatment families and emerging options. It is a discovery inventory, not a claim that every listed method is compatible, commercially mature, or simulated. Only the capacity/washing/accounting examples are executed. Missing prices prevent an actual vendor ranking or ROI finding.

The governing economic principle is **portfolio viability**. A properly characterized, permitted fines stream can lose money while profitable metals and verified avoided infrastructure costs make the combined program worthwhile. Stream accounts remain visible; positive cash elsewhere cannot override an environmental veto. A public benefit can justify a service payment or subsidy, but is not automatically cash available to pay the operator.

## Full Desen public-suite coverage

Reviewed the product and application navigation on [materialwashing.com](https://www.materialwashing.com/) on October 23, 2026. “Full suite” here means all three published top-level product families, four named mobile washing machines, three screening variants, and all five linked application families. It does not imply access to unpublished/custom options or exhaustive review of news posts. These are **manufacturer publications, not independent performance verification or quotations**.

| Family or unit | Treatment role | Source and unresolved issue |
|---|---|---|
| Fixed washing/remediation plant | Integrated scrubbing, classification, solids separation and water treatment | [Fixed plant](https://www.materialwashing.com/Fixed-Washing-Plant/79.html); project configuration needed |
| Mobile washing train | Package of the four machines below | [Mobile family](https://www.materialwashing.com/Mobile-Washing-Plant/); quote package OR components, not both |
| DSLXC/01 | Feeding, pre-screening and scrubbing | [Unit](https://www.materialwashing.com/Mobile-Washing-Plant/26.html); table 15–20 t/h and 71.5 kW, overview 15–30 t/h |
| DSLXC/02 | Fine slurry classification | [Unit](https://www.materialwashing.com/Mobile-Washing-Plant/27.html); table 30 t/h and 70 kW; clarify slurry/dry-solids basis |
| DSLXC/03 | Filter press / solid-liquid separation | [Unit](https://www.materialwashing.com/Mobile-Washing-Plant/205.html); cake requires a final outlet; capacity/power unresolved |
| DSLXC/04 | Washwater treatment/recycle | [Unit](https://www.materialwashing.com/Mobile-Washing-Plant/206.html); heading/body/table model labels differ; “90 m³” lacks time basis; table power cannot yet establish train load |
| DS260 / DS15SE screening | Vibrating, rotary/trommel and bar/grizzly alternatives | [Product page](https://www.materialwashing.com/Mobile-Screening-Plant/281.html) versus [DS15SE article](https://www.materialwashing.com/news/1051.html): model/version, capacity, weight and transport dimensions unresolved |

Separate application recipes are included for [contaminated soil](https://www.materialwashing.com/application/soil-washing-and-remediation-plant.html), [oily soil/sludge hot washing](https://www.materialwashing.com/application/oil-contaminated-soil-washing-and-remediation-plan.html), [ditch/dredged sludge](https://www.materialwashing.com/application/ditch-and-dredged-sludge-washing-and-disposal-plan.html), [bulk screening](https://www.materialwashing.com/application/bulk-material-screening-plant.html), and [mineral/material washing and classification](https://www.materialwashing.com/application/material-washing-and-classification-plant.html). These are applications of configured systems, not five extra machines to charge or five additive recovery yields. Hot washing is distinct from thermal desorption. The soil application excludes mercury: mercury-bearing material needs separate specialist evaluation.

The [machine-readable catalog](catalog.json) retains the conflicting specifications. The approximately $300,000 lead remains an unverified conversion/landed-budget assumption from an unspecified ¥2 million B2B configuration. **None of these additional modules is assumed included at that price.** No complete-line power, throughput, electrical compliance, shipping configuration or contaminant-removal guarantee is established.

## Beyond Desen: attachable alternatives

The catalog also covers hazard/whole-item recovery; magnets, eddy-current and sensor sorting; external refining; aggregate certification; chemical extraction, electrokinetics, biological treatment, phytoremediation, thermal desorption, destruction and stabilization; polymer mechanical/solvent/depolymerization/conversion routes; organics composting/digestion, biochar and nutrient recovery; water clarification, biological treatment, adsorption, membranes, precipitation, specialist destruction and crystallization; brine mineral/salt/acid/base recovery; heat integration, power, fabrication, controls and authorized residual disposal.

These are candidate families, not claimed Desen products. General references include the [FRTR matrix](https://frtr.gov/matrix/), [soil washing](https://frtr.gov/matrix/Soil-Washing/), [stabilization](https://frtr.gov/matrix/Solidification-and-Stabilization/), [thermal treatment](https://frtr.gov/matrix/Desorption-Incineration/), [EPA polymer pathways](https://www.epa.gov/plastics/advanced-recycling-plastics), [EPA digestion](https://www.epa.gov/anaerobic-digestion/basic-information-about-anaerobic-digestion), [ITRC PFAS treatment](https://pfas-1.itrcweb.org/12-treatment-technologies/) and [GAO brine minerals](https://www.gao.gov/products/gao-25-108484). These references support technology discovery, not Oʻahu suitability or present pricing. Some candidate interfaces need more specific literature before design. Brine extraction must be assessed by mineral/process; broad commercial readiness is not assumed.

[Pathways](pathways.json) allocates those modules to 19 recipes and records cross-layer decisions. Soil washing or biotreatment cannot destroy metal elements. Immobilization is a different endpoint from extraction, destruction of an organic contaminant, or unrestricted reuse. Biological sludge, oily sludge and mineral filter cake are not interchangeable fuel feedstocks. For each candidate, ask whether the relevant constituents are separated, transformed, immobilized or still present, and where they go next.

## Capacity result: washing only the appropriate fraction matters

Assume 8 hours/shift, 80% availability once, 20% fines, and a **hypothetical sustained 15 t/h washing capacity**, chosen as the lower published scrubber-table value. The complete train may be slower: filter press, water chemistry, feed basis and cycle times remain unknown.

| Screen sensitivity, with enough feed | Screened t/shift | Fines t/shift | Washed t/shift | Unwashed fines t/shift |
|---|---:|---:|---:|---:|
| 50 t/h | 320 | 64 | 64 | 0 |
| 200 t/h | 1,280 | 256 | 96 | 160 |

A 200 t/h screen does not imply a 200 t/h wash plant. Conversely, washing only selected fines means the washer does not need the screen's full nominal capacity. At 40% fines, even a 50 t/h screen produces 128 t/shift, exceeding this assumed washer's 96 t/shift.

The **current-incoming-feed v0.1 adapter** is different from the ample-feed/legacy sensitivity above. Its feed availability limits the 200 t/h case; both current-flow cases fit the assumed washer capacity at 20% fines. They offer 19,200 and 23,119 t/year of as-received fines respectively. These are inherited composition assumptions, not landfill assays. No legacy excavation or seasonality was added.

## Conserved washing demonstration

The example starts with **1,000 dry tonnes** of hypothetical mineral fines plus 538.46 t inherent water and 2,000 t added water. Assumed outputs are 700 dry t candidate product, 300 dry t cake solids with 300 t cake water, and 2,238.46 t filtrate. Trace-contaminant partition is 4% product / 95% cake / 1% water. Solids, water and contaminant ledgers close. Contaminants have not disappeared.

The illustrative product concentration is 57.14 mg/kg against a **fictional 100 mg/kg demonstration threshold**; this is not a threshold for any named contaminant or Hawaiian reuse standard. At unresolved external clearance, accepted product is zero. A hypothetical all-gates-pass case accepts 700 dry t; a worse separation case fails the quality test even with external clearance set true. A real decision requires a vector of contaminants, speciation, leaching, pathogens, engineering suitability, permits and buyer requirements—not a single surrogate number.

Attaching this hypothetical 70% dry-product split to v0.1's metals-only cases, with a new assumed 65% fines dry-solids content, gives about **8,736–10,519 dry t/year candidate accepted product if every external gate passes**. This is not net disposal avoidance: cake moisture, water purge, treatment residuals and reagents still need full closure. No product or real-world benefit is credited in the unresolved case. The v0.1 integrated mineral scenario is not used as feed, avoiding duplicate mineral credit.

## Cost effectiveness: stream accounts and the combined program

The complete-cost function requires annualized capital, fixed O&M, variable processing, power, water/reagents, tests, transport, residual management, accepted-product netback and avoidable baseline cost. Null costs remain unknown, never free. Identical labor, equipment or transport must not be charged once in a stream and again in shared overhead. A contract may bundle transport into a netback; then do not subtract it again.

For a public comparison, evaluate the discounted difference between complete alternatives:

**disposal alternative's avoidable capital + operating + closure + monitoring costs − recovery program's complete corresponding costs**, with material revenue, land effects, timing, residual liability and other benefits assigned consistently.

Use equivalent time horizon, service requirements and stakeholder boundary. Historic sunk costs and unavoidable closure costs are not savings from this project. Tipping fees can be operator revenue and payer expenditure; internal transfers cancel in a consolidated public account. Required residual landfill capacity remains in both scenarios as appropriate. Do not credit the full cost of a new landfill merely because some tonnes leave the current one. Avoided or delayed construction must be causally demonstrated, including minimum viable capacity and legal closure constraints.

**Cross-subsidy example, entirely hypothetical annual equivalents:** metals +$300,000; fines −$400,000; shared costs −$100,000 → program cash −$200,000. If independently justified avoidable public infrastructure cost were $300,000/year equivalent, the comparison becomes +$100,000/year. The operator still needs funding for the $200,000 cash deficit. With unverified avoided cost the public result is unknown; with a failed environmental gate a positive dollar result cannot clear the proposal. A viable portfolio does not require every stream to be profitable.

The runnable portfolio function retains these separate stream and public accounts. It supplies **break-even avoided-cost requirements**, not an invented value for Hawaiian land or a claim that a second landfill has been avoided. Education, research, resilience, ecology and land preservation can also be evaluated as separate measured/nonmonetary outcomes; they are not silently converted to dollars.

### Incremental fines-treatment cost ceiling

The sensitivity CSV asks how much *all remaining wash-train costs* could total while matching disposal of an already-separated mineral stream:

`ceiling = baseline disposal cost + accepted fraction × product netback − residual fraction × residual disposal cost`.

All rates are **hypothetical dollars per dry-equivalent tonne** so the calculation is transparent. Actual disposal invoices must use wet tonnage and waste class; this is not a vendor cost estimate. The ceiling must cover processing, annualized equipment, water treatment/purge, reagents, tests, labor and any transport not already in the netback.

| Assumed accepted dry fraction | Baseline disposal | Residual disposal | Product netback | Maximum other cost / dry feed t |
|---:|---:|---:|---:|---:|
| 70% | $100 | $100 | $10 | $77 |
| 70% | $100 | $400 | $10 | −$13 |
| 0% | $100 | $100 | $0 | $0 |

An expensive residual can reverse standalone washing economics. The negative $13 ceiling means that example needs additional support or portfolio value even before processing costs. It does **not** automatically reject the combined program. The 144 cases are sensitivity axes, not probability bounds or market rates. No universal "$100+/t washing" assumption is adopted.

## Physical capacity and ecological attribution

Report separately: (1) source-cell volume excavated; (2) reburied residue volume; (3) accepted product/fuel exports; (4) disposal/stockpiles elsewhere; (5) new water/sludge liabilities. Net recoverable permitted capacity needs measured densities, compaction, cover, slope stability, gas and leachate controls, and legal authorization. Source-cell clearance is useful even where external treatment costs money, but moving material alone is not regional disposal avoidance or environmental remediation.

For ecological claims, define endpoints before operation, use upstream/downstream or matched reference sites where feasible, measure contaminant loads as well as concentrations, record rainfall/pumping/other interventions, and specify monitoring duration and attribution limits. Baseline plus monitoring alone does not prove causation. For education/employment use training completion, competency retention and local paid-work measures against an explicit baseline. For optional AI use held-out sorting/control benchmarks and incremental energy/cost. Unresolved is distinct from a demonstrated failure and from a pass.

## Supplier/operator questions now sharpened

1. Quote screening, four-machine washing package, fixed alternative, and applicable oil/sludge configurations separately; bind price to model, modules, exclusions and trade terms. Confirm any shared components so package and component costs are not added twice.
2. Resolve DS260/DS15SE specifications and DSLXC/01 15–20 versus 15–30 t/h. State sustained **complete-train** throughput on the proposed feed and dry-solids/slurry/as-received basis.
3. Supply filter-press cycle/throughput/cake-solids data and a corrected DSLXC/04 datasheet, including whether 90 m³ means tank volume or flow rate.
4. Provide contaminant-specific input/output mass balance, soluble contaminants, recycle accumulation, makeup/purge, reagent dose, cake wet mass and lawful residual endpoints. No generic clean-soil guarantee.
5. Provide connected load/starting demand, 60 Hz export package, interconnections, required site containment, transport pieces, reassembly, commissioning, parts and service.
6. Normalize capex, operating costs, payment/inspection milestones and quote validity. Request separate accepted-product and disposal offers using wet tonnage and actual waste classes.
7. Ask the site/authority to quantify capacity actually recovered and infrastructure cost actually avoidable or deferrable. Record stream cross-subsidy openly; keep ecological vetoes independent of financial balance.

## Run and reproduce

Requires Python 3 standard library. Keep this directory beside the repository's `oahu-lattice-v0_1` folder. Local development folder spelling `oahu-lattice-v01` is also accepted.

```bash
python prototypes/oahu-lattice-v0_2/build_catalog.py
python prototypes/oahu-lattice-v0_2/model.py
python -m unittest discover -s prototypes/oahu-lattice-v0_2 -v
```

- [catalog.json](catalog.json): source-linked modules, machine specifications and ambiguities.
- [pathways.json](pathways.json): candidate recipes, cost fields and cross-layer decisions.
- [model.py](model.py): capacity, contaminant/water ledger, full-cost interface, portfolio function and v0.1 adapter.
- [results/summary.json](results/summary.json): executed illustrative outputs; no actual cost ranking.
- [results/cost_ceilings.csv](results/cost_ceilings.csv): 144 hypothetical break-even cases.
- [test_model.py](test_model.py): conservation, gates, capacity, unknown costs, portfolio subsidies/vetoes and adapter checks.

The treatment recipes are deliberately broader than the executed surrogate. Next calibration needs assayed feed classes, supplier line balances, written acceptance conditions, complete cost offers and a real disposal/infrastructure counterfactual. This release adds a place to attach that evidence without turning an unpriced module into a free solution.
