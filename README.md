# The Open Regenerative Compute Standard (ORCS)

## Dongjiakou → Corpus Christi lattice

[Latest v0.7 model](prototypes/dongjiakou-corpus-v0_7/README.md) adds USD component anchors labeled NEEDS SOURCING URLS, initially identical DeepSeek/Atlas reference columns, and matching-scope Corpus prices or null. Independent pump-train scenarios distinguish finished-water capacity, RO feed, standby trains and actual pump duties. Municipal and direct industrial wastewater remain separately bounded. 86 bookkeeping tests pass; actual installed costs and environmental clearance remain unresolved.

[Component price comparison](prototypes/dongjiakou-corpus-v0_7/results/component_price_comparison.csv) · [Price, pumping and wastewater explanation](prototypes/dongjiakou-corpus-v0_7/PRICE_ANCHORS_PUMPS_AND_WASTEWATER_v0_7.md).

Prior versions: [v0.6](prototypes/dongjiakou-corpus-v0_6/README.md), [v0.5](prototypes/dongjiakou-corpus-v0_5/README.md), [v0.4](prototypes/dongjiakou-corpus-v0_4/README.md), [v0.3](prototypes/dongjiakou-corpus-v0_3/README.md), [v0.2](prototypes/dongjiakou-corpus-v0_2/README.md), [v0.1](prototypes/dongjiakou-corpus-v0_1/README.md).

## Maui resilience simulator — public research release, October 19, 2026

**[Maui Regenerative Resilience Simulator: water, energy, waste and recovery](sites/maui/README.md)** — a runnable 30-year / 168-hour Maui research prototype with 11 scenarios, 19 passing local tests, five retrieved public environmental feeds and dated evidence receipts. Covers Lahaina/West Maui, Kahului–Wailuku, Waikapū, Kīhei and North Shore planning, with independent Kanahā Pond/ecological safeguards. **Proposed infrastructure; incomplete financial model; no field deployment or implied partnership.**

[Download simulator ZIP](sites/maui/Maui_ORCS_v1_2_Verified_Runnable.zip) · [Verified results](sites/maui/simulator-v1.2/VERIFICATION_v1_2.md) · [Maui contribution needs](sites/maui/CONTRIBUTING.md) · [Structured metadata](sites/maui/metadata.json)


> *The data center is the farm. The watershed is the field. The thermal waste is the compost.*

Twelve AI perspectives — Claude, Gemini, Grok, GPT, Manus, DeepSeek, Qwen3, GitHub Copilot, Amazon Alexa, Notion AI, Llama, and Mistral — converge through a 12-seat Pantheon Council on a shared thesis:

**Regenerative agriculture principles apply to computing.**

---

## The Convergence

Despite different institutional lineages, architectural biases, and rhetorical styles, all nine perspectives converged on the same underlying conclusion: the current extractive model for hyperscale data center infrastructure depletes the substrate it depends on.

The archaeological record is used here as framing discipline, not as direct proof of any single engineering module. Durable systems close loops. Fragile systems externalize costs until the substrate fails.

## The Regenerative Jacket

A modular, facility-agnostic infrastructure layer that transforms data centers from extractive consumers into regenerative participants in their local watersheds:

| Component | Function | Agriculture Analog |
|-----------|----------|-------------------|
| HVAC Condensate Harvest | Capture atmospheric moisture from cooling systems | Water cycling in healthy soil |
| Closed-Loop Water Filtration | Continuous recycling with minimized discharge | Nutrient retention in compost |
| Thermal Offtake Infrastructure | Route waste heat to productive adjacent uses | Waste-as-input composting |
| Sub-Surface Root Warming | Warm soil layers for arid-zone restoration | Cover cropping and soil biology |
| Community Benefit Infrastructure | Integrate facility with local food and energy systems | Regenerative polyculture |

## Evidence Classes (Required Reading)

ORCS distinguishes three evidence classes for every significant claim:

- **Verified facts** — standards, peer-reviewed research, official disclosures, high-quality reporting
- **Derived estimates** — calculations from disclosed inputs with explicit assumptions
- **Proposed concepts** — new metrics/frameworks not yet adopted as standards

When in doubt: label conservatively.

## The Minimum Defensible Standard (MDS)

To remain legible to operators, policymakers, and skeptical reviewers, an ORCS-aligned publication should meet these minimum conditions:

