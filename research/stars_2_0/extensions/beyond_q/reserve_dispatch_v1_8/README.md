# Beyond Q v1.8 — finite-horizon reserve / isotope dispatch

[Report](REPORT.md) · [Power-basis reconciliation](POWER_BASIS_RECONCILIATION.md)
· [Inputs](inputs.json) · [Scientific figure](outputs/dispatch.svg)

Primary design: two proposed1100MW ARC-class sources. The historical A+20MWe
projection is separate from its fusion rating and remains unvalidated. Laser
energy comparison is a separate variant at matched source exposure.

```bash
python provenance.py
python run.py
python -m unittest test_dispatch -v
```

Standard library only; optional figure needs matplotlib. Three-year fuel and
helium stocks are carried continuously. B breeding, recovery and He3 targets
remain assumptions; no actual isotope revenue or profit is credited. All physical
gates G1-G5 remain open. Earlier versions are unchanged.
