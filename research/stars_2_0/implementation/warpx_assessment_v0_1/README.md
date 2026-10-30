# Stellar Forge — WarpX qualification assessment v0.1

2026-10-30. Upstream pinned at `BLAST-WarpX/warpx` commit **a389dc54a27136176bdd48f7bfd36da62a873a61**. This assessment identifies reusable capabilities and executes a scalar cross-section audit. It does **not** build/run the full WarpX PIC application, reproduce Schramm's simulation, validate ignition or replace any Stars reference result.

## Finding

WarpX is directly relevant to the next Stellar Forge layer. The inspected source already contains **p–¹¹B nuclear fusion, sequential three-alpha product initialization, pairwise Coulomb collisions, bremsstrahlung, external fields and particle-boundary diagnostics**. Its p–B implementation has dedicated 2D and 3D reaction tests. Use it as a named kinetic backend behind the shared particle/energy interface, with the existing lightweight models retained as independent controls.

This is a stronger lead than merely locating a generic PIC framework. In particular, the native p–B cross-section model explicitly includes the narrow **148 keV center-of-mass resonance** missing from the earlier Sikora-based handoff interpolation. A candidate publication model is now available for that region. Numerical source availability is not apparatus calibration, and the fit's experimental uncertainties have not been recovered or propagated in this assessment.

## Verified source facts

| Capability | Inspected primary source | Qualification |
|---|---|---|
| Reuse terms | vendor/LICENSE.txt | BSD-3-Clause-LBNL-style license permits source/binary redistribution under its conditions. Retain copyright, conditions, disclaimers and endorsement restrictions. GitHub API metadata returned NOASSERTION; the actual license text was read. |
| p–B event cross section | ProtonBoronFusionCrossSection.H | Tentori–Belloni 2023 analytical fit through 9.76 MeV CM; separate modified Buck high-energy power-law branch |
| Alpha initialization | ProtonBoronFusionInitializeMomentum.H | Sequential alpha + excited Be8, then Be8 decay into two alphas; second breakup is isotropic. This is not automatically our coherent l=1/l=3 source model. |
| Conservation/weights | analysis_proton_boron_fusion.py | Checks physical weighted proton/boron consumption, alpha creation, charge, momentum and energy. Six alpha **macroparticles** per sampled reaction representation do not mean six physical alphas. |
| Coulomb and stopping | Docs/source/usage/parameters.rst | Pairwise kinetic collisions and fixed-background stopping are distinct models with applicability assumptions |
| Radiation | BremsstrahlungFunc.H/.cpp; analysis_collision_1d_Bremsstrahlung.py | Explicit photon-production implementation and a regression test. The inspected benchmark uses 1 MeV electrons; it does not independently validate radiation physics at every proposed keV plasma state. |
| Fields and boundary outputs | Repository tree and parameters documentation | Candidate mechanisms for the finite-orbit and injection/exhaust adapters; no Stars geometry or boundary implementation has been run here |

All primary file URLs and inspected text hashes are recorded in SOURCE_INDEX.json. The copied cross-section/constants/license files are preserved verbatim under vendor with their original notices. The two harness_include files are explicitly **our test shims**, not AMReX source or a replacement for its numerical implementation.

## Executed scalar audit

`kernel_probe.cpp` compiles the unchanged upstream cross-section header and original WarpX constants using g++ 13.3.0, double precision and minimal CPU/type/integer-power shims. It has no particles, mesh, fields, plasma evolution, Monte Carlo collisions or GPU execution. `fit_candidate.py` is a separate Python transcription of the formulas, retaining their attribution and license reference.

```bash
python run_kernel_audit.py --out /tmp/stellar-warpx-kernel-001
```

Requires Python 3.12 and a C++20-capable g++; no third-party Python packages. Output directory must be new. The run compiles the probe, checks 315 energies including fit boundaries and the explicit high-energy tail, verifies nine invalid-input/domain guards, and writes a frame-conversion table and receipt. The Python entry point rejects energies beyond the Tentori branch unless the caller explicitly opts into the high-energy model tail. This guard does not assert a calibrated upper range for that tail.

Recorded result: **315 C++/Python comparisons pass**, maximum relative difference **5.66×10⁻¹⁴**. This checks numerical transcription, units and wrappers, not the physical fit's accuracy. The low-resonance scan, using a 0.01 keV CM grid, peaks near **148.10 keV CM**, with candidate cross section approximately **0.10325 barn**. Grid-search precision is numerical resolution, not experimental energy or cross-section uncertainty.

