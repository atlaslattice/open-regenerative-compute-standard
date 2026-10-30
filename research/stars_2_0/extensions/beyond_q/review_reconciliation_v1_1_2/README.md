# Beyond Q v1.1.2 — Independent review integration

Continues v1.1.1, with original v1.0/v1.1/v1.1.1 directories untouched.

```sh
python run_review.py
```

Python 3.10+, standard library only. Includes 17 mandatory regressions with
visible failure status, independent A plasma/blanket processing, primary DD
and secondary DT neutron-response coefficients, secondary on/off cases,
static %/kg balances, dynamic independent outages and threshold comparisons.

- [Independent-review reconciliation appendix](INDEPENDENT_REVIEW_RECONCILIATION.md)
- [Mass conventions](outputs/mass_conventions.csv)
- [Annual screening and thresholds](outputs/annual_screening.csv)
- [Dynamic reconciliation and matched threshold shifts](outputs/dynamic_reconciliation.csv)
- [Enrichment comparison specification](outputs/enrichment_comparison_plan.csv)
- [Regression results](outputs/regression_results.txt) and [status](outputs/regression_status.json)
- [Append-only audit](AUDIT_HISTORY.jsonl)

All assumed inputs are in reference.json. Separate A recovery/rates and DD/DT
blanket response coefficients are illustrative, not measured. The historical
1.3–2.6 kg/FPY range is retired as derived performance; no fabricated transport
result replaces it. The old aggregate A neutron yield is removed. No qualified
usable surplus or physical self-sufficiency is declared. All G1–G5 remain OPEN.

No new external neutron transport has been run. Natural/intermediate/high-Li6
fixed-geometry and separately optimized comparisons remain UNRESOLVED pending
actual geometry/data/solver results; the specification keeps these distinct.

Inputs inherited from v1.1.1 retain its hypotheses. New assumed processing
values: eta_A_plasma=.95, eta_A_blanket=.90, k_A_plasma=4/day,
k_A_blanket=1/day; y_DD=y_DT=.52 births/source neutron. No universal natural-Li
yield is implied. Reference.json contains redundant plasma descriptive values
from Argon's reference; dynamic hazards are authoritative, as in prior releases.

Research originator Dave Sheldon / Atlas Lattice; GPT-6, DeepSeek and Gemini
Argon credit as documented in the appendix. Repository CC BY-SA 4.0 terms.
