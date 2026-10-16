#!/usr/bin/env python3
"""ORCS Maui v1.0 visitor revenue, household rebate, financing stress test.
All amounts 2026 USD. Does NOT imply legislative power to levy visitor-specific tax.
Run with: python3 maui_visitor_funding_v10.py
"""
import csv
from pathlib import Path
BASE=Path(__file__).resolve().parent
PREVIOUS_DEBT=622.8e6
PREVIOUS_FULL_GAP=856.2e6
HOUSEHOLDS=55841 # county ACS 2020-24, not Maui Island-only
ELIGIBLE_SPEND_PER_HOME=30000 # pure assumption
RESIDENT_DISCOUNT=.03
RESIDENT_COST=HOUSEHOLDS*ELIGIBLE_SPEND_PER_HOME*RESIDENT_DISCOUNT
CAPTURE_COST=.02 # Assumed admin/collection cost as % of gross visitor collections
SPENDING_BASES={"User-selected eligible spending scenario":3.9e9,
                "All 2025 Maui visitor expenditures (upper-base stress)":5.97e9}
RATES=[.02,.03,.04,.05]
def main():
 rows=[]
 for name,base in SPENDING_BASES.items():
  for rate in RATES:
   gross=base*rate
   admin=gross*CAPTURE_COST
   net=gross-admin-RESIDENT_COST
   gap=PREVIOUS_FULL_GAP-net
   rows.append({"base":name,"spend_usd":round(base),"rate":rate,
    "gross_visitor_charge_usd":round(gross),
    "collection_cost_usd":round(admin),
    "resident_3pct_discount_usd":round(RESIDENT_COST),
    "net_new_funding_usd":round(net),
    "existing_modeled_annual_debt_usd":round(PREVIOUS_DEBT),
    "existing_full_annual_funding_gap_usd":round(PREVIOUS_FULL_GAP),
    "remaining_annual_gap_usd":round(gap),
    "share_debt_paid_by_net_new_funding":round(net/PREVIOUS_DEBT,4)})
 with open(BASE/"maui_visitor_funding_v10.csv","w",newline="") as f:
  w=csv.DictWriter(f,rows[0].keys());w.writeheader();w.writerows(rows)
 for row in rows:
  print(row["base"],"Rate",f'{row["rate"]*100:.0f}%',
    "gross",f'${row["gross_visitor_charge_usd"]/1e6:.1f}M',
    "net",f'${row["net_new_funding_usd"]/1e6:.1f}M',
    "remaining annual gap",f'${row["remaining_annual_gap_usd"]/1e6:.1f}M')
 print("Caution: tourism spend base may include items not legally eligible; rate is")
 print("NOT authorized; no effects on visitor volumes, spending or retail prices modeled.")
if __name__=="__main__":main()
