# Stellar Forge — hollow-sphere and external solver integration v0.1

2026-11-01. Additive continuation of draft PR64 at a080438ab6ff3321f13d8f8b29fcb00ec32c7f70. This package executes a real Gmsh geometry/mesh adapter and exports the same SI spatial mask for WarpX. It does not execute a new fusion or facility-performance calculation.

## Geometry clarification and material separation

The project originator identifies the original ceramic pocket with the cited hollow-sphere geometry. The prior assertion that the geometry FAMILY was unrecovered is superseded by this clarification. Exact original manufacturing CAD is not claimed to have been recovered.

The cited paper has two distinct numerical descriptions: its fabrication section gives an approximately500um capsule diameter,18um wall and200um entrance; its PIC section gives a500um cavity radius,20um wall and200um entrance. PROFILES.json preserves both. The fabrication adapter interprets capsule diameter as outer diameter, deriving a232um cavity radius; this is an explicit convention, not a new measurement. The aperture is represented as a cylindrical bore on+z. Aperture machining shape, mounting and alignment tolerance remain unspecified. Neither profile silently resolves the paper's discrepancy. The study's2D simulation cannot distinguish a sphere from a cylinder; our3D CAD is not reproduction of its2D plasma dynamics.

The paper's fabricated spheres use boron-oxide nanopowder in a polymer matrix. That is not calibration of the user's boron-ceramic variant. Ceramic composition, density, enrichment, stopping, equation of state and mechanical properties remain separately qualified inputs. The existing cold pure-B11 column is not assigned to this shell. A/B/C apparatus identities remain intact; a shared geometry family does not merge their equipment or transfer performance.

## What is integrated

- geometry.py: one SI hollow-shell/aperture definition, analytic volume, Gmsh CAD generation and WarpX-parser spatial expression.
- run.py: actually invokes Gmsh with--mesh, exports.geo/.msh and a geometry-only WarpX binding; checks CAD volume, mesh volume and element quality. The binding explicitly lacks density; it is not a complete runnable PIC input deck.
- Physical volume target_shell and unassigned_target_boundary are exported. Mounting, acoustic/electrical boundary conditions and material models must be supplied before an Elmer solve.
- A material gate refuses absent composition/density/transport evidence. Future cited derived estimates are permitted; this does not require every input to be directly measured.
- MODULE_RETENTION_v002.json retains all26 C entries and the A additions, with the pocket identity correction.
- SUPERSESSION.json distinguishes executed replacement, existing control, and candidate replacement. External solver availability is not a passed integration test.

The old relative-column event bank is not reinterpreted as SI positions on the sphere. The facility pipeline remains the unchanged PR64 control until a qualified source-to-shell/transport adapter produces new events. Acoustic readiness and shot reliability remain separate from per-fired reaction physics. No combination gain, nuclear cross-section multiplier or zero physical acoustic effect is inferred here.

## Reproduction

Use a separate environment; no binaries or third-party source are vendored. The standard Gmsh wheel required absent GUI libraries in this container. The executed fallback is the official headless DEVELOPMENT distribution, not a stable release. INSTALL_RECEIPT.json records the failed attempts and exact executed version.

```
python -m venv --system-site-packages /path/to/new-env
/path/to/new-env/bin/python -m pip install numpy==2.3.5
/path/to/new-env/bin/python -m pip install --index-url https://gmsh.info/python-packages-dev-nox 'gmsh==5.0.0.dev20261101+nox'
python -m unittest discover -s research/stars_2_0/implementation/solver_integration_v0_1 -v
/path/to/new-env/bin/python research/stars_2_0/implementation/solver_integration_v0_1/run.py --mesh --out /path/to/new-output
```

Every output directory must be new. Without--mesh, stdlib Python exports the geometry bindings without importing Gmsh. Mesh resolution is a numerical choice, not a measured manufacturing tolerance. CAD/mesh checks do not establish convergence of a stress, acoustic, plasma or fusion prediction.

Execution receipts and compact generated inputs are preserved. Large mesh files are reproducible generated outputs: their hashes are recorded, but the meshes are not committed. run001 and run002 preserve earlier geometry/quality audits; see RESULTS.md for the current selection and any failed quality gates. Rebuilt meshes need numerical comparison, not guaranteed byte-identical output across toolchains.

## Integration sequence

1. Resolve the published diameter/radius difference or carry both as separate sensitivity configurations. Qualify one ceramic material state with cited measured/derived properties.
2. Use these meshes for an Elmer modal/forced-response benchmark with measured mounting/damping; validate readiness and relaxation. Transfer geometry/density/temperature at shot time rather than seconds of forcing into femtosecond PIC.
3. Reproduce a published FLASH-to-WarpX target case before importing an acoustic-perturbed state. FLASH and Flash-X are not presumed interchangeable builds.
4. Qualify SI particle birth/exit coordinates and time, material stopping and charge states before replacing the finite-box transport control or connecting the collector.
5. Bring in IBSimu/ngspice and TESPy/ExerPy under their individual acceptance gates. Facility unknowns stay unknown until those models receive qualified inputs.

## Sources and licenses

Accessed2026-11-01. Software licenses and data permissions are separate. Discovery head SHAs are in DISCOVERY_SNAPSHOTS.json and are not execution pins.

- Geometry, composition and comparison conditions: https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/hydrogen-boron-fusion-in-confined-geometries/D273DDE00ABB65D29D2053845A22A887 (Sections2.1,4,5). Its filter-dependent enhancement is not applied as a global gain.
- Gmsh: https://gmsh.info/ and https://gmsh.info/doc/texinfo/ ; GPL2-or-later with linking exception; external dependency only. Cite Geuzaine & Remacle(2009), IJNME79,1309–1331.
- Elmer: https://docs.csc.fi/apps/elmer/ ; mixedGPL/LGPL policy: https://github.com/ElmerCSC/elmerfem/blob/devel/license_texts/ElmerLicensePolicy.md . No FEM solve executed here.
- FLASH/WarpX pB workflow: https://doi.org/10.1103/PhysRevResearch.7.013230 . Supporting data available on reasonable request; a complete public replay package has not been recovered.
- WarpX tutorial: https://blast-warpx.github.io/warpx-tutorials/instructor/a-laser-driven-ion-accelerator.html . Educational parameters contain placeholders; not a calibrated apparatus deck.
- RustBCA: https://github.com/lcpp-org/RustBCA ; GPL3. A BN example does not qualify our material.
- IBSimu: https://ibsimu.sourceforge.net/index.html ; GPL. Steady-state space-charge iteration needs qualification for pulsed collection.
- ngspice: https://ngspice.sourceforge.io/ ; license details: https://ngspice.sourceforge.io/devel.html . Terminal circuit simulation is not plasma simulation.
- TESPy/ExerPy: https://tespy.readthedocs.io/en/main/advanced_features/exergy.html and https://exerpy.readthedocs.io/en/stable/exergy_analysis.html ; bothMIT. Neither supplies missing heat-stream temperatures or recoverability.

Scientific freeze remains blocked. Actual apparatus fusion yield and net power are not evaluated by this increment.
