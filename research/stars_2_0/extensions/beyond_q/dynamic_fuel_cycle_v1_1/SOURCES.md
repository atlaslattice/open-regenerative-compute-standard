# Source registry and access limits — 2026-10-29 America/Chicago

The complete v1 white paper, citation appendix, correction ledger, source
script, metadata and 28 scenarios were read and preserved byte-for-byte in
`baseline_v1/`, from commit `876bb375d278e9ccb934638fbfbe64852fbcbfbd`.
That appendix retains all 17 v1 source leads. External literature below is
method/context evidence, not experimental validation of this architecture.
Full texts not obtained are expressly distinguished from inspected abstracts.

| ID | Exact reference | Inspected evidence / use / limitation |
|---|---|---|
| V1 | [Published audit directory](https://github.com/atlaslattice/open-regenerative-compute-standard/tree/876bb375d278e9ccb934638fbfbe64852fbcbfbd/research/stars_2_0/extensions/beyond_q/tritium_self_sufficiency_audit_v1) | Complete six-file snapshot; source of all legacy benchmarks/corrections |
| R1 | Hillesheim J.C. et al. (2026), *Overview of the physics basis for the ARC fusion power plant*, J. Plasma Phys. 92 E69, [doi:10.1017/S0022377826101706](https://doi.org/10.1017/S0022377826101706) | Publisher/search text confirms 1.13 GW design rating and evolving vessel/blanket. DOI open initially failed, publisher search result recovered. No geometry TBR inferred |
| R2 | Sorbom B.N. et al. (2015), *ARC: A compact, high-field, fusion nuclear science facility and demonstration power plant with demountable magnets*, Fusion Eng. Des. 100, 378–405, [doi:10.1016/j.fusengdes.2015.07.008](https://doi.org/10.1016/j.fusengdes.2015.07.008), [arXiv v2](https://arxiv.org/abs/1409.3540v2) | arXiv abstract and bibliographic record inspected. Older conceptual FLiBe architecture only, not new V3A geometry |
| R3 | Segantin S., Testoni R., Hartwig Z., Whyte D., Zucchetti M. (2020), *Optimization of tritium breeding ratio in ARC reactor*, Fusion Eng. Des. 154, 111531, [doi:10.1016/j.fusengdes.2020.111531](https://doi.org/10.1016/j.fusengdes.2020.111531) | Publisher abstract/introduction inspected: older 525 MW concept; materials, Li enrichment and channel geometry studied. No numerical curves transferred into new transport output |
| R4 | Ferry S.E., Woller K.B., Peterson E.E., Sorensen C., Whyte D.G., *The LIBRA Experiment: Investigating Robust Tritium Accountancy in Molten FLiBe Exposed to a D-T Fusion Neutron Spectrum*, Fusion Sci. Technol. 79(1), 13–35, [doi:10.1080/15361055.2022.2078136](https://doi.org/10.1080/15361055.2022.2078136) | [ANS record](https://wx1.ans.org/pubs/journals/fst/a_52640) inspected: published online 13 Dec 2022, journal issue Jan 2023. v1 year 2022 is online-publication convention; retain both dates. Abstract only; no extraction calibration taken |
| R5 | MIT PSFC, [Tritium breeding and monitoring in molten salt for fusion energy applications](https://www.psfc.mit.edu/research-areas/fusion-energy/tritium-breeding-for-fusion-energy/) | Project goals/accountancy gap inspected. Supports need for experimental evidence, not any model recovery percentage |
| R6 | Malone C.R., Flynn H.B., Somers A.D., Rowell P.A., Larsen G.K. (2024), *Approach to startup inventory for viable commercial fusion power plant*, Fusion Eng. Des. 206, 114563, [doi:10.1016/j.fusengdes.2024.114563](https://doi.org/10.1016/j.fusengdes.2024.114563), [OSTI manuscript](https://www.osti.gov/servlets/purl/2403075) | Publisher abstract/sections and OSTI record inspected. RHINO transient approach; reported 327 g for different 500 MW study. Not our startup stock |
| R7 | Meschini S. et al. (2023), *Modeling and analysis of the tritium fuel cycle for ARC- and STEP-class D-T fusion power plants*, Nucl. Fusion 63, 126005, [doi:10.1088/1741-4326/acf3fc](https://doi.org/10.1088/1741-4326/acf3fc), [institutional record](https://iris.polito.it/handle/11583/2995586), [code release record](https://zenodo.org/records/10070335) | Institutional abstract and code metadata inspected. Time-dependent inventory/recycling methods; code not ported and paper result not independently reproduced here. Does not certify Argon's loop-time or efficiency ranges |
| R8 | INL TMAP8, [Fuel Cycle Benchmarking from Meschini et al. (2023)](https://tmap8.inl.gov/examples/fuel_cycle_Meschini/) | Official documentation inspected; 11-system ODE model and comparison with original MATLAB. Useful next external computational benchmark, not yet passed by this simpler seven-stock model |
| R9 | DOE-STD-1129-2015, [Tritium Handling and Safe Storage](https://www.energy.gov/documents/doe-std-1129-2015pdf), half-life discussion p.18; EPA [Method 906.0 technical notes](https://nepis.epa.gov/Exe/ZyPURL.cgi?Dockey=P10154R2.txt) | Official search extracts: 12.323 y measurement convention / 12.32 y rounded. Model uses 12.32, with lambda computed from ln2, not a separately rounded fitted constant |
| O1 | OpenMC [quick install](https://docs.openmc.org/en/stable/quickinstall.html), [data configuration](https://docs.openmc.org/en/stable/usersguide/data.html), [official library downloads](https://openmc.org/data/) | Docs inspected. Engine and nuclear data are separate dependencies. No local engine, data or run verified |
| O2 | OpenMC [tallies](https://docs.openmc.org/en/stable/usersguide/tallies.html), [cross-sections format](https://docs.openmc.org/en/stable/io_formats/cross_sections.html) | H3-production, heating-local and per-source normalization definitions inspected. heating-local local-photon approximation is explicit |
| O3 | OpenMC [ZTorus](https://docs.openmc.org/en/stable/pythonapi/generated/openmc.ZTorus.html), [CylindricalIndependent](https://docs.openmc.org/en/stable/pythonapi/generated/openmc.stats.CylindricalIndependent.html), [IndependentSource](https://docs.openmc.org/en/stable/pythonapi/generated/openmc.IndependentSource.html) | API signatures inspected; generator syntax-checked only in this environment |
| A1 | Gemini Argon proposal supplied verbatim by Dave Sheldon in this conversation, 2026-10-29 | Exact burn/FLiBe equations transcribed to inputs/argon_candidates.json; scenario table independently recalculated. Analytical proposal, not published experimental dataset |

## Other inherited source checks

v1 S9 [SCSP supply-chain report](https://www.scsp.ai/wp-content/uploads/2025/12/Fusion-Supply-Chain-Report.pdf)
and S10 [FIA 2026 release](https://www.fusionindustryassociation.org/fia-launches-2026-fusion-industry-supply-chain-report/)
were opened for context; no cost/enrichment-production number is used by v1.1.
S11 [INL NSUF project 5525](https://nsuf.inl.gov/Home/ProjectLayer/5525) is an
award/proposal, not completed permeability validation. Its chemistry/redox
discussion reinforces the missing model variables.
S12 [CFS publications](https://cfs.energy/technology/publications/) and S15
[ARC vendor page](https://cfs.energy/technology/arc/) were opened; commercial
targets are not physical validation.
S17 [Woller LIBRA July 9 2025 slides](https://arpa-e.energy.gov/sites/default/files/2025-08/Day2_03_Woller.pdf)
were opened; project configuration/goals, not validated commercial yield.
S2 announcement and S13 collection landing page were opened for context.
S14 Segantin full PDF failed with HTTP 502; S16 disruption DOI could not be
fetched. Those full texts were not reviewed in this release.
They support no new v1.1 quantitative input. No claim of a complete full-text
literature review is made. Exact experimental calibration, spatial neutron
transport and independent published-model replication remain open work.
