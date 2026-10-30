# Beyond Q — canonical power-basis lock (2026-10-30)

STATUS: USER-CORRECTED DESIGN INPUT; not validated reactor output.

## Reactor identities
- Reactor A: D-D LASER reactor, **1.1 GW GROSS FUSION POWER**. Historical **~20 MW NET ELECTRICAL OUTPUT** is an electrical-ledger assumption ONLY, never the D-D fusion source term.
- Reactor B: D-T LASER reactor, **1.1 GW GROSS FUSION POWER**. Net electrical power is to be independently calculated.
- Laser/plasma operating point, confinement, wall-plug gain, tritium recovery, and sustained operation: not yet demonstrated.

## Mandatory unit names
Use `A_gross_fusion_W = 1.1e9`, `A_net_electric_W = 20e6 (historical assumption)`, `B_gross_fusion_W = 1.1e9`. NEVER substitute the second for the first in reaction-rate or isotope-yield calculations.

## Continuous 365-day ideal physics-only baseline
Assume equal D-D branches, Q_DD_mean=3.65 MeV per D-D reaction, Q_DT=17.6 MeV, no secondary reactions, 100% availability before recovery and separation losses.
- T born in reactor A: ~148.5 kg/y.
- He3 born in reactor A: ~148.5 kg/y.
- T burned in reactor B: ~61.6 kg/y.
- T production / consumption: ~2.41, prior to recovery losses.
- At 90% T extraction/transfer: ~133.7 kg/y recovered, ~72.1 kg/y nominal excess before decay, delays, processing, reserves, startup requirements, and other losses.
- At 90% He3 recovery: ~133.7 kg/y recovered He3.

All are conditional stoichiometric figures at ASSUMED gross fusion outputs; these are not WarpX laser simulations, net-energy results, or an indefinite-operation demonstration.

## Provenance and conflict control
Older Beyond Q branches used A=20 MW as a *gross D-D fusion* scenario, and B=1.13 GW. These older inputs are **historical scenarios, NOT the current user-selected two-laser design**. Keep them versioned; do not silently replace their historical test fixtures. All new two-laser coupling calculations must use this canonical lock, explicitly state input power bases, and flag contradictory inputs as an error.
