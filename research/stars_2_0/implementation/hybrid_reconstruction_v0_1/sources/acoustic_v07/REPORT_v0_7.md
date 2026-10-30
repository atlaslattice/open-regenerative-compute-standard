# STARS 2.0 G1/G2 — Spherical Geometry A/B v0.7

**2026-10-28 · simulation / exploratory geometry-only · no fusion prediction**

## Aim and model choice
This append-only continuation asks whether a spherical cavity can preserve a modelled intentional acoustic response under an assumed −80 dB ambient-vibration isolation path, and whether a spherical electromagnetic boundary is crossed by idealized protons and alpha particles. It does NOT model an actual STARS vacuum chamber, solid BN catcher, magnetic-mirror coil system, electrostatic confinement, nuclear reactions, space charge, alpha-born angular correlations, laser dynamics, acoustic-to-fusion coupling, or electric output.

**Explicit arbitrary illustrative geometry:** cavity radius R = 0.30 m. One *fluid-filled rigid spherical cavity*, uniform sound speed 343 m/s, scalar pressure wave equation, rigid-wall Neumann boundary and assumed radial-mode damping ratio ζ=0.05. This is a mathematical reference problem, NOT a propagation model for sound across vacuum, nor a structural eigenmode solution for a solid boron-nitride shell. Real STARS acoustic actuation would travel through supports / target solids and require actual elasticity and boundary conditions.

## 1. Acoustic eigenmodes
For radial symmetry ℓ=0 with pressure p(r) ~ j₀(kr)=sin(kr)/(kr), rigid wall ∂p/∂r=0 yields roots tan(x)=x, x=kR. The first four NONZERO radial-mode frequencies for the example sphere:

| Radial mode | root x | frequency (Hz) |
|---:|---:|---:|
| 1 | 4.493409458 | 817.652920 |
| 2 | 7.725251837 | 1,405.742072 |
| 3 | 10.904121659 | 1,984.191959 |
| 4 | 14.066193913 | 2,559.585240 |

**Not the complete 3-D acoustic spectrum:** angular modes ℓ>0 exist and some have lower frequencies than the first ℓ=0 mode. A uniform-pressure zero eigenmode also exists. The four-mode display is explicitly the radial subfamily.

For illustrative single-mode response H(f) = 1/sqrt[(1−(f/f₁)²)²+(2ζ f/f₁)²], the gain at resonance is 1/(2ζ)=10. All "drive pressure" numbers below are *generalized center-modal pressure-amplitude inputs*, not a physical sound source boundary force or empirically calculated acoustic displacement.

## 2. Four-arm mechanical comparison
Assumptions: 1.00 Pa generalized modal disturbance entering from outside; isolated external transfer = 10^(−80/20) = 10^-4; internal modal drive 0.05 Pa OFF/ON, unaffected by isolation. Separate, uncorrelated modes for illustrative amplitude combination. Frequency f₁ = 817.6529 Hz.

| Arm | External pressure at center | Internal pressure at center | Static B |
|---|---:|---:|---:|
| A: unisolated, drive OFF | 10 Pa | 0 | 0 |
| B: isolated, OFF | 0.001 Pa | 0 | 0 |
| C: isolated, ON | 0.001 Pa | 0.500 Pa | 0 |
| D: isolated, ON, B=3T | 0.001 Pa | 0.500 Pa | 3 T |

**Interpretation:** amplitude differences follow directly from the assumed transfer and linear drive; no real −80 dB acoustic isolation hardware is modeled or demonstrated. Pressure is not stress or strain of BN, and has no computed nuclear influence. Magnetic field has zero effect on this *deliberately uncoupled* scalar fluid model.

## 3. Spherical particle-boundary test
Place a single proton (675 keV kinetic energy) or representative alpha (2.893 MeV) at the sphere center. Uniform static B along z; no E, no collisions, no gradients, no relativistic correction (v ≈ 0.04c), no collective self-fields. Particle velocity pitches are measured **from the B axis**, not from the plane.

