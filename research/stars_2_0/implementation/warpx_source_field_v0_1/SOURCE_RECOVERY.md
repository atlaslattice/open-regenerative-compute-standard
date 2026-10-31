# Source recovery and bounded applicability

Current project search: default-branch proton-spectrum matches at
cbf6c07359b132de1db4e9f7b15d531fd0fdfac1; local preserved dataset catalog,
pB source bridge and particle-handoff records. This is not an exhaustive search
of every paper/private artifact/branch and is not a claim that data do not exist.

| Available item | Can constrain | Cannot supply alone |
|---|---|---|
| EXFOR/Sikora reaction tables | Source-qualified cross-section candidates | Absolute laser proton source |
| Spraker alpha spectra | Reaction/product/detector comparisons in their source conditions | Proton energy–angle–position–time distribution |
| ENN suprathermal energy interval | A regime to investigate with proper pair CM velocities | Laser-driven source normalization or spectrum |
| Hollow-sphere reported cutoff | Candidate upper-energy feature | Absolute spectrum, divergence or joint correlations |
| Existing assumed675keV packet tests | Unit/weight/transport verification | Installed apparatus beam calibration |
| FEMM/openPMD example field | Field-loader, units and finite-orbit benchmark | Real STARS or PRISM field map/power/capture performance |

Original map source:
https://github.com/openPMD/openPMD-example-datasets/tree/11e1a9d8281044c7e01dea9977291c871273da3f

HDF5 original Git blob fddd0a849d8f5ffc8ce9cd00fdc3dedd4ff62161,3,561,320bytes.
Dataset/source scripts areCC0; original license preserved. mirror.FEM uses
millimetres; Lua queries points at those coordinates. Its source file describes
an axisymmetric example with1A circuit and10-turn labels. Do not treat the
imported map as a measured field or a high-field fusion-confinement device.
The binary mesh has spacing[.05,.05,.125],offset[-1.15,-1.15,-.375],gridUnitSI=1,
XYZ axes and B component unitSI=1. It is a47³ grid. Values are retained unchanged.

The canonical-mm branch is a **source-inferred spatial interpretation**, not an
author-confirmed erratum. Original and metadata-only branches remain visible.
The original example can be a valid intentionally rescaled algorithm test; its
numerical usefulness does not establish its physical identity with the FEM geometry.

WarpX source pin:
https://github.com/BLAST-WarpX/warpx/tree/ec1660d961696c865c87c26728b7e248b5454082

Inspected ExternalField.cpp and GetExternalFields.cpp, plus particle-load input
and collision inputs/analyses. Tests use NOMPI, two OpenMP threads, the same
installed package as PR50. No source/build revision is invented for its Unknown
banner. WarpX BSD-3-Clause-LBNL license/notices retained.

The pB apparatus must acquire or explicitly derive complete joint source and
magnet/material states before transporting that source into reactions and a
wall-plug ledger. Normalization, spatial/timing correlations and calibration
uncertainties are not optional when estimating capture or successful-shot yield.
