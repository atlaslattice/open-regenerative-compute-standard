# Stellar Forge — fresh source-to-facility integration v0.1

2026-11-01. Additive continuation of draft PR61, base `34c4a8c3f3994805958395a48787be9cda56f00c`. **Current entrypoints: pipeline_v004.py, run_v006.py, accounting_v004.py and PROFILE_v003.json. Current executed result: pipeline_run004.** Earlier iterations are preserved and superseded where identified below. No merge or scientific freeze.

One command now executes actual reference source PIC/target transport, correlated alpha generation, finite escape, ideal collection and facility accounting. This is an integrated conditional reference control, **not a spatially closed or calibrated physical apparatus**. Actual p–11B A/B/C net power remains unevaluated.

## What runs

The pipeline executes the archived source/target runner in WarpX, then the archived correlated-alpha producer, then the new integration runner with those FRESH receiver and event-bank outputs. The integration checks the producer/receiver hashes and rejects a collector setting without its registered comparison. It does not merely concatenate saved summaries.

The canonical source-derived magnetic map is the previous numerical interpretation of the public FEMM dataset, not an actual STARS magnet map. Source cohorts, target column, relative finite-box geometry, hypothetical charge state and collector bias remain numerical/exploratory controls. No input is relabeled as a laboratory observation.

PROFILE_v003.json has a separate control ID under C's reference family. It does not replace original C or the unrecovered pocket and does not inherit A/B hybrid performance. MODULE_RETENTION.json preserves all 26 original C inventory entries and the A additions; availability does not mean every alternative is installed or every coupling is implemented. See APPARATUS_SPEC_AUDIT.md.

## Energy result and boundary correction

For this single-pass cold-target control, proton kinetic input is 23625 weighted MeV and modeled primary-channel nuclear release is 0.141354941 weighted MeV: about **5.983 ppm** of the input beam energy. This is a conditional model ratio, not a measured source or plant efficiency. Common normalization changes do not improve the ratio within this assumed linear control. Different reaction probabilities, material/plasma states, recirculation or sustained burn need different physical calculations.

An important correction is preserved in BOUNDARY_CORRECTION.md. The initial expression `B+Q-B/eta` excludes electrical recovery of source-conversion losses; it is NOT a universal whole-facility bound.

With source kinetic energy B, gross source efficiency eta, modeled nuclear release Q, source-conversion remainder L=B/eta-B and electrical recovery fraction r_s, a perfect downstream recovery scenario gives:

`net = Q - (1-r_s)*B*(1/eta-1) - net_auxiliary_draw`.

If r_s=0, zero auxiliary draw and cyclic storage, positive net requires eta greater than approximately **99.9994%** for this control. This threshold is scoped to source losses receiving no electrical credit. If r_s=1 and every other input loss is also returned as electricity, the energy-only net upper envelope is Q. That perfect-recovery limit does NOT establish thermal/exergy feasibility. Source/auxiliary remainders are not automatically heat or electricity, and their actual electrical recoverability is unknown.

At the selected finite aspect=2, bias=1MV coherent-source control, ideal alpha circuit transfer is 0.0107488877 weighted MeV. Direct alpha collection alone cannot repay this control's source-beam energy even with ideal source-loss recovery. Other beam-energy recovery, changed reaction probability, or different physics must be explicitly modeled rather than silently credited.

The efficiency probes1/0.5/0.1 evaluate equations; they are not device estimates. The bound also assumes no unmodeled nuclear/chemical/external energy source and no stored-energy depletion. No new confidence interval or experimental p–11B performance estimate is inferred. The separate TMX benchmark's efficiency is not applied to STARS.

## Current facility accounting

The interface separates:

- gross wall-to-beam efficiency, alternatively a wall-to-laser × laser-to-beam chain;
- downstream ideal alpha circuit work, other alpha energy and non-alpha beam/target energy;
- source-conversion remainder and its own electrical recovery;
- source idle/preparation wall draw per attempted preparation and its own recovery;
- each auxiliary's per-attempt/per-fired wall draw and recovery of its OWN input energy;
- attempt/firing rate and cycle energy inventories.

These energy partitions are disjoint: source-loss recovery excludes energy already passed into the beam; auxiliary-own-input recovery cannot re-credit beam/alpha heat. Supplying both source-efficiency routes or duplicate physical hardware IDs is rejected. The source driver cannot be billed again as an auxiliary; its idle/preparation draw has a separate explicit field. Efficiencies here are gross, before recovery credits, to avoid double counting.

