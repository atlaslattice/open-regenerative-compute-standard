# Beyond Q v1.9 — 350k total-coproduct capture

[Technical report](REPORT.md) · [Inputs](inputs.json) ·
[Reference annual table](outputs/reference_350k.csv) ·
[Tritium ledger figure](outputs/tritium_350k.svg)

Targets are350,000STP liters each **total** captured He-3 and direct recovered
T, before a sale/retention split. T kilograms and atom-equivalent/T2 molecular
liters are both explicit. B is continuously scheduled with15/16 source duty;
its burn, breeding, extraction and campus stock change remain separate.

```bash
python capture_provenance.py
python run.py
python summarize.py
python -m unittest test_target -v
```

Standard library; optional matplotlib figure. Two proposed1100MW ARC-class
fusion sources, with a separate laser energy variant. No qualified product,
actual revenue or physical self-sufficiency is claimed. G1-G5 remain OPEN.

[Original350k/350k benchmark reconciliation](CAPTURE_RECONCILIATION.md) traces equal branch births, route recovery and startup pipeline timing without changing the physics. Run `python reconcile_350k.py` and `python -m unittest discover -v` for the15-check combined audit.
