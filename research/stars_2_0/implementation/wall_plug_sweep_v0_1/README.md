# Stellar Forge wall-plug sweep v0.1

An additive accounting experiment based on the executed PR64 cold single-pass control, stacked after PR67. Current execution: **run002**. Earlier run001 is retained; its recovery-threshold field excluded containment costs and is superseded by run002's explicitly scoped threshold.

## Result and interpretation

There is no demonstrated slight net electrical gain. The inherited model releases5.983277924531208e-6 J of nuclear energy per1 J of incident proton kinetic energy. It does not establish electrical return of that1 J. Alpha birth energy also includes reacting-proton kinetic energy and must not all be called newly created nuclear energy.

The sweep uses the unchanged facility_integration_v0_1/accounting_v004.py, explicit optical-chain source cost, the saved coherent-control energy partition and the existing load registry. It does not rerun PIC, stopping, reaction rates or geometry. A linear normalization to1 J of beam preserves the archived model ratio; scaling to a dense real pulse without collective effects is unvalidated.

The current sweep has108 efficiency/recovery rows and36 operations/containment rows. All36 efficiency cases with source-conversion remainder receiving no electrical credit have negative net electricity, even with zero other loads and including perfect downstream recovery as the most favorable return. This is a finding about the supplied control/scenarios, not a general pB impossibility result.

| Conditional wall-to-laser | Conditional laser-to-proton | Optical J / beam J | Wall J / beam J |
|---:|---:|---:|---:|
| 1% | 10% | 10 | 1000 |
| 5% | 10% | 10 | 200 |
| 10% | 10% | 10 | 100 |
| 20% | 15% | 6.6667 | 33.3333 |

These are sensitivity scenarios, not observed STARS driver efficiencies. LLNL's>=10% wall-plug efficiency is an IFE development goal, not a measurement of our driver. The published15% laser-to-proton result is for5–30MeV protons using a specific double-pulse/thin-gold target; it does not calibrate our675keV control. Combining those efficiencies and the inherited source spectrum is a conditional cross-configuration estimate, not a self-consistent new laser simulation.

For the10%/10% scenario at1 attempted/fired shot per second and1 J beam per shot:

- Main laser wall draw:100 W; optical delivery:10 W; nuclear release:5.983 microW.
- Perfect electrical recovery of ALL downstream beam-plus-nuclear energy:1.000005983 W.
- Net, with no source-conversion-loss recovery and all auxiliary loads excluded:approximately-98.999994 W.
- A1kW continuous containment budget changes net to approximately-1098.999994 W. This1kW is a sensitivity budget, not a specified magnet.
- A separate500J optical laser-driven-coil pulse, with assumed10% electrical-to-optical efficiency, adds5000J wall input per fired shot. At1Hz, net is approximately-5098.999994 W. The coil optical input is published for a separate apparatus; its hypothetical pairing here is not confinement validation or a magnet sizing result.

Cold-control nuclear yield is held fixed in these cost sweeps. A real magnet or changed target state could change the reaction probability; a new qualified physics calculation is needed to quantify it. No measured magnetic or acoustic enhancement is assumed or ruled out.

## Explicit boundaries

Let B be beam energy, Q nuclear release, eta the wall-to-beam product, and r_s the electrical recovery fraction of the source-conversion remainder B/eta-B. With perfect downstream electrical return and cyclic storage:

`net_J_per_fired = Q - (1-r_s)*(B/eta-B) - containment_J_per_fired - other_net_loads`.

For continuous containment power, its equivalent per fired shot is P_hold/(attempt_rate*fired_fraction). Main-source cost and a pulsed containment driver apply per fired shot; continuously running containment is charged across every attempt, including nonfiring attempts. Preparation/idle costs are explicitly set to zero only for a favorable sensitivity case, not measured to be zero. No acoustic multiplier is used. Stated repetition rates are sensitivity inputs, not demonstrated operating rates or target-replacement feasibility.

The source refund options0%,30%,100% are hypothetical electrical recovery, not heat recovery.100% is an energy-only limiting case without established thermodynamic feasibility. The source remainder includes optical energy not transferred to the selected protons as well as driver losses; it cannot be re-credited elsewhere. A positive row under perfect source/downstream return is a formal bound, not evidence of a feasible generator.

