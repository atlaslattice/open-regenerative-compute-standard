# Stellar Forge — finite alpha-transport controls v0.1

2026-10-31. Additive continuation of draft PR57, commit `d35d31a95253ed91a942236ecf500a14acc74ec8`. No merge, apparatus relabeling or scientific freeze. **Net electrical output remains unevaluated.**

## Recovery before geometry

The current GitHub versions of these two original reference digests were read again; their Git blob identities are in SOURCE_RECOVERY.json:

- [DeepSeek hybrid boron-target fabrication follow-up](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/main/research/stars_2_0/reviews/DEEPSEEK_V08_HYBRID_BORON_TARGET_FABRICATION_FOLLOWUP_2026-10-27.md).
- [DeepSeek cross-domain engineering audit](https://github.com/atlaslattice/open-regenerative-compute-standard/blob/main/research/stars_2_0/reviews/DEEPSEEK_V08_CROSS_DOMAIN_ENGINEERING_AUDIT_2026-10-27.md).

They distinguish a candidate 4–6 micrometre reaction film from printed supporting hardware, require the actual backing and whole stopping stack, and do not provide the original particle-pocket dimensions/composition/packing. They are attributed reviewer digests, not recovered complete drawings or new experimental data. Historical P1/P2/P3 suggestions are not substituted for the original pocket. ORIGINAL_POCKET_INPUTS.json explicitly retains missing values. Supplying arbitrary values would not establish a qualified adapter: apparatus_gate distinguishes missing inputs from a complete-but-unqualified profile.

## What this release adds

A three-dimensional, straight-ray finite uniform-box boundary calculation, separate from the infinite-slab control. Coordinates are **material column coordinates**: q = n*r, with q in atoms/cm2, n in atoms/cm3 and r in cm. A uniform number density cancels from geometric aspect ratios and path columns, so this control needs no invented physical density or length. It does NOT yield SI positions or transit times without additional physical information.

The unchanged 4096-event bank from PR57 run003 supplies all three correlated alpha four-vectors and all five conditional model weights. It also fixes every local reaction contribution and depth. Birth positions follow the mean incoming proton ray in relative column coordinates: (d*ux/uz, d*uy/uz, d). This is a centroid-ray control, not a recovered finite beam profile. The beam entry point is the center of the front face by numerical construction. A geometry that places any birth outside the box is rejected, never silently clipped or renormalized.

Normal column stays at 1e18 11B atoms/cm2, with widths 2, 10, 100 and 1,000,000 times the normal thickness. These dimensionless choices are numerical controls, not proposed apparatus dimensions or measured target parameters. Every control uses the SAME reaction count and bank: this is a postprocessor comparison, not a rerun of the proton source, laser, material evolution or reaction-depth calculation. No new fusion enhancement, acoustic term or gain factor is applied.

## Results

Exploratory coherent l1+l3 case, conditional on the inherited source and cold stopping model:

| Width / normal thickness | Resolved escaping kinetic energy (weighted MeV) | Difference from infinite slab |
|---:|---:|---:|
| 2 | 0.1514654950 | +1.6525% |
| 10 | 0.1506061460 | +1.0757% |
| 100 | 0.1494157274 | +0.2768% |
| 1,000,000 | 0.1490032470 | 0 |

The fixed birth kinetic energy is 0.1522944597 weighted MeV and expected reactions are 0.01628033146332977. A higher escaping-energy value here means shorter material paths to side boundaries; it is **not more fusion** or demonstrated electrical recovery. No ranking of physical target designs follows from this control. Five source variants are retained in the machine-readable results; the coherent variant is shown here to explain one consistent comparison, not selected as the best source. The inherited source remains an uncalibrated local-energy extension of an isolated unpolarized 2-minus model. Physical model uncertainties and unknown beam-profile effects are not estimated by these four aspect ratios.

All 17 refined-run checks pass, including per-alpha energy conservation, fixed event weights, nonincreasing escape with wider boxes, stopping-grid refinement, endpoint reconstruction and recovery of the saved infinite-slab result. The largest stopping-grid discrepancy is 0.292 eV, below the unchanged 1 eV gate, with no resolved/unresolved status changes. Twenty-two geometry/material-boundary unit tests pass, including 500 seeded independent random rays, scale/translation covariance, first-boundary checks and corner reporting. The 161 saved-bank audits pass. Repeated run002/run003 scientific JSON and every array reproduce exactly (elapsed runtime excluded; NaNs compared as missing values).

## Boundary and energy semantics

Cold ELEMENTAL 11B only; same calculated SRIM13 + ZBL_SIMNRA_7_04 stopping prescription and positive 0.004002603 MeV alpha floor as PR57. This is not a measured stopping curve and is not silently reused for BN, B4C or an unidentified ceramic. All source/mass/stopping references and limitations are inherited without modification. No scattering, straggling, sheath fields, granular transport, target heating, porosity, backing or frame is represented.

Every alpha retains:

`birth kinetic = resolved escaping kinetic + material transfer lower bound + unresolved kinetic budget`.

The missing tail is neither “fully stopped” nor credited as recovered heat. Geometry calculates a **candidate** boundary for every ray; an unresolved alpha is not claimed to reach it. Current arrays therefore distinguish candidate boundaries from resolved exit positions. Unresolved exit positions are NaN with an explicit boolean mask, never zero coordinates or a fabricated exit. There are no SI exit positions or times. Candidate intersections with a side are reported separately from resolved side escapes. At a corner, face code 0 records multiple coincident faces, not an unknown-energy flag. Other face codes: +1 rear Z+, -1 front Z-, 2 a unique lateral face.

`run.py` / run001 are preserved initial computations (13 numerical checks pass). Their `exit_column_positions_atoms_cm2` name does not distinguish candidate boundaries from resolved exits and must not be used as a collector input. Separately named `run_v002.py` / run002 and run003 correct this schema, expose the missing-value mask, add alpha count fields and the stopping-refinement check. Numerical energies are unchanged; no failed test was rewritten. Use the v002 runner for continuation.

## Reproduction

Keep prior implementation directories as siblings. First unpack PR57 event banks with its `unpack_banks.py` if needed. Full replay needs Python/NumPy and inherited particle-handoff/stopping files, **not** a new WarpX run, SciPy amplitude evaluation or compiled Coulomb backend. Every inherited input is hash checked before execution. The extra inherited source files in the lock attest bank provenance; the coherent amplitudes are not regenerated here. NumPy 2.3.5 was used.

```
python finite_alpha_transport_v0_1/unpack_arrays.py
python finite_alpha_transport_v0_1/audit.py
python -m unittest discover -s finite_alpha_transport_v0_1 -v
python finite_alpha_transport_v0_1/run_v002.py --models . --bank alpha_birth_escape_v0_1/run003/EVENT_BANK.npz --receiver warpx_target_handoff_v0_2/run001/RESULTS.json --out finite_alpha_transport_v0_1/fresh_run
```

The output directory must be new. Original source-bank generation instructions and original-source uncertainty register remain in PR57. This release preserves A/B/C apparatus identities and supplies no numeric apparatus performance result for any of them.

## Next requirements

Recover the original pocket drawing or explicitly define a new candidate version. Required: target form (loose bed vs bonded/sintered/deposited), composition and isotopic inventory, number density/porosity, finite dimensions, backing/frame/apertures, beam position distribution, and a birth space/time adapter consistent with proton transport. Resolve material-dependent stopping for every segment. Then transport alphas through the actual collector geometry and fields with electrode losses, species/charge state and full energy accounting. Do not feed geometric candidate exits or unresolved alpha energy to a collector as measured/recovered output.
