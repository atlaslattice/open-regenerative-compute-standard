#!/usr/bin/env python3
"""Reproduce v0.3 screening; stdlib only. UNKNOWN is represented by null."""
import csv,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/"data/us_supply_ledger_v0_3_2026-10-12.json").read_text())
out=[]
for r in d["rows"]:
    p,i,e,c,s0,s=[r.get(k) for k in ("production","imports","exports","consumption","stocks_prior","stocks")]
    net=i-e if i is not None and e is not None else None
    simple=p+net if p is not None and net is not None else None
    draw=s0-s if s0 is not None and s is not None else None
    adjusted=simple+draw if simple is not None and draw is not None else None
    out.append(dict(commodity=r["id"],basis=r["basis"],production=p,imports=i,exports=e,
      net_imports=net,consumption=c,simple_supply=simple,stock_change= None if draw is None else -draw,
      stock_adjusted_supply=adjusted,residual=None if adjusted is None or c is None else adjusted-c,
      imports_zero=False if i is not None and i>0 else None,
      reserve_gap=None,deliverable_surplus=None,export_gate="NOT_SATISFIED_IMPORTS" if i is not None and i>0 else "UNKNOWN"))
dest=ROOT/"data/us_supply_derived_v0_3_2026-10-12.csv"
with dest.open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
# Sensitivity: divert fractions of exported aluminum scrap, NOT landfill recovery.
cases=[]
for capture in (.25,.5,.75):
    scrap=2200*capture
    for yield_ in (.7,.85,.95):
        product=scrap*yield_
        cases.append(dict(capture=capture,assumed_yield=yield_,scrap_diverted_kt=scrap,
          potential_product_kt=product,percent_gross_product_imports=product/4400*100,
          verified_import_displacement_kt=None,net_benefit=None))
(ROOT/"data/us_aluminum_sensitivity_v0_3_2026-10-12.json").write_text(json.dumps(cases,indent=2)+"\n")
assert out[0]["net_imports"]==1590 and out[0]["stock_adjusted_supply"]==2113
assert next(r for r in out if r["commodity"]=="aluminum_scrap")["net_imports"]==-1310
assert next(r for r in out if r["commodity"]=="phosphate_rock")["net_imports"] is None
assert all(r["export_gate"]!="ELIGIBLE" for r in out)
print(json.dumps({"rows":len(out),"output":str(dest),"checks":"passed","realized_credit":0}))
