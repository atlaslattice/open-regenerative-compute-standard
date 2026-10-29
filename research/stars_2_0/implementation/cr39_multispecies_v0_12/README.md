# Stellar Forge Reference — multi-species measurement audit v0.12

This additive version recovers a substantially more detailed published calibration package: Schollmeier et al., [Scientific Reports13,18155(2023)](https://doi.org/10.1038/s41598-023-45208-x), including its original supplement. It extracts four coefficient rows, three species-width records, six nominal filter stacks, source-specific conditions/geometry, campaign calibration adjustments, and two explicitly reported analytic source spectra.

It does **not** deliver a complete TPS reproduction. Raw numerical campaign data are available on request and were not recovered or requested here. Nominal filters are known; qualified transmission, tolerance/covariance and exact matched TPS geometry are not. The benchmark-selection result remains blocked.

## Literal response reconstruction failed

The coefficient table was independently compared between official XML and PDF text; both agree. The PDF page5 equation, table and graph were visually inspected, as was supplementary TableS1 on page4. Under the explicit interpretation x=ion energy inMeV, y=pit diameter inum and beta=Euler beta, the printed Eq2/Table1 prescription does not reproduce Figure3:

- The literal He function is strictly decreasing for every positive x because its p2=0.49 is below1, whereas the source graph/text describe a nonmonotonic response.
- At the3MeV carbon boundary, the low/high branches give approximately0.4466um and0.0000682um. Both are outside the deliberately coarse1.0–1.3um graphical envelope verified on the source figure. That envelope is a broad visual check, not a measured uncertainty or new calibration dataset.
- The literal H peak is at0.6977MeV, outside the source's approximate0.1–0.2MeV peak description.

The independent40-digit calculation agrees with our direct double-precision formula at all28 points (maximum relative arithmetic difference4.22e-15). This verifies arithmetic, not the scientific response. No parameter permutation, hidden normalization or coordinate transformation was invented to make the source gate pass. `literal_audit.py` is quarantined, and its apparatus adapter always rejects use. Original implementation/definitions or a corrected prescription are needed. This is not proof the experiment is wrong.

## Other source limitations retained

The study reports diameter adjustments typically within±3%, an approximately-15% proton calibration shift, and a factor-of-two difference in absolute proton flux between CR39 and TPS. These are preserved discrepancies, not corrections imported into Stars. The compared diagnostics are also at different angles: CR39a45degrees and TP2 about35degrees to target normal; an angular source map is needed before treating their absolute difference as a single detector-calibration error.

The supplement distinguishes Landau and Gaussian convolution widths. These are not interchangeable with fit residual scatter, a parameter covariance or independent Gaussian errors. Its prose gives an unqualified He width0.4–0.6um while TableS1 lists Landau scale0.030–0.060um; definitions need reconciliation before transfer. No Langau response was substituted with an arbitrary Gaussian.

Nominal He accelerator energy up to8MeV is not a recovered7.5MeV at-detector calibration: the RBS setup introduces significant energy loss/broadening. The new coefficient table remains quarantined in any case. The earlier v0.11 condition-specific reference remains preserved; no global alpha coverage upgrade is claimed.

## Useful runnable source-form replay

`spectra.py` reproduces the paper's two explicitly parameterized CR39b analytic fits, with units retained. Eq4 is the reported proton form; Eq3 is the reported carbon form proportional to N0/E. The latter's integrated particle count diverges as its lower bound tends to zero. A strictly positive cutoff is required, and its amplitude N0 must not silently become an all-energy particle count. The query energies and finite integration domain in the audit are computational choices, not assertions of measured coverage or Stars source applicability.

The replay is not a fit to raw measurements and does not establish new particle yields. No filter transport, detector fold, full measurement likelihood or net-energy result is supplied.

## Evidence and next action

`MEASUREMENT_PACKAGE_v3.json` retains the source values. `BENCHMARK_READINESS.json` adds applicability, independence and failure-consequence fields. `DATA_RECOVERY_REQUIREMENTS.json` specifies the concrete missing data/code package. `ACOUSTIC_REFERENCE_POLICY.json` gives no unmeasured yield credit in the OFF reference while leaving unqualified ON effects/costs unknown and retaining adverse/null/positive sensitivities. `REVIEW_DISPOSITION.md` records corrections to the suggested dependency order and calibration assumptions.

The most decisive next source acquisition is the original response implementation plus matched raw calibration/campaign records. More flexible fitting or a discrepancy GP cannot replace that evidence. No message was sent to authors and no scientific freeze is requested.

## Reproduce

Python3.12.14, SciPy1.17.0, mpmath1.3.0 and Poppler26.05 were used. Source PDFs/XML are downloaded by hash, not bundled. Earlier source versions remain unchanged.

```sh
cd research/stars_2_0/implementation/cr39_multispecies_v0_12
python -m pip install -r requirements.txt
python extract_package.py --download --sources sources --out receipts/new_extraction.json
python -m unittest -v test_package
python run_audit.py --out receipts/new_audit
```

Extraction outputs/source files and audit destinations are never overwritten. Source-dependent tests skip explicitly when source files have not been downloaded. All14 tests, including source re-extraction, passed in the recorded environment. Arithmetic checks pass; the separate scientific source-reconciliation gate fails and remains blocked. Repeated audit/receipt bytes match, and an isolated file-layout replay uses no source PDFs or nuclear backend.
