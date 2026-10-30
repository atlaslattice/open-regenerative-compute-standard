# Beyond Q v1.1.2 — Secondary D-T Burn: Tritium-Credit, Neutron-Damage, and Campus Opportunity-Cost Addendum

**Dated:** 2026-10-30 · **Status:** APPEND-ONLY, SOURCE-BOUNDED RESEARCH ADDENDUM / POTENTIAL-DERIVED · **Parent:** v1.1.2 draft PR #41 · **No physical self-sufficiency claim.**

**Provenance:** Atlas Lattice project originator raised the hypothesis that Reactor A's secondary D-T burning may produce blanket and energetic benefits exceeding its neutron-induced maintenance cost. GPT-6 (OpenAI/Tidal Lantern) derived the comparison and checked public primary/review literature on 2026-10-30; DeepSeek and Gemini Argon contributed preceding independent discussions on design differentiation, tritium-lean operation, blanket tradeoffs, and modeling methods. Attribution denotes model-assisted research discourse, not institutional coauthorship, experimental work, or endorsement.

## Abstract / key finding
Permanent separation of dedicated D-D isotope Reactor A and D-T power Reactor B is a testable **architectural choice**. It cannot be credited as complete avoidance of 14.1-MeV neutrons in A if the proposed in-situ secondary D-T burn remains enabled. Nevertheless, secondary D-T burning *could* provide incremental nuclear heat, energetic neutrons usable by natural-lithium and enriched-lithium blankets, and improved campus economics. The critical question is whether these qualified incremental outputs exceed internally consumed tritium plus additional neutron damage, activation, shielding, outages, capital, and auxiliary costs. No reactor-specific neutronics, lifetime, or economic numbers have yet demonstrated a positive net benefit.

## 1. Fixed reference; explicit source-rate conditions
Reactor A: **20 MW primary D-D fusion power** (hypothetical), near-equal D-D branches, gross direct tritium births ~**2.70 kg/FPY** and D-D 2.45-MeV neutron emission ~**1.71×10^19/s**. Reactor B: **1.13 GW D-T fusion power**, with its own lithium-breeding blanket. These are reference operating points, not measurements.

Let `f` be the fraction of the **D-D-born** tritium that undergoes in-situ secondary D-T fusion. For a constant primary D-D rate, `N_DT,sec = f * N_T,DD` and `P_DT,sec = f * N_T,DD * Q_DT`. For the prior **18 MW** secondary D-T screening case, `f≈0.373` and internal burn is **~1.01 kg T/FPY**. Secondary 14.1-MeV neutrons number **~6.38×10^18/s**; the secondary power is an **assumed conditional case**, not a plasma-confinement prediction. It adds ~18 MW nuclear fusion energy, not automatically recoverable electricity. Full-power-year assumptions, operating schedules and exact reaction branching must remain versioned.

## 2. Incremental tritium break-even (the central test)
Compare two matched Reactor A operating conditions: the *same primary D-D source* with secondary D-T **OFF** versus **ON**. Define `L_A(f)` as gross blanket-born T under a modeled neutron spectrum, and `Q_A(f)` as qualified net T export after distinct plasma and blanket recoveries, processing losses, permeation, decay and inventory holdup.

`ΔQ_A = Q_A(f) - Q_A(0)`

Under the deliberately simplified idealized 100%-recovery, equal-loss model:

`ΔQ_A = [L_A(f) - L_A(0)] - f * D_A`.

Thus secondary burn **improves Reactor A's available T production only when the added *recovered* blanket T exceeds the recovered-tritium opportunity cost of the in-plasma secondary burn**. At the former 18 MW case, the *gross* illustrative threshold with no losses is **>~1.01 kg/FPY of incremental blanket T**. With route-specific losses, the full `ΔQ_A` equation replaces this shortcut.

