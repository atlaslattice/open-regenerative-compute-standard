# Stars 2.0 v0.10 — Acoustic pre-treatment vs sustained excitation at laser arrival

**2026-10-28 · Exploratory coupled timing surrogate · 15/15 checks · NO measured fusion increase.**

## Source context and reason for intervention
DeepSeek's Stars 2.0 review suggested acoustic target conditioning *before* the laser interaction; this v0.10 independently compares pre-treatment, late-start concurrent excitation, and combined continuously driven preparation. The prior v0.8-v0.9 phase-lock models used a single instantaneous acoustic displacement; they did not differentiate pre-shot target history.

## Physically distinct interventions
- **OFF**: no applied acoustic drive; source noise/laser jitter are paired across all scenarios.
- **SHAM**: numerically same as OFF; not a verified equal-heat/equal-EMP physical sham.
- **PRE_ONLY**: actuator ON from t=-10 to -2 ms; then OFF until t=0 laser arrival; free decay modeled.
- **SUSTAIN_ONLY**: actuator ON only from t=-0.25 ms until laser arrival; limited build-up time.
- **PRE_PLUS_SUSTAIN**: actuator ON continuously from t=-10 ms through laser arrival.
These schedules are illustrative test definitions, not a recommended experimental pulse protocol.

## Dynamical and optical model, with explicit unsupported links
Amplitude envelope a(t) obeys da/dt=(1-a)/1 ms (drive ON) or da/dt=-500 a /s (OFF). It modulates u=0.1 μm*a*cos(ωt+φ). A separate **hypothetical** slow preparation-memory proxy m(t) obeys dm/dt=(a²-m)/5 ms; it is not a measured permanent material transformation or microstructure law. Its influence χ on absorptance is explicitly optional and **unvalidated**.
Optical overlap G=exp[-2(x0-u)²/w²], x0=2 μm, w=5 μm, then hypothetical absorptance η=clip[0.30*(1+β(G/G0-1)+0.05χm),0,1] with β=0 or 1 and χ=0,0.5,1. Matched random laser-energy jitter 4%, phase jitter 10°, 2000 paired shots. No plasma model, cross section, stopping power, nuclear reaction, magnetic confinement, alpha collector or calibrated laser absorption is computed. The laser optical energy is set to 0.6 J; NO net-electric claim.

## Numerical state at laser arrival
| Arm | Acoustic envelope relative to nominal | Slow-memory proxy (dimensionless) |
|---|---:|---:|
| OFF | 0.000000 | 0.000000 |
| SHAM | 0.000000 | 0.000000 |
| PRE_ONLY | 0.367205 | 0.615880 |
| SUSTAIN_ONLY | 0.221173 | 0.000887 |
| PRE_PLUS_SUSTAIN | 0.998955 | 0.812298 |

## Optical absorbed-energy proxy at 0° phase
Compare as a sensitivity range, **not** as measured improvement. `β=0,χ=0` forces all modeled arms to the same output; `β=1,χ=0` exposes a geometry-only pathway; `β=1,χ=1` adds an imposed memory pathway.

| Arm | β=1,χ=0 mean J | β=1,χ=1 mean J | Difference vs OFF for β=1,χ=0 |
|---|---:|---:|---:|
| OFF | 0.17993817 | 0.17993817 | +0.0000% |
| PRE_ONLY | 0.18201449 | 0.18755551 | +1.1539% |
| SUSTAIN_ONLY | 0.18119046 | 0.18119844 | +0.6960% |
| PRE_PLUS_SUSTAIN | 0.18555187 | 0.19286005 | +3.1198% |


Universal no-coupling null mean absorbed energy: **0.17993817 J**, independent of acoustic schedule. Any better result when χ or β >0 is determined by assumed coefficients and does not validate the mechanism. Unlike earlier models, pre-treatment alone can leave a nonzero mechanical ringdown and a slowly relaxing history variable; that does not imply a real boron catcher exhibits preparation memory.

## Decision gates
1. Measure actual BN/boron target wave modes, mechanical damping and phononic isolation in the relevant structure, not in the fluid sphere surrogate.
2. Measure target surface/morphology/density/temperature at laser arrival after PRE_ONLY vs SUSTAIN_ONLY vs combined actuation. Fit a memory model only with experimental data; compare to zero-memory null.
3. Calibrate laser absorption and proton spectral distributions with actual diagnostics. Fit β and χ on training shots, predict withheld phase/schedule arms.
4. Real hardware SHAM must match electrical/thermal/EMP conditions; all shots and per-shot energy expense included.
5. For Stars fusion interpretation, only after calibrated proton source and target state should EXFOR nuclear cross sections, BN proton/alpha stopping, correlated 3-alpha event kinematics, detectors and collector acceptance be applied. No invented fusion multiplier.
6. Do not claim electromagnetic confinement is modeled here; integrate it as separate measured E/B field and loss topology later.

## Preservation
This is a NEW v0.10 local artifact. No v0.9/v0.8 files overwritten; no GitHub writes. Numerical checks are consistency checks, not empirical validation.
