# STARS 2.0 — Integration-First Industrial Stack Simulation Policy
**Date:** 2026-10-29
**Status:** Project-lead methodological clarification; research design, NOT validated integrated device, simulation result, hardware claim, or G0-B prediction freeze.
**Related prior addendum:** [PRISM, Hollow-Sphere and Stacked-Hybrid Comparison](STARS_2_0_2026-10-29_PRISM_HOLLOW_SPHERE_MODULAR_ARCHITECTURE_ADDENDUM.md)
**Project:** Atlas Lattice / Stars 2.0

## 1. Correction to prior emphasis
The objective is **not** to default to the simplest possible isolated research apparatus, or to avoid simulated combinations merely because the source laboratories studied separate subsystems. The objective is to **explore and optimize an integrated, industrial-scale, multi-module physics apparatus using measured/qualified components where available**, and compare it with single-purpose laboratory reference configurations.

An integrated PRISM-like mirror, hollow-sphere laser accelerator/target, Stars pulsed proton pitcher, staged boron catchers, acoustic pretreatment and alpha energy management **should be simulated together as an exploratory configuration when plausible interfaces can be parameterized**. Physical incompatibility is an outcome to quantify, not a reason to suppress the scenario a priori. A fully combined configuration is a valid **POTENTIAL-DERIVED hypothesis**, not a laboratory-validated machine. Its performance must not be constructed by summing independent published percentage gains.

In particular, PRISM-like sustained magnetic confinement and pulsed laser-source/hollow-sphere devices have disparate operating regimes, so integration modeling must represent injection, duty cycle, plasma disturbance, phase space, timing, ash exhaust, power requirements and source/collector boundaries; simply spatially 'bolting' them together is not a meaningful physical model.

## 2. Architecture portfolio to implement
A0. Stars published stacked-hybrid baseline, reconstructed from latest actual apparatus and code (topology not yet locked by this addendum).
A1. Hollow-sphere pulsed laser target/source as an independently benchmarked reference (specific 2026-10-27 reported data HOLD pending original methods).
A2. PRISM-like multi-cell magnetic mirror as an independently benchmarked reference (company engineering design, not demonstrated plant).
A3. Stars + hollow-sphere source/target substitution.
A4. Stars + PRISM-like confinement/ash transport.
A5. Hollow sphere + PRISM-like plasma injection / transport (requires coupling model).
A6. **Full stacked industrial candidate:** all physically meaningful components plus explicitly modeled interface/adaptation subsystems.
A7. **Optimized industrial subset:** selection of modules from A6 using ablation, Pareto optimization and justified redundancy elimination.

No combination is implicitly endorsed as technically feasible or net-positive merely because it is present in the portfolio.

## 3. Modular interface contract
Every component declares:
- input/output particle species, charge, energy/angle/time phase-space distribution, emittance, density, temperature, flux and duty cycle;
- magnetic, electric, mechanical, thermal, vacuum/pressure, electromagnetic-pulse and physical-boundary requirements;
- applicable measurement domain and original source grade;
- interface-specific transfer matrix or physics solver, with reflection, stopping, scattering, heating, loss, contamination and downtime;
- power demand, auxiliary power and thermal handling, conversion losses and cost;
- error/uncertainty model plus couplings and covariances, rather than independent multiplicative confidence intervals.

When connecting modules, explicitly calculate matching/transport efficiencies and lost particles/energy. If a physically necessary adapter is undefined, report BLOCKED/UNRESOLVED for that integrated result; allow a parameterized potential-derived envelope separately and visibly.

## 4. Evidence and dual-track results
LAB-MEASURED = direct facility measurements with conditions, instrument/observable metadata and uncertainty.
VERIFIED-DERIVED = reproducible qualified calculations based on actual measurements **within supported domains**, not proof of untested integrated performance.
POTENTIAL-DERIVED = conditional cross-domain and industrial extrapolations with physical conservation, explicit interface assumptions, ranges, scenario flags, null/failure cases.
UNRESOLVED = missing/calibration-incompatible; no invented precise performance number.
Output side-by-side per subsystem and per whole architecture. Preserve original measured values, correlations, source hashes and extrapolation flags. A lab measurement of one component never validates a different laboratory's operating regime or their combined gain.

## 5. Optimization objective and ablation
Optimize **industrial-system output subject to physical constraints**, not maximum number of parts:
- useful fusion reactions and viable alpha energy per wall joule / per attempted shot / per operating hour;
- success rate and jitter; transport efficiency; material use, erosion, replacement/maintenance; power recirculation and operational availability;
- cost and industrial scalability, with CAPEX/OPEX assumptions labeled and no unsupported economic claims.
Compare A6 to A0–A5, then generate A7 by removing modules whose marginal contributions are negative or redundant. Evaluate interactions: two parts may each improve isolated performance yet reduce combined performance, or have genuinely synergistic gains. Report both synergy and adverse interference.
An architecture comparison across pulsed and continuous systems must normalize duty cycle, facility electricity, observation horizon, and experimental versus simulated input.

## 6. Required physical invariants
Reaction observables are typed; alpha production detector-window data are not automatically event cross sections. Track lab/CM frames, actual nuclear masses and three-alpha four-vectors.
A proton consumed in fusion cannot react again. Staged reaction probability is conditional on proton survival and evolved energy/angle; no duplicate reaction opportunities.
Every alpha's birth energy is partitioned among channeling to fuel ions, escaped/recovered electricity, deposited heat and loss; never recover and channel the same joule twice.
No magnetic confinement or hollow-sphere sheath effect is represented by an independent 'gain factor' unless its underlying physically consistent transport is modeled.
All pulsed-to-steady injection, ash removal, target destruction/refresh and heat removal must appear in the time-resolved flow and complete wall-plug ledger.
A zero-cross-section control must give zero fusion and Q energy while preserving nonfusion input/loss accounting.

## 7. Staged computational research plan
G0: recover source-verified newest apparatus configuration and code, and reproduce prior run receipts before topology changes.
G1: separate calibrated submodule models from EXFOR, diagnostic, material and geometry sources; verify measurements and observable types.
G2: implement modular interfaces and validate each against independent tests, including pulsed-to-mirror injection and collector energy partition.
G3: run A0–A7 full factorial/ablation scenarios, uncertainty propagation, sensitivity, Pareto front and adverse-interaction checks.
G4: expose side-by-side lab reference versus potential-derived industrial stack results (including blocked metrics and explicit nulls).
G5: only after outside experimental calibration and preregistered independent review, consider future verified whole-system predictions.
Maintain separate SHUGS operator research; no uncalibrated speculative operators in Stars physics.

## 8. Scientific question
**What would a physically constrained, integrated industrial p–11B system look like if complementary experimentally characterized subsystems were allowed to cooperate across historical laboratory boundaries—and which combinations actually survive complete conservation, compatibility, reliability and economic analysis?**

This is a systems-level extrapolative research question, not a claim that the integrated device has been fabricated or shown to produce net electric power.
