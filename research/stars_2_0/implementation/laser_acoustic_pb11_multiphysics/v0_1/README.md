# Stellar Forge — Laser–Acoustic p–¹¹B Multiphysics v0.1

2026-10-30. Implements the first source-recovery and reporting-interface slice of
the user-authorized GPT-6 work order. Append-only, no scientific freeze, no
Beyond Q D–D/D–T reactor assumptions. This is not a completed multiphysics
apparatus simulation or acoustic/energy gain result.

## Completed

- Scanned all 61 main-branch Stars text documents at a pinned commit; preserved
  the distinction between pocket, printed support, film and hollow sphere.
- Created an unresolved geometry/material parameter template and executable
  completeness gate. No pocket dimensions or material response values invented.
- Defined six pocket/reference × OFF/SHAM/ON cells and physical/detection/energy
  interfaces, retaining A/B/C apparatus lineage separately.
- Implemented descriptive all-attempt accounting: unconditional and conditional
  yield, missing outcomes, timing bias/jitter, disjoint wall-cost categories and
  net electricity when all required inputs are supplied. Expected weighted
  reactions cannot be thresholded into a physical shot-success probability.
- Ran 22 targeted verification tests. Synthetic fixtures test accounting only;
  they do not supply physical acoustic coefficients or apparatus parameters.
- Reran the unchanged PR44 cold-B11 conditional transport reference. Result:
  0.039825758215570835 expected reactions across three assumed input attempts.
  Output SHA256 88baaa298034e2f376a797331f02aed1050370256d306132a134b49808c64074
  matches the preserved reference. It has no pocket, alpha escape or recovery.
- Read official ESTHER and Flash-X access pages. One-dimensional ESTHER and
  access-controlled Flash-X remain optional dependencies, not falsely installed
  solvers. Read pinned Smilei README; kinetic nuclear-feature parity remains open.

## Run

From this directory, using Python 3.12 and standard library only:

```bash
python -m unittest -v test_benchmark
python benchmark.py geometry geometry_template.json --output /tmp/sf-geometry-001.json
python benchmark.py shots fixtures/accounting_only.json --output /tmp/sf-accounting-001.json
```

Outputs must be new. Geometry correctly returns BLOCKED_UNRESOLVED_GEOMETRY.
The synthetic accounting fixture exercises all six arms; it has no evidential
relationship to apparatus performance. Its arbitrary threshold/values must not
be used as a campaign prediction or laboratory calibration.

The separate transport replay requires the stacked PR44 dependencies and NumPy:

```bash
python ../particle_handoff_v0_1/run.py ../particle_handoff_v0_1/examples/C_conditional_reference.json --out /tmp/sf-transport-001
```

Full WarpX upstream PIC benchmark remains pending: current installed environment
has no pywarpx, MPI launcher or cmake. No full build was attempted in this release.
The earlier PR47 scalar cross-section audit is retained as a separate numerical
check, not silently promoted to a PIC execution.

## Reliability and yield

For success event S and shot yield Y:

E[Y] = P(S) E[Y|S] + (1-P(S)) E[Y|not S].

More successful shots can increase total yield at unchanged successful-shot yield.
Failed shots can still react. Higher conditional yield alone can hide lower
all-attempt output. Increased preparation time/cost can offset per-attempt gains
when expressed per hour or wall joule. Code preserves these distinct quantities;
no acoustic cross-section multiplier is introduced.

## Navigation and next execution

- RECOVERY_REPORT.md: documented/reconstructed/unresolved design evidence.
- COMPARISON_SPEC.md: matching, sham, grouped holdouts and interaction tests.
- SOLVER_MATRIX.md: sources, access limits and applicability.
- INTERFACES.md: units, state transfer, particle ownership and ledger boundaries.
- DEEPSEEK_POCKET_REVIEW.md and POCKET_CANDIDATES.json: integrated candidate designs and technical corrections.
- GATE_STATUS.json: implemented versus proposed WP1–WP8.
- BENCHMARK_MANIFEST.json: exact current and pending benchmark identities.
- HANDOFF.md: next actions and blockers.
- receipts/: actual runs, tests and official access check.

Next independent engineering step is a pinned full WarpX pB operator build/run,
followed by finite-orbit field tests. In parallel, recover actual pocket fabrication
specifications and condition-specific material/optical/acoustic properties. These
must precede a physically meaningful pocket-vs-reference prediction. Do not wait
for ESTHER/Flash-X permission to complete accessible qualification tasks. Access
requests to maintainers have not been sent.
