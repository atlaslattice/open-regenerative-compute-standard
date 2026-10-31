"""Adverse control: keep A operating but credit neither reactor with breeding."""
from calculate import base,run,write
p=base('A0');p['tbr_b']=0
start=75
for _ in range(72):
 t,s=run(dict(p,step_days=1/96),start)
 if s['b_unserved_burn_kg']<=1e-8:break
 start+=1
else:raise RuntimeError('No full-year fuel-available start found in tested window')
launch=t[start-1];end=t[-1]
r=dict(A_case='A0',B_TBR=0,A_gross_fusion_W=1.1e9,B_gross_fusion_W=1.1e9,A_only_precharge_hours=start,B_available_at_start_kg=launch['b_store'],
 B_burn_kg=end['b_burn'],unserved_burn_kg=s['b_unserved_burn_kg'],stock_growth_B_year_kg=end['total_inventory']-launch['total_inventory'],
 final_B_available_kg=end['b_store'],maximum_mass_residual_kg=s['maximum_mass_residual_kg'],qualified_surplus_kg=None,
 evidence='Conditional arithmetic; prescribed gross fusion and assumed95percent A plasma recovery; no breeding credit')
write('zero_breeding_control.csv',[r]);print(r)