Analytical helical paths: x=(v_perp/ω)sin(ωt); y=(v_perp/ω)(1−cosωt); z=v_parallel t, ω=qB/m. First spherical boundary when x²+y²+z²=R². B=0 straight line first-hit times are about 26.38 ns proton and 25.40 ns alpha.

| Species | B | 30° first wall hit | 60° first wall hit | 90° first wall hit |
|---|---:|---:|---:|---|
| p | 1 T | 28.10 ns | 40.65 ns | none within 3 μs |
| p | 3 T | 30.23 ns | 51.62 ns | none within 3 μs |
| alpha | 1 T | 25.80 ns | 26.75 ns | 27.34 ns |
| alpha | 3 T | 28.47 ns | 49.70 ns | none within 3 μs |

At 3 T and pitch=90°, proton gyro radius 0.03957 m and alpha radius 0.08164 m, giving 2r maxima less than R. In this ideal infinite uniform field, their exactly transverse trajectories remain bounded radially; this is **not** finite-real-world confinement. At oblique pitch, z-motion enables rapid escape because uniform B has no axial reflection. Real confinement needs designed topology and loss budgets, not just a spherical wall.

## 4. What this run establishes
- Numerical implementation of analytical radial spherical j₀ modes with Neumann roots.
- Arithmetic of −80 dB exterior-only attenuation for a SINGLE specified frequency and idealized separation of disturbance/actuation paths.
- Comparison of ideal 0T/1T/3T charged test-particle trajectories against a *spherical* collision boundary, including axial escape.
- **13/13 deterministic numerical consistency checks pass**, including root identities, modal gain, isolation ratio, zero-B trajectory, and existence of oblique escape at 3T. These are implementation checks, not validation of a reactor.

## 5. What it does NOT establish
- Mechanical standing waves in an evacuated sphere (impossible through vacuum itself); elasticity of an actual BN target or support; real shock/plasma/ion-acoustic coupling.
- Spherical electromagnetic containment, electrostatic trapping, plasma stability, recirculated reactions or long dwell time.
- Proton–boron nuclear yield, isotopic resonance gain, alpha collection or net electric energy.
- Real acoustic isolation at −80 dB across a frequency band; transfer must be independently measured.

## 6. Next physical gates
1. Identify actual spherical **reaction location** (center, catcher surface or finite spherical target) and solid target/support stack; preserve these as alternative configurations until fixed.
2. Replace scalar fluid cavity with solid elastodynamic FEM / verified material properties; obtain a frequency-dependent external-to-target isolation transfer function and internal actuator-to-target transfer function, plus measured phase and losses.
3. Specify coils and electrostatic fields, calculate finite 3-D E/B fields and trajectory/space-charge/escape effects; test analytic conservation against independent numerical integrators.
4. Reuse G0-B isotope, energy-frame, stopping/straggling, correlated event, detector-forward and collector-gate standards from Stars v0.9. Do not freeze blind nuclear predictions without approved verification contract.
5. Preserve four-arm REFERENCE/OFF/SHAM/ON experiment for causal claims, with real electrical/thermal/EMP parity. Our A/B/C/D subsystems here are NOT replacements for that sham-controlled nuclear experimental design.

## Sources / related research
- STARS v0.9, 2026-10-27: https://github.com/atlaslattice/open-regenerative-compute-standard/blob/main/research/stars_2_0/whitepapers/STARS_2_0_v0_9_PRE_SIMULATION_MULTI_AGENT_SYNTHESIS_AND_HARMONIC_ANALYSIS_2026-10-27.md
- Earlier local independently simulated v0.6: /mnt/data/stars2_g1g2_coupled_v06/REPORT_v0_6.md
- Reproducibility: `run_spherical.py`, `numerical_receipt.json`, `arm_comparison.csv`, `particle_boundaries.csv`, figures, tests, SHA256 manifest.

**Wizards in the back, receipts in the front. No physics = no magic.**
