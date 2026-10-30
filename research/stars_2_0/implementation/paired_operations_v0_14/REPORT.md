# Paired simulations, source stability and energy gaps v0.14

## Main result

The user's acoustic hypothesis is primarily operational: preparation may increase the probability of a physically productive firing and reduce instability/jitter. A change in successful pulses per attempt can materially change aggregate energy even if conditional energy per productive pulse is unchanged. Reduced variance alone does not guarantee an increase in mean energy. Extra preparation energy/time, alignment bias and productive outputs from nominally unsuccessful pulses matter.

This release implements that distinction, recovers an experimental source-stability benchmark, and provides extrapolated detector-location estimates. It does not claim actual acoustic response, complete apparatus calibration, net electricity or ignition.

## Published experimental data reproduced

Streeter et al., Nature Communications16,1004(2025), DOI10.1038/s41467-025-56248-4, and authors' CC-BY4.0 dataset DOI10.5281/zenodo.14236097. The archived stability notebook and selected numeric records were recovered via ordinary HTTP byte ranges. Individual ZIP member CRCs and SHA256s were verified; whole-archive MD5 was not verified. Original notebook code was inspected, not executed. Source numerical pickles were loaded only through explicitly allowlisted NumPy/Pandas constructors, after hash checks.

Recovered run20210803/run05 has420 dataframe rows. The source analysis selects bursts5..21 (340rows), retains dose>0.1Gy (323rows), then uses the first300. Seventeen below-threshold entries in that window are not automatically17 failed laser pulses: background, acquisition, preparation and physical outcomes require separate records. The initial80 excluded rows and final23 retained-but-not-plotted rows are not silently lost; their selection counts are recorded. The all-preparation success denominator remains unknown.

| Recomputed selected-window statistic | Result |
|---|---|
| Peak dose mean / population SD | 40.651583 /4.587187 Gy |
| Minor divergence mean / population SD | 23.475178 /2.352276 mrad |
| Major divergence mean / population SD | 39.997638 /3.159031 mrad |
| x centroid population SD about mean | 4.884922 mrad |
| y centroid population SD about mean | 4.629915 mrad |

Dose/divergence round to the published notebook outputs; centroid SDs reproduce its cached numeric values. Centroid SD includes slow drift and is pointing variation, not laser timing jitter. Data come from a liquid-sheet source without an acoustic ON/OFF comparison. The paired potential lane does not claim these are acoustic enhancements or Stars measurements.

The source paper describes approximately190mJ optical pulses, approximately0.5% optical-to-proton conversion and5Hz operation. These imply approximately0.95mJ proton-beam energy/pulse and4.75mW average beam power under those component conditions. Optical input is not wall input, and beam output is not fusion energy. These approximate paper-level figures are not a new calibration for the specific300-record window or for Stars. Dose in Gy is not converted to total fusion energy without detector mass, deposition and acceptance.

## Operational model

Let r=P(ready), f=P(fires|ready), s=P(physical success|fired), and q=energy of an unsuccessful fired pulse / energy of a successful pulse. Holding successful-pulse energy fixed gives normalized energy per attempted preparation:

    r*f*[s+(1-s)*q]

These are conditional stages, not independent marginal probabilities. Physical overlap/success is distinct from a detector qualification cut. Nuclear output can remain nonzero on unsuccessful fired pulses. Missing detector outcomes do not become zero physical output. All attempted preparations, including timeouts/aborts and misfires, belong in the denominator. Wall costs for preparation and auxiliaries survive aborts; extra laser consumption by misfires must be allocated explicitly upstream rather than assumed refunded.

The exploratory jitter lane rescales the measured selected centroid deviations about a fixed mean. Acceptance windows of0.5/1/2 reference SD and scale ratios0.25..2 are analyst scenarios, not measured target acceptance or acoustic transfer. A separate 1D Gaussian model illustrates an analytic comparison. Neither model establishes effects on plasma timing, source fluence or nuclear cross section.

