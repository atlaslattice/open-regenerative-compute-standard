# Beyond Q v1.2 — Neutronics Research Package

Atlas Lattice / STARS 2.0. October 30, 2026. New versioned artifact stacked
on draft PR #41, parent `dbb01d6d96a429cd3aeae5d6edaf5c006afb3f02`.
Earlier releases are untouched. **B=1130 MW D-T; A=hypothetical 20 MW primary D-D.**

Start with [WHITE_PAPER.md](WHITE_PAPER.md), [SOURCES.md](SOURCES.md),
[gate_status.json](gate_status.json) and [dashboard.html](dashboard.html).
Download dashboard.html and open locally for interactive filters. GitHub's
file view does not execute HTML. Scientific plots are in outputs/*.svg.

**44 actual OpenMC campaign calculations** plus a distinct synthetic-data
analytic method benchmark. These are results for an explicitly assumed,
room-temperature-data spherical testbed, **not ARC V3A predictions or physical
validation**. All qualified-surplus fields remain null. Evaluated nuclear data
are fetched from IAEA; no breeding responses are fabricated.

## Reproduce

Run from this directory. Requires Linux x86-64 for the exact explicit conda
lock; other environments require a new recorded lock and numerical comparison.
Install micromamba from its official distribution and use:

```bash
micromamba create -y -p /absolute/path/bq-env -f outputs/environment_explicit.txt
```

Alternatively `micromamba create -y -p /absolute/path/bq-env -c conda-forge openmc=0.15.3`
creates a compatible environment but is not the exact dependency lock.
Use that environment's Python and executable below. Set task-specific paths:

```bash
BQ_ENV=/absolute/path/bq-env
BQ_CACHE=/absolute/path/bq-cache
"$BQ_ENV/bin/python" prepare_data.py --cache "$BQ_CACHE/data"
"$BQ_ENV/bin/python" campaign.py --xs "$BQ_CACHE/data/hdf5/cross_sections.xml" --executable "$BQ_ENV/bin/openmc" --cache "$BQ_CACHE/campaign"
"$BQ_ENV/bin/python" analytic_benchmark.py --executable "$BQ_ENV/bin/openmc" --output "$BQ_CACHE/analytic_benchmark"
"$BQ_ENV/bin/python" integrate.py --cache "$BQ_CACHE/campaign"
"$BQ_ENV/bin/python" analyze_outputs.py --cache "$BQ_CACHE/campaign"
"$BQ_ENV/bin/python" plot_results.py
"$BQ_ENV/bin/python" build_dashboard.py
"$BQ_ENV/bin/python" run_checks.py
```

The published analytic QA result is already in outputs/analytic_benchmark.
A fresh analytic run writes its new artifacts to the chosen cache; compare
benchmark_result.json with the published result and retain its new provenance.
The campaign cache skips completed matching cases. Use an empty cache for
fresh transport execution; `--only DT_Li0.075_cm90` runs a smoke case but
writes a subset summary, so do that in a separate checkout from full analysis.
Downloads are roughly 1.5 GB ACE plus converted HDF5; allow several GB disk.
No externally hosted live service is required for the saved dashboard.

## Audit recorded calculations without rerunning transport

```bash
"$BQ_ENV/bin/python" -m zipfile -e outputs/raw_statepoints.zip outputs/runs
"$BQ_ENV/bin/python" integrate.py --cache outputs/runs
"$BQ_ENV/bin/python" analyze_outputs.py --cache outputs/runs
"$BQ_ENV/bin/python" run_checks.py
```

Statepoints, tally sums/squares, standard errors, XMLs and per-run hashes are
included. The bridge checks raw-statepoint, provenance and XML hashes, source
identity and matching A geometry, and compares its yield against raw tally
moments. Synthetic responses, missing statepoints and edited yield summaries
are rejected. This is reproducibility checking, not a tamper-proof trust system.

`outputs/numerical_replay.json` records one fresh same-seed replay. The
source-data ACE hashes are locked in outputs/nuclear_data_manifest.json;
prepare_data refuses changed source bytes. HDF5 conversion hashes and absolute
path-dependent XML hashes may differ on another machine and must be recorded
anew, not silently asserted byte-identical. Statistical results, not binary
HDF5 timestamps, are the replay objective.

## Modules and outputs

- prepare_data.py: source-locked evaluated data retrieval and ACE-to-HDF5 conversion.
- transport.py / campaign.py: explicit materials, geometry, source, tallies and 44-run matrix.
- analytic_benchmark.py: synthetic pure-absorber analytic method QA, NOT breeding data.
- integrate.py / fuelcycle/: separate source spectra, A recovery routes, dynamic stocks and adverse cases.
- analyze_outputs.py: matched secondary-burn, mass-percent and energy ledgers, timestep sensitivity.
- plot_results.py / build_dashboard.py: reproducible plots and self-contained interactive explorer.
- run_checks.py: isolated regression suites; failure exit status and visible logs.
- AUDIT_HISTORY.jsonl: append-only corrections; earlier histories remain in earlier releases.

Inputs use cm, g/cm³, K and eV in transport; kg-T, calendar days and 1/day
in inventory. Source tally yields are atoms/source-neutron, not kg/year.
Full-power-year conversion is 365.25 days; integrated runs use 365 calendar days.
See the white paper for boundaries, evidence classes and unresolved parameters.
