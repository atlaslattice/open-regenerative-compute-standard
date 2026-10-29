# Measured stopping calibration and exact Gemini source reproduction v0.6

2026-10-29 America/Chicago. Additive draft stacked on coupled reference v0.5 / PR #27. No historical source, measurement, assumption or result is replaced. No scientific or blinded-prediction freeze.

We can start calibrating with actual measurements now. This release fits a tightly scoped stopping correction to the recovered experimental curve and completes exact-source reproduction of the earlier sequential generator. It does **not** label the whole apparatus calibrated.

## What was calibrated

The 27 stopping points were digitized in v0.3 directly from Figure 7, printed p82 / PDF p87 of Jack Castle Overley's Caltech PhD thesis (1961), [DOI 10.7907/XZP6-5P63](https://doi.org/10.7907/XZP6-5P63), [original repository](https://thesis.caltech.edu/6305/). The fixture and source hash are preserved in `OVERLEY_BENCHMARK.json` and the earlier source versions. These are measured proton energy-loss data reconstructed from a plot, not raw digital laboratory observations. The original target was 95.96 atom% B10 and 4.04 atom% B11. The fitted energy domain is 0.09898212970495418–2.964723145468535 MeV LAB.

For each of the two calculated cold stopping replays from v0.4, fit one positive scale `a` to **total** stopping by minimizing the unweighted mean squared logarithmic discrepancy. The analytic solution is `a = exp(mean(log(measured / model)))`. No statistical per-point weights or likelihood are invented. This is a descriptive calibration against one historical dataset, not an independent validation or a new physical decomposition into electronic and nuclear stopping.

| Model replay | Fitted total scale | RMS fractional discrepancy before | After |
|---|---:|---:|---:|
| SRIM96 + ZBL | 1.028252 | 3.305% | 1.915% |
| SRIM13 + ZBL | 1.073454 | 6.937% | 1.272% |

These are fit residuals, not parameter uncertainties or total prediction errors. The fitted scale can absorb source normalization, digitization and physical model discrepancy. The model generations may already include this historical experiment in their calibration ancestry. The smaller fitted residual does not prove that one underlying stopping model is universally better.

The callable `adjusted_stopping` requires this proton/target identity and supported energy range; it rejects alpha, B11, BN, hot-target and out-of-domain transfer. It returns adjusted total stopping, with fitted Se/Sn decomposition and confidence interval explicitly null. Previous v0.5 transport results remain unchanged. No fitted scale is automatically applied to its B11 or BN simulation.

## Checks that challenge the fit

Three contiguous energy blocks of nine points each are excluded in turn, and the scale is refit to the other 18 points. All blocks come from the same source, so these are **retrospective within-source diagnostics**, not independent campaign holdouts or blinded tests. All data had been inspected before this diagnostic design. Held-out outcomes do not enter each fold's scale fit; a mutation test checks that property.

| Replay | Held-out block | RMS before | RMS after training on other blocks |
|---|---|---:|---:|
| SRIM96 | 0.099–0.471 MeV | 2.275% | **2.960% — worse** |
| SRIM96 | 0.530–1.542 MeV | 3.379% | 1.427% |
| SRIM96 | 1.746–2.965 MeV | 4.021% | 2.138% |
| SRIM13 | 0.099–0.471 MeV | 7.611% | 1.373% |
| SRIM13 | 0.530–1.542 MeV | 6.674% | 1.335% |
| SRIM13 | 1.746–2.965 MeV | 6.474% | 1.558% |

The worsened SRIM96 low-energy block is preserved. One scale does not remove all energy-dependent model discrepancy.

The author's reported 4% probable error is not converted into a Gaussian standard deviation. Full covariance and raw beam/target calibration are unavailable. Eight coherent stress cases combine source scales 0.96/1.04, stopping-axis offsets ±0.08e-15 eV cm2/atom and energy-axis shifts ±0.008 MeV. The last two are explicit digitization analysis allowances inherited from v0.3, not recovered measurement standard errors. Resulting fitted-scale ranges are 0.9580–1.0995 (SRIM96) and 1.0000–1.1479 (SRIM13). They are **not confidence intervals** and do not bound every possible systematic. No independent point noise is manufactured to average down a shared systematic.

## Exact original sequential-source reproduction

Recovered the original project-lead attachment `Pasted markdown(20261028-014210).md` (37,431 bytes) and preserved it as `original/GEMINI_V04_ATTACHMENT.md`, including existing encoding artifacts. SHA256: `3e07fde07ecf899f0ca550e5d8ea4e817ce691588051a95f2819e70d0c52df4d`.

Removing only the first and last Markdown fence lines yields the unchanged 760-line Python file, SHA256 **`2db27298ea7f11c24cf891b4b784a5e21a8417c0207a3089f51bd037c44e522e`**. This exactly matches Tidal Lantern's [independent execution record](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/4512e9bb8505591ea207d28c2f0689ab5aecae9f/research/stars_2_0/reviews/GEMINI_V04_INDEPENDENT_EXECUTION_AND_AB_REGRESSION_GATES_2026-10-27.md). It still differs from Gemini's earlier claimed `0fdfcc...` hash; that discrepancy is preserved rather than silently reconciled.

The original executes with Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0. Both original bundled tests pass. All five CSVs reproduce byte-for-byte over repeated executions, with row counts 200 / 5 / 16 / 4 / 3. Source seed is 20261027; the bundled conservation test separately uses seed 42. The original acoustic PDE CSV is retained solely as part of this execution receipt, not promoted as calibrated membrane physics.

