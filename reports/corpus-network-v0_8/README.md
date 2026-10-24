# Corpus network white paper v0.8

24 October 2026. Networked retrofit nodes; co-location optional. Extends frozen v0.7 without overwriting it.

Read [WHITE_PAPER.md](WHITE_PAPER.md). Covers existing industrial reuse, full Desen integration surface and landfill mining, biological and nutrient sidecars, brine/mineral/chloride recovery, residual closure, industrial/agricultural uses, and 0/100/500/1210 MW IT comparisons. The 1.21 GW case is deliberately exploratory and has no claimed Stargate affiliation.

Chinese-reference packages remain candidates. All 27 price anchors are retained; imported comparisons are excluded from the proposed Chinese package. Prices need original sourcing URLs. No installed total or physical performance is established.

Run `python scenarios.py` and `python -m unittest discover -s . -p 'test_*.py' -v`. Nine new tests check boundaries and arithmetic, not treatment performance. The earlier v0.7 suite has 86 tests separately.

Results are in `results/`; inputs in `inputs.json`; the module and network registers make unknown suppliers and acceptance gates explicit. CSV blanks mean unknown. Actual mineral revenues remain zero pending qualification, not a forecast of zero potential.

Source register and full narrative references are in the paper. No full copyrighted source PDFs are redistributed.

## Public-health integration addendum

[Wastewater observability v0.1](../../docs/wastewater-observability-v0_1/WASTEWATER_PUBLIC_HEALTH_OBSERVABILITY_v0_1.md) establishes a first-class sampling/laboratory/data interface for future wastewater nodes and retrofit assessments. No new measured health output, provider agreement or cost is added to these scenarios. The original v0.8 PDF and model remain preserved.
