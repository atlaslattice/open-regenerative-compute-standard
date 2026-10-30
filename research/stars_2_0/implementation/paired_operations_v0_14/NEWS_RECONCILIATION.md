# October2026 p-B additions: source reconciliation

Audit date2026-10-29 America/Chicago. These new leads are preserved separately from the source-stability benchmark. Source URLs/status are in SOURCE_INDEX.json and HOLLOW_SPHERE_SOURCE.json.

## EXL-50U

ENN's2026-09-28 announcement and its hosted2026-10-08 Science and Technology Daily report support the September reaction demonstration. The hosted report describes a suprathermal162..200keV population from NBI/RF and approximately1e8alpha particles/s. Other reporting calls the headline >1e8reactions/s. Do not silently choose one denominator: alpha production, detected alpha counts and reaction-event rate require the technical diagnostic normalization. GPTWork initially characterized the headline as a reaction rate in commentary, then found and acknowledged the explicit alpha-rate wording in the hosted report. Preserve this reconciliation.

At an illustrative rate exactly1e8events/s, Q=8.682559153MeV gives1.3911e-4W nuclear Q power; exactly1e8produced alphas/s with three per event gives4.637e-5W. These conditional unit checks are not measured electrical output, a conversion of detector counts without acceptance, or an estimate of plasma gain. Additional incoming kinetic energy is distinct from nuclear Q.

A reported energy interval is a benchmark lead, not an entire fast-ion distribution or cross-section calibration. A plasma reaction-rate model needs measured proton/boron velocity distributions, densities, spatial overlap, confinement/time history, diagnostic acceptance and uncertainty. In plasma use relative collision energy; do not copy a stationary-target laboratory energy into CM variables automatically. The current coherent2-minus engine is scoped near0.65..0.70MeV laboratory protons; it must not be reused unchanged for the first low-energy resonance or tens-of-MeV proton sources. Current sparse normalized cross-section nodes at0.15/0.22MeV do not resolve the narrow162keV feature; linear interpolation between them is not a resonance reconstruction.

An actionable primary nuclear-data lead is *Proton-boron fusion in a hydrogen-doped-boron target* (Cambridge link in SOURCE_INDEX): the paper explicitly describes21 laboratory-energy measurements120..260keV and2keV spacing near162keV. The numerical dataset and its target/source semantics have not yet been extracted here. H-mode DOI10.1016/j.xinn.2026.101458 is a separate measured result, online2026-06-03, not the September alpha-rate paper.

## Hollow sphere

R.M. Arun Kumar, H. Habara, Y. Nakamura, B. Ramakrishna, *Laser-driven proton-boron fusion in a hollow spherical target*, Physics of Plasmas33,103104, DOI10.1063/5.0349072. Publisher-deposited Crossref metadata confirms online2026-10-27; issue date2026-10-01 explains the university listing's earlier date. Direct AIP full text/PDF access failed; no restriction bypass, institutional login, purchase or author contact was attempted.

The deposited abstract describes2D PIC at1e21W/cm2, proton cutoff53MeV versus39MeV planar, transient fields near a rear opening, PIC+FLUKA alpha production around20MeV, and an alpha spectral quantity of order1e11/MeV. It also mentions preliminary3D PIC and a calcium-to-scandium isotope application. The /MeV must not be dropped: this is not automatically1e11total alphas or1e11/s. Full geometry, timing, spectrum/solid-angle/shot normalization, macro-particle weights, nuclear reaction implementation and convergence need the paper/data before numerical reproduction.

The source is a simulation lead, not a new laboratory observation. Proton cutoff is not mean energy, useful resonance occupancy or fusion yield. Alpha energies can include incoming proton kinetic energy and field work in addition to Q; do not assign20MeV per alpha as extra nuclear energy. The useful architecture addition is a born-alpha -> material transport -> field work -> escaping distribution -> detector/collector chain with energy attribution. No20MeV detector response is inferred from the current two-point4.52MeV tail fit.

## Borealis PRISM

The company's2026-10-15 introduction confirms a tandem-mirror-derived PRISM concept (pB11 Rotating Ion Separation Mirror), founded by five people, four previously involved in Princeton pB11 research. Its stated focus includes selective helium-ash exhaust, fuel retention, radiation losses and system economics. The company explicitly says integrated power-plant conditions have not been demonstrated.

This is a useful comparator for finite residence time, fuel/ash separation and energy accounting, not validation of Stars repeated encounters or a recovery efficiency. Model finite fuel loss, pitch-angle transport, slowing, ash residence, radiation, external heating and end-loss energy before claiming a benefit. Neither company association nor an architectural analogy supplies a measured gain.
