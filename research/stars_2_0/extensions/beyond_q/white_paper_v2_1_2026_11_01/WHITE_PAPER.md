# Beyond Q: An Isotope-First Dual-Reactor Module and Fuel-Supported Expansion

## White paper v2.1 — research consolidation, November 1, 2026

**Atlas Lattice / STARS 2.0 / Stellar Forge / Nightmare Lab**

**Status:** source-bounded computational research. This paper consolidates the day's review, software execution, economic sensitivities and originator decisions. The executed implementation is v2.0, with disclosure/reconciliation v2.0.1. The proposed fuel-triggered expansion controller is specified here but has NOT been executed. No operational or experimental self-sufficiency is claimed. All physical research gates G1–G5 remain open.

**Research direction:** Dave / Atlas Lattice. **Computational implementation and reconciliation:** GPT Work. **Documented analytical contributions:** GPT-6 / Tidal Lantern, DeepSeek and Gemini Argon, attributed below according to their roles. No cited author, laboratory, university, company or institution is represented as endorsing this architecture.

## Abstract

Beyond Q studies a proposed dual-reactor module whose first product is usable isotopes and whose second product is available electricity. Reactor A is a hypothetical 1.10 GW primary D-D isotope factory; Reactor B is a D-T electricity generator with its own lithium-breeding blanket. The default matched-power computational case uses 1.10 GW for B, while retaining an explicit 1.13 GW public-ARC reference. The proposed system is not contingent on building a quantum computing campus. GPU and QPU equipment, financing and compute revenues are outside the module boundary.

Today's work distinguishes isotope birth, internal consumption, recovery, qualification, allocation, inventory value and cash sales; examines existing helium-exhaust and separation equipment; and connects time-dependent inventories to reactor-only financing. Executed 60-year scenarios cover one module and a staged 50-module fleet, with overall He3 recovery sensitivities of 37.5%, 75% and 90%. They preserve explicit decay, losses, startup stocks, donor-bounded transfers and conditional exports. Numerical checks establish accounting consistency, not reactor validity.

The originator's latest operating policy removes mandatory He3 retention for standalone/GPU-hosted modules. A zero-retention financial recalculation gives positive coverage of currently priced debt and electricity imports in years 1 and 2 under the assumed product prices; complete cost and qualified-sales evidence remain missing. Existing fixed-calendar fleet results are not the intended deployment strategy. The decisive new specification is a fuel-supported cascade: each new campus has separate external project financing, while eligible operating predecessors pool uncommitted tritium to supply the new startup. Fuel availability can accelerate with the number of productive modules, but construction, financing, qualification, reserves and demonstrated sustainability remain independent constraints.

## 1. Purpose, architecture and boundaries

The design objective is a modular industrial system producing harvestable He3, tritium and He4 while sustaining its own fuel cycle and, if the electrical balance permits, exporting net electricity. A host campus can consume those outputs without becoming part of the reactor module's financial model. An existing GPU campus, a future hybrid QPU/GPU campus, a standalone isotope customer and the grid are different possible customers; none is required to establish the module's basic isotope ledger.

| Boundary | Included | Excluded or unresolved |
|---|---|---|
| Reactor A | Proposed 1,100 MW primary D-D fusion; direct T/He3 births; candidate secondary DT consumption; processing and electrical-load sensitivity | Demonstrated DD operating point, driver/confinement solution, mechanistic He3 transport and D-He3 consumption |
| Reactor B | Default 1,100 MW DT; explicit 1,130 MW option; own blanket breeding; extraction, consumption and recycle | Exact source-qualified ARC blanket yield and operational breeding/recovery performance |
| Module facilities | Reactor A and B buildings/site scope, isotope train, common services, heat rejection, maintenance and reserves | Unpriced installed scope and validated footprint |
| Finances | Reactor/isotope capital, own financing, material sales sensitivities and electrical exchanges | GPU/QPU capital, financing, computing configuration and computing revenue |
| Fleet | Separate campus stocks, startup and independent project financing; future fuel-pooling controller | A completed deployment forecast or demonstrated exponential expansion |

Do not confuse A's historical **+20 MWe NET projection**, which remains unvalidated, with a 20 MW fusion source. Older 20 MW primary-DD and 525 MW ARC cases are historical research artifacts, not silent substitutes for the active full-size proposal. A 1.10 GW DD operating point is not established merely by adapting a published DT design.

Public CFS material describes approximately 400 MWe from ARC [1]. The executed screen inherits a 500 MWe gross / 100 MWe own-load comparator at 1,130 MW fusion, scales the gross term to configured B power and actual served burn, and keeps A's net electrical balance separate. This is a modeling convention, not an independently demonstrated plant balance.

The lithium-breeding configuration requires consumed lithium feedstock as well as deuterium. It also requires coolant, processing materials, replacement components, maintenance and heat rejection. The meaningful long-term aspiration is autonomy from continuing external tritium purchases plus positive available energy and products—not an immortal plant requiring deuterium alone.

## 2. Evidence discipline and numerical conventions

| Label | Meaning in this paper |
|---|---|
| SOURCE-TRACED | An identifiable publication, patent, announcement or prior artifact supports the stated provenance; this does not validate its transfer to Beyond Q |
| VERIFIED-DERIVED | Arithmetic or a conservation identity independently checked under explicit conventions |
| POTENTIAL-DERIVED | A computed scenario depending on assumed performance or operating conditions |
| UNRESOLVED | Physical validation, missing parameters, missing cost, qualification or unsupported transfer of a result |

