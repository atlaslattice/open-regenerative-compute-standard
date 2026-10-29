# Stars 2.0 v0.12 — 10-second acoustic pre-treatment extension
**2026-10-28 · APPEND-ONLY · NO fusion gain claim**

This re-evaluates the v0.11 *uncalibrated* duration-history oscillator at **10 seconds (10,000 milliseconds)**, in both schedules: PRE_ONLY (drive ends 2 ms before laser) and PRE_PLUS_SUSTAIN (drive continues until the laser shot). The entire earlier sweep is retained, with new logarithmically spaced durations from 0.25 to 10 seconds.

## Actual computation
Original illustrative equations: ON `da/dt=(1-a)/(0.001 s)`; OFF `da/dt=-500a/s`. Toy memory `dm/dt=(a²-m)/(0.005 s)`; accumulated exposure `∫a²dt`. This version uses analytic amplitude/exposure and accurate quadrature for memory, avoiding millions of small numerical timesteps at 10 seconds. The assumed memory has an artificial **5 ms** time constant; therefore it is expected to saturate far earlier than 10 seconds. No real BN memory or material saturation measurement is implied.

## Ten-second numerical results
- PRE_ONLY: envelope at laser 0.367879441; history proxy 0.804066237; exposure 9.9985000 s.
- PRE_PLUS_SUSTAIN: envelope at laser 1.000000000; history proxy 1.000000000; exposure 9.9985000 s.

## How to interpret
- A target exposed for 10 seconds has much more **modeled cumulative acoustic exposure** than one exposed for 100 milliseconds, but does not show a corresponding increase in the saturated history variable under the fixed 5-ms-memory assumption.
- The exposure integral is not a watt-hour, absorbed energy, thermal dose or damage estimate. No actuator power, acoustic coupling efficiency, heat transport, fatigue or materials data were provided.
- This does **not** prove that long treatment has no physical benefit; a real target may possess much slower processes (thermal diffusion, microstructure, flow, relaxation), but none is calibrated here. Longer treatment could instead damage or heat the target.
- **Fusion reaction probability, alpha yield and net power are intentionally NOT MODELED.** The success endpoint remains reactions per incident proton (with source distribution and boron areal inventory), with qualified alpha output and all-attempted-shot operations tracked separately. No arbitrary positive effect of 10 s has been inserted.
- No ability to distinguish 'acoustic memory' from ordinary vibration ringdown from these equations. Test against a zero-memory null and real target-state measurements.

## Scientific follow-up
Model target state using actual relevant time constants, elastic/thermal modes, measured density/porosity, support boundary conditions and laser timing; then pass measured effects through source-qualified proton stopping, energy-dependent p–B11 cross sections and detector-forward models. Include 0/0.1/1/10 s treatment, both pre-only and sustained plus OFF/SHAM, under equal-temperature/equal-energy controls.

## Reproduction and provenance
New v0.12 only. Prior v0.11 outputs untouched; reference rows were cross-checked against the original numerical Euler scheme. Source code + CSV + plots + SHA-256 manifest included.