When incremental blanket yield is expressed as effective *qualified* T births per secondary D-T neutron, the idealized threshold is **>1 recoverable T per secondary D-T neutron** *if* the triton otherwise would have been recovered with unit efficiency. This is a demanding **conditional threshold**, not a claim that neutron multiplication or a particular TBR can achieve it. Neutron multiplication, Li-7 reactions, parasitic capture, geometry and materials must be solved in G2.

**Do not subtract the entire A blanket yield from secondary-burn costs**: primary D-D neutrons and their associated baseline breeding remain in both cases. Also avoid counting secondary tritium burned as available for both Reactor B export and helium-3 decay banking.

## 3. Broader value equation; physical neutron costs cannot be 'cancelled' in units
Net *economic* benefit, not net neutron count, decides whether a secondary burn is worthwhile:

`ΔNPV_A = PV(qualified incremental T value + qualified incremental recoverable energy + any additional coproducts) - PV(incremental RF/heating/processing/shielding + activation/maintenance + downtime + replacement + financing + opportunity costs)`.

The tritium mass balance and the energetic/financial ledger must remain **separate**. More nuclear power does not guarantee positive wall-plug electricity or lifecycle value; more fast neutrons may increase blanket breeding and structural damage **simultaneously**. The appropriate damage metrics include spectrum-resolved flux to first-wall/vacuum-vessel components, dpa/FPY, He/H transmutation appm/FPY, activation/contact dose/cooldown requirements, replacement schedule, and plant availability. These require material-specific transport/damage libraries and component geometry—not simple 14.1-to-2.45 MeV neutron count ratios.

## 4. Suggested experiment matrix (G1–G5)
1. Hold 20 MW primary DD constant where physical plasma solutions permit, and sweep secondary triton burn fraction `f=0,0.05,0.10,0.20,0.373,0.50,0.75,1.0` as **formal bound/sensitivities**, not all physically achievable operating points.
2. For each f, independently derive secondary neutron spectrum and physically attainable confinement; G1 must reject impossible regimes rather than force convergence.
3. Compare A0 no breeding (functional shield/cooling retained), A1 natural Li, A2 optimized Li enrichment and multiplier. G2 tally separate ^6Li, ^7Li tritium births, extra neutrons, nuclear heating, neutron leakage, component exposure and uncertainties.
4. Couple source-resolved neutron yields into G3 recovered plasma-derived and blanket-derived T streams, and G4 time-resolved storage, outages, fuel transfers and optional helium-3 decay allocations. Do not use the retired 1.3–2.6kg estimate as validated calibration.
5. G5 report nuclear MW, recoverable heat, parasitic MW, net electric MW, annual qualified isotope kg, dpa, activation, cost, component replacement, and lifetime NPV; run adversarial low-yield/high-damage scenarios.
6. Evaluate three decisions: secondary OFF, partial burn, full physically achievable burn. Present Pareto fronts rather than assume monotonically increasing value.

## 5. Related independent research and novelty caveat
- Morandi, Meschini, Testoni & Zucchetti (2026) study 0D multispecies plasma–fuel-cycle dynamics, including D/T/He-3/He-4, non-50:50 operation and residence times. Relevant **cross-validation model**, not proof of Beyond Q geometry [R1].
- Lopes Cardozo & van Rheenen (2026) analyze tritium-lean/intermittent startup and deployment [R2]. Their result motivates transient/initial-inventory comparisons, not a claim that permanent separation is necessarily economically better.
- Dedicated tritium breeding plants and power-producing plants with cooperative fleet-level fuel cycles have been discussed in contemporary 2026 literature [R7]; **do not claim globally unique two-reactor operation without an exhaustive literature and patent review**. Specific isotope-refinery + cryogenic coproduct campus integration remains a potential research differentiator, not verified intellectual-property novelty.
- Pure D-D startup, pure D-D isotope operation, and a D-D system with secondary D-T burn are different neutron environments. Separate-system architecture may localize damage but **does not eliminate A's fast-neutron activation** in the secondary-on configuration.

