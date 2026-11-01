"""Expose existing v2.0 DD/DT flows without changing physics or financial inputs.

Run the parent module_fleet_v2_0/run.py first, then python audit.py.
"""
from pathlib import Path
import csv,json,hashlib,math

ROOT=Path(__file__).resolve().parent
PARENT=ROOT.parent/'module_fleet_v2_0'
T_MOLAR=.00301604928;HE3_MOLAR=.0030160293201;HE4_MOLAR=.00400260325413
YEAR=365.25;NA=6.02214076e23;MEV=1.602176634e-13

def number_rows(path):
    with path.open() as f:
        return [{k:None if v=='' else (v if k in ['price_case','offtake_case'] else (v=='True' if v in ['True','False'] else float(v)))
                 for k,v in row.items()} for row in csv.DictReader(f)]

def reconcile(products,physical,p):
    grouped={};stages=[]
    b_source_kg_day=p['B_fusion_MW']*1e6/(17.6*MEV)*86400*(T_MOLAR/NA)*p['source_duty']
    for r in physical:
        key=(int(r['fleet_modules']),int(r['year']))
        group=grouped.setdefault(key,[]);group.append(r)
        base=dict(fleet_modules=key[0],module=int(r['module']),year=key[1])
        requested_commission=(base['module']-1)*p['commissioning_interval_years']*YEAR
        simulated_commission=math.ceil(requested_commission/p['step_days']-1e-10)*p['step_days']
        active_days=max(0.,min(YEAR,base['year']*YEAR-simulated_commission))
        a_net=-24*(p['A_net_draw_MW_assumed']*r['A_on_days']+p['A_shutdown_draw_MW']*(active_days-r['A_on_days']))
        b_gross=r['b_burn']/b_source_kg_day*24*p['B_gross_electric_MW_at_1130_fusion']*p['B_fusion_MW']/1130
        b_net=b_gross-24*(p['B_own_draw_MW']*r['B_on_days']+p['B_shutdown_draw_MW']*(active_days-r['B_on_days']))
        shared=p['shared_processing_draw_MW_assumed']*active_days*24
        if not math.isclose(a_net+b_net-shared,r['net_MWh'],rel_tol=1e-9,abs_tol=1e-5):
            raise ArithmeticError('stage electrical reconciliation failed')
        for reactor,role,birth,bred,burn,transfer_in,transfer_out,he3,he4,net in [
            ('A_DD','He3 and T factory',r['dd_birth'],0.,r['a_burn'],0.,r['a_transfer'],r['he3_born'],r['a_burn']/T_MOLAR*HE4_MOLAR,a_net),
            ('B_DT','DT power and own blanket breeding',0.,r['b_birth'],r['b_burn'],r['a_transfer'],0.,0.,r['b_burn']/T_MOLAR*HE4_MOLAR,b_net)]:
            stages.append(dict(**base,reactor_id=f"{reactor}-{base['module']}",stage_role=role,
                T_direct_DD_birth_kg=birth,T_blanket_birth_kg=bred,T_consumed_kg=burn,
                T_transfer_in_kg=transfer_in,T_transfer_out_kg=transfer_out,
                He3_direct_birth_kg=he3,He4_plasma_birth_kg=he4,
                conditional_net_electricity_MWh=net,
                T_decay_by_reactor_kg=None,T_processing_loss_by_reactor_kg=None,
                note='Per-reactor losses/states are not separately exported by parent; use explicit campus balance, do not assign zero. Shared site electrical load excluded from these stage nets.'))
    enriched=[];largest_residual=0.;largest_ratio_error=0.
    for r in products:
        r=dict(r);raw=grouped[(int(r['fleet_modules']),int(r['year']))]
        total=lambda k:sum(x[k] for x in raw)
        born=total('dd_birth');he3=total('he3_born')
        ratio=(he3/HE3_MOLAR)/(born/T_MOLAR) if born>0 else None
        residual=total('T_start_kg')+born+total('b_birth')-total('a_burn')-total('b_burn')-total('decay')-total('permeation')-total('process_loss')-total('exports')-total('T_end_kg')
        largest_residual=max(largest_residual,abs(residual))
        if ratio is not None:largest_ratio_error=max(largest_ratio_error,abs(ratio-1.))
        r.update(T_A_DD_birth_kg=born,He3_A_DD_birth_kg=he3,
            DD_He3_to_T_atom_birth_ratio=ratio,T_A_secondary_DT_consumed_kg=total('a_burn'),
            T_A_processed_delivery_kg=total('a_delivery'),T_A_to_B_transfer_kg=total('a_transfer'),
            T_start_kg=total('T_start_kg'),T_decay_kg=total('decay'),
            T_permeation_kg=total('permeation'),T_processing_loss_kg=total('process_loss'),
            T_inventory_change_kg=total('T_end_kg')-total('T_start_kg'),
            T_accounting_residual_kg=residual,
            He4_A_secondary_DT_birth_kg=total('a_burn')/T_MOLAR*HE4_MOLAR,
            He4_B_DT_birth_kg=total('b_burn')/T_MOLAR*HE4_MOLAR,
            B_gross_TBR_ratio=total('b_birth')/total('b_burn') if total('b_burn') else None,
            gross_He3_candidate_market_cap_share=(r['He3_market_cap_STP_L_per_year_fleet']/r['He3_product_candidate_STP_L'])
                if r['He3_market_cap_STP_L_per_year_fleet'] is not None and r['He3_product_candidate_STP_L']>0 else None)
        enriched.append(r)
    if largest_residual>1e-6 or largest_ratio_error>1e-9:raise ArithmeticError('birth or mass reconciliation failure')
    return enriched,stages,dict(largest_campus_T_residual_kg=largest_residual,
        largest_equal_branch_atom_ratio_error=largest_ratio_error,physical_validation=False)

def write(path,rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def main():
    from dashboard import render
    out=ROOT/'outputs';out.mkdir(exist_ok=True)
    products=number_rows(PARENT/'outputs/annual_products_finance.csv')
    physical=[]
    p=json.loads((PARENT/'outputs/execution.json').read_text())['inputs']
    for n in p['module_counts']:physical+=number_rows(PARENT/f'outputs/module_ledger_{n}.csv')
    rows,stages,checks=reconcile(products,physical,p)
    write(out/'annual_reconciled.csv',rows);write(out/'reactor_stages.csv',stages)
    render(rows,out/'dashboard.html')
    files=[PARENT/'model.py',PARENT/'finance.py',PARENT/'inputs.json',PARENT/'outputs/annual_products_finance.csv']
    hashes={str(x.relative_to(ROOT.parent)):hashlib.sha256(x.read_bytes()).hexdigest() for x in files}
    (out/'checks.json').write_text(json.dumps(dict(**checks,product_rows=len(rows),stage_rows=len(stages),parent_sha256=hashes),indent=2)+'\n')
    print(json.dumps(checks));print(f'{len(rows)} reconciled rows; {len(stages)} reactor-stage rows')

if __name__=='__main__':main()
