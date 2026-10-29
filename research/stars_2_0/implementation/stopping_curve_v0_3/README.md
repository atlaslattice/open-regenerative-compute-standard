# Boron stopping curve and finite-interval transport v0.3

New version, 2026-10-28 America/Chicago. Earlier source records, mirror quarantines and research versions remain intact. This addition reconstructs a complete 27-point plotted proton-stopping dataset and makes finite-interval transport runnable. It does not complete alpha transport or the Stars apparatus calibration.

## Source and reconstruction

Jack Castle Overley, Caltech PhD thesis (1961), DOI https://doi.org/10.7907/XZP6-5P63 , https://thesis.caltech.edu/6305/ . The original PDF SHA256 is pinned in SOURCE.json. Figure 7 is printed page 82 / PDF page 87. It was rendered with pdftoppm at scale-to 2600 and visually checked. Direct pixel-component extraction finds 27 plotted points. It uses a fixed intensity threshold, component area cutoff and annotation-exclusion regions. The candidate mirror is NOT used to seed or fit point detection. Pixel coordinates, tick calibration and affine transforms are retained in CURVE.json.

Digitized support runs from 0.098982 to 2.964723 MeV LAB. The author's nominal experimental range is 0.1–3 MeV. The curve is newly digitized data, not original digital measurements or a fit to raw transmission spectra. Working digitization allowances of +/-0.008 MeV and +/-0.08e-15 eV cm2/atom are explicit analysis allowances, not statistically estimated standard deviations. The source's +/-4% total probable error is separate and shares target/calibration ancestry. Full covariance and beam-energy uncertainties remain unavailable.

The two exact textual absolute anchors are kept in the previous source version and are not substituted into this scan reconstruction. Both reconstructed anchor points lie within the working digitization allowances. Only AFTER extraction, all 27 points were paired by order with the old mirror's A series. Maximum absolute differences are 0.007232104 MeV and 0.054714402e-15 eV cm2/atom. This supports source lineage and numerical consistency; mirror and scan are not independent experimental validation. B/C/D series are still unresolved and are not imported.

The actual absolute-normalization target was 95.96% B10 and 4.04% B11. Its measured energy-loss stopping has no separately recovered Se/Sn decomposition. The fixture is therefore labeled OVERLEY_COLD_B10_ENRICHED_95.96_PERCENT. A B11, BN, B4C or warm-target assignment is rejected. A future isotope/material-transfer model must expose its assumptions and uncertainty, compare overlapping data and qualify electronic/nuclear contributions. It is not necessary to pretend no data exist, nor to pretend these are direct BN measurements.

## Transport model

The solver uses atomic areal density N in atoms/cm2 and atomic stopping epsilon in eV cm2/atom:

    N = 1e6 * integral(E_out to E_in) dE_MeV / epsilon(E)

Epsilon(E) is explicitly piecewise linear between reconstructed points. Its reciprocal is integrated analytically on each segment with a stable log1p expression, then inverted by bisection. No density assumption is needed for this atom-column calculation. The supplied examples are verification inputs, not apparatus targets. No straggling, scattering, target evolution, charge-state model or separately resolved nuclear stopping is added.

For 0.65 MeV incident protons and an assumed 1e18 atoms/cm2 of the source material, the conditional model returns E_out=0.644488697 MeV and primary energy loss 0.005511303 MeV. Primary energy loss is not automatically recoverable heat. If the requested column would carry the proton below the lowest supported energy, the solver returns LOW_ENERGY_DATA_BOUNDARY_REACHED with E_out=null and stopped=null. Missing low-energy coverage must never become zero outgoing energy or a complete CSDA stopping range.

Eight coherent sensitivity cases vary the source stopping scale by +/-4%, the digitization stopping offset by +/-0.08e-15, and the energy-axis shift by +/-0.008 MeV. They are stress scenarios, not a confidence interval, a recovered covariance model or proof that all combinations are equally likely. No independent per-point Gaussian noise is manufactured.

## Run offline

Python >=3.11. The transport CLI itself uses the standard library; reference tests and digitization use the versions in requirements.txt. CURVE_LOCK.json protects the bundled reconstruction against silent edits.

```bash
python -m pip install -r requirements.txt
python run_reference.py --out receipts/new_transport_run
python transport_interval.py --curve CURVE.json --energy 0.65 --atoms-cm2 1e18 --material OVERLEY_COLD_B10_ENRICHED_95.96_PERCENT
```

To reproduce digitization from the hash-pinned original PDF, install Poppler and run:

```bash
python digitize_curve.py --pdf PATH_TO_Overley_jc_1961.pdf --out receipts/new_digitization
```

The recorded renderer is Poppler 26.05.0. Different rendering versions can alter pixel components; the point-count gate will reject a changed extraction. Do not widen that gate without inspecting the original scan. No existing output directory is overwritten. The original PDF and generated page raster are not redistributed here. CURVE.json and POINTS.csv are derived numerical records with source attribution.

Ten tests pass: constant and linearly varying analytic stopping, independent quadrature, zero-thickness identity, energy loss/accounting, two-layer composition, unavailable low-energy output, material mismatch, invalid grids/extrapolation, a unit-factor mutation, interval additivity and stopping-scale response. These verify mathematics and implementation. They do not substitute for an independent foil-transmission experiment. Source verification, mirror comparison, test output, sensitivity cases, environment and hashes accompany the version.

An initial digitization attempt detected only 26 points because the right mask clipped the last dot. The correction expanded the mask to include that dot while retaining plot-border exclusion. FAILED_RUN001.json preserves the failure; no scientific curve was issued from that run.

## Alpha stopping remains a specific acquisition gap

Kamke and Kramer (1962), DOI https://doi.org/10.1007/BF01378142 , reports alpha stopping/range over 0.2–5.3 MeV using boron foils on mica, with about 2% error per datum. The full numerical article remains subscription-restricted. Its additional-information footnote describes a purity assessment on a DIFFERENT foil deposited under worse vacuum conditions, finding O/B atom ratio about 5%. Do not assign that composition to every experimental foil, or ignore the qualification.

The IAEA helium index explicitly lists He->B and an Origin file. The Origin and ZIP downloads returned 403 via direct retrieval; web retrieval recognizes the binary Origin file but cannot decode it. The UNAM historical curator mirror identifies the conventions and file-number symbols, but its data links now return a 404 page. An HTML access/error page is not a recovered PDF or numeric dataset. These failures are recorded in ALPHA_ACQUISITION.json. No alpha stopping curve, alpha escape probability or full yield is invented to fill this gap. Versioned SRIM/TRIM or another documented model remains a useful parallel calculation to benchmark once actual numerical outputs are recovered.

All apparatus modules remain in scope. This is a source-reproduced proton transport component, with material transfer and independent calibration acceptance still open. No merge or scientific freeze is requested.
