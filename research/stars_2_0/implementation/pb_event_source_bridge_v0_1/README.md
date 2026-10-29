# Stellar Forge p–B event-source bridge v0.1

2026-10-28 America/Chicago. New source derivation and conditional reaction-yield screen; originals untouched. SOURCE_REPRODUCED table extraction / publication-model-derived event observable. Not a calibrated Stars prediction, physical event sampler or net-energy result.

## What was recovered

The primary publisher's three Sikora–Weller tables were acquired. Their 59 rows contain alpha1 and alpha0 angular coefficients. Applying the paper's prescribed 4*pi/3 factor to A0 (and adding the tabulated channel components where applicable) gives 41 event-cross-section nodes, with mb converted to barn. This is a NEW dataset, not division of the restricted Spraker observable by three. The underlying spectrum extrapolation and selected reaction-model assumptions remain part of its provenance; it is not raw model-free experimental evidence.

At 0.65 MeV LAB, the derivation gives 1.3982152382 barn. At higher energies the alpha0 coefficient is included where table 3 supplies it. Untabulated low-energy alpha0 is not claimed independently measured zero. Statistical error calculations expose both independent-channel-fit quadrature and a maximum positive-correlation bound; source inter-channel covariance is unavailable. Do not silently treat either as a recovered full likelihood.

Primary: M.H. Sikora and H.R. Weller, J. Fusion Energy 35, 538–543 (2016), https://doi.org/10.1007/s10894-016-0069-y . Source table fragments are redistributed under CC BY 4.0, https://creativecommons.org/licenses/by/4.0/ ; authors credited, surrounding publisher webpage omitted. SOURCE_INDEX records full-page and extracted-table hashes and transformation. Tables are source data; project code licensing does not relicense them.

The 0.162 MeV narrow feature is not resolved by the tabulated grid. This release accepts exact source nodes only, avoiding an invented interpolation across it. No resonance fit, channel angular sampler or Maxwellian rate curve is supplied. Table angular distributions alone are insufficient for a correlated three-alpha event generator.

## Important source-lineage discrepancy

The archived C2973002 central values closely reproduce the new event derivation at 40 shared energies: maximum absolute difference 0.00002514194 barn. This numerical relationship challenges an overly categorical interpretation that all those archived values are necessarily the unreanalyzed restricted-window yield. The original EXFOR bibliography explicitly includes the 2016 evaluation/Legendre-polynomial reference, despite its subentry's 2012 citation. Its source lineage therefore requires renewed review.

One explicit energy disagreement is preserved: the publisher table lists 0.25 MeV; the archived record lists 0.26 MeV for the nearby point. The uncertainty conventions also differ: e.g., the table-derived A0 statistical error at 0.65 MeV is about 0.002876 barn, whereas the archived error is 0.0476262 barn. Neither an energy correction nor an uncertainty reinterpretation is made silently. The earlier CSV, source-type guard and negative findings remain intact. Numeric similarity is evidence to investigate, not permission to collapse sources into independent measurements or overwrite metadata. The two records share experimental ancestry; they are NOT independent validation datasets.

See receipts/run001/ARCHIVE_COMPARISON.json for the 40 comparisons. The original master's target systematic is 3.6%; the 2016 paper discusses a different systematic convention for its rate analysis. No common universal covariance is asserted across both records.

## Conditional yield calculation

thin_target.py now calculates expected reaction counts and probability of at least one fusion event from a source-defined event cross section, an assumed fixed-energy proton count and an assumed B11 areal atom inventory:

- optical depth tau = sigma_event * B11_atoms_cm2 * 1e-24;
- event probability per proton = 1-exp(-tau);
- expected event count = Np * (1-exp(-tau));
- at-least-one-event probability = 1-exp(-Np*tau), conditional on the stated independent identical protons.

This is a homogeneous fixed-energy attenuation screen with one reaction removing each proton. It omits stopping, energy spread, competing channels, target evolution, collective effects and depletion. Supplied areal inventory does not establish a target physically thin enough for negligible energy loss. The example inventories/counts are deliberately assumed scenarios, not apparatus specifications. No acoustic enhancement factor is inserted.

For a synthetic fixed mean proton count of 1 million, the example useful-event probability is 0.752963. A hypothetical equal mixture of zero and 2 million protons has the SAME expected event count but useful-event probability 0.469486. This illustrates why a distribution and useful-shot probability matter; it is NOT a measured acoustic effect or a universal guarantee about every output threshold. All zero-proton attempts remain included.

## Reproduction

Python standard library only. From this directory:

```bash
python run_bridge.py --out receipts/new_run_name
```

Output directory must be new. The runner checks source-fragment hashes, reconstructs coefficients and event values, runs nine tests and emits conditional examples and a receipt. No RNG/network needed. Raw primary HTML pages are retained locally; their table fragments are the portable inputs. Run001 derivation/archive comparison is preserved; run002 is the authoritative portable runner receipt. No PDF visual verification is claimed: numerical PDF text was cross-checked at sample anchors, but the available web screenshot interface did not return usable pixels.

Next: resolve energy/uncertainty lineage, constrain actual target stopping/source distribution, implement mass-correct correlated events and detector transport. Our full apparatus module catalog is retained separately; unavailable modules stay BLOCKED or PARAMETRIC, not quietly removed or assigned zero effect. Scientific freeze remains pending.
