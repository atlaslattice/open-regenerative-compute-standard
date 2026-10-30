# Source and transfer-limit register — v1.2

SOURCE-TRACED means an identifiable source supports the stated method or
context; it does not qualify this reactor. Earlier complete registers remain
in ../dynamic_fuel_cycle_v1_1 and the historical v1 white paper. This extension
uses those sources without replacing them.

| ID | Bibliographic / official source | Use and transfer limit |
|---|---|---|
| S1 | OpenMC project, version 0.15.3, executable commit `27e38e894697bb32a1dac7848d2618818b6b8daf`; [versioned documentation](https://docs.openmc.org/en/v0.15.3/), [source](https://github.com/openmc-dev/openmc/tree/v0.15.3) | Fixed-source transport, material/source construction and tally semantics. Engine execution is not physical validation. Exact environment lock and executable hashes accompany runs. |
| S2 | IAEA Nuclear Data Section, **FENDL-3.2c** processed neutron ACE distribution; [official neutron index](https://www-nds.iaea.org/fendl/data/neutron/index.html), [ACE directory](https://www-nds.iaea.org/fendl/data/neutron/ace/); [processed repository](https://github.com/IAEA-NDS/FENDL-Processed/tree/9f4e8ec72bb973858479dac57c4cf014561a9072) | 46 publicly accessible evaluated ACE files; individual URLs, headers and hashes recorded. 293.6 K data, not operating molten-salt data. No data covariance propagated. Follow distributor notices; public retrieval is not a blanket relicensing claim. |
| S3 | Schnabel, G. et al., *FENDL: A library for fusion research and applications*, Nuclear Data Sheets 193 (2024), 1–78, [doi:10.1016/j.nds.2024.01.001](https://doi.org/10.1016/j.nds.2024.01.001) | Evaluated fusion nuclear-data context. Does not benchmark this geometry or license room-temperature density assumptions. |
| S4 | Sorbom, B.N. et al., *ARC: A compact, high-field, fusion nuclear science facility and demonstration power plant with demountable magnets*, Fusion Engineering and Design 100 (2015), 378–405, [doi:10.1016/j.fusengdes.2015.07.008](https://doi.org/10.1016/j.fusengdes.2015.07.008) | Historical ARC/FLiBe architecture context. Older 525 MW reference is not substituted for B=1130 MW; dimensions are not copied and labeled current ARC. |
| S5 | Segantin et al., *Optimization of tritium breeding ratio in ARC reactor*, Fusion Engineering and Design 154 (2020), 111531, [doi:10.1016/j.fusengdes.2020.111531](https://doi.org/10.1016/j.fusengdes.2020.111531) | Geometry, structural material and enrichment dependence; cited through the inherited source register. No published TBR is adopted as this design's calculated response. |
| S6 | Hillesheim et al., ARC design reference, Journal of Plasma Physics 92 (2026), E69, [doi:10.1017/S0022377826101706](https://doi.org/10.1017/S0022377826101706) | Inherited source anchor for 1.13 GW design reference. This release has no source-qualified complete current ARC geometry. |
| S7 | Ferry et al., *The LIBRA Experiment: Investigating Robust Tritium Accountancy in Molten FLiBe Exposed to a D-T Fusion Neutron Spectrum*, Fusion Science and Technology 79(1) (2023), 13–35, online 2022, [doi:10.1080/15361055.2022.2078136](https://doi.org/10.1080/15361055.2022.2078136) | Inherited experimental-program anchor for FLiBe breeding/extraction research. No measured efficiency is transferred to the hypothetical full plant. |
| S8 | Meschini et al., Nuclear Fusion 63 (2023), 126005, [doi:10.1088/1741-4326/acf3fc](https://doi.org/10.1088/1741-4326/acf3fc); [INL TMAP8 gold case](https://github.com/idaholab/TMAP8/tree/devel/test/tests/ver-1d/meschini) | Inherited 11-stock fuel-cycle benchmark. v1.1.1 reproduces 115 rows with max 4.465e-9 kg (=4.465 micrograms). This is not a neutron-transport experiment. |
| S9 | Das, S. et al., *Quantum Computations on Fusion Blanket Molten Salts*, arXiv:2606.30402v1, submitted June 29, 2026, [official abstract](https://arxiv.org/abs/2606.30402v1) | Primary abstract retrieved in the October 30 news reconciliation: nine clusters, fragment MAD ~0.3 kcal/mol, whole-system conformational/binding discrepancies ~12/~110 kcal/mol. No kinetic or recovery input taken. |
| S10 | Myers, E.G. et al., *Atomic Masses of Tritium and Helium-3*, Physical Review Letters 114, 013003 (2015), [doi:10.1103/PhysRevLett.114.013003](https://doi.org/10.1103/PhysRevLett.114.013003); [BIPM SI](https://www.bipm.org/en/measurement-units/) | Inherited isotope-mass convention and exact SI conversion definitions. 17.6 MeV is a rounded convention, not a many-digit physical prediction. |

## New parent addendum: identified cross-validation leads, not reproduced here

The October 30 addendum in parent PR #41 supplies these metadata and equations:
[secondary-DT tradeoff](../review_reconciliation_v1_1_2/addenda/SECONDARY_DT_BURN_NET_BENEFIT_AND_MATERIALS_TRADEOFF_2026-10-30.md).
Morandi, Meschini, Testoni & Zucchetti, *Modeling fuel cycle dynamics beyond
50:50 deuterium–tritium operation*, Fusion Engineering and Design 231 (2026),
115982, doi:10.1016/j.fusengdes.2026.115982; Lopes Cardozo & van Rheenen,
*An analytical model linking tritium breeding, tritium-lean startup and fusion
power deployment*, Nuclear Materials and Energy 48 (2026), 102183,
doi:10.1016/j.nme.2026.102183. **These are source leads from the parent
addendum; this release has not reproduced their code or independently audited
all bibliographic metadata.** They are priorities for a subsequent comparison,
not calibration or novelty evidence. No globally unique dual-reactor claim.

Other dated news is mapped in NEWS_2026_10_30_RECONCILIATION.md, including
which primary source was directly checked and which announcements remain
repository-reported. A failing web-search lookup is not used as verification;
the directly retrieved official files and inherited source boundaries are stated.
