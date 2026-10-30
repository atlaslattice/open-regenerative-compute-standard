# Solver capability/access review v0.1

Official ESTHER and Flash-X pages were fetched successfully on 2026-10-30.
Receipt includes page hashes and paraphrased findings. No access request or
message was sent to maintainers.

| Solver | Evidence inspected | Appropriate candidate role | Qualification/access status |
|---|---|---|---|
| WarpX | Pinned native source and scalar audit in PR47 | Local laser–plasma, finite-orbit/field and pB reaction studies | Public source; BSD-3-Clause-LBNL notices preserved upstream. Full PIC regression not run here. Existing one-step reaction regression disables pushing/deposition and is not confinement. |
| Smilei | README at 61aa917e851e89c64a0a2c17ca869fa71128422d | Independent laser–plasma/field/source comparison | Public PIC source; no run or pB nuclear-feature equivalence established here. Full dependency/license/build review pending. |
| ESTHER | Official CEA page | 1D multilayer deposition, mechanical response, solid-to-plasma evolution | Officially described as open-source; GitLab invitation required. Actual software license/material tables not recovered. No 3D particle-pocket/granular equivalence established. |
| Flash-X | Official source access page | Candidate hydrodynamic state preparation | Apache 2.0 according to official page; repository collaborator access required. Do not equate every Flash-X build with FLASH laser physics capabilities. No executable/material model inspected here. |
| Structural/acoustic solver | Requirements recovered, implementation not selected | Pocket/shell response and measured transfer functions | Selection pending geometry, constitutive data, damping, contact and computational scale; Elmer is only an unqualified lead, not selected. |
| Granular/contact solver | No recovered boron packing/contact data | Only if pocket contains mobile particles | Requires contacts, friction, adhesion and vacuum/environment applicability; not replaced by elastic continuum without a scale test. |
| Optical solver | No recovered optical boundary data | Reflection/absorption and alignment dependence | Ray/wave model selection pending wavelength-to-feature ratio, surface properties, pulse/damage regime. |

Official resources:
- https://www-lmce.cea.fr/en/cond_matt_physics/4_codes/3_esther.html
- https://flash-x.org/pages/source/
- https://github.com/SmileiPIC/Smilei/blob/61aa917e851e89c64a0a2c17ca869fa71128422d/README.md
- https://github.com/BLAST-WarpX/warpx/tree/a389dc54a27136176bdd48f7bfd36da62a873a61

The user-supplied FLASH→WarpX pB workflow is a high-priority reproduction lead,
but its original full methods, actual code versions, numerical state mapping and
input decks have not been recovered by this release. Do not report it as a
reproduced benchmark. MULTI/HYDRA and burn-propagation headlines likewise confer
no executable capability on the present branch.

Current environment: Python 3.12.14, NumPy 2.3.5 and g++ available; no pywarpx,
mpi4py, cmake, ninja or mpiexec found. No full PIC build attempted or declared
impossible. A dependency-pinned build environment is a pending engineering task;
missing installed tools are not evidence of a physical or permanent compute limit.
