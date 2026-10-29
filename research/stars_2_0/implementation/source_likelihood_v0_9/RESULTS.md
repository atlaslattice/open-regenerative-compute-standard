# Result and decision — v0.9

The coherent source now has a checked conditional event-likelihood kernel. This is an engineering and experimental-design result, not a fit to new physical observations.

| Ideal observable | Local information rank | Condition number in `(raw k, phase radians)` |
|---|---:|---:|
| Sorted triple of CM energy-fraction bins |2|740.9|
| One randomly selected alpha energy bin per reaction |2|2870.0|
| Total reaction count, with separate normalization |0|undefined|

Values use32768 invariant-phase-space proposals, seed20261030,12 bins per alpha energy fraction, and the unchanged v0.8 literature-informed candidate. Both shape parameters are locally distinguishable in this idealized diagnostic, but a weak parameter combination remains. Rank alone is not calibration success. Parameter scaling changes condition numbers; detector noise, response uncertainty and model discrepancy can make practical calibration worse. No required exposure or confidence interval is inferred.

Retaining three-alpha correlations passes the positive-semidefinite information comparison against its random-alpha marginal. The latter is one alpha selected per reaction, not a claim about the entire correlated inclusive histogram or3 independent alpha counts. Real experimental channels may have different efficiencies, live time and costs, which this diagnostic does not compare.

The8192-to32768 refinement changes the exclusive information matrix by0.685% in relative Frobenius norm; its weakest eigenvalue changes by about5%. An independent8192-proposal run changes the matrix by3.29%. These checks expose finite-integration sensitivity; they do not establish a measured uncertainty budget.

Constant basis rescaling leaves all normalized probabilities unchanged after transforming the free mixing coefficient. This removes one artificial implementation barrier to a future exploratory fit, while preserving the prohibition on interpreting a raw coefficient as a universal branching ratio.

Decision: retain coherent amplitudes as preferred; retain pure/incoherent controls; keep source normalization separate; prioritize acquisition of matching exclusive counts and detector response. Do not fit the pure2-minus model to alpha0-channel cross sections, and do not claim that a full-rank information matrix validates the physics. Existing transport calibration and module versions remain preserved. Scientific freeze stays blocked.
