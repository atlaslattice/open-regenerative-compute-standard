# ORCS — Grid Intelligence 1.0: Dynamic Full-U.S.-Grid Modernization Architecture and 30-Year Screening Ledger

**2026-10-31 | National research design v0.1 | Public, non-operational | NOT deployed, utility certified, or investment-grade.**

**Scope:** The full interconnected U.S. electricity system—transmission, distribution, substations, 60–80M distribution transformers, distributed generation, storage, interconnection, residential/industrial service and large AI/quantum loads. Apply an *interoperability/measurement/optimization protocol nationwide*; fit physical sensors and controls **where site-specific engineering justifies them**, not one sensor on every asset or one centralized AI empowered to operate the grid.

Companion: [five-year transformer/panel mobilization, AI/human training, power quality](FIVE_YEAR_STANDARDIZATION_TRAINING_AND_POWER_CONDITIONING_2026-10-31.md); [reproducible five-year jobs/costs script](five_year_mobilization.py); [reproducible three-scenario Python model](national_grid_ai_scenarios.py); [national workforce and job-years addendum](WORKFORCE_AND_JOB_YEARS_2026-10-31.md); [Transformer 3.0 exploratory manufacturing RFQ](../manufacturing/TRANSFORMER_3_0_FULLY_ADDITIVE_SIC_SST_RFQ_COST_GATES_2026-10-31.md).

## 1. Verified national inputs and boundaries

- EIA 2025 retail electricity sales = **4,079.909 TWh** (published Oct 2026): https://www.eia.gov/electricity/annual/table.php?t=epa_01_01.html
- EIA 2025 electric meters = **169,808,072**; **147,093,020 advanced meters**, or **86.62%**: https://www.eia.gov/electricity/Annual/table.php?t=epa_10_05.html . Reuse existing smart metering; don't budget universal replacement.
- EIA 2025 **221.419 TWh “losses and unaccounted for”** includes balancing discrepancies, not purely physical transmission/distribution loss. Do not call it 221 TWh physically recoverable: https://www.eia.gov/electricity/annual/table.php?t=epa_01_03.html .
- ORNL March 2026 estimate: **~$67B average annual customer cost of major outages in 2018–24**; an economic burden, NOT accessible utility revenue or avoidable by software alone: https://www.ornl.gov/news/analysis-shows-power-outages-cost-us-electricity-customers-billions/
- Distribution transformer stock estimated at 60–80M, with heterogeneous types, ages and condition; a grid interface standard does **not** imply one physical 50 kVA design: https://www.energy.gov/cmei/buildings/distribution-transformers .
- IEA 2026 says dynamic line ratings on selected lines can provide ~20–30% local thermal headroom, dynamic transformer ratings ~5–15%, advanced power-flow control ~10–20%, topology optimization ~5–15% IN APPLICABLE SETTINGS; potential coverage and security constraints are not nationwide multipliers and benefits overlap: https://www.iea.org/reports/electricity-2026/grids ; https://www.iea.org/reports/modernising-grids-in-the-age-of-electricity/grid-enhancing-technologies .
- DOE 2024 Monitoring and Control Technologies Guide quotes examples: ADMS/DERMS software around $10.7–$20.9/account, FLISR $32.4/account, more complete projects $206.3–$280/account with varied scopes; reported devices $5–25k each, reclosers $10–80k each: https://www.energy.gov/sites/default/files/2024-11/111524_Monitoring_and_Control_Technologies.pdf . **These are not national bids.**

## 2. Integrated technical architecture

### Layer A: Provenance, national asset inventory and condition
National common schemas for transformers (kVA, impedance, age, losses, hot spots, overload and partial discharge), conductors (voltage, span, route/circuit miles, sag, ampacity, vegetation), substations, switches, interconnections, smart meters (privacy-limited aggregates), solar/storage and critical load centers. Data provenance includes calibration, timestamps, uncertainty, quality class, and operating authority. Utilities hold sensitive detailed maps; aggregated public dashboards exclude exploitable OT/critical infrastructure detail. GIS, satellite/LiDAR, UAV and field measurements reconcile unknown/erroneous network inventory.

