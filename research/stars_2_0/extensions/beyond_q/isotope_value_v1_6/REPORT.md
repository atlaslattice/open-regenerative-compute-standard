# Beyond Q v1.6 — isotope coproduct accounting and electricity-cost thresholds

2026-10-31. New versioned package dependent on draft PR #54. The research
objective is an isotope-producing campus: A may consume electricity if usable
isotope output and other benefits justify its full cost. This package measures
conditional isotope quantities and the prices required to offset modeled
imports; it does not assume that a buyer or qualified product exists.

## What changed

The unchanged fuel-cycle engine replays A0/A1/A2 staged startup plus one full
B operating year. Tritium birth, internal consumption, blanket production,
transfers, decay and permanent losses remain separate. A new He-3 compartment
tracks direct D-D birth, collection holdup, capture losses, retained stock and
conditional terminal-sale allocation for He-3. Tritium is retained for D-T fuel and reserves by default. Every modeled T decay also creates one
He-3 atom, recorded separately and credited **zero recovery** here.

All sources use the inherited current dual-laser scenario identity: A=1.1 GW
**primary D-D**, plus additional candidate secondary D-T, B=1.1 GW D-T. These
are prescribed powers, not demonstrated laser yields. The historical
A=20 MW primary D-D / B=1.13 GW D-T remains an independent preserved reference.
No source power or recovery coefficient has been tuned to fund the campus.

## Direct capture is the core source, not tritium decay

The user correction is explicit: the intended retrofit captures the direct
D-D coproducts, with tritium feeding B and He-3 providing the principal saleable
coproduct. Decay-derived He-3 is a separate unavailable byproduct and supplies
no revenue or justification for this architecture.

`direct_capture_reference.py` reconstructs the older 500 MW A / 500 MW B scale
at 85% availability and 80% capture: approximately **45.945 kg of each captured
isotope**, or **341,443 STP liters of He-3**. That is consistent in scale with
the recalled roughly 350,000-liter result; its precise historical input file
has not yet been located. This reconstruction is not asserted to be that file.
The same atom count is 341,443 atom-equivalent liters for T, but **170,721 liters
of molecular T2**. Tritium is best budgeted in kg/atoms to avoid this factor of
two. Equal D-D branching means equal born atom counts, not equal molecular gas
volumes or equal delivered output after internal burn and recovery.

The current 1.1 GW primary-DD reference, 100% availability and 90% capture,
gives 133.780 kg each, approximately 994,201 STP L of He-3, before secondary
consumption and downstream losses. This direct-source screen supplies
approximately 72.127 kg more T than equal-power B burns per FPY, before those
remaining deductions. The dynamic simulations include their candidate internal
T burn and stock losses; no decay-produced He-3 is needed for the direct source.
Do not confuse this newer power case with the older 500 MW reconstruction.

## ARC, laser and the actual kinetic sample

Published ARC is a D-T tokamak concept [1]. Its main D-T reaction makes He-4,
not He-3. Any ARC He-3 account needs its D-D side reactions, tritium decay,
plasma conditions, residence and extraction. Hypothetical D-D operation of an
ARC-like chassis is not published ARC D-T performance.

Likewise, our archived WarpX 20 keV, 2 ps result is a frozen collision-box
sample, **not laser-target interaction or a demonstrated laser-driven yield**.
At matched primary D-D reaction energy it has approximately 4.20% more direct
He-3 atoms/J than the inherited equal-branch convention, with its own reaction
Q-values explicitly retained. This is a source-normalization comparison, not
a tokamak-versus-laser advantage. The 0.480957 T branch in that sample must
not silently replace the equal-branch assumption in the annual trajectories.

For a driver-specific comparison the required quantities are separate:

`He3 collected / wall-plug J = (He3 born / primary DD fusion J) × achieved primary-DD gain × laser efficiency × survival × recovery`.

This stationary shorthand is only applicable with matching time boundaries;
pulses require integration. Ion energy distributions affect the first factor,
while coupling/gain, residence, D-He3 secondary consumption and recovery affect
the rest. Current driver-specific factors are unresolved. WarpX supports
D-He3 reactions [2], but our archived network disabled that pathway. This
package consequently does **not** infer complete-network He-3 survival.

## Equations, units and conservative boundaries

- Direct He-3 atoms = primary D-D events minus T-branch events. Neutron and He-3
  coproducts identify the same branch; they are not independent source terms.
- Each decayed T atom produces one He-3 atom. Convert atoms to each isotope's
  own mass: m_He3=0.0030160293201/N_A kg [3], with the inherited
  m_T=0.00301604928/N_A kg. Equal atom counts are not equal isotope masses.
