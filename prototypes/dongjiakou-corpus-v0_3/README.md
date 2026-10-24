# Dongjiakou → Corpus Christi: Atlas Lattice screening model v0.3

**Research draft • 24 October 2026 • No supplier quotation, engineering design, procurement commitment or realized environmental credit.**

Dave Sheldon's requested comparison: start with an operating Chinese reference, expose the component evidence, and design a Corpus adaptation that includes mineral recovery and the full community/ecological ledger. **No routine process-brine discharge to marine habitat is a design constraint. ZLD is aspirational; permitted residual treatment is an alternative only with verified final fate.**

The reference and the integrated adaptation have different boundaries. A low-cost operating RO plant does not establish the cost of a U.S. plant plus mineral recovery and no-ocean residual closure.

## What changed in v0.3

The reviewer response now produces equipment-savings percentages, recovery break-even conditions and discount/horizon sensitivities. Actual fallback quotes remain absent and are explicitly labeled. Chloride-inventory tests are separated from product-use acceptance gates. Chloride recovery/conversion alternatives and an intermediate-resource/final-residue policy implement the full-recovery aspiration.

**Halving only the historical2025 process-equipment line reduces that construction total by7.73%, or construction plus planning/design/admin by6.48%.** This is a narrow line-item sensitivity; it does not measure a whole-plant design substitution or the2026 GMP.

Actual mineral break-even remains unknown. Illustrative break-even and price sensitivities are assumptions, not production-cost or buyer quotations. Twenty-eight bookkeeping tests pass.

## Deliverables

- [Reviewer response and attachment guide](REVIEW_RESPONSE_v0_3.md)
- [Full-recovery policy and chloride routes](RESIDUE_POLICY_AND_CHLORIDE.md)
- [Draft Corpus Christi system and decision gates](CORPUS_DRAFT.md)
- [Component cost ledger](component_cost_ledger.csv) and [dated cost-category alignment](cost_category_alignment.csv)
- [Brine-to-products, construction uses and long-horizon financing](BRINE_TO_PRODUCTS_AND_RESIDUALS.md)
- [New DeepSeek claims and audit status](new_claims_register.csv)
- [Full brine product/pathway register](mineral_pathways.csv)
- [Chloride pathways](chloride_pathways.csv), [acceptance gates](chloride_acceptance_gates.csv), [resource status](resource_status.csv) and [fallback pricing status](fallback_pricing_status.csv)
- [Twelve-domain lattice register](lattice_couplings.csv)
- [Residual-stream routes and unresolved destinations](residual_routes.csv)
- [Source and provenance register](sources.json)
- [Editable assumptions](inputs.json), [executable model](model.py), [tests](test_model.py)
- [Calculated output](results/summary.json) and CSV scenario exports in `results/`

## Headline screening results

| Quantity | Result | Interpretation |
|---|---:|---|
| Base product design | 30 MGD / 113,562 m³/day | Online-day nameplate; not firm delivery |
| Annual product at assumed 90% availability | 37.31 million m³ | Annual average equivalent 27 MGD |
| Intake at 42.5% whole-plant recovery | 267,206 m³/day | RO recovery separately assumed 47.5% |
| RO concentrate | 125,516 m³/day | Idealized flow balance |
| Other pretreatment residual | 28,127 m³/day | Backwash/loss envelope; not a detailed recycle design |
| Combined residual liquid | 153,643 m³/day | Must be explicitly routed |
| Dissolved feed-salt inventory | 9,352 tonnes/day | 35 kg/m³ assumed; excludes added reagents and solids |
| Unadjusted capital-intensity ratio | 13.89× or 9.61× | Corpus preliminary GMP vs historical ¥450m or ¥650m reference; mixed date/scope |
| U.S. all-in capital cost | **Unknown** | Missing categories remain null |
| Mineral revenue / realized credit | **Zero baseline** | No qualified products or contracted buyers established |
| Environmental gate | **Unresolved** | No downstream route has yet been cleared |

## Reproduce

Python 3, standard library only:

```sh
python model.py
python -m unittest discover -s . -p 'test_*.py' -v
```

Twenty-eight tests cover water and salt conservation, competing ion allocations, chloride limitation, missing costs, availability, thermal matching, additional compute energy, and off-site disposal gates. Passing software tests validates bookkeeping, not treatment performance.

No full source documents are redistributed. `sources/local_source_receipt.json` identifies the downloaded ministry casebook by SHA-256 and relevant printed pages. All research inputs have URLs and status labels. Some procurement details exist only in mirrors and are explicitly provisional.