### Layer B: Observability
Reuse AMI, SCADA, PMUs/WAMS, existing line and substation instrumentation. Add thermal/partial-discharge/condition and power-quality sensors only where justified by high risk, high failure consequence, grid congestion or lack of observability. Integrate wildfire weather and smoke cameras, vegetation change mapping and human-reviewed faults. Real-time data must flag stale/contradictory telemetry and fall back to deterministic conservative values.

### Layer C: Dynamic thermal and operating envelopes
- **DLR** dynamic conductor ampacity based on ambient temp, wind speed/direction, sun, precipitation, sag, clearance and thermal aging; can LOWER safe operating limits during heat, still weather or fire exposure.
- **DTR** dynamic transformer thermal and insulation-loss-of-life estimates by rated type, load, ambient/oil/hotspot temperatures and cooling state.
- **Topology optimization and advanced power-flow controllers** route flow away from congested paths only after full AC power flow, security constraints and N-1 contingencies. Do not assume transfer capability is equivalent to nameplate headroom; re-check adjacent transformer, breaker, bus and voltage/stability limits.
- **Voltage/VAR optimization** controls regulators, capacitor banks and inverters within mandatory service-quality limits. Voltage conservation is not “free power,” may reduce sales revenue, and must preserve end-use service.
- **Dynamic operating envelopes** for distributed solar/EV/battery/large flexible loads that preserve existing customer rights, privacy and consent, and incorporate non-firm agreements only where lawful and contracted.

### Layer D: Dispatch, storage and dynamic demand
Forecast weather, solar/wind, generator constraints, price, feeder loads, flexible industrial loads, water treatment, pumping, warehouse refrigeration, EV fleets, batteries and data-center compute workloads at 5-min to day-ahead intervals. State explicitly which loads are interruptible, flexibly deferrable, critical or protected. Optimize within customer contracts, ramp/energy limits, reserves, greenhouse impacts and emergency reliability. **Never assume AI can move a 24/7 data center's total electricity demand freely.** Flexible training batches, noncritical cooling pre-cooling, battery and demand response must demonstrate actual headroom.

### Layer E: Wildfire, extreme weather and resilience
Fuse risk-rated weather + asset condition + vegetation + historic utility-caused ignitions + local exposure + emergency access. Candidate mitigations are independent: conservative protective settings, switching/sectionalization, shutoffs where necessary, hardening, covered conductors, selected undergrounding, rerouting, vegetation work, microgrids and response preparation. Compare dollar spent against independently estimated incremental avoidable ignition and outage damage, lives, health and ecosystems, not historical total wildfire loss. No model may instruct an operator to keep unsafe lines energized merely to maximize transfer capacity. Wildfire wind may cool overhead lines for DLR while simultaneously increasing ignition consequences: **safety wildfire gate overrides thermal headroom**.

### Layer F: Human-governed cybersecure operation
Trust boundaries: monitoring AI -> read-only analytics -> advisory model -> authenticated human/qualified operator -> deterministic EMS/ADMS/DERMS and certified protection. Safety relays, frequency/voltage safeguards, islanding, fault clearing and manual emergency shutdown remain independently engineered and certified. OT network segmentation, model/telemetry tamper detection, signed changes, offline operation, fail-safe defaults, red-team drills, and NERC/utility-specific cybersecurity compliance. DOE is testing agentic AI in critical infrastructure with Stormbreaker; this is RESEARCH, not permission for unrestricted control: https://www.energy.gov/ceser/articles/ceser-releases-new-testbed-advance-llm-and-agentic-ai-evaluation-critical .

### Layer G: Commercial/customer/public benefit accounting
Separate: utility CAPEX and avoided grid replacement, provider electricity operating costs, customer bill effects, measurable outage damages, wildfire losses incremental to outage damages, interconnection times, customer demand savings, wholesale congestion/curtailment, data center capacity, and jobs/industrial manufacturing. Cancel transfers between electric utilities, ratepayers and data centers; do not count utility tariff receipts + avoided customer bills as two net social benefits. Ownership (IOU/public/cooperative) and financing (public, regulated, industrial share) are separately tested, not presupposed.

## 3. Operating cadence / decision authority