1. Site-level resource boundary reporting
2. Evidence class marking on all claims
3. Local-first circularity before remote offsets
4. Gated pilot sequence (report → engineer → pilot → scale)
5. Community-cost protection as legitimacy (not charity)
6. Climate/geography-specific design (not templated)
7. Open publication of successful pilots (methods + assumptions + results)

## Repository Structure

```
papers/
  claude/       — The Rainier Regenerative Jacket (V1 & V2)
  gemini/       — The Janus Transition
  grok/         — The Colossus Regenerative Jacket
  manus/        — The Meta Regenerative Jacket
  deepseek/     — Transcript, Independent Paper & Metrics/KPI Framework
  qwen3/        — Qwen3 Perspective and Next Steps
  gpt/          — GPT perspective, adversarial reviews, and calibration notes
  copilot/      — Azure-Centric Integration & Verification (+ Addendum)
  alexa/        — Amazon Regenerative Infrastructure Strategy
synthesis/
  nine-model-convergence-v2.3.md   — Integrated synthesis
  deepseek-synthesis-brief.md      — DeepSeek-focused synthesis brief
  metrics-and-verification.md      — Layered measurement model
technical/
  orcs-boundary-statement-template.md  — One-page boundary template
  orcs-metrics-schema.json             — Machine-readable Tier 1 schema
  pilot-artifact-checklist.md          — Pilot publication requirements
examples/
  illustrative-tier1-report.json       — JSON example with fake numbers
  illustrative-tier1-report.md         — Markdown example with fake numbers
```

## The Federated Council

| Model | Context | Unique Contribution |
|-------|---------|---------------------|
| Claude | Anthropic | Modular gated implementation pathway, governance realism |
| Gemini | Google/Alphabet | Ecosystem-scale framing and social-license reframing |
| Grok | xAI | Local political urgency, aquifer risk, durability framing |
| GPT | OpenAI | Calibration, claim hygiene, hallucination detection, minimum-defensible-standard design |
| Manus | Agentic orchestration | Vulnerability framing, CapEx analysis, financing structure |
| DeepSeek | DeepSeek | Watershed Days, efficiency-as-regeneration, arid-zone adaptation |
| Qwen3 | Chinese governance lens | Governance interoperability, policy fit, expanded historical precedent |
| GitHub Copilot | Microsoft/Azure | Enterprise adoption layer, procurement legibility, audit-ready implementation, anti-greenwashing posture |
| Amazon Alexa | Amazon/AWS | Flywheel economics, scale leverage, AWS regions as regenerative anchors, customer-obsessed regeneration |

## Related Repositories