One FPY is 365.25 days = 31,557,600 seconds. SI conversions use 1 eV = 1.602176634e-19 J and Avogadro's constant 6.02214076e23 mol^-1. Isotope molar masses are T 0.00301604928 kg/mol, He3 0.0030160293201 kg/mol and He4 0.00400260325413 kg/mol. Gas-volume reporting uses 0 C and 1 atm with 22.414 L/mol.

**Tritium atom-equivalent liters are not molecular T2 liters.** At equal atom count, gaseous T2 occupies half the volume of monatomic He3. The historical 350k/350k comparison must retain its declared basis. Approximately 350,000 He3 STP L corresponds to 47.096 kg; 350,000 T atom-equivalent L also corresponds to approximately 47.096 kg T, whereas 350,000 molecular T2 L requires approximately 94.193 kg T.

## 3. Nuclear birth and consumption accounting

The screening convention takes equal DD branches:

\[
D+D\rightarrow T+p+4.03\;\mathrm{MeV},\qquad
D+D\rightarrow{}^3He+n+3.27\;\mathrm{MeV}.
\]

The mean is 3.65 MeV per primary reaction under that assumption. Thus:

\[
R_{DD}=P_{DD}/\overline E_{DD},\quad
R_{T,A}=R_{He3,A}=R_{DD}/2,\quad R_{n,DD}=R_{He3,A}.
\]

Equal branching is a scenario convention, not a claim that every actual plasma distribution has exactly equal branches. The old factor-of-two neutron error is avoided by counting primary DD neutrons only in the neutron-producing branch. Historical swapped branch-energy labels in v2.3 did not change the equal-branch mean, but did affect unequal-branch weighting; current physics code uses the correct assignment.

DT consumes one T nucleus per reaction and produces one He4 nucleus and one neutron. With Q_DT=17.6 MeV, the first-principles consumption factor is:

\[
c_T=\frac{10^9\,t_{FPY}}{17.6\times10^6 e}\frac{M_T}{N_A}
\simeq56.049\;\mathrm{kg/(GW_{fusion}\,FPY)}.
\]

The historical 55.8 kg convention remains documented, not silently substituted. At 1.10 GW, uninterrupted DT burn is approximately 61.654 kg/FPY. The executed source duty and outages determine actual calendar-year burn.

At hypothetical continuous 1.10 GW primary DD, direct T and He3 births are each approximately 148.6 kg/FPY. The He3 source is approximately 1.105 million STP L/FPY. At 85% **effective fusion exposure**, it is approximately 938,968 L/year; recovering 350k requires approximately 37.27% overall recovery under those conditions. If 85% instead means macro availability before a separate 15/16 pulse duty, gross source exposure is lower. The distinction must not be hidden or counted twice.

Candidate secondary T burn is derived from a birth/burn/escape model, not fixed as an independent 18 MW source. In its simplest form, Argon's proposed expression is:

\[
f_{burn}=f_{fast}+(1-f_{fast})\frac{n_D\langle\sigma v\rangle\tau_T}{1+n_D\langle\sigma v\rangle\tau_T}.
\]

The product n_D<sigma v>tau is dimensionless. The inherited implementation additionally accounts for a separate prompt escape fraction, so the remaining thermal pool is 1-f_fast-f_fast_escape. Stoichiometric closure does not prove the assumed confinement, slowing-down or reaction rates. D-He3 secondary consumption remains unresolved and cannot be inferred from a lumped recovery loss.

Earlier short WarpX collision experiments are useful microscopic accounting benchmarks, not full ARC or laser-target demonstrations. A picosecond sample and its particle-weight closure do not establish long-residence burn fraction, whole-plant gain, a unique neutron spectrum or an eight-hour operating point. A numerical discrepancy between estimators needs uncertainty analysis rather than being labeled either validation or failure. No new WarpX/OpenMC run was performed in this day's module/fleet consolidation.

## 4. Recovery mechanism: existing designs before new invention

Direct DD He3 originates in the plasma. Its principal candidate recovery path is plasma exhaust and downstream processing. The lithium blanket is a separate neutron-driven tritium source; it is not the principal collector of plasma-born He3.

The candidate functional chain is:

**Plasma survival/escape → divertor exhaust → fuel/helium separation → helium capture and regeneration → detritiation and purification → He3/He4 separation as needed → assay and storage.**

A metal-foil pump selectively permeates hydrogen isotopes; helium remains on the feed/residual side and needs its own controlled handling path. Helium collection at fusion vacuum conditions can use charcoal cryosorption, rather than ordinary fuel condensation. The process configuration may combine these functions differently; a metal-foil stage and a staged cryopump are not automatically mandatory series equipment.