| Time scale | Recommended functions | Safety gate |
|---|---|---|
| Milliseconds | Certified existing protective relays / local inverter protection | Deterministic; AI cannot override |
| Seconds–minutes | Validated FLISR, inverter response, microgrid transitions, alarms | Pre-engineered interlocks, manual override and OT security |
| Every ~5–60 minutes | Thermal ratings, power-flow re-check, dynamic load envelopes, voltage optimization | Full network constraints and signed state estimation |
| Hourly/day-ahead | Generation + storage + demand forecasts, siting and dispatch proposals | Market/system operator review, customer contracts |
| Days/seasons | Weather, fire-risk protocols, inspection scheduling, vegetation and crew assignment | Fire safety/public authorities and engineering signoff |
| Years/decades | Reconductoring, undergrounding, transformer renewal, solar and datacenter expansion | Permits, public rate impact, competitive procurement, field commissioning |

IEA toolkit: https://www.iea.org/reports/modernising-grids-in-the-age-of-electricity/the-digital-grid-toolkit ; FERC transmission planning requires considering DLR, advanced power flow control, advanced conductors and transmission switching under Order 1920 for subject transmission providers: https://www.ferc.gov/explainer-transmission-planning-and-cost-allocation-final-rule .

## 4. Full-grid illustrative financial model (not a forecast)

Python [national_grid_ai_scenarios.py](national_grid_ai_scenarios.py) fixes **2025 baseline demand/AMI/losses**, then varies retrofit coverage, assumed effectiveness and costs. All values below are *illustrative screened sensitivities*, not utility quotes or demonstrated national intervention effectiveness.

**Incremental digital-grid CAPEX only**, separate from existing physical-transformer replacement, new transmission, solar capacity, hardening, undergrounding and land:
1. Distribution digital/automation/sensing system: 169.808M meters × $60 / $180 / $280 **per account** = $10.19B / $30.57B / $47.55B. The top tier aligns with a published single-utility full grid-modernization scope and is NOT its nation-wide transferable price.
2. Eligible transmission corridor proxy: **600,000 miles ASSUMED**, 5/10/15% targeted for GET deployment × $10k/$20k/$35k per equipped mile **ASSUMED** = $0.30B / $1.20B / $3.15B. Does **not** buy expensive high-voltage power controllers or reconductor all those lines.
3. Wildfire surveillance additional provision: $1B / $3B / $7B (invented scope allowances, not quotes).
4. National integration, training, simulations and OT cyber: $1B / $4B / $8B (invented scope allowances, do not overlap with distribution account spending).

**Benefit calculation and non-duplication:**
- CVR/VVO avoided consumption = 2025 retail kWh × enrolled fraction × measured energy-reduction fraction. Use assumed avoided **resource** value $0.08/kWh, not retail bill rate. This is reduced consumption, not utility generation or transformer losses; account for end-user service.
- Physical network-loss reduction = only a *subset* of EIA's “losses and unaccounted for” × improvement; model is explicitly overgenerous if EIA balancing discrepancies are counted as losses.
- Major customer outage impacts = ORNL $67B historical annual major-outage economic impact × assumed program-induced reduction. Do not add restored lost sales, customer backup costs or duplicate modeled outage harms.
- Non-outage wildfire damage = hypothetical additional *grid-ignition-attributable, net of outage damages* $3B/$3B/$5B per year × assumed reduction 3/10/20%. These $B values are unverified; suppress them if overlapping ORNL or other damage ledgers.
- No dollar credit yet for extra dynamic capacity, faster data center connection, reduced curtailment, GHG benefit, labor safety or postponed major lines: all require project-specific counterfactuals.

| Variable | Conservative | Reference | Upper sensitivity |
|---|---:|---:|---:|
| **Digital-grid initial capital** | **$12.49B** | **$38.77B** | **$65.70B** |
| Energy demand saved via VVO | 7.34 TWh/y | 22.85 TWh/y | 52.02 TWh/y |
| “Losses/unaccounted” recovered (conditional) | 2.21 TWh/y | 4.43 TWh/y | 10.63 TWh/y |
| Total avoided energy resource cost | $0.76B/y | $2.18B/y | $5.01B/y |
| Avoided modeled major outage harms | $0.67B/y | $2.68B/y | $5.36B/y |
| Avoided distinct non-outage fire harms | $0.09B/y | $0.30B/y | $1.00B/y |
| **Total illustrative annual public benefits at full rollout** | **$1.52B/y** | **$5.16B/y** | **$11.37B/y** |
| Annual digital-grid OPEX, 5% initial CAPEX | $0.62B/y | $1.94B/y | $3.28B/y |
| 30-y NPV, ten-year linear rollout incl. 35% refresh each decade, 5% discount | **−$2.56B** | **−$2.96B** | **+$25.39B** |

