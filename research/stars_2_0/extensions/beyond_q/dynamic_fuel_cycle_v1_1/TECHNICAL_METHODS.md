# Equations, boundaries and interpretation

## Evidence vocabulary

**SOURCE-TRACED** means an exact source or supplied proposal was identified.
It does not imply that a claimed performance was experimentally established.
**VERIFIED-DERIVED** means reproducible conditional arithmetic or code identity.
**POTENTIAL-DERIVED** means a scenario depends on unvalidated physical inputs.
**UNRESOLVED** means required data, calibration or physical closure is missing.
Passing a unit test never promotes a physical prediction to validated evidence.

## G1 — primary and secondary reactions

Use FPY = 365.25 days, 86400 s/day; MW = 10^6 J/s.
For assumed D-D T-branch probability b, Qbar = b*4.03+(1-b)*3.27 MeV.
R_DD=P_DD/(Qbar*1.602176634e-13 J/MeV). T birth = b R_DD;
DD neutron birth = (1-b) R_DD. Branches are exclusive. Equal branching is
a screening approximation; no reactivity-weighted distribution is solved.

Argon proposed:

`x = n_D [m^-3] * <sigma v>_DT [m^3/s] * tau_p,T [s]`

`f_T = f_fast + (1-f_fast) x/(1+x)`

`C_A = D_A f_T; P_DT,sec = R_T,born f_T Q_DT`.

This has consistent dimensions and 0<=f_T<=1 for nonnegative rates and
0<=f_fast<=1. It is the steady two-stage competing-hazard result, not a
self-consistent kinetic plasma calculation. Let r=n_D<sigma v>, e=1/tau.
The dynamic model tracks thermal tritium stock X:
`dX/dt=(1-f_fast)D_A - (r+e+lambda)X`;
fast burn is `f_fast D_A`, thermal burn `r X`, escape `e X`.
This reproduces Argon's steady formula when decay is negligible. Daily hazards
are r*86400 and 86400/tau. D_A here has kg/day units. Thermal T held across
an outage continues to escape/decay and does not burn while A is off.

The reference n=1e20 m^-3, reactivity=1e-22 m^3/s, tau=59.6 s, f_fast=0
are **illustrative inputs**, chosen to explore a fraction near the legacy
18 MW assumption, not independently predicted parameters. Rate fields
`a_reaction_day`/`a_escape_day` are the authoritative dynamic inputs; the
n/reactivity/tau fields explain the reference conversion. Sensitivity CSVs
explicitly vary a hazard independently. No fast-ion slowing-down integral,
spatial profiles, slowing-down cross sections, plasma heating or confinement
power balance is claimed. In particular f_fast is not solely a universal
function of electron temperature.

Using a common 17.6 MeV convention, primary 20 MW with equal branches permits
48.219178 MW **steady** secondary power if all born T burns, with no external
T feed or previously accumulated inventory. Thus 18 MW implies f=0.373295.
Argon's 48.19 / 0.3735 uses rounded 17.59 MeV and rounded birth rates;
“exactly” is too strong at that precision. Transient power can exceed the
instantaneous birth-limited bound if accumulated T burns; integrated burn
cannot exceed integrated birth plus explicitly modeled initial plasma stock.

A fixed exposure model `1-exp(-n<sigma v>tau)` is also available to demonstrate
why different escape/residence distributions give different burn fractions.
Do not add overlapping fast and thermal fractions or treat unlike-ion D/T
reactions as having the identical-particle D-D factor of one half.

## G3 — Argon extraction equations

With I in kg-T, time in days, b_B in kg/day:

`dI/dt = TBR_B*b_B - (k_ext+lambda+k_perm) I`

`k_ext=epsilon_ext/(tau_loop_minutes/1440)`

`I_ss=TBR_B*b_B/(k_ext+lambda+k_perm)`

`eta_salt+ISS = k_ext/(k_ext+lambda+k_perm)*(1-f_ISS_loss)`.

lambda=ln(2)/(12.32*365.25) day^-1; k_perm day^-1. B(t) in this ODE
must be a **rate**, not an annual total inserted alongside minute-scale rates.
These are exact solutions of a constant-rate well-mixed linear model, not
first-principles proof of extraction performance. Salt chemistry, T2/TF/HT
speciation, diffusive mass transfer, redox, wall trapping and recoverable
permeation paths remain unmodeled. Permeation is explicitly assumed irreversible
here; add a donor/recipient recovery compartment if data support recovery.