| Candidate | Traceable evidence | Integration judgment |
|---|---|---|
| ASIPP/Hefei composite cryopump | Official April 21, 2025 prototype announcement: 1.2 m body, 0.58 m valve, 4 tonnes; reported D 110,000 L/s and He 40,000 L/s; separate adsorption/regeneration [3] | High-priority physical prototype; speed is not STP product throughput or recovery yield |
| CN107993733B | Three-stage fusion-exhaust cryopump: 70–80 K, 10–20 K, charcoal-bearing 4.2–10 K stages and sequenced desorption [4] | Existing architecture for interface modeling; no validated Beyond Q efficiency |
| KIT EP3061098B1 | Continuous fusion-exhaust processing and separate hydrogen/residual-gas routes [5] | Candidate fuel recycle architecture |
| Colorado School of Mines US20250360467A1 | Published metal-foil DIR application [6] | Candidate alternative; patent claims are not measured He3 product performance |
| ORNL continuous cryopump | Preliminary D2/He tests reporting >99% DIR at tested flows below 50.7 Pa m3/s with 1% He [7] | Measured fuel recycling reference; NOT 99% He3 recovery |
| Linde US20240261731A1 | He3/He4 cryogenic-distillation design, largely for trace-He3 feed [8] | Real process reference; actual fusion mixture requires a new calculation |
| Dalian CN117819497B | Membranes/oxidation/condensation for He3 extraction from tritiated heavy-water headspace [9] | Different feed and chemistry; not a direct fuel-recycle replacement |

The cited 582-tonne Chinese magnet is not a priority integration candidate. Official reporting distinguishes that toroidal-field magnet from a separate HTS central-solenoid coil; component scale or national manufacturing capability does not establish ARC retrofit compatibility [10]. Additional Chinese pump/purification leads CN120544972A and CN224822076U await accessible original documents. The claimed Shenzhen quasi-pulsed DD/FRC selective-recovery patent remains unverified; no parameter depends on it.

Required next evidence includes inlet pressure/composition/temperature, pumping-speed curves and conductance, saturation capacity, isotope-specific regeneration yields, cross-contamination, cycle degradation, tritium containment, product assay limits and refrigeration power. Buyer chemical purity, isotopic purity and radiological acceptance must be specified separately. The study does not claim these technologies have no possible integration route; it also does not claim they already constitute a qualified reactor-scale train.

## 5. Dynamic inventory, recovery and energy model

The exact first-order compartment operator solves dI/dt=S-KI with explicit integrated exits. Positive constant sources and rates preserve nonnegative stock. Inter-compartment coupling is operator-split and therefore has timestep error, measured separately by refinement.

For blanket inventory, the candidate well-mixed equation is:

\[
\dot I_b=\mathrm{TBR}\,\dot m_{burn}-\left(\epsilon/\tau_{loop}+k_{perm}+\lambda\right)I_b.
\]

All rates must share time units. Unextracted material remains in inventory and recirculates; single-pass extraction efficiency is not permanent recovery. The steady-state expression follows from this assumed well-mixed model, not verified reactor chemistry. A plug-flow pass model and a well-mixed first-order model require different interpretations of epsilon/tau.

The campus T identity is:

\[
I_0+T_{DD,A}+T_{blanket,A}+T_{blanket,B}
=I_{end}+T_{burn,A}+T_{burn,B}+T_{decay}+T_{loss}+T_{export}.
\]

Internal transfers and unburned recirculation cancel at the campus boundary. They cannot be counted as new production. Gross B TBR=1 is the originator's conservative replacement-breeding screen, not proof that recovered B supply covers losses. A is the separate source for startup, makeup and potential exports. A0 disables A breeding without removing primary DD neutron production.

The He3 pipeline uses mobile and purification compartments. The **37.5% conservative-potential, 75% planning and 90% optimistic** fractions are assumed overall eventual birth-to-product-candidate recovery, applied once to pipeline exits. They are not separately measured pump capture fractions. This nomenclature does not establish a guaranteed physical lower bound. Holdup is inventory, not permanent loss; loss already included in an overall fraction must not be deducted again. The model does not resolve saturation, regeneration cycles, wall retention or D-He3 reaction kinetics.

He4 from A secondary DT and B primary DT is separately counted. Blanket-path He4 is flagged unavailable. No laboratory-grade certificate, purification yield or He4 sales price is inferred merely from nuclear birth. He4 revenue is uncredited.

The neutron ledger counts primary DD and DT births. It is NOT a closed neutron-transport capture/leakage balance. Fusion energy is partitioned once into charged-particle and neutron kinetic components. Prescribed blanket reaction Q is separate; it is not an additional copy of neutron kinetic energy. Deposited thermal heat remains unresolved without transport/heating evidence.

The electrical scenario subtracts A net draw, B own loads and common loads from B generation. The executed A draw is **100 MWe ASSUMED**, not a physics result. Shutdown draws and common processing are explicit. Positive annual net energy can coexist with imports during startup or outages. Electrical islanding, storage and ramp dynamics have not been demonstrated.

## 6. Executed single-module and fixed-calendar fleet results

The v2.0 execution uses Python 3.12.14, NumPy 2.3.5, seed 119 and 0.25-day integration. One module and 50 separately inventoried modules were run for 60 years. The saved fleet commissions one module every 0.1 year, reaching 50 over 4.9 years. A/B daily permissions have separate marginal macro availabilities of 85% and 90%, a shared 2% outage probability, and independent residual permissions. Source duty 15/16 is additional and applied once. These are synthetic schedule assumptions, not calibrated outage-duration or repair distributions.

B starts only after its storage reaches one uninterrupted FPY of burn plus a 10 kg reserve: 71.654 kg at 1.10 GW. Starting inventory is zero; A supplies the initial T. This threshold is a policy, not proof that one-year operation is guaranteed independently of holdup and processing. B first starts on day 246 in the executed single-module realization.