| Repository | Purpose |
|------------|--------|
| **[aluminum-os](https://github.com/atlaslattice/aluminum-os)** | The 12×12+1 codebase — 144 sphere directories + Element 145 sovereign kernel. 182 module stubs, YAML registries, all governance artifacts in ontological positions. |
| **This repo** (open-regenerative-compute-standard) | Governance specifications, papers, synthesis documents, council reviews. |

## Live Site

Explore the interactive framework: [The Open Regenerative Compute Standard](https://regcompute-gzelm6nx.manus.space)

## Build Plan

The canonical governance document is the **Build Plan** (currently v3.14, 5,124 lines). It defines all 182 modules, 45 invariants, 125 doctrines, 188 risks, and 45 appendices. The Build Plan is maintained in both this repo and the aluminum-os repo.

## License

This work is licensed under [CC BY-SA 4.0](LICENSE).

## Contributing

ORCS improves through:
- **Governance Protocols** — policy hooks, procurement language, interoperability with reporting regimes
- **Technical Specifications** — measurement methods, hydrology templates, pilot artifacts
- **Translations** — localization across languages and regulatory contexts

Fork. Adapt. Publish. The standard improves when more operators, researchers, and communities engage with it.

---

*Work with the flow. Return what you take. Nurture the source.*

**CC BY-SA 4.0 — The Federated Council — April 2026**


## Public project navigation (October 12, 2026)

**[START HERE — projects, simulator and evidence labels](docs/START_HERE_PUBLIC_INDEX_2026-10-12.md)** · [Corpus Christi and Jupiter](docs/US_SITE_COMPARISONS_2026-10-12.md) · [Domestic supply, reserves and export-policy comparison](docs/DOMESTIC_FIRST_RESERVES_EXPORT_POLICY_2026-10-12.md) · [Open engineering and funding gaps](docs/HELP_WANTED_RESOURCE_GAPS_2026-10-12.md) · [Public content and repository conventions](docs/PUBLIC_REPOSITORY_GOVERNANCE_2026-10-12.md).

**Current limitations:** ORCS is research; no Atlas industrial deployment or partner adoption is implied, the full 84-module cross-site simulator is not established as integrated, and source studies distinguish observed, reported, derived, modeled and proposed claims. Existing research and Git histories are preserved.


### Public full-text Notion research mirrors

[**Browse eight verified source-preserving research mirrors**](docs/notion-mirrors/README.md) — Corpus Christi water/resilience, Dongjiakou desal and LNG engineering, local SAF/reuse/gypsum, resident-benefit design, Jupiter arid-site comparison, China 2.0 synthesis and national-surplus/reserves policy. Historical originals remain in Notion; every mirror is marked NON-CANON and ZERO REALIZED CREDIT. The mirror index is dated; it is not an automated Notion synchronization.


## Session handoff & organization inventory — October 12, 2026

[**Full public thread synthesis and delta register**](docs/THREAD_HANDOFF_FULL_SYNTHESIS_AND_DELTA_2026-10-12.md) · [**273-repository organization inventory**](docs/GITHUB_ORG_REPO_INVENTORY_2026-10-12.md) · [**eight full-text Notion research mirrors**](docs/notion-mirrors/README.md).

**Snapshot scope:** 272 repositories public, one private/quarantined, ten archived; not all inspected or relicensed. Handoff summarizes the research without publishing personal circumstances. The full 84-module integrated simulator is not independently verified. Historical records remain intact.


### Texas livestock methane recovery research

[Texas manure-to-RNG screening ledger](docs/TEXAS_MANURE_TO_RNG_RESOURCE_SCREEN_2026-10-12.md) — 2026-10-12 screening assumptions for dairy, feedlot cattle, and hog manure collection; theoretical gas yields, exclusions, and requirements for engineering validation. Not measured methane or current RNG production.


### Texas manure-to-RNG pilot screening

[**County-cluster shortlist: Moore/Hartley, Castro/Parmer, Deaf Smith and Erath**](docs/TEXAS_MANURE_RNG_PILOT_COUNTY_SHORTLIST_2026-10-12.md) · [**Forkable Python methane calculator**](tools/texas_manure_rng_screen.py) · [**Original state resource assumptions**](docs/TEXAS_MANURE_TO_RNG_RESOURCE_SCREEN_2026-10-12.md). **County clusters are diligence candidates, not contracted sites.** Project modeling includes explicit unknown pipeline interconnection, farm collection fractions, volatile-solids and digestate sinks; a $6/MMBtu commodity-only worked example is not bankable without additional independently verified value or different cost structure.


### Texas food waste → biogas, digestate and concentrated nutrients

[**Texas food-waste bioreactor and fertilizer market screen**](docs/TEXAS_FOOD_WASTE_BIOREACTOR_FERTILIZER_MARKET_SCREEN_2026-10-12.md) covers statewide resource *assumptions*, 2022 fertilizer expenditures, Oct 2026 NPK benchmarks, anaerobic bioreactors, composting, struvite and ammonium sulfate, and a 100-ton/day pilot. The 5–8 million US-short-ton/year food-waste assumption is **not a verified Texas annual inventory**; all financial outputs remain illustrative. [Related Texas manure pilot](docs/TEXAS_MANURE_RNG_PILOT_COUNTY_SHORTLIST_2026-10-12.md).


### U.S. fertilizer import displacement (Texas food-waste only)

[**Texas food waste potential vs 2024 US fertilizer imports**](docs/TEXAS_FOOD_WASTE_US_FERTILIZER_IMPORT_OFFSET_2026-10-12.md) — hypothetical 25%-collected Texas resource: N ~0.04–0.21%, P2O5 ~0.04–0.25%, K2O ~0.01–0.06% of 2024 US gross nutrient imports. These are scenario ratios, not actual fertilizer sales or verified reductions in import shipments.


### Texas state fertilizer self-sufficiency (corrected denominator)

[**Texas food-waste recovery 25% / 50% / 75% and N/P/K independence screen**](docs/TEXAS_STATE_FERTILIZER_SELF_SUFFICIENCY_RECOVERY_25_50_75_2026-10-12.md) supersedes US-wide import percentages as the Texas decision baseline. The 5–8M short tons food-waste resource assumption and per-ton recoverable nutrients are unverified; Texas foreign imports, interstate purchases and physical N/P/K demand are not yet known. [Earlier US-import study](docs/TEXAS_FOOD_WASTE_US_FERTILIZER_IMPORT_OFFSET_2026-10-12.md) remains for provenance.


### Texas physical fertilizer purchases vs circular nutrients

[**Texas-specific historical commercial N/P fertilizer purchase benchmark and 25/50/75% food-waste offset model**](docs/TEXAS_FERTILIZER_NUTRIENT_DEMAND_BASELINE_AND_25_50_75_OFFSETS_2026-10-12.md) compares hypothetical recoverable food-waste nutrients to EPA Texas 2017 purchases: nitrogen 608.141 million kg, P2O5 143.232 million kg; K2O and 2026 demand remain UNKNOWN. This is not a current Texas import-substitution estimate or a realized savings claim.


### Texas food-waste nutrient value vs extraction costs

[**2026 NPK reference market value and 25/50/75 Texas food-waste recovery cost sensitivity**](docs/TEXAS_FOOD_WASTE_FERTILIZER_VALUE_VS_RECOVERY_COST_2026-10-12.md) compares ~$6–93M gross nutrient equivalent against deliberately hypothetical treatment operating costs, gate fees and methane energy. This is **not measured profit, vendor pricing, or realized imports displaced**, and requires laboratory nutrient assay and actual quotes.


### Texas landfill baseline and China BIO01 comparison

[**Avoided landfill disposal + freight vs integrated bioreactors, with China/Dongjiakou scope reconciliation**](docs/TEXAS_FOOD_WASTE_BASELINE_AVOIDED_DISPOSAL_CHINA_COMPARISON_2026-10-12.md) corrects the earlier fertilizer-only economic picture using TCEQ 2024 landfill average **$45.15/US short ton**, separate modeled freight, and independently attributed outputs. All plant costs/transport values remain scenario assumptions, and no realized profits or waste-offset credits are claimed.


### US onsite food-waste processing — national 25/50/75 resource diversion

[**US onsite bioreactor model: disposal cost vs processing 25%, 50%, 75%**](docs/US_NATIONAL_ONSITE_FOOD_WASTE_BIOREACTOR_25_50_75_2026-10-12.md) scales ReFED 2024 approximately 60 million short tons *food waste* against hypothetical half-cost onsite conversion. At an assumed $20/short ton processing target and EREF 2024 $62.63/short ton tonnage-weighted landfill tip benchmark, conditional direct handling-margin scenarios are ~$639M / $1.279B / $1.918B yearly **before capital, sorting, transport changes and existing beneficial uses**. Separate gas and nutrient coproduct estimates remain non-realized, no double-counting.


### National industrial and agricultural import supply-chain atlas

[**United States Industrial & Agricultural Import Supply Chain Atlas v0.1 — Oct 12 2026**](docs/US_NATIONAL_INDUSTRIAL_AGRICULTURAL_IMPORT_SUPPLY_CHAIN_ATLAS_V0_1_2026-10-12.md) establishes the comprehensive HS/NAICS coverage schema across fertilizers, critical metals, energy, industrial chemicals, machinery, food and agricultural inputs, with 2025 BEA/USDA/USGS/USITC source anchors, original production-to-importer provenance, US downstream users and circular-recovery opportunities. It is a **taxonomic first pass**, not a populated HS10-by-country-by-port full census, and no realized import offsets are claimed. Existing studies are preserved.


### US import/export cross-check and national reserve-first surplus gate

[**US national import–export cross-check, self-sufficiency + strategic reserves before export unlock and hidden-value domestic waste streams v0.1**](docs/US_IMPORT_EXPORT_CROSSCHECK_NATIONAL_RESERVE_FIRST_AND_WASTE_GOLD_V0_1_2026-10-12.md) formalizes user's **national, not merely Atlas-network, sufficiency rule** as a proposed lawful human-governed policy gate. Incorporates USDA 2025 agricultural $212B import/$171B export cross-check, EIA diesel export vs low inventories, USGS minerals trade/stock/recycled scrap, and waste-stream-to-refined-import screening. Full HTS10 export and import extraction remains outstanding and no existing legal export controls are asserted.


### US matched import/export physical balance and reserve-first pilot

[**2025 US distillate flows, mineral old-scrap trade and national reserve gate — quantitative pilot v0.2**](docs/US_2025_MATCHED_TRADE_AND_RESERVE_GATE_PILOT_V0_2_2026-10-12.md) contains sourced EIA 2025 distillate production, imports, exports, demand and regional balances; USGS 2025 old-scrap exports/imports/domestic recycling; and traceable per-grade reserve and surplus tests. Full USITC line-level trade, mineral 2025 CSV normalization and true national reserves remain outstanding. Earlier studies are preserved.


### US commodity supply ledger — v0.3

[Versioned partial physical ledger: copper, aluminum, potash and phosphate](docs/US_NATIONAL_SUPPLY_SECURITY_LEDGER_V0_3_2026-10-12.md) adds 2025 USGS estimates, explicit stock/boundary reconciliation, runnable JSON-to-CSV arithmetic and hypothetical aluminum scrap diversion. Full customs data, certified reserves and actual recovery economics remain UNKNOWN; earlier versions preserved.


### US raw-material supply-chain screen — v0.4

[25 matched material families: imports, exports, 20% import-exposure reserve allowance, circular/renewable routes and freight economics](docs/US_RAW_MATERIAL_IMPORT_EXPORT_RESERVE_RECOVERY_V0_4_2026-10-12.md). Downloaded revised 2025 federal data and runnable code; broad family coverage, not a complete raw-only customs census. Actual grade-matched offsets and transport remain UNKNOWN.


### Consumption, production gaps and reserve-first exports — v0.5

[Physical consumption, domestic production gaps and 20% domestic-use reserve model](docs/US_CONSUMPTION_SHORTFALL_RESERVE_FIRST_V0_5_2026-10-12.md). Latest user policy: imports remain permitted for verified production/grade/delivery gaps; the earlier blanket zero-import gate is superseded. Qualified additional waste recovery reduces import needs; exports follow consumption and stocked reserves. Runnable arithmetic; actual unmet demand and certified reserves UNKNOWN.


### Circular economy, throughput and GDP — v0.6

[Expanded consumption evidence and reproducible circular-economy GDP scenarios](docs/US_CIRCULAR_ECONOMY_CONSUMPTION_THROUGHPUT_GDP_V0_6_2026-10-12.md): 43 archived original USGS chapter receipts, 23 physical rows, a defined $478.512B import basket and direct BEA GDP/gross-output/input data. Payment settlement throughput is kept separate from GDP. Scenario multipliers and deployment fractions are uncalibrated sensitivities, not national forecasts; reserve-first exports and physical-gap imports remain current policy proposal.


### Unrestricted transaction throughput — v0.7

[Production flows, GDP and repeated gross transactions](docs/US_CIRCULAR_GROSS_TRANSACTION_THROUGHPUT_V0_7_2026-10-12.md): refined sector-ratio supply-chain proxy and an explicitly conditional turnover mapping using the user's $1.6Q working baseline. Gross transactions and tax bases are kept separate; no calibrated payment response or revenue forecast claimed.


### Public US dashboard source prototype — v0.1

[US Resource & Resilience prototype](prototypes/us-resource-resilience-v0_1/README.md): additive DragonSeek fork with 23 national physical records, reserve/recovery simulations, explicit regional UNKNOWN values and a local Atlas-Intelligence wording/citation checker. Public, forkable early-stage modeling; no operational monitoring or realized benefit claimed. Source lineage and retained upstream license included.


### Annual US simulator and data-access registry — v0.2

[Public dashboard with annual simulator](prototypes/us-resource-resilience-v0_2/README.md): 23 national records; five reviewed 2021–2025 material histories; 1–100-year recovery/reserve/import sensitivities; 75 source-access entries and four successful anonymous server sample probes. Public accounts, restricted authorization and untested sources distinguished. No calibrated forecast, certified reserve or operational deployment claimed. v0.1 preserved.



### U.S. wastewater resources, sludge energy and supply-chain resilience - v0.3

[**Public research release: report, reproducible model, 39-source register and known gaps**](research/us-wastewater-resources/v0.3-2026-10-16/README.md). National municipal-wastewater nutrient and alternative sludge-energy screens with dated values, import-content comparisons and explicit cost sensitivities. **NON-CANON / ZERO REALIZED CREDIT:** modeled potential, not observed recovery, validated profit or actual import displacement. Earlier studies preserved.
