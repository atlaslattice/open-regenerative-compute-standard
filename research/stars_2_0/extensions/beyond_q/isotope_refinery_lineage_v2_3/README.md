# Beyond Q v2.3 — Isotope-refinery lineage and recovery-boundary audit

This additive research appendix integrates the originator's supplied historical and contemporary precedents with the v2.2 package at commit `50c4c322c239874f43a9908b7a4522007b621af8`. It changes no parent physics, financial inputs, cascade results or earlier release files. See [REPORT.md](REPORT.md) and the machine-readable [source register](sources.json).

Reproduce with Python 3.12 or later, standard library only:

```sh
cd research/stars_2_0/extensions/beyond_q/isotope_refinery_lineage_v2_3
python audit.py
python -m unittest -v test_audit.py
```

Outputs: `normalization.csv`, `decay_comparator.json`, `execution.json`. The historical benchmark record in `inputs.json` is deliberately disabled for calibration: the full 1982 equations and operating points have not been obtained. All physical gates remain open.

Current 1100 MW primary-DD A and 1100 MW DT B scenarios, explicit 1130 MW B comparator, 37.5/75/90% overall He3 recovery sensitivities and separate recipient financing policies remain as documented in [v2.2](../fuel_cascade_v2_2/REPORT.md). No GPU/QPU economics are added.