| One module | Year 1 | Year 2 | Year 10 |
|---|---:|---:|---:|
| He3 product candidate at 37.5%, STP L | 335,841 | 332,089 | 337,214 |
| He3 product candidate at 75%, STP L | 671,682 | 664,179 | 674,428 |
| T terminal export in selected conditional scenario, kg | 20 | 20 | 20 |
| Net electricity, MWh | 119,053 | 2,170,561 | 2,199,117 |
| Gross electricity imports, MWh | 629,520 | 85,320 | 73,590 |

The 37.5% output is slightly below 350k because this run uses separate macro availability and pulse duty, pipeline holdup and replacement outages. It does not negate the earlier 85%-effective-exposure arithmetic. The fixed-exposure release reports output instead of forcing v1.9's 350k target controller to pass.

The fixed-calendar fleet's first year is net negative: approximately -2.877 TWh, with ten A units operating and only three B units started by year-end. Fleet year 2 is approximately +12.909 TWh, and year 10 approximately +105.406 TWh. This startup timing, not a reversal of mature-module energy arithmetic, explains the initially confusing negative fleet energy. The financial curve in dollars is a different quantity.

Initial loan payments continue independently for each staggered module. They do not all disappear at fleet year 30. The model includes illustrative 30-day replacement outages every two operating-calendar years, with B's clock beginning at actual startup. Actual FPY/damage-based lifetimes, installed replacement costs and refurbishment scope are unresolved.

## 7. Independent-review reconciliation

DeepSeek correctly identified poor aggregate dashboard disclosure: the first display hid the DD source, internal transfers, decay, unsold inventories and scenario controls. It incorrectly concluded that the underlying model lacked the DT stage, decay or a DD T source, and incorrectly compared A's direct He3 with B's blanket T as if they were coproducts.

The exact one-module year-one ledger is:

| Flow | kg |
|---|---:|
| A direct DD T births | 121.041309 |
| A direct DD He3 births | 121.040508 |
| A secondary T burn | 6.314544 |
| B DT T burn | 17.130502 |
| B gross blanket T births | 17.130502 |
| A-to-B storage transfer, internal | 108.447535 |
| T decay | 2.964505 |
| T processing losses | 5.763101 |
| T permeation | 0.000014 |
| T conditional external exports | 20.000000 |
| Final T inventory, starting from zero | 85.999144 |

The DD atom-birth ratio is unity to numerical precision. B's gross birth/burn equality is the selected TBR=1 input and does not remove A's source. Terminal exports are min(available storage above reserve, module cap), limited again by fleet cap and physically deducted. A flat saturated cap is not an invented source. Decay is present in all T compartments. A may consume T internally and must not be assigned zero secondary consumption merely because it is called a DD factory.

The v2.0.1 reconciliation exposes 1,440 scenario/year rows and 6,120 reactor-stage rows, with DD/DT birth, burn, transfers, separate plasma He4 sources, campus decay/loss balance, market bank and actual selector filtering. Per-reactor loss allocation unavailable from the parent export remains null. Parent physics and inputs were not changed to make the review pass.

The old delivered HTML was complete with 1,440 JSON records and syntactically valid JavaScript; external copying may have truncated a shared version. The proposed replacement's fallback from DD birth to B breeding and its decay-free label were rejected. Its price/offtake change events did not themselves implement filtering; the corrected dashboard does.

At 50 modules / 75% recovery / capped He3 offtake, the executed year-60 unsold bank is about **890.924 million STP L**. That is a real stress-case result. The fleet-wide 350k-L cap is NOT measured global market demand. In year 60, that cap is approximately 1.10% of total He3 candidate output, or 2.20% of the year's allocation after the saved 50% retention rule—not 0.03%. Unsold stock accumulation is visible and must inform future dispatch and price scenarios.

## 8. Market context and alternatives

USGS's 2026 publication estimates world He3 production at about 40,000 L/year in 2024 and 2025 [11]. A hypothetical 350k-L qualified source is therefore about 8.75 times that annual production reference, subject to consistent volume normalization. This comparison establishes scale, not a guaranteed customer base, price or measured 2026 shortfall.

The day's public-source scan found substantial superconducting activity: IBM's August modular cryogenic announcement, Rigetti's April 108-qubit availability, IQM international deployments, Alice & Bob's on-premises system, Origin Quantum's Wukong 180 announcement and QpiAI's Kaveri program [12–17]. Quantum-company count and qubit count do not directly determine isotope purchases. Announcements, plans and operating equipment must be distinguished; the scan was broad, not a census of every startup.

Bluefors agreed to purchase up to 10,000 L/year for 2028–2037; Maybell announced thousands of liters annually for 2029–2035 [18–19]. Interlune's July 2026 release reports nearly $500M in binding multi-year purchase agreements and a 99%-He3 separation demonstration from industrial helium [20]. Contract totals are not annual revenue; demonstration purity is not industrial throughput. Topaz's October recovery agreement is an evaluation, not established commercial production [21].

He3-based dilution refrigeration is a current application, not solely a future D-He3-fusion bet. However, existing dilution refrigerators recirculate working fluid; they are not generally once-through consumers. Demand is new fills + expansions + replacement losses + strategic stocks - reclaimed inventory.

Alternatives are not uniformly speculative. A 2026 cADR paper reports continuous sub-30-mK cooling without He3 [22]; kiutra announced a modular He3-free X-Type with first deployments planned for 2027 [23]. Maybell claims up to 80% less He3 per qubit in its ColdCloud architecture [24]. Neutral atoms, trapped ions and some warmer photonic/solid-state designs are meaningful alternatives, although they are not drop-in replacement refrigerators for an installed superconducting system. Google's March addition of neutral-atom work illustrates diversification [25]. These developments belong in demand sensitivities rather than being ignored or assumed to eliminate demand.

