# Unresolved physics and missing run artifacts — v0.1

These gaps do not remove modules from the research apparatus. Evidence-constrained performance remains unavailable where necessary inputs are absent; potential-derived envelopes may proceed with independently specified assumptions and sensitivities. An unimplemented effect is not a measured zero.

| ID | Open item | What closes or narrows it | Consequence if unresolved |
|---|---|---|---|
| R01 | Exact latest high-output full-hybrid run | Original entrypoint, config, data files, output tables/figures, receipt, seed and source commit/content hash | Cannot reproduce that reported run or identify its precise numerical drivers |
| R02 | Historical software environment | Original Python/dependency lock and launch logs | Current-environment reproduction only; original dependency identity unknown |
| P01 | Barrier parameter definition | Define V as actual potential energy or effective scaled parameter; provide B(s), potential(s), rotation/centrifugal profile and convention | Archived 2.535785× versus conditional 1.711366× illustrates material normalization sensitivity |
| P02 | Pitch-angle transport and confinement | Evolving injected phase space, loss-cone depletion/refilling, collisions, return time and independent orbit benchmarks | Per-pass isotropic hazard is an assumption; no measured confinement time |
| P03 | Hollow-sphere to mirror injection | Full proton energy-angle-position-time distribution, charge, electron content, emittance, acceptance, timing and interface fields | Neither 53 MeV cutoff nor scalar capture fraction defines the captured source |
| P04 | Catcher stages and recirculation | Stage-specific material/composition/density/state, stopping, scattering, paths, thermal damage and replacement | Effective pass count is not a model of traversing multiple solid catchers |
| P05 | Nuclear kernel energy coverage | Source-qualified cross sections and exclusive models across the actual relative-energy distribution; keep alpha-production/event semantics distinct | One low-energy resonance model cannot cover tens of MeV without extension |
| P06 | Acoustic readiness and firing probability | Target/source-specific time-series, OFF/sham/pre/sustain controls, physical success definition, attempted-shot denominators and grouped holdouts | Proxy absorption/history cannot determine productive shots or materialize nuclear gain |
| P07 | Combined shared fields and material state | Coupled external/self fields or justified reduced handoff; vacuum/solid/plasma stages, return-current effects, heating and EMP | Independently favorable component assumptions may not coexist; model adverse couplings explicitly |
| P08 | Alpha ash and plasma feedback | Species-resolved production, trajectories, slowing, dilution/space-charge effects and exhaust | Original alpha barrier changes only an escape proxy, not reaction counts |
| E01 | Usable alpha output | Event-correlated birth and escape distributions, acceptance, charge-state evolution, field work, collector IV/load and conversion losses | Q×events is not recovered electricity or full birth kinetic energy |
| E02 | Complete wall-plug energy | Laser/actuator/RF/NBI/magnet/pumping/cryogenic loads, storage changes, startup, duty cycle and losses | Neither net power nor grid supplementation needed to sustain operation is evaluated |
| E03 | Absolute industrial scaling | Shot/source normalization, repetition rate, replacement downtime, heat extraction, balance of plant and scale law | 525 MW cases are arithmetic assumptions rather than plant predictions |
| C01 | Capex and coproduct economics | Dated component costs, lifetime/maintenance, financing assumptions, collected isotope mass/purity, extraction cost and dated buyer-qualified prices | No realized product revenue or economic break-even claim |
| V01 | Source/detector validation | Full source/filter/TPS chain and condition-specific detector response, acceptance, raw/bin counts and uncertainty | Published curves or plausible spectra alone do not validate the assembled apparatus |

## Full-hybrid artifact recovery checklist

The missing execution package is specifically the run that couples the complete intended apparatus, rather than the recovered three-module mirror toy or the separate 525 MW arithmetic. Recover:

1. Its original run filename/entrypoint and source commit or byte hash.
2. Exact parameters/configuration, operating track and apparatus identity.
3. Source distributions and target/field/collector data with units and provenance.
4. Any seeds, event counts, particle weights and normalization constants.
5. Per-stage output tables, total energy ledger, all-attempt timing/failure records and figures.
6. Software lock/environment and launch log/receipt, or an explicit record that these were never captured.

None of these requirements implies that the reported simulation did not happen. If its artifact is unavailable, reconstruction must be newly named, retaining original recoverable components and distinguishing inferred interfaces from recovered ones.

## Next coupled milestone

Build a new append-only, weighted-particle source-to-catcher/mirror handoff. Record input/output species, phase space, reaction consumption, stopping, field work, time and energy destinations at every stage. First benchmark no fields, no reactions, zero capture, a single pass and analytically solvable adiabatic mirrors. Then add finite field maps, scattering, repeated encounters and alpha exhaust. Keep source-geometry alternatives and acoustic OFF/pre/sustain controls available; introduce readiness-to-source changes as explicit derived scenarios until calibrated. Report blocked absolute metrics alongside runnable conditional envelopes. This is an integration experiment, not a frozen design.
