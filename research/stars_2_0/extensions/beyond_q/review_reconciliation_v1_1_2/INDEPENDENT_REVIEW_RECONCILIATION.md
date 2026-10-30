# Beyond Q v1.1.2 — Independent-review reconciliation appendix

**Atlas Lattice / STARS 2.0 / Beyond Q.** Versioned addition to v1.1.1,
parent commit `891cd5008a5d470d83e064b38a529b64c2790fce`. Earlier releases
are unchanged. Configuration remains B **1.13 GW D-T fusion**, A hypothetical
**20 MW primary D-D**. No operating reactor or qualified fuel surplus claimed.

## Review receipt and accepted findings

Dave Sheldon supplied the review in this conversation, with provenance
**DeepSeek independent cross-audit followed by GPT-6 reconciliation**. This
is the source for the review's attribution, not evidence of an independent
experimental or institutional review. The eight requested changes are accepted
as accounting/provenance requirements, subject to the following evidence limits.

| Finding | Disposition in v1.1.2 |
|---|---|
| Derive kg/GW-FPY from physical constants | Explicit stoichiometric function and CSV; preserves legacy 55.8 and 63.1 display conventions |
| Report campus balance as kg and % of B burn | Static FPY and dynamic calendar-time quantities separately labeled |
| Independent A plasma/blanket processing | Two disjoint processing stocks, rates, permanent recovery fractions and loss counters |
| Recheck A blanket 1.3–2.6 kg envelope | Traceable only to a DeepSeek test range in published v1; retire as derived performance; do not scale by two |
| Enrichment at fixed and optimized geometry | Separate comparison specifications, no transport-based rankings without runs |
| Distinct TBR, recovery, inventory and uptime | Gross births, recovered transfers, external initial stock, delays, decay, losses and independent on-days are separate |
| A secondary D-T on/off | Both tested; DD source remains, blanket response recomputed per source spectrum |
| Regression corrections and visible failures | 17 tests gate the runner; initial failed test log retained, final status JSON/text emitted |

| Evidence category | What it applies to here |
|---|---|
| SOURCE-TRACED | Supplied review provenance; published v1 origin of the test envelope; SI/mass source anchors |
| VERIFIED-DERIVED | Reproduced legacy arithmetic, explicit mass conversion, conservation and regression identities |
| POTENTIAL-DERIVED | Yield/recovery scenarios, reported conditional balances and threshold searches |
| UNRESOLVED | Actual geometry-dependent yields, route-specific qualified recovery, optimized enrichment, physical self-sufficiency |

## Exact numerical conventions — VERIFIED-DERIVED conditional arithmetic

One FPY = 365.25 days = 31,557,600 seconds. D-T screening Q=17.6 MeV,
with a separate 17.59 MeV sensitivity, not a silent change. One T atom is
consumed per D-T reaction. Adopted tritium molar mass M_T=0.00301604928 kg/mol,
N_A=6.02214076e23 mol^-1, and 1 MeV=1.602176634e-13 J.

`k_T = (10^9 J/s)*(365.25*86400 s)/(Q_DT MeV * 1.602176634e-13 J/MeV) * (M_T/N_A kg/atom)`

| Convention | kg T / GW-fusion-FPY | B at 1.13 GW, kg/FPY |
|---|---:|---:|
| Legacy screening coefficient | 55.8 | 63.054 (historical displayed 63.1) |
| Common 17.6 MeV stoichiometry | 56.0490732962 | 63.3354528247 |
| 17.59 MeV sensitivity | 56.0809374652 | 63.3714593357 |

The 55.8 coefficient is about 0.444% below this 17.6 MeV calculation. Changing
365.25 to 365 days alone cannot explain the full difference. The originating
derivation of 55.8 is not in the v1 package: retain it as a legacy screening
convention, not a second equally precise constant. Legacy benchmark arithmetic
uses exactly its published 63.1 display basis. Do not mix source atoms from one
convention and consumed kg from another within a dynamic conservation ledger.

M_T is a rounded molar-mass convention from tritium isotope measurements,
not an exact SI defining constant. Neutral-atom rather than bare-triton mass
is appropriate to the reported fuel-material kg convention; the ~electron-mass
distinction and molar-mass-constant uncertainty are below the precision needed
with rounded reaction Q. N_A and J/eV conversion use exact SI values. No
claim of 11-digit physical prediction follows from displaying arithmetic digits.

