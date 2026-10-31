# Beyond Q v1.5 — wall-plug coupling checkpoint

October 30, 2026 (America/Chicago). Additive checkpoint on PR #52; no historical
release overwritten. **Scenario energy integration is implemented; physical
laser and economic calibration remain unresolved.**

This adapter reads all27 current dual-laser A0/A1/A2 eight-hour results from
v1.4. It derives primary DD, internal secondary DT and actual B DT reaction
energies from their modeled reaction/mass counters, checks the primary-DD
power normalization, and applies explicit assumed laser/electrical scenarios.
It does not run a new laser/plasma simulation or establish an achieved gain.

## Equations and boundaries

- A primary DD Q: equal-branch3.65MeV convention, independently reconciled to
  the prescribed1.1GW gross DD source. The historical20MW electrical assumption
  is never used as this source.
- A secondary DT Q: consumed A tritium atoms times17.6MeV, counted separately.
  A total reaction energy includes both; A primary-DD target gain is explicitly
  defined against primary DD Q only. A total-fusion-gain convention would
  require a different input and cannot be mixed with this one.
- B DT Q: actual consumed B T, not scheduled demand, times17.6MeV.
- A optical laser energy=primary-DD Q/G_A; B scheduled optical budget=
  prescribed B target power×ON duration/G_B. Default scheduled drive continues
  to cost electricity in unfueled cases. Optional fuel-adaptive drive is a
  separate optimistic policy, not a measured control capability.
- Laser electrical input=optical input/laser wall-plug efficiency.
- Formal gross electricity=sum of fusion Q×assumed captured fraction×assumed
  thermal/electrical conversion. No extra neutron energy or blanket-Q
  multiplier is appended. Capture/conversion are not transport-qualified.
- Net electricity=gross electricity−both laser inputs−explicit auxiliary load.
  Positive electricity is before campus load, not qualified export. Negative
  net electricity is modeled import. Neither can be allocated twice.

The1.1GW A input means primary DD fusion in these inherited numerical scenarios;
secondary DT contributes additional modeled Q. This convention must be checked
against any future proposal specifying a fixed *total* A fusion power instead.

## Exploratory inputs, not technology forecasts

Equal A/B target gains1,10,100; laser wall-plug efficiency10%/20%; captured
fusion fraction90%; conversion40%; combined auxiliary load50MW. These are
**ASSUMED sensitivity bounds**, not measured values or recommendations. Every
real input remains to be source-qualified. The adapter rejects missing gain,
missing efficiency, unknown gain basis and invalid power normalization.

162 energy rows cover six energy scenarios×27 fuel cases. Eighteen price
sensitivities use assumed$0.05/$0.10/$0.20 per kWh, not current market quotes.
No isotope prices or market demand values are invented; profit, qualified
isotope revenue and total production cost stay null.

For continuous A1, the assumed gain10/laser-efficiency20% case gives~−308MW
net before campus loads. Gain100/20% gives~+682MW under the same capture,
conversion and auxiliary assumptions. This illustrates how assumptions can
change the sign; it is not an achieved reactor result. Nuclear-fuel arithmetic
can be positive while electrical balance is negative.

DD laser input charge per *gross born T kilogram* assigns all DD laser input to
that screening denominator. It is **not** a complete isotope production cost:
no He3/heat coproduct allocation, qualified recovery, CAPEX, maintenance,
replacement, financing, downtime or campus electricity opportunity cost is
included. Do not separately assign the entire joint DD cost to both T and He3
and then sum it. Internal T fuel value and external T sales must use disjoint
atoms. `allocate_T` rejects consumption+sales+reserves exceeding availability.

## Reproduce and verify

Python standard library only, from this directory:

```bash
python ledger.py
python -m unittest test_ledger -v
```

Nine checks pass. Source-linked calculations are POTENTIAL-DERIVED because the
fusion powers and laser/engineering assumptions are unqualified. Numerical
energy partitions, unit checks and allocation identities are VERIFIED-DERIVED
conditional on those inputs. All physical G1–G5 remain OPEN.

Read HANDOFF.md before continuing. The next paper can describe these methods
and results; it must not claim profitable isotope manufacturing, achieved
laser fusion, qualified surplus or electrical autonomy.
