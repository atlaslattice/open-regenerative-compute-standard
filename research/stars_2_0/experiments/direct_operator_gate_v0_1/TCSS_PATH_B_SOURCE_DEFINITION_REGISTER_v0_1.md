# TCSS / Path B / SHUGS source-definition register v0.1

STATUS: REVIEW — partial reconstruction; historical TCSS matrix gate blocked  
CANON: no · DEPLOYMENT: no · AUTHORITY: none · PROOF: no  
Date: 2026-10-28. Existing artifacts are preserved.

## Refreshed lineage

The target repository was refreshed at `7942c3d7d348cbfe713bf71eba5a6a4bf9ad50a3`, including Tidal Lantern's three-lineage probe and PR #9 independent review. Tidal had already identified the two SHUGS implementations, their window/scaling differences and the isolated last node using an independent numerical transcription. The present companion adds execution of the exact pinned historical Python files and controlled scale/window comparisons; it does not claim those observations as new discoveries.

Three distinct constructions must remain distinguishable:

| Lane | Source | Recovered executable definition |
|---|---|---|
| Historical SHUGS HSUF | `atlaslattice/element-145/shugs/shugs_core.py` | Yes; executed here |
| Packaged Element-145 HSUF | `atlaslattice/element-145/element145/shugs/operator.py` | Yes; executed here |
| TCSS / Path B | `atlaslattice/manus-artifacts/archive/research/math/tcss/` | Symbolic formula only; full finite terms unresolved |

The project lead's SHUGS pointer led to the `element-145` sources. Historical naming varies across documents; an acronym expansion does not establish that operators are equivalent. The 145-dimensional HSUF construction is not the 1,728-dimensional TCSS operator.

## Public pinned sources

TCSS parent commit: `3c9cbcbd4c7c76b75d090fbfc627d452f4cb1fa6` in `atlaslattice/manus-artifacts`.

- `archive/research/math/tcss/TCSS_121212_WORKING_BASELINE_v1_1_2026-05-21.md`, blob `7ef7c367a5980e7dc8d138c7e54c71370e6cf0af`.
- `archive/research/math/tcss/PATH_B_v0_2_NUMERICAL_SWEEP_TASK_2026-05-21.md`, blob `1d5df7de24e91950ef0e96530d3f1af79e77bf12`.
- Earlier Path B task at commit `60672ceb44fa82ef7b7c469ed6633f1b2d844a5c`, blob `d69e1266324850794f9ef28ddd6f2a3932c4cc66`, also gives the symbolic expression without finite entries.

SHUGS parent commit: `42e640e8b79bdc8d58af19946d3b9ede825af042` in `atlaslattice/element-145`.

- `shugs/shugs_core.py`, blob `03357c2085b333b1abbc7fd2b8df6a19bdc346f0`, SHA-256 `05ec9fbcaec930f954b581af67d460c7105909270735292e8c5cd63c80c1bfee`.
- `element145/shugs/operator.py`, blob `116b725bbf98c037ca015e0f73cebd203e21ad6c`, SHA-256 `731e9aa6be6be27b3d2685d755175530a6d0ab62580e555567df335fc9fbca3b`.

Git blobs and SHA-256 were checked before execution. Original source files remain external inputs; this companion does not vendor or relicense them.

## TCSS finite-matrix stop gate

The recovered expression is H_B = alpha H_xp + beta(-Delta_tor) + gamma L_z + epsilon X_z L_z, with alpha=.5, beta=pi, gamma=.3, epsilon=.1.

