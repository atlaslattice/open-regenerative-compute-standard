# Stars 2.0 — Gemini Argon reported 125-row tabular recalibration (audit hold)
**2026-10-27 | Provenance: Gemini Argon (reported computation), Atlas Lattice (research direction), ChatGPT/Tidal Lantern (independent review).**

## What was actually provided
Gemini Argon's user-supplied message describes a **125-row** CSV allegedly named `stars_2_0_reference_nuclear_stopping_tables.csv`, covering proton laboratory energies of 10–5000 keV with BN proton/helium stopping, ranges, p–¹¹B cross-section bounds and spin scenarios. **That CSV itself was not supplied or independently inspected.** Neither the revised generator, source EXFOR entry identifiers, raw SRIM run settings or publication-licensed tables nor fitting residuals were provided. Do **not** commit a reconstructed 125-row file as a verified evaluated reference.

## Reported anchor numbers (NOT independent measurements)
- Proton S(75 keV)=94.08 keV/µm; S(736.77 keV)=42.09 keV/µm; S(1000 keV)=35.84 keV/µm (reported CSDA range at 1 MeV 19.36 µm); hBN density 2.10 g/cm³.
- Helium at 2.900 MeV: S=245.2 keV/µm and integrated range 9.07 µm. At 2.461 MeV range 7.34 µm; 3.760 MeV range 12.81 µm.
- Reported example cross sections old surrogate vs 'audited': at 161.53 keV lab 0.105→0.100±0.010 b; 300 keV 0.108→0.040±0.004 b; 736.77 keV 2.078→1.278±0.083 b; 1500 keV 2.625→0.111±0.011 b; 2881.60 keV 4.317→0.364±0.036 b. Cross-section provenance and the 1σ error model are **unverified**.
- Reported thickness scan at L=1,3,4,4.5,5,5.5,10,50 µm: total escaped energy (µJ) 0.1319, 0.2582, 0.2834, 0.2903, 0.2943, 0.2960, 0.2685, 0.1836; rear component (µJ) 0.0656, 0.1243, 0.1329, 0.1339, 0.1333, 0.1313, 0.0922, 0.0021. Values are user-supplied Gemini outputs **not independently reproduced**.
- Reported born alpha particles: 3.15e5, 8.08e5, 1.00e6, 1.09e6, 1.18e6, 1.25e6, 1.77e6, 2.70e6 at those respective thicknesses.

## Critical problem: main resonance still in wrong energy frame
The purported evaluated cross-section labels a **736.77 keV lab = 675 keV CM** feature as the **J^π=2+ main resonance**. The primary published experiment Stave et al. (2011), DOI 10.1016/j.physletb.2010.12.015, describes the prominent 0.675 MeV feature at **E_p(lab)=0.675 MeV**, in their account a **2− resonance**. For a stationary ¹¹B target, 675 keV incident proton energy maps to approximately 618 keV CM, *not* 675 keV CM. This is a substantive energy and spin assignment conflict, not a cosmetic labeling issue. See https://www.sciencedirect.com/science/article/abs/pii/S0370269310013626 and https://link.springer.com/article/10.1007/s10894-011-9473-5 . Do not treat the proposed table as a trustworthy EXFOR evaluation until provenance and channel/frame metadata are reconciled.

## Further audit cautions
1. A single agreement of alpha range (~9.1 µm) with Popper et al. (2026) does **not** independently validate a full energy-dependent helium stopping curve; electronic/nuclear partitions or compound density.
2. 'Exact range inversion' means numerical inversion **conditional on a particular table**. It does not include stochastic range straggling, correlated three-body decay, charge exchange, angular scattering or uncertainty.
3. Comparing modeled **born** alphas (e.g. 2.70e6) with a detector-inferred NePTUN escaping yield under different beam/shot conditions is not experimental validation; compare the same denominator, detector acceptance, particle class, proton spectrum and per-shot exposure.
4. A phenomenological fit sampled at 125 energies can be made into a CSV without ceasing to be a surrogate. Require raw source data, units, identifiers, fitting code, uncertainty provenance and external residual comparison.
5. The claimed few-micron plateau may be physically sensible, but its exact peak and absolute magnitude remain strongly dependent on BN stopping, actual differential alpha spectrum, incident spectrum and collector topology.

## Preservation: reported excerpt
A **separate** 8-row CSV was transcribed from Gemini's message solely to protect its reported numbers; it is **not** the alleged 125-row evaluated source table.

## Requested next deliverables for Gemini Argon
- Supply actual 125-row CSV and generation script; include source license, dataset IDs, SRIM material/composition/stopping model, experimental ranges and uncertainty derivation.
- Correct nuclear energy frame and resonance/channel/spin labels according to original references; show comparison plot before/after using exact same proton source.
- Include correlated three-alpha event generator and detector response; run acoustic ON/OFF/SHAM without assuming gains.
- Publish comparisons as MODEL-REPORTED / INDEPENDENTLY REPRODUCED / DATA-BENCHMARKED / EXPERIMENTAL separately.

**Scientific verdict:** The *reported* tradeoff still shows a broad few-micron escaped-alpha-energy plateau under another parameterization. Not yet a calibrated physical prediction; no direct electrical fusion gain follows.
