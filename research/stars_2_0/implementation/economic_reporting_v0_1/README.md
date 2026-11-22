# Stars multi-experiment economic reporting v0.1

2026-10-28. PHYSICAL_CANDIDATE / ACCOUNTING SCAFFOLD. New version, no historical outputs replaced. Implements the project lead's direction: Stars supports many reproducible laser, acoustic and nuclear experiments with different objectives; a failed primary hypothesis can coexist with a separately supported coproduct benefit.

## Reporting contract

Every new experiment-summary adapter should emit both its unchanged scientific outcome and this economic footer, with the complete JSON manifest alongside it. Economic assumptions must not flow upstream into physical reaction rates or change a hypothesis verdict. This module provides a callable renderer and examples; existing archived scripts and all past outputs have NOT been retrofitted. Other experiment producers must explicitly adopt the interface in subsequent versions.

For each inventory allocation supply product identity, material/product specification, quantity unit, modeled/measured evidence, produced quantity if known and independently justified saleable quantity if known. Unknown values stay null. The module does not derive recoverability or purity from particle births, nor validate the caller's saleability assumption. Define one reporting interval per experiment ID; use consistent currency, units and cost boundary. Unit/currency conversions must be performed and documented upstream.

For each price snapshot require identifier, quote date, access date, source, product specification, currency, quantity basis and quote kind. Preserve the source document or permission-compatible hash/reference in the experiment's source registry. Public/contract quotes are scenarios rather than guaranteed demand. Quotes are immutable inputs, not live-feed lookups. Quote age is displayed; there is no universal hardcoded expiration policy. Reprice a new output version when useful. A quote is not automatically today's market price because it was accessed today.

**No actual market quote is ingested here.** The only numeric price is a deliberately fictional synthetic fixture, not a price for tritium, helium-3 or any real isotope. Unverified figures from conversation are not defaults. An actual market snapshot can be supplied later after source/date/specification qualification; unknown price remains UNPRICED rather than zero.

Report potential gross for each priced, saleable allocation; explicitly label the priced-subset sum and whether all products are valued. Require electricity, extraction, purification, storage, transport, capital allocation and other operating costs as explicit categories. Unknown costs remain null and block potential net. Users must justify explicit zeros; a filled category list alone does not prove complete plant economics. Revenue is not inferred: realized revenue remains null/NOT RECORDED in this scenario module. Actual invoiced sales require a separate transaction ledger.

Physical product, heat and electrical outputs remain separate. No heat credit is calculated here; any later thermal offtake needs temperature/quality, real demand, measured useful delivery and corresponding costs. Heat must never be treated as an equal electrical-bill reduction. Potential economic value does not establish energy gain, feasibility or a market.

## Inventory and decay limitations

The v0.1 allocation guard rejects duplicate inventory IDs within a report and saleable quantity exceeding its same-species produced allocation. It is not a complete atom-balanced decay/conversion ledger and cannot detect callers relabeling the same stock under different IDs or in different reports. Derived isotope stocks must first pass an external time-dependent inventory ledger identifying parent depletion, transfers, decay, daughter recovery and sale allocation. Do not value the same allocation as both sold parent inventory and retained future daughter inventory. No breeding, extraction hardware or isotope-production optimization is implemented.

## Examples and checks

`python run_examples.py --out receipts/new_run_name` creates a fresh output directory, runs the test suite and emits JSON plus a compact Markdown footer for both examples. Python 3.12.14; standard library only, exact Decimal arithmetic, no RNG or network. Run from this directory or pass the script path. Source hashes and execution receipt accompany the outputs.

1. A **fictional** failed hypothesis: 1 g modeled production, assumed 0.5 g saleable, synthetic $10/g, $2 assumed total cost → $5 potential gross, $3 potential net. Scientific FAIL stays FAIL and realized revenue remains unknown. All costs and saleability are fixture assumptions.
2. A G0-B design placeholder: scientific NOT_TESTED, no coproduct inventory assessed, costs unknown, potential net unresolved. This does not assert zero actual product generation. No price or revenue is fabricated to fill the footer.

Nine tests check positive potential value with unchanged scientific failure; unpriced/unknown saleability; incomplete costs; duplicate/overallocated stock; mismatched units/specifications/currency; future/invalid prices; invalid quantities; quote-age visibility. These verify accounting behavior, not physical yields or commercial viability.

## Integration sequence

First adopt this interface in new experiment runners and preserve their physical receipts. Then qualify dated public or contract price snapshots and carry market uncertainty/quantity limits as separate scenarios. Extend to shared calibration uncertainties, atom-balanced decay inventories, explicit marginal versus fully allocated costs and cost-allocation sensitivities before economic optimization. Keep p–B reference experiments and alternative reaction experiments on separate source-qualified manifests.