For a centered Gaussian, an acceptance half-window of one reference SD and an assumed halving of jitter change overlap0.682689->0.954500. If q=0 and r/f are unchanged, normalized energy per attempt rises1.398146x. If extra serial preparation increases cycle time50%, energy per time becomes0.932097x. If q=1, narrowing alone produces no mean-energy increase. A biased beam can lose overlap when narrowed. These are conditional examples, not predicted Stars gains. Startup-only/concurrent preparation must be charged differently from per-attempt serial time; the dimensionless delay scenario is not a prescription to wait after every pulse.

Absolute nuclear output, actual r/f, acoustic costs, load electricity and wall totals remain null where missing. The accounting API accepts supplied boundary-specific energies but never equates nuclear Q with electricity. Failure of an energy boundary to be specified is not filled with an ideal efficiency.

## Detector extrapolation

Schollmeier et al.2023, DOI10.1038/s41598-023-45208-x, supplement S3: use the two same-condition high-energy Langau location labels (2.25MeV,0.639um),(4.52MeV,0.611um). These are source fit locations, not arithmetic means or inferred incident efficiency. The4.52MeV displayed histogram includes sputtered-ion contamination; its printed fitted helium component is used, not the whole histogram mean.

At7.5MeV the two-anchor models give:

| Model | Extrapolated location um |
|---|---|
| Linear | 0.574242 |
| Exponential | 0.576096 |
| Power law | 0.591446 |

Nominal model spread0.574..0.591um is not a confidence interval. Using the reported source energy intervals as corner sensitivities plus +/-0.0005um printed-location rounding allowances gives a combined model/sensitivity span roughly0.568..0.595um; this is also not a statistical uncertainty bound and is not comprehensive. Two anchors cannot establish curvature, high-energy detectability, response tails or efficiency. The unexplained original analytic formula remains quarantined. This separately named extrapolation does not repair it or establish measured7.5MeV coverage. The implementation refuses energies above8MeV; the new20MeV news claim is not covered.

## Missing energy inputs and outputs

ENERGY_GAPS.json separates source stability, nuclear Q, escaped-alpha energy, field work, transmitted particles, recoverable heat, load electricity, radiation/secondary losses and stored-energy change. The most consequential missing quantities for net electricity are real pulse-normalized fusion/exit energy, full converter acceptance and load output, laser wall consumption, acoustic preparation/sustain energy, and full-cycle auxiliaries. Existing loss remainders are not automatically recoverable heat. Model- or vendor-derived values are allowed if cited, applicable and explicitly labeled; unknown entries are not zero.

The ENN converter paper DOI10.1088/2058-6272/ae445a supplies a low-parameter unit result, not a qualified MeV-alpha Stars efficiency; its full methods were not recovered in this audit. I-BEAT (arXiv2111.06180, DOI10.1117/12.2592415) is a useful independent per-pulse diagnostic lead, not acoustic target preparation. Acoustic shell metrology DOI10.1016/j.pacs.2026.100801 is a separate possible readiness/metrology lead, not a fusion-gain measurement.

## Validation and next step

Thirteen tests cover all-attempt denominators, finite costs on aborts, nonzero failed-fired output, absence of direct nuclear-to-electric conversion, missing wall costs, biased/narrowed adverse outcomes, variance without mean gain, zero firing, invalid probabilities, extrapolation anchors/range, rejected arbitrary pickle constructors, immutable outputs and published summary rounding. Replays are deterministic; grouped independent experimental validation is still open. No new lab experiment or author contact was performed.

Next: specify a physically measured overlap/readiness observable for a selected Stars target/source configuration, recover all-attempt logs, and connect that operational layer to the existing conditional source/transport engine through its explicit source inputs. No hypothetical gain is silently attached to the nuclear kernel. Preserve all previously retained modules and alternatives; complete apparatus integration remains open.
