# Calibration source audit — 2026-10-29

This review advances the conditional coherent source from v0.8; it does not fit experimental observations.

**Exclusive coherent source.** Kuhlwein et al., [Phys. Lett. B825,136857](https://doi.org/10.1016/j.physletb.2021.136857), Eq1–4 and Table2, is the structural reference. Its best reported fit remains significantly discrepant; final-state interactions are explicitly omitted. Its experimental selection requires three detected particles, energy/momentum consistency and individual energies above250keV, with Be8-ground-state events removed. Those cuts and their detector response have not been reproduced here. The paper quotes a1361(2)keV molecular H2+ beam; the diagnostic's0.675MeV proton LAB point is not asserted to be the exact reference entrance energy. Source PDF SHA256 is recorded in the preceding v0.8 source index.

The original paper and institutional publication record were rechecked. Public searches for numerical exclusive events, supplementary datasets, HEPData and associated source code did not recover a matching data/acceptance package. This is a retrieval limit, not a claim that the data do not exist. No author contact was sent.

**Alpha-zero data.** The [publisher's version-of-record page](https://link.springer.com/article/10.1140/epja/s10050-019-00016-8) confirms that tabulated cross sections are in Table1. The full journal content remains subscription-restricted through the accessed route, and the public table link returned the same preview or was inaccessible. The arXiv-v1 extraction remains explicitly a preprint fixture; its duplicate-energy labels are still unresolved. Neither an unofficial transcription nor guessed corrections are promoted to primary-source data.

The alpha0 observable is a different channel from this pure2-minus model: alpha0 through Be8(0+) is forbidden for that parent by angular momentum and parity. It can constrain other contributions to the full reaction, but cannot be used as a direct fit target for the present conditional source shape.

**Stopping and apparatus.** No new measured stopping table is claimed in this version. Earlier cold-proton calibration, SRIM model tables, event cross-section bridge and spectrum fixtures remain in the stack. Their uncertainties and observable limitations are not removed by the new likelihood.

**What can be resolved without the authors' normalization code?** A constant rescaling of either amplitude basis can be absorbed by a freely fitted relative coefficient. The normalized event distribution is invariant under this change, as tested here. Therefore basis normalization need not prevent an exploratory fit with a declared convention and a free coefficient. It does prevent treating the coefficient as a convention-independent branching fraction or transferring the paper's fitted percentage without reconciliation. Energy-dependent phase changes and final-state interactions are not removed by this reparameterization.
