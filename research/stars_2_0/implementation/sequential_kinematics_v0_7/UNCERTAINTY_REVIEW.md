# STARS uncertainty review v0.7

2026-10-29 America/Chicago. Focused source recovery accompanying the sequential kinematic repair; additive to earlier calibration records.

| Gap | Published evidence recovered or confirmed | What it closes | What remains open |
|---|---|---|---|
| Three-alpha decay law | Kuhlwein et al., Physics Letters B825(2022)136857, [DOI](https://doi.org/10.1016/j.physletb.2021.136857), full open paper recovered and hashed | Supplies a symmetrized R-matrix amplitude, coherent l=1/l=3 alternatives, and reported fit uncertainty | Raw exclusive events/acceptance and full fit covariance not recovered; even best fit has substantial discrepancy; rescattering omitted |
| New measurement campaign | Mazzucconi et al., EPJA61(2025)114, [DOI](https://doi.org/10.1140/epja/s10050-025-01589-3), Table2 transcribed directly | **28 numerical rows, 222 central/error numbers and one upper limit**; energy and yield errors retained | Single LAB angle; energy errors tied to FWHM comparison; shared covariance and event-multiplicity normalization require reconciliation; possible support alphas |
| Ground-state channel normalization | Munch et al., EPJA56(2020)17, [DOI](https://doi.org/10.1140/epja/s10050-019-00016-8) | Independent targeted alpha0 experiment; publisher says tabulated cross sections are in Table1 | Full numeric table not recovered in this pass; no new values imported; reference is a recovery target, not an empty dataset or a calibrated branch fraction |
| Cold alpha stopping in boron | Kamke & Kramer, Z.Physik168(1962)465–473, [DOI](https://doi.org/10.1007/BF01378142) | Primary abstract confirms experimental 0.2–5.3MeV coverage and about2% datum errors | Numeric stopping/range table remains unrecovered; target chemistry and uncertainty definition must be qualified before importing; not direct BN data |
| Warm dense boron stopping | Lahmann et al., PPCF65(2023)095002, [DOI](https://doi.org/10.1088/1361-6587/ace4f2), [MIT author-paper lead](https://www2.psfc.mit.edu/research/hedp/Papers/Lahmann_PFCF-2023.pdf) | Published experimental warm-boron stopping study exists; relevant alternative to cold-table transfer | Author PDF retrieval returned503 and web502 this pass; no numerical warm-target correction imported; not evidence for a BN acoustic gain |
| Thick-target impurities | Bikchurina et al., PPNL21(2024)390–394, [DOI](https://doi.org/10.1134/S1547477124700328), [institutional PDF](https://bnct.inp.nsk.su/publics/2024/PHP_p_11B_2024.pdf) | Real thick-B4C spectra and composition diagnostics support explicit impurity/background treatment | Does not supply the desired thin-target channel-cross-section calibration; material and geometry differ from STARS |

## Consequences for the source

The 2016 evaluation remains preserved as a model-dependent normalization. The later exclusive measurement changes the candidate amplitude family; it does **not** supply a universal replacement event cross section or a numerical correction to the 2016 table. Both must be compared at their actual measurement boundaries.

For a pure2-minus parent, the ground-state Be8 branch is forbidden. This is a selection rule, not a missing branch fraction to estimate. Nearby parent states and finite beam-energy distributions can still yield observed alpha0 counts. Do not apply this isolated-state exclusion to the entire measured reaction.

A mixture of partial-wave amplitudes is coherent. The published mixture percentage must not be implemented as independent coin flips between classical event types. Likewise, random permutation of output labels is not Bose-amplitude symmetrization. A constant-width Breit-Wigner, an R-matrix formal level energy, and an observed resonance centroid/width are distinct parameterizations; citing a paper does not make them interchangeable.

## Consequences for fitting and experiment design

Keep energy uncertainty, correlated target normalization, detector efficiency, counting uncertainty, digitization allowances and model discrepancy separate. Do not turn FWHM into1sigma without establishing the response shape; do not treat shared calibration errors as independent bin noise. The current measured stopping fit already demonstrates that small training residuals can coexist with a worsened energy block.

The 2025 telescope separates scattered protons from alphas, making it a valuable apparatus-design precedent. Its target-specific calibration values are not our detector calibration. The paper also discusses possible Al(p,alpha) contamination at selected energies: a future experiment should include backing-only/blank measurements and material-specific forward models. Its raw data are offered on reasonable request; no author contact was sent.

Priority: qualify channel-resolved measured spectra and their acceptance/covariance, recover the cold alpha-stopping numbers, and compare the newer amplitude alternatives through a common response model. Then validate on a separate campaign/target batch. Preserve nulls, discrepancies and unqualified data rather than filling gaps with invented Gaussian errors or gain factors.