All real facility inputs in the default current profile remain unknown—**30 unresolved scalar fields**—rather than silently becoming zero or100%. Unknown rates prevent power inference; negative outcomes are preserved. Strict steady storage-neutral power needs a supplied zero inventory change. Noncyclic storage requires a qualified flow adapter; a formal inventory correction is exposed separately without promoting it to a valid steady result.

Preparation costs apply to all attempts, including nonfiring attempts. Firing fraction changes throughput/cost amortization, not this fixed per-fired reaction bank. Actual fired-shot inputs must represent misfires/known zeros and source variability appropriately. Acoustic-induced changes in overlap, jitter or target/source state require a new physical source/transport calculation; diagnostic qualification does not create a nuclear multiplier. An unmodeled acoustic effect is not a calibrated zero effect.

## Verification and preserved history

A pinned Git snapshot and266 critical files were restored and hash verified. The WarpX/AMReX26.10 runtime was restored; six fresh prescribed-E trajectory controls pass27 checks. The pinned Michel CPC backend was rebuilt with source/compiler receipts. No compiled binary or downloaded source archive is redistributed.

The fresh source/target stage passes25 checks and19 original bridge tests. The fresh4096-proposal alpha stage passes30 checks. The integrated stage passes21 checks. Source/target scientific results, alpha scientific values excluding elapsed runtime, and alpha bank bytes match the archived references. REPLAY_VERIFICATION.json verifies these statements for each saved pipeline execution.

Thirty-one unit tests cover energy boundaries, signed source/cost accounting, source/auxiliary loss recovery, idle costs, missingness, storage, source alternatives and comparator rejection. Current saved-output audit checks27 conditions. Initial75/94-check audits are historical numerical audits, not validation of the initial overbroad boundary interpretation. The current package was also extracted and audited separately.

Initial code/profiles/runs are retained. Read BOUNDARY_CORRECTION.md first when inspecting historical run001–003 and pipeline_run001–003: older bounds need the stated restricted boundary, and source idle draw became explicit in current pipeline_run004. Those historical facility inputs stayed unknown and no actual apparatus gain was reported. Particle/source/target physics is unchanged by the accounting refinements.

## Run the current chain

Keep prior implementation versions as siblings. The full pipeline uses Python3.12.14/NumPy2.3.5, inherited SciPy1.17.0, system GSL for angular coefficients, the compiled Michel CPC backend and WarpX26.10. See `coherent_source_v0_8/prepare_cpc.py` and `warpx_pb_kinetic_v0_1/environment_install.txt`. Copies of `warpx_source_field_v0_1/fetch_dataset.py` and `prepare_maps.py` build the source-derived map in a fresh folder, using the runtime's openPMD Python package. Installation/build receipts are included; do not overwrite earlier receipt folders.

From the repository root, restore the archived replay inputs and execute:

```
python research/stars_2_0/implementation/alpha_birth_escape_v0_1/unpack_banks.py
python research/stars_2_0/implementation/finite_alpha_transport_v0_1/unpack_arrays.py
python research/stars_2_0/implementation/facility_integration_v0_1/pipeline_v004.py --models research/stars_2_0/implementation --runtime /path/to/warpx/environment --map /path/to/canonical_mm.h5 --profile research/stars_2_0/implementation/facility_integration_v0_1/PROFILE_v003.json --out new_full_run
```

For a numerical-layer replay without a new PIC/backend execution:

```
python research/stars_2_0/implementation/facility_integration_v0_1/run_v006.py --models research/stars_2_0/implementation --profile research/stars_2_0/implementation/facility_integration_v0_1/PROFILE_v003.json --out new_integration_run
python -m unittest discover -s research/stars_2_0/implementation/facility_integration_v0_1 -v
python research/stars_2_0/implementation/facility_integration_v0_1/unpack_current.py
python research/stars_2_0/implementation/facility_integration_v0_1/audit_current.py
```

Every output directory must be new. Current replay arrays/traces are in replay_arrays_and_traces_current.tar.xz; earlier archives are retained. Fresh alpha banks identical to PR57 are referenced by hash instead of copied. The generated numeric outputs are simulations; reproducibility is not experimental validation. No isotope revenue or cost offset is converted into energy. DECISION_MEMO.md identifies the next physical work; the definitive apparatus contract remains unfrozen.
