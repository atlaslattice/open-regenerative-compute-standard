---
title: "Beyond Q v2.3 — Global Quantum-First Infrastructure and Fusion Isotope Integration"
date: "2026-10-29"
version: "2.3-TECH"
keywords: ["fusion-powered quantum computing","ARC fusion","Google Quantum AI","Microsoft Majorana 2","China quantum computing","deuterium deuterium","deuterium tritium","helium-3","tritium fuel cycle","quantum cryogenics","isotope refinery","neutron transport","data center electrical load","quantum error correction"]
status: "Independent research; not peer reviewed or endorsed"
---

RESEARCH BRIEF • OPEN TECHNICAL REVIEW

Global quantum-first infrastructure and fusion isotope integration

Technical screening white paper \| Google, Microsoft, China \| ARC D-T and hypothetical D-D

Version 2.3-TECH \| 29 October 2026 \| Independent proposed research; not endorsed by MIT, Microsoft, Google, CFS or any Chinese institution.

Evidence code: SOURCE-TRACED = sourced statement; VERIFIED-DERIVED = checked arithmetic; POTENTIAL-DERIVED = hypothetical-input result; UNRESOLVED = not sufficiently evidenced; LAB-MEASURED reserved for a traceable physical measurement and scope.

# Abstract

We develop a reproducible, evidence-graded pre-feasibility framework for aligning quantum-computing hardware requirements with advanced power generation and strategic helium-3/tritium supply. The study compares Google superconducting and neutral-atom research, Microsoft Majorana topological and ecosystem-partner hardware, and Chinese neutral-atom, superconducting and photonic platforms. We contrast C1 conventional dual-D-T ARC, C2 D-T plus speculative D-D isotope refinery, C3 grid-hybrid integration and C4 embedded quantum-classical nodes. Primary-source records establish disparate hardware stages but do not establish a 200-400 MWe quantum-only demand or commercial D-D retrofit feasibility. A transparent algebraic D-D model checks nuclear branches, secondary D-T burn, lithium-6 Q energy, injected RF energy, thermal conversion, recovered isotopes, tritium decay, and electrical opportunity cost. All reactor-specific performance outputs remain potential-derived pending a self-consistent plasma and neutron-transport solution.

# Executive finding

The best presently supportable action is a staged feasibility investigation. Commercial D-T ARC power has an independently published design basis; a D-D isotope refinery does not. Quantum-system electricity and cryogenic isotope inventory differ by modality and cannot be specified from physical-qubit count alone. The study identifies measurable gate criteria and refuses to monetize hypothetical isotope production before physical closure.

# 1. Research scope, definitions and evidence policy

This is a research memorandum intended for independent physicist/cryogenic/quantum-computing review; it is not peer-reviewed, an MIT-authored paper, a vendor-endorsed facility design, or a claim of production readiness. No proprietary operator information is assumed. Version date is 29 October 2026; published timelines and component numbers can change. Every quantitative claim uses one of five grades: LAB-MEASURED when primary reporting includes an experimental protocol and appropriate context; SOURCE-TRACED for a directly attributed sourced claim; VERIFIED-DERIVED for arithmetic on defined assumptions; POTENTIAL-DERIVED when physical inputs are hypothetical; UNRESOLVED for missing key sources or transferability.

The report intentionally does not place p-B11 STARS/PRISM results in the baseline reactor ledger. Those are separate research branches. A source-traced hardware specification is not necessarily a measured wall-plug requirement, and vendor qubit count is not equivalent to logical-qubit performance.

# 2. Commercial fusion reference and version control

The ARC V3A 2026 peer-reviewed physics-basis paper lists major radius 4.62 m, minor radius 1.18 m, axial field 11.4 T, and plasma current 12 MA; it projects approximately 1.13 GW D-T fusion power and \>=400 MWe grid delivery. The operating power balance explicitly adds about 100 MW of exothermic lithium-blanket energy and about 20 MW plasma heating, giving approximately 1260 MWth at flattop. After time-averaging a 15-minute flattop plus a 1-minute interflattop interval, the paper reports about 1180 MWth and approximately 500 MWe gross at 42% steam Rankine efficiency, minus about 100 MWe auxiliaries. These are design calculations, not achieved plant performance. \[R01,R26\]

The 2015 Sorbom ARC is a different, smaller approximately 200-250 MWe conceptual design, with demountable REBCO magnets, replaceable vessel and FLiBe blanket. The 2018 Kuang study explores modified vessel/divertor heat-exhaust geometry, not a tested D-D cartridge. Neither paper establishes 85-90% commonality or a priced D-D conversion of ARC V3A. The 2026 disruption study anticipates 1-2-year vessel lifecycle but does not establish 20-year operation for a different D-D neutron field. \[R04,R05,R22\]

| **Reference**        | **Reported/derived size**         | **What is justified**                                    |
|----------------------|-----------------------------------|----------------------------------------------------------|
| 2015 ARC conceptual  | ~200-250 MWe; R=3.3 m; 9.2 T      | Demountable magnet/VV idea; no current V3A retrofit cost |
| 2026 ARC V3A         | ~1.13 GW fusion; \>=400 MWe grid  | Published D-T design reference; not commissioned         |
| Hypothetical ARC-D-D | 20 MW primary D-D screening input | No reactor operating point established                   |

# 3. Real Google fusion PPA versus hypothetical quantum campus

Google committed in June 2025 to purchase 200 MW of electricity from the initial CFS ARC plant and has options on future plants. It is not a 200 MW quantum facility contract, and the plant is planned for grid supply in the early 2030s. The commercial benchmark is valid for price/power opportunity comparisons but must not be presented as a quantum demand commitment. \[R03,R23\]

# 4. Global quantum hardware architecture: source-traced matrix