The three sampled optima reproduce: rear escaping energy 5.5 µm, full-sphere escaping energy 6.0 µm, and collector accepted energy 7.0 µm. These remain surrogate outputs, not validated apparatus optima.

### Independent physical-mass gate: FAIL, preserved

The source's internal residuals are tiny because it uses an effective boron mass, scaled velocity vectors and Galilean boosts. Independently reconstructing relativistic longitudinal momentum from its exported alpha kinetic energies and polar cosines, using the pinned physical masses from v0.5, gives:

| Check on original 200-event export | Maximum absolute residual |
|---|---:|
| Internal scaled momentum | 4.44e-16 in internal scaled units |
| Internal kinetic-energy balance | 3.55e-15 MeV |
| Physical energy balance | **5.5915e-4 MeV** |
| Physical longitudinal momentum | **4.7153e-2 MeV/c** |

Both physical residuals exceed the previously stated numerical gate of 1e-8 MeV (or MeV/c). The historical B11 mass uncertainty and the original rounded Q cannot explain away a claim of exact physical four-momentum closure. Full physical momentum cannot be reconstructed from this CSV because alpha azimuths/full vectors are absent; the longitudinal failure alone suffices to reject exact closure. The source's fixed branching and line shape also remain uncalibrated. Its thickness sweep still uses separate hard-coded spectral bins rather than these generated events.

The original is retained unchanged and is **not** substituted for the v0.5 phase-space control. The next source implementation must be a separately versioned Lorentz-covariant sequential generator with physical masses, explicit channel/width/angular assumptions and full birth four-vectors, followed by a fit at the published measurement boundary. Merely adjusting Q or renaming the old residual is insufficient.

## What the existing citations can and cannot calibrate

| Component | Available measurement/source | Current permitted use | Remaining gate |
|---|---|---|---|
| Cold proton stopping in historical boron | Overley 1961, 27 reconstructed points | Source-specific total-stopping calibration in this release | Independent experiment; isotope/compound/temperature transfer |
| p–B11 event normalization | [Sikora–Weller 2016](https://doi.org/10.1007/s10894-016-0069-y), 41 reconstructed event nodes | Publication-model-derived normalization already runnable | Consistent sequential source; shared source covariance; narrow-resonance resolution |
| Alpha energy/angle spectra | [Spraker et al. 2012](https://doi.org/10.1007/s10894-011-9473-5), 22,100 recovered spectrum cells plus matching statistical errors | Fit targets with frame, source-bin and acceptance qualifications | Source repair; energy-dependent CM/LAB mapping and acceptance; covariance and background |
| Alpha stopping in B / BN | Calculated SRIM96/13 + ZBL replays; historical measured-alpha leads identified | Explicit calculated-model sensitivities | Recover original measured-alpha numbers and qualify material identity |
| Detector response in new apparatus | Literature descriptions, synthetic matrix currently implemented | Verification / experimental design | Measured gain, resolution, dead layer, efficiency, solid angle, threshold, background and live time |
| Acoustic conditioning and stacked modules | Existing literature/module register retained | Mechanism-specific comparisons and experimental controls | Target-specific mechanical/laser/proton diagnostics; sham-controlled all-attempt measurements |
| Sustained burn and wall-plug net power | Accounting modules and conditional drive tracks retained | Energy-boundary checks and scenario screens | Validated plasma/target evolution, feedback/self-heating and measured auxiliary loads |

The 2016 evaluation reuses earlier reaction data and assumes a sequential l=3 source to extrapolate low-energy alphas. It is not an independent validation set for the 2012 spectra. The 2012 workbook has LAB incident proton energies, CM alpha energies and a CM differential quantity per original source bin; a LAB detector angle label does not authorize multiplying those values by LAB solid angle. Zero cells outside unqualified acceptance do not establish zero physical emission. These distinctions prevent fitting the wrong observable.

## Reproduce

This directory is expected beside the preserved `stopping_models_v0_4` and `coupled_reference_v0_5` directories on the stacked branch. Dependency hashes are checked before fitting or auditing the original.

```bash
python -m pip install -r calibration_reference_v0_6/requirements.txt
python calibration_reference_v0_6/reproduce_gemini.py --out calibration_reference_v0_6/receipts/new_original_run
python calibration_reference_v0_6/calibrate.py --out calibration_reference_v0_6/receipts/new_calibration_run
python -m unittest discover -s calibration_reference_v0_6 -v
```

Output directories must be new; earlier runs are never overwritten. `receipts/gemini_original_run003` and `receipts/calibration_run002` contain the published reference outputs. Eleven new tests pass, in addition to the unchanged original's two bundled tests. Conservation failure in the original is an expected **scientific rejection**, not a failed verification-suite assertion or a calibrated-source success. No randomness is involved in fitting; original simulation seeds and all five CSV hashes are recorded.

## Decision

Proceed with source-specific measured-data calibration while keeping its material scope enforced. Preserve the failed source gate. Next repair the sequential source's kinematics, recover its literature-supported energy-dependent channel/angular model, and use the recovered spectrum cells in a response-aware joint fit. New target batches/calibration campaigns must be held out for actual validation. The published data can constrain components; they cannot by themselves settle ignition, acoustic enhancement or net electrical gain for a new laser apparatus.
