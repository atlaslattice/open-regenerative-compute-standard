# Beyond Q — Moon/Mars Closed-Loop Habitat Testbed Mission & Dual-Objective Ledger
**v0.1 | 2026-10-30 | PROPOSED DESIGN MISSION, not demonstrated space-habitat capability or approved grant**
**Provenance:** Author's Oct 30 proposal: the terrestrial Beyond Q campus should explicitly function as a Moon/Mars long-duration habitat analog; in-situ food, water, gas and thermal loops serve both terrestrial and 20-year habitat R&D objectives. Extends [bioreactor thermal integration](BQ_INTEGRATED_BIOREACTOR_THERMAL_GAS_CIRCULARITY_DESIGN_NOTE_2026-10-30.md) and [Nightmare Lab](../safety/BQ_NIGHTMARE_LAB_PROTOCOL_v0_1.md). No changes to underlying fusion/quantum model, code, capital assumptions or reactor baselines.

## 1. Programmatic reframing
Beyond Q remains a terrestrial dual-reactor / compute campus concept, with a proposed **separable Moon and Mars habitat systems testbed mission**. The testbed does not require pretending the campus is literally on the Moon/Mars or changing its core physics. Study how the same on-site bioreactor, wastewater, desalination, heat and gas systems behave under controlled scarcity, isolation and resupply constraints.

**Two independently audited objective functions:**
(A) terrestrial delivered products and service economics, including reliability and environmental performance;
(B) testbed research value, maturity, reproducibility, data rights, transferability, operational learning and reduced future uncertainty for extraterrestrial habitats.

A subsystem can be uneconomic for (A) yet worth funding for (B), but only with explicit research sponsors/commitments, research milestones, and a defensible incremental cost ledger. The same dollar benefit cannot be counted twice.

## 2. Nightmare Lab response template
**Challenge:** Why build expensive local food and water loops rather than import established products at lower cost?
**Defensible answer:** We have a separate, explicit long-horizon Moon/Mars habitat analog objective. The incremental premium is budgeted to an R&D work package, and the research outputs are independently scored against predefined closure, safety, autonomous operation and resupply benchmarks. If the research outcomes underperform or the financing does not materialize, the terrestrial-only case must stand on its own or the experimental module must be downsized/removed.
**Disallowed answer:** It is obviously safer/cheaper/inherently sustainable because it is closed loop.

## 3. Reference configurations
T0 = conventional externally supplied terrestrial food/water/gases with compliant waste treatment and safe vents.
T1 = existing campus with heat recovery, high-efficiency water treatment and measured emissions.
T2 = segregated experimental food bioreactors, nutrient recovery, gas capture, reject-heat cascade and modular water-recycling systems.
T3 = habitat-constrained testing: simulated limited resupply, limited spare parts, multi-week isolation, resource inventory and automation; fail-safe vents/relief maintained.
T4 = distinct Moon- and Mars-targeted environment replication/validation campaigns. Earth analog performance must not be relabeled as verified lunar/Martian operation.

## 4. Mass/energy/safety accounting
For each stream i, use time-indexed mass closure:
inventory_i(t+Δt) = inventory_i(t) + imports_i + regenerated_i - consumed_i - exported_product_i - treated_discharge_i - loss_i.
**Closure fraction** is defined per water, carbon, nitrogen, phosphorus, oxygen and key trace nutrients; distinguish recirculation from genuine recovery and external replenishment.
Thermal exergy and energy balances must account for reactor/compute reject heat, bioreactor metabolic heat, sterilization loads, heat pump work, radiator or terrestrial heat rejection, and process cooling. A bioreactor can generate net heat and need cooling; never assert generic 30–37 C jacket heating offsets large fractions of campus waste heat.
Compare electricity, consumables, emergency reserves, labor, maintenance frequency, contamination, isolation time, environmental release, redundancy and consumable purity.

## 5. 'No vent / no discharge' as research discipline, not safety prohibition
Target **zero uncontrolled routine venting/discharge and maximum feasible capture, monitored treatment and reuse**. Do not prevent pressure relief, fire safety, radiological/chemical containment, oxygen management, or emergency isolation. 'Closed loop' must be quantified and never mean literally zero inevitable entropy generation, zero external heat rejection, or zero material loss.
The Moon and Mars require heat rejection to their environment (e.g., radiators), which is not equivalent to discharging liquid process waste; reject heat remains unavoidable.

## 6. Twenty-year roadmap (illustrative, not schedule commitment)
Years 0–3: process baselines, hazards, physics-grounded digital twin, instrumented modular test rigs, reproducible balances.
Years 3–7: pilot bioreactors, quality assurance, water/gas recycling, monitored nominal and fault cases.
Years 7–12: long-duration closure and maintenance demonstrations, limited-resupply campaigns, contamination isolation and cross-training.
Years 12–16: environment-specific subsystem design reviews for lunar gravity/vacuum/radiation/dust and Mars low gravity/atmosphere/dust; validate engineering portability with independent expert testing.
Years 16–20: integrated life-support analog demonstrations and partners' evaluation for space-environment test missions; no claim of flight readiness without applicable testing and certification.
Long-horizon mission deliverables must be versioned and stoppable at review gates.

## 7. Space-specific invalid assumptions to audit
- Earth gravity ≠ 1/6 g lunar gravity or ~0.38 g Mars.
- Earth radiological shielding, natural convection, atmospheric pressure and dust are not representative.
- Space economics weight transported mass, reliability, local regolith chemistry, power-storage autonomy and repairability much more heavily than Earth commodity prices.
- Different feedwater and resource deposits mean seawater desalination on Earth is at best a systems analog; actual Moon/Mars feedstocks require mineral/ice extraction and purification models.
- Local bioreactors need dedicated food-quality, containment and biosecurity review; reactor-side tritium/FLiBe and food-product systems must remain physically segregated.

## 8. Funding and governance
Potential sponsor classes to research: space life-support R&D, lunar/Martian ISRU programs, industrial biomanufacturing and water-treatment partners, energy/compute infrastructure research, and resilience technology programs. **No specific funding source, contract, award, revenue or grant eligibility is asserted by this document.**
Use ring-fenced cost centers, sponsor-specific rights and data deliverables, independent milestones, reproducible experimental protocols, public/partner-safe reporting and strict conflict-of-interest treatment.
Do not include grant income in the base case without an actual award; use grant/funding scenarios as optional sensitivities.

## 9. Canon and research boundaries
Iron Empire may dramatize advanced habitat-building and food autonomy as **future fictional extrapolation**. This document is a real-world project proposal, not technical validation of extraterrestrial settlement or a locked fiction scene.
Retain Beyond Q fuel-cycle baseline: Reactor B 1.13 GW D-T fusion, Reactor A hypothetical 20 MW primary D-D reference. Existing site plans, physics and numerical scenario baselines unchanged.

## Next deliverables
1. Dual-objective balance sheet (terrestrial margin vs independently funded habitat testbed research value).
2. Instrumentation plan for water/air/nutrient/heat closure and uptime.
3. Nightmare Lab adversarial failure suite: blocked exhaust, oxygen failure, CO2 accumulation, contaminated culture, source heat loss, sensor failure and simultaneous resupply interruption.
4. Earth analog vs Moon vs Mars transferability matrix with 'not demonstrated' markers.
5. Funding eligibility survey and research partner outreach only after specific program confirmation.

**Design invariant:** Expensive in-situ pathways may be justified by explicitly priced, independently reviewed habitat learning—not by hiding their costs in an ordinary industrial profit estimate.
