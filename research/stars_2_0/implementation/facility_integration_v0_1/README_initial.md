# Stellar Forge — source-to-facility integration v0.1

2026-11-01. Additive continuation of draft PR61, base `34c4a8c3f3994805958395a48787be9cda56f00c`. A single executable reference profile now connects freshly run source PIC and receiving target, correlated alpha generation, finite escape, ideal planar collection and explicit facility accounting. **It is not a spatially closed or calibrated physical apparatus. Actual A/B/C net power remains unevaluated.** No merge or scientific freeze.

## Executed chain

`pipeline_v002.py` executes the prior source/target runner (actual WarpX), then the prior correlated-alpha producer, then `run_v004.py` with the NEW receiver and event-bank outputs. It does not merely concatenate old summaries. Fresh bank/receiver provenance is checked. The field map is the previously qualified numerical interpretation of a public FEMM dataset, not an actual STARS magnet map. Source/target controls, event proposals and relative finite geometry retain their original verification/exploratory evidence categories.

PROFILE.json uses a separate control ID under C's reference family; it does not relabel or replace original C, A, B or the unrecovered ceramic pocket. All original C inventory modules remain in MODULE_RETENTION.json, with unresolved couplings explicit. The current field/source and stopping state do not implement sustained burn, plasma self-consistency, recirculation, a physical support or acoustic-induced source changes.

## Result: a useful energy frontier

For the fixed source control, source proton kinetic energy is 23625 weighted MeV. Expected primary-channel nuclear release is 0.141354941 weighted MeV, about **5.983 ppm** of the source kinetic energy. This ratio is conditional on the modeled reaction count and cold state; it is not a measured efficiency.

Let B be source kinetic input, Q the modeled nuclear release and eta the gross wall-to-source kinetic efficiency. For this externally driven cold-target control, with no other energy sources, even an ideal enclosing facility cannot return more than B+Q. With zero auxiliary draw and zero storage change:

`net <= B + Q - B/eta`.

Hence strictly positive net requires `eta > B/(B+Q) = 0.9999940167578748` (about **99.9994%**). This deliberately optimistic bound allows recovery of every modeled energy channel, including energy that leaves the modeled source domain. It is not a heat-recovery prediction. Real losses or auxiliary draw make the requirement harder. The three dimensionless efficiency probes (1, 0.5, 0.1) are numerical evaluations of this inequality, not assumed device efficiencies.

At the selected aspect=2, bias=1MV coherent-source control, ideal alpha circuit transfer is 0.0107488877 weighted MeV. The remaining source/alpha energy is NOT automatically saleable electricity or recoverable heat. No TMX efficiency is imported from PR61. Neither more simulated particles nor a common normalization change improves the dimensionless bound within the assumed linear control. Different reaction probabilities, transport, plasma states, repeated encounters or burn require a new physical calculation; the inequality's current numerical threshold is not a verdict on those designs.

## Explicit facility interface

`accounting_v002.py` separates direct wall-to-beam efficiency from the product of wall-to-laser and laser-to-beam efficiencies; supplying both routes is rejected. Recovery of other alpha energy and non-alpha energy must be supplied separately and cannot exceed unity in this restricted control. Physical loads have unique instance IDs, with per-attempt and per-fired wall draws. The source driver cannot be booked again as an auxiliary load. All physical operating inputs in the default profile are unknown, not replaced by zero.

Preparation costs remain per attempted preparation, including nonfiring outcomes. Firing fraction changes expected throughput and amortizes fixed attempt costs; it does not change this fixed per-fired reaction bank. A source/target change from acoustic preparation or jitter reduction must enter a new physical source/transport calculation. This interface does not transform diagnostic qualification into a nuclear gain.

Steady storage-neutral power is returned only for a supplied zero inventory change. A nonzero storage change requires a qualified flow adapter; a formal `load - wall + (U_end-U_start)` correction is exposed separately but not promoted to a valid steady result. Missing rates allow conditional energy calculations when otherwise complete, but not power. Negative results remain negative.

The initial accounting/run versions are preserved. The v002 accounting adds the noncyclic-storage guard. `run_v003.py` adds live bank/receiver input binding. Current `run_v004.py` also rejects an unregistered collector comparison rather than silently treating a missing comparator as a passed test. `pipeline_v002.py` uses that current entrypoint. These refinements do not change the default profile's physical outputs. Use the current commands below.

## Verification and restoration

- A pinned Git snapshot and 266 critical restored files were hash-verified.
- The pinned WarpX/AMReX26.10 runtime was reinstalled and six prescribed-E alpha trajectory controls freshly passed 27 checks.
- The archive-pinned Michel CPC backend was rebuilt; compiled binary/source build receipts are retained, not redistributed binaries or source archives.
- Fresh source/target execution passes 25 checks and 19 original bridge tests; its scientific result equals the archived reference exactly.
- The freshly regenerated 4096-proposal alpha bank passes 30 checks and matches the prior same-seed bank's arrays and scientific values exactly (elapsed runtime excluded).
- Each integrated run passes 21 checks. Nineteen unit tests cover budgets, source alternatives, missingness, per-attempt costs, storage and unsupported-comparator rejection. Saved-array audits and complete live-input replay comparisons are recorded separately.

This verifies software behavior conditional on the nominal physics/models and data. It does not turn numerical precision, repeatability or an installed solver into independent experimental validation. Source/model/material/facility uncertainties are not propagated into a physical confidence interval.

## Run

Python3.12.14, NumPy2.3.5 and inherited SciPy1.17.0/GSL coupling/C++ build requirements were used. Keep implementation versions as siblings. The prior WarpX installation manifest is `warpx_pb_kinetic_v0_1/environment_install.txt`; the backend build recipe is `coherent_source_v0_8/prepare_cpc.py`. The source-map fetch/preparation scripts are `warpx_source_field_v0_1/fetch_dataset.py` and `prepare_maps.py`; execute copies in a fresh working folder to preserve their original receipt paths. They require the WarpX runtime's openPMD Python package. Installation/build/map receipts for this execution are retained under restoration and the raw replay archive.

From the repository root, after restoring dependencies and unpacking PR57/58 inputs:

```
python research/stars_2_0/implementation/alpha_birth_escape_v0_1/unpack_banks.py
python research/stars_2_0/implementation/finite_alpha_transport_v0_1/unpack_arrays.py
python research/stars_2_0/implementation/facility_integration_v0_1/pipeline_v002.py --models research/stars_2_0/implementation --runtime /path/to/warpx/environment --map /path/to/canonical_mm.h5 --profile research/stars_2_0/implementation/facility_integration_v0_1/PROFILE.json --out new_full_run
```

Or replay the numerical layers using the pinned saved source bank, without a new PIC/backend run:

```
python research/stars_2_0/implementation/facility_integration_v0_1/run_v004.py --models research/stars_2_0/implementation --profile research/stars_2_0/implementation/facility_integration_v0_1/PROFILE.json --out new_integration_run
python -m unittest discover -s research/stars_2_0/implementation/facility_integration_v0_1 -v
python research/stars_2_0/implementation/facility_integration_v0_1/unpack_v002.py
python research/stars_2_0/implementation/facility_integration_v0_1/audit.py
```

Every run requires a new output directory. The compressed replay archive preserves arrays and raw source/trajectory traces. A freshly generated event bank identical to PR57 is referenced by hash rather than redundantly copied. Original inputs, failures and versions remain intact. Prices/isotope revenue are not converted into energy credits. See DECISION_MEMO.md and APPARATUS_SPEC_AUDIT.md for the concrete next physical decisions.
