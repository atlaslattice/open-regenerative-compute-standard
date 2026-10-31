# Beyond Q v1.4 — Slowing, escape and eight-hour fuel-cycle research

October 30, 2026 (America/Chicago). New versioned package stacked on PR #48,
parent `674eb174ff935bcfc9829109b57c1187d25dc710`. Earlier releases are unchanged.

Start with [REPORT.md](REPORT.md), [SOURCES.md](SOURCES.md),
[the figure](outputs/multiscale.svg), [comparison data](outputs/coupled_burn_comparison.csv)
and [eight-hour results](outputs/eight_hour_summary.csv).

This package retains six accepted WarpX cases, including actual 0.1-second
background-drag and drag-plus-DT calculations, plus three rejected cold-triton
initialization cases. The eight-hour cases are **reduced fuel-cycle simulations**,
not eight hours of fully resolved WarpX reactor evolution. All physical G1–G5
remain OPEN and all qualified-surplus fields remain null.

## Explicit power bases

| configuration_id | A gross DD fusion | B gross DT fusion | Status |
|---|---:|---:|---|
| historical_20_1130 | 20 MW | 1130 MW | Preserved historical benchmark |
| dual_laser_1100_1100 | 1100 MW | 1100 MW | Current repository user-corrected design input; no demonstrated laser operating point |

See [the parent correction](../DUAL_LASER_POWER_BASIS_LOCK_2026-10-30.md).
The historical 20 MW **net electrical** assumption for the new laser design is
not used as its fusion source. Explicit gross-W fields and scenario locks reject
mixed power bases. New laser cases reuse unqualified testbed transport and
prescribed plasma assumptions; they do not simulate a laser.

## Reproduce

Install micromamba from its official distribution. From this directory:

```bash
micromamba create -y -p /absolute/path/wx-env -f outputs/environment_explicit.txt
BQ_ENV=/absolute/path/wx-env
BQ_CACHE=/absolute/path/bq-v14-cache
"$BQ_ENV/bin/python" run_warpx.py --executable "$BQ_ENV/bin/warpx.3d" --cache "$BQ_CACHE"
"$BQ_ENV/bin/python" run_research.py
"$BQ_ENV/bin/python" plot_results.py
"$BQ_ENV/bin/python" run_checks.py
```

The explicit lock begins with `@EXPLICIT`; package URLs are retained and
actual installed package checksums are separately recorded. The inherited v1.3
listing had a display banner and lacked that marker: this new release corrects
the install format without modifying v1.3. The Linux build uses two CPU OpenMP
threads, WarpX 26.10, SciPy, NumPy and yt. Its embedded WarpX git version is
Unknown; package, binary and reference-source identities remain distinct.
Allow several GB for dependencies and regenerated plotfiles.

Neighboring v1.2/v1.3 directories are required for reused transport means,
physical constants and source cross-section functions. `run_checks.py` also
runs the archived v1.3 suite, writing its logs only in this release. v1.2's full
OpenMC-dependent suite is not rerun here; its prior results remain historical.
No new OpenMC calculation is claimed.

Saved `outputs/warpx/*` reduced diagnostics, used inputs, execution logs and
status records permit numerical inspection without rerunning. Full field/particle
plotfiles are regenerable from decks. Rejected setup results and their input
are retained under `outputs/failures/cold_triton_initialization/` and excluded
from accepted comparisons. `outputs/package_sha256.json` covers package bytes.

## Model files and units

- `slowing.py`: approximate electron/ion drag, Maxwellian-D reaction quadrature,
  competing fast burn/escape and an assumed thermal transition.
- `run_warpx.py`: pinned upstream stopping test, trace-drag and coupled-DT decks.
- `run_research.py`: numerical comparisons, 36 sensitivity cases, transition and
  refinement studies, 54 eight-hour scenarios and four startup brackets.
- `fuelcycle/`: versioned adaptation of v1.2 with minute schedule slots and
  disjoint fast-burn/fast-escape/thermal routes; rates remain per calendar day.
- `test_multiscale.py`: numerical acceptance, source and gross-power identity checks.

Kinetic energy uses joules/eV, density m^-3, temperature eV (converted to kelvin
in WarpX), and time seconds. Plant stocks are kg-T, rates 1/day, minute slots
1/1440 day, with explicit seconds-to-days conversion. One FPY remains365.25
calendar days; this run is exactly8 hours and is not an annual-surplus estimate.

Schedule manifests encode half-open slot ranges as `[start,end,A_on,B_on]` and `[start,end,extract_A,extract_B,process_A,process_B]`. Their exact480-slot coverage is regression-checked. Final check results:19v1.4 tests and16archivedv1.3 tests pass.
