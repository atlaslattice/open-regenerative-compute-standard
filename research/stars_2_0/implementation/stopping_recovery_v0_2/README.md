# Boron stopping-source recovery v0.2

Additive source qualification, 2026-10-28 America/Chicago. Prior quarantines and files remain preserved.

## Essential new source recovered

Jack Castle Overley, Caltech PhD thesis (1961), A Study of the Elastic Scattering of Protons by B10, DOI https://doi.org/10.7907/XZP6-5P63 . Primary repository: https://thesis.caltech.edu/6305/ . Original PDF: https://thesis.caltech.edu/6305/1/Overley_jc_1961.pdf . The institutional abstract states proton stopping was measured over 0.10–3.0 MeV with 4% absolute accuracy. The original 27,603,374-byte PDF was acquired and hash-pinned in OVERLEY_SOURCE.json.

Printed page 32 / PDF page 37 gives TWO absolute normalization anchors: 2.72e-15 eV cm2/atom at 1.805 MeV and 2.10e-15 eV cm2/atom at 2.642 MeV. Both were checked in the rendered original page. Printed page 34 / PDF page 39, Table III, was visually inspected: total probable error +/-4%, with contributions from area, deposit weight, enriched-boron molar mass, thickness, uniformity, diffusion, contamination, geometry and local-linearity assumptions. It is not silently relabeled as Gaussian 1-sigma or independent per-point error.

The target used for absolute normalization was 95.96% B10 and 4.04% B11, with reported molar mass 10.05 g/mol, deposited on tungsten. Its deposit was 909 +/-7 micrograms. The thesis describes measured energy loss, rather than a separately recovered electronic/nuclear decomposition. This observable should not automatically be relabeled as electronic-only because a later database specializes in electronic stopping.

At the two anchor energies the old headerless mirror's A-tagged values match EXACTLY if its energy coordinate is keV and stopping coordinate is 1e-15 eV cm2/atom. This is strong source-lineage evidence and resolves the units at those anchors. It does not establish that every A-tagged point was transcribed correctly, assign B/C/D to papers, or establish nuclear subtraction choices. The whole 77-point file remains outside calibrated runtime transport. Shared mirror/thesis/article ancestry is not independent validation.

The thesis also quotes its curve at 0.5 MeV as 6.40e-15 eV cm2/atom (printed page 35 / PDF 40). That text value is retained separately from the two absolute normalization anchors. Full figure 7 digitization with its own numerical error remains to do. No invented 0.675 MeV measurement is inserted.

## Runnable source check

```bash
python check_anchors.py --out receipts/new_run
python check_anchors.py --pdf sources/overley1961.pdf --mirror PATH_TO_PREVIOUS_MIRROR --out receipts/new_verified_run
python -m unittest -v test_anchors
```

Python standard library only. The portable JSON contains the visually checked anchors and source metadata. With the original PDF and mirror supplied, hashes and exact anchor matching are verified. The runner never claims to OCR-reconstruct the measurements itself. Source PDF is not redistributed here.

Mass stopping is epsilon * 1e-6 * NA / molar_mass, in MeV cm2/g. The conversion is implemented and tested. Using a different molar mass does not demonstrate isotope transfer. There is no full stopping curve, CSDA range, automatic interpolation, warm-target correction or alpha stopping in this release. Four tests pass. The receipt verifies both exact mirror matches and the PDF identity.

## Other sources and next acquisition priorities

1. Overley and Whaling, Phys Rev 128,315 (1962), https://doi.org/10.1103/PhysRev.128.315 . Publisher abstract independently confirms 0.1–3.0 MeV boron stopping measurements. Related thesis/article are one experimental lineage. Next: reconstruct the full measured curve, including digitization uncertainty, and compare to a versioned calculated total-stopping model.
2. Kamke and Kramer, Z Phys 168,465–473 (1962), Energieverlust und Reichweite von Alpha-Teilchen in Bor im Energiebereich von 0.2 bis 5.3 MeV. SRIM's original reference index https://www.srim.org/Citations/Cit%2002-05.pdf identifies He->B coverage. DOI recovered through Crossref: https://doi.org/10.1007/BF01378142 . Original article/table still to recover; publisher web retrieval was denied by robots.txt. This is the highest-priority alpha-escape measurement lead, not qualified numerical data yet.
3. Macdonald, Ormrod and Duckworth (1966), DOI 10.1515/zna-1966-1-220, electronic stopping for low-energy H/He and other ions in boron. Useful low-energy endpoint/straggling lead, not a substitute for MeV measurements. Original publisher archive retrieval returned 503 this session.
4. SRIM/TRIM author source https://srim.org/ and SR-NIEL's documented electronic and nuclear stopping calculators https://www.sr-niel.org/ supply model alternatives. Record executable/version, settings, ion, isotope mass, density, phase, stoichiometry, Se and Sn separately. These are candidate calculations to compare to measurements; no SRIM executable or calculated numerical table was recovered or executed in this release.
5. Lahmann et al. (2023), DOI 10.1088/1361-6587/ace4f2, author archive https://library.psfc.mit.edu/catalog/reports/2020/23ja/23ja010/abstract.php . Warm-dense boron/Be proton measurements need actual state, shot spectra and error recovery. Author PDF retrieval returned 503. Do not transfer warm-dense values into cold foils by name alone.
6. NIST PSTAR/ASTAR are useful controls for Al, C and Si, but do not list elemental B or BN. Their total/electronic/nuclear definitions remain essential. A boron composition record is not a boron PSTAR table.

The current IAEA ZIP and legacy ZIP returned 403 via direct download; web retrieval identifies binary archives but cannot deliver their contents. These access failures are recorded, not treated as proof that stopping measurements are absent. SRIM reference lists are discovery tools, not substitutes for original measurements. BN and B4C require their own material models and validation. Bragg additivity may be an explicitly labeled estimate with uncertainty; it is not a direct compound measurement.

Physical module retention is unchanged. This release narrows a data gap without freezing the scientific contract or claiming net-energy calibration.
