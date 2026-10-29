# Stellar Forge readiness v.1.2

An additive preparation-policy evaluator and local UI for Stellar Forge Reference v.1.1. Original packages remain intact. **Offline sampled-observation analysis; no live sensors or laser-control connection. Readiness does not prove saturation, safe triggering or fusion benefit.**

## Run

Python >=3.11, standard library only. Install this add-on from this directory:

```bash
python -m pip install .
stellar-forge-ready ui examples/readiness_attempts.json --out readiness_editor.html
stellar-forge-ready evaluate examples/readiness_attempts.json --out runs/attempt_batch_001
python -m unittest discover -s tests -v
```

The generated editor defaults to Prepare until ready, with fixed-duration comparison under the policy selector. It edits confirmation, timeout and fixed duration for all attempts in the loaded batch. Specimen-specific criteria, calibrations, observations and outcomes remain editable in full JSON. Download configuration, evaluate through the installed CLI, and load RESULTS.json into the viewer. No calculation or device triggering occurs in the HTML. The already-generated ui/STELLAR_FORGE_READINESS_v1_2.html is bundled for local use; no public website deployment.

This add-on does not replace the v.1.1 waveform/location editor or directly feed a fusion-yield model. Link attempt.acoustic_configuration_id to the exported v.1.1 configuration and retain both hashes in the experiment record. The readiness input is an observation trace, not invented sensor data derived automatically from the uncalibrated oscillator. Later integration needs a calibrated response/sensor adapter. No existing Stellar Forge modules or scientific assumptions were overwritten.

## What gets recorded

Every attempt has an ID, UTC start timestamp, acoustic configuration ID, control arm, specimen/batch, composition, geometry, support, sensor/calibration identities, criteria with units, complete observation trace and subsequent-outcome fields. Readiness criteria may include amplitude/envelope error, phase error, thickness, temperature or a separately justified stability metric; examples use synthetic envelope and temperature only. Phase wrap and preprocessing must be declared upstream. Criteria units are labels, not automatic unit conversions or proof of calibration.

An observation qualifies only when all required values are present and within the specified inclusive bounds. The UNTIL_READY policy reports readiness at the first observed sample completing the confirmation window. Missing values, out-of-bound values or sample gaps larger than max_sample_gap_s reset the window. No unobserved crossing time is interpolated. Passing sampled criteria is not proof the state stayed acceptable between samples. Sensor bandwidth, sampling rate, noise/hysteresis and thresholds require independent qualification.

The evaluator retains first qualifying sample, first confirmed readiness, history, data gaps, preparation end, outcome and integrated driver wall energy. Power is trapezoidally integrated between supplied samples; sparse power measurements can miss transients. It never extrapolates power beyond the observation span. Aborts have priority if exactly coincident with readiness. A fixed-duration comparison ends at its requested time whether or not criteria were ever met; it is not automatically labeled ready. Incomplete observation traces remain incomplete. No value is inferred for fusion counts or trigger phase.

Successful preparations, timeouts and aborted attempts all remain in ATTEMPTS.jsonl and SUMMARY.csv. Conditional readiness-time samples are explicitly labeled; aggregate comparisons must also include timeout/abort fractions and cost per attempted preparation. IDs are unique within a batch; cross-run uniqueness/experiment database is not implemented. Use immutable run directories and an external experiment registry when aggregating campaigns.

## Physical interpretation

The controlled entity is the specimen/material configuration and response modes, not individual nuclei becoming acoustically ready. Different specimens, supports, material histories and operating conditions may have different settling distributions. No universal saturation duration is assumed. Ten seconds or one minute is an input observation window, not a predicted benefit. A synthetic long-window test first qualifies at 40 s and confirms at 42 s.

For continuous operation distinguish apparatus startup/settling from each material element's residence time. A stable field does not establish a particular droplet's exposure. Drive-stop delay, phase synchronization, residual vibration, target motion/flow and thermal/mechanical history must be supplied by qualified measurements or models. This release does not solve them, measure full saturation or infer acoustic effectiveness on nuclear outcomes.

Future facility use requires independently validated instrumentation, interlocks, operator procedures and the facility's own laser-control system. This package intentionally has no trigger output, network control API or device driver.

## Reproduction and limits

Each evaluation requires a new output directory. INPUT.json preserves the complete configuration; ATTEMPTS.jsonl logs each input/result pair; RESULTS.json and SUMMARY.csv retain all statuses; REPORT.md summarizes them; MANIFEST.json hashes inputs, code and outputs. Malformed evaluations receive FAILURE.json. Existing output directories refuse replacement. No RNG, live market price or physical calibration is used.

Thirteen Python tests include independent time/power arithmetic, missing observations, sample gaps, simultaneous abort priority, long preparation, fixed-duration comparison, invalid timestamps/power/calibrations, duplicate IDs, outcome preservation, installed CLI flow and overwrite refusal. UI event tests exercise policy changes and export; browser-rendering QA remains unavailable because the current environment lacks Chromium. No browser compatibility or lab validation is claimed.
