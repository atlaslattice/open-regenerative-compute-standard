# Stellar Forge Reference — CR-39 response v0.11

This additive release recovers numerical CR-39 evidence and implements a condition-specific reference adapter. The requested Zheng2026 model remains unrecovered. An accessible older source, Zhang et al., [Nuclear Science and Techniques30,87(2019)](https://doi.org/10.1007/s41365-019-0619-x), supplies a separately labeled benchmark. It is not a replacement calibration for Zheng's BA/TA profiles or the Stars detector.

## Recovered evidence

`ZHANG2019_DIGITIZED.json` preserves10 alpha response points from the black series of Figure10, plus52 bins from the displayed3.2–24um portion of the Figure4 histogram at4.42MeV. Point energies come from the paper's Table2; diameter means and core spreads come from the figure. Figure4's printed raw statistics and Gaussian fit parameters are transcribed separately.

The selected conditions are TASTRAK CR-39,6.25mol/L NaOH,98C,1hour. The publication also studies other species and etches, which this implementation does not substitute. Source detector dimensions are25×25×1.5mm. Alpha energy was characterized using a SiC detector in the source experiment. Energy-calibration uncertainty, detector-lot/age transfer, angular response, absolute detection efficiency, track losses and covariance are not recovered here.

The two publisher figures were downloaded with SHA256 verification and visually inspected. `digitize.py` records manually inspected marker/cap coordinates and verifies visible black marks at those locations. Means have a declared0.06um digitization allowance and core spreads0.08um. These are analyst-selected conservative pixel allowances, not measured calibration errors or confidence intervals. Figure error bars summarize reported track-diameter fit spreads, not uncertainty of the mean.

Source images and full article text are not bundled. `SOURCE_INDEX.json` records official URLs, hashes, access limits and the separate Zheng search result. Downloading accessible source figures is sufficient to replay extraction. No author contact, institutional login or purchase was made.

## Implemented behavior

`ReferenceResponse.mean` returns a digitized reference point or an explicitly labeled piecewise-linear interpolation. It supports alpha energies1.105–4.915MeV only, under the exact nominal detector/etch designation. Other species, BA detectors and other etching conditions are rejected. Out-of-range energies, including7.5MeV, return `UNCOVERED` with no diameter prediction. Matching nominal conditions does not validate transfer to an apparatus or a new detector lot.

The3.3 and3.9MeV queries return interpolated mean diameters, not new measurements or a reproduced two-peak fusion spectrum. A reported/interpolated core width is provided as a descriptive quantity only; no full Gaussian response is invented at those energies. The mean-response uncertainty remains unknown.

`energy_candidates` preserves the nonmonotonic inverse. For example,13um maps to approximately1.456 and2.757MeV in the declared piecewise-linear mean curve. These are candidate energies, not a unique reconstructed spectrum or posterior probabilities.

`fold_registered_display_subset` is available only at4.42MeV. It maps a known count of registered tracks **within the digitized display subset** into that subset's approximate histogram. It does not map incident alpha fluence into detected counts. Absolute efficiency and missed tracks remain unknown. At other energies the full distribution is unavailable even when a mean can be interpolated. No generic full-spectrum detector fold or TPS reconstruction is claimed.

## Checks and preserved discrepancies

At4.42MeV, the digitized mean differs from the printed Gaussian-fit mean9.65um by0.0052um; its core spread differs from0.9028um by-0.0063um. These are same-paper internal anchor checks within pixel allowances, not independent validation.

The source Figure4 reports14740 entries, raw mean9.773um, raw standard deviation1.482um, and Gaussian chi-squared1140 for22 degrees of freedom. The displayed-histogram digitization totals about14619 and has standard deviation1.3856um, about6.5% below the reported raw value. The finite display subset, raster precision and baseline/tail recovery remain unresolved; the extraction is not relabeled an exact raw-histogram reproduction. Conservative pixel-based count bounds are reported without treating them as stochastic experimental errors.

The poor reported Gaussian fit is retained. Neither its narrow core nor Zheng's separate within2% statement is promoted to a universal response. This release uses an empirical displayed-histogram reference at the single supported energy instead.

Retrospective leave-one-out interpolation over eight interior response points has an RMS residual about0.71um. This is a same-campaign interpolation diagnostic, not an acceptance claim. It warns against treating simple interpolation as a high-accuracy calibrated model. Endpoints are not extrapolated; systematic calibration and energy uncertainties are not invented to manufacture passing fits.

## Reproduction

Python3.12.14, NumPy2.3.5 and Pillow12.3.0 were used. No GSL or nuclear-model backend is required.

```sh
cd research/stars_2_0/implementation/cr39_response_v0_11
python -m pip install -r requirements.txt
python digitize.py --download --sources sources --out receipts/new_extraction.json
python -m unittest -v test_response
python run_reference.py --out receipts/new_run
```

Outputs and source files are never overwritten. A changed publisher image hash requires inspection and a new extraction version. The image-reextraction test explicitly skips if source images have not been downloaded; all12 tests, including reextraction, passed in the recorded run. Repeated results/receipts are byte-identical, and an isolated directory replay using only published files reproduces them.

`EVIDENCE_UPDATE.json` advances the detector gap only to a source-traced reference. The v0.10 apparatus response remains unknown. Next needs: Zheng's actual numerical model and conditions, high-energy alpha calibration, numerical track distributions/efficiency, then a fully specified TPS comparison. No experimental calibration, scientific freeze, merge or net-energy conclusion is made.
