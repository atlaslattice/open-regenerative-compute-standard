# Source, equation and transfer-limit register

| Source | Role and limitation |
|---|---|
| [WarpX 26.10 reference source](https://github.com/BLAST-WarpX/warpx/tree/ec1660d961696c865c87c26728b7e248b5454082), commit ec1660d961696c865c87c26728b7e248b5454082 | Source fixture and operator reference; actual conda executable/package hashes recorded separately. No embedded source-build attestation. |
| [BackgroundStopping.cpp](https://github.com/BLAST-WarpX/warpx/blob/ec1660d961696c865c87c26728b7e248b5454082/Source/Particles/Collision/BackgroundStopping/BackgroundStopping.cpp) | Electron exponential proper-velocity decay and ion proper-energy stopping; cites Goldston & Rutherford, Introduction to Plasma Physics, §14.2, Eqs14.12/14.20. The textbook is referenced through this inspected implementation, not claimed independently benchmarked here. Approximate asymptotic drag, no thermal diffusion or background response. |
| [Upstream ion-stopping input and analysis](https://github.com/BLAST-WarpX/warpx/tree/ec1660d961696c865c87c26728b7e248b5454082/Examples/Tests/ion_stopping) | Unmodified input and supplied analysis executed; analysis explicitly uses the same stopping formulas. Numerical verification, not independent experimental validation. |
| [WarpX parameter documentation](https://github.com/BLAST-WarpX/warpx/blob/ec1660d961696c865c87c26728b7e248b5454082/Docs/source/usage/parameters.rst) | background_stopping density/temperature/mass, electrostatic solver and timestep semantics. No electromagnetic-wave or confinement claims in prescribed collision-only runs. |
| [BoschHaleFusionCrossSection.H](https://github.com/BLAST-WarpX/warpx/blob/ec1660d961696c865c87c26728b7e248b5454082/Source/Particles/Collision/BinaryCollision/NuclearFusion/BoschHaleFusionCrossSection.H); Bosch,H.-S. & Hale,G.M., Nuclear Fusion32(1992)611, doi:10.1088/0029-5515/32/4/I07 | Same parameterized nuclear physics in WarpX and reduced quadrature, inherited from v1.3. Model agreement does not independently qualify nonthermal fits or operating plasma conditions. |
| [Higginson,Link & Schmidt, JCP388(2019)439–453](https://doi.org/10.1016/j.jcp.2019.03.020) and pinned WarpX fusion operator | Weighted fusion sampling, product/consumed-particle accounting. Event multipliers affect sampling rather than physical gain. |
| [v1.2 transport report](../neutronics_v1_2/WHITE_PAPER.md) and per-run artifacts | Reused DD/DT salt-yield means in an assumed 293.6K spherical-shell testbed. No new transport, hot-state data, laser-specific geometry or current ARC prediction. |
| [v1.3 kinetic-source report](../kinetic_source_v1_3/REPORT.md) and analysis.py | Prior DD-born-T / DT collision tests, SI constants, source conventions and cross-section function. New 0.1 s coupled case starts from trace T; it is not a continuous extension of the2ps DD run. |
| [User-corrected dual-laser power basis](../DUAL_LASER_POWER_BASIS_LOCK_2026-10-30.md), parent674eb174ff935bcfc9829109b57c1187d25dc710 | Current repository design input: A/B each1.1GW gross fusion. Earlier20 MW gross-DD/1.13GW DT fixtures remain historical. No achieved gross power, net electricity or indefinite operation is implied. |

SOURCE-TRACED identifies an inspected source or provenance receipt.
VERIFIED-DERIVED identifies numerical identities conditional on explicit inputs.
POTENTIAL-DERIVED identifies assumed-background/plasma/plant scenario results.
UNRESOLVED covers real confinement, model validity, extraction, source geometry,
laser and wall-plug performance, qualified startup and self-sufficiency.

Upstream BSD-3-Clause-LBNL LICENSE.txt and NOTICE.txt are retained. Dave Sheldon /
Atlas Lattice supplied research direction and the repository power correction;
GPT-6/Tidal Lantern, DeepSeek and Gemini Argon receive their documented preceding
analytical credits. WarpX contributors retain separate code/algorithm credit.
No company, laboratory, university or cited author endorses or validates this
architecture by virtue of being cited or their code being executed.
