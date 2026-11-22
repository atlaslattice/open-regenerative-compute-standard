# G2 conditional transport configuration

Current environment: no OpenMC Python API, executable, Conda or Docker; no
`OPENMC_CROSS_SECTIONS` and no `cross_sections.xml`/`Li6.h5` found in the searched
`/opt` and this task workspace. Public documentation and download listings are
accessible; libraries were not downloaded. **No transport simulation was run.**

The stdlib-only inventory suite does not depend on OpenMC. Independently run:

```sh
python neutronics/openmc_surrogate.py --preflight
```

On a prepared machine, use the official Conda/Docker installation instructions
in SOURCES.md. An OpenMC 0.15.x-compatible Python API and matching executable
are required. Download a documented official processed HDF5 library, record its
exact version/archive hash and all relevant HDF5 hashes, then set the
`OPENMC_CROSS_SECTIONS` path. Li6, Li7, Be9, F19, W, alloy/shield isotopes and
consistent temperatures/heating data must be covered. Audit every data warning.

```sh
python neutronics/openmc_surrogate.py --export-only --li6 .075 --blanket-cm 90
python neutronics/openmc_surrogate.py --run --li6 .30 --alloy vanadium_4cr4ti --output run_li30_v
```

This input generator has only been syntax-checked, not exported/executed against
the absent API. Treat engine/runtime compatibility as unverified. Sweep Li-6
atom fractions .075/.20/.30/.90, blanket thickness 85/100 cm and the three
explicit alloy surrogates. Geometry is concentric circular toroidal shells,
not V3A. Plasma radius/major radius are only a source-basis anchor. Structural
specifications, shielding and FLiBe density are assumed. Separate shell layers
are explicit; the source proposal's phrase “7 zones” does not uniquely specify
its several sublayers. A source option preserves the **legacy conditional**
20+18 MW A spectrum; for dynamic A, derive DD/DT mixture from actual event counts.
No universal 72.8/27.2 split applies after burn fraction changes.

No empirical port multiplier is applied. A 6–12% scalar removal cannot capture
streaming, spatial breeding or magnet damage. Explicit ports/divertor/shaping,
temperature/material state, spatial coverage and variance/convergence studies
are still needed. No surrogate result automatically enters the dynamic defaults.

Tallies: Li6/Li7 `H3-production` in salt, neutron-only `heating-local`, outer
surface current and shield fast-neutron tracklength. Tracklength requires
volume and source-rate normalization to become flux. Magnet lifetime requires
spatial spectra, fluence, damage thresholds, temperature and engineering evidence.
`heating-local` assumes local deposition of secondary photon energy; compare
coupled neutron/photon `heating` before closing G5. It includes deposited neutron
energy: **do not add it to the full fusion Q**. Use charged-particle deposits plus
transport heat once, with leakage and any source energy boundary reconciled.

G2/G5 remain OPEN even after a surrogate run. No fabricated TBR is delivered.
