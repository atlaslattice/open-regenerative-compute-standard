# Stellar Forge Reference — evidence and coherent transport v0.10

This additive package provides (1) a parameter/evidence register, (2) a hash-pinned calibration-source catalog with applicability guards, and (3) a traceable coherent three-alpha transport benchmark. All26 earlier apparatus modules remain in an explicit coverage inventory. No existing research version is replaced.

The reference connects publication-model event normalization, depth-dependent proton stopping, locally normalized coherent decay amplitudes, mass-correct four-vectors, bounded alpha exit transport and a primary-particle energy ledger. It stops at true exit/geometry quantities: detector counts, recovered heat, wall-plug energy, net energy and financial results remain `null` because qualified inputs are absent. No synthetic detector efficiency is introduced.

## What the registers distinguish

`PARAMETER_EVIDENCE_REGISTER.json` has38 entries covering configured scenario inputs, numerical controls, source/mass provenance, model selections and unavailable interfaces. Its scope is this reference, not every parameter inside every retained module. Constituent stopping tables and formulas remain separately hash-pinned. Assumed target inventory, incident proton counts and geometry are clearly distinguished from measured values. Literature model conventions are not relabeled as measurements.

`DATASET_CATALOG.json` covers six source records: Sikora event normalization, Spraker spectra, Mazzucconi differential quantities, the Munch preprint alpha0 table, Overley stopping data and the Kuhlwein parameter reference. These are not six interchangeable calibration datasets. Shared Spraker/Sikora ancestry is explicit. Alpha0 data are not admitted as a fit target for the pure2-minus source. The Overley stopping fit applies to its cold B10-enriched proton benchmark, not to alphas, B11, BN or hot targets.

The catalog points to preserved source versions and verifies their hashes. Spraker's22100 spectrum cells are not bundled: its preceding extraction receipt and reconstruction recipe are provided, respecting the publisher-source handling. Run the extractor under its own documented requirements when numerical spectra are needed. `calibration_bundle.py --metadata-only` verifies the portable anchors without pretending those cells are locally present. An audit role does not authorize a statistical fit or observable conversion. No new measured numeric dataset was recovered in this release.

`MODULE_COVERAGE.json` preserves26 modules, with new status overlays only where work was actually verified. Other modules are retained outside this run, not assumed absent or effective. All installed CAPEX fields remain unknown, not zero. Mutually alternative components must not be automatically stacked or their costs summed as though simultaneously installed.

## Coherent reference calculation

The assumed example uses cold elemental B11 with1e18 atoms/cm²,0.675MeV proton LAB energy, three supplied attempts of10000,0,20000 protons, and a60-degree cone about the positive LAB z axis. These are verification choices, not apparatus measurements. The planar foil is infinite laterally. The source assumes an unpolarized pure2-minus parent in the declared0.65–0.70MeV local-energy benchmark interval, with the v0.8 raw-basis k0.76 and phase0.67*2pi. It is not a universal multi-resonance source or a calibrated LAB anisotropy model.

Proton energy varies with depth. Each hazard cell has its own local source energy and independent phase-space proposals. Coherent weights are normalized **within that cell**. This avoids accidentally changing the depth distribution or total reaction probability through arbitrary amplitude normalization. A common-proposal phase-space-null control is retained. Equal reaction probability between these arms is a construction of the conditional benchmark; it does not prove coherent physics can never affect a self-consistently inferred reaction rate.

The Sikora2016 total normalization was extracted with a different source ansatz. Combining it with the current coherent shape is explicitly a conditional normalization/shape pairing, not a joint refit to its source spectra. The B10 empirical stopping scale is deliberately not applied to the B11 transport model. Electronic stopping uses the pinned SRIM13 model; nuclear stopping explicitly selects ZBL_SIMNRA_7_04. No scattering, straggling, target heating/evolution, support layer or recirculation is represented.

Alpha directions and birth depths determine remaining column to a foil surface. Below the positive stopping-model energy floor, exit energy remains unresolved within a bound; it is not changed into zero energy or claimed fully stopped. The true exit-energy threshold is above that floor. The readout cone gives a geometric quantity, not a measured detector efficiency.

Each proposal log retains local energy, depth, source weight, normalized event-probability weight, three LAB birth four-vectors, conservation checks and alpha exit statuses/bounds. The initial event probability is normalized separately from conditional source weights. Every supplied attempt is retained, including the zero-proton one.

## Results and limitations

Run002 contains1024 proposals (8 depth cells ×128 per cell). Run003 doubles depth cells; run005 raises proposals per cell to512. Run004 exactly repeats run002. Results and full event logs repeat byte for byte. The isolated repository-layout replay also reproduces results, events and receipts using the explicitly selected prepared CPC library.

For the assumed three attempts, expected reactions are about0.03983 under the selected model. This is not a Stars experimental yield. The coherent and null branches have the same total reaction probability but different exit spectra. The hazard refinement changes probability by about2.74e-8 relative. Geometry/transport spectra retain finite sampling and discretization sensitivity; no source-shape or transport convergence claim is made. `receipts/INTEGRATION_COMPARISON.json` preserves those changes and finite-integration diagnostics.

Maximum four-momentum residual in run002 is3.64e-12MeV. This is a numerical check conditional on nominal masses, not physical parameter precision. Source, stopping, calibration and model-discrepancy uncertainties have not been propagated.

Self-normalized importance covariance is a delta-method integration estimate using each reaction's three alphas as one cluster. The same proposal ensemble is reused across attempts: their Monte Carlo errors are correlated and must not be summed as independent. Neither that covariance nor expected-event weighting represents actual observed shots or physical shot noise.

Beam input plus primary nuclear Q equals exiting primary particles plus a bounded ledger remainder. That remainder is not recoverable heat. Secondary particles, storage, energy conversion, auxiliaries, startup and sustained burn are not solved. `GAP_REGISTER.json` lists the remaining evidence and engineering requirements.

## Reproduce

Use the full stacked repository and prepare the adjacent v0.8 Michel backend according to its README (Python3.12.14, NumPy2.3.5, SciPy1.17.0, GNU GSL shared library2.7.1 and the pinned CPC build). No network is required during the benchmark after dependencies/backend are prepared.

```sh
cd research/stars_2_0/implementation/reference_evidence_v0_10
python -m unittest -v test_evidence
python calibration_bundle.py --metadata-only --out receipts/new_dataset_audit.json
python reference.py examples/assumed_reference.json --out receipts/new_run
python reference.py examples/refined_depth_reference.json --out receipts/new_depth_run
python reference.py examples/refined_source_reference.json --out receipts/new_source_run
```

Output destinations must be new. The full JSONL logs are regenerated by the runner; published previews are selected original records, not substitute datasets. Their complete log identities are recorded in each run receipt. The isolated replay used existing Python/system libraries and an explicitly selected prepared CPC library; it was not a fresh OS install or clean compiler rebuild.

Sixteen tests check normalization, source-weight scaling invariance, four-momentum, energy boundaries, zero/missing attempts, covariance, source/material/role guards, module retention and spectrum reconstruction metadata. `SEARCH_RECEIPT.json` records public-source recovery attempts. No experimental calibration, author contact, merge, scientific freeze or blinded prediction freeze occurred.