| **Track**              | **Published hardware/goal**                                      | **Cooling and energy evidence**                        | **Caution**                                           |
|------------------------|------------------------------------------------------------------|--------------------------------------------------------|-------------------------------------------------------|
| Google superconducting | Willow, 105 physical qubits; below-threshold code evidence       | Dilution refrigeration; facility kW absent             | No 320 MW decoder demand                              |
| Google neutral atom    | Boulder initiative announced 2026                                | Laser/ultrahigh-vacuum; architecture-dependent cooling | No universal 4K requirement                           |
| Microsoft Majorana     | 2026 Majorana 2 lead stack; company-reported ~20 s mean lifetime | Low-T topological devices; no rack MW                  | M2 engineering evidence needs independent replication |
| Microsoft partners     | Magne/Atom Computing neutral-atom roadmap                        | Different from Majorana cryo envelope                  | Do not reduce Microsoft to topological-only           |
| China neutral atoms    | Hanyuan-2 200 atoms; reported \<7 kW total                       | Laser-cooling without dilution refrigeration           | Single-machine vendor-reported power                  |
| China superconducting  | Zuchongzhi-3.0 105 qubits; SL3000 vendor cold capacity           | 3 mW @100 mK and 90 uW @20 mK for SL3000               | Cold watts != wall watts                              |
| China photonics        | Jiuzhang 4.0 boson-sampling device                               | Optics + superconducting photon detectors              | Sampling != universal fault tolerance                 |

# 5. Google track: superconducting and neutral-atom demand model

Willow showed error suppression as a surface-code array grew from 3x3 to 7x7, with 105 physical qubits in the 2024 experiment. The source also reports decoder delays of approximately 50-100 microseconds in its setup; a typical microsecond-scale QEC cycle cannot be converted directly to a requirement for hundreds of MW of TPUs. The duty cycle, parallel decoding architecture, operation type and accelerator efficiency must be specified first. \[R08,R24\]

Google announced a parallel neutral-atom program in March 2026 led by Adam Kaufman, complementing rather than replacing superconducting research. Neutral atoms rely on atomic arrays, laser controls and vacuum, with system-specific cryogenics. No source substantiates the previously proposed 45 MW superconducting + 20 MW neutral-atom cryogenic split. \[R09\]

# 6. Microsoft track: Majorana 1, Majorana 2 and partner hardware

Microsoft reported that Majorana 2 replaces aluminum with lead in a semiconductor-superconductor stack, enlarges the topological gap, and exhibits mean qubit lifetimes around 20 seconds, at least 1000x relative to its older devices, with microsecond-scale control. This is company-reported and must be checked against protocol-level primary research for experimental grading. Microsoft roadmap aims for Level 3 systems starting at 1 million reliable quantum operations per second and error rate less than 1 in a trillion; these are aspirational application-level goals, not specified facility MW. \[R11-R13,R25\]

Microsoft software/ecosystem work includes partner hardware: the planned Magne machine with Atom Computing neutral atoms. A Microsoft campus specification should therefore include topological and partner-neutral-atom branches, each with separate cooling, optical control and error correction. \[R14\]

# 7. China track: three modalities, not one power figure

Hanyuan-2 comprises two 100-atom arrays (Rb-85 and Rb-87), 200 neutral-atom qubits overall, with a reported whole-system electricity demand below 7 kW, no millikelvin dilution refrigerator, and a standard-rack form factor. The power figure is source-traced public reporting, not an independent energy audit. Scaling to 10^6 error-corrected qubits requires new control, lasers, routing, electronics, cooling and overhead evidence. \[R15,R16\]

Origin SL3000 vendors specify ≥3000 microW of cooling at 100 mK, ≥90 microW at 20 mK, 1000+ qubit packaging capacity and 4000+ cable accommodation. No public whole-wall-plug consumption is specified. Zuchongzhi-3.0 is a 105-qubit superconducting processor, while Jiuzhang 4.0 is a peer-reviewed large-scale Gaussian boson-sampling photonic prototype, not a demonstrated universal gate-model computer. Their performance metrics must be compared task-by-task. \[R17-R19\]

Claims concerning the Turpan ~900-rack project, Tumed Right Banner ~411-rack cluster, and 1000 MW Spain quantum+AI memorandum remain unverified in the supplied records; they are excluded from the benchmark until original project documents establish status, rack electrical limits, actual loads and the size of the quantum subsystem.

# 8. Quantum-first load specification and thermal boundaries

For every hardware route, define discrete QPU electronics and cold stages; physical control waveform generation; FPGA/ASIC error decoder; instrument networking; optional AI/HPC; facility distribution/cooling; and backup power. Require time-averaged and peak loads separately, including duty cycle, ramp and availability. The algebraic campus sum applies only to nonoverlapping boundary terms:

P_campus = P_QPU_electronics + P_cryogenic_wall + P_control + P_QEC_decoder + P_optics + P_network + P_justified_HPC + P_facility_overhead. Do not apply PUE to a campus total that already includes overhead. Cold-stage loads (W at 20 mK/100 mK/4 K) cannot be directly added to electrical MW without a measured complete refrigerator model.

For any ideal single-stage refrigerator rejecting heat at 300 K and extracting at 100 mK, the Carnot minimum work ratio is W/Q_cold \>= (300/0.1)-1 ≈ 2999. Real multistage systems have higher effective wall-plug costs. The earlier suggested sensitivity of 200-1000 W_elec per watt extracted at 100 mK is below this minimum and must not be used as a physical power model. A 3 mW @100 mK cold capacity does not mean ~3 W input or any fixed vendor power. \[R17,R21\]

# 9. Demand-driven sizing and the null result

