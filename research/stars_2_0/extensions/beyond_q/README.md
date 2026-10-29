# Beyond Q — STARS / Stellar Forge extension

Paired D-D isotope refinery / D-T power research.

Continuation checkpoint, 2026-10-29. The architecture remains the research baseline. No validated engineering design or economic feasibility conclusion is asserted.

## Ancestry

`archive/COPILOT_RECOVERY_BASELINE_2026-10-29.md` preserves the supplied archival paper's substantive Markdown, including contradictory numerical ancestors. Chat transport escapes and list formatting were normalized; original M365 bytes and the mature 34-page paper were not retrieved. This is not a byte-identical DOCX archive.

`deltas/RECONCILIATION_v0_1.md` records the user's subsequent correction instructions and new calculations. Do not silently amend the archive.

## Reproduce

From repository root, Python 3 with the standard library:

```sh
python3 research/stars_2_0/extensions/beyond_q/models/rebuild_ledgers.py
python3 research/stars_2_0/extensions/beyond_q/models/check_arc_table.py
python3 -m unittest discover -s research/stars_2_0/extensions/beyond_q/tests -v
```

The isotope model is conditional primary-branch stoichiometry. The base case assumes no secondary product burn; survival is separately swept, not predicted. Recovery/qualification is assumed at 80%. Twenty-year output is a repeated physical production/demand scenario, not an operational fuel-cycle simulation. Startup inventory, reserves, decay, processing latency, fuel processing losses and outages are unresolved. Allocated helium is not booked as sales or avoided purchases.

## Evidence labels

Use separate fields for quantity provenance (OBSERVED / PUBLISHED DESIGN / DERIVED / ASSUMED / UNKNOWN / SPECULATIVE), evidence maturity (SOURCE-TRACED / SOURCE-REPRODUCED / CALIBRATED / VALIDATED, or NOT_ESTABLISHED), and claim disposition (ACTIVE / SUPERSEDED / OPEN). A derived calculation is not itself an evidence gate. A source-reproduced table is not a validated reactor.

## Completed here

- Ancestor archived in its own commit; corrections live in descendants.
- ARC v2 Table 11 transcribed from PDF page 30 and visually checked; source hash recorded.
- Cost-share arithmetic separated from D-D/DT commonality claims.
- Primary D-D production and D-T tritium burn rebuilt; direct-fuel deficit visible.
- Survival/recovery sensitivity and twenty-year primary-only physical ledger generated.
- No Li breeding credit, merchant sales, undocumented energy terms or strategic revenue imputed.

## Remaining gates, in order

1. Recover or reconstruct the D-D energy balance, retaining UNKNOWN inputs until sourced. Do not fit the missing balance to 105 MWth or -40 MWe.
2. Coupled secondary reaction/extraction model and optional neutron transport/blanket model.
3. Time-resolved inventory including decay, startup/reserves, latency, processing loss, availability and outage coverage.
4. Bottom-up exhaust/isotope-train scope and cost; resolve overlap with adaptation allowance. No defensible equipment/throughput estimate is yet available.
5. Recover $2.8B chassis ancestry and consistent cost year/scope. Adaptation ranges remain assumptions.
6. Update CAPEX/OPEX and 20-year finance only after these inputs are explicit. Do not fabricate ROI from missing costs or fuel closure.
7. Update white paper as a descendant; retain all ancestors and negative findings. Dual-DT comparison remains optional appendix material.

Hyperscaler internal use remains a scenario family, not predetermined consumption, revenue or proof of improved quantum performance. No Microsoft/Google affiliation is implied.
