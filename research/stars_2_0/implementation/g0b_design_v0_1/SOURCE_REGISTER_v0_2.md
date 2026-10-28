# Stopping-source register v0.2 — acquisition status

2026-10-28. Supplements v0.1; does not replace its files. Physical validation NOT_RUN. No new physical numerical data were acquired in this release.

Primary references rechecked:

- NIST material list https://physics.nist.gov/PhysRefData/Star/Text/table2.html includes aluminum, silicon and carbon but not elemental B or BN. Proton and helium-ion transport require separately qualified datasets.
- NIST introduction https://pml.nist.gov/PhysRefData/Star/Text/intro.html describes a default 133-energy proton grid. Our pinned aluminum mirror has 132 rows. Completeness/version remains unresolved: the discrepancy does not identify a missing row or prove a particular corruption. No interpolated repair is authorized. Exact primary table acquisition and row-by-row comparison remain open.
- IAEA https://www-nds.iaea.org/stopping/ explicitly compiles electronic stopping with nuclear stopping subtracted or negligible. Its proton AND helium-on-B data are acquisition targets, not substitutes for total CSDA ranges. Original numeric archive/reference-map retrieval remains incomplete.
- SRIM author pages https://www.srim.org/SRIM/SRIMPICS/STOPPLOTS.htm and https://www.srim.org/SRIM/SRIMPICS/IONIZ.htm provide B stopping/experimental-reference leads for H and He. No numeric values or paper labels were recovered or adopted here. Calculations/plots require provenance back to original experiments before validation; a different host is not independent experimental evidence.

Qualification queue, in order:

1. Reconcile aluminum PSTAR primary values, grid, version and units with mirror SHA256 3fe6459ec4abde6052bcb63f427ea856bbc35dd8506014191145b4eb9253db5e. Keep mirror status candidate until resolved.
2. Obtain original proton/B and helium/B numeric data with paper IDs, errors, material state and energy/charge-state conventions. Resolve A–D mapping of the earlier headerless 77-row boron mirror; retain quarantine meanwhile.
3. Select relevant energy coverage from the actual incident spectrum and reaction birth distribution; require residual-energy tail coverage or an explicit, tested model. Never extend a table silently to zero.
4. Qualify any nuclear-stopping contribution separately; propagate model and shared source uncertainty. Electronic stopping alone is not total stopping.
5. Acquire independent transmission and alpha calibration observations with target areal-density/composition metadata, detector response, beam distribution and shared-source ancestry. An evaluated table used to make the prediction cannot independently validate that prediction.

Fabrication feasibility and independent metrology may force revision of the proposed self-supporting B-11 target. This is a tracked decision, not a reason to import BN stopping or conceal an unmodeled backing.