Source anchors: [BIPM defining constants](https://www.bipm.org/en/measurement-units/),
[NIST SI definitions](https://www.nist.gov/si-redefinition/definitions-si-base-units),
Myers E.G. et al., *Atomic Masses of Tritium and Helium-3*, Physical Review
Letters 114, 013003 (2015), [doi:10.1103/PhysRevLett.114.013003](https://doi.org/10.1103/PhysRevLett.114.013003).
Q/branching and design anchors remain the source-bounded v1/v1.1 registry.

## Independent A pathways and threshold equations

Let D_A be gross primary DD T birth, C_A internal secondary DT consumption,
L_A gross blanket T birth, and eta_AP / eta_AB be the assumed eventual
plasma-derived / blanket-derived processing recovery. For an ideal annual
screening balance, with all rates on a common FPY basis:

`Q_A,potential = eta_AP*(D_A-C_A) + eta_AB*L_A`

`S = Q_A,potential + eta_B*TBR_B*B - B - L_other - reserve_additions`

`S_percent = 100*S/B`

`TBR_B,min = (B + L_other + reserve_additions - Q_A,potential)/(eta_B*B)`

These are POTENTIAL-DERIVED screening equations; no recovered quantity here
is automatically qualified for export. eta_B is ultimate recovery for this
static equation, not single-pass extractor efficiency. Transient holdup,
storage decay and repeated-pass losses require the separate time model.
Reserve additions are explicitly a static sink; startup stock is an initial
external source, not an annual birth or recurring surplus.

The dynamic model now has eight disjoint stocks: A plasma, A/B blankets,
A plasma-processing, A blanket-processing, B processing, A/B storage.
For each A processing route j, `dP_j/dt=inflow_j-(k_j+lambda)P_j`;
recovered outflow is `eta_j*k_j*P_j`, permanent processing loss is
`(1-eta_j)*k_j*P_j`. Plasma escape enters only A plasma-processing; salt
extraction enters only A blanket-processing. Recovered A material joins A
storage, from which actual bounded transfers move it to B. No consumed atom
can reach either recovery path. A's two processing routes share an outage
flag in this release but have independent parameters and counters.

Reference eta_AP=.95, eta_AB=.90, k_AP=4/day, k_AB=1/day are **assumed test
values**, not measured extraction performance. A plasma/blanket recovery is
applied once per respective processing path. B retains the prior repeated-pass
processing loss model. Blanket extraction, permeation, mobile decay and
processing decay remain separate; single-pass efficiency is not ultimate eta.

## Blanket-envelope provenance and secondary on/off

The [v1 provenance appendix](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/876bb375d278e9ccb934638fbfbe64852fbcbfbd/research/stars_2_0/extensions/beyond_q/tritium_self_sufficiency_audit_v1/APPENDIX_SOURCES_AND_PROVENANCE.md)
attributes the 1.3–2.6 kg/FPY range to DeepSeek's test envelope. The v1 white
paper explicitly says no transport/geometry derivation supports it. No original
reaction-response table, lithium mass/geometry, extraction chain or energy-group
neutron calculation is supplied. Consequently dependence on the old
8.55e18/s DD-neutron error cannot be established. **Retire the range as a
derived production estimate.** Historical files/regressions retain it as an
unvalidated assumption; neither doubling it nor declaring it unchanged is
a justified neutron-transport correction.

New source bookkeeping instead uses independent coefficients:

`N_DD = (1-b)*P_DD/[b*Q_DDp+(1-b)*Q_DDn]`

`L_A(t) = y_DD*N_DD(t) + y_DT*N_DT(t)` (atoms/time)

Here y_DD and y_DT are T atoms born per respective source neutron, not
transport results. Numerical reference .52/.52 reproduces an illustrative
earlier surrogate only. Equal coefficients do not assert equal physical
responses at 2.45 and 14.1 MeV. A0 must set both to zero; actual A1/A2
responses remain UNRESOLVED. The obsolete aggregate `tbr_a` input is removed.

With secondary DT off, set both fast burn and thermal burn hazard to zero.
The primary DD neutron source remains ~1.71e19/s. Under this **same assumed**
y_DD=.52, the new blanket scenario is 1.405373 kg/FPY, rather than zero.
With the reference secondary burn fraction .3734336 and y_DT=.52 it is
1.930186 kg/FPY. These are recomputed potential scenarios, not validation of
the retired 1.3–2.6 interval. Gross DD birth is 2.702640 kg/FPY; internal
secondary burn is 1.009257 kg/FPY in the on case.

## Enrichment comparisons and the 427-tonne claim

`outputs/enrichment_comparison_plan.csv` separates natural .075, intermediate
.20/.30 and high .90 Li6 **atom fractions** into two analysis routes:

1. Fixed geometry: same 90 cm surrogate blanket, source, materials, temperature,
   salt stoichiometry, ports and tally normalization; vary only enrichment.
2. Separately optimized geometry: for each enrichment/material independently
   evaluate candidate 85/90/100 cm blankets before selecting an optimum under
   common shielding, heat-removal, inventory and engineering constraints.

No solver/data/calibrated geometry is available, so TBR and selected geometry
are null/UNRESOLVED. This is an executable comparison specification, not
completed neutron transport or proof of universal 20–30% optimal enrichment.
Separate optimization must not compare one optimized case against an
unoptimized case while attributing all gains to enrichment.

The supplied 427-tonne figure matches `118.6*0.90/0.25=426.96 tonnes`.
This is conditional constant-fraction-inventory arithmetic only. It is not
a design requirement, nor evidence that reduced enrichment must preserve
the same Li6 atom count. If the fractions are atom fractions and mass denotes
bulk FLiBe, even this simple inverse-fraction scaling requires a molar-mass
correction: `M_new/M_old = (x_old/x_new)*(M_formula,new/M_formula,old)` for
fixed stoichiometry. The underlying material boundary and isotope basis of
118.6 tonnes are not established here; no salt-mass prediction is made.

## Effect on modeled thresholds and accounting categories

For B=63.335453 kg/FPY, TBR_B=1.02, assumed ultimate eta_B=.95, and the
secondary-on source scenario, perfect A processing gives Q_A=3.623570 kg/FPY,
S=1.660171 kg/FPY (2.621235% of B burn), and screening TBR_min=.992408.
Using separate eta_AP=.95 / eta_AB=.90 reduces Q_A to 3.345882 kg/FPY,
S to **1.382483 kg/FPY (2.182795%)**, and raises TBR_min to **.997023**.
This comparison holds sources and numerical conventions fixed.

With secondary DT absent and the same unvalidated neutron-response coefficients,
the recovered A scenario is 3.832344 kg/FPY and screening TBR_min=.988938.
Less internal T burn can outweigh reduced secondary-neutron blanket births;
this result is conditional on those response coefficients, not a recommendation
to remove secondary reactions from an actual reactor.

Dynamic CSVs separately record initial stock, gross A/B births, route-specific
recovery/loss, storage transfers, decay, reserve/stock growth, uptime and unmet
burn. Actual calendar-time stock growth is **not** the annual qualified surplus;
its denominator is actual B burn in that same interval. The simulation covers
365 calendar days, whereas FPY calculations use 365.25 days. Requested A/B
schedules are independent before common shocks; true burn is fuel limited.

The finite-horizon dynamic threshold requires final **B available storage**
at least equal to initial B storage and cumulative unmet B burn <=1e-8 kg;
it is not a physical self-sufficiency criterion. The CSV also computes a
matched unified-processing counterfactual, so the threshold shift caused by
separate A processing can be seen without changing the schedule or sources.
Its B recovery follows the original dynamic hazards/repeated processing, not
the static eta_B=.95. Thus dynamic and static thresholds cannot be directly
compared as if their recovery and inventory objectives were identical.

| Secondary DT | Schedule | Unified-processing counterfactual threshold | Split-processing threshold | Shift |
|---|---|---:|---:|---:|
| Off | Continuous | .96791 | .97229 | +.00438 |
| Off | Independent/common outages | .97437 | .97861 | +.00424 |
| On | Continuous | .97555 | .97998 | +.00443 |
| On | Independent/common outages | .98175 | .98604 | +.00429 |

These are timestep-dependent search results, rounded for inspection; the
root-search precision is not a physical uncertainty bound. Startup stock
and the absence of unmet burn over this finite horizon do not establish
long-term resilience, qualified reserves or regulatory compliance.

## Regression status and open evidence

`python run_review.py` runs the correction tests first and exits nonzero on
failure; logs and a machine-readable status remain visible. Tests cover the
legacy 28 cases, source-free noncreation, internal burn, separate recovery,
secondary-off primary neutrons, neutron/energy nonduplication, % denominator,
power lock, 427-tonne arithmetic and unresolved transport output.
An initial C03 test had a mistyped expected coefficient; its failure is retained
in `outputs/initial_regression_failure.txt`, and its test-only correction is in
the append-only audit. The final run passes all 17 tests.

G1 plasma/slowing-down/confinement inputs, G2 source-resolved transport and
geometry/material qualification, G3 route-specific measured extraction/speciation,
G4 calibrated failures/reserves/processing and G5 deposited heat/wall-plug
closure all remain OPEN. G6 external replication/provenance remains cross-cutting.

Research conception/direction: Dave Sheldon / Atlas Lattice. DeepSeek: reported
independent cross-audit and historical test-envelope proposals. GPT-6: supplied
review reconciliation, numerical corrections and computational integration.
Gemini Argon: documented candidate burn/extraction equations and enrichment
challenge. These are analytical contributions, not experimental measurements,
institutional endorsements, or independent identities verified by this release.
