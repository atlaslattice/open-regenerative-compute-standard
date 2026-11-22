# Stellar Forge Reference v.1

An installable, offline research reference workflow for the Stars program. **Verification demo only: not a calibrated fusion simulator, ignition model or reactor design.** Originals and previous PRs remain unchanged.

## What is runnable

One configuration drives material-specific synthetic proton transport, supplied alpha-ray transport, energy binning and detector forward response. The same report also includes a source/observable audit when supplied, a separate noise-aware identifiability toy, a separate assumed energy scenario, and modular CAPEX/economic accounting. The latter calculations are not physically derived from the alpha-ray fixture. This distinction appears in JSON and the human-readable report.

The included example is called pb11_reference.json to identify its future reference lane; its materials, source rays and detector matrix are SYNTHETIC and have no claim to B/BN calibration. No three-alpha event generator or physical reaction-rate inference is implemented. Only VERIFICATION_DEMO runs are accepted. Exploratory and calibrated run classes are intentionally blocked pending their required implementations and data.

## Install and run

From this directory, using Python 3.11 or later:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install .
stellar-forge run examples/pb11_reference.json --out runs/demo_001
python -m unittest discover -s tests -v
```

NumPy 2.3.5 is the pinned runtime dependency. Installation may need a package index; runs need no network. This is a version-pinned Python package, not a fully hash-locked container. Example configuration schema is JSON v0.1 while package version is 1.0.0. A package v.1 name does not signify physics maturity.

Output directory must be new. Successful runs emit CONFIG.json, RESULTS.json, REPORT.md, transmission.svg and MANIFEST.json. Input, source, copied-code and output hashes are recorded; errors after directory reservation emit FAILURE.json. Malformed/unreadable JSON fails before reservation. Existing run directories are never overwritten. Randomness: none. Float last bits can vary by platform; repeat results in the same tested environment are byte-identical. File hashes show identity, not scientific validity.

The source audit is optional and does NOT feed the reaction probability. To audit the archived 41-point C2973002 CSV, copy the example into a new configuration, set source_audit.raw_csv_path relative to that configuration and set sha256 to e56d240ea05fb8663debbb42cef99a93ef466d309eec3dbeb239f77509a6d089. The upstream file is at research/stars_2_0/wp_b/revised/data/EXFOR_C2973002_SPRAKER_2012_41PT_CROSS_SECTION_SOURCE_NORMALIZED_2026-10-27.csv in repository commit 4512e9bb8505591ea207d28c2f0689ab5aecae9f. The importer applies only the documented hash-bound legacy comma repair. It preserves the reported alpha observable, statistical/shared errors and missing energy uncertainty; it never silently divides by three. Original EXFOR numeric reproduction is a prior separate receipt, not rerun by this importer alone. Third-party raw data are not redistributed in this package.

## Integration and deltas

**Not all relevant deltas are implemented.** DELTA_COVERAGE_v1.json records 23 requirement/status entries, including implemented guards, partial interfaces, blocked physics, deferred experiments and superseded historical statements. This is a scoped traceability register against STARS DELTAS and subsequent user requirements, not proof that every historical suggestion has been found. Unknown or deferred requirements must remain visible when promoting the release.

VENDOR_LOCK.json records seven unchanged modules copied from the earlier draft slices, with exact SHA256 and parent commit. Local package imports provide namespace isolation without modifying the original files. Attribution remains to the earlier slice and council sources; no new nuclear theory is claimed. Repository license applies to project code; external data retain upstream terms. Source-label enums are caller declarations, not independent certification.

The physically unresolved gates include observable-to-event normalization, measured mass/Q and correlated kinematics, actual target/beam/response calibration, straggling/scattering, connected burn/storage/collector dynamics, grouped experimental holdouts, causal shot accounting, isotope retention and dated market/installed-cost qualification. Later Gemini v0.4 exact-source reconciliation and local reproduction remain OPEN. Source received/executed by Tidal is distinct from a GPTWork rerun.

Three burn research tracks are represented in the accounting: startup/drive-off, externally driven and grid-assisted. A single-pass reference is also retained. No selected track or positive assumed energy result certifies ignition. Installed CAPEX remains unknown when any asset estimate is missing; coproduct potential is not realized revenue. No actual isotope price is preloaded.

## Validation and next release

Tests exercise installed command execution, connected transport/binning/response against independent arithmetic, input-domain mutations, stopped particles/background preservation, source covariance and energy uncertainty, observable conversion refusal, zero versus missing, deterministic outputs, hashes, no-overwrite behavior, calibrated-mode refusal, alpha energy partition and shared capital assets. Original module verification receipts remain at their prior paths; this release adds cross-module tests.

Next priority: recover and independently execute the actual later Gemini engine, qualify physical nuclear/material/detector inputs and connect mass-correct reaction events to transport. Then a local UI can expose configuration, evidence state and downloadable reports. No public hosted computation or website is deployed here, and no PR is merged or scientific prediction frozen.
