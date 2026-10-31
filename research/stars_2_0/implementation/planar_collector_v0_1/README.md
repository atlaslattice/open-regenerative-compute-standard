# Stellar Forge — planar alpha-collector reference v0.1

2026-10-31. Additive continuation of draft PR58, parent `9299019cd7f78c0844b175594f2b46f1fe6523df`. No merge, relabeling of A/B/C, or scientific freeze. **Net wall-plug power remains unevaluated.**

## What ran

1. An analytic relativistic planar-retarder oracle with 13 unit/property tests, including 1000 seeded energy-budget cases, a deliberately wrong total-energy acceptance counterexample, negative-bias debit, reflection and marginal cases.
2. Actual WarpX prescribed-uniform-E nominal-alpha trajectories: normal incidence, grazing incidence, acceleration and zero-field controls. Normal/grazing cases repeat at half timestep. Six cases, 27 checks; a second execution reproduces scientific summaries and all 12 reduced trace files exactly. These are test-particle trajectories with deposition disabled and no Maxwell solve, not a self-consistent collector or new fusion calculation.
3. PR58's fixed correlated alpha bank and resolved finite-target exits connected to an ideal **rear-face-only** collector. Four aspect ratios, ten signed bias settings and a zero-charge force-null control; five source models retained. Two executions pass 91 checks each and reproduce exactly. The saved-result audit passes 910 checks (including repeated ledger checks); that count is numerical bookkeeping, not 910 independent validations.

## The acceptance condition

Let M be alpha rest energy, T its incoming kinetic energy, and mu its cosine to the outward normal of a planar retarding field. For a static planar potential, transverse momentum is conserved. Define

`p2 = T*(T+2*M)`

`m_perp = sqrt(M*M + p2*(1-mu*mu))`

`normal_available = p2*mu*mu / (M+T+m_perp)`.

The last expression is the rationalized form of `(M+T)-m_perp`. Collection requires `q*deltaV < normal_available`, not merely `q*deltaV < T`. MV times charge in elementary-charge units gives MeV. Equality within the stated numerical tolerance is marginal/deferred, never silently collected.

A transmitted particle transfers q*deltaV to the **ideal** circuit and deposits residual T-q*deltaV at the absorbing terminal. These are separate energy terms. A reflected particle temporarily transfers energy to the field on its outward leg, then receives it back on the return to its launch potential: net ideal circuit transfer is zero and return kinetic energy is retained. For accelerating negative bias, circuit transfer is negative and terminal heat increases accordingly. Startup, circuit leakage, space charge, electron dynamics and thermal conversion are not represented.

## Connected-control result

For the inherited exploratory coherent l1+l3 source at a common **1 MV numerical bias setting**, assuming nominal alpha mass and hypothetical +2e charge at exit:

| Target width/thickness | Resolved escaping energy (weighted MeV) | Ideal rear-port circuit transfer (weighted MeV) |
|---:|---:|---:|
| 2 | 0.1514654950 | 0.0107488877 |
| 10 | 0.1506061460 | 0.0108019001 |
| 100 | 0.1494157274 | 0.0108019001 |
| 1,000,000 | 0.1490032470 | 0.0108019001 |

The narrow control releases about 1.65% more total alpha kinetic energy than the slab limit, yet transfers about 0.49% less to this rear-only ideal collector. Side escapes bypass its port. This is a conditional illustration of acceptance/phase-space coupling, not a target recommendation, physical efficiency or demonstrated gain. Other collector arrangements could behave differently.

A deliberate mutation accepting particles on total energy alone would overcredit the wide-box 1 MV case by about 3.48x relative to the correct ideal planar test. This is a constructed wrong-model control, **not a claim that a historical Stars implementation made that error**. INTERPRETATION.json records the comparison. Voltage settings (-0.25, 0, 0.1, 0.25, 0.5, 1, 1.5, 2, 3, 5 MV) are verification/sensitivity controls, not calibrated hardware settings or an optimized design. No physical uncertainty interval or best-source ranking is inferred.

## Complete conditional ledger

`alpha birth kinetic = material-transfer lower bound + unresolved upstream tail + ideal circuit transfer + ideal terminal heat + returned kinetic + bypass kinetic + marginal deferred kinetic`.

Particle weights are partitioned into collected, reflected, bypassed, unresolved and marginal. Every original expected reaction and all three-alpha event correlations remain fixed. Bypassed particles are outside this rear-only control; they are not asserted to be irretrievably lost in a real device. Finite-target unresolved alphas are not injected into the collector. The side/front/corner paths and unknown low-energy tail remain explicit. No arbitrary collection efficiency or nuclear multiplier is introduced.

