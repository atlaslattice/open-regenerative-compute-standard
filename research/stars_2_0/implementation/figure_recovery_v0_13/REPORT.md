# Published experimental benchmarks: recovery and implications v0.13

2026-10-29. Additive to v0.12; no changes to previous research or apparatus modules.

## What was actually done

1. Checked SHA256 of the original Schollmeier supplement and published Kuhlwein PDF against previously recovered source pins.
2. Recovered four helium histograms from the original embedded raster in Supplement Figure S3, not a screenshot. Read the reported Langau fit labels independently by visual inspection. Identified approximate display bins with blue-color segmentation and visually verified tick anchors.
3. Recovered the six stroked PDF paths in Kuhlwein Figure3. Preserved original line/Bezier commands. Cubic segments are evaluated at 32 subdivisions, rather than treating control points as data. Axis anchors map the display to CM energy in MeV and relative heights.
4. Compared the published experimental trace to each published model with a descriptive area-normalized shape distance. No new physical model fit or comparison to the full Stellar Forge apparatus was performed.
5. Rendered the source independently with Poppler and checked 48 curve locations. All were visible and agreed within 0.496784 vertical pixel. Initial media-box/crop-box mismatch failed the check; its receipt remains preserved. Using the source crop box resolves the coordinate mismatch without relaxing the original gate (>=24 visible, <=2 pixels).

## Evidence recovered

| Helium energy MeV | Source interval MeV | Published Langau location um | Visible bins / candidate bins |
|---|---|---|---|
| 0.23 | +/-0.05 | 0.932 | 25 / 46 |
| 0.56 | +/-0.06 | 1.002 | 26 / 46 |
| 2.25 | +/-0.06 | 0.639 | 33 / 46 |
| 4.52 | +/-0.11 | 0.611 | 34 / 46 |

The location is not an arithmetic mean. The source's eta and sigma labels are retained; they are not silently reinterpreted as equivalent Gaussian SDs. Source width-convention questions from v0.12 remain open. At 4.52 MeV the displayed histogram contains an additional population attributed to sputtered C/O ions. A pure-helium response cannot be obtained by treating every displayed bar as helium.

Candidate bin edges 0.425..1.575 um in 0.025 um steps are an analyst reconstruction of the raster bars. Two-pixel vertical and horizontal allowances are extraction diagnostics, not reported experimental uncertainties, confidence bounds, or a complete accounting of occlusion/raster bias. Unseen bars remain null. Visible-bin sums and subset means are diagnostic summaries only; they are not full event totals or full distribution means. No bin normalization to incident alpha fluence is known.

Four representative panels do not establish the full calibration inventory or its highest energy. 7.5 MeV remains NOT_ESTABLISHED_FROM_RECOVERED_NUMERICAL_PACKAGE. No extrapolation is qualified.

## Formula reconciliation

Using the previously checked literal helium coefficients (47.83,0.49,1.53,0.05), Equation2 yields 1.205303,1.150314,1.030908,0.959973 um at the four source energies. Differences from the printed Langau locations are +0.273303,+0.148314,+0.391908,+0.348973 um. This strengthens the source-internal diagnostic fixture. It is not a statistical rejection of the measurements; missing conventions, prescription errors, or reconstruction interpretation remain possible. We did not substitute log-energy, reorder parameters, or tune a scaling to force agreement. The literal model remains quarantined. A direct condition-specific tabulated benchmark can still be useful without claiming the analytic formula is resolved.

## Nuclear projected-shape comparison

The extracted CM energy interval is approximately 0.030016..5.970025 MeV. First/last plotted samples are near30/5970 keV, not the axis endpoints0/6000. All three black paths represent the same experimental projection, with residual rendering differences below1e-4 in relative height. Do not concatenate them as independent observations.

| Published model | Display-shape total variation |
|---|---|
| pure l=1 | 0.1332646885 |
| pure l=3 | 0.0969255938 |
| coherent mixture | 0.0475600461 |

The statistic is half the integral of absolute difference after separately normalizing the two rendered curves to unit area over their common recovered interval. It is a descriptive figure comparison, not a hypothesis-test statistic. Its ordering need not match a full Dalitz fit: Figure3 throws away correlations that Figure2 retains. Pure l=3 being closer than pure l=1 by this projected metric does not contradict the paper's modest opposite preference in full Dalitz chi-square. The mixture is the closest of the three by this metric.

Analyst +/-0.05 PDF-point vertical-offset sensitivity ranges are [0.132878,0.133658], [0.096609,0.097231], [0.047129,0.047996]. These are not statistical intervals or comprehensive uncertainty bounds. Increasing cubic subdivisions32->128 changes any reported distance by at most1.58135e-6. The mixture still has visible residuals. Published best-fit chi-square12297 for approximately5350 degrees of freedom already flags model inadequacy; the authors discuss omitted final-state interactions. Merely recovering predominantly l=1 would not reproduce that fit or establish model adequacy.

This is a benchmark against published experimental data, recovered from a figure. It provides a quantitative comparison target. Fitting parameters to this target would be calibration; independent predictive validation would require different observations/conditions or a genuinely held-out group. Source tracing does not require fit success and is not the same status as calibration.

## Material implications

- Nuclear source correlations and coherent terms can materially change projected alpha spectra. That supports testing the coherent lane and using measured distributions to constrain it. It supplies no new total cross section, all-shot reaction-rate enhancement, or wall-plug gain.
- Source-shape changes can affect escape, acceptance, energy conversion and inferred yield; the amount must be computed through qualified transport/detector interfaces. We have not yet quantified that transfer in this release.
- A detector response prescription mismatch is large enough to matter for interpretation. These recovered measurements strengthen the benchmark without proving the published experiment is wrong.
- No acoustic experiment appears in these extracted datasets. The release neither establishes nor excludes a large acoustic effect. Retain mechanical preparation, sustain, readiness and laser control as distinct, revisable lanes.

## Next bounded work

Use the S3 histogram fixtures for a condition-specific forward-response comparison; preserve the sputtered-ion component and missing-bin semantics. Reconcile the original Equation2 prescription in parallel. Compare the coherent source through an explicitly reconstructed Kuhlwein acceptance/response chain; do not fit an unfiltered CM truth spectrum directly to a selected detector spectrum and call that apparatus calibration. Recover Figure2 numerical cells/color mapping or original data if possible. Seek original target-specific acoustic sources; support quantitative component inputs within their actual applicability and measure stack interactions. No arbitrary uncertainty envelope or permanent zero-gain label replaces missing evidence.

## Sources and attribution

M.S. Schollmeier et al.2023, Scientific Reports13,18155, DOI10.1038/s41598-023-45208-x, supplement Figure S3 p3. CC BY4.0 source content retains attribution. M. Kuhlwein et al.2022, Physics Letters B825,136857, DOI10.1016/j.physletb.2021.136857, published Figures2/3 and Table2; CC BY source. Pinned publication PDF is the numerical recovery source; arXiv:2109.07886 is a related preprint, not assumed byte/content-identical. No contact with authors, proprietary access, purchase, physical experiment, original raw-event recovery, or scientific freeze is claimed.
