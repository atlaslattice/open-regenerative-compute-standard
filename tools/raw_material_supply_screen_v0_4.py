#!/usr/bin/env python3
"""Whole raw-material family screen. Standard library; frozen Census receipt."""
import csv,json
from pathlib import Path
R=Path(__file__).resolve().parents[1];D=R/"data/raw_materials_v0_4"
d=json.loads((D/"trade_2025.json").read_text())
rows=d["rows"]
for r in rows:
    i,e=r["imports_musd"],r["exports_musd"]
    r["export_minus_import_minus_reserve_proxy_musd"]=round(e-1.2*i,3)
    r["freight_sensitivity_2pct_musd"]=round(.02*i,3)
    r["freight_sensitivity_5pct_musd"]=round(.05*i,3)
    r["freight_sensitivity_10pct_musd"]=round(.1*i,3)
with (D/"raw_material_trade_reserve_screen.csv").open("w",newline="") as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
scenarios=[]
for capture in (.25,.5,.75):
 for yield_ in (.5,.8,.95):
  for grade in (.5,.8,1):
   # Normalized to 100 wet tonnes eligible additional feedstock.
   feed=100*capture;output=feed*yield_*grade
   for processing in (10,30,60,100):
    for freight in (10,30,60):
     scenarios.append(dict(capture=capture,yield_assumption=yield_,grade_fraction_assumption=grade,
      feed_tonnes=feed,qualified_product_tonnes=output,
      processing_usd_per_feed_tonne=processing,
      assumed_avoided_import_freight_usd_per_product_tonne=freight,
      processing_usd_per_qualified_product_tonne=processing/(yield_*grade),
      freight_only_margin_usd=output*freight-feed*processing,
      full_net_benefit=None,coast_to_coast_transport=None))
(D/"processing_vs_freight_sensitivity.json").write_text(json.dumps({"columns":list(scenarios[0]),"rows":[list(r.values()) for r in scenarios]},separators=(",",":"))+"\n")
assert len(rows)==25 and len(scenarios)==324
assert next(r for r in rows if r["commodity"]=="Fertilizers")["deficit_plus_reserve_proxy_musd"]==6540.8
assert next(r for r in rows if r["commodity"]=="Metalliferous ores and metal scrap")["surplus_musd"]==18494
assert all(r["coast_to_coast_transport"] is None for r in rows)
head="| Material family | Exports $B | Imports $B | Deficit $B | Deficit + reserve proxy $B |\n|---|---:|---:|---:|---:|"
table=head+"\n"+"\n".join(f'| {r["commodity"]} | {r["exports_musd"]/1000:.3f} | {r["imports_musd"]/1000:.3f} | {r["deficit_musd"]/1000:.3f} | {r["deficit_plus_reserve_proxy_musd"]/1000:.3f} |' for r in rows)
(D/"table.md").write_text(table+"\n")
print(json.dumps({"families":len(rows),"freight_processing_cases":len(scenarios),"checks":"passed","realized_credit":0}))
