# Stars p–B product map v0.1
2026-10-28. PHYSICAL_CANDIDATE / CHANNEL INVENTORY ONLY. Seven candidate persistent product identities; no yield, recoverability, price or net-value prediction. This supplements product_registry_v0_1 without overwriting it.

## Scope
The G0-B configuration is not frozen: enriched elemental boron is a candidate, while BN and supports remain comparison branches. The exact incident spectrum, isotope assay, contamination and layer stack are unknown. Consequently this is a conditional map, not seven products predicted in every shot. The 0.5–2 MeV reference-transport grid is a numerical fixture, not a guaranteed cutoff for a laser-generated spectrum.

| Product | Pathway to consider | Inclusion condition | Economic status |
|---|---|---|---|
| He-4 | B-11(p,3alpha), including sequential breakup | Primary fusion channel | Recovery and value unknown |
| C-12 | B-11(p,gamma)C-12 | Competing radiative capture; not extra C-12 from each 3-alpha event | Unpriced |
| C-11 | B-11(p,n)C-11; B-10(p,gamma)C-11 | First requires sufficiently energetic protons; second requires B-10 | Unpriced; radioactive inventory |
| Be-7 | B-10(p,alpha)Be-7 | B-10 fraction and channel cross section | Unpriced; radioactive inventory |
| N-14 | B-11(alpha,n)N-14 | Secondary alpha transport and interaction | Unpriced |
| N-13 | B-10(alpha,n)N-13 | B-10 and secondary alphas | Unpriced; radioactive inventory |
| F-18 | N-14(alpha,gamma)F-18 | Nitrogen in BN or another identified layer; secondary alphas | Unpriced; radioactive inventory |

Sources:
1. Primary channel experiment: https://www.sciencedirect.com/science/article/pii/S0168583X2400260X — publisher search extract records B-10(p,alpha)Be-7, B-10(p,gamma)C-11 and B-11 radiative capture. Full publisher retrieval returned 403; no numerical table ingested.
2. Labaune et al., Scientific Reports 6, 21202 (2016), https://doi.org/10.1038/srep21202 — primary laser B/BN experiment. Reports activation interpretations involving C-11, N-13 and F-18; N-13 yield was not accurately resolved. Supports conditional channel inclusion, not transfer of yields to Stars.
3. Haxby et al., Phys. Rev. 58, 1035 (1940), https://doi.org/10.1103/PhysRev.58.1035 — primary measured proton-neutron thresholds; B-11 approximately 3 MeV. Historical threshold is a screening reference, not a precision boundary for code; obtain modern mass-consistent thresholds and measured channel curves.
4. IAEA alpha-neutron data-needs presentation: https://conferences.iaea.org/event/366/contributions/29470/attachments/15776/26514/MParvu_IAEA_30nov23.pdf — source lead for B-11(alpha,n)N-14 and B-10(alpha,n)N-13 data. Pointwise tables not imported.

Access check: 2026-10-28. Source publication dates differ from retrieval date. No quoted production yield, branching fraction, activity or price is adopted.

## What is not a saleable byproduct
C-12* and Be-8 are transient intermediates of the principal three-alpha sequence, not separately recoverable stock. Helium-4 is the primary product, not always a byproduct. Neutrons, prompt photons, electrons and heat require physical ledgers, not an isotope price by default. Transmitted protons and unused boron are retained feedstock/energy inventories, not newly manufactured isotopes.

He-3 and tritium are not products of the principal p–B-11 -> 3alpha channel. They remain in the multi-reaction registry for other experiments; do not award them to this run without a separately sourced physical pathway.

This map is not exhaustive. Carbon/Al/Si supports, oxygen, hydrogen/deuterium contamination, windows, holders and chamber materials can add channels. Secondary proton reactions, scattering/inelastic photons, neutron capture/activation and decay daughters require a material-resolved network. Stable daughters must be linked to parent depletion; never count both as simultaneously saleable stock from the same allocation.

## Consequences for the comparison experiment
Elemental B-11 versus BN changes nuclear channels as well as stopping. Nitrogen creates a conditional F-18 pathway; residual B-10 creates others. Enrichment removes neither all secondary reactions nor neutron production. A high-energy proton tail may enable channels absent in a lower-energy beam. No automatic all-neutron-free label is permitted simply because the principal channel has no neutron.

Before simulation promotion, populate each channel with original data IDs, projectile energy frame/domain, differential yields, uncertainty, isotope abundance, transport and decay metadata. Sum competing events consistently with projectile survival and per-event conservation; an alpha consumed by a secondary reaction cannot also be counted as an escaping collectible alpha.

## Economics and next work
All seven products have NULL produced/recovered/saleable quantities, product specifications, price snapshots and processing costs for Stars. Seven identities mapped does not mean seven profitable streams or seven working engine modules. Current price-qualified count remains ZERO. The reporting module must preserve these gaps.

First characterize the full layer stack and source spectrum, then acquire channel data and build conservative source-to-retention predictions. Diagnostic activation can be useful even when saleable isotope recovery is negligible. Compare diagnostic utility and potential inventory value separately. No isotope extraction hardware, production optimization or experimental activity is specified here.