The inherited source is still an uncalibrated isolated unpolarized 2-minus model extended over local receiving energies. Cold elemental-11B calculated stopping, positive-floor limitations and centroid-ray geometry remain unchanged. The original ceramic pocket, its backing and physical SI exits remain unresolved. The numerical charge-zero case is a force-off test at fixed nominal alpha mass, **not a modeled neutral-helium atom**. The +2e cases do not establish the charge-state distribution after a real solid target; charge exchange and electrons must be supplied separately.

## WarpX verification and preserved failure

The fixture uses a single nominal 3 MeV alpha, prescribed Ez=+/-1e8 V/m or zero, 0.5 ns duration, and 1 ps / 0.5 ps timesteps in a large nonintercepting domain. These values test the solver; they do not assert that this field or electrode environment is achievable. For uniform E, pz(t)=pz(0)+qEt and transverse momentum remains constant. Position is compared with the rationalized relativistic exact solution

`z(t) = c*c*t*(pz(t)+pz(0))/(Etotal(t)+Etotal(0))`.

Particle kinetic plus prescribed electrostatic potential energy is conserved to a maximum residual about 4.25e-11 MeV across these runs. The grazing trajectory reverses its normal momentum as expected. All macroparticle counts and weights remain one in all traces. Position errors refine with timestep.

The original `run_warpx.py` and warpx_run001 remain preserved: 26/27 gates passed; a grazing refinement gate failed because its analytic position oracle subtracted two large total energies. Separately named `run_warpx_v002.py` rationalizes that expression; the unchanged 27 gates pass in warpx_run002/003. No physics threshold was weakened and no original failure erased. At these small errors, stable oracle arithmetic matters.

The executed binary identifies WarpX/AMReX 26.10 in the installed runtime lineage; executable SHA256 is recorded in each result. The binary does not attest its exact source commit. Installation recipe/package receipts remain in the earlier WarpX release; no binary is redistributed here. External-field syntax was checked against the previously recovered official WarpX parameters source at commit `a389dc54a27136176bdd48f7bfd36da62a873a61`, `Docs/source/usage/parameters.rst`: [official pinned documentation source](https://github.com/BLAST-WarpX/warpx/blob/a389dc54a27136176bdd48f7bfd36da62a873a61/Docs/source/usage/parameters.rst). That documentation pin is not asserted to be the binary's source commit. Nominal alpha mass and exact SI conversion constants follow the inherited MASS_SOURCE.json/CODATA references; their physical uncertainties are not propagated.

## Reproduction

Preserve sibling implementation directories. Unpack PR57 source banks and PR58 result arrays using their own scripts. NumPy 2.3.5 / Python 3.12.14 were used for postprocessing. The saved audit needs NumPy and the archived traces; no WarpX execution or Coulomb library is needed. Full fixture regeneration requires the installed WarpX 3D binary.

```
python planar_collector_v0_1/unpack_traces.py
python planar_collector_v0_1/audit.py
python -m unittest discover -s planar_collector_v0_1 -v
python planar_collector_v0_1/run.py --models . --out planar_collector_v0_1/fresh_bank_run
python planar_collector_v0_1/run_warpx_v002.py --runtime restore_runtime/env --models . --out planar_collector_v0_1/fresh_warpx_run
```

Each output directory must be new. Dependencies and input banks are hash checked in the connected runner. The standalone WarpX fixture reads the sibling nominal mass file and records the binary/runner hashes; it does not invoke the source/target models. `audit.py` compares current saved traces and summaries without rewriting original runs. Raw traces and input/execution logs are archived losslessly; `unpack_traces.py` refuses replacements.

## Physical boundary before apparatus claims

The missing collector inputs are explicitly listed by apparatus_gate: actual target exits/space-time, post-material charge-state distribution, electrode geometry/apertures, a qualified E/B/sheath model, space-charge/electron/secondary-emission treatment, load circuit and startup/bias/leakage, material losses/thermal recovery, absolute shot normalization and complete facility inputs. Prescribed-field test particles verify a numerical limit; they do not resolve those coupled effects.

`apparatus_recovered_electricity_J`, `facility_net_electricity_J`, physical current, time and power remain null. No sustained-burn, acoustic-improvement or net-power claim is made. The next physical task is an explicitly versioned target/collector configuration with actual or clearly derived geometry, material and field inputs, preserving the unrecovered original-pocket identity.
