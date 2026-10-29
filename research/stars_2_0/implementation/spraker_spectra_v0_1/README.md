# Spraker measured-spectrum recovery v0.1

Additive research source fixture, 2026-10-28 America/Chicago. Earlier versions remain unchanged.

Recovered BOTH original publisher supplements for Spraker et al., J Fusion Energy 31, 357–367 (2012), DOI https://doi.org/10.1007/s10894-011-9473-5 . Workbook 2 supplies 22,100 alpha-spectrum cells and 22,100 matching statistical-error cells: eight detector sheets, each 27 proton energies by 100 alpha bins, plus 500 low-energy cells. Workbook 1 supplies alpha-on-boron elastic-scattering data and fitted phase shifts, inventoried here but not yet implemented as a scattering model.

The paper's numerical example reproduces: at 1.4 MeV proton LAB energy, detector LAB angle 90 degrees, and alpha CM bin center 4.635 MeV, workbook cell 90!B54 is 4.2779 mb/sr, rounding to the published 4.28. The bins are 0.09 MeV wide. Values are per SOURCE BIN, not per MeV; no extra bin-width factor is applied. No division by three or conversion to a fusion-event cross section is permitted.

## Critical qualifications

Workbook Notes explicitly distinguish incident proton LAB energy, outgoing alpha CM energy, and Counts/(L dOmega) in the CM frame. Numeric sheet names identify detector positions matching the paper's LAB angle list. Thus LAB detector position does NOT make the tabulated observable a LAB differential yield. Do not directly multiply it by LAB detector solid angle. An energy-dependent frame transformation / Jacobian is needed for a new apparatus. The 2012 text also explicitly describes CM angular fits; the 2016 angular-coefficient frame needs reconciliation before a LAB aperture model is adopted. Total full-sphere source cross sections from the preceding release are unchanged.

The high-energy sheets include columns 3.9 and 4.0 MeV, beyond the paper's stated 3.8 MeV coverage. All 1,600 such cells are retained and flagged pending reconciliation. Low-energy sheets contain 0.152, 0.224, 0.248, 0.296 and 0.4 MeV; their detector angle is not explicitly specified on those sheets and is left null. The workbook's notes describe the high-energy campaign, so low-energy metadata must be checked separately.

There are 9,943 reported zero cells. A reported zero outside hardware/analysis acceptance is not evidence for zero alpha emission. Zeros are preserved but excluded from the initial residual comparison until acceptance is qualified. The original paper documents detector thresholds, scattered-proton backgrounds and restricted integrations. Neither complete acceptance masks nor full uncertainty covariance have been recovered. The article's 3.6% target normalization and <=5% overall spectral systematic discussion must not be treated as independent per-bin noise. Related 2012/2016 evaluations are not independent datasets.

## Run

Requires Python >=3.11 and xlrd==2.0.1 (read-only XLS parser). Existing source files and outputs are never overwritten.

```bash
python -m pip install -r requirements.txt
python extract_spectra.py --download --sources sources --out receipts/new_run
python -m unittest -v test_spectra
```

The source URLs and SHA256 hashes are pinned in SOURCE_INDEX.json. Downloads can be performed once, then rerun offline without --download. The raw XLS files are unchanged. Original spreadsheets retain their own rights notice; the article identifies a Creative Commons Noncommercial license. Source workbooks are not bundled or relicensed as project code.

Optional --predictions FILE accepts JSON records with record_id, frame='CM', the exact observable tag from SPECTRA.csv, and prediction_CM_mb_sr_per_source_bin. It produces signed residuals and statistical-error-only standardized residuals at explicitly supplied cells. It does not fit a model, calculate a reduced chi-squared, infer independence or declare validation. No fake predictions are supplied to manufacture calibration success. This fixture is a target for a future source -> transport -> frame-correct detector forward calculation, not a new birth spectrum or joint three-alpha sampler.

Nine tests cover all high-energy values/errors, the published numerical anchor, source hashes, frame/observable guards, reported-zero handling, residual units, and a deliberately corrupted error-axis mutation. The extractor was run successfully. No workbook authoring or visual rendering is claimed.