A peer-reviewed 2026 ORNL-associated resource study independently identifies He3 as a possible quantum-scale-up bottleneck under modeled futures [26]. Beyond Q's defensible market proposition is the possibility of materially expanding qualified supply. It does not establish a universal quantum capacity threshold or a perpetual selling price.

## 9. Reactor-only capital, financing and year-one/year-two economics

The originator specifies 30-year financing at 5%, He3 at $1,500/STP L and tritium at $1,500/g as illustrative corrections to earlier market-price assumptions. These are user scenario values, not financing offers or offtake quotations.

For fully financed principal C, annual level debt service is C*r/[1-(1+r)^(-30)], with r=0.05. The annual factor is approximately 0.0650514351.

| Alternative capital scope | Annual debt service |
|---|---:|
| Corrected historical $5.67B ledger | $368.842M |
| Two assumed $2.8B chassis + $300M adaptation = $5.90B | $383.803M |
| $8B cost stress | $520.411M |
| $12B cost stress | $780.617M |

The historical $5.67B sum was $2.8B+$2.8B+$150M-$200M+$120M, not $5.87B. Possible overlap between adaptation and isotope-equipment scope remains. The alternate $5.90B scenario does not take the same turbine credit. These are research assumptions, not CFS prices. A 10–15% component-mass retrofit does not imply a 10–15% price increment. The approximately $300M recollection is adaptation scope, not two complete reactors.

Both A and B housing, foundations, shielding/confinement, maintenance/hot-cell access, isotope processing/storage, cooling/heat rejection, switchgear/interconnection, engineering, construction interest/fees and contingency must be reconciled with chassis scope. Do not double-add items already included. Site/housing/OPEX/replacement/decommissioning fields remain unresolved. The $5.9B subtotal is not a complete installed budget.

The saved runs retain 50% of recovered He3 internally. **The originator has now removed that mandatory reserve for standalone and GPU-only-hosted modules.** This change is an accepted policy specification and a postprocessed financial comparison, not a claim that the saved v2.0 inputs were already updated. Tritium startup and operating buffers remain necessary.

At zero mandatory He3 retention, assuming all stated product qualifies and sells at the illustrative prices:

| One module, 37.5% overall recovery | Year 1 | Year 2 |
|---|---:|---:|
| He3 sold, STP L | 335,841 | 332,089 |
| He3 gross receipts | $503.762M | $498.134M |
| Conditional T exports: 20 kg/year | $30.000M | $30.000M |
| Initial hardware-subtotal debt service | -$383.803M | -$383.803M |
| Modeled electricity imports | -$62.952M | -$8.532M |
| **Remaining before unresolved costs** | **+$87.006M** | **+$135.799M** |

This is coverage of known charges, not full-cost operating profit, investment payback or demonstrated midyear-two break-even. The unresolved annual costs and additional financing must fit inside the remaining headroom. Annual data do not establish an exact intra-year crossover date. Selling only 350k L in the 75% recovery case gives approximately $108.245M and $162.665M headroom in years 1 and 2 with the same T-export assumption; additional inventory is not automatically cash.

Illustrative product value, realized external revenue, internal avoided purchases and stored inventory must be separate. At the assumed price, 350k L has $525M of illustrative gross value. Retention changes allocation and cash receipts, not nuclear production. Internal QPU use could have additional strategic benefits, but those are not priced here. No molecule is sold twice, and unsold stock does not service debt merely by having an illustrative valuation.

Electricity export receipts and He4 receipts remain uncredited in the year-one/year-two table. This is not evidence that electricity has zero value. GPU/QPU computing revenue remains excluded. A separate 2026 IREN $3.4B/5-year/approximately-60-MW contract was examined as context, but its GPU equipment and service scope cannot be inserted as reactor revenue [27]. The host facility's own economics belong to its owner.

After each original loan is fully amortized, that debt-service obligation ends; costs of maintenance, replacements, refurbishment, new debt and eventual decommissioning do not. Constant 2026 prices over a 60-year sensitivity are not forecasts. Full-cost financial viability and physical sustainability remain different gates.

## 10. Critical originator clarification: separately financed, fuel-supported cascade

**This section is the controlling expansion specification and must be preserved in future work.**

The originator does NOT propose that campus 1 must accumulate enough cash to purchase campus 2. Every new campus receives its own project financing. Established campuses support later startups with available tritium, subject to their own sustainability and reserves.

| Campus commissioned | Eligible predecessor fuel donors | Capital source |
|---|---|---|
| 1 | Bootstrap A operation or explicitly modeled external startup arrangement | Campus 1's project financing |
| 2 | Campus 1 | Separate campus 2 financing |
| 3 | Campuses 1 and 2 | Separate campus 3 financing |
| 4 | Campuses 1, 2 and 3 | Separate campus 4 financing |
| k | Eligible operating campuses 1 through k-1 | Separate financing for campus k |

There are at least four independent readiness conditions:

1. **Operating qualification:** donors meet the specified sustained energy/fuel performance and reserve policy over a defined evaluation window. A positive simulated annual net energy is not itself demonstrated continuous autonomy.
2. **Fuel readiness:** physically available, uncommitted, qualified tritium above donor reserve floors can supply the recipient startup inventory, including processing/transport buffers.
3. **Financing readiness:** the recipient's external financing and working capital are committed. Donor cash does not silently finance it.
4. **Engineering/site readiness:** equipment, construction, commissioning, staffing, approvals and maintenance capacity are available.