| **Capacity envelope** | **Purpose**                     | **Acceptance criterion**                               |
|-----------------------|---------------------------------|--------------------------------------------------------|
| Node / embedded C4    | kW-class to a few MW            | Actual QPU + shared IT facility loads measured         |
| 25 MW M0              | research and supporting compute | Justified dedicated equipment and utilization          |
| 50 MW M1              | intermediate R&D campus         | Measured cooling/controls and commercial workload      |
| 100 MW M2             | expanded hybrid                 | Verified classically useful workload separate from QEC |
| 200 MW M3             | hyperscale reference            | No reliance on Google PPA as quantum demand            |
| 400 MW M4             | ARC output ceiling scenario     | Only if measured load stack actually scales there      |

The null result is commercially meaningful: if real quantum hardware needs 10 kW to 10 MW in an existing facility, a 400 MW power plant could supply a separate grid or Azure/AI workload, but a dedicated quantum-first campus at that nameplate would be unjustified.

# 10. D-D nuclear reaction ledger: requirements and branch closure

For pure D-D fuel, two principal low-energy branches are D(d,p)T with Q ≈3.269 MeV and D(d,n)He-3 with Q ≈4.033 MeV. At a hypothetical constant 20 MW primary D-D fusion output and equal branch fractions, source reactions are determined by Q-weighted energy per event. Tritium and He-3 are born in different branches. Secondary D-T uses Q≈17.589 MeV; its fusion power is a function of the fraction of born T that undergoes in-plasma burn, not an independent free 18 MW knob. \[R04,R07\]

The independent algebraic run at a 28% born-T secondary burn gives 13.49 MW secondary D-T, not the previously circulated 18 MW. To obtain 18 MW secondary D-T with this 20 MW D-D source and equal branching would require approximately 37.4% burn of born T, subject to a real plasma solution. A secondary D-He-3 branch and any beam-target fast-ion tails must be added using explicitly calibrated cross sections and transport; omitted channels are not assumed zero in a validated plant.

At 85% annual availability, this illustrative 20 MW DD case births approximately 2.295 kg/year of tritium before burn and processing, and 17,057 STP L/year of born He-3. With 28% T burn, 78% remaining-T capture, 50% neutron capture, and 85% blanket extraction, the model yields 2.538 kg/year recovered tritium. These are merely conditional stoichiometry, not a tritium-breeding claim. The 75% He-3 capture assumption produces about 12,793 L/year. No plant extraction apparatus is established.

# 11. Neutron source, blanket and RF energy: no invented residual

Li-6(n,alpha)T releases approximately 4.783 MeV per qualifying capture, in addition to deposited incident neutron kinetic energy. A 38 MW fusion scenario cannot claim 97 MW blanket nuclear heat by subtracting its fusion power from a desired thermal total. The 2026 ARC D-T reference has about 100 MW lithium reaction heat at 1.13 GW fusion; those D-T figures are not a fixed coefficient for low-energy D-D neutron spectra. Source-specific neutron transport is necessary. The July 2026 laser-driven D-D source-fidelity preprint demonstrates sensitivity to angular-energy spectra and lithium composition, but laser-accelerated thick-target sources differ from thermal D-D tokamak plasmas. \[R01,R07\]

Separately, injected RF power is external electrical energy; when absorbed, it can eventually produce thermal energy. It must appear as an incoming RF stream and later heat, not be misclassified as additional nuclear fusion Q. The earlier 135 MWth may be numerically close to a sum of nuclear energy and ~80 MW RF deposition, but the historical ancestry is unverified. Additional magnet, vacuum, cryogenic and isotope loads must remain electrical debits.

# 12. Reproducible provisional D-D whole-facility calculation

The included beyond_q_physics_v23.py is an algebraic sensitivity calculator only. It assumes 50:50 D-D branching, 28% born T in-plasma secondary D-T burn, 50% effective Li-6 neutron capture without multiplication, 80 MW delivered RF, 70% RF wall-plug conversion, 90% RF power deposited, 85% of deposited energy collected as thermal recovery, 40% turbine efficiency, 15 MWe other electrical auxiliaries, and 85% annual capacity factor. Neutron leakage, material/temperature constraints, impurity radiation and secondary He-3 burn are not solved.

| **Term**                      | **Illustrative calculation** | **Evidence**                |
|-------------------------------|------------------------------|-----------------------------|
| Primary D-D fusion            | 20.00 MW                     | POTENTIAL-DERIVED           |
| Secondary D-T fusion          | 13.49 MW                     | POTENTIAL-DERIVED           |
| Li-6 capture Q                | 8.38 MW                      | POTENTIAL-DERIVED           |
| Total nuclear Q               | 41.87 MW                     | POTENTIAL-DERIVED           |
| RF deposited                  | 72.00 MW                     | POTENTIAL-DERIVED           |
| Collected recoverable thermal | 96.79 MWth                   | POTENTIAL-DERIVED           |
| Gross electrical generation   | +38.72 MWe                   | POTENTIAL-DERIVED           |
| RF electric input             | -114.29 MWe                  | POTENTIAL-DERIVED           |
| Other auxiliary input         | -15.00 MWe                   | POTENTIAL-DERIVED           |
| Net DD electricity            | -90.57 MWe                   | Derived from assumed inputs |

This does not prove the heating power is compatible with the stated confinement, current drive, divertor heat flux, plasma beta, neutron field or isotope evacuation. No OpenMC, Serpent, MCNP or gyrokinetic/tokamak transport simulation was executed in this work. The pilot result is an accounting consistency test, not physical feasibility.

# 13. Tritium decay bank, daughter helium and inventory

At half-life 12.32 years, lambda = ln(2)/12.32 per year. For an initially empty vault receiving constant S kg/year with no withdrawals, active tritium I(t)=S/lambda\*(1-exp(-lambda\*t)). Cumulative daughter He-3 at 0 C and 1 atm is V3=(S\*t-I)\*1000\*22.414/3.01605 liters. The complete-decay theoretical yield is approximately 7.43 STP L per gram T; the approximately 0.42 L per gram per year is an initial decay rate, not total yield. \[R20\]

