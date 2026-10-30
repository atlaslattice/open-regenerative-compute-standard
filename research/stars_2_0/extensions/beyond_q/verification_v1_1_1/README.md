# Beyond Q v1.1.1 — independent benchmark and resilience pass

New versioned verification extension; v1.0 and v1.1 remain unchanged.
B stays 1130 MW D-T fusion; A stays hypothetical 20 MW primary D-D.

```sh
python run_verification.py
python -m unittest test_verification -v
python plot_results.py
```

Requires Python 3.10+, NumPy and SciPy (matplotlib for optional SVG plots); exact tested versions are in
outputs/manifest.json. Runtime is several seconds. All code/data required for
the external numerical comparison are included; no network required to rerun.

- [Report](outputs/REPORT.md): benchmark scope, model mapping, startup envelope and error budget.
- [Benchmark metrics](outputs/benchmark_metrics.json) and [curves](outputs/benchmark_curves.csv).
- [Stress results](outputs/stress_tests.csv), [startup brackets](outputs/startup_brackets.csv).
- [Numerical budget](outputs/numerical_budget.csv), [parameter budget](outputs/parameter_budget.csv), [extraction comparison](outputs/extraction_comparison.csv).

External reference: Meschini S., Ferry S.E., Delaporte-Mathurin R., Whyte D.G.,
*Modeling and analysis of the tritium fuel cycle for ARC- and STEP-class D-T
fusion power plants*, Nuclear Fusion 63 (2023) 126005,
https://doi.org/10.1088/1741-4326/acf3fc, as implemented by INL TMAP8 at
https://github.com/idaholab/TMAP8/tree/7dfbc71378fb243afba23db80a8284cd4b6429a4/test/tests/fuel_cycle_Meschini.

The exact input, test overrides and reduced-runtime gold CSV are retained in
upstream/. The original MATLAB/Simulink repository v1.1 was inspected but its
binary model was not executed. INL's reference executable was not executed
either: an independent Python implementation is compared with its stored gold.
The gold comparison matches its implicit timestepping and lagged forcing;
a continuous-time oracle exposes remaining numerical bias separately.

Seven-stock Beyond Q and the external 11-stock fixture are different models.
No false parameter-only equivalence is claimed. Two extraction hypotheses are
compared in a standalone module; full discrete-loop integration is future work.

Source license: upstream TMAP8 files retain GNU LGPL v2.1 (upstream/LICENSE).
benchmark.py is a modified-language implementation of its published equations,
distributed under LGPL v2.1 with notices retained here. The other new project
files follow repository CC BY-SA 4.0 terms; no upstream relicensing is implied.
Preserved fuelcycle/ copies the previous Beyond Q model with explicit
component-outage schedules and substep minimum-storage reporting added.

Research direction Dave Sheldon / Atlas Lattice; GPT-6 computational analysis,
with prior DeepSeek and Gemini Argon analytical contributions retained. All
physical gates G1–G5 remain OPEN; G6 independent provenance/replication remains
cross-cutting. No qualified usable surplus, experimental validation or
institutional endorsement.
