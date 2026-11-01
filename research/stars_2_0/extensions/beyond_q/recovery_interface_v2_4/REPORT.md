# Beyond Q v2.4: recovery interfaces, precursor audit and unresolved calibration

2026-11-01. Parent commit `3b5cfe43513f51dd65321ee40d0fd5109a5b5710`. This directory adds a research interface without modifying prior releases. The current A 1100 MW primary-DD and B 1100 MW DT scenarios, explicit 1130 MW B comparator, 37.5/75/90% overall recovery cases and external successor financing remain unchanged.

## Outcome

We obtained and inspected a distinct 1980 CoSCD precursor report, but not the full 1982 Greenspan–Miley journal paper. Consequently the 1982 plasma-recovery benchmark is **not reproduced**, and physical calibration stays disabled. We implemented a positive, conservative dynamic recovery-stage interface and ran five diagnostic cases plus negative controls, refinement and an independent integrator comparison. These establish software behavior under assumed inputs, not reactor performance.

## Source acquisition and the precursor's accounting boundary

**SOURCE-TRACED:** *Semi-catalyzed deuterium reactors for co-generation of 3He and synfuels (the CoSCD concept)*, report COO-2218-190, 1980, DOI [10.2172/6712040](https://doi.org/10.2172/6712040). [DOE PDF](https://www.osti.gov/servlets/purl/6712040); [UNT catalog](https://digital.library.unt.edu/ark:/67531/metadc1186582/). UNT leaves authors unidentified; the Wisconsin historical bibliography attributes the report to Greenspan and Miley. The downloaded scan has 11 PDF pages, including inserted disclaimers, versus the catalog's nine-page description. Figures were checked visually after OCR.

The reaction illustration (PDF p.6, printed p.4) combines two primary DD events and one secondary DT event, using rounded energies 3.2 + 4.0 + 17.6 = 24.8 MeV. It consumes the illustrated DD-born T internally, leaving none for external B in that example. The energy diagram (PDF p.7) displays 7.4 and 4.5 output energies alongside a 74%/26% split. Direct normalization gives 62.18%/37.82%; missing weighting or boundary remains **UNRESOLVED**, visibly flagged in `outputs/precursor_arithmetic.json`. We retain the source claim rather than fit to it. This checks conceptual arithmetic, not plasma recovery.

The 1982 journal PDF returned HTTP403 through direct retrieval; publisher full-text and ANS routes were also inaccessible through the web tool. Its accessible abstract is still the evidence for study-specific approximately70/80% plasma recovery, not downstream equipment yields. DOI [10.13182/FST82-A20733](https://doi.org/10.13182/FST82-A20733). No operating-point tables or equations sufficient to reproduce that paper were obtained. The precursor must not be presented as an equivalent full-text substitute.

## Explicit recovery-state equations

Amounts are moles of He3 and time is days. For plasma \(x_p\), pump-side collection inventory \(x_c\), purification inventory \(x_u\) and product-candidate storage \(x_s\):

\[
\dot x_p=S_3-(k_b+k_e)x_p,\quad
\dot x_c=e\,k_e x_p-k_c x_c,
\]
\[
\dot x_u=c\,k_c x_c-k_u x_u,\quad
\dot x_s=p\,k_u x_u.
\]

Here \(k_b\) represents secondary D-He3 consumption, \(k_e\) exhaust, \(k_c\) collection/regeneration release and \(k_u\) purification release. All have units day^-1. Conditional fractions \(e,c,p\) are dimensionless and apply to their incoming streams, once. The model does not derive these rates from plasma temperature, confinement or measured apparatus. It uses competing first-order hazards as a replaceable interface approximation. Source and burn turn off during source outages; pump and purifier have independent outage schedules. Plasma exhaust can continue after source shutdown.

Permanent removed amounts accumulate as

\[
\dot B=k_bx_p,\quad \dot L_e=(1-e)k_ex_p,\quad
\dot L_c=(1-c)k_cx_c,\quad \dot L_u=(1-p)k_ux_u.
\]

With zero initial stock, the independently checkable identity is

\[
\int S_3dt=x_p+x_c+x_u+x_s+B+L_e+L_c+L_u.
\]

Internal cumulative flow counters are diagnostic and must not be added again to the right side. Pump-off material remains inventory until release. Each mole of secondary He3 consumption requires one mole D and creates one mole He4 plus one mole protons under the stipulated D-He3 reaction. `DHe3_reactions_mol`, `additional_deuterium_consumed_mol` and `additional_He4_born_mol` explicitly record those counts. They are not three independent sources of material or revenue. Proton/energy transport and deposited heat are not modeled; `energy_J=null`. He4 birth does not establish He4 capture or purity.

The source interface is He3 mol/day. The diagnostic feed uses v2.3's 938967.9947 STP L/year at85% effective exposure, divided by22.414 L/mol and365.25 days, supplied continuously as an average. An adverse source-off window is an additional reduction. This is separate from the parent85% macro-availability ×93.75% source-duty schedule. No source power, uptime or primary reaction rate is silently changed in the parent.

## What the diagnostic cases show

All stage parameters below are **ASSUMED**, and resulting scenarios are **POTENTIAL-DERIVED**. The base hazard ratio imposes plasma survival \(k_e/(k_e+k_b)=0.70\); it does not reproduce the historical study. Exhaust delivery0.90, capture/regeneration0.90 and purification yield0.95 give asymptotic overall0.53865. Transient inventories reduce the first year's delivered amount.

| Diagnostic case | First-year product-candidate STP L | Meaning |
|---|---:|---|
| Imposed70% plasma survival, illustrative downstream stages | 503075 | Conditional response, not calibrated output |
| Secondary He3 consumption disabled | 718085 | Tests the cost of the imposed burn hazard |
| Zero pump capture | 0 | No product despite unchanged birth |
| Pump stopped days180–210 | 503075 | Material is delayed, then released in this idealized system |
| Source and pump stopped days180–210 | 461948 | Additional lost source exposure lowers annual product |

The pump-only outage's similar year-end product is **not** evidence that a real pump outage is harmless. This model has unbounded retention capacity, no pressure feedback, no saturation, no contamination-driven rejection and no permanent loss during stoppage. Its peak pump inventory rises from approximately72.3 to2185.8 mol in that case. Those missing capacity and pressure constraints must be resolved before sizing equipment or feeding this response into a plant-operability forecast.

Qualified product is unknown (`null`) in every case. No buyer assay thresholds, tritium contamination guarantee, commercial sales or updated cash flows are inferred.

## Overall targets versus plasma survival

For any fixed survival scenario, required downstream yield is \(r_{overall}/s_{plasma}\). This is **VERIFIED-DERIVED conditional arithmetic**:

| Imposed plasma survival | Required for37.5% overall | Required for75% overall | Required for90% overall |
|---|---:|---:|---:|
| 70% | 53.57% | 107.14%: infeasible | 128.57%: infeasible |
| 80% | 46.88% | 93.75% | 112.5%: infeasible |
| 100% | 37.5% | 75% | 90% |

These are scenario bounds, not universal plasma limits. The historical70/80% figures cannot be imported as universally applicable values. The parent37.5% is still a conservative-potential assumption, not an evidence-supported minimum. The parent overall recovery already includes lumped unresolved losses; multiplying it by this explicit chain would double-apply losses unless the scenario boundary is deliberately replaced and versioned.

## Numerical execution and audit

Each scalar compartment uses the analytic constant-source/hazard update, with `expm1` and a small-rate series. This avoids negative stocks under stiff removal rates. Coupling substitutes step-averaged upstream flow, so the coupled transient remains approximate and requires refinement. The annual constant-source result is already near steady flow and shows roundoff-level variation on refinement; that is not a sufficient convergence test by itself.

An initial test incorrectly required strictly decreasing annual steady-state differences when both differences were at floating-point roundoff. That assertion failed visibly and was replaced with a short transient comparison; the failure and correction are preserved in `AUDIT_HISTORY.jsonl`. At one day, successive timestep differences decrease by approximately4x. A separate fourth-order Runge–Kutta coupled ODE estimator confirms the refined transient within0.1% for the test case. Neither solver assumes the historical plasma solution has been reproduced.

**Eleven software checks pass**, including zero source, zero capture, disabled secondary consumption, pump-stop holdup, no double delivery of burned atoms, nonnegative stiff-rate evolution, target-bound feasibility, transient refinement and independent integration. Across five annual cases, maximum He3 atom-equivalent ledger residual is below7.2e-10 mol. Raw stage CSVs, JSON states and execution hashes are provided. The historical74/26 arithmetic check remains visibly `FAIL_UNRECONCILED_AT_DISPLAYED_OUTPUT_BOUNDARY`, separately from passing software tests.

## Remaining work and integration contract

The next required evidence is the full1982 numerical model or another fully specified contemporary plasma benchmark. Extract its reaction network, energy boundary, profiles, confinement, residence losses and uncertainty before calibrating \(k_b,k_e\). A hazard ratio chosen to equal70% is not such calibration.

For equipment, obtain species-resolved exhaust feed, inlet pressure/temperature, conductance, sorbent capacity, measured regeneration yield, cross-contamination, cycling degradation, purification recovery, energy draw and product assay requirements. Helion's publications and ARC's preliminary exhaust work remain process/interface references from v2.3, not numerical efficiency assignments here.

Before connecting staged outputs to the integrated plant model, replace the parent's lumped He3 pipeline and recovery boundary in a new version; do not append a second pipeline or add secondary products twice. Include D-He3 reaction energy once in the full reaction ledger, then reconcile wall-plug draw and thermal deposition. Re-run finance and cascade only after that boundary is established. No financial or self-sufficiency change is claimed from this diagnostic module.

G1–G5 remain **OPEN**. No new WarpX/OpenMC execution occurred. Source arithmetic, code conservation, physical calibration, qualified product and operational self-sufficiency remain distinct.

Dave / Atlas Lattice originated the isotope-first dual-reactor direction. GPT Work performed source acquisition, visual checks, implementation and execution. Earlier GPT-6/Tidal Lantern, DeepSeek and Gemini Argon analyses retain their documented credits. Published authors and developers receive credit for their own work; no institutional or experimental endorsement is implied.
