# Stars operating modes, necessary energy screen and component costs v0.1

2026-10-28. PHYSICAL_CANDIDATE / SYNTHETIC SCREEN. New additive release. No ignition, measured net electricity or economic viability result.

## Two grid-powered alternatives, plus the current reference

- SINGLE_PASS_DRIVEN: externally driven beam–target reference experiment. No self-sustained burn presumed.
- STARTUP_THEN_BURN_HYPOTHESIS: grid-powered preparation/startup followed by a declared burn interval without sustaining drive. Auxiliary power may remain. The hypothesis requires a separate time-dependent validated physical model, not a renamed beam-target calculation.
- CONTINUOUSLY_DRIVEN: grid-supported source/heating throughout operation. Can be useful for research/manufacturing even with negative net electricity. It is not labeled ignition merely because reactions occur.

All modes include startup electricity and the declared full-cycle duration. Report target gain, plasma heating, wall electricity and delivered output using distinct denominators. Ignition definitions vary by context; each future study must state its physical criterion and duration. The user's direction includes both startup and continuous-drive scenarios.

## What this screen computes

For supplied fusion energy F, self-heating fraction h, collected fraction c, and collected-energy-to-load efficiency eta:

- alpha self-heating = h F;
- gross electrical output = c eta F;
- net electrical output = c eta F - startup wall input - sustaining wall input - auxiliary wall input;
- necessary fusion energy for electrical breakeven = total wall input / (c eta), undefined if c eta is zero.

Require h+c<=1: the same alpha energy cannot heat the fuel and reach an external collector. Remaining alpha energy and collector losses are displayed; neither is credited as recoverable heat. This release screens the principal p–B three-alpha energy channel; it is not a universal energy partition for neutron-producing reactions. Fusion energy is an externally supplied assumption, not a prediction of this module. A high assumed F can make a positive result by construction.

This is a necessary gross accounting screen, not proof of ignition or a complete power-cycle solver. It does not calculate plasma losses, source coupling, hydrodynamics, stored-energy changes or nonfusion energy recovery. Comparison assumes the apparatus returns to a consistent stored-energy state; unresolved startup/field/thermal inventory changes block a physical net-power claim. Internal recirculation must not become a second exported-energy credit. Sustaining input must not be hidden in another category to claim drive-off operation.

The separate burn model must eventually evolve alpha deposition, electron/ion exchange, radiation, expansion/confinement, transport, fuel/ash inventories and external drive, with independent tests and experimental constraints. Acoustic inputs must be measured target/source changes with their own power, never assumed nuclear multipliers. No beam-target reference output is relabeled a burn prediction.

## Modular capital inputs

COMPONENT_TEMPLATE_v0_1.json lists source, target/feed, acoustic apparatus, chamber/vacuum, diagnostics, shielding, cooling, collector/converter and product-handling assets. Include hardware versus installed cost, dated source, capacity, power, lifetime/replacements, maintenance, availability, installation scope and uncertainty. Actual cost fields remain null. No component estimate has been invented.

costs.py sums explicitly supplied USD installed costs once per physical asset. Unknown costs block a total; known subtotal remains visible. Shared cooling/vacuum assets need a single physical ID and an explicitly justified allocation rule. Do not add purchased hardware again if already included in installed cost. Financing, inflation/currency rebasing, learning curves and replacement scheduling are not calculated by this release. Capacity-dependent pricing and correlated uncertainty need source-qualified follow-up.

Connect economic_reporting_v0_1 to future experiment adapters for separate scientific outcome, net electricity and coproduct/cost scenarios. This release does not retrofit old engines or freeze a plant design.

## Baseline reconciliation status

At main commit 4512e9bb8505591ea207d28c2f0689ab5aecae9f, a filename inventory did not locate the original later Gemini engine v0.4 standalone Python or source ZIP. That is not an exhaustive content search or proof the attachment is lost. Tidal's prior execution report remains evidence of its execution; GPTWork's exact local reproduction remains OPEN. Do not substitute the older surrogate and claim the later engine reproduced. Next recovery should use the source attachment/archive and reconcile its documented hash mismatch.

## Reproduction and sources

Run python -m unittest -v from this directory. Standard library, Python 3.12.14, no random numbers or live data. Eleven tests cover explicit energy arithmetic, zero fusion/conversion, startup inclusion, invalid inputs, partition double counting, hidden sustaining drive, conditional positive output without ignition promotion and cost completeness/duplicate assets.

Conceptual source references, not calibration data:
- LLNL target versus fuel gain definitions: https://lasers.llnl.gov/sites/lasers/files/2025-03/03_Present-Understanding-of-Ignition-And-Gain-Using-Indirect-Drive-Inertial-Confinement-Fusion-Target-Designs-On%20The-US-National-Ignition-Facility-Omar-Hurricane.pdf
- Ochs et al., bremsstrahlung constraints in specified p–B inertial-fusion models: https://par.nsf.gov/biblio/10695120-bremsstrahlung-constraints-proton-boron-inertial-fusion
- UKAEA cost-model uncertainty: https://scientific-publications.ukaea.uk/papers/fusion-power-plant-cost-modelling-uncertainties/

No numerical facility quote or physical gain estimate is imported from these references. Published constraints must be reproduced within their assumptions before comparing a different configuration.