The required-refund threshold includes the selected containment load. Values above1 mean no permitted source-conversion refund can break even under that selected budget. This is distinct from the earlier restricted99.9994% source-efficiency bound. No universal apparatus threshold is inferred.

## What containment actually costs

An exact apparatus cost remains unavailable: no actual coil circuit, current waveform, resistance, cryogenic load or qualified confinement lifetime has been specified. containment.py provides separate engineering bookkeeping functions:

- Steady coil: startup magnetic inventory L*I^2/2 is separate from continuous I^2*R/supply_efficiency plus cryogenic/support power. Superconducting operation is not automatically zero wall draw.
- Pulsed coil: unrecovered magnetic inventory plus the resistive current-time integral. The helper uses an explicit rectangular-current approximation; realistic waveforms require their own integral and supply model. An external measured wall-energy trace should replace this estimate, not be added to it.
- Laser-driven coil: count its additional optical pulse through its own wall-to-optical efficiency. Do not also bill the same coil dissipation as a second independent supply. These rows do not infer confinement volume or lifetime from field strength alone.

## Prior art and primary-source anchors

Reviewed2026-11-01(Pacific). All contextual measurements below belong to their cited setups. No measured datum is automatically transferred into the STARS model.

1. Labaune et al.(2013), *Fusion reactions initiated by laser-accelerated particle beams in a laser-produced plasma*, https://doi.org/10.1038/ncomms3506 . Demonstrated laser-generated protons on laser-produced boron plasma. Its separate400J long pulse and20J short pulse illustrate why target preheating must also enter a full driver ledger. This sweep does not reproduce that experiment or silently add its yield.
2. Tosca et al.(2025), *Hydrogen boron fusion in confined geometries*, https://doi.org/10.1017/hpl.2025.10055 . Experimental hollow/curved target work and self-generated-field PIC analysis. Not experimental validation of the complete external PRISM/ceramic/acoustic stack; filtered angular alpha flux is not automatically total nuclear energy.
3. Molloy et al.(2025), *Alpha particle production from novel targets via laser-driven proton-boron fusion*, https://doi.org/10.1103/PhysRevResearch.7.013230 . Published experimental/source-model comparison; data on request. Its target/temperature dependence is a different benchmark lane from the current cold single-pass model.
4. Brenner et al.(2014), *High energy conversion efficiency in laser-proton acceleration by controlling laser-energy deposition onto thin foil targets*, https://doi.org/10.1063/1.4865812 . Author manuscript: https://strathprints.strath.ac.uk/50198/1/Brenner_etal_APL2014_laser_proton_acceleration.pdf ;15% in5–30MeV protons with an optimized double pulse/5um Au foil. Not a675keV coupling measurement.
5. LLNL driver-technology roadmap: https://lift.llnl.gov/research-areas/ife/driver-technology . >=10% wall-plug development goal; ideally>15%. This is not a matched measurement for a short-pulse proton driver.
6. Santos et al.(2015), *Laser-driven platform for generation and characterization of strong quasi-static magnetic fields*, https://doi.org/10.1088/1367-2630/17/8/083051 .500J,1ns laser input and reported fields up to800T in its capacitor-coil experiment. Used only as an optional extra-driver energy reference; not a cost or field map for our apparatus. The paper discusses diagnostic limitations and earlier overestimated field claims.

Thus much of the conventional laser/target research has indeed been done before. The exact combined apparatus and claimed net-power performance do not follow merely from assembling those papers. The immediate research value is reproducible comparison, power accounting and resolving measured source/target behavior; the archived enhancement stack remains available for controlled future tests.

## Run

From the repository root, using the sibling PR64 files preserved in the parent commit:

```
python research/stars_2_0/implementation/wall_plug_sweep_v0_1/run.py --out new_wall_plug_results
python -m unittest discover -s research/stars_2_0/implementation/wall_plug_sweep_v0_1 -v
```

Python standard library only. Every output directory must be new. Source hashes are in the receipt.10 tests cover optical-chain accounting, ideal refund limits, containment, failure-rate/continuous-power accounting, input rejection and startup-field inventory. Numerical test fixtures are not coil specifications. Actual apparatus net power remains null; scenario powers are explicitly conditional.