At high single-pass efficiency the residence assumption matters: continuous
well-mixed turnover k=epsilon/tau differs from a deterministic loop with
survival (1-epsilon) each pass; survival-equivalent k=-ln(1-epsilon)/tau.
The implementation does not silently switch between these models. For a
discrete loop, use delayed transport/age bins rather than relabeling k.

`argon_table_audit.csv` reproduces the supplied 1.44/2.45/7.34/36.7 g table.
The proposal supplies **combined** irreversible losses but no separate
k_perm and ISS-loss values. The reproduced table therefore explicitly assumes
k_perm=0 and assigns the listed fraction to ISS, with nuclear decay retained.
This is one decomposition, not an inferred measured permeation rate. Those
loss fractions dominate the quoted eta; the table cannot independently
identify permanent recovery. Grams of mobile inventory are not a pressure
calculation without salt volume, chemical equilibria and temperature data.

The dynamic processing compartment additionally has residence time, decay
and repeated-pass processing loss; `eta_salt+ISS` is not automatically overall
campus recovery. Unextracted salt T remains in inventory. B unburned feed
returns to processing. A escaping T is processed then sent to storage, not
injected back into the A plasma in this reference architecture.

## G4 — conservation, schedules and numerical method

The dynamic compartments and sources are specified in `fuelcycle/model.py`.
B requested consumption is derived from 1130 MW fusion and Q_DT. Its feed
requirement = consumption/pass-burn fraction, subject to available B storage.
Unburned feed is transferred to processing; actual B burn generates the
source neutrons and blanket births. Fuel starvation reduces actual power,
rather than accumulating negative storage or breeding from a failed burn.

Every compartment uses the exact constant-coefficient solution:
`X_new = X_old exp(-K dt) + S (1-exp(-K dt))/K`.
Integrated exits are allocated by competing hazards; a stable small-K
expansion avoids cancellation. Sequential coupling creates first-order
splitting error. Positive compartment stocks and closed isotope accounting
are numerical invariants, not evidence for the chosen rate constants.
`timestep_refinement.csv` quantifies finite-step bias at identical schedules.

Schedules are daily binary pairs; supplied schedules can be passed directly
to `simulate`, independently of the reproducible Bernoulli generator. With
independent on probabilities p_A,p_B and common-off probability c:
E[A]=(1-c)p_A, E[B]=(1-c)p_B,
Cov(A,B)=c(1-c)p_A p_B before planned windows. This models a common daily
shock, not empirically fitted repair times or multi-day failure correlation.
Processing/extraction continue through reactor shutdown. Export is a storage
transfer and never a fresh source. A reserve is protected by the transfer rule.
External imports after initial stock are zero. Initial inventory is declared,
not a predicted or regulatory-qualified startup requirement.

Decay converts one T atom to one He3 atom. The ledger reports kg-T-equivalent
decayed, not exact daughter mass or recoverable He3 product. Blanket birth
operators assume inexhaustible Li reservoirs and externally prescribed yields;
these require physical transport/depletion checks. TBR_A means T births per
total A source neutron; TBR_B means T births per B D-T burn. They are not the
same denominator as “A total tritium births per primary D-D T birth.”

For constant net addition S and storage-only decay, dV/dt=S-lambda V gives
V(t)=V0 exp(-lambda t)+S(1-exp(-lambda t))/lambda and ceiling S/lambda if
S>0. Argon's ceiling is correct for this restricted model, not a general
upper stock guarantee with changing schedules and recirculation losses.

## G2/G5 — neutron and energy boundaries

Neutron sources: DD n branch, A secondary DT, B DT, separately recorded.
No neutron fate closure is invented from a TBR, especially TBR>1 with
multiplication and Li7 reactions. Transport tallies remain missing.
Fusion energies partition neutron kinetic energy (2.45/14.1 MeV) and charged
energy; `fusion_neutron+fusion_charged=fusion_total`. Blanket Li6 Q=+4.78 MeV,
Li7 Q=-2.47 MeV are distinct **reaction** terms with assumed birth fractions.
The Li6-birth fraction is not Li6 enrichment. Unmodeled capture reactions
and photon escape prevent this source-release ledger from certifying total heat.

For a future transport calculation, use charged deposited fusion energy plus
neutron/photon deposited heating once. Never add neutron heating tallies on
top of full fusion energy. Net wall-plug electricity is null/UNRESOLVED until
RF/heating efficiencies, thermal conversion, cooling, pumping, magnets and
other loads/deposits are independently sourced and reconciled.
