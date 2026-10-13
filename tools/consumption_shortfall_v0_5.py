#!/usr/bin/env python3
"""Consumption/production and reserve screen; all annual unless daily indicated."""
import json,csv
from pathlib import Path
R=Path(__file__).resolve().parents[1]
d=json.loads((R/"data/consumption_shortfall_v0_5_2026-10-12.json").read_text())
out=[]
for r in d["rows"]:
 c,p,e,stock=[r.get(k) for k in ("consumption","production","exports","stocks")]
 target=.2*c if c is not None else None
 gap=max(c-p,0) if c is not None and p is not None else None
 exportgap=max(c+e-p,0) if c is not None and p is not None and e is not None else None
 zero_stock_year1=max(1.2*c-p,0) if c is not None and p is not None else None
 out.append(dict(id=r["id"],unit=r["unit"],annual_consumption=c,daily_average=None if c is None else c/365,
  annual_production=p,domestic_production_only_gap=gap,existing_exports_retained_gap=exportgap,
  reserve20_domestic_use_target=target,reported_stock_candidate=stock,
  raw_stock_screen_gap=None if target is None or stock is None else max(target-stock,0),
  certified_reserve_gap=None,
  one_year_build_zero_initial_reserve_no_exports_gap=zero_stock_year1,
  actual_unmet_demand=None,deliverable_grade_matched_shortfall=None))
with (R/"data/consumption_shortfall_v0_5_2026-10-12.csv").open("w",newline="") as f:
 w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
assert abs(out[3]["domestic_production_only_gap"]-5.4)<1e-8
assert abs(out[5]["raw_stock_screen_gap"]-185.1058)<1e-6
assert abs(out[6]["one_year_build_zero_initial_reserve_no_exports_gap"]-954.84)<1e-6
assert all(r["actual_unmet_demand"] is None for r in out)
print(json.dumps({"rows":len(out),"checks":"passed","realized_credit":0}))
