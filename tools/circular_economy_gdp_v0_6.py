#!/usr/bin/env python3
"""Reproduce v0.6 circular GDP sensitivities and expanded consumption ledger."""
import csv,json
from pathlib import Path
R=Path(__file__).resolve().parents[1];D=R/"data/circular_economy_v0_6"
def read(p):return json.loads(p.read_text())
trade=read(R/"data/raw_materials_v0_4/trade_2025.json")["rows"]
basket=[r for r in trade if r["scope"] not in ("energy_comparator","mixed_review")]
imports=sum(r["imports_musd"] for r in basket)/1000
macro=read(D/"macro_sources.json");gdp=macro["gdp_2025_busd"]
assumptions=read(D/"scenario_assumptions.json")
scenarios=[]
for a in assumptions["scenarios"]:
 replaced=imports*a["eligible_import_fraction"]*a["deployment_fraction"]
 direct=replaced*a["incremental_direct_va_fraction"]
 gross=direct*a["va_multiplier"]
 displaced=gross*a["displacement_fraction_of_gross_va"]+a.get("additional_displaced_gdp_busd",0)
 net=gross-displaced
 scenarios.append(dict(name=a["name"],import_replacement_busd=replaced,
  direct_incremental_va_busd=direct,multiplier_gross_va_busd=gross,
  displaced_va_busd=displaced,net_gdp_level_busd=net,
  percent_2025_gdp=100*net/gdp,
  sum_10year_linear_ramp_gdp_busd=net*(assumptions["ramp_years"]+1)/2))
industries=["Agriculture, forestry, fishing, and hunting","Mining","Utilities","Construction","Manufacturing"]
effbase=sum(macro["intermediate_inputs"]["rows"][k] for k in industries)
efficiency=[dict(name=a["name"],input_base_busd=effbase,
  addressable_input_busd=effbase*a["addressable_share"],
  gross_cost_saving_busd=effbase*a["addressable_share"]*a["cost_reduction"],
  gdp_impact=None) for a in assumptions["efficiency_cases"]]
old=read(R/"data/consumption_shortfall_v0_5_2026-10-12.json")["rows"]
new=read(D/"additional_physical_rows.json")
# Replace the previously incomplete steel row, never duplicate its consumption.
phys=[r for r in old if r["id"]!="steel"]+new
expanded=[]
for r in phys:
 c,p,e=[r.get(k) for k in ("consumption","production","exports")]
 expanded.append(dict(id=r["id"],unit=r["unit"],annual_consumption=c,
  domestic_output_or_proxy=p,
  annual_domestic_only_gap=None if c is None or p is None else max(c-p,0),
  reserve20_target=None if c is None else c*.2,
  exports=r.get("exports"),imports=r.get("imports"),
  gap_with_exports_retained=None if c is None or p is None or e is None else max(c+e-p,0),
  actual_unmet_demand=None,certified_reserve_gap=None,boundary=r["boundary"]))
# Retain literal source tables separately; numerical proxy validation is explicit.
for file,rows in [("gdp_scenarios.csv",scenarios),("physical_consumption_gaps.csv",expanded)]:
 with (D/file).open("w",newline="") as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
summary={"status":"SIMULATED assumptions, not calibrated GDP forecast","import_basket_busd":imports,
 "trade_families_in_basket":len(basket),"gdp_2025_busd":gdp,
 "gross_output_2025_busd":macro["gross_output"]["rows"]["All industries"],
 "intermediate_inputs_2025_busd":macro["intermediate_inputs"]["rows"]["All industries"],
 "scenario_results":scenarios,"efficiency_savings_separate_from_gdp":efficiency,
 "physical_rows":len(expanded),"source_chapters":len(read(D/"mineral_43_chapter_receipts.json")["chapters"]),
 "realized_credit":0}
(D/"summary.json").write_text(json.dumps(summary,indent=2)+"\n")
assert len(basket)==23 and abs(imports-478.512)<1e-6
assert len(expanded)==23
assert next(r for r in expanded if r["id"]=="zinc_refined")["annual_domestic_only_gap"]==600000
assert next(r for r in expanded if r["id"]=="steel")["annual_domestic_only_gap"]==13
assert next(r for r in expanded if r["id"]=="nickel_total")["annual_domestic_only_gap"] is None
assert next(r for r in scenarios if r["name"]=="adverse")["net_gdp_level_busd"]<0
assert abs(macro["gross_output"]["rows"]["All industries"]-macro["intermediate_inputs"]["rows"]["All industries"]-gdp)<.01
print(json.dumps(summary,indent=2))
