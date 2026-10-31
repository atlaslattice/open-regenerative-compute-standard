# Handoff and unresolved physics

Completed: actual weighted-source → prescribed-field → domain-removal → target-
selection → cold-B11 expected-reaction coupling; particle/energy balances;
reaction-off, zero-column, aperture-miss, known-zero/missing controls; timestep
comparison; raw and derived surface records;19 tests and25 coupled checks.

Still open: measured/source-qualified joint proton source and covariance;
actual magnetic/target/pocket geometry; plasma electron/proton/boron state,
Coulomb/radiation coupling and field drive; material-specific scattering,
straggling and heating; correlated alpha generation/escape; detector/collector
calibration; target readiness, jitter and acoustic OFF/SHAM/ON response; target
replacement/duty cycle and full wall-plug energy. No calibrated apparatus or
net-energy gate closes. Higher reliability can increase all-attempt yield; this
release neither assumes nor estimates an acoustic gain.

Next coupling: export correlated alpha birth events from receiver reaction cells
within the selected source model's qualified state/energy domain, transport them
through the actual material/support and field boundaries, then forward-fold the
detector response. Keep coherent-source versus sequential-source conventions and
Q/mass differences explicit. Do not invent alpha phase space from a single mean
energy or label birth energy as escaping/collected electricity. Post-slab proton
reinjection also needs a new exit-state/scattering/time adapter.

Primary references:
- WarpX26.10 source pin ec1660d961696c865c87c26728b7e248b5454082,
  Source/Particles/ParticleBoundaryBuffer.cpp: CopyAndTimestamp versus
  FindEmbeddedBoundaryIntersection; domain timing differs from EB intersections.
  https://github.com/BLAST-WarpX/warpx/blob/ec1660d961696c865c87c26728b7e248b5454082/Source/Particles/ParticleBoundaryBuffer.cpp
- Public FEMM/openPMD source pin11e1a9d8281044c7e01dea9977291c871273da3f;
  source-inferred millimetre interpretation remains separate from original data.
  https://github.com/openPMD/openPMD-example-datasets/tree/11e1a9d8281044c7e01dea9977291c871273da3f
- Previous source/field admission release: PR53,3095e5a18d2507bd453c7ae356c3c5b57da0ae12.
- Existing cold receiver: PR44,8452c95a0c45034e3e842fd9db6b85f787062328;
  source/dependency hashes are checked by the new runner.

No third-party solver code/binary is redistributed in this release. It uses the
existing installed runtime and pinned sibling model. Raw diagnostics here are
new numerical outputs, not laboratory measurements. The work remains a draft
candidate; apparatus A/B/C mappings and separate BeyondQ D–D/D–T work are intact.
