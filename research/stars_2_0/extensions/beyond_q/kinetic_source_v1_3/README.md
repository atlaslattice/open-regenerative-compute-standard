# Beyond Q v1.3 — WarpX D-D / D-T kinetic-source benchmark

**Actual executions, October 30, 2026.** Stacked on draft PR #46 / v1.2 at
`1d759cffda8423993fa1a6887a124ac7e29d6b2d`. All prior releases preserved.
Canonical reference remains **A20 MW primary DD, B1130 MW DT**.
These powers are not imposed as an achievable operating point in the microscopic box.

Read [REPORT.md](REPORT.md), [SOURCES.md](SOURCES.md),
[outputs/benchmark_summary.csv](outputs/benchmark_summary.csv),
[outputs/inventory_kernel_comparison.csv](outputs/inventory_kernel_comparison.csv)
and [outputs/benchmark.svg](outputs/benchmark.svg).

- Two upstream DD/DT tests run without numerical-parameter overrides; supplied analyses pass.
- Nine collision-network cases execute actual DD-born T followed by secondary DT.
- Six cases exercise the existing v1.2 inventory kernel against WarpX sources.
- 16 new tests and 17 v1.2 tests pass in their appropriate environments.
- No physical research gate closes and no qualified surplus is inferred.

## Reproduce

Install micromamba using its official distribution. On compatible Linux x86-64:

```bash
micromamba create -y -p /absolute/path/wx-env -f outputs/environment_explicit.txt
WX_ENV=/absolute/path/wx-env
WX_CACHE=/absolute/path/wx-cache
"$WX_ENV/bin/python" run_upstream.py --executable "$WX_ENV/bin/warpx.3d" --cache "$WX_CACHE"
"$WX_ENV/bin/python" run_campaign.py --executable "$WX_ENV/bin/warpx.3d" --cache "$WX_CACHE/campaign"
"$WX_ENV/bin/python" analyze.py --cache "$WX_CACHE/campaign"
"$WX_ENV/bin/python" export_source.py
"$WX_ENV/bin/python" compare_inventory.py
"$WX_ENV/bin/python" plot_results.py
"$WX_ENV/bin/python" -m unittest test_benchmark -v
```

The lock includes WarpX 26.10, Python 3.14, yt, SciPy and plotting dependencies.
A fresh compatible environment can also use conda-forge `warpx=26.10 yt scipy
matplotlib`, but its dependency versions must be recorded separately. GPU/MPI
is not required; these runs use two CPU OpenMP threads. Allow approximately
15GB disk for installation plus full upstream plotfiles; no wall-time guarantee.
No WarpX solver source is copied or patched. Vendored upstream test fixtures,
analysis/parser and license/notices retain their original attribution.

The separate OpenMC v1.2 suite requires its own installed environment:

```bash
"$WX_ENV/bin/python" run_checks.py --reference-python /absolute/path/openmc-env/bin/python
```

`run_checks.py` writes logs only under this release. The inherited eight-stock
campus model is unchanged. `compare_inventory.py` imports its exact compartment
kernel from the neighboring v1.2 directory, so preserve the stacked repository.

## Audit without rerunning

Saved reduced diagnostics, used inputs, logs and input/provenance hashes are in
outputs/runs. The baseline compressed NPZ contains final daughter weights and
momenta plus initial/final D weight arrays. It supports independent weighted
source and compensated donor-accounting checks. Full upstream/campaign
plotfiles remain regenerable from inputs; multi-GB field/particle plotfiles
are not bundled. Other-case spectra/moments and all reduced diagnostics are
included. NPZ momentum units are kg·m/s and weights are physical particle counts.

`outputs/source_interface.json` is tagged **ACTUAL_WARPX_SOURCE_SAMPLE_NOT_TRANSPORT**.
It must not be passed off as an OpenMC transport result. Formal20 MW renormalization
of the2 ps interval is arithmetic only, not a stationary reactor source. Future
transport coupling must preserve spectrum, angular distribution, absolute source
normalization, geometry, time-window provenance and uncertainty.

`outputs/numerical_replay.json` records an independent same-seed run: number,
energy and momentum diagnostic files were byte-identical. Reproduction on other
hardware/builds should compare numerically, not assume binary identity.