| Term | Recovered | Still required |
|---|---|---|
| Product graph | Twelve periodic sites on each of three axes, 1,728 states | Exact basis ordering in old code |
| Laplacian | Independent graph source defines positive L=6I-A | Resolve whether historical `-Delta_tor` means L or -L; no silent substitution |
| H_xp | Symbolic name | x and p matrices, factor 1/2 or other normalization, axes, discretization, lattice spacing, seam and domain |
| L_z | Symbolic name | Entries, signs, angular-momentum definition and coordinate factors |
| X_z | Third-axis modulation described | Coordinate values/origin, normalization, seam convention, tensor placement |
| Inner product | Not pinned by summaries | Euclidean or weighted metric; adjoint depends on this choice |
| Units | Baseline numbers only | Dimensionless declaration or consistent term units and coefficient dimensions |
| Trace/statistic terms | Names and partial formulas | Definitions of R, Omega+, M, K_tor, G, unfolding, sectors, degeneracy and target selection |

The directory history contains three May-21 commits introducing/expanding these summaries; neither initial task nor current summary provides the original PATH_B_v0.1 numerical implementation. Repository search is not proof of global absence. Broader SHUGS archive lookup recovered executable HSUF sources, but those do not fill the missing TCSS terms.

The positive graph heat-trace expression in the baseline is consistent with beta L under the graph convention, but that is a consistency clue, not recovery of the historical Hamiltonian sign.

## Conditional algebra worth testing before reconstruction

For Hermitian X and L, `(XL)^dagger = LX`; their unsymmetrized product is Hermitian exactly when they commute. If X_z acts on the third tensor factor and L_z acts on the first two, they commute identically. Thus the ordering issue is conditional, not an established defect. Silent replacement by an anticommutator would change a noncommuting historical model.

The diagnostic script uses explicitly NEW illustrative matrices only: central-difference momentum on a twelve-site periodic axis, branch coordinates 0,...,11, unit spacing and hbar, and a tensor-factor angular term. It does not assemble or label these examples as the historical H_B.

Executed examples show:
- Tensor-separated X_z and L_z commute and their product is Hermitian.
- A noncommuting two-dimensional Hermitian pair has an anti-Hermitian product with eigenvalues +/-i; the guard rejects it before `eigh`.
- Finite matrices cannot obey [X,P]=iI exactly: trace of any commutator is zero, while trace(iI)=iN. Cauchy-Schwarz gives Frobenius residual at least sqrt(N).
- Twelve-site central-difference momentum has two zero modes; the positive graph Laplacian has one. P squared and L are different discretizations (max entry difference 1.5 in the illustrative convention).
- A consistently translated coordinate seam preserves operator covariance. Fixed physical input/output maps must transform too to preserve observables.
- In a degenerate eigenspace, an odd observable's expectations can change from 0,0 in a parity-adapted basis to +1,-1 after rotation. Any historical per-eigenvector L_z-collapse test needs a stated basis/sector convention.
- The task's delta_c ratio obeys a triangle-inequality bound [0,1] when its denominator is positive. Zero can reflect cancellation of positive/negative spectral contributions, and a zero denominator needs an explicit undefined state. This ratio alone does not establish physical chirality.

These are finite algebraic consequences and illustrative checks, not new mathematical theorems or verification of the full TCSS model. Eleven diagnostic conditions passed; the historical reconstruction state remains BLOCKED.

## Recovered HSUF definition and semantic limits

With zero-based indices, both recovered files use a diagonal built from Lambda(i+1), prime-power exponential smearing at weight .3 and decay 18.9, and .15 log(i+2). Their off-diagonal kernel uses the first twenty stored zeta ordinates through sum_k cos(gamma_k log(|i-j|+1))/gamma_k, times coupling .05 and a source-specific scale.

The core source takes the scale from the completed diagonal and applies diag(hann) H_raw diag(hann), normalizing its window maximum. The package takes the scale from positive bare Lambda values and applies sqrt(hann_i hann_j) entrywise. These are distinct operators. Zeta ordinates are explicit inputs: matching their features cannot be treated as independent prediction of the input zeros.

Both return real symmetric matrices. Calling them Hermitian is correct; that property alone does not establish GUE universality, physical damping, positive stiffness, efficient routing or useful control. The legacy score's unfolding and filtering remain unqualified statistical choices here.
