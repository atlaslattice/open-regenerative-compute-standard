# American Recovery and Resilience: public research release

**October 17, 2026 · White paper/model v0.1 · Dashboard v0.8**

PROPOSED / SIMULATED / NO REALIZED CREDIT. County requirements are mandatory design constraints; no actual local benefits are claimed verified.

- [Read the white paper](WHITE_PAPER.md).
- [Download the prototype and reproducible research package](ORCS_Recovery_Resilience_v08.zip).
- [Compare A/B/C summaries](abc-summary.csv).
- [Inspect every projection year, including loan tail](abc-annual.csv).
- [Inspect county-by-county benefit requirements](county-benefit-gates.csv).
- [Inspect assumptions](scenario-inputs.json) and [model code](run_abc.py).

The downloadable ZIP includes the standalone HTML dashboard, white paper, Python model and input/results files, county registry, editable-source extractor and tests. Extract it, then open `prototype/ORCS_American_Resilience_Lab_v08.html` in a modern browser. Bundled snapshots and simulations work offline. Source pages and optional live feed refreshes require connectivity. No hosted fork was created; the original public dashboard is unchanged.

The A/B/C screens use partial installed capital of about $38.6B/$96.7B/$196.5B after assumed allowances, last modeled commissioning in years 6/7/10, and steady uncovered cash of about $2.64B/$8.33B/$21.22B annually while all loans are active. These are disclosed scenario assumptions, not actual vendor costs or commitments. See the white paper for exclusions, county requirements, the verified phosphate-fertilizer emergency, environmental gates, workforce/QOL proposals, and why trade-deficit elimination is not established.

## Reproduce

Run `python run_abc.py` and `python test_abc.py` from this directory. In the ZIP these files are under `analysis/`.

For dashboard source and tests, run `python unpack_portable.py` from `prototype/`, then (with Node.js installed) run:

```
node test-recovery.cjs
node test-upstream.cjs
node test-build.cjs
node test-ui-startup.cjs
```

The extractor recreates editable `dist/` files from the self-contained HTML. It does not download dependencies. A/B/C results are precomputed in the prototype; edit inputs and rerun the Python model to create new scenarios. The other recovery and regional construction controls calculate interactively in the browser.

The Python model extends beyond programme year 30 through final loan payments, which occur in years 33/34/36. It does not treat debt at the reporting boundary as forgiven. The funding gap includes debt service; it is not a public economic loss calculation. Zero inflation is a scenario convention, not a forecast.

## Verification

Nine Python model checks pass, along with 19 recovery checks, critical-path construction checks, existing ledger/route checks, and a DOM startup/interaction harness. Inline scripts pass syntax checks. Browser visual and touch-interaction QA were unavailable; no claim of full production validation is made.

## Provenance and license

Derived from the owner-authorized ORCS America Supply Atlas source commit `984922b39cd0956d2bdf660a2c6789b6eb7d9ad7`, national waste-network v0.1 screening outputs, and New Deal 2.0 v0.2 source commit `c6a0890734d315b414e86d5b8a1665825bff014e`. Historical data retain their source labels. No new connection to government, ICON, or other manufacturers is implied. Documentation and original new code follow the repository's CC BY-SA 4.0 contribution terms; bundled third-party code retains its own notices, including Leaflet's BSD license. Government datasets and third-party source materials retain their respective terms.
