# Stellar Forge — executed WarpX pB and magnetic-orbit benchmarks v0.1

2026-10-30, America/Chicago. New append-only lane following draft PR49. **Actual
WarpX execution**, not the earlier scalar-header harness. No full apparatus,
acoustic enhancement, confinement lifetime, ignition or net-power result claimed.

## Results

1. Recreated the other thread's WarpX26.10 conda environment from PR48's URL lock.
   CPU, double precision, no MPI, two OpenMP threads. Binary banner has Unknown git
   revision; package/build, binaries and environment are hashed separately.
2. Ran the supplied 3D pB input and analysis. All five native subtests pass their
   unchanged analysis. Final canonical run uses byte-exact release-source fixtures.
   Native CMake requests two MPI ranks; our single-process layout is a recorded
   difference, not an exact recreation of the CI configuration.
3. Executed seven particle-pushing fixtures: two uniform-field helix resolutions,
   loss-cone escape, mirror reflection and timestep refinements. Compared with an
   independent relativistic Lorentz ODE and, for the uniform case, an analytic helix.
4. Retained failures: invalid initial boundary combination; coarse mirror momentum
   phase errors exceeding 2%; an extra terminal newline introduced by file packaging.
   None was hidden by loosening tolerance or changing upstream numerical settings.
5. Exported retained particles with actual diagnostic position, time, SI momentum
   and weight. Escaped particles have no invented boundary phase-space records.

| Numerical test | Result |
|---|---|
| Native pB reaction/product analysis | PASS, unchanged analysis, canonical run002 |
| Native repeat | Weighted count and alpha-energy summaries identical |
| Uniform-field relative momentum error, dt=0.2 ns | 0.003307 |
| Uniform-field relative momentum error, dt=0.1 ns | 0.0008268 |
| Mirror reflection error, dt=0.2/0.1/0.05 ns | 0.08303 / 0.02077 / 0.005195 |
| Loss-cone trajectory error, dt=0.05 ns | 0.006300 |
| 10° pitch | Escapes the +/-5 m synthetic mirror domain |
| 45° pitch | Reflects, first turn z≈2.498658 m; adiabatic guide 2.500000 m |
| Relative kinetic-energy drift | <2e-14 in these magnetic-only fixtures |

Error is maximum vector-momentum difference divided by initial momentum norm,
over each run's retained diagnostic samples. Coarse failures remain: **15/18
listed numerical checks pass; three coarse phase-accuracy checks fail**. Four
explicitly selected qualified cases pass the unchanged 2% phase-error target,
with the required escape/reflection behavior and decreasing timestep error.
This tolerance is a numerical engineering target, not experimental uncertainty.
Near-machine-precision energy conservation does not imply accurate gyrophase.

All orbit values (675keV proton, 2T field, geometry, pitch and duration) are
**synthetic verification fixtures**, not recovered apparatus specifications.
The mirror field is divergence-free:
Bx=-B0*a*x*z; By=-B0*a*y*z; Bz=B0*(1+a*z^2), with a=0.16m^-2.
At z=+/-5m its on-axis mirror ratio is5. Magnetic mirroring here is prescribed
field transport, not optical reflection or a physical PRISM field map.

## Reproduce

Install micromamba from its official distribution, then on compatible Linux:

```bash
micromamba create -y -p /absolute/path/wx-env -f environment_install.txt
python run_native.py --executable /absolute/path/wx-env/bin/warpx.3d --analysis-python /absolute/path/wx-env/bin/python --out /tmp/sf-pb-native-001
python run_orbits.py --executable /absolute/path/wx-env/bin/warpx.3d --out /tmp/sf-orbits-001
/absolute/path/wx-env/bin/python verify_orbits.py --runs-root /tmp/sf-orbits-001 --output /tmp/sf-orbit-analysis-001.json
```

Or verify saved orbit traces without rerunning WarpX:

```bash
python unpack_diagnostics.py --out /tmp/sf-saved-traces-001
/absolute/path/wx-env/bin/python verify_orbits.py --runs-root /tmp/sf-saved-traces-001 --output /tmp/sf-saved-analysis-001.json
```

Verification uses NumPy/SciPy; upstream pB analysis additionally uses yt. Installing
this full environment and generating native plotfiles requires multiple GB.
Output roots must be new. Do not rerun legacy prepare/analyze scripts into bundled
output paths; those scripts are retained to document original execution history.
Portable run_native.py, run_orbits.py and verify_orbits.py are the current entrypoints.
Full native plotfiles are regenerable, not bundled; manifest retains their hashes.
All raw reduced orbit diagnostics are preserved in diagnostics_reduced.tar.gz.

## What is not modeled

The native pB test has max_step=1 and disables particle pushing/deposition. Its
huge event multipliers alter macroparticle sampling/weights, not physical fusion
probability. Its large weighted outputs are constructed test populations, not
predictions of device yield. Sequential three-alpha generation is not the complete
coherent l1+l3 source model and its fixed Q convention still needs reconciliation
with other Stars branches. Empirical upstream tolerances are not physical accuracy.

Orbit fixtures do push particles, with deposition disabled and no collisions,
fusion, radiation, target, laser or self-consistent plasma field. PEC boundaries
apply to otherwise zero mesh self-fields; the analytic magnetic field is applied
directly to particles, with no solved coils/currents or hardware field-boundary
claim. Finite particles are absorbed at domain boundaries. No beam capture
fraction, stationary confinement or facility magnet power is inferred.

## Integration progression

Completed: scalar kernel qualification (PR47), native pB CPU regression, finite
external-field trajectory tests, actual-state particle export.
Next: source-qualified input phase space and realistic magnetic geometry; Coulomb
relaxation and radiation qualification; solid/plasma region ownership; reaction
and product transport in the same evolving case. Then hollow-sphere laser source,
ceramic-pocket state and acoustic-conditioned ensembles. Preserve a fixed-source
control so changed source production does not hide worsened confinement.

Original A/B/C apparatus mapping and Beyond Q D–D/D–T separation remain intact.
Source/fabrication/acoustic/detector and whole-facility power gaps are unchanged.
