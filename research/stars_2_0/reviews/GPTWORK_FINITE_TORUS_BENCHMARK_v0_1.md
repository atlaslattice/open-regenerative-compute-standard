# Finite-torus spectral benchmark v0.1
Status: exploratory analytical/numerical validation; no physical membrane validation.
Date: 2026-10-28 UTC. Append-only companion to implementation-contract candidate v0.3.

## Source and scope
[Atlas lattice mathematical source](https://github.com/atlaslattice/manus-artifacts/blob/3c9cbcbd4c7c76b75d090fbfc627d452f4cb1fa6/archive/math/RAINBOW_YINYANG_LATTICE_MATH_REFINEMENT_v2.2_CANDIDATE_2026-05-20.md), pinned commit 3c9cbcbd4c7c76b75d090fbfc627d452f4cb1fa6, source Git blob b2d8897ea84c8d6b21c706d3859d61402d594e7c.

The recovered operator is L = 6I - A on the periodic nearest-neighbor graph (Z/12Z)^3: 1,728 nodes. Its Fourier eigenvalues are lambda(k) = 4 sum_j sin^2(pi k_j/12). They are nonnegative, span [0,12] and have one zero mode. These are dimensionless graph quantities, not measured specimen frequencies.

The script assembles sparse coordinate edges independently of the Fourier symbol. It checks selected Fourier eigenpairs, sparse-matrix heat propagation against FFT propagation, impulse positivity and mass, and undamped wave energy with M=I and K=L. Positivity of the entire spectrum follows from the analytical expression; this run does not independently diagonalize the full dense matrix.

## Executed results
All ten numerical checks passed at the declared regression tolerance 1e-10. This tolerance is a numerical fixture choice, not an experimental acceptance threshold.

| Check | Result |
|---|---:|
| Symmetry / constant-mode residual | 0 / 0 |
| Maximum residual, four selected Fourier modes | 7.963e-14 |
| Sparse versus FFT heat propagation maximum difference | 9.992e-16 |
| Impulse mass absolute error | 0 |
| Minimum impulse heat value | 4.169e-17 |
| Relative undamped wave-energy error | 9.492e-16 |
| Positive spectral gap, analytical symbol | 0.26794919243112264 |

Environment: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, OPENBLAS_NUM_THREADS=1. Seed 20261028. Heat time 0.37; wave time 0.81. Parameters, metrics, checks and script SHA-256 are in the machine receipt.

## A useful counterexample: the spectrum is not the response
For K1=diag(1,4), K2=R K1 R^T with a 45-degree orthogonal rotation, M=I and a fixed collocated force/sensor b=(1,0), the eigenvalues agree to 8.882e-16. Yet the static compliance b^T K^-1 b is 1.000 for K1 and 0.625 for K2.

This is a standard linear-systems consequence, not a new physical discovery. It demonstrates why a spectral match alone cannot validate membrane control. Rotating the operators while keeping the physical forcing and sensor fixed changes their coupling to the modes. If all coordinates and input/output maps were rotated together, the observable would be unchanged.

## Next experiment and falsification
Identify a specimen's M, C, K, boundary conditions and actuator/sensor maps, carrying uncertainty. Compare conventional modal/FEM reduction against the proposed spectral reduction at equal training information and computational cost. Hold out complete specimens or acquisition campaigns and drive conditions. Measure transfer magnitude/phase and displacement/strain; treat stress and fatigue as model-inferred quantities with additional validation.

Reject the proposed reduction's utility claim if it fails the prespecified accuracy/cost comparison or if apparent gains vanish on grouped holdouts. Test sensor/actuator placement through noise-aware practical identifiability before selecting an experimental configuration.

## Explicit limits
This does not implement or validate the full TCSS H_B or Path B construction, its xp-like terms or domain choices. It establishes no Riemann-zero, random-matrix, local-smoothing, material-survival or fusion-enhancement claim. The OpenAI local-smoothing lead remains a separate theorem-applicability investigation. The 3D periodic graph has no demonstrated mapping to a bounded physical membrane.

Heat evolution is an analytical benchmark here, not a claim about membrane thermal transport. The undamped wave equation is a dimensionless toy. This is an independent implementation of the stated formulas, not an independent institutional audit.

## Reproduction
Files in ../experiments/:
- finite_torus_benchmark_v0_1.py
- finite_torus_receipt_v0_1.json

Run: OPENBLAS_NUM_THREADS=1 python finite_torus_benchmark_v0_1.py
The script emits JSON to stdout and exits nonzero on a failed check. Save reruns under new filenames; preserve the recorded receipt. Floating-point last digits can vary by platform. No existing research artifact was overwritten.
