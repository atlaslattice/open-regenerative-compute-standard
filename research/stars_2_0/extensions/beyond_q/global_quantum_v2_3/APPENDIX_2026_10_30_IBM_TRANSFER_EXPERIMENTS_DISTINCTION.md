# Quantum evidence graph — Distinguishing IBM transfer experiments
**2026-10-30 · Source-tracing note; no calibrated demand.py parameter changes**
## Interchip coupling experiment
IBM Oct 27 connected two Nighthawk R1 processors using four ~80 cm L-couplers **within one dilution refrigerator**, demonstrating 99% average quantum-state transfer fidelity and 94.75% average distant CZ-gate fidelity. Not remote cryostats or demonstrated distributed fault-tolerant computation.
Primary: https://www.ibm.com/quantum/blog/connecting-quantum-processors-with-l-couplers
## Quantum-walk state-transfer preprint (different experimental object)
Copilot cites *Perfect and peak state transfer on IBM quantum hardware*, https://arxiv.org/abs/2610.20855v1 . Reported quantum walk experiments on Heron processor **are not the L-coupler hardware experiment**. Original preprint was not independently retrieved in this review; treat its detailed performance and 156-qubit claim as **EXTERNAL-AI-REPORTED / PENDING FULL-TEXT AUDIT**.
## Explicit non-equivalence chain
Algorithmic state transfer on an individual processor ≠ physical interchip couplers ≠ independent-cryostat network ≠ distributed fault-tolerant computation. Preserve configuration IDs, device types, fidelities, mitigated/unmitigated conditions and source types separately.