At an exogenously assumed 1.90 kg/year vault deposit for 20 years, the bank retains 22.81 kg tritium and theoretically generates 112,889 STP L daughter He-3. This is a mathematical stock-and-flow example, not an output claim from the D-D model. Indeed, the modeled qualified tritium available for a vault is constrained by prior in-plasma burn, recovery, reactor consumption and reserve policy. The 1.90 kg bank deposit must not be automatically combined with the recovered tritium case without checking available volume and any competing allocations.

| **Year** | **Active T vault (kg)** | **Cumulative daughter He-3 (STP L)** |
|----------|-------------------------|--------------------------------------|
| 0        | 0.00                    | 0                                    |
| 1        | 1.85                    | 390                                  |
| 5        | 8.28                    | 9,061                                |
| 10       | 14.53                   | 33,212                               |
| 15       | 19.25                   | 68,752                               |
| 20       | 22.81                   | 112,889                              |

# 14. Quantum helium demand: inventories are not annual burn

Dry dilution refrigerators generally recirculate a He-3/He-4 mixture; physical initial inventory is distinct from makeup after service, leaks or losses. Model wet/dry refrigerators separately, verify actual initial gas mixture, pressure, stage loads and closed-loop recovery, and distinguish STP liters of gas from liquid liters. No available primary Microsoft/Google manufacturer source supports universal 150 L per million-qubit cryostat or 1-2% annual loss. He-4 may be circulated in pulse-tube hardware; He-4 ash can only be credited to helium inventory after validated exhaust capture, separation, purification and storage. \[R17,R21\]

# 15. Opportunity-cost benchmark and competing system cases

In the example, replacing a second 400 MWe D-T reference with the hypothetical D-D unit changes net electrical capability by 400 - (-90.57) = 490.57 MW. At \$65/MWh and 85% capacity factor, that amounts to 3,653 GWh/year or \$237.4 million/year equivalent before plant capital, dispatch, power contract, permits, wholesale basis and sales constraints. This compares two alternative systems, not a measured electricity bill or market revenue. Isotope sales, reserves and avoided scarcity value must be in separate mutually exclusive economic categories.

| **Alternative**           | **Energy/isotope treatment**                                                | **Financial control**                              |
|---------------------------|-----------------------------------------------------------------------------|----------------------------------------------------|
| C1: 2x D-T                | ~800 MWe planned grid output reference; real availability requires sourcing | Electricity maximization counterfactual            |
| C2: D-T + D-D             | D-D potentially negative net; isotopes theoretical until gated              | Explicit lost second D-T power plus DD imports     |
| C3: grid-hybrid           | DD plant buys/exports power at time-varying tariffs                         | No free behind-the-meter power                     |
| C4: embedded quantum node | Only actual quantum + supporting classical load                             | Shared campus power/cooling and saved construction |

# 16. Business case: from value hypothesis to testable cost

At present, a confident economic positive case cannot be established. He-3 offtake price, licensed tritium markets, qualified helium purity, cost of plant availability, neutron damage and tritium processing are all unresolved. The customer benefit may be first-fill inventory, procurement avoidance, supply-chain resilience or validated research service. Use a cash-flow ledger with isotope sale revenue, truly avoided purchase costs and avoided-loss expected value never counting the same helium atom or same loss event twice. Record strategic reserve as a stock whose benefit is assessed by event probabilities, not a recurring sales line.

Commercial estimates in the recovered Gemini/Copilot discussion (85-90% hardware commonality, \$85-205M net adaptation, 20-year DD vessel, specific cryostat losses, 3.85 kg qualified T/year) must be carried forward as historical hypotheses with the source reconciliation required, not as accepted base-case inputs. \[R27\]

# 17. Engineering and deployment specifications

- Electrical: Separate QPU IT power, classical IT, facility cooling, RF wall-plug, thermal recovery, net import/export, grid failure and UPS; nameplate and annual energy independent.

- Thermal: Meter heat at 20 mK/100 mK/4 K/300 K and first wall/divertor/blanket/turbine/cooling system; thermal capacity equals actual reject energy, not an accounting residual.

- Magnet and plasma: Trace field, plasma current, beta, density, pressure, current drive, impurity, divertor and vessel envelopes to a declared ARC design generation.

- Nuclear: Distinguish source spectra, 6Li/7Li, Be multiplication, leakages, activation, alpha deposition, gamma streams and reaction Q values; use an actual transport code.

- Isotope: Separate born/recovered/captured/purified/stockpiled/sold T, He-3, He-4 at consistent STP and time denominators.

- Availability: Compute all-attempted availability, outage scenarios, startup charge and fault tolerance without claiming uninterrupted compute from single-unit supply.

- Compliance: Licensed tritium storage/transport and nuclear regulator review; detailed radiation protection, waste and secure isotope accounting are non-optional.

- Cyber/AI: Use human-in-the-loop operations for critical controls; no autonomous safety-critical override; separately audit ML decoder/control reliability.

# 18. Acceptance gates for an external technical-review committee

