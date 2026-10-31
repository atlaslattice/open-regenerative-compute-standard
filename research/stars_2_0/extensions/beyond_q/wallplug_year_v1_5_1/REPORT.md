# Beyond Q v1.5.1 — staged-year electricity accounting

2026-10-31. Additive continuation of draft PR #54. This package connects the
unchanged v1.4.1 A1 staged startup to the v1.5 electricity adapter. It replays
48 hours of A-only operation followed by one 365.25-day B operating year
(8,766 hours); A continues throughout. All archived trajectory fields reproduce
exactly. This is not a new WarpX run, a laser-gain calculation, or physical
validation of a reactor.

## Power configuration and evidence

The inherited `dual_laser_1100_1100` scenario specifies A at 1.1 GW **primary
D-D** fusion and B at 1.1 GW D-T fusion. A secondary D-T energy is additional.
The historical A=20 MW primary D-D / B=1.13 GW D-T configuration remains a
separate preserved research case and is not replaced by these results.
The hypothetical blanket yields, extraction/recovery and plasma parameters
are inherited unchanged. No outages are introduced in this reference case.

SOURCE-TRACED: repository scenario inputs, startup policy, archived trajectory,
and executable v1.4/v1.5 code at commit
`3ed8d2029f14c4446527a53ed84c3114cc55c3fe`. File hashes are retained in
`outputs/source_sha256.json`. These trace the computational inputs; they do
not turn assumptions into measurements. The underlying literature and
limitations remain in the preceding versioned reports and source registers.

VERIFIED-DERIVED: exact archived replay; clock conversion; energy partitions
and interval accounting identities conditional on the stated inputs.
POTENTIAL-DERIVED: all reactor-scale electricity and import-charge scenarios.
UNRESOLVED: actual laser gain, target coupling, engineering efficiency, qualified
isotope supply, market value and profitability. Physical G1–G5 remain OPEN.

## Energy and import boundaries

Each hourly energy input uses differences of cumulative nuclear counters,
not repeated summation of cumulative production. The engine internally steps
at 15 minutes. With tritium atom mass m_T=0.00301604928/N_A kg:

- Primary D-D energy = delta(T birth mass)/m_T × 2 × 3.65 MeV under the
  inherited equal-branch convention, checked against prescribed power × uptime.
- A secondary and B D-T energy = their respective consumed T atoms × 17.6 MeV.
- Optical input = A primary D-D energy/G_A plus B scheduled target energy/G_B.
- Laser electricity = optical input / assumed wall-plug efficiency.
- Generated electricity = total fusion Q × assumed capture × assumed conversion.
- Net electricity = generated electricity minus laser electricity and auxiliaries.

No extra neutron kinetic energy or blanket reaction-Q multiplier is appended.
The v1.5 energy convention uses 17.6 MeV, not a silent switch to the 17.59 MeV
candidate equation. The inherited fusion-counter normalization is unchanged.
B scheduled drive is charged while B is on; B is off during precharge. The
combined 50 MW auxiliary assumption is charged throughout both phases; a
source-qualified A/B split and shutdown loads remain unresolved.

Hourly imports = max(0, -net energy) and positive electricity = max(0, net
energy), summed separately. Annual positive energy cannot erase an earlier
import without an explicitly modeled storage or settlement mechanism.
Intrahour import peaks remain unresolved because these are hourly averages.
Positive electricity is before campus loads and is not qualified export.

## Conditional results

All cases retain assumed capture=90%, thermal conversion=40%, combined
auxiliaries=50 MW. A/B gains are equal here; neither these gains nor the
10%/20% laser efficiencies are achieved-device claims.

| Assumed gain / laser efficiency | A-only startup average net | B-year average net | Startup imports | B-year imports |
|---|---:|---:|---:|---:|
| 10 / 20% | -154.193 MW | -308.193 MW | 7.401 GWh | 2,701.616 GWh |
| 100 / 20% | +340.807 MW | +681.807 MW | 0 GWh | 0 GWh |

At an **assumed** import price of $0.10/kWh, the gain-10/20% case incurs
approximately $0.740 million startup import charge and $270.162 million over
B's year. These are electricity charges only, not isotope production costs.
No isotope revenue, export credit, capital recovery, replacement, financing,
maintenance or profit is imputed. Prices of $0.05/$0.10/$0.20 are sensitivity
inputs, not market quotations. Internally consumed T remains unavailable for
external sale. An energy-consuming isotope refinery is a valid research
objective; commercial viability requires qualified recovery and demand.

## Reproduce and tests

Python standard library only. From this directory:

```bash
python year.py
python -m unittest test_year -v
```

The neighboring versioned modules and inputs must remain at their repository
paths. Seven tests pass: archived replay, phase clocks, zero B energy during
precharge, energy/import balance, counter reversal rejection, daily aggregation,
and explicit absence of qualification/profit claims. No invented result is
used to close a missing physics gate. Maximum fuel mass residual is about
5.66e-11 kg; unserved B burn is numerical roundoff (~5.70e-15 kg).

Outputs: 12 phase/scenario rows, 36 import-price sensitivities, and 368 daily
bins for the gain-10/20% reference (the final day has 6 hours). Counter energies
are computed hourly before aggregation. The complete original stock trajectory
is preserved in v1.4.1 rather than copied or overwritten.

## Next work

1. Qualify laser pulse energy, repetition rate, gain basis and achievable ranges.
2. Add independent A/B auxiliaries and campus loads; model storage before
   describing time-separated production as energy autonomy.
3. Extend this adapter to adverse outage and zero-breeding trajectories.
4. Track He-3 birth, capture, purity, storage and external demand; allocate joint
   costs once across retained fuel, saleable isotopes and usable energy.
5. Reconcile all costs and uncertainties before a commercial conclusions paper.

Dave Sheldon/Atlas Lattice supplied the research direction and isotope-factory
objective. GPT-6/Tidal Lantern, DeepSeek and Gemini Argon analytical contributions
remain credited as documented in prior source registers. This implementation
adds temporal electricity accounting; it claims no institutional endorsement
or experimental validation.
