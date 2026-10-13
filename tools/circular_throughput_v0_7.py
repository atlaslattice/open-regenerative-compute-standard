#!/usr/bin/env python3
"""Gross output and unrestricted transaction turnover sensitivities; stdlib."""
import json,csv
from pathlib import Path
R=Path(__file__).resolve().parents[1];D=R/"data/throughput_v0_7"
def read(p):return json.loads(p.read_text())
a=read(D/"assumptions.json");m=read(R/"data/circular_economy_v0_6/macro_sources.json")
trade=read(R/"data/raw_materials_v0_4/trade_2025.json")["rows"]
gdp=m["gdp_2025_busd"];transaction_ratio=a["transaction_baseline_busd"]/gdp
funds_ratio=a["reference_fedwire_busd"]/gdp
cases=[];details=[]
for c in a["cases"]:
 B=X=V=0
 for r in trade:
  sector=a["mapping"].get(r["commodity"])
  if sector is None:continue
  z=m["intermediate_inputs"]["rows"][sector]/m["gross_output"]["rows"][sector]
  b=r["imports_musd"]/1000*c["eligibility"]*c["deployment"]
  # Geometric proxy: same sector coefficient in every upstream round.
  x=b/(1-z*c["domestic_input_fraction"])
  v=x*(1-z)
  B+=b;X+=x;V+=v
  details.append(dict(case=c["name"],commodity=r["commodity"],sector=sector,
   source_input_share=z,domestic_input_fraction=c["domestic_input_fraction"],
   imports_replaced_busd=b,before_displacement_gross_output_busd=x,
   before_displacement_gdp_busd=v))
 retention=1-c["displacement_fraction"]
 netX=X*retention;netV=V*retention
 cases.append(dict(case=c["name"],imports_replaced_busd=B,
  before_displacement_gross_output_busd=X,
  incremental_production_gross_output_busd=netX,
  incremental_gdp_busd=netV,percent_gdp=100*netV/gdp,
  user_baseline_incremental_transactions_busd=netV*transaction_ratio,
  user_baseline_total_transactions_busd=a["transaction_baseline_busd"]+netV*transaction_ratio,
  reference_fedwire_incremental_transactions_busd=netV*funds_ratio,
  actual_incremental_transactions=None,actual_taxable_base=None,tax_revenue=None))
sens=[dict(case=c["case"],response_factor=q,incremental_transactions_busd=c["user_baseline_incremental_transactions_busd"]*q) for c in cases for q in a["turnover_response_sensitivity"]]
for filename,rows in [("scenario_results.csv",cases),("sector_calculations.csv",details)]:
 with (D/filename).open("w",newline="") as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
summary={"status":"SIMULATED; aggregate payment/GDP ratio is a scaling assumption, not money velocity or estimated causal multiplier",
 "user_transaction_to_gdp_ratio":transaction_ratio,"reference_fedwire_to_gdp_ratio":funds_ratio,
 "cases":cases,"turnover_response_sensitivity":sens,"realized_credit":0}
(D/"summary.json").write_text(json.dumps(summary,indent=2)+"\n")
assert len(details)==69
assert abs(cases[1]["imports_replaced_busd"]-95.7024)<1e-6
assert all(c["actual_taxable_base"] is None for c in cases)
assert all(c["incremental_production_gross_output_busd"]>c["incremental_gdp_busd"] for c in cases)
assert all(c["user_baseline_total_transactions_busd"]>=a["transaction_baseline_busd"] for c in cases)
print(json.dumps(summary,indent=2))