| **Gate**           | **Pass condition**                                                 | **Blocking evidence**                         |
|--------------------|--------------------------------------------------------------------|-----------------------------------------------|
| Q0: operator facts | Primary hardware dimensions, QEC metrics, stage-specific data      | No published wall-plug and material estimates |
| Q1: power/heat     | Disjoint electrical + cryogenic stage balance; no Carnot violation | No real per-QPU electrical data               |
| Q2: decoding       | Workload and latency benchmark on real decoder hardware            | No decode watts per logical operation         |
| F0: reference ARC  | 2026 V3A parameters and power cycle source-pinned                  | Future power plant not commissioned           |
| F1: DD plasma      | Self-consistent DD confinement, heating and exhaust                | 20 MW not yet demonstrated                    |
| N0: neutronics     | Spectrum-dependent blanket capture and all reactions closed        | No OpenMC/Serpent/MCNP run                    |
| I0: mass balance   | T/He-3/He-4 no double accounting, decay and extraction             | Separation/retention data absent              |
| I1: facility       | DD gross electrical, all loads, heat reject and island fallback    | Vessel/aux/cooling unqualified                |
| C0: interfaces     | QPU demand, firm power and reserve matched at common boundary      | No signed quantum offtake                     |
| E0: economics      | Risk-aware CAPEX/OPEX/foregone second DT/market capacity           | Price and replacement cost unresolved         |
| A0: adversarial    | Independent recalculation and negative gates retained              | Third-party review not completed              |

# 19. Proposed experimental/data acquisition packet

1.  Request from Google/Microsoft/CN operators (public or permissioned): whole-rack kW at each QPU generation, per-stage thermal watts, compressor kW, control/decoder watts per error-correction cycle, initial He-3 charge, annual refill, measured maintenance/uptime.

2.  Request from CFS or qualified independent authors: ARC V3A interface/magnet/VV/blanket limits, D-rich operating envelope, allowable port/ICRH modifications, realistic RF wall-plug, heat exhaust, vessel neutron damage, expected neutron spectra.

3.  Develop a reproducible OpenMC-based geometry/spectrum benchmark for a hypothetical DD unit, with Li6/Li7 and Be reactions, tally uncertainty, activation and dose. Do not use the unrelated laser-driven DD preprint as a reactor spectrum proxy.

4.  Procure independent isotope separation and cryogenic equipment vendor quotations, price elasticity evidence, storage requirements and end-to-end qualified output tests.

5.  Seek an independent subject-matter review with at least plasma confinement, neutronics, cryogenics, QEC and energy economics represented before presenting to potential customers.

# 20. Negative-results and falsification policy

A valid outcome can be: no ARC-compatible D-D operating point; too little tritium after secondary burn; He-3 market or demand smaller than the first-fill capacity; favorable isotope output but unacceptable foregone electricity; quantum C4 node not requiring any dedicated fusion supply. Record each of these outcomes as decisive rather than adjusting economic assumptions until a positive ROI appears.

# 21. Limitations and publication readiness

This technical report combines independently checked public sources with an executed transparent algebraic model and source inventory. It does not include experimental reactor operation, calibrated QPU electrical measurements, licensing feasibility, neutron Monte Carlo, plasma transport, an audited plant capital budget or an actual offtake agreement. The code passes algebraic invariants but that does not validate its assumed reactor physics. Consequently this document is appropriate for exploratory scientific discussion and external review, not for a claim of validated MIT-grade engineering feasibility or an investment solicitation as though such validation had occurred.

# 22. Quantum demand as an experimentally recoverable transfer function

Define a machine-scale vector X = (N_phys, N_logical, qubit family, cryostat topology, readout channels, code distance, cycle time, decoder implementation, optical lanes, device yield, uptime). Power P(X) must be predicted and then tested against a withheld hardware configuration. A single MW-per-qubit scalar is not physically justified. QPU silicon may dissipate very little at the cold stage while attached drive/readout electronics and refrigeration consume orders of magnitude more at the room-temperature boundary. Keep cold-stage and room-temperature budgets in different unit columns.

| **Sub-meter**      | **Required measured fields**                                                     | **Acceptance and failure mode**                                        |
|--------------------|----------------------------------------------------------------------------------|------------------------------------------------------------------------|
| QPU cold plate     | Cooling load at 10-20 mK, 100 mK and 4 K; uncertainty and instrumentation        | At least three distinct operating points and one idle control          |
| Control/readout    | Number of lines, line attenuation, cryo-CMOS/FPGA rack kW, duty cycle            | Account for every heat ingress and line; avoid hidden support racks    |
| Decoder            | Physical cycles/s, syndrome bits/cycle, operations/bit, hardware joules/op       | Real implementation latency and error performance; not AI-training TDP |
| Laser/neutral atom | Beam count, optical power, wall-plug laser efficiency, vibration/vacuum services | End-to-end kW including optical bench and cooling                      |
| Photonics          | Pump-laser electrical watts, SNSPD cold load, signal processing                  | Sampling demonstration distinguished from universal logical gates      |
| Facility           | Electrical distribution, UPS losses, chilled-water/fan/pump energy and PUE       | PUE reference boundary documented, not applied twice                   |

Benchmark operating points must include cold idle, active representative quantum program, peak calibration, recovery/restart, and simultaneous quantum/classical stress. Each state should report uncertainty on measured energy and algorithmic useful work. A device may produce zero commercial logical operations in an early laboratory state; that result must not be converted to cost per logical operation by inventing a throughput denominator.

# 23. Route-specific scalability and hard-to-transfer parameters

For Google superconducting devices, model thermal attenuation on all drive lines, resonator readout amplifier loads, fault-tolerant code distance and decoder interconnect. Willow-type surface-code figures are experimental at modest code distances; future error correction architecture, yield and networking cannot be inferred by multiplying 105-qubit results by 10,000. \[R08,R24\]

For Microsoft Majorana devices, preserve measured physical parity lifetime, control pulse duration, protected/nonprotected operations, magic-state overhead, code architecture and logical metrics as different axes. Company-reported multi-second lifetime does not uniquely determine real logical error probability or facility power. Also analyze Atom Computing/Magne as a distinct partner branch; Microsoft is a software/control ecosystem, not one refrigerator specification. \[R11-R14\]

