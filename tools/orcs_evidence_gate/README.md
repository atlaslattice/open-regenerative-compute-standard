# ORCS evidence-vector gate (candidate)

This small, offline Python standard-library gate validates **claim metadata**, not scientific truth or real-world operation. It is an additive component of [ORCS #70](https://github.com/atlaslattice/open-regenerative-compute-standard/pull/70), not the full 84-module cross-site engine.

## Run

```sh
cd tools/orcs_evidence_gate
python -m unittest -v test_check.py
python check.py example_unknown.json
```

A schema PASS means required claim fields and seven independent state entries are present; it does **not** verify that a source exists or that the evidence supports the claim. A `VERIFIED` status requires nonempty evidence_ref and observation strings, but these are **self-reported**, not independently authenticated. Do not promote them to measured or deployed capacity without review.

The seven dimensions are authority, funding, construction, commissioning, operation, measured_output and delivered_benefit. UNKNOWN is valid and should remain UNKNOWN when source evidence is absent. Reserve coverage must be computed separately for each product, region, accessibility boundary and demand interval.

## Current CI blocker

GitHub Actions run [45053865330](https://github.com/atlaslattice/open-regenerative-compute-standard/actions/runs/45053865330) failed. Its job log could not be retrieved by the connected review lane; the root cause is unknown. Local tests and hosted CI must be reported separately. No merge approval follows from this document.

## Negative controls to preserve

- No evidence laundering from DPA funding ceiling to installed diesel capacity.
- No conversion of announced tanker voyage to delivered, accessible U.S. inventory.
- No conversion of a desalination permit to achieved zero-liquid-discharge.
- No conversion of LNG thermal-integration design to metered net power.
- No accidental parsing of duplicate JSON keys, nonfinite values or malformed statuses as valid evidence.

## Limits

No network calls, signature checks, source retrieval, scientific calibration, rights decisions or deployed authorization. Inputs must be trusted only as candidate data.
