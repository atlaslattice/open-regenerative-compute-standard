# Beyond Q placement and integration map

2026-10-29. Beyond Q is a STARS / Stellar Forge extension, not a separate project. Its present deliverable is an auditable D-D refinery / D-T power campus accounting checkpoint. It is not integrated into the existing Stellar Forge CLI or UI, and adds no calibrated tokamak solver.

## Existing material inspected before placement

All links are immutable snapshots in atlaslattice/open-regenerative-compute-standard. These draft PRs remain unmerged; this extension does not merge or supersede them.

| Existing material | Inspected source | Relationship |
|---|---|---|
| Stellar Forge v1.1 README | [PR35 snapshot](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/80430c859c57c10222e2673f680811584f31ce64/research/stars_2_0/implementation/stellar_forge_reference_v1_1/README.md) | Existing CLI/UI and separate synthetic physics/economics slices. Full isotope recovery remains a deferred gate in that version. |
| Integration contract v1.1 | [Contract](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/80430c859c57c10222e2673f680811584f31ce64/research/stars_2_0/implementation/stellar_forge_reference_v1_1/INTEGRATION_CONTRACT_CANDIDATE_v1_1.md) | Four evidence gates, provenance and BORN→EXIT→ACCEPTED→DELIVERABLE→REALIZED. Beyond Q's isotope-survival and recovery stages refine its own physical accounting; they do not redefine detector acceptance. |
| Grid-assisted operating tracks | [PR19 snapshot](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/d2166e4b224720e62735eaea5d1a4f4ef298257b/research/stars_2_0/implementation/energy_screen_v0_1/OPERATING_TRACKS_v0_2_2026-10-28.md) | Net electrical balance and economic margin remain distinct; supplemental wall power, heat recovery and internal transfers must close. |
| Multi-reaction product registry | [PR17 snapshot](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/37d8da263450610715fe493748c8ab3ec052c30f/research/stars_2_0/implementation/product_registry_v0_1/README.md) | Existing He-3/T/He-4 identities and decay relationships. Registry membership supplies neither a yield nor a qualified price. |

## Extension boundary

- Existing p–B transport/detector/source results retain their original scope. They do not calibrate D-D tokamak performance.
- Beyond Q introduces conditional primary-reaction isotope ledgers, paired-campus ancestry, ARC table reproduction and unresolved energy/cost requirements.
- Future adapters should use shared product IDs and evidence schemas after compatibility checks; this checkpoint does not import draft implementations or silently upgrade their evidence.
- Internal helium allocation is not demonstrated campus use or merchant revenue. Prompt neutrons remain transport/heat liabilities unless an explicit module qualifies a benefit.
- SHUGS/governance/operator material is outside this extension's physical model.

## Publication ancestry

The first commit in this review archives only the supplied historical recovery paper at this STARS location. The second adds corrected descendants, source receipts and calculations. The archive retains $5.87B and other disputed figures. Local preparation had used research/beyond_q in an unpublished branch; the publication destination is research/stars_2_0/extensions/beyond_q. No published files were removed or moved.

## Next technical work

Recover the missing 25 MW D-D energy ledger and derive a coupled reaction/extraction/inventory model. Qualify separation and exhaust scope/cost before running financial scenarios. A future Stellar Forge adapter must carry unresolved fields and assumption provenance through to reports rather than treating these accounting fixtures as physical predictions.
