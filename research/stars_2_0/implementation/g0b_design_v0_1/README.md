# G0-B measurement design v0.1

2026-10-28. PHYSICAL_CANDIDATE. Synthetic design study, not a calibrated p–B prediction. New files only. Parent: stopping-source check PR #12, commit 470e81a26db95496757a27e4991556345772593e.

## Minimal configuration candidate

Use a conventional accelerator proton beam on a characterized, preferably self-supporting enriched boron-11 layer in vacuum. Self-supporting feasibility is OPEN; do not silently substitute a supported target. Any backing, oxide, contamination, window or detector dead layer must become an explicit characterized layer with its own transport inputs. Avoid BN in the first candidate because nitrogen adds transport and reaction channels. This choice is an engineering proposal, not proof that the proposed foil can be fabricated or survive.

Measure the incident beam spectrum, integrated charge with secondary-electron correction and live time; transmitted proton spectra; alpha spectra at two known angles; and separate detector efficiency/energy calibration. Include open-beam, no-target and backing-only controls where applicable. Record angular acceptance, resolution, pileup, dead time and particle identification. Charge normalization and composition uncertainties are not included in the toy calculation and must be added before physical inference. A beam stop may preclude simultaneous transmission acquisition: facility geometry and synchronized or interleaved acquisition remain unresolved.

No beam current, foil thickness, exact energy, angle, acquisition time or acceptance threshold is frozen. The existing reference calculation's 0.5–2 MeV grid is a numerical test range, not an approved experimental prescription. Choose operating points after qualifying the cross-section observable, excitation function, transport coverage and facility constraints. The alpha production observable remains distinct from fusion-event cross section; no implicit division by three.

`CONFIGURATION_CANDIDATE.json` makes unavailable measurements explicit nulls. Physical execution is blocked until its inputs and calibrations are supplied. No exotic operators, acoustic enhancement or energy-recovery claim enters this candidate.

## What was actually computed

Let t, p, a, n, e be positive dimensionless scales for areal density, proton stopping, alpha stopping, reported reaction normalization and efficiency. For a fixed thin-target geometry, assume three normalized observables:

- proton mean energy loss / reference = t p;
- alpha transport-induced mean energy loss / reference = t a;
- expected alpha signal / reference = t n e.

The last expression assumes known incident fluence and geometry. The alpha-loss observable requires an independently constrained birth distribution; it is not automatically measurable from a singles spectrum. These assumptions deliberately favor identifiability and are not an implemented reaction generator or detector fit. Energy-dependent stopping, reaction-depth distribution, branching, straggling, backgrounds and detection thresholds are omitted. A real spectrum may supply more information or more nuisance parameters.

Taking logs yields the explicit three-by-five matrix in `design.py`. Observations have independent Gaussian log errors (synthetic SD 0.03, 0.05, 0.08). Additional calibration SDs are assumed 0.02 for log areal density and 0.04 for log efficiency. These are sensitivity settings, not demonstrated laboratory precisions. No zero-count log transformation is permitted in a real count analysis; use a suitable count likelihood there.

Six designs were evaluated with noise-whitened SVD. Ranks: joint observables 3; repeating the same geometry 3; either one independent calibration 4; both calibrations 5. For rank-deficient designs uncertainty is null, not a pseudoinverse masquerading as a finite bound. With both calibrations, reaction-normalization log SD is 0.0916515; making both calibration errors ten times larger leaves rank five but increases that SD to 0.454313. Neither number is an uncertainty forecast for Stars.

Four verification groups passed: design ranks; independent algebraic variance oracle; exact finite multiplicative invariances; and a deliberately invisible model discrepancy. A +0.1 shift in log counts is fitted exactly as +0.1 reaction normalization with no residual. Thus full rank does not establish model adequacy. An independent held-out measurement with different discrepancy sensitivity is necessary. Merely repeating shots or angles with the same product dependence cannot cure these exact degeneracies.

The null transformations are t→ct, p→p/c, a→a/c, n→n/c; and n→dn, e→e/d. They provide explicit counterexamples rather than relying solely on numerical rank. Two angles help only if their modeled responses constrain distinct parameter combinations. No numerical angle recommendation follows from this toy.

## Decision and next acceptance gates

Prioritize independent areal-density/composition metrology and detector efficiency calibration alongside transmission. Before selecting additional angles, evaluate their marginal information with correlated calibration errors and realistic spectral response. Use grouped target-batch/calibration-cycle holdouts, preserve all shots and missing outcomes, and prohibit outcome-driven retuning of held-out predictions.

Next numerical release: replace the three scalar observables with transport-linked spectral bins; include beam-energy, fluence, birth-distribution and calibration nuisance parameters; test discrepancy alternatives and low-count likelihoods. Prior to physical validation, obtain independent measured foil transmission and alpha calibration data. No final acceptance precision is invented here.

## Reproduce

Python 3.12.14, NumPy 2.3.5. Run `python design.py --out receipts/new_run_name` from this directory. Output directory must not exist. No RNG, no external numerical dataset, no network needed. Results include source SHA256 and environment. Null-vector bases and tiny singular values can vary with BLAS; compare null spaces and stated rank/variance invariants rather than exact vector bytes. Review source register v0.2 for unresolved stopping inputs.