For Chinese neutral-atom devices, count independent traps, parallel Rb species and optical channels, with source-reported \<7 kW treated as a whole-device point estimate. Do not assign all neutral-atom systems the same kW per 200 atoms: scalable addressing, rearrangement, laser stability, optical absorption and correction overhead will evolve nonlinearly. For superconducting devices, Origin SL3000 is a capacity-and-load specification rather than an electrical meter. Jiuzhang 4.0 photonic sampling is valuable evidence of a different modality but its task metric cannot be compared directly with rQOPS. \[R15-R19\]

# 24. Formal pre-feasibility test matrix: integration shall not be presumed

| **Test ID** | **Independent variable**                    | **Physical observable**                                  | **Predeclared reject condition**                         |
|-------------|---------------------------------------------|----------------------------------------------------------|----------------------------------------------------------|
| Q-EXP-01    | QPU modality and generation                 | kWh/useful logical operation and useful error rate       | Denominator lacks demonstrated logical operation         |
| Q-EXP-02    | QEC method and code                         | Syndrome traffic, joules per decoded operation, latency  | Decoder misses deadline or source omitted support racks  |
| Q-EXP-03    | Cryogenic scale/line count                  | Cold watts by stage and total measured AC input          | Thermodynamic lower bound violated or undocumented input |
| F-DD-01     | D-D density, temperature, auxiliary heating | Confinement, tritium birth, neutron source, wall loading | No stationary feasible operating point                   |
| F-DD-02     | T/He3 residence and secondary burn          | Energy-resolved particle flux and survival               | Predicted recovered output exceeds born inventory        |
| N-BLK-01    | Li-6/Li-7, Be, geometry, source spectrum    | Reaction-by-reaction Q, capture and neutron escape       | Heat or bred tritium not supported by transport tallies  |
| E-LDG-01    | Full auxiliary and heat recoverability      | Plant electric/thermal boundary residual                 | Energy conservation residual outside numerical tolerance |
| I-REC-01    | Isotope extraction and purification chain   | Qualified T, He3 product and radionuclide carryover      | No commercial grade or licensed chain demonstrated       |
| ECO-01      | Alternative C1-C4 capital constraints       | Risk-adjusted NPV versus foregone power and operation    | Positive case depends on unpriced displaced energy       |

Each test needs a version-controlled data receipt and uncertainty protocol. Within a gated simulation, a failed physics test blocks economic promotion regardless of the remaining model metrics. A pass in algebraic software only verifies code behavior; it does not replace experiments. Hardware acceptance is conditioned on measured or licensed process data.

# 25. Neutron-transport model specification for the proposed D-D blanket

A prospective OpenMC/Serpent/MCNP analysis must specify a 3-D vessel, first wall, FLiBe lithium composition and isotope enrichment, beryllium content, vacuum-vessel materials, port and divertor coverage, cooling channels, and thermal/activation regions. Neutron births should be represented as energy/angle/position distributions for each D-D and secondary D-T branch, normalized to branch rates from the plasma solver; do not reuse the laser-driven-target neutron source distributions as if they were thermal tokamak spectra. \[R01,R07\]

Mandatory tallies: source neutrons by type; Li-6(n,t), Li-7(n,x t) and Be multiplication; captures in metals/coolants and parasitic isotopes; escaping neutrons by surface and energy; photon-production and deposition; nuclear Q energy released by reaction; first-wall/divertor displacement per atom and gas production; tritium species location; power deposited in each thermal extraction circuit. Separate neutron slowing-down energy (part of the original fusion Q) from the extra exothermic nuclear capture Q to avoid double counting.

Report per-source-neutron dimensionless reaction probabilities and MeV per source neutron before multiplying by reactor MW. Statistical uncertainty must be supplied for both tritium yield and region-resolved heat. Sensitivity inputs should include moderator coverage, 6Li enrichment, LiF-BeF2 ratio, first-wall thickness, thermal boundaries, energy conservation, activation and neutron leakage. Critical accept gate: a balance must close for the neutron+photon transport energy and produced nuclide counts within statistical uncertainty; a positive full-device tritium breeding ratio cannot be inferred solely from primary D-D branching.

# 26. Plasma and secondary reaction self-consistency

The 20 MW D-D operating point must be supported by a plasma equilibrium, density profile, core temperature and external current-drive specification respecting ARC V3A geometry or an explicitly revised reactor. It must report achievable Q_plasma, stored energy, confinement time, radiation (including bremsstrahlung), impurity constraints, alpha/triton slowing-down, current-drive efficiency, disruptions, fuel injection and divertor exhaust. An apparent improvement in isotope survival could simultaneously decrease useful secondary energy or alter heating requirements, so reactor performance cannot be tuned by independent beneficial multipliers.

Secondary D-T rates must be calculated from the born-triton phase-space distribution and collisions, fast-ion confinement and exhaust. The same is true for D-He-3 secondary burn and its 14.7 MeV protons; a fixed zero is a programming placeholder rather than a prediction. State whether isotope accumulation occurs in plasma, divertor, blanket, pumps, storage or atmosphere and ensure each atom is allocated once. Separately assess effects of using protium-minority ICRF on energy deposition: the earlier suggestion that ICRF tuned to He-3 minority would necessarily destroy product is a mechanism hypothesis, not a validated retrofit operating rule.

# 27. Dynamic power resilience, availability and island operation

The nominal 400 MWe reference should not be sold as guaranteed continuous 400 MW delivered to a quantum site under every condition. ARC V3A is designed with pulsed 15-minute flattop and approximately 1-minute interval in the 2026 modeling paper; its total thermal cycle is time-averaged. The 400 MW net is a projected reference at the grid boundary. Power quality, storage, power electronics, utility interties, ride-through, frequency stability, redundancy, cooling continuity and time-to-restore matter particularly for dilution refrigerators and fault-tolerant logical states. \[R01\]

