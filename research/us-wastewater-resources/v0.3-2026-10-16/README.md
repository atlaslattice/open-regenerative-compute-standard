# U.S. Wastewater Resources, Energy and Supply-Chain Resilience - v0.3

**Date:** October 16, 2026 (America/Chicago)  
**Status:** NON-CANON / screening research / ZERO REALIZED CREDIT  
**Evidence:** source-reported baselines, derived arithmetic and modeled sensitivities. No field recovery, pilot deployment, profit or actual import displacement is established.

## Read or download

- [15-page PDF report](US_Wastewater_Resources_Energy_Resilience_v03.pdf)
- [Full report in Markdown](report.md)
- [Complete downloadable analysis package](US_Wastewater_Full_Analysis_v03.zip)
- [39-source evidence register](sources.md)
- [Known gaps and next evidence](KNOWN_GAPS.md)

## What this research does

Screens annual municipal wastewater nutrients and sludge energy against U.S. imports, with 25/50/75 recovery or deployment sensitivities, dated market benchmarks, process-load deductions and deliberately hypothetical cost stress tests. Includes a register of other material, thermal and isotope opportunities with unsupported recovery/value left unknown.

At the 50% screening case, P/N/K retail replacement value is approximately $2.38B/year. Alternative sludge pathways give modeled CHP net electricity of 5.36 TWh/year, cleaned gas of 47.9 Bcf/year, or diesel of 262.5M gallons/year under explicitly assumed upgrading yields. **These are not additive energy outputs or measured national production.** Existing recovery has not been fully subtracted. Price levels, years and financial counterfactuals differ; no combined national profit is reported.

## Run the numerical model

Requires Python 3 standard library only. No credentials, accounts, services or network calls.

```bash
python run_model.py
python test_model.py
```

Run in this folder. `inputs.json` holds source data and assumptions; `results.json` holds output. Six tests cover conservation, reproducibility, unknown economics, price realization, parasitic electricity and heat-use assumptions. All six were executed, and an extracted package reproduced the numerical results exactly. This validates arithmetic and accounting properties, not engineering feasibility or source data accuracy.

## Boundaries that matter

- U.S. municipal wastewater is the quantified baseline. National all-industrial/mining/agricultural wastewater coverage is incomplete.
- Nutrient fractions are net qualified-output assumptions; energy fractions are shares of dated literature potentials.
- AD-CHP, AD-RNG and full-sludge HTL allocate the same sludge carbon differently. A hybrid needs its own process balance.
- Struvite nitrogen is already inside the N total. Added magnesium is an input, not free recovered-waste income.
- Potential includes existing beneficial uses. Additional supply and profit require a matched before/after baseline.
- Import-content ratios require product/grade, buyer, location, timing and freight validation before claiming displacement.
- Null means unknown. No speculative metal/isotope sales, PFAS destruction or soil-use clearance is credited.
- Water reuse sales, environmental-credit revenue and unverified partnerships are excluded.

## Files and provenance

`sources.json` is machine-readable evidence metadata. `SHA256.json` describes the original bundle files. `PUBLICATION_SHA256.json` describes the public-folder payload. The ZIP preserves the previously delivered research package; this folder adds public navigation and a GitHub-readable report without changing the model results. Earlier repository research remains in place.

## License

Newly authored release material follows this repository's [CC BY-SA 4.0 license](../../../LICENSE). External publications and datasets retain their original rights; the package links sources and contains original synthesis/calculations rather than reproducing full third-party publications.
