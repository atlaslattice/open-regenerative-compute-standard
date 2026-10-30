# v1.3 primary/official source register

All links identify scope, not endorsement or reactor validation.

| Source | Use and limits |
|---|---|
| [WarpX 26.10 release](https://github.com/BLAST-WarpX/warpx/releases/tag/26.10), reference source commit [ec1660d9](https://github.com/BLAST-WarpX/warpx/tree/ec1660d961696c865c87c26728b7e248b5454082) | Pinned reference source for fixtures and algorithms. Installed executable identified by conda package/build/checksum and binary SHA; its embedded WarpX git version is Unknown. |
| [Upstream nuclear fusion tests](https://github.com/BLAST-WarpX/warpx/tree/ec1660d961696c865c87c26728b7e248b5454082/Examples/Tests/nuclear_fusion), including analysis_two_product_fusion.py | Actual supplied DD/DT inputs and analysis executed. Tests check numerical operators under prescribed conditions; not fusion reactor experiments. |
| [WarpX 26.10 collision parameters](https://github.com/BLAST-WarpX/warpx/blob/ec1660d961696c865c87c26728b7e248b5454082/Docs/source/usage/parameters.rst) | Species, nuclearfusion, physical weights/event multipliers and product controls; build and feature limitations apply. |
| [NuclearFusionFunc.H](https://github.com/BLAST-WarpX/warpx/blob/ec1660d961696c865c87c26728b7e248b5454082/Source/Particles/Collision/BinaryCollision/NuclearFusion/NuclearFusionFunc.H) and [SingleNuclearFusionEvent.H](https://github.com/BLAST-WarpX/warpx/blob/ec1660d961696c865c87c26728b7e248b5454082/Source/Particles/Collision/BinaryCollision/NuclearFusion/SingleNuclearFusionEvent.H) | Sample probability, multiplier handling and removal of reactant weights. No extra physical reaction rate is inferred from increased macroparticle sampling. |
| [BoschHaleFusionCrossSection.H](https://github.com/BLAST-WarpX/warpx/blob/ec1660d961696c865c87c26728b7e248b5454082/Source/Particles/Collision/BinaryCollision/NuclearFusion/BoschHaleFusionCrossSection.H); Bosch,H.-S. & Hale,G.M., *Improved formulas for fusion cross-sections and thermal reactivities*, Nuclear Fusion32(1992)611, [doi:10.1088/0029-5515/32/4/I07](https://doi.org/10.1088/0029-5515/32/4/I07) | Shared cross-section parameterization in WarpX and independent numerical integration. Lower cutoff is implemented; upper fit domains, nonthermal tails and reactor conditions are not independently qualified here. |
| Higginson,D.P., Link,A. & Schmidt,A., *A pairwise nuclear fusion algorithm for weighted particle-in-cell plasma simulations*, Journal of Computational Physics388(2019)439–453, [doi:10.1016/j.jcp.2019.03.020](https://doi.org/10.1016/j.jcp.2019.03.020) | Algorithm reference explicitly cited by upstream code; not empirical validation of our network or geometry. |
| [ParticleNumber.cpp](https://github.com/BLAST-WarpX/warpx/blob/ec1660d961696c865c87c26728b7e248b5454082/Source/Diagnostics/ReducedDiags/ParticleNumber.cpp), ParticleEnergy.cpp and ParticleMomentum.cpp in same directory | Source-traced diagnostic units and total-weight versus macroparticle distinction. Large-pool summation precision is separately checked. |
| [Conda-forge WarpX](https://anaconda.org/conda-forge/warpx) | Actual prebuilt package26.10/build np2py314h0f05cbd_0, recorded URL, dependencies and checksums. No claim of independent source-build attestation. |
| Neighboring [v1.2 inventory kernel](../neutronics_v1_2/fuelcycle/inventory.py) and [report](../neutronics_v1_2/WHITE_PAPER.md) | Existing exact constant-hazard compartment implementation, explicit kg/day units and unresolved campus physics boundaries. Used unchanged. |

Only upstream fixtures, analysis/parser and notices are vendored. BSD-3-Clause-LBNL
LICENSE.txt and NOTICE.txt are retained under upstream/. Reuse of test code and
formula coefficients is credited; no solver fork or codebase merger was performed.
