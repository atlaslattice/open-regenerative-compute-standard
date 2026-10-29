# Stellar Forge Reference v.1.1

Local research configuration editor and reproducible Python verification workflow. New version: v.1 and all prior research originals remain unchanged. **Synthetic verification only. No calibrated fusion, ignition or acoustic enhancement prediction.**

## Install, configure and run

Python >=3.11; runtime NumPy 2.3.5. From this directory:

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install .
stellar-forge ui examples/pb11_reference.json --out experiment_editor.html
stellar-forge run examples/pb11_reference.json --out runs/demo_001
python -m unittest discover -s tests -v
```

Open experiment_editor.html locally in a browser, select acoustic location and preset, edit waveform parameters, and download the complete configuration. Run that JSON through the CLI and load its RESULTS.json back into the editor to inspect status and synthetic displacement. The bundled ui/STELLAR_FORGE_REFERENCE_v1_1.html is an already generated editor. No server, API, CDN or network call is required to use it. No public website has been deployed. JSON rather than YAML is the supported configuration format.

The UI is a configuration editor/result viewer, not a browser fusion solver. Defaults are test fixtures, not laboratory recommendations. Presets cover tone, sinusoidal frequency modulation, linear chirp and REFERENCE/OFF/SHAM/ON arms. Location options are pitcher, catcher, support and a characterized beamline component. Pitcher/catcher cannot acquire physical properties merely by selecting their names.

## Acoustics: an explicit, limited physical benchmark

The new module numerically integrates x'' + 2 zeta omega0 x' + omega0^2 x = a(t), with zero initial displacement and velocity, using RK4 and a coarse/fine time-step check. A tone has fixed frequency; sinusoidal FM integrates the instantaneous frequency into phase; linear chirp sweeps from carrier-deviation to carrier+deviation over the drive duration. All frequencies are Hz and phase is radians. Amplitude is prescribed modal acceleration in m/s², not measured acoustic power, pressure, strain or force. The synthetic natural frequency and damping are not calibrated component properties.

The output is displacement/velocity and sample-based peak/RMS metrics. Displacement is not stress or fatigue. Actuation must finish no later than shot arrival. If it finishes earlier, this version does NOT evolve the residual free response to shot arrival. It cannot assert target state at the shot. No drive-induced changes to nuclear rates, source spectrum, stopping, target thickness or alpha collection are implemented. A real actuation → measured material/source state → particle transport interface is a future calibration gate.

SHAM has zero intended coherent forcing in this benchmark; thermal/EM confounding is NOT modeled or validated. Reference/OFF intended driver energy is zero; SHAM/ON may declare driver wall energy. That energy must fit within the separately declared auxiliary total, not be silently added twice. Different locations currently share the mathematical test mode; this is visible metadata, not a claim of equivalent mechanical plants. Arbitrary user frequencies are test inputs, not validated material domains.

Conventional oscillator reference: MIT OCW driven damped oscillator lecture, https://ocw.mit.edu/courses/res-8-009-introduction-to-oscillations-and-waves-summer-2017/mitres_8_009su17_lec5.pdf . No measured Stars parameters are imported from it.

## Module integration and evidence

MODULE_INTEGRATION_v1_1.json inventories prior executable slices, registries, historical audits and exclusions. DELTA_COVERAGE_v1.json retains the original physical/experimental gates and adds v1.1 status entries. INTEGRATION_CONTRACT_CANDIDATE_v1_1.md adjudicates the supplied DeepSeek/Copilot suggestions. This is NOT a claim that all historical ideas or missing physical engines have been implemented.

Nine unchanged source modules are pinned in src/stellar_forge_reference/VENDOR_LOCK.json: source/observable semantics and covariance; local identifiability; CSDA transport; detector response; economics; energy screen; installed costs; six measurement-design comparisons; candidate stopping-source checks. Local namespace imports do not alter the originals. Product registries include three initial cross-reaction isotope identities and seven conditional p–B product identities; they are not simulated yields. The unpriced equipment template is bundled as component-cost input guidance.

The runner connects synthetic supplied alpha rays → layer transport → energy bins → expected detector counts. It separately reports synthetic design diagnostics, assumed energy scenarios, economics and capital. Those are not a single physical reaction/burn prediction. Evidence dependencies are explicitly recorded for the acoustic benchmark without promoting derived model maturity. The new dependency helper supports all four maturity gates and orthogonal provenance; historical module enums remain unchanged for source compatibility.

Only VERIFICATION_DEMO executes. Physical/calibrated modes refuse. The actual physical mass-correct correlated nuclear generator, dynamic burn and storage, calibrated source/material/detector/collector, full uncertainty propagation, grouped holdouts, all-shot causal inference and isotope recovery remain blocked/deferred. Later Gemini v0.4 exact-source local reproduction remains OPEN. SHUGS/TCSS operators remain external; no generic resonance multiplier exists. Nuclear, particle–wave and mechanical resonance research are retained as distinct future lanes.

## Optional external source audits

source_audit.raw_csv_path and sha256 configure the EXFOR-derived reported-alpha CSV importer. Paths are relative to the configuration file. Original required SHA256 is e56d240ea05fb8663debbb42cef99a93ef466d309eec3dbeb239f77509a6d089; no automatic alpha-to-event conversion occurs. The source is the archived C2973002 normalized table in the main research tree. Raw third-party files are not redistributed here.

reference_audits.pstar_aluminum_path optionally runs the pinned 132-row aluminum mirror check and 12 independent range-vs-stopping-integral comparisons. reference_audits.boron_quarantine_path optionally inventories the pinned headerless 77-row boron mirror while retaining quarantine. These data do not become calibrated B/BN transport. Mirror completeness, original units/reference mapping and physical calibration remain open. Exact SHA requirements are in the unchanged audit module.

Neither source audit feeds a nuclear-rate prediction. Default null paths produce explicit NOT_REQUESTED statuses, not synthetic substitute data. Missing requested source, unsupported range or invalid inputs receive failure receipts. The current structured failure-code subset is documented in the candidate contract; complete per-module classification remains future work.

## Reproducibility and validation

Every run reserves a NEW directory, records config/code/source/output hashes and returns REPORT.md, RESULTS.json, CONFIG.json, transmission.svg and MANIFEST.json. Parsing/runtime failures after reservation produce FAILURE.json. An existing directory is never overwritten. No RNG or live market feed is used. Same-environment repeat numerical results are checked; cross-platform exact identity is not promised. Input labels and hashes do not prove physical truth. Python dependencies are version-pinned, not a hash-locked container supply chain.

Thirty Python tests cover the prior integration workflow plus independent analytic transient oscillator response, FM/tone equivalence, amplitude scaling, sampling/timing guards, controls, no acoustic-to-nuclear feedback, evidence dependency isolation and UI creation. A standard-library Node DOM-event harness checks the emitted JavaScript configuration/export/viewer behavior. It is NOT a browser-rendering test. Browser QA was attempted but the environment had no installed Chromium binary; visual layout/browser compatibility remain unverified. No browser QA success is claimed.

The published run receipt additionally checks the actual aluminum/boron mirror audits, the archived 41-row CSV path, an exported UI configuration and deterministic repetition. Test outputs are not empirical calibration. No scientific freeze or PR merge occurs with this release.