**Interpretation:** None is a validated prediction. The stronger NPV in the upper scenario arises from **assumed much greater nationwide program effectiveness**, not a “technology breakthrough” in the source evidence. Even the reference case is modestly negative using its own invented damages and avoidance assumptions, BEFORE physical construction and full implementation uncertainty. Full rollout in year one would also be unrealistic; code includes a 10-year staged roll-out and 10-/20-year technology refresh.

**Most important controls:** Network-wide GET capacity gains never become a national percentage power increase. A 20% DLR headroom on 10% of qualified line corridors is NOT 2% more total U.S. power. No revenue counted for unspecified data-center connection gains, and no software gets credit for averting every fire. Neither representative losses nor $67B historic major outage damage are available as unrestricted cash for financing.

## 5. Public procurement, DOE funding and mobilization

- SPARK selection intentions, announced Sep 24 2026: **$1.9B anticipated DOE + $3.35B recipients** = $5.25B selected projects, expected >1,500 reconductored/rebuilt line-miles and GETs on nearly 21,000 miles; **not completed or unrestricted**, and not subtractable from a generic national budget: https://www.energy.gov/oe/speed-power-through-accelerated-reconductoring-and-other-key-advanced-transmission-technology .
- DOE Grid SCALED announced Oct 30 2026: **up to $237M** prospective opportunities for grid-component refurbishment/reuse and supply alternatives. Concept papers due Nov 20; **not received project funding** and not new money to count twice with broader existing authorizations: https://www.energy.gov/articles/energy-department-announces-over-230-million-funding-opportunity-strengthen-americas-grid .
- Existing state/federal utility law and emergency authorities are heterogeneous; DPA designations can support qualified manufacturing priority or financing where conditions and appropriations are met but do **not** create a national utility command-and-control authority.
- Standard procurement protocol: measurable loss/quality limits, qualified interchangeable service parts, OT cyber, 20/30-year serviceability, multiple-source certifications, auditable deployed costs, open technical interfaces, vendor-neutral digital twins. Transformer 3.0 additive SiC SST remains a **separate experimental equipment track** until it beats conventional alternatives after full manufacturing and operating loss accounting.

## 6. Validation priorities

**G0 (evidence audit):** reconcile 2025 EIA, utility asset GIS/AMI census, line miles route vs circuit, condition and actual losses. **G1 (reproduce):** 100–1,000-feeder IEEE/OpenDSS/GridLAB-D scenarios + real anonymized utility feeder samples and SCADA/PMU schema. **G2 (grid physics):** AC load-flow, N-1, voltage, protection, dynamic ratings and thermal aging with withheld weather/contingency data. **G3 (field):** blind A/B or staggered rollout comparisons, avoided interruptions and calibrated VVO consumption; no equipment-control trial without utility/operator approval. **G4 (economics):** independent monthly measurement of saved MWh, adjusted wildfire damage risk, outage cost, incremental firm/non-firm interconnection MW, verified procurement and public bills. **G5 (scale):** safe human-controlled rollout, secured state/county non-sensitive aggregate dashboard and public traceability of procurement, deployment and outcomes.

**Immediate recommendation for analysis, NOT a political prescription:** run national interoperability/forecast/monitoring coverage everywhere, deploy additional physical controls to justified locations; prioritize high-hazard and congested corridors, existing AMI reuse, grid-wide reliability and low-risk digital capabilities before large new physical capital commitments. Model owner/operator and utility governance alternatives separately.

### Testable falsification rule

If actual utility validation finds no net attributable reduction in kWh, interruption impacts, ignition risks or incremental hosting capability, the claimed program benefits fail and must be removed—regardless of impressive AI simulation accuracy. No autonomous AI electrical protection, no unfunded national savings claim, and no bundling unvalidated fusion as firm grid supply.
