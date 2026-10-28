# SHUGS direct-source review v0.1

STATUS: REVIEW — direct byte-pinned numerical execution  
CANON: no · DEPLOYMENT: no · AUTHORITY: none · PROOF: no  
Date: 2026-10-28. Physical validation not run.

## Result and prior independent work

The exact pinned historical SHUGS and packaged Element-145 source files reproduce the central calculations in [Tidal Lantern's earlier three-lineage probe](../../reviews/SHUGS_E145_TCSS_THREE_LINEAGE_NUMERICAL_PROBE_v0_1_2026-10-27.md). This is an additional execution receipt, not a claim that its reconstruction was newly discovered here.

| No-jitter calculation | Historical core | Packaged HSUF |
|---|---:|---:|
| N144 legacy GUE-KS | 0.2941819211 | 0.2424563673 |
| N145 legacy GUE-KS | 0.2669144127 | 0.1822648251 |
| N145 final-node off-diagonal L1 norm | 0 | 0 |
| N145 seed42 legacy GUE-KS | 0.2674634545 | 0.2458946788 |
| N145 seed42 minimum eigenvalue | -0.0777321902 | -0.0364911847 |

The prior no-jitter scores agree within the precision printed in Tidal's probe. All eight source-run eigensystem residuals are below 1e-12. The score is computed with the historical core metric for both sources to keep that comparator fixed. No KS significance or universality inference is made.

The N145 matrix relative Frobenius difference is 0.2795994312 and sorted eigenvalue maximum difference is 3.1436914429. A 2x2 factorial comparison of coupling scale (bare Lambda versus completed diagonal) and window weighting (hann versus sqrt(hann)) reconstructs both source matrices to entrywise error below 1e-12. The differences are explicit construction choices, not merely random seed noise.

## Coupling claim: fails for these matrices

Hann endpoints are zero. Both weight every edge touching either endpoint by zero. The first and last nodes therefore have zero off-diagonal connections; without jitter they are complete zero rows. Adding diagonal jitter changes their diagonal energy but cannot connect them to other nodes.

The package's `admin_sphere_coupling()` returns twelve zeros at N145. A shift-i resolvent applied to the final node has exactly zero response on all other nodes in both implementations. This is an algebraic connectivity check, not a membrane transfer calculation.

The no-window package control restores final-node coupling. It is a controlled new comparison using an existing explicit source parameter, not a replacement historical model or proposed production fix.

The source report's interpretation of node145 as a load-bearing coupling node is unsupported by these particular windowed matrices. This says nothing by itself about a separate governance implementation. Also, changing N modifies the whole construction, including smearing, scaling and the window; a favorable N145 spacing score cannot isolate the causal contribution of a last-node edge that is absent.

## Physical mapping remains open

The seeded examples have negative eigenvalues. Used unchanged as K with M=I in an undamped mechanical equation, a negative eigenvalue would produce an unstable mode. This does not make a dimensionless Hermitian research operator mathematically invalid; it prevents an automatic claim that it is a stable stiffness operator. A shift, projection or different dynamical interpretation would be a separately versioned modeling choice requiring justification.

Multiplying by a real window is not a physical absorbing boundary: the resulting Hermitian matrix still generates norm-preserving Schrödinger evolution. No damping, material constitutive law or actuator model has been established.

## Refresh reconciliation and next useful work

The target repository was refreshed at `7942c3d7d348cbfe713bf71eba5a6a4bf9ad50a3` before this companion was prepared. Relevant new work includes:

- Tidal's SHUGS/E145/TCSS probe: direct-source receipt gap now narrowed here; full TCSS definitions remain missing.
- Atomic/nuclear data-to-SHUGS design note: a useful typed-data bridge requirement, not a validated physical unification.
- PR #9 review: independently corroborates covariance mathematics; requests stronger curated semantics, energy-domain inference, numerical robustness and reproducibility as future versioned work.
- Fractal Path/mycelial prototypes: separate simulated research workflow. The v0.4 receipt explicitly says its code itself was not uploaded, despite locally reported 23 tests. No deployment or physics inference follows.

A productive cross-domain addition is to measure whether source-linked cross-domain retrieval helps recover *operator definitions*, rather than scoring a routing metaphor by GUE-KS. A held-out task set could compare ordinary lexical retrieval, graph retrieval and the mycelial proposal at equal budget using exact source recovery and correct missing-definition detection as outcomes. That is a proposed benchmark, not an executed benefit.

For spectral utility, keep three follow-ups distinct: recover TCSS's exact matrices; qualify spectral statistics with independent comparators and holdouts; test control response only after a physical M,C,K and input/output mapping exists. A hybrid is a new fourth construction with explicit lineage and ablations.

## Reproduction

Dependencies tested: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0. Retrieve the two external source files from the pinned `atlaslattice/element-145` revision in the source register, preserving exact bytes.

```bash
OPENBLAS_NUM_THREADS=1 python shugs_source_audit_v0_1.py \
  --core /path/to/shugs/shugs_core.py \
  --packaged /path/to/element145/shugs/operator.py \
  > NEW_SHUGS_receipt.json
OPENBLAS_NUM_THREADS=1 python operator_definition_diagnostics_v0_1.py \
  > NEW_definition_gate_receipt.json
```

Choose new output filenames; shell redirection otherwise overwrites an existing file. The scripts themselves only emit stdout and do not mutate inputs. Source hashes are checked before import. Receipts record code hashes, dependencies, parameters, seeds and limitations. No private archive bodies are republished. Original code is external and retains its own attribution/rights.

Nine direct-source diagnostic conditions and eleven illustrative algebraic conditions passed. The historical admin-coupling hypothesis fails for these windowed matrices. Full TCSS, historical ensemble replication, the old 0.0527 score, physical membrane performance and scientific freeze remain unestablished.
