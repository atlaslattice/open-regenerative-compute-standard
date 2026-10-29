# Coupled p-B11 reference v0.5

New additive version, 2026-10-28 America/Chicago. Earlier files, the Gemini work and their statuses remain preserved. This release connects the publication-defined event normalization, depth-dependent proton stopping, a mass-correct three-alpha PHASE-SPACE NULL, alpha transport and detector folding. It is a workflow verification control, not a calibrated Stars apparatus or a replacement for the sequential reaction model.

## What is connected

1. The source is the 41-node Sikora–Weller2016 model-extrapolated event cross section recovered in PR23, copied unchanged with a source hash. Explicit linear interpolation in proton LAB energy is introduced above 0.22 MeV only. The narrow 0.162 MeV feature is excluded. Interpolation error and the incident beam distribution have not been calibrated.
2. The selected PR26 electronic+nuclear stopping estimate gives a relative atomic-column coordinate for protons. The primary reaction hazard is integrated along their changing energy: d(tau)=sigma(E(N))*B11_atomic_fraction*dN. Only p+B11 ->3 alpha removes a proton; competing channels, target depletion and evolution are absent. Constant rates within 256 depth bins define reaction-position sampling. The 128-bin comparison must change probability by less than 1e-4 relative. The no-reaction survival is retained explicitly.
3. Conditional event samples use the local proton energy at the sampled reaction depth. Each event contains THREE on-shell alpha four-vectors. Their sum must equal the incident proton plus stationary B11 nucleus. The birth energies are generated event by event; no detached hard-coded alpha spectrum is folded into the detector.
4. Each alpha follows a straight path to the front or rear surface of an assumed infinite planar foil. Its direction and birth depth set the remaining atomic column. The same selected stopping model then gives an exit energy or a positive-energy model-boundary result. No scattering or straggling is included.
5. A configurable cone in the LAB frame selects trajectories. An explicitly SYNTHETIC single-hit response matrix maps true LAB exit-energy bins into measured bins. Matrix deficits remain non-detection; background is zero in this verification fixture. This is not a calibrated detector, detector pileup model or measured alpha-count prediction.
6. Every supplied attempt is reported, including zero-proton attempts. Conditional Monte Carlo samples carry expected-event weights and are not presented as actual shots. A reaction's three alphas remain one statistical cluster when estimating Monte Carlo error.

## The null source is a deliberate control

The generator uses constant matrix element over Lorentz-invariant three-body phase space. A pair mass w is sampled with density proportional to p_outer(w)*p_inner(w), followed by two isotropic two-body orientations, boosts from the pair frame into the reaction CM and then into the LAB frame. Rejection uses a product of individual momentum maxima as a conservative bound. Identical alpha labels are randomized.

This includes correct kinematics but no Be8 dynamics, resonance line shape, angular-momentum amplitude, Coulomb final-state correction or interference. It does not reproduce the publication's sequential l=3 ansatz. Crucially, the 2016 total normalization was itself extrapolated using that sequential ansatz. Combining it with this different null shape is an explicitly conditional normalization/shape combination, NOT a self-consistent refit of the measured spectra. A future calibration must reconcile normalization, source shape and detector response together. The null is not an accepted scientific replacement for Gemini's correlated generator.

Primary mathematical reference: Particle Data Group, Kinematics (2025), https://pdg.lbl.gov/2025/reviews/rpp2025-rev-kinematics.pdf . The constant-matrix-element choice is this project's null assumption, not a claim made by the p-B experiment.

## Nuclear masses and conservation

MASS_SOURCE records 2022 CODATA proton/alpha/electron energy-equivalent masses and atomic mass unit, plus an explicitly older NIST B11 atomic-mass snapshot and NIST ASD5.12 ionization energies. B11 nuclear mass is atomic mass*u minus five electron masses PLUS total electron binding. The nucleus is not replaced with an effective mass. Stopping parameterizations retain their own approximate atomic-mass conventions separately.

Nominal masses give Q=8.682559153 MeV. The older B11 atomic-mass uncertainty alone corresponds to about 0.000419 MeV. These uncertainties and correlations have not been propagated. Numerical conservation tolerances are conditional on nominal masses, not claims of physical mass precision. Each event is checked for total energy and three-momentum closure to 1e-8 MeV and alpha mass-shell residual relative to m_alpha^2 <=1e-12. The measured run's maximum residual is recorded in VERIFICATION.json. Mutation tests reject a nonconserving alpha and nonfinite initial four-vector.

## Missing coverage, counters and energy boundaries