No new startup is triggered merely by multiplying a theoretical annual surplus. The recipient may produce its own DD tritium as its A unit starts; predecessor fuel can accelerate B startup and reduce initial grid dependence. That benefit needs an explicit chronology, not a second count of the recipient's own source.

### 10.1 Conservation and allocation requirements

For donor i, available fuel is max(0, qualified mobile stock - own reserve - existing commitments). A commitment must reserve those atoms, not leave them free for sale or another recipient. A shipment is debited from donor storage and credited to an in-transit compartment; transport decay and loss are explicit; receipt is credited only once. The recipient's stock is then subject to its own processing and burn ledger.

For a shipment of mass m and transport time tau, a simple candidate received amount is m*(1-loss_fraction)*exp(-lambda*tau), with separately recorded sinks. Exact transfer mechanics and qualification requirements remain unresolved.

Fuel shipped to a successor cannot simultaneously earn external tritium-sale revenue. At the illustrative $1,500/g, allocating the current 71.654 kg threshold has approximately $107.481M of gross sale-value opportunity cost, not automatically an equal cash expense or a new source of revenue. Transfer purchase, grant, loan and ownership contracts are separate policy inputs; none is assumed without disclosure. Internal charges cancel only in consolidated reporting, not necessarily in each independently financed project.

### 10.2 Why acceleration is plausible and exponential growth is conditional

If each mature module contributes transferable surplus s_T per year and each new startup requires I_start, a fuel-only continuous approximation is dN/dt=(s_T/I_start)N. This illustrates a compounding capacity mechanism. It does not prove an unlimited exponential rollout.

With construction and maturation delay tau, a more informative idealization is dN/dt approximately (s_T/I_start)N(t-tau), before capacity/financing/site constraints. Only qualified eligible modules contribute. Surplus can shrink with outages, reserve commitments, exports or degradation. Market constraints affect prices and financial readiness even when new capital is externally financed.

For illustration ONLY, using the current 20 kg/module/year export-cap sensitivity as if it were transferable supply and a 71.654 kg threshold requires approximately 3.58 donor-module-years per startup. Two mature donors could accumulate that quantity in roughly half the fuel-only time. The 20 kg value is a selected export cap, not a demonstrated maximum surplus, and this illustration is not a commissioning forecast.

Faster fuel readiness can justify more financeable projects without requiring predecessors to pay for their construction. It does not create free capital, qualified tritium, component manufacturing or customer demand. Finite limits eventually dominate any unconstrained exponential approximation.

### 10.3 What has and has not been implemented

**Executed:** fixed-calendar 1/50-module inventories; zero-external-T bootstrap; campus-local A→B transfer; separate outage permissions; conditional external exports; reactor-only finance; market and recovery sensitivities.

**Not executed:** qualification-triggered expansion; shared predecessor fuel pool; intercampus reservations, shipments and receipts; separate project-finance readiness events; a demonstrated exponential growth curve. The saved v2.0 input explicitly has intermodule_transfers=false. Its 0.1-year commissioning cadence must not be described as the cascade specified here.

The next controller must report why each candidate is waiting: operating proof, fuel, financing, site/build capacity or uncertainty. Unknown readiness must remain unknown/blocked in strict mode, not be silently assigned true. Clearly labeled sensitivity mode may assume readiness, but its growth curve remains conditional. Whether donor electricity can physically supply a geographically separate new campus also requires a grid/contract boundary, not an automatic wire.

## 11. Verification, provenance and remaining gates

The executed v2.0 suite has 16 passing checks; the v2.0.1 reconciliation has five more passing checks, plus a Node-based dashboard data/filter test. The dashboard harness checks actual filter wiring and null handling, not full browser rendering. Three-year refinement from 0.25 to 0.125 to 0.0625 day gives a coarse/fine final-T difference of about 0.02156%, while B burn and day-246 startup agree to numerical precision in that case. These are limited numerical checks, not universal accuracy bounds.

Maximum per-module 60-year T residual is below 4.4e-9 kg. Aggregate annual reconciliation residual is below 1.3e-8 kg. The DD equal-branch atom-ratio error is below 5.5e-12. Recovery ranges are scenario bounds, not confidence intervals. A single seeded outage realization does not establish reliability uncertainty.

| Gate | Current software contribution | Still open |
|---|---|---|
| G1: plasma and secondary burn | Source/stoichiometric consistency and inherited candidate burn/escape rates | Feasible full DD operating point, distributions, slowing, confinement, He3 consumption and wall transport |
| G2: neutronics | Explicit assumed yields, A0 control and neutron-birth normalization | Qualified ARC geometry/materials/data, Li pathways, uncertainty, transport/heating and benchmark comparison |
| G3: recovery | Explicit holdup and 37.5/75/90% overall sensitivities; equipment references | Actual saturation, regeneration, detritiation, purity, yield, component energy and buyer acceptance |
| G4: inventory/operations | Startup, reserves, decay, losses, local transfers and fixed fleet | Calibrated outages/replacements, intercampus fuel cascade, qualification and operational reserve validation |
| G5: thermal/electrical | Separate nuclear partition and prescribed electrical screen | A draw and deposited heat, complete auxiliaries, load dynamics, storage and continuous energy autonomy |

