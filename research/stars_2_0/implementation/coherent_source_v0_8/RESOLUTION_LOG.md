# Source and uncertainty resolution — v0.8, 2026-10-29

| Question | Search result and action | Remaining qualification |
|---|---|---|
| Coherent mixture or classical branch selection? | Implement coherent partial-wave and Bose permutation sums, retaining incoherent ablations. Kuhlwein2022 Eq1–4 supports this candidate structure. | Adapted coefficients are not verified branch fractions in our raw basis. |
| Be8 level energy reference? | Bhattacharya2006 TableIII gives 3037keV excitation; Refsgaard2016 Table3.1 gives 3129(6)keV relative to two-alpha threshold. Explicit candidate uses 3037+91.84keV. | Exact original Kuhlwein code energy zero not recovered; no allegation of a published error. |
| Which width? | Recovered formal reduced width squared1075(9)keV, distinct from observed width1477(13)keV and observed reduced width squared811(7)keV. | No full covariance matrix recovered. |
| Can radius errors be varied independently? | Bhattacharya reports strong parameter correlations and radius refits. | Do not freeze other parameters and label radius sweeps as a published confidence band. |
| Coulomb numerical reliability? | Independent Michel/GSL comparison failed; 40-digit mpmath comparison selects Michel with the original gate unchanged. | Validation is on the declared grid, not every possible parameter. |
| Exact Coulomb phase and amplitude normalization? | Standard relative-to-sigma0 phase explicitly selected. Alternative absolute phase diagnostic retained. ORM archive recovered; full original experiment configuration not recovered. | Still unresolved for an exact paper reproduction; no calibrated source claim. |
| Alpha0 calibration data? | Munch preprint Table1 recovered and visually checked:45 entries with reported errors. | Four duplicated-energy entries quarantined from automatic fitting; journal identity and full covariance unresolved. |
| Other real-source calibration? | Existing Spraker spectra, Mazzucconi differential tables and event cross-section bridge remain preserved. | Observable/multiplicity semantics, acceptance and shared systematics must be reconciled before joint fitting. |
| Measured alpha-on-boron stopping? | Rechecked IAEA stopping gateway and experimental data leads; no new usable original numeric table recovered. | Existing SRIM models remain model data, not a new measured alpha/B calibration. No invented table added. |

Primary sources, exact downloaded hashes, and their roles are listed in `SOURCE_INDEX.json`. Further public searches did not resolve every missing convention or covariance. Absence from recovered public sources is not evidence that the data do not exist. No author contact was sent.

The common-proposal sensitivity receipt compares two deliberate changes: an absolute Coulomb-phase convention and omission of the91.84keV threshold offset. Alpha probability histogram L1 differences are approximately0.00701 and0.03457, respectively. They are diagnostics, not physical uncertainty distributions, confidence intervals or measured effects.

Next: reconcile the ambiguous preprint labels against the journal/source data, recover the exact fitting conventions, and fit a detector-folded exclusive source with correlated uncertainties and independent campaign holdouts. Full apparatus prediction also needs material- and state-specific alpha transport. Coherent interference can reshape distributions without increasing the total reaction rate.
