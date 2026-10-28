# ⚡ Project Frankenstein 1728 — First Ignition, Independent Executed Probe

**Date:** 2026-10-27 (America/Chicago) • **Status:** EXECUTED EXPLORATORY NUMERICS, NOT FULL HISTORICAL TCSS OR PHYSICAL CALIBRATION.  
**Authority:** project-lead approved the 1,728-state research direction; this is a **new** artifact, not a revision to old sources.  
**Local machine receipts:** `frankenstein_1728_v02.py` SHA-256 `dc4052e311dbaf281be2a0142e121c882b80d8ac88d653f11914c60c00f416da`; `FRANKENSTEIN_1728_EXPLORATORY_RECEIPT_v0_2.json` SHA-256 `61043e377ff4edad32dd0b85f548dc2af103601ad7e52aa65293119896b00472`. These are provided as downloadable conversation artifacts, **not yet source-code files committed to this repository**. Do not claim GitHub CI reproduced this experiment.

## Objective and code contract

At 12×12×12 states, form an independently generated positive periodic graph Laplacian `L`, and two explicitly NEW hybrid Laplacians:
- Original SHUGS matrix `H_144`, sourced by independently re-transcribing `atlaslattice/element-145/shugs/shugs_core.py`, is converted into an **unsigned graph Laplacian** `Q(H)=diag(sum_j |H_ij|)-|H_offdiag|`.
- Element-145 HSUF matrix `H_144`, sourced by independent transcription of `atlaslattice/element-145/element145/shugs/operator.py`, undergoes the same operation.
- Hybrid `A=L+0.15(I_12⊗Q(H_144))` with 144-state blocks along the first 12×12 slice; a new **candidate** embedding, not the historical physical, ontological or control interpretation.

The use of absolute values and row-sum diagonal **changes the original source spectra and physics**; we test a mathematical diffusion process to obtain numerical A/B controls, not source-faithful HSUF itself. The first two original mathematical transcriptions at N144/N145 were previously compared in [three-lineage probe](../reviews/SHUGS_E145_TCSS_THREE_LINEAGE_NUMERICAL_PROBE_v0_1_2026-10-27.md). Full TCSS `H_xp,L_z,X_z L_z` remains undefined from the recovered summary, **NOT EXECUTED**.

## Executed results — corrected stand-alone v0.2 harness

Environment Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, OPENBLAS_NUM_THREADS=1. Seed 20261028 for random zero-mean unit-norm state. Diffusion time 0.20; impulse at state 0. Metrics from locally executed receipt:

| Metric | L torus | SHUGS-derived hybrid | E145-derived hybrid |
|---|---:|---:|---:|
| Matrix dimension | 1728 | 1728 | 1728 |
| Sparse nnz | 12096 | 245640 | 245640 |
| Max symmetry error | 0 | 8.67e-19 | 0 |
| Max constant-null residual | 0 | 3.44e-15 | 5.33e-15 |
| Heat-evolved state L2 norm | 0.38733150565 | 0.38333205262 | 0.38320501896 |
| Impulse total after heat | 1.0 | 0.9999999999999999 | 1.0 |
| Minimum impulse value | 1.69e-21 | 1.78e-14 | 1.50e-13 |
| Number with impulse response > 1e-5 | 177 | 183 | 186 |
| Node 1 graph degree | 6 | 144 | 144 |

**6/6 Boolean toy regression checks PASS:** symmetry, constant null mode, total impulse mass, impulse nonnegativity, contractive heat evolution and numerically distinct baseline/hybrid dynamics. These six checks aggregate the three models and are **not** six independent experimental validations.

**No validated superiority result:** higher diffusion reach in this arbitrary toy at a chosen threshold does not prove better network throughput, robustness, material stress prediction, spectral theorem, nuclear yield or electrical efficiency.

## Failure and correction preservation

The first locally executed `frankenstein_1728_v01.py` harness imported another research script with top-level execution, creating an unwanted side effect: regeneration of an earlier v0.1 receipt (same results). It also specified a hypothetical node-removal perturbation without actually implementing that experiment. **These are harness defects; preserve the original v0.1 run and disclosures.** A new `frankenstein_1728_v02.py` uses copied self-contained source formula functions (with independent lineage) and marks node-removal `NOT RUN`. The attempted initial v0.2 edit produced a NameError for `idx`; this was immediately corrected in the same uncommitted working copy before successful execution; the executed v0.2 byte hash above applies to the successful result. No original GitHub historical files were changed.

## Next gates

1. **Source-faithful historical A/A runs:** original SHUGS and Element-145 imports without translated code, output/hash reconciliation and original-seed KS baseline.
2. **TCSS Path B source reconstruction:** recover exact `H_xp,L_z,X_z` matrices; refuse to label generic Laplacian as full Path B.
3. **Fair graph-control experiment:** explicitly model packets, graph construction from source operators, node-removal, fallback, optional observer and distributed versus centralized authority; report control-plane SPOFs separately from mathematical Hanning edge-zero artifacts.
4. **Uncertainty and selection:** source-qualified parameters and held-out tests, not post-selected maximum KS or fastest mixing.
5. **Physical experiments:** separate measured plate/foil transfer function `M,C,K`, calibrated actuator/sensor, and blind test before any material or fusion claim.

**Scientific freeze still blocked; PR #8/#9 remain separately governed.**

**Wizard disclaimer:** Igor pulled the switch. The numerical monster twitched. It still has to pass a physical exam. ⚡🧙‍♂️☕