Earlier releases, failed assumptions and corrections remain append-only artifacts. The initial JSON serialization and plot type failures are logged; the reconciliation's first stage-energy mismatch was traced to requested versus timestep-rounded commissioning and corrected without changing parent physics. A successful test is never promoted to a physical gate closure.

## 12. Continuation order

1. Preserve this checkpoint and decision register on GitHub before more modeling.
2. Add zero mandatory He3 retention as the next versioned default, keeping saved 50%-retention results intact and explicitly comparable.
3. Separate product value, qualified sale allocation, receipts and inventories; keep capped and full-offtake sensitivities clearly labeled.
4. Implement the separately financed predecessor-fuel controller with donor reserve floors, commitments, in-transit stock, losses, receipt, foregone sales and recipient startup gates.
5. Run synchronized-mature, fixed-calendar and readiness-triggered rollout controls, including finance unavailable, no transferable surplus, correlated outages and delayed construction. Do not assume an exponential outcome.
6. Replace unverified performance with source-qualified plasma, transport and equipment evidence; obtain installed building/site/OPEX/replacement inputs for full-cost cash flow.
7. Report finite 30/60-year operating boundaries, failure conditions and uncertainty; keep GPU/QPU configuration and economics outside the module model.

## References and source-transfer limitations

All URLs below were used in today's source inspection or earlier source registers read during the session. Corporate statements are treated as corporate statements; patent descriptions as proposed mechanisms; numerical conventions and modeled outputs retain their own evidence labels. No new experiment is reported here.

