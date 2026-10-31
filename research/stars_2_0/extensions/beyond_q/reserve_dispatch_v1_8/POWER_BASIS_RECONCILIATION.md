# ARC D-D power / cost ancestry reconciliation — v1.8

## Newly located current design lock

Source: `ARC_DUAL_REACTOR_CANONICAL_BASELINE_2026-10-31.md` at
https://github.com/atlaslattice/open-regenerative-compute-standard/blob/6fb057618d6d6ff0ce813a99d9edf9d1485561d5/research/stars_2_0/extensions/beyond_q/ARC_DUAL_REACTOR_CANONICAL_BASELINE_2026-10-31.md.
An exact Git-blob-verified copy is preserved under `sources/`.

- Primary architecture: TWO ARC-class tokamaks, A D-D and B D-T, each with a
  proposed 1100 MW fusion source. Laser studies are separate variants.
- A's historical +20 MW net-electric projection is an owner-reported model
  input, not its fusion power and not a recovered whole-plant calculation.
- B's approximately 400 MW net comparator comes from the published approximately
  1.13 GW D-T ARC design, not an exact demonstrated 1.1 GW result.
- 10–15% refers to modeled modified **mass**, not cost. The 3% vessel reference
  retains an unresolved denominator; it must not become a plant CAPEX fraction.

This source corrects the October30 file's platform label without changing its
1100 MW fusion rating. v1.7 already separated ARC and laser. This release adds
the owner +20 MW electrical projection as a clearly labeled sensitivity; its
unknown-budget row remains unknown. Signed A net draw=-20MW means A net output
+20MW, not extra electrical input and not 20MW fusion.

## Earlier recovered record is not the current power basis

Source: draft PR36, head `12a3511691fc8b210a3763330ef96348ceac43fe`, archive
`research/stars_2_0/extensions/beyond_q/archive/COPILOT_RECOVERY_BASELINE_2026-10-29.md`;
its `models/assumptions_v0_1.json` and `deltas/RECONCILIATION_v0_1.md` were read.

That record explicitly describes an older A25MW primary-DD / B525MW scenario,
with a reported105MWth/-40MWe A chain whose detailed heating/electrical ancestry
was not recovered. The explicit `DD_heating_wall_power_MW` input is null. It
cannot substantiate the current1100MW/+20MWe operating point, nor be linearly
scaled into one. The v2.3 20MW-DD/80MW-RF screen is also a different scenario.

**Result of this investigation:** the architecture and owner projection are
source-traced. A's detailed heating, RF wall-plug, conversion, cryogenic, pump
and isotope-processing budget is still unresolved. No missing budget was invented.

## Cost scope retained without double counting

The current design lock records gross adaptation categories totaling $235M–$455M
and a conditional turbine credit of $150M–$250M. These are historical scenario
estimates, not quotations. The owner's approximately $300M recollection is a
retrofit-scale figure, not the purchase cost of both reactors. The alternative
$2.8B+$2.8B+$150M−$200M+$120M ledger sums to $5.67B; its previously written
$5.87B remains an ancestry discrepancy. Adaptation and isotope-plant line items
may overlap. No such conflicting schedules are stacked or converted into an
accepted finance model in this release.

Next required receipt: the original current-power operating-point sheet giving
A heating/current drive, efficiencies, all auxiliary loads, recovered heat and
conversion, with separately stated startup/off-state loads and thermal boundary.
Until that exists, +20MWe is a conditional projection and full costs stay null.
