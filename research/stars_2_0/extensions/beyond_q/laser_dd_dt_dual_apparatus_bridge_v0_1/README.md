# Laser / pulsed D–D → D–T dual-apparatus WarpX interface v0.1
**2026-10-30 · scenario prototype only · no WarpX PIC run / no experimental claim.**

## User-defined architecture (corrected and authoritative)
- **Apparatus A:** deuterium–deuterium primary fusion to generate **helium-3 and tritium** in two branches. Prioritize recoverable He-3 and tritium delivery, not necessarily A's net electric output. Acoustic/laser variants optional and physically separate from the earlier p–¹¹B hollow-sphere program.
- **Apparatus B:** deuterium–tritium fusion optimized for sustained usable electric output, using tritium recovered from A **plus a separately characterized B blanket breeding stream if required**; B must sustain its own fuel inventory. Do not assume that 'indefinite' follows from a closed flow drawing.
- Baseline reference A **20 MW primary D–D fusion power**, B **1.13 GW D–T fusion power**, both **hypothetical**. Never substitute 525 MW or 500 MW older proposals without explicit scenario naming.
- This is **two distinct physical apparatuses** with a material-transfer interface, not an assumed in-target secondary D–T burn. A's own secondary burn is separate and consumes tritium otherwise available for B.
- **Off-world architectural variants:** (1) two apparatuses for specialization/redundancy; (2) one reconfigurable or combined apparatus for mass-constrained lunar/Mars deployment; (3) one unit plus external imported tritium/fuel. A single vessel with two functions is not physically redundant; redundancy requires independent failure and common-mode analysis.
- Assess launch/landing dry mass, shielding (14.1 MeV DT neutrons), thermal rejection, energy storage/black start, helium-3 separation, tritium extraction/purification/delay, radiation safety, automation, spares, startup inventory, maintenance dose, reliability, lunar/Martian gravity, local D and Li availability. No implied 2035 operational feasibility.
## How to use
`python dual_apparatus.py reference_scenario.json`
`python -m unittest discover -p 'test_*.py'`
No external Python packages required; test locally before claims. Files are conceptual transfer interface and synthetic arithmetic, not an installed WarpX run.
## Fuel audit / falsification
B consumes one T atom per D–T reaction. A's D–D T branch produces one T per D–D T+p reaction, and the competing branch produces one He-3. This reference deliberately approximates constant branch fraction and mean D–D reaction energy, not energy-distribution-dependent cross-section integration.
At A=20 MW / B=1.13 GW and equal branches, ideal A T delivery supports ~4.3% of B demand. Thus **A alone cannot feed B indefinitely** at the preserved reference powers. An effective recovered breeding ratio near ~0.957 or greater would be required for steady-state atom balance *before other losses*; actual required production exceeds this due to losses, decay, startup/reserve and process delays. Breeding ratio here is an effective delivered T/reaction proxy, **not** an independently computed neutronic TBR.
A's 3He production is only gross generation, not recovered saleable isotope. Sim must add isotope separation, decay, burn-up, environmental/tritium control and internal resource/economic accounts.
## Work GPT with WarpX installed — execution order
1. Reproduce unmodified upstream WarpX D-D and D-T nuclear reaction examples on known version with quantitative energy/product conservation and reference cross-sections. Store exact commit, compiler, libraries, mesh, macro-particle weights, random seed, platform.
2. Add a *small* bounded laser-driven D-D target input based on upstream laser ion acceleration examples. Export D-D branch-resolved reactions, ion spectrum, power/shot and uncertainties. Do not use arbitrary 20 MW as PIC-observed output.
3. Simulate a **separate** D–T pulse/kinetic case as applicable; distinguish laser shot yield from continuously operated fusion power. Export DT burn rate/spectra. For sustainment, add confinement, neutron transport, thermal conversion and control solvers; WarpX alone does not prove steady 1.13 GW or stable operation.
4. Feed branch-resolved outputs into this interface in a new version. Integrate time-dependent inventory from existing `../tritium_self_sufficiency_audit_v1/`, including blanket neutron transport (e.g. OpenMC), extraction, delay/decay and losses; preserve G1–G5 research gates.
5. Compare terrestrial two-unit, off-world dual and single-apparatus variants on 50-year reliability, initial inventory, upmass and delivered power, resource extraction/sales and total lifecycle economic value. Output multiple Pareto objectives instead of treating negative electricity as disqualifying A.
6. Validate against independently measured D-D and D-T reaction results where comparable; do not promote solver runs to experimental validation.
## Provenance
Prior synthetic prototype `warpx_laser_dd_dt_bridge.zip` generated in a previous chat: its `bridge.py` models **secondary D–T reactions inside a D–D event population**, not the now clarified two-apparatus design. Do not treat that toy as the physical dual architecture; this folder is the corrected integration starting point. No physical hardware or partnership asserted.
