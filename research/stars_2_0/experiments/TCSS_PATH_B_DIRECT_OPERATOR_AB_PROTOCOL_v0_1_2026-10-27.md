# TCSS / Path B — Direct-Operator A/B Protocol v0.1
**Atlas Lattice / STARS 2.0 • New append-only research artifact • Proposed, not run**
**Purpose:** Implement and test the *actual user-authored TCSS / Path B operator*, not merely the generic 1,728-node graph Laplacian. No physical membrane or fusion claim.

## Fixed original source lineage
- [TCSS-121212 working baseline v1.1](https://github.com/atlaslattice/manus-artifacts/blob/3c9cbcbd4c7c76b75d090fbfc627d452f4cb1fa6/archive/research/math/tcss/TCSS_121212_WORKING_BASELINE_v1_1_2026-05-21.md)
- [PATH_B v0.2 task](https://github.com/atlaslattice/manus-artifacts/blob/3c9cbcbd4c7c76b75d090fbfc627d452f4cb1fa6/archive/research/math/tcss/PATH_B_v0_2_NUMERICAL_SWEEP_TASK_2026-05-21.md)
- [Rainbow lattice math refinement v2.2](https://github.com/atlaslattice/manus-artifacts/blob/3c9cbcbd4c7c76b75d090fbfc627d452f4cb1fa6/archive/math/RAINBOW_YINYANG_LATTICE_MATH_REFINEMENT_v2.2_CANDIDATE_2026-05-20.md)
- [Independent finite-torus base benchmark](../reviews/GPTWORK_FINITE_TORUS_BENCHMARK_v0_1.md) (on draft PR #8, not yet merged).
- [Draft contract v0.3](../contracts/GPTWORK_IMPLEMENTATION_CONTRACT_CANDIDATE_v0_3.md) (on PR #8). Do not infer that relative linked files exist on default branch until merged.

## Operator to reconstruct
```math
H_B = \alpha H_{xp}+\beta(-\Delta_{tor})+\gamma\hat L_z+\varepsilon\hat X_z\hat L_z
```
Baseline parameters quoted: alpha=0.5, beta=pi, gamma=0.3, epsilon=0.1; 12x12x12 periodic product torus (1728 states). The preceding finite graph Laplacian tested 6I-A; **sign convention of minus-Delta versus positive graph Laplacian must be pinned explicitly**.

### Stop gate: recover full operator definitions
The reviewed May 21 baseline and Path B task provide the symbolic terms and numerical parameters but **not enough explicit finite-matrix entries** to unambiguously reconstruct `H_xp`, `L_z`, and `X_z`. Before implementation, locate the original numerical code and receipts (likely earlier Path B v0.1 source) or publish a *separately labeled candidate discretization*, preserving any departures. Do not invent a discretization and claim reproduction of the user's actual operator.

If `X_z` and `L_z` are separately Hermitian but noncommuting, their unsymmetrized product need not be Hermitian. Evaluate `||H_B-H_B†||`; examine whether original ordering, commutation, or symmetrized anticommutator `(X_z L_z+L_z X_z)/2` is intended. Do not silently alter ordering. Check periodic position-coordinate seam and angular-momentum domain.

## Explicit A/B/C/D tests
- **A:** conventional physically derived FEM/modal `M,C,K,B,C_{sensor}` with appropriate foil boundary conditions, or clearly labeled dimensionless control before measurements.
- **B:** plain graph Laplacian with exactly the tested 1728 periodic nodes, plus standard eigenmode reduction.
- **C:** full source-faithful TCSS H at baseline; include `H_xp` and `L_z`.
- **D:** full Path B `H_B` with position-weighted chiral `X_z L_z`, and ablations: gamma=0; epsilon=0; both=0. Distinguish the previous RH/GUE spectral-spacing hypothesis from control-response utility. No assumed effect direction.

Gate 0: identity of every term; actual sparse/dense matrix reproducibility; operator sign and units; hermiticity, eigensystem residuals and stable energy/time evolution. Gate 1: old source receipts reproduce or discrepancies logged. Gate 2: gamma/epsilon 5x5 sweep per Path B task, independent spectral-statistic comparators, degeneracy, numerical stability, full eigenspectrum where feasible. Gate 3: fixed actuator/sensor pairs and transfer function `C( K-omega^2 M+i omega D)^{-1}B` ONLY if a physically justified mapping from operator to dynamical stiffness exists; do not insert `H_B` into a mechanical equation without dimension and positivity checks. Gate 4: physical plate/foil experiments, measured transfer functions, held-out specimens and batches; stress/fatigue inference independently validated. Gate 5: compare error/runtime/DOF and reject utility claim if TCSS doesn't beat standard comparator under preregistered criteria.

**Critical warning:** Matching eigenvalues, GUE-like spacing, Riemann-zero analogies, heat traces, or finite torus identities does not establish a material actuator advantage. The direct scientific target is independently reproducible mathematics first; physically predictive membrane mapping second.

## Required outputs (new version names)
1. `TCSS_PATH_B_SOURCE_DEFINITION_REGISTER_v0_1.md` with source, exact formula/matrix, units, ambiguity and sign.
2. `tcss_path_b_direct_operator_v0_1.py` *only after source recovery*; standalone executable with tests and saved seed.
3. `TCSS_PATH_B_ABLATION_RECEIPT_v0_1.json` with all A/B/C/D outcomes including failures and timing.
4. `TCSS_PATH_B_PHYSICAL_MAPPING_GAP_v0_1.md` preserving no-mapping/null outcome.
5. Subsequent independent review and explicitly versioned iteration, with all originals unchanged.

**Disposition:** YES, implement and test *the user's operator itself*, but do not call the generic Laplacian a direct test of full TCSS/Path B. This protocol is an exploratory plan, not an implementation or performance receipt.

**Wizard line:** The hat is spectral; the matrix entries still need identification. ☕🧙‍♂️
