# Conventional G0-B transport reference v0.1

STATUS: EXPLORATORY SOFTWARE VERIFICATION; PHYSICAL INPUT QUALIFICATION PENDING  
No scientific freeze, calibrated boron prediction, blind-data access or deployment.

## Purpose

Implement the first conventional pieces of the G0-B beam-to-target-to-detector pipeline from the v0.4–v0.9 research sequence. This is a new reference kernel with analytical tests, not a replacement for historical Gemini code or the source/observable slice in PR #9.

Parent repository inspected at `7942c3d7d348cbfe713bf71eba5a6a4bf9ad50a3`. Basis: [G0-B protocol](../../protocols/G0_B_BLINDED_PROTON_TRANSMISSION_AND_ALPHA_ESCAPE_PROTOCOL_v0_1_2026-10-27.md). The project lead explicitly redirected the work to conventional, laboratory-reproducible proton–boron physics. No exotic spectral operators, acoustic gains or collector-efficiency assumptions enter this kernel.

## What runs

- Proton transmission through an explicitly ordered planar material stack, using a separate range table for each material and species.
- Alpha propagation from a supplied birth layer, depth, energy and direction to the beam-upstream or beam-downstream interface, with support/substrate loss included. Alpha births are supplied inputs; no reaction-rate or decay generator is claimed.
- Forward folding of expected true-bin counts through a nonnegative single-hit detector response, retaining detection losses and measured background separately.
- Per-layer primary energy-loss accounting, source/table identity, domain checks and independent analytical fixtures.

The actual beam distribution, target characterizations, range tables and detector response must be provided before this can make a physical prediction. **All executable examples and current receipts are synthetic. TEST_A/TEST_B are artificial materials, not boron or BN.** The runner demonstrates refusal when a BN table is missing.

## Conventional approximation and reference definitions

NIST distinguishes CSDA path length from projected penetration depth. CSDA neglects energy-loss fluctuations; its range follows integration of reciprocal total stopping power. NIST tables express CSDA range in g/cm2, and mass stopping power in MeV cm2/g. References: [NIST definitions](https://physics.nist.gov/PhysRefData/Star/Text/appendix.html), [PSTAR/ASTAR methods](https://physics.nist.gov/PhysRefData/Star/Text/programs.html).

For a straight track with normal areal mass tau and direction cosine mu, path areal mass is tau/abs(mu). Within one layer, the deterministic residual energy is R_inverse(max(0,R(E_in)-path)). This is a range-table-dependent CSDA approximation. Multiple scattering, straggling and finite lateral boundaries are absent; projected range is not substituted for path range.

Range and inverse range use explicitly declared piecewise linear interpolation of the same monotone table. No interpolation-accuracy claim is made for a real material. No domain extrapolation is allowed. If a residual lies below the lowest reported positive-energy knot, the code refuses to invent a low-energy tail. A path longer than the supplied total CSDA range stops the primary; this does not require extrapolating an intermediate energy.

Geometric micrometres are converted to normal g/cm2 only with explicitly supplied density. Comparisons involving boron will additionally require independent B-11 atoms/cm2 and isotope/composition data; total mass alone is not reaction inventory.

## Accounting boundaries

The exact per-primary bookkeeping target is E_in = E_out + primary_energy_loss. **Primary energy loss is not automatically deposited calorimetric heat or recoverable electricity.** Its partition among target heating, excitation, secondary escape, recoil and storage is unresolved here. No nuclear Q is added because this module does not generate reactions.

Beam-upstream/downstream labels refer to the incident proton axis. For negative alpha direction cosine, preceding layers are traversed in reverse order. Exactly tangential trajectories are rejected because the infinite-slab geometry has no finite lateral exit. A stopped alpha has no exit face.

The response matrix columns correspond to declared true energy bins and rows to measured bins. Columns may sum to less than one; the deficit remains non-detection. Bin migration and background are explicit. No inverse unfolding, solid-angle correction, spectrum inference or Poisson independence is silently assumed. Expected counts are conditional on the supplied angular acceptance, geometry, species and exposure; an actual calibration must specify these in its external response record.

## Executed verification

**21 tests passed** in Python 3.12.14 with NumPy 2.3.5. The deterministic suite checks:

- Constant synthetic mass-stopping oracle E_out=max(0,E_in-S*tau/mu), including stopping and obliquity; split-layer invariance and material-specific multilayer loss.
- Upstream/downstream alpha paths, substrate orientation and invalid birth coordinates.
- Independent uniform-depth, isotropic, fixed-range slab formula: P_escape=1-L/(2R) for L<=R; R/(2L) otherwise. The actual transport function is used in the numerical quadrature.
- Input-hash mutations, projected-range/unit-header rejection, missing material/species, invalid monotonic tables, table limits and floating overflow.
- Identity and migrating detector response; missed counts, measured background under zero signal, invalid response probabilities, species mismatch and overflow.
- Deliberately incorrect omission of the oblique-path factor and changed stopping strength produce detectable disagreement with the analytical oracle.

Reference run maximum constant-stopping discrepancy is 4.44e-16 MeV. The slab grids 30/60/120 show finite discretization error; for L=R the finest result is 0.4976389 versus 0.5, absolute error 0.0023611. This is a numerical fixture result with a conservative 2/n acceptance bound; it is not a physical uncertainty estimate or a continuous-convergence proof. Sharp escape boundaries and floating-point equality affect boundary cells.

For the synthetic detector example, 150 true expected particles produce 125 detected signal counts and 25 missed counts; adding backgrounds [3,4] gives measured expectations [78,54]. Closure residual is approximately 1.07e-14 counts from floating-point arithmetic. Lost counts are not renormalized into detector efficiency.

The first passing run is retained under `receipts/run_001`, including snapshots of the two files later tightened for numeric input normalization and thickness-conversion overflow. `receipts/run_002` is the final authoritative run for the published root code; it also passes 21 tests. Both runs remain inspectable.

## Reproduction

From this directory:

```bash
python -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 python -m unittest discover -s . -p test_transport.py -v
OPENBLAS_NUM_THREADS=1 python run_reference.py --out /path/to/NEW_DIRECTORY
```

The output directory must not exist. The runner emits a test log and `REFERENCE_RUN_SYNTHETIC_ONLY.json` with parameters, code/input hashes, analytical comparisons, environment, data class and physical-readiness status. It makes no network calls. There is no RNG. Repeated test runtimes can differ; preserve each run under a new path.

`transport.py` uses the standard library; `detector.py`, tests and reference runner require NumPy. `run_reference.py` intentionally imports artificial fixtures from the test module: it is a verification runner, not a facility application. The package is not yet a containerized or cross-platform-qualified release.

Evidence-state fields are supplied declarations checked for consistency, not independent certification. Setting a label to CALIBRATED does not establish calibration. A reviewed source registry, experimental calibration receipts and physical input checks remain required.

## Inputs still required

See [input qualification register](INPUT_QUALIFICATION_v0_1.md). Next priorities are qualified proton stopping/transmission for one measured material stack, independently calibrated proton response, then qualified alpha transport/birth/response. Do not tune alpha yields to compensate for failed proton transmission.

No target-thickness optimum, detector-calibrated alpha spectrum, physical reactor gain or new blind prediction is produced by this version. The existing 41-point EXFOR alpha observable remains separate from an event cross section until its normalization is independently qualified.