The stopping coordinate is zero at a POSITIVE model energy floor. It is not a complete range to rest and is not exported into the old full-CSDA RangeTable. A particle crossing below that floor keeps exit_energy=null and a remaining-energy upper bound. The code does not turn that into a stopped particle or full deposited heat.

For this cold, monotonic, no-reacceleration reference, an unresolved alpha has energy below the floor. A detector threshold at or above that floor can therefore exclude it from above-threshold counts while its physical escape/stopping status remains unknown. A lower detector threshold is rejected, rather than converted into zero measured output. Alpha escape and geometric-acceptance count intervals preserve that distinction. Born, escaping, geometrically accepted, in-response-bin and folded detector quantities are separately reported.

Unreacted protons leave with their calculated kinetic energy. Beam kinetic input, nuclear Q contribution, exiting proton energy, bounded alpha exit energy and the primary-particle energy-loss remainder are recorded. The remainder is NOT recoverable heat; secondary transport, storage and conversion are missing. Net energy and heat recovery remain UNAVAILABLE. Nothing in this release proves or disproves ignition or sustained net electricity.

The p-B11 source lane accepts only B11 or BN_B11_N14. It rejects generic boron and the historical B10-enriched stopping benchmark, preventing B11 cross sections from being applied to B10 inventory. BN counts total B+N atoms separately from B11 atoms and requires an explicit electronic mixing factor. All prior model-transfer qualifications still apply.

## Example and reproduction

Clone the draft branch, then from research/stars_2_0/implementation/coupled_reference_v0_5:

```bash
python -m pip install -r requirements.txt
python run.py examples/reference.json --out receipts/NEW_RUN
python -m unittest -v test_reference
```

The sibling stopping_models_v0_4 directory from PR26 is required. DEPENDENCY_LOCK checks its model, table manifest and eight tables before loading it, plus the unchanged source-event table and detector module. No network is required at runtime. Python 3.12.14 and NumPy 2.3.5 were used. The example's PCG64 seed is 20261028, with one SeedSequence child per supplied attempt.

The example is entirely assumed: 0.65 MeV monoenergetic protons, B11 target inventory 1e18 atoms/cm2, incident proton counts 10000,0,20000, a LAB detector cone of 60 degrees and a synthetic diagonal 60% response. No laser or readiness measurement fixes those inputs. The three attempts together give conditional expected fusion events 0.0417516771 under the selected interpolated normalization and stopping law. The two nonzero attempts each use 256 conditional event samples, not hundreds of actual observed reactions. This number is a verification example, not a Stars yield estimate. Counts cannot be multiplied by arbitrary acoustic gain.

Outputs: CONFIG, RESULTS, EVENTS.jsonl, RECEIPT and MANIFEST. The full event log records depth, local proton energy, birth four-vectors, transport statuses, bounds and event weights. Existing output directories are refused. On failure, the input configuration and FAILURE receipt remain available. Published receipts include full results, three example event records, verification and hashes; all 512 full event records can be regenerated offline. Raw full event logs from repeated runs are retained locally and are not bundled as a second dataset.

## Verification and limits

Sixteen tests pass: nuclear/atomic mass distinction and binding correction; four-momentum and mass shells at multiple beam energies; bad-particle/NaN mutations; inverse boosts; phase-space pair-mass sampling against an independently expressed invariant-mass integral; analytic constant stopping; analytic constant-hazard probability; narrow-resonance guard; all-shot and zero-source accounting; detector/count closure and energy bounds; event-cluster covariance; repeatability; frame/null-mode guards; unresolved threshold rejection; zero target; isotope guard; and the BN/no-heat-credit path. Several related assertions belong to one test method.

The sampling-distribution check uses 2000 events with seed814 and a six-estimated-MC-standard-error tolerance against numerical quadrature. It is an implementation check, not a scientific significance threshold. The reported detector covariance measures finite conditional-sampling error only. It omits physical shot noise, source uncertainty, systematic calibration, material-model discrepancy and parameter covariance. No independent-alpha Poisson likelihood is asserted.

Repeated final RESULTS, EVENTS and RECEIPT files are byte-identical in the recorded environment. This validates reproducibility of the implementation, not fidelity of the null to real p-B spectra. Experimental acceptance and grouped holdouts have not run. No actual nuclear experiment, detector calibration, acoustic intervention or wall-plug test ran here.

Next: ingest/reproduce the correlated sequential reaction engine, fit source shape and normalization jointly against frame-correct measured spectra, calibrate detector and compound stopping, then compare the null and physical source model on campaign-level holdouts. The full apparatus catalog, readiness controls and energy/economic modules remain retained but are not newly coupled into this reference. The main UI is unchanged. No supersession, merge or scientific freeze is requested.
