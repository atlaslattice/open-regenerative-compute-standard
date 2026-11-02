# Beyond Q v2.4 — recovery interface and historical benchmark preparation

This additive package follows [v2.3](../isotope_refinery_lineage_v2_3/README.md) and preserves the v2.2 reactor, financing and rollout results. It supplies a dynamic He3 stage interface with **assumed** response parameters, not a calibrated plasma or equipment model. No overall parent recovery case is replaced.

```sh
cd research/stars_2_0/extensions/beyond_q/recovery_interface_v2_4
python run.py
python -m unittest -v test_model.py
```

Python 3.12+, standard library only. Outputs include five diagnostic stage ledgers, molar inventories, consumption/loss accounts, required downstream yields, timestep refinements and a visible historical source disagreement. Read [REPORT.md](REPORT.md) before interpreting them.

The 1982 journal PDF remains inaccessible in this environment. The downloaded 1980 precursor is distinct and does not supply its later plasma benchmark. Optional lawful acquisition of the precursor:

```sh
python fetch_precursor.py /tmp/CoSCD1980.pdf
```

The PDF is not redistributed here. `source_access.json` records its hash, source location and inspected pages. All physical gates remain open.
