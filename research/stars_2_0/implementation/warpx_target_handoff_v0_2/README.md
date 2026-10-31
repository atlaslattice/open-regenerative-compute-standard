# Stellar Forge — source/field/boundary/boron handoff v0.2

2026-10-31. Reconstructed and freshly executed after a workspace reset interrupted
publication of the earlier unpublished v0.1. Existing GitHub releases remain
unchanged. This is an executed **one-way numerical integration**, not a calibrated
laser/acoustic apparatus, ignition or net-power result.

## Executed chain

Joint weighted proton fixture → WarpX prescribed magnetic transport → particles
removed at domain faces → target-face routing → unchanged cold-elemental-B11
stopping/reaction model. Only target arrivals enter the receiving model; side and
upstream losses are separate sinks. No particle remains counted in both regions,
and fusion/stopping are not counted in both solvers over the same region.

| Verification result | Value |
|---|---:|
| Source physical proton weight |35,000 |
| Target-face arrival weight |10,000 |
| Other boundary losses |25,000 |
| Field-on expected reactions |0.01628033146 |
| Field-off expected reactions |0.01628032192 |
| Half PIC timestep |0.01628033151 |
| Coupled routing/conservation/control checks |25 passed |
| Bridge unit tests |19 passed |

The source comprises three675keV weighted cohorts, with deliberately selected
forward/oblique/backward directions. The receiver is a new verification plane at
z=3.5mm inside the separately derived millimetre interpretation of the public
FEMM example. Source, geometry,1e18B11 atoms/cm2 column,16 integration cells and
.04cm2 inventory area are **verification choices**, not apparatus measurements.
The area is inventory bookkeeping, not a measured beam footprint or local target
heating/depletion model. No physical capture fraction or useful enhancement is
inferred from these deliberately selected weights/directions.

Reaction-off retains stopping but produces no alphas. Zero column gives no
stopping or births. A narrow-aperture miss produces no target reactions. Known
zero source is an explicitly analytic zero-input control, not another PIC run;
missing source remains null/blocked. Simulated weighted expected reactions are
not observed counts or a physical shot-success probability.

## Surface and ledger semantics

The ordinary WarpX26.10 domain scraper copies a post-step state; its coordinates
may overshoot the face and deltaTimeScraped is zero. It differs from the embedded-
boundary intersection path. Raw positions, momentum, uint64 IDs as strings,
source-file hashes and timestamps are preserved. A final-drift projection gives
a **derived** surface estimate with a one-timestep time bracket and a conservative
magnetic direction-change bound. It is not an exact laboratory crossing state.
Ambiguous corners/duplicate IDs, near-aperture classification, unsupported clock
conventions and invalid units/states are rejected rather than silently resolved.

For the field-on target arrival the entry estimate is about107.760ps, bracketed
by107–108ps. The direction-change bound during that last1ps is about1.13e-6rad
for the weak example map. These are numerical-resolution quantities, not a full
physical uncertainty budget. The observed time record lacks a time-dimension
annotation in this build; seconds are established from the documented definition
and checked against step*dt.

Weighted total balances:

N_source = N_other_loss + N_reacted + N_post-target + N_PICremaining.

K_source + Q_nuclear = K_other_loss + K_post-target + K_alpha_birth
+ E_material_transfer + K_PICremaining + numerical_residual.

The current runs end with no active PIC particles. A nonzero remaining population
is rejected until its energy and phase space are exported explicitly. The internal
target handoff is counted once. All kinetic/Q/transfer quantities use weighted
MeV totals;1MeV=1.602176634e-13J. Maximum particle residual is about1.82e-12 weight;
combined energy residual about2.5e-9MeV, roughly1.1e-13 of the declared beam input.
Residuals remain visible and are not repaired with fictitious field work.

The receiving model retains its pinned SRIM13/ZBL stopping, publication-derived
event kernel and Q/mass convention. This does not transfer its cold-B11 model to
BN, B4C or hot plasma. PIC fusion is disabled here, so the receiver's products are
not duplicated by a different native Q/alpha convention. It produces alpha birth
count/total energy only. Slab-exit position/time, scattering and alpha phase space
remain unresolved; outgoing expected populations are **not reinjected** into PIC.
Stopping transfer and escaped proton energy are not automatically useful heat.
Alpha escape/detection/collection, physical shot success, wall input and net
electricity remain unresolved/null.

## Reproduce

Use the WarpX26.10 environment and source-derived canonical-mm map from PR50/PR53,
and the original particle_handoff_v0_1 directory with its14 locked dependencies.
The runner verifies the receiver and lock hashes, checks canonical SI XYZ map
units/coverage and creates a new output root. No solver patch or fork is used.

```bash
python run.py \
  --runtime /absolute/path/wx-env \
  --map /absolute/path/canonical_mm.h5 \
  --handoff-dir /absolute/path/particle_handoff_v0_1 \
  --out /tmp/sf-target-handoff-new
```

Python with SciPy is needed for the launcher; the solver environment includes
NumPy, SciPy and openpmd-api. Both recorded runs pass. Six raw reduced diagnostic
files reproduce byte-for-byte; all boundary particle fields and coupled event
counts/residuals reproduce exactly between these fresh runs. HDF5 metadata/file
hashes can differ. Raw HDF5 and reduced traces are in raw_diagnostics.tar.gz with
an extraction/hash-check helper. No multi-GB field files are needed for this case.

See RECOVERY.md for the interrupted unpublished version, REPLAY_CHECK.json for
fresh reproduction and HANDOFF.md for next steps. Do not claim byte recovery of
lost v0.1 files. No historical artifacts, A/B/C identities or BeyondQ reactor
assumptions are changed, and no scientific freeze or merge is authorized here.
