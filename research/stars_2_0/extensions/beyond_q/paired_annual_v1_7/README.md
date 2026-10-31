# Beyond Q paired annual v1.7

[Technical report](REPORT.md) · [Sources](SOURCES.md) · [Continuation](HANDOFF.md)
· [Offline dashboard](dashboard.html)

ARC-based and laser-based conditional campus accounting with explicit fusion
power, gross/net electricity, startup, B lithium replacement breeding, tritium
fuel retention, direct He-3, He-4 recovery candidates and outage controls.
All physical gates remain open. No isotope output is certified and no total
profit is inferred. The normal B replacement assumption is not the all-zero
breeding adverse control.

```bash
python compare.py
python refine.py
python -m unittest test_compare -v
python render_dashboard.py
node check_dashboard.cjs
```

Python standard library runs the model. Optional `plot_results.py` needs
matplotlib. The neighboring pinned v1.4 scenario input and engine sources must
remain present for provenance checks. Open `dashboard.html` locally; GitHub's
source view does not execute it. CSV outputs are under `outputs/`.
