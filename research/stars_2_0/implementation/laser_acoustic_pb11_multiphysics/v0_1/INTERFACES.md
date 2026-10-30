# Interfaces v0.1 — contracts, not implemented multiphysics solvers

The p–B apparatus identities A/B/C retain PR43 meanings. Local arms REF_OFF,
REF_SHAM, REF_ON, POCKET_OFF, POCKET_SHAM and POCKET_ON are treatment cells,
not apparatus aliases. Nothing from Beyond Q D–D/D–T power assumptions is imported.
The new pocket lane has unresolved membership in the recovered physical topology;
its existence in a research inventory is not an installed fabrication specification.

## Geometry and preparation

`geometry_template.json` is a flat, CAD-compatible parameter exchange template,
not a CAD solid or a fabrication-ready mesh. Unknown values are null, never zero.
The geometry command detects unresolved critical fields; passing completeness
would still require dimensional, material, topology and mesh qualification.
No preset ceramic chemistry, dimensions, packing, grain size, damping or acoustic
coupling is fabricated. The ten-second duration is a project design choice.
Readiness thresholds and their sensors remain unresolved. Longer preparation and
PRE_ONLY versus PRE_PLUS_SUSTAIN remain campaign variables, not fixed gain factors.

State transfer from mechanics/granular physics to hydro/PIC must include mesh and
frame identity, timestamp, region material/composition, mass density kg/m3,
velocity m/s, displacement m, stress Pa, temperature K, charge/ionization state,
uncertainties/correlations and source hashes. Resolve separate electron/ion
thermal states where the selected model needs them. Porous/granular homogenization
requires a documented scale test. A global acoustic phase or envelope alone is
not a density field. Solid acoustics, plasma waves and laser spectral phase
control are distinct modules.

## Optics, hydro and kinetic regions

Optical boundary records need wavelength m, polarization, pulse temporal profile,
fluence J/m2, angle-dependent reflectance/absorption, roughness and damage model.
The ray/wave approximation is not chosen until feature scales are recovered.
Optical reflection and magnetic mirroring are different boundaries.

Hydro-to-PIC transfer needs conservative mass/charge/energy mapping, species
number density m^-3, electron/ion distributions and both prescribed and evolving
fields. An equation-of-state temperature is not necessarily a Maxwellian kinetic
population. Imports must identify field sources, coordinate frames and domain
ownership; initial states cannot be assumed maintainable without drive power.

Particle interchange uses species/isotope/charge, physical macroparticle weight,
position m, time s, and SI momentum kg m/s or an explicitly named alternative.
Do not confuse WarpX internal gamma*v, velocity and SI momentum. Preserve joint
energy–angle–position–time distributions. Weighted products, not raw macro-counts,
enter the physical ledger. Use both species' velocities for pair CM energy.

One solver owns a physical region/process/time interval. A transferred particle
must leave the sending active population. Cold-solid stopping and PIC collision
loss cannot both debit its same path. Fusion events and alpha products are also
created once. Any overlap/remapping correction needs a separate residual ledger.

## Physical, detection and electrical ledgers

Keep reaction events, alpha births, post-field alpha energy, escaping alphas,
accepted particles, detected counts and delivered electricity as separate metrics.
Escape can exceed initial birth kinetic energy only with explicitly tracked
external work; the initial accounting interface rejects that situation until an
extended field-work ledger is supplied. Birth/escape units are joules. Detected
counts cannot determine fusion-event counts without a calibrated response model.
Alpha channeling, direct recovery and thermal recovery partition disjoint energy.
Radiation, particle losses, stored energy and unconverted heat remain explicit.
Stopping transfer and electrostatic deceleration are not automatically electricity.

## Attempt-level implementation

`benchmark.py` accepts JSON with a positive, predeclared
`success_threshold_events` and a `shots` array. This initial threshold endpoint is
fusion-event count; a future detector-defined endpoint needs its own version and
calibration. Each row requires shot_id, apparatus_id, arm, campaign_id, batch_id,
evidence_class, source_ref, event_semantics and explicit wall_input_J keys.
Optional metrics are fusion_events, alpha_birth_energy_J, alpha_escape_energy_J,
detected_alpha_count, useful_electricity_J, elapsed_s and firing_time_error_s.
Absent optional metrics mean missing. Wall category keys are laser, acoustic,
magnets, rf_nbi, cooling, vacuum, target_handling, diagnostics, collector_bias and
other; unknown values are null, genuine known absence is zero. Categories must be
mutually exclusive. Common facility loads need a documented allocation once.
Time intervals include preparation, failed attempts and replacement downtime and
must be disjoint; overlapping/continuous facility operations need a campaign
interval ledger rather than summing overlapping shot durations.

Event semantics REALIZED_COUNT, DRAWN_MODEL_COUNT and EXPECTED_POPULATION are
reported separately. Thresholding expected weighted reactions does not establish
a shot-success probability; that classification is withheld. Synthetic and
measured evidence are not pooled. This descriptive interface does not perform
causal inference, detection correction, Bayesian calibration or physical transport.
Unknown outcomes prevent unconditional yield totals; worst/best-case success
bounds are logical missing-data bounds, not confidence intervals. Timing RMS,
bias and population SD concern observed values only, with missing counts retained.

The exact accounting identity is
E[Y] = P(S) E[Y|S] + (1-P(S)) E[Y|not S].
Failures may have nonzero yield. Higher reliability increases all-attempt yield
when conditional yields and opportunity rate support that conclusion. Per-hour
power also depends on cycle duration, downtime and auxiliary power.