For campus C2/C3, model external grid import not only during cold startup but across the full electricity demand profile of a potentially negative-net D-D facility. Island mode should have a predeclared load-shed list distinguishing algorithm jobs that can be interrupted from cold systems that require continuous cooling. The earlier conjecture that shedding 65 MW of conventional AI jobs solves an emergency has no support without real quantum loads, process transfer curves, and storage autonomy. An honest model may require two D-T plants, grid support, storage and diversified critical feeds; compare architectures with equivalent reliability before economic claims.

# 28. Economic model specification with uncertainty and option value

A 20-year ledger should have annual rows by configuration and separate capital deployment, maintenance, isotope material balances and energy. Define revenue from grid exports or genuinely contracted quantum services only when demand exists. Internal electricity use is a cost at an explicit transfer price; commodity helium is a sale only after qualified product, licensed offtake and shipping. The 400+90 MW difference in our screening is electrical opportunity capability, not a proved loss in profits: plant capital budgets, market value, dispatch constraints and grid conditions may differ materially.

A defensible comparison must present at least four discount-rate sensitivities, carbon/power price cases, 70/85/95% capacity factors, helium offtake fraction, tritium market saturation, construction schedule and financing costs. For C4, shared cooling/network capital should be credited only to the fraction legitimately avoided. The economic gate should also test a no-isotope-sale/no-strategic-premium case, because claiming a premium without an actual buyer or risk model would make the investment result tautological.

Do not treat the 3.85 kg/year T from the prior Gemini scenario as a given; update in-plasma burn, blanket spectral capture, extraction, annual availability and internal use simultaneously. The hypothetical bank deposit of 1.90 kg/year is only attainable if physically qualified output after consumption reaches that amount. With our example gross recovered 2.54 kg/year, reserving 1.90 would leave only 0.64 kg/year for other purposes; that is a model allocation, not evidence that the actual plant can satisfy its sister D-T fuel requirement or grid-scale demand.

# 29. 2026 quantum and fusion readiness matrix

| **Claim**                        | **Best available evidence**                | **Missing demonstration**                                    |
|----------------------------------|--------------------------------------------|--------------------------------------------------------------|
| ARC V3A 1.13 GWfus / 400 MWe net | Peer-reviewed 2026 design physics basis    | Commissioned net-electric plant and operating availability   |
| D-D ARC module at 20 MWfus       | Pure scenario assumption                   | Tokamak confinement and engineering-compatible operation     |
| DD neutron captures and Li Q     | Known nuclear reaction data                | 3-D blanket source-appropriate transport/activation          |
| He-3 from T decay                | Established half-life + mole conversion    | Bank storage, licensed recovery and qualified product losses |
| Google 200 MW ARC purchase       | Signed corporate electricity announcement  | Quantum-exclusive offtake or site demand                     |
| Google Willow 105 qubits         | Published QEC experiment                   | MW/QPU at fault-tolerant scale                               |
| Microsoft Majorana 2             | Company-disclosed new material/device data | Independent full-system 2029 scaling and power               |
| China Hanyuan-2 \<7 kW           | Publicly reported product rating           | Independent power metering and error-corrected scale         |
| China Origin SL3000 3 mW@100 mK  | Vendor cold capacity                       | Total AC electricity and full load curve                     |
| Jiuzhang 4.0                     | Peer-reviewed specialized sampling         | Universal fault-tolerant workload and wall power             |

# Appendix A. Equations and unit conventions

- D-D branch event rate: N_DD = P_DD / \[f_T Q_DDpT + (1-f_T) Q_DDnHe3\]; energy units must convert MeV to joules.

- Secondary D-T fusion: P_DT = f_burn,T × f_T × N_DD × Q_DT; f_burn must emerge from transport for predictive purposes.

- Li6 Q-value: P_Li6 = N_Li6_capture × 4.783 MeV; capture count comes from neutron-transport tallies, not a forced TBR.

- RF electric: P_RF_wall = P_RF_delivered / eta_RF; RF absorbed creates deposited thermal power and must not be added twice as nuclear Q.

- Recoverable thermal: P_to_converter = f_collection × (P_nuclear_deposited + P_RF_absorbed + other identified recoverable deposition).

- Net: P_net = eta_cycle × P_to_converter − sum(all electrical auxiliary loads), with distinct boundaries.

- Tritium vault: dI/dt = S − lambda I; daughter He3 flow = lambda I; correct STP 0 C/1 atm mole conversion.

- Carnot: minimum work W/Qcold = (Thot/Tcold) −1 for reversible refrigerator; measured system uses stage-specific electricity.

- P_campus = sum(disjoint QPU electronics, optical, cryogenic wall, control, decoding, network, justified HPC and facility overhead), not QPU-nameplate plus PUE if facility was already included.

# Appendix B. Model reproducibility receipts

Run python beyond_q_physics_v23.py (standard library only) in the accompanying source folder. It generates screening_results.json, dd_sensitivity.csv, tritium_bank_20y.csv, assumptions.csv and model_checks.txt. Six invariants check net power, nuclear Q, plant boundary, recovered isotope \<= birth, vault material conservation and monotone decay. This is computational reproducibility of algebra, not independent experimental validation. Change inputs and re-run before drawing inference. The source registry CSV links all major assertions.

# Sources and claim scope

**\[R01\] Hillesheim et al. (2026), Overview of the physics basis for the ARC fusion power plant, Journal of Plasma Physics 92 E69** https://doi.org/10.1017/S0022377826101706 \| Peer-reviewed; ARC V3A reference, plasma and balance assumptions

**\[R02\] CFS (2026), ARC Physics Basis press release (June 4)** https://cfs.energy/news-and-media/commonwealth-fusion-systems-builds-on-learnings-from-sparc-to-publish-five-peer-reviewed-papers-validating-the-physics-of-the-arc-fusion-power-plant/ \| Operator source; design still future

