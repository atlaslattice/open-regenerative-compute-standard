# Beyond Q / STARS 2.0 — DIII-D helicon RF current-drive evidence and Reactor B work order

**Date:** 2026-11-01  
**Evidence:** SOURCE-TRACED experimental result; **NOT** a validated ARC current-drive performance or a net-electric gain.  
**Scope:** D-T Reactor B (canonical target ~1.13 GW fusion output) as an **optional** non-inductive current-drive candidate. Preserve all earlier ARC and D-D Reactor A baselines.

## Primary experimental evidence

Lestz et al., **"First Experimental Evidence of Helicon Current Drive,"** *Physical Review Letters* **137, 155101**, published **9 October 2026**, DOI **10.1103/mbn4-fd4v**: https://journals.aps.org/prl/abstract/10.1103/mbn4-fd4v

The paper reports dedicated DIII-D tokamak experiments using a **megawatt-level helicon RF system** and a traveling-wave antenna. Researchers observed core power deposition and evidence for **helicon-driven plasma current**. Electron-temperature response was consistent with time-dependent integrated modeling with ray tracing and thermal transport. Continuous helicon co-current injection produced faster safety-factor-profile flattening and earlier sawtooth onset than comparison shots using comparable electron-cyclotron heating. Reconstructed current-drive profiles were core-peaked, consistent with deposition and ray tracing.

**What was demonstrated:** proof-of-principle auxiliary current drive in DIII-D.  
**Not demonstrated:** reactor-scale current-drive efficiency, a complete self-sustaining tokamak, ARC hardware compatibility, favorable commercial wall-plug net electricity, unchanged transport/confinement, or economic payback. Heating, current drive and plasma stability interact and must be co-modeled.

## How to integrate without altering canon

Maintain Reactor A **D-D 1.10 GW fusion-power target**, Reactor B **D-T 1.13 GW fusion-power reference**, B lithium breeding approximately covering *its own* tritium use subject to audited mass-balance; A is the external helium-3/tritium source. The helicon paper does not measure the fuel-cycle, byproduct, thermal-conversion, neutron-transport or tritium inventory quantities.

Add an **HCD module** as a new candidate under *Reactor B auxiliary loads / current drive*, alongside existing RF/ECCD/NBI/other baseline options. Do **not** replace an existing current-drive technology in ARC's published design without a credible validated compatibility study.

Required modeled fields, with status **ASSUMED** until calibrated:
- `P_HCD_RF_coupled_MW`, `eta_RF_source`, `eta_transmission_matching`, `eta_antenna_plasma_coupling`, `P_HCD_wall_MW`; define each denominator consistently and avoid double-counting ancillary RF loads.
- `eta_CD_A_per_W` or suitable normalized `gamma_CD` with geometry and density/temperature dependencies; `I_CD_MA` and central versus off-axis current-drive spatial profiles.
- `P_other_CD_MW`, `P_ECRH_MW`, `P_ion_heating_MW`, `P_magnets_MW`, `P_cryo_MW`, `P_vacuum_MW`, `P_controls_MW`, `P_pumps_MW`, steady-state `P_aux_total_MW`.
- `f_noninductive`, bootstrap fraction, plasma current target, q-profile constraints, sawtooth/instability impacts, and reactor operations/duty-cycle compatibility.
- Net electric: `P_net_e = P_turbine_gross - P_aux_total - P_BOP_other` with consistent thermal recovery/conversion and clear wall-plug boundary. RF power deposited in plasma is **not** interchangeable with electric draw at the grid.
- Costs and feasibility: per-MW RF system capital, reliability, maintenance/replacement, antennas and port constraints, component radiation life, spare inventory, controls and availability.

## Experiments and independent validation work order

1. **Literature evidence intake:** acquire paper's numerical experimental tables, supplementary data and apparatus parameters (RF frequency, injected source MW, coupled power, antenna geometry, plasma profiles, diagnostics, estimated driven current and model uncertainties); quote exact values only after reviewing full text/appendices.
2. **Baseline before replacement:** identify ARC's currently published current-drive scheme, its actual auxiliary loads and system boundaries. Preserve source/version/date. Distinguish original ARC assumptions from Beyond Q design variants.
3. **Constrained scenario sweep:** zero-helicon baseline vs conservative vs optimistic helicon branch. Sweep RF conversion and coupling; current-drive efficiency; bootstrap fraction; transport/stability penalty; installed CAPEX; availability. No fixed default 70% wall-plug efficiency merely because it was once proposed.
4. **Calibration:** forward-compare RF power deposition, current profile, q evolution and heating with public DIII-D data. Preserve uncertainty and model discrepancy. WarpX may be used for appropriate kinetic wave-particle studies if geometry/frequency/regime permits, but **do not claim a direct WarpX-to-whole-tokamak validation**. Couple to suitable RF ray/full-wave + transport/equilibrium/MHD models before plant-scale claims. OpenMC still handles independent neutron transport and tritium accounting; no claim that it validates helicon current drive.
5. **Go/no-go criteria:** report measured/credible current driven per wall-plug watt, reactor-relevant transport/stability, incremental net-electric benefit with uncertainty, CAPEX/availability, safety and compatibility. *If there is no robust modeled improvement under source-bounded uncertainty, retain the prior baseline*.
6. **Provenance:** input/assumption/data-source matrix, run settings, software versions, validation residuals, credible bands, full reproducible artifacts and independently reviewed conclusions. Evidence gates: SOURCE-TRACED -> SOURCE-REPRODUCED -> CALIBRATED -> VALIDATED only with corresponding evidence.

## Requested handoff to GPT Work / current STARS/Beyond Q thread

> **New November 1 literature delta:** Add Lestz et al., Phys. Rev. Lett. 137, 155101 (2026), DOI 10.1103/mbn4-fd4v, *First Experimental Evidence of Helicon Current Drive* to the source register. DIII-D has observed RF helicon current drive with a MW-level traveling-wave antenna; it is not ARC-validated and has no demonstrated full-reactor wall-plug or net-power benefit. Introduce an OPTIONAL Reactor B helicon RF current-drive branch into the auxiliary electric load and q-profile accounts, preserving the canonical 1.13 GW D-T fusion-power reference and all isotope/tritium ledgers. First recover actual DIII-D paper parameters and public ARC current-drive requirements; then benchmark coupled RF, conversion efficiency, wave/current drive, stability and costs against the existing baseline with uncertainty gates. Keep Reactor A D-D 1.10 GW separate. No invented RF efficiency, endorsement or net-power claim.**

## Provenance and cross-references

- Primary: https://doi.org/10.1103/mbn4-fd4v
- Journal issue: https://journals.aps.org/prl/issues/137/15
- Existing ARC dual reactor baseline: [ARC_DUAL_REACTOR_CANONICAL_BASELINE_2026-10-31.md](ARC_DUAL_REACTOR_CANONICAL_BASELINE_2026-10-31.md)
- Program start: [GPTWORK_START_HERE_STARS_2_0.md](../../../../GPTWORK_START_HERE_STARS_2_0.md)

*This is an evidence-intake/work-order artifact, not a claim the experiment was numerically reproduced or integrated into production solver code.*