- For direct He-3 mobile inventory H [kg], `dH/dt = source - k_collect H`.
  The exact compartment operator integrates collection [kg], with capture
  fraction c going to stored stock and (1-c) to a permanent capture-loss ledger.
- Decay-derived He-3 from all modeled T stocks is inaccessible in this scenario:
  its source and unavailable inventory are both logged, without sales credit.
- Collection rate 1/day, capture fractions 0/0.5/0.9, retained He-3 fraction 0.5
  and terminal quality-acceptance factor 0.9 are **ASSUMED sensitivities**.
  No measured capture or purity is implied. No D-He3 burn is included; its
  omission can overstate survival and requires a coupled particle/energy model.
- He-3 terminal candidates = captured stored stock × (1-retained fraction) ×
  assumed quality acceptance. The remaining stock stays in retained/held bins.
- T external sales are disabled by default (`retain_for_DT`). Storage above an assumed reserve is reported separately and retained. Optional `sell_terminal` is a counterfactual accounting control, not the campus policy. Its terminal candidate = max(0, A storage + B storage - assumed reserve).
  Reserves 1/10/64.46 kg are sensitivity inputs, not qualified startup standards.
  T in plasma, blankets or processing cannot be sold by this allocation.
- Sales are evaluated only at the **terminal boundary**, after the complete
  modeled year. No atom burned that year is also sold. Such sales can impair
  the following year's operation: no indefinite-operation claim follows.

T closure is `DD birth + A blanket birth + B blanket birth = A burn + B burn +
decay + processing loss + permeation + mobile inventory change` for each
phase. Transfers cancel internally. He-3 closure includes direct and decay
birth, capture loss, collection holdup, stored allocation and inaccessible
decay inventory. Stored T is never treated as extra birth.

Actual revenue remains null without qualification, external demand and price.
The executable revenue function applies `min(candidate, qualified, demand) ×
price` and rejects qualification exceeding the disjoint candidate allocation.
No extra energy or heat credit is claimed for these products.

## Numerical screening results

One B operating year, with A running continuously, gives the following
conditional source ledger (kg; excludes the preceding A-only startup):

| Quantity | A0 | A1 | A2 |
|---|---:|---:|---:|
| Direct D-D T birth | 148.645 | 148.645 | 148.645 |
| Direct D-D He-3 birth | 148.644 | 148.644 | 148.644 |
| A secondary D-T T consumption | 7.755 | 7.755 | 7.755 |
| B D-T T consumption | 61.654 | 61.654 | 61.654 |
| A blanket T birth | 0 | 125.193 | 145.517 |
| B blanket T birth | 64.375 | 64.375 | 64.375 |
| T decay | 3.827 | 6.953 | 7.460 |
| T permanent processing loss | 7.168 | 19.680 | 21.711 |
| Total mobile T stock change | 132.617 | 242.171 | 259.956 |

Blanket quantities inherit unqualified simplified-neutronics response and
assumed recoveries; they are **not qualified usable surplus**. He-3 birth is
the same across these three cases because their primary D-D source is the
same. Real He-3 destruction and capture differences have not been resolved.

A1 including its 48-hour startup, at assumed 90% capture, 50% retention and
90% quality acceptance:

| He-3 category | kg |
|---|---:|
| Direct gross birth |149.458|
| Additional birth from T decay, inaccessible |6.953|
| Collection holdup |0.407|
| Capture loss |14.905|
| Retained captured stock |67.073|
| Terminal quality hold |6.707|
| Terminal sale candidate, unqualified |60.366|

A1 has approximately 242.245 kg T in terminal storage, all retained for future
D-T fuel and reserves. A 10 kg assumed reserve leaves 232.245 kg above that
arbitrary reserve, but external T sales remain zero. Other pipeline inventory
is held separately. These large stocks depend strongly on inherited blanket
assumptions and do not establish qualified or indefinitely renewable surplus.

## What would cover the electrical sink?

With assumed gain 10, laser efficiency 20%, captured fusion fraction 90%,
conversion 40%, combined auxiliaries 50 MW and import price $0.10/kWh, A1's
startup plus B-year import charge is approximately **$270.902 million**.
Under the full-sale assumption, the terminal candidates would require:

| Electricity-cost boundary | He-3 alone | T allocation |
|---|---:|---|
| Campus net import charge |$4.488 million/kg|Retained for D-T, no sales credit|
| A's laser electrical input charge only |$8.031 million/kg|Retained for D-T, no sales credit|

