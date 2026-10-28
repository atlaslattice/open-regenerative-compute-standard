# G0-B source acquisition and benchmark register v0.1

STATUS: CANDIDATE SOURCES AND REJECTIONS RECORDED; CALIBRATION OPEN  
Date: 2026-10-28. New version; prior source registers preserved.

## Findings that change the acquisition plan

1. **NIST PSTAR/ASTAR do not list elemental boron or BN.** The authoritative [74-material list](https://physics.nist.gov/PhysRefData/Star/Text/table2.html) includes aluminum, silicon and carbon variants. The broader [boron composition page](https://physics.nist.gov/cgi-bin/Star/compos.pl?matno=005) explicitly cautions that not every composition entry is available in PSTAR/ASTAR. A composition record is not a stopping table.
2. The [IAEA database](https://www-nds.iaea.org/stopping/) compiles experimental **electronic** stopping, assuming nuclear stopping has been removed or is negligible. Its [legacy hydrogen-ion index](https://www-nds.iaea.org/stopping-legacy/stopping_hydr.html) explicitly lists boron. That establishes a source lead, not a qualified total-stopping range table.
3. The header-bearing aluminum mirror can be audited as a candidate evaluated reference. The headerless boron mirror cannot yet supply verified units, A-D paper identities or nuclear stopping. Neither is calibrated BN.

NIST's [method documentation](https://physics.nist.gov/PhysRefData/Star/Text/programs.html) defines electronic, nuclear and total mass stopping separately and specifies CSDA integration of reciprocal total stopping. These definitions motivate the two-column-formulation check; the current mirror has not been reconciled byte-for-byte to a primary download.

## Acquisition outcomes and source grades

| Source / attempt | Outcome | Allowed use |
|---|---|---|
| Direct NIST PSTAR text page | Earlier direct urllib HTTP 403; primary method/material pages readable through web retrieval | Definitions and coverage; no claimed B/BN numerical table |
| IAEA current download `/stopping/download/tuples` | Web tool identifies ZIP; direct urllib HTTP 403; archive not acquired | Located download and version claim only |
| IAEA legacy H-data ZIP | Web tool identifies binary ZIP but cannot decode it; no numerical ingestion | Retrieval locator only |
| IAEA legacy H-B Origin graph | Binary Origin file not readable through retrieval tool | Graph/source lead only |
| `dedx-erpa/dedx` aluminum PSTAR mirror | Exact pinned bytes recovered; 132 rows with explicit units and distinct source columns | Candidate evaluated table; model reference check only |
| Same repository boron electronic mirror | Exact pinned bytes; 77 numeric records with A-D tags and no unit/ref header | Quarantined inventory only |
| Same repository calculated boron `dedx.dat` | Identified as model output, with separate run-card/model context | Not adopted as measured or total stopping |
| NBS NSRDS 29 boron-table search hit | Official NIST publication identifies it as **photon** cross sections/attenuation | Rejected for proton stopping |

Rejected wrong-projectile reference: [NIST publication record, NSRDS 29](https://www.nist.gov/publications/photon-cross-sections-attenuation-coefficients-and-energy-absorption-coefficients-10). A boron heading and an energy column alone do not establish the projectile or observable.

The current IAEA landing page reports version 2026-09. The recovered GitHub mirror is not demonstrated to equal that release. No current-version claim is attached to its rows.

## Independent experimental leads, not yet qualifying benchmarks

- [MIT PSFC author archive: Lahmann et al., Measuring stopping power in warm dense matter plasmas at OMEGA](https://library.psfc.mit.edu/catalog/reports/2020/23ja/23ja010/abstract.php), publication DOI `10.1088/1361-6587/ace4f2`. The author abstract reports proton stopping measurements in Be and boron, with target-state characterization. This is a credible experimental lead. Complete shot spectra, source distribution, areal densities, uncertainties and the regime relevant to the intended G0-B run still need recovery before any numerical validation. No points have been digitized or used here.
- Macdonald, Ormrod and Duckworth, *Stopping Cross Sections in Boron of Low Atomic Number Atoms with Energies from 15 to 140 keV*, DOI `10.1515/zna-1966-1-220`: literature lead found in secondary indexing; original publisher retrieval did not succeed. Retain as **unqualified lead**, not an asserted A-D label mapping or an imported experiment. No secondary text is treated as verified finite-range data.
- [Authors' first-principles hBN calculation bibliographic record](https://pubmed.ncbi.nlm.nih.gov/39904061/), DOI `10.1088/1361-648X/adb233`: theoretical stopping lead. Not imported as a measured transmission result.

None closes the desired independent transmission gate yet. A stopping table and a validation measurement must not be declared independent merely because they appear at different URLs; common experimental ancestry must be checked.

## What must be qualified next

For elemental boron: recover the IAEA original numeric archive and reference map, confirm projectile/isotope, units, electronic-versus-total definition, experimental errors, target phase/composition and energy range. Add a source-qualified nuclear contribution if a total-stopping model is constructed, and propagate uncertainty rather than silently discarding that term.

For BN: use actual composition/phase and independent material-state data. A Bragg-additive estimate may be an explicitly labeled model sensitivity case, but it is not a BN measurement. No elemental-B or aluminum range is reused as BN.

For the aluminum control: reconcile primary source bytes and establish mirror completeness/version, then test against independent measured foil transmission with known beam distribution, areal mass, geometry and detector calibration. The current 12 cases are deterministic table predictions, not laboratory observations.

For a prospective G0-B experiment: the measured input beam and material characterization should constrain transport before alpha outcomes tune nuclear normalization. Freeze the comparison, grouping and uncertainty criteria before inspecting the held-out results. Retain source aliases and shared calibration groups to avoid false independent evidence.