## 6. Source appendix / evidence mapping
| ID | Source | Exact role; limitation |
|---|---|---|
| R1 | Morandi et al., *Modeling fuel cycle dynamics beyond 50:50 deuterium–tritium operation*, *Fusion Engineering and Design* **231** (2026) 115982; https://doi.org/10.1016/j.fusengdes.2026.115982 | Open-source multispecies, residence-time methods; no A+B performance or neutron-material validation |
| R2 | Lopes Cardozo & van Rheenen, *An analytical model linking tritium breeding, tritium-lean startup and fusion power deployment*, *Nuclear Materials and Energy* **48** (2026) 102183; https://doi.org/10.1016/j.nme.2026.102183 | Startup/inventory/TBR theory and external T kickstart; no coupled A+B experiment |
| R3 | ITER, *Engineering Basis Handbook*, chapter 9: Li-6(n,α)T and Li-7(n,n'α)T breeding and isotope-enrichment context; https://www.iter.org/sites/default/files/media/2026-02/vol.1_ch.09_gaps_to_fill_beyond_iter_e5ynb7.pdf | Reaction pathways and material issues; not a measured proposed blanket TBR |
| R4 | Knaster, Moeslang & Muroga, *Materials research for fusion*, *Nature Physics* **12** (2016) 424–434; https://doi.org/10.1038/nphys3735 | 14.1-MeV neutron damage, gas production and materials challenges; no reactor-A lifetime estimate |
| R5 | *Fusion Neutrons: Tritium Breeding and Impact on Wall Materials and Components of Diagnostic Systems*, *Journal of Fusion Energy* (2018); https://doi.org/10.1007/s10894-018-0182-1 | D-D 2.45-MeV source, D-D branch and general D-T neutron context; no coupled A geometry |
| R6 | *Predictive modelling of tritium breeding ratio in EU DEMO WCLL blankets: OpenMC simulations and analytical insights*, *Fusion Engineering and Design* (2026 online record); https://www.sciencedirect.com/science/article/pii/S0920379625007124 | Energy-dependent lithium breeding and neutron heating in another design; not ARC evidence |
| R7 | *Observations for a Fusion Tritium Economy*, *Fusion Science and Technology* (2026), https://doi.org/10.1080/15361055.2026.2716587 | Fleet-level dedicated tritium-breeder / power-plant separation explored; read exact modeling conditions before novelty claims; not experimental validation |

## 7. Verification / exit criteria
- Preserve v1.0 and v1.1–v1.1.2 historical outputs; this is an append-only addendum.
- Treat threshold `ΔQ_A>0` for *isotope only*, and `ΔNPV_A>0` for economic benefit, independently.
- Source labels: **SOURCE-TRACED** for cited actual research, **VERIFIED-DERIVED (conditional)** for reaction stoichiometry and algebra, **POTENTIAL-DERIVED** for hypothetical source strength/blanket yields/NPV, **UNRESOLVED** for physics, lifetime and operational gain.
- Reconstruct a physics-consistent `f` with plasma kinetic model; do not simply hold DD power fixed if changing secondary reaction changes confinement and input power.
- No new verified tritium yield, power gain, quantified vessel-life improvement or operational net benefit is claimed.

**Search/metadata keywords:** Beyond Q, Atlas Lattice, STARS 2.0, GPT-6, DeepSeek, Gemini Argon, D-D, D-T, secondary deuterium-tritium fusion, in-situ triton burn, tritium mass balance, neutron-induced activation, 14.1 MeV, 2.45 MeV, tritium breeding blanket, lithium-6, lithium-7, FLiBe, neutron multiplication, TBR, dpa, helium transmutation, isotope refinery, standalone reactor architecture, ARC V3A, 1.13 GW, startup tritium, fuel-cycle dynamics, capital allocation, helium-3, quantum cryogenics, full power year, OpenMC, independent replication, uncertainty propagation, reactor lifetime, Pareto optimization, NPV, safety, materials durability.
