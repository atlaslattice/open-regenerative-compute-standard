# Stars 2.0 v0.11 — Duration × Success Endpoint Gate

**October 28, 2026. NEW version, append-only. Toy pre-treatment model, NOT measured p–B11 performance.**

## Correct primary outcomes
The previous v0.9-v0.10 models emphasized laser geometric overlap and assumed absorbed optical energy. These are **mediators**, not the Stars success endpoint. The quantitative scientific scoreboard must report, from measured source-qualified data:

1. **Nuclear/particle success:** nuclear reaction count or rate per *measured incident proton distribution* and 11B areal inventory; transmitted proton spectrum; correlated born 3-alpha distributions; front/rear/side escaped alpha energy.
2. **Collector success:** *detector-qualified* alpha counts and energies, collector accepted alpha kinetic energy, gross measured electrical output at load, all uncertainties and detector/collector transfer functions.
3. **Operational success:** unbiased all-attempted-shot qualified yield, stability/variance, target lifetime, cost per qualified shot, throughput, and wall-electric J spent per useful collector J.
4. **Net success:** all-input, facility-boundary net electric energy (including laser, acoustic, EM coils, thermal loads, replacement, standby). Never declare net gain from optical absorption.

Success defined in the Stars 2.0 v0.9 paper as qualified collector-accepted energy per all-shot facility cost, alongside full physical and wall-plug ledgers. Comparing OFF/SHAM/ON must not condition on post-treatment mediators when estimating the total causal effect.

## Model actually executed
Sweep 0.1, 0.25, 1, 2, 5, 10, 25, 50, 100 milliseconds of acoustic actuation, separately:
- PRE_ONLY, with a fixed two-millisecond off period before the laser.
- PRE_PLUS_SUSTAIN, with continuous actuation up to the shot.

Envelope: `da/dt=(1-a)/1 ms` when driven, `da/dt=-500 a/s` when off. **Hypothetical, uncalibrated** slow-history state: `dm/dt=(a²-m)/5 ms`. Cycle-integrated `∫a² dt` is an exposure proxy, not thermal energy or damage. Compare duration, residual amplitude, modeled history and exposure. All fusion success fields remain NOT_MODELED. No optical output treated as success. This demonstrates why a duration-dependent experiment is meaningful, **not** that long preparation improves reactions.

## Interpretation and negative controls
A long treatment approaches the imposed steady-history state; the model *cannot* establish that this variable physically exists in a boron-rich catcher, whether it benefits fusion, or that more exposure is safe. Under the **zero-memory physical null**, the history variable has no effect on particle/collector outcomes. Excess input energy, heating, erosion, plasma disruption or target deformation may overwhelm any benefit. Equal-energy and equal-temperature controls are necessary in addition to identical-duration controls, and a longer ON history without a measured change in target state does not justify a yield bonus.

## Proposed preregistered multiarm experiment
OFF, hardware-matched SHAM, PRE_ONLY, SUSTAIN_ONLY, PRE_PLUS_SUSTAIN, and time/phase-scrambled controls. Block by target batch, beam energy/angle, fluence and detector run; independently measure target temperature, areal density, morphology, vibration/displacement, laser spot/shot timing, transmitted proton spectrum and alpha spectra. Predeclare primary endpoint: **collector-accepted alpha energy per attempted shot**, conditional only on preregistered detector quality criteria; include all shots in cost and wall-plug denominators. Secondary endpoint: fusion reaction estimate normalized by incident proton and 11B atom inventory. Do not infer reaction count from gamma/alpha counts without calibrated backgrounds and forward model.

## Stopping gate
A physically predictive proton–boron success simulation awaits measured energy-angle proton distributions, source-qualified reaction cross sections/branches, target stopping/straggling and stack geometry, calibrated detector acceptance and complete EM field geometry. A simulation that simply maps higher pretreatment time to higher yield would be circular. Frozen G0-B predictions remain on hold.

## Run receipts
- 18 duration-arm rows; 21 checks passed.