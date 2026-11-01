# Executed geometry integration results

Current execution: **run006**. Both geometry variants pass the selected numerical mesh gates; neither is a calibrated physical apparatus. Tests:13/13. CAD/material-mask comparison:1000 sampled points per profile,2000 total, zero mismatches; random seed20261101 is a numerical verification fixture.

| Quantity | Fabrication-derived outer diameter interpretation | Published PIC cavity-radius description |
|---|---:|---:|
| Inner radius(m) | 0.000232 | 0.000500 |
| Wall(m) | 0.000018 | 0.000020 |
| Entrance diameter(m) | 0.000200 | 0.000200 |
| Volume elements | 91,529 | 341,355 |
| Minimum inverse condition number | 0.15237 | 0.33859 |
| Relative mesh-volume error | 0.01131% | 0.003971% |
| CAD/analytic relative volume error | 1.10e-8 | 1.34e-9 |
| Material-qualified fusion prediction | Not available | Not available |

CAD geometry uses micrometre coordinates for OpenCASCADE robustness; exported meshes use metres. Mesh files were re-imported and their maximum radii checked:250um and520um. TheWarpX spatial expressions remain in SI metres. Mesh-quality gates are minSICN>=0.01, positive scaled Jacobian and mesh-volume error<2%; these are numerical acceptance choices, not experimental uncertainty or stress-solver convergence criteria. The initial mesh size is half the wall thickness; downstream predictions require their own refinement study.

Preserved attempts:

- run001: initial CAD/mesh generation. No shape-quality acceptance inferred from its normalized Jacobian alone.
- run002: stronger quality audit exposed near-degenerate elements in the small shell despite good volume agreement.
- run003: Netgen optimization improved the larger shell but did not resolve the small-shell sliver.
- run004: HXT also left the small-shell sliver. Both profile masks were compared against CAD.
- run005: rotating CAD parameter seams in SI-scale geometry caused an HXT PLC failure; FAILURE.json preserves it. No result was promoted.
- run006: micrometre CAD coordinates with explicit SI mesh export resolved the detected failure. CAD parameter seams remain rotated; physical spherical geometry is unchanged. Both profiles pass the present checks.

The failed attempts are mesh/software findings, not evidence against the hollow-sphere experiment. No measured gain is applied. No source/target/collector/facility rerun occurred. All30 physical facility scalars in the PR64 profile remain unresolved. All26 C inventory modules and A/B identities are retained. The only executed external solver in this increment is Gmsh; Elmer, IBSimu, ngspice, RustBCA and TESPy/ExerPy remain candidate replacements under named tests.

Large meshes are excluded from Git; their SHA256 values are recorded in each execution receipt. Current code regenerates run006-style outputs in a new directory. Historical receipts describe the earlier numerical variants and are not a claim that current code produces every historical byte sequence.
