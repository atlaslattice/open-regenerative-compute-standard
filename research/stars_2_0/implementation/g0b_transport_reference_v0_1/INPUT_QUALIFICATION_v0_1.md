# G0-B physical-input qualification register v0.1

STATUS: INPUT GAPS RECORDED; PHYSICAL PREDICTIONS NOT RUN  
Date: 2026-10-28. Append-only companion to the conventional transport reference.

## Existing usable evidence

The repository contains a source-normalized 41-point C2973002 alpha-observable table. The earlier observable slice in draft PR #9 reproduced its 123 numerical cells against the original EXFOR record. That is numerical source reproduction, not proof of a fusion-event normalization, angular decay law, detector efficiency or stopping curve. This transport version does not reinterpret that table as a reaction probability.

The conventional G0-B protocol is a design draft with facility, specimen, detector and numerical acceptance fields still unfilled. Its hypotheses do not require a predetermined micron optimum. The later Gemini correlated-source audit remains a separate historical code-reproduction task; it must not supply unqualified default stopping or synthetic spectra to this reference.

## Required input contracts

| Input | Required qualification | Available for a physical run here |
|---|---|---|
| Incident proton ensemble | LAB energy/angle/time/spot/current, uncertainties, exposure, calibration and dataset hashes | No |
| Target stack | Layer order, material/phase/composition, measured normal areal mass, B-11 atoms/cm2, isotope ratio, batch/sample IDs and uncertainties | No |
| Proton stopping/range | Species/material-state identity, original source bytes, CSDA versus projected definition, units, domain, interpolation assessment, uncertainty and measured transmission benchmark | No qualified tables ingested |
| Proton detection | Response, geometry/acceptance/exposure, dead layer, calibration/source hashes, losses and backgrounds | No |
| Event-rate nuclear input | Reaction-channel/observable semantics and LAB/CM frame; source-qualified event normalization with correlations | Alpha-observable source exists; conversion unresolved |
| Correlated alpha births | Physical masses/Q, channels/branch probabilities, eventwise conservation oracle, source-qualified energy-angle correlations | No qualified generator in this reference |
| Alpha stopping/range | Separate species/material-state tables, straggling/scattering qualification, same layer stack | No qualified tables ingested |
| Alpha detection | Measured species/energy/angle response, geometry, exposure, uncertainty, saturation/background behavior | No |
| Independent holdouts | Grouped specimen/batch/calibration partition and frozen criteria derived from measurement precision | Protocol only |

A physical proton-transmission study can proceed before the alpha chain is complete, once its own inputs qualify. That is the first discriminating interface. The same stopping model must predict withheld energies and areal densities without thickness-by-thickness retuning. Only then use alpha spectra to test the additional nuclear/alpha/detector interfaces.

## Acquisition receipt

Official NIST documentation was consulted for range definitions, units and approximation limits:
- https://physics.nist.gov/PhysRefData/Star/Text/appendix.html
- https://physics.nist.gov/PhysRefData/Star/Text/programs.html

A direct Python urllib retrieval of `https://physics.nist.gov/PhysRefData/Star/Text/PSTAR-t.html` returned HTTP 403. No numerical stopping table was acquired from that attempt. This access result does not prove that BN data are globally absent, and neither elemental data nor a mixture estimate will be silently relabeled as a measured BN table.

If a NIST, IAEA or SRIM/TRIM table is used later, retain the original bytes, license/access terms, material recipe/state, software/version and run card where relevant. Evaluated or calculated tables are useful model inputs but must retain their evidence class and be checked against a physical transmission benchmark.

## Experimental comparison sequence

1. Choose a documented conventional beam and the simplest manufacturable target stack supported by actual material data. Do not choose thickness by forcing an old model's optimum.
2. Predict incident/transmitted proton distributions, fold the measured proton response and compare held-out material/energy points. Current straight-track CSDA is a reference; add scattering/straggling where data show they matter.
3. Qualify event normalization and correlated birth kinematics separately; retain the reported alpha observable if event normalization remains unresolved.
4. Propagate alphas through the same actual stack and calibrated detector response. Compare absolute spectra and shapes on beam-upstream/downstream faces, plus any measured lateral acceptance under a suitable geometry model.
5. Propagate source/material/calibration covariance and test grouped holdouts. Keep all raw attempts and explicit missingness; this kernel is not the all-shot causal estimator.
6. Freeze predictions only under the existing independently reviewed G0-B blinding protocol and project-lead approval. Calibration is not blind validation.

This register records evidence needs. It is not a beam-time request, hardware instruction, fabricated calibration or scientific acceptance record.