1. Commonwealth Fusion Systems, *ARC: Putting fusion energy on the grid*. https://cfs.energy/technology/arc/ . Public DT electrical design context, not DD proof or price quotation.
2. ARC 2026 physics-basis overview, Journal of Plasma Physics. https://doi.org/10.1017/S0022377826101706 . Exact source geometry and design boundaries govern any transfer.
3. ASIPP/Hefei, April 21, 2025, *Large composite cryopump capable of deuterium/helium separation*. https://hf.cas.cn/kxyj/kyjz/202504/t20250421_7605156.html . Prototype announcement; no Beyond Q yield.
4. CN107993733B, *Three-stage cryopump treatment of radioactive fusion-reactor exhaust*, granted publication November 3, 2020. https://patents.google.com/patent/CN107993733B/zh . Patent, not measured end-to-end recovery.
5. KIT, EP3061098B1, *Method and device for continuous re-processing of exhaust gas of a fusion reactor*. https://patents.google.com/patent/EP3061098B1/en . Candidate equipment topology.
6. Colorado School of Mines, US20250360467A1, *Systems and methods employing metal foil pumps for direct internal recycling of fusion reactor exhaust plasma*, published November 27, 2025. https://patents.google.com/patent/US20250360467A1 . Published application.
7. Gebhart, T. E. et al. (2026), *Preliminary Testing of a Continuous Cryopump for Primary Fusion Device Pumping and Direct Internal Recycling*, IEEE Transactions on Plasma Science 54(6), 2665–2671. https://doi.org/10.1109/TPS.2025.3635057 . Institutional abstract: https://impact.ornl.gov/en/publications/preliminary-testing-of-a-continuous-cryopump-for-primary-fusion-d/ . D2/He DIR measurements, not He3 certification.
8. Linde, US20240261731A1, *Method and apparatus for separation of helium-3 from helium-4 by means of a cryogenic process*. https://patents.google.com/patent/US20240261731A1/en . Different trace feed requires separate process calculation.
9. Dalian University of Technology, CN117819497B, *Multi-membrane coupled extraction of He3 from tritiated heavy-water headspace*. https://patents.google.com/patent/CN117819497B/zh . Different feed chemistry.
10. Chinese Academy of Sciences, June 29, 2026, *World's Largest Superconducting Magnet for Fusion Reactor Unveiled in Hefei*. https://english.cas.cn/newsroom/cas-in-media/202606/t20260629_1175003.shtml . Large TF magnet and separate HTS solenoid, not an ARC-fit conclusion.
11. U.S. Geological Survey, *Mineral Commodity Summaries 2026: Helium and rare gases*. https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-helium.pdf . Estimated 2024/2025 production context, not a future demand cap.
12. IBM, August 19, 2026, *IBM Connects Its First Modular Cryogenic Systems in Milestone Toward Fault-Tolerant Quantum Computing*. https://newsroom.ibm.com/2026-08-19-ibm-connects-its-first-modular-cryogenic-systems-in-milestone-toward-fault-tolerant-quantum-computing . Corporate engineering announcement.
13. Rigetti, April 7, 2026, *General Availability of 108-Qubit System*. https://investors.rigetti.com/news-releases/news-release-details/rigetti-announces-general-availability-108-qubit-system . No isotope inventory disclosed.
14. IQM, April 27, 2026, *First enterprise quantum computer purchase in Japan*. https://iqm.tech/press-releases/first-enterprise-quantum-computer-purchase-in-japan-iqm-to-deploy-system-to-toyo-corporation/ . Deployment/procurement context.
15. Alice & Bob, June 2026, *Unveils First Quantum System, Helium*. https://alice-bob.com/newsroom/alice-bob-unveils-first-quantum-system/ . No automatic liters-per-qubit conversion.
16. Origin Quantum, May 7, 2026, *OriginQ Wukong 180*. https://originqc.com/blogs/originq-wukong-180 . Corporate system announcement.
17. QpiAI, March 25, 2026, *High-speed quantum error correction on superconducting systems*. https://www.qpiai.tech/pressreleases/2026-03-25-qpiai-achieves-high-speed-quantum-error-correction-on-superconducting-systems-with-new-decoder-platform . Corporate development claim.
18. Bluefors, September 16, 2025, *Bluefors to Source Helium-3 from the Moon with Interlune*. https://bluefors.com/news/bluefors-to-source-helium-3-from-the-moon-with-interlune-to-power-next-phase-of-quantum-industry-growth/ . Prospective up-to annual procurement, not delivered lunar supply.
19. Interlune, *Maybell Quantum as First Commercial Customer*. https://www.interlune.space/press-release/interlune-announces-maybell-quantum-as-first-commercial-customer-to-buy-helium-3 . Future delivery schedule, not a total market measure.
20. Interlune, July 20, 2026, *Produces Pure Helium-3 from Domestic Helium Using Novel Cryogenic Technology*. https://www.interlune.space/press-release/interlune-produces-pure-helium-3-from-domestic-helium-using-novel-cryogenic-technology . Claimed purity and contracts; industrial throughput remains separate.
21. Pulsar Helium, October 14, 2026, *LH3M Evaluation Agreement for Recovery Assessment at Topaz*. https://www.nasdaq.com/press-release/pulsar-helium-and-lunar-helium-3-mining-sign-evaluation-agreement-helium-3-recovery . Issuer release, evaluation stage.
22. *A compact cryogen-free continuous adiabatic demagnetization refrigeration platform for quantum technology applications*, Review of Scientific Instruments 97, 025214 (2026). https://pubs.aip.org/aip/rsi/article/97/2/025214/3381412/A-compact-cryogen-free-continuous-adiabatic ; bibliographic record https://pubmed.ncbi.nlm.nih.gov/41758002/ . Demonstrator scale, not established large-fleet equivalence.
23. kiutra, April 15, 2026, *X-Type modular cooling architecture*. https://kiutra.com/news/kiutra-announces-the-x-type . Announced specifications and planned deployments.
24. Maybell, March 12, 2026, *ColdCloud*. https://www.maybellquantum.com/news/coldcloud . Manufacturer efficiency/inventory claims, not independent demand reduction measurement.
25. Google Quantum AI, March 24, 2026, *Building superconducting and neutral atom quantum computers*. https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/ . Architectural diversification, not a substitute refrigerator qualification.
26. McCollum, D. L.; Sharma, N.; Pan, M.; Yao, W.; Bhanja, S.; Chehade, S.; Delgado, A. (2026), *Uncertain quantum computing futures and potential energy and physical resource impacts at scale*. https://doi.org/10.1016/j.rset.2026.100140 ; institutional record https://impact.ornl.gov/en/publications/uncertain-quantum-computing-futures-and-potential-energy-and-phys/ . Scenario-dependent resource analysis.
27. IREN, May 7, 2026, *$3.4bn AI Cloud Contract with NVIDIA*. https://irisenergy.gcs-web.com/news-releases/news-release-details/iren-secures-34bn-ai-cloud-contract-nvidia . Different equipment/service boundary; not included as reactor revenue.
28. Meschini, S.; Ferry, S. E.; Delaporte-Mathurin, R.; Whyte, D. G. (2023), *Modeling and analysis of the tritium fuel cycle for ARC- and STEP-class D-T fusion power plants*, Nuclear Fusion 63, 126005. https://doi.org/10.1088/1741-4326/acf3fc . Fuel-cycle modeling precedent; hydrogen ISS does not establish He3/He4 separation.
29. Niculescu, A. et al. (2025), *Helium-3 Applications and Recovery Techniques*, Journal of Fusion Energy 44, article 20. https://doi.org/10.1007/s10894-025-00491-6 . Its own high-purity column result is simulated; prior experiments and prospective validation must be distinguished.
30. *Power and particle exhaust for the ARC fusion power plant* (2026), Journal of Plasma Physics. https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/power-and-particle-exhaust-for-the-arc-fusion-power-plant/EE21BB8586540AACDA3B624D9058EFF3 . Preliminary exhaust estimate with stated uncertainty. Its printed 1100 MW/17.6 MeV=3.2e20/s differs from direct conversion ~3.90e20/s; resolve before using the numerical estimate as calibration. This does not alter the DD birth arithmetic.

## Artifact and publication provenance

Repository: https://github.com/atlaslattice/open-regenerative-compute-standard . Draft PR: https://github.com/atlaslattice/open-regenerative-compute-standard/pull/65 . This paper is prepared against implementation/reconciliation commit `971a94300d91d4ff514061a4918e44684277e78b`, stacked on v1.9 commit `597ae386d185ed0fe812ffc3f3a1bb3af2b3f4f8` / draft PR #63. Earlier releases remain intact.

Reproduce v2.0 with `python -m unittest test_model -v` and `python run.py` in `../module_fleet_v2_0`. Then run `python audit.py` and `python -m unittest test_audit -v` in `../review_reconciliation_v2_0_1`; optional `node test_dashboard.js` checks data/filter wiring. Full raw CSVs and dashboards are regenerated; compact execution evidence is committed. `NUMERICAL_SNAPSHOT.json` in this directory records the zero-retention postprocessing and its source hashes. `DECISIONS.json` and `HANDOFF.md` are the continuation authority for the new reserve and rollout policies. This paper adds no new physical simulation.