**\[R03\] CFS + Google (2025), 200 MW ARC PPA announcement (June 30)** https://cfs.energy/news-and-media/google-and-commonwealth-fusion-systems-sign-strategic-partnership/ \| Corporate primary; electricity PPA, not quantum-site commitment

**\[R04\] Sorbom et al. (2015), ARC demountable-magnet design, Fusion Engineering and Design** https://doi.org/10.1016/j.fusengdes.2015.07.008 \| Peer-reviewed conceptual 2015 design, not 2026 V3A chassis

**\[R05\] Kuang et al. (2018), ARC heat exhaust management, Fusion Engineering and Design** https://doi.org/10.1016/j.fusengdes.2018.09.007 \| Peer-reviewed conceptual divertor/vessel design

**\[R06\] Meschini et al. (2023), Tritium fuel cycle for ARC/STEP-class plants, Nuclear Fusion** https://doi.org/10.1088/1741-4326/acf3fc \| Peer-reviewed model; needs scenario-specific closure

**\[R07\] Zhang et al. (2026), Neutron-source fidelity in laser D-D blanket tests, preprint** https://arxiv.org/abs/2607.13585 \| Preprint; non-tokamak D-D source; transfer limited

**\[R08\] Google Quantum AI (2024), Making quantum error correction work: Willow** https://research.google/blog/making-quantum-error-correction-work/ \| Primary reported 105-qubit below-threshold experiment

**\[R09\] Google (2026), Building superconducting and neutral atom quantum computers** https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/ \| Official expansion to neutral atoms

**\[R10\] Google Research (2025), A verifiable quantum advantage: Quantum Echoes** https://research.google/blog/a-verifiable-quantum-advantage/ \| Company research report, task-specific computational claims

**\[R11\] Microsoft Quantum (2026), Quantum Roadmap** https://quantum.microsoft.com/en-us/vision/quantum-roadmap \| Official goals: Level 1-3, milestone 6 rQOPS; targets not loads

**\[R12\] Microsoft Quantum (2026), Majorana 2 scalable quantum processor** https://quantum.microsoft.com/en-us/insights/blogs/majorana-2-scalable-quantum-processor \| Company-reported device claims; needs raw technical paper for measurement replication

**\[R13\] Microsoft Quantum (2025), Majorana 1 announcement** https://quantum.microsoft.com/en-us/insights/blogs/microsoft-unveils-majorana-1-worlds-first-quantum-processor-powered-by-topological-qubits \| Company architecture and aspirations

**\[R14\] Microsoft Quantum (2026), Logical qubit product engineering and Magne** https://quantum.microsoft.com/en-us/insights/blogs/from-research-to-product-engineering-logical-qubit-demonstrations-shaping-microsoft-utility-scale-quantum-software-platform \| Microsoft partners on neutral atom; not just topological platform

**\[R15\] Hubei Department of Economy and IT (2026), Hanyuan-2 release** https://jxt.hubei.gov.cn/bmdt/szgz/202605/t20260508_5929809.shtml \| Public provincial source: 200 dual-isotope neutral atoms

**\[R16\] Xinhua (2026), Hanyuan-2 reported whole-system \<7 kW** https://app.xinhuanet.com/news/article.html?articleId=2026050922f472aebdd345e9b1c927d29e48943d \| Reported vendor figure, not independent electrical metering

**\[R17\] Origin Quantum (2026), SL3000 manufacturer specification** https://originqc.com.cn/en/product/hardware?id=388 \| Vendor refrigeration capacity at 20/100 mK; wall-plug unresolved

**\[R18\] USTC (2025), Zuchongzhi-3.0 105-qubit superconducting prototype** https://en.ustc.edu.cn/info/1007/5015.htm \| University-reported prototype; no facility power

**\[R19\] Nature (2026), Jiuzhang 4.0 Gaussian boson sampling** https://doi.org/10.1038/s41586-026-10523-6 \| Peer-reviewed photonic sampling; not universal gate-model proof

**\[R20\] DOE (1999), Tritium handling and safe storage handbook** https://www.energy.gov/documents/doe-hdbk-1129-99pdf \| Authoritative decay constants, handling context; current regulations separate

**\[R21\] Guan et al. (2025), Cryogen-free dilution refrigerator, Rev. Sci. Instrum.** https://doi.org/10.1063/5.0294894 \| Peer-reviewed cold-capacity measurements; not wall power

**\[R22\] CFS (2026), ARC disruptions and design strategy, J. Plasma Phys.** https://doi.org/10.1017/S0022377826101585 \| Peer-reviewed design: replaceable vessel planned with 1-2 year life cycle

**\[R23\] CFS (2026), ARC grid-scale design overview** https://cfs.energy/technology/arc/ \| Operator commercial design and timelines

**\[R24\] Google Research (2026), Dynamic surface codes** https://research.google/blog/dynamic-surface-codes-open-new-avenues-for-quantum-error-correction/ \| New circuit QEC approach; no campus-load disclosure

**\[R25\] Microsoft Quantum (2026), Reliable quantum operations per second** https://quantum.microsoft.com/en-us/insights/education/concepts/rQOPS \| Definition: logical qubits times logical clock frequency, with error rate

**\[R26\] Cambridge University Press (2026), ARC physics basis collection** https://www.cambridge.org/core/journals/journal-of-plasma-physics/collections/arc-fusion-power-plant-physics-basis \| Collection of five peer-reviewed 2026 papers

**\[R27\] Atlas Lattice (2026), Beyond Q recovery draft PR \#36** https://github.com/atlaslattice/open-regenerative-compute-standard/pull/36 \| Unmerged draft; conditional recovered figures, not validation