These are **required price thresholds, not market quotations**. The A-only
charge ($484.770 million) is an alternative gross-input screening boundary,
not an additional charge to add to the campus net import charge. Generation
and A/B electrical allocation must not be counted twice.

Default revenue screening uses He-3 only; the following general frontier supports a separately requested counterfactual T sale. In the default, T_sale_candidate=0:

`P_He3 × min(H_candidate,H_qualified,H_demand) + P_T × min(T_candidate,T_qualified,T_demand) >= selected electricity charge`.

No prices or demand curves are supplied. Full facility cost also includes
capital, replacement, maintenance, isotope separation and storage, financing,
campus loads and other unmodeled expenses. Positive revenue after electricity
alone would not establish profitability. Terminal sales also cannot finance
startup without a separately modeled funding/timing arrangement.

## Evidence, verification and next decisions

SOURCE-TRACED: pinned code/data manifest, archived WarpX sample and [1]–[3].
VERIFIED-DERIVED: conditional source/stock/allocation identities and normalization.
POTENTIAL-DERIVED: reactor-scale production, recovery and required-price scenarios.
UNRESOLVED: ARC-versus-laser performance, achievable gains, D-He3 consumption,
qualified recovery/purity/demand, full costs and sustained operation.

Twelve new tests pass, covering zero sources, zero capture, an independent
analytic collection solution, isotope mass conversion, T/He-3 disjoint terminal
allocations, demand caps, missing qualification, zero-inventory thresholds,
T conservation and source normalization. All physical G1–G5 remain OPEN.

Three questions must remain separate: fuel sufficiency, electrical autonomy
and commercial viability. Buying electricity with isotope income could support
an energy-consuming refinery; it does not make that refinery electrically
self-sufficient. Finite positive stocks cannot establish indefinite operations.

Next: source-qualified D-D laser distributions and absorbed/incident energy;
paired D-He3 and D-T slowing/escape calculations; qualified gas extraction and
purity; terminal-sale impacts on the second operating year; external isotope
demand/price curves and joint full-cost allocation.

## Reproduce

From this directory, Python standard library:

```bash
python account.py
python direct_capture_reference.py
python -m unittest test_account -v
```

Optional `python plot.py` requires matplotlib (figure generated with 3.10.8).
Inputs and every dependency are pinned by Git blob and SHA256; numerical execution
fails on changed source bytes. No OpenMC or WarpX executable is needed for this
replay. Outputs include 6 phase ledgers, 27 terminal allocations, 486 price
thresholds, daily He-3 stocks, source comparisons and test/execution logs.

A provenance correction is retained: the preceding v1.5.1 source-hash list
hashed recovered working copies with an additional terminal newline in some
files. This changes hashes, not numerical meaning. This release verifies exact
canonical Git bytes before running, records both Git and SHA256 hashes and
preserves the earlier artifact rather than silently replacing its hash list.

## Sources

[1] Hillesheim, J.C., Creely, A.J., Eich, T.H., Howard, N.T., Leuthold, N.,
Sweeney, R., LeViness, A., Nelson, A.O., Nichols, L. and Tinguely, R.A. (2026).
*Overview of the physics basis for the ARC fusion power plant*. Journal of
Plasma Physics. Published 4 June 2026. DOI:
https://doi.org/10.1017/S0022377826101706. Used to distinguish D-T tokamak physics
from the proposed D-D isotope source; no ARC He-3 production value is borrowed.

[2] WarpX contributors. *Inputs: Parameter List*, nuclearfusion collision model,
WarpX 26.10 documentation, https://warpx.readthedocs.io/en/26.10/usage/parameters.html.
Accessed 31 October 2026 (current documentation also inspected). DD/DT/D-He3
support does not establish that a particular input enabled all three channels.
Actual source values here come from the repository's pinned v1.3 sample, not
from a new kinetic run. Its original report preserves algorithms and Q-values.

[3] NIST Physical Measurement Laboratory. *Atomic Weights and Isotopic
Compositions for Helium*,
https://physics.nist.gov/cgi-bin/Compositions/stand_alone.pl?ele=He.
Accessed 31 October 2026. He-3 relative atomic mass 3.0160293201(25) supplies the
molar-mass approximation used consistently for recovered neutral isotope mass.

Dave Sheldon / Atlas Lattice supplies the research direction, including the
isotope-factory and campus-sustainability objectives. GPT-6/Tidal Lantern,
DeepSeek and Gemini Argon retain credit for their documented analytical
contributions. WarpX contributors retain code/algorithm credit. No laboratory,
university, company or cited author endorsement or experimental validation is
implied.