For a stationary B11 target, the relativistic invariant conversion gives:

| Proton LAB energy | Pair CM kinetic energy | Candidate event cross section |
|---:|---:|---:|
| 162 keV | 148.416 keV | 0.101606 barn |
| 200 keV | 183.230 keV | 0.022148 barn |
| 675 keV | 618.389 keV | 1.400379 barn |

The original conditional handoff interpolation gives 1.319721 barn at 675 keV LAB. Their approximately **6.11% difference is a model comparison**, not a confidence interval or proof that either source is wrong. Both numerical values remain preserved. For ENN plasma conditions, relative velocities of both species are required; the stationary-target conversion alone is insufficient.

## Critical upstream-test limitations

The supplied `inputs_test_3d_proton_boron_fusion` sets **max_step=1**, periodic field boundaries and `do_not_push=1`, `do_not_deposit=1` for its species. It intentionally tests the fusion operator under constructed populations. Its extreme event-multiplier values improve numerical sampling by reducing product weights; they are not physical yield enhancements. One test deliberately sets an excessive probability threshold to demonstrate underestimation. Reproduce these tests with their existing analysis before changing them, and never report their raw macro-counts as reactor output.

Consequently, passing that test would establish operator behavior within its numerical setup, not mirror capture, a persistent nonthermal population, electron cooling, ignition or useful recovered energy. A confinement test must actually evolve particles/fields and enable the intended collision/radiation processes explicitly.

The product model's fixed Q is 5.55610759 + 3.12600414 = **8.68211173 MeV**. The earlier Stars mass-derived nominal Q is **8.68255915 MeV**. Their roughly **0.447 keV** difference must be retained as a mass/convention reconciliation item. Do not mix source-specific masses, Q and outgoing product kinematics while claiming exact conservation under one common convention.

## Proposed backend qualification sequence

1. **Source and scalar kernel — completed here.** Pin commit/license, preserve original code, establish energy-frame and cross-section-unit agreement.
2. **Full upstream p–B regression — pending.** Build the selected double-precision WarpX executable and run its existing 2D/3D test plus upstream analysis. Record AMReX/PICSAR/submodule versions, build flags, compiler/MPI, seeds, macroparticle weights and output checksums. Do not claim our scalar harness completed this gate.
3. **Finite single-particle fields — pending.** Benchmark gyro motion, prescribed work, adiabatic limits, aperture losses and finite-boundary escape against independent solutions and the PR44 ledger. Track source work and collected charge/energy.
4. **Multi-species collisions and radiation — pending.** Reproduce upstream relaxation/conservation and radiation tests; then qualify parameter ranges and resolution for actual electrons, protons and boron. Keep external cooling and drive power explicit.
5. **Stellar Forge handoff adapter — pending.** Import/export positions, times, species, weights and momenta/energies with explicit units and frames. Weighted sums, not raw macroparticle counts, drive the event and energy ledger. Pin the momenta convention: WarpX components may store gamma*v rather than velocity or SI momentum depending on the interface.
6. **Local apparatus experiments — pending.** A: qualify hollow-source/ENN-informed preparation/PRISM injection interfaces. B: connect the selected STARS stages and alpha-management branches. C: preserve original controls and add explicitly named backend comparisons. Retain alternative source/collision models and all negative outcomes.

Use explicit region/physics ownership. A PIC collision model for a plasma region and a cold-solid stopping model must not both debit the same energy loss over the same path. Transfer a particle once across a domain boundary; do not leave a counted copy active in both solvers. Resolve overlapping radiation, reaction and product-generation processes similarly.

Acoustic preparation belongs to the slower mechanical/target/readiness model. Transfer measured or derived target-state/geometry snapshots into the fast PIC experiment; do not presume that simulating a ten-second preparation at an electron-scale timestep is necessary or computationally practical. Full 3D density, Debye-length, gyro/plasma-frequency and boundary requirements need a feasibility study before selecting a production mesh or solver.

## Integration decision

**Adopt WarpX for a scoped qualification track and independent kinetic comparisons.** The direct p–B support can materially reduce implementation work and narrow the low-energy **model-coverage** gap. Keep the coherent exclusive-source, cold-material transport, detector calibration, acoustic readiness, collector response, facility power, uncertainty and economic modules as separately qualified components. No native WarpX capability alone closes those apparatus-specific questions or establishes net positive output.
