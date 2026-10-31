# Stellar Forge — source/field admission and FEMM scale audit v0.1

2026-10-30 America/Chicago. Actual WarpX26.10 executions, appended after PR50.
No previous model or apparatus definition changed. A/B/C retain their meanings;
Beyond Q D–D/D–T assumptions are not imported. **No STARS beam-capture fraction,
acoustic gain, ignition, usable energy or net-power prediction is produced.**

## Material finding

A public openPMD magnetic-mirror dataset already used by WarpX supplies a useful
geometry-derived field benchmark. Its FEMM file declares **millimeters**, and its
Lua sampling coordinates match the exported numerical mesh coordinates. The
openPMD file instead declares gridUnitSI=1. Thus the supplied coordinate numbers
are interpreted as metres, a factor1000 different in length from the FEM source.
This is a source-chain inconsistency or undocumented rescaling, not proof of
author intent, an erroneous experiment, or a universal WarpX problem.

We preserve the original and create two separately named derivatives:
- metadata_only_mm: change gridUnitSI only, a deliberate negative control;
- canonical_mm: multiply numeric gridSpacing and gridGlobalOffset by.001, retain
  gridUnitSI=1 and B component units/values unchanged.

The inspected26.10 ExternalFieldReader directly uses numeric spacing/offset.
The tested metadata-only change leaves the trajectory **byte-identical** to the
original. The adapter therefore requires explicit canonical SI coordinates and
components; it does not trust a metadata-only conversion in this reader path.

| Conditional numerical case | Outcome |
|---|---|
| Original metre-scale map,12.7085eV upstream test-particle momentum | Retained through132.3µs; axial momentum reverses |
| Same numeric mesh with only gridUnitSI changed | Identical trajectory in the tested WarpX path |
| Source-derived millimetre map, same particle momentum | Escapes near35ns; half-timestep escape brackets overlap |
| Original metre geometry, B disabled | Escapes, with no axial reversal |
|675keV sensitivity particle, original or millimetre map | Escapes in both geometries |

The source-map field at the initial point is about1.476mT. The local initial
perpendicular gyroradius estimate is about0.202m for the low-energy particle and
46.46m for the675keV sensitivity particle. A millimetre aperture cannot inherit
the metre-scale confinement interpretation. These are finite-time controls of a
weak upstream **example map**, not a test of the real STARS/PRISM magnet design.
The rectangular absorbing simulation bounds are not a recovered physical chamber.
The geometry-derived map has not been independently regenerated in FEMM or
validated against magnetic measurements. No local gyroradius estimate alone
establishes confinement; full trajectories are executed here.

## Other completed work

- Two byte-exact upstream1D Coulomb inputs and their unchanged analyses pass:
  corrected energy/momentum conservation and weighted-population relaxation.
  These are carbon12 numerical tests, not electron–proton–boron calibration.
  Relaxation's reference-temperature error is1.3213%, below its native2% tolerance.
  Conservation's relative energy residual is about-3.01e-11, within its native bound.
-17 source/field admission tests pass. Joint records, absolute physical weights,
  frames, SI units, source provenance, domain membership and snapshot clocks are
  explicit. A marginal energy spectrum cannot silently become a joint source.
- The adapter generates MultipleParticles input and executes it in WarpX. A
  weight7 verification particle follows the original weight1 trajectory within
  the stated numeric check, and weights scale exactly7× with no self-fields.
-15 field-control checks pass. All raw reduced traces from the seven map cases
  and weighted adapter case are archived. Independent isolated workflow replay
  reproduces all16 raw reduced diagnostic files byte-for-byte and the corrected
  map summary. Native collision analyses also pass in that replay.

## What remains missing

No complete measured STARS source distribution (joint energy, angle, position,
time, absolute per-shot count and uncertainties) or apparatus field map was
recovered by this bounded search. Existing Spraker data are **alpha spectra**;
EXFOR/Sikora are reaction observables, not a proton-beam source. ENN's energy
interval and a hollow-sphere cutoff are not complete source distributions.
Derived joint source hypotheses remain allowed, but must declare their coupling,
normalization and uncertainty assumptions rather than inherit calibrated status.
See APPARATUS_GAPS.json and SOURCE_RECOVERY.md.

## Reproduce in a new directory

Use the pinned WarpX environment from PR50 (environment_install.txt in its sibling
warpx_pb_kinetic_v0_1 release). Needs WarpX1D/3D, NumPy, SciPy, yt and openpmd-api.
No FEMM installation or h5py is needed to replay the supplied map controls.

```bash
python reproduce.py --runtime /absolute/path/wx-env --out /tmp/sf-source-field-new
```

The workflow copies this release's scripts/pinned text inputs to a new tree,
fetches the exact public CC0 HDF5 blob when uncached, derives explicit SI copies,
runs collisions/maps/adapter/analysis and17 tests. It never overwrites bundled
receipts. Original and derived HDF5/NPZ caches are regenerable, not bundled.
Source-index hashes and the original dataset Git blob are checked before use.
The map data values are checked bit-identical across spatial-unit transformations.

`diagnostics_reduced.tar.gz` contains the16 recorded raw map/adapter trace files.
Collision plotfiles are regenerable; their component hashes are retained.
`receipts/REPRODUCTION_CHECK.json` records the isolated replay.

Legacy root scripts retain the exact initial execution paths and outputs.
Use reproduce.py for a portable new run. Set STELLAR_WARPX_ENV explicitly if
running individual copied scripts. All case parameters and12.7eV/675keV particle
inputs are benchmark/sensitivity choices, not apparatus calibration data.
