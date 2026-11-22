# Beyond Q — Dynamic Fusion Fuel-Cycle Research Model v1.1 candidate

Atlas Lattice / STARS 2.0 / Stellar Forge. Continues v1.0 without overwriting it.
**B = 1.13 GW D-T fusion; A = hypothetical 20 MW primary D-D.**
No physical research gate is closed by arithmetic. No qualified usable surplus
or operational self-sufficiency is claimed.

## Run (Python 3.10+, standard library only)

```sh
python -m unittest discover -s tests -v
python run_research.py
python neutronics/openmc_surrogate.py --preflight
```

Optional Node 18+ logic check: `node tests/check_dashboard.cjs`. This verifies
selection/chart updates with a controlled DOM stub, not rendered layout.
Rendered-browser QA was blocked by an absent Chromium executable.

Run from this directory or use absolute paths. The model accepts a versioned
JSON input via `--input`, result directory via `--output`, and ensemble count
via `--samples` (default 64). Run at identical inputs/runtime for deterministic
results. Audit history is not rewritten by the runner. Tests verify the original
28 benchmark scenarios before dynamics. Files under `outputs/` are generated.

- [Technical results](outputs/TECHNICAL_REPORT.md): scenario bounds, ledgers, limitations and exact G1–G5 status.
- [Technical methods](TECHNICAL_METHODS.md): Argon equations, units, assumptions, stable integration and conservation boundaries.
- [Interactive results explorer](outputs/dashboard.html): select A0/A1/A2, inventory measure and day; export displayed CSV. Open locally in a browser; no network needed.
- [Inputs and provenance](inputs/parameter_provenance.csv): every reference parameter and evidence label.
- [Sensitivity CSV](outputs/sensitivity.csv), [ensemble CSV](outputs/ensemble.csv), [schedule](outputs/schedule.csv), [time refinement](outputs/timestep_refinement.csv).
- [Argon table audit](outputs/argon_table_audit.csv), [G1 arithmetic](outputs/argon_g1_audit.json).
- [Source registry](SOURCES.md), [append-only audit history](AUDIT_HISTORY.jsonl), complete [v1 snapshot](baseline_v1/WHITE_PAPER.md).
- [OpenMC blocker and surrogate instructions](neutronics/README.md). No transport results were fabricated.

A0 has a nonbreeding functional shield/coolant. A1 and A2 use explicitly
assumed source-neutron breeding yields; A2 is not a proven optimization. Argon's
two-stage burn and well-mixed extraction models are candidate equations;
unknown parameters are not promoted to measurements. The explorer selects
computed trajectories; use Python to change and rerun physical assumptions.

Research direction: Dave Sheldon / Atlas Lattice. GPT-6, DeepSeek and Gemini
Argon analytical contributions are described in the report and inherited
provenance. No institutional endorsement, experiment or independent peer
review is implied. Repository CC BY-SA 4.0 terms apply.
