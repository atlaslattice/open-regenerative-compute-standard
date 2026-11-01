"""Derive custody/project tables and a standalone dashboard from executed logs."""
from pathlib import Path
import csv,json,math
ROOT=Path(__file__).resolve().parent

def read(path):
    with path.open() as f:return list(csv.DictReader(f))
def write(path,rows):
    keys=list(dict.fromkeys(k for r in rows for k in r))
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(rows)
def typed(rows):
    out=[]
    for row in rows:
        r={}
        for k,v in row.items():
            if v=='':r[k]=None
            elif v in ('True','False'):r[k]=v=='True'
            else:
                try:r[k]=float(v)
                except ValueError:r[k]=v
        out.append(r)
    return out

def main():
    from dashboard import render
    out=ROOT/'outputs';execution=json.loads((out/'execution.json').read_text());p=execution['inputs']
    decay=math.log(2)/(p['T_half_life_years']*365.25);horizon=p['years']*365.25
    custody=[];projects=[];timing=[]
    for check in execution['checks']:
        scenario=check['scenario'];path=out/f'events_{scenario}.jsonl'
        events=[json.loads(x) for x in path.read_text().splitlines()]
        received={e['shipment']:e for e in events if e['event']=='receipt'}
        commissions=[e for e in events if e['event']=='commissioned']
        for e in events:
            if e['event']=='construction_authorized':
                projects.append(dict(scenario=scenario,module=e['module'],authorized_day=e['day'],planned_ready_day=e['ready_day'],
                    donors=';'.join(map(str,e['eligible_donors'])),separate_external_hardware_subtotal_commitment_USD=e['hardware_subtotal_commitment_USD'],
                    donor_cash_required_USD=e['donor_cash_required_USD'],complete_installed_CAPEX_USD=None,
                    financing_evidence='conditional permission, not a real financing offer'))
            if e['event']!='fuel_reserved':continue
            receipt=received.get(e['shipment']);loaded=e['reserved_kg'];dispatch=e['day']+p['cascade']['construction_days']
            end=receipt['day'] if receipt else horizon
            current=0. if receipt else loaded*math.exp(-decay*(horizon-e['day']))
            loss=receipt['loss_kg'] if receipt else 0.
            mass_received=receipt['received_kg'] if receipt else 0.
            radioactive_loss=loaded-current-loss-mass_received
            custody.append(dict(scenario=scenario,shipment=e['shipment'],donor=e['donor'],recipient=e['module'],
                reserved_day=e['day'],scheduled_dispatch_day=dispatch,
                receipt_day=receipt['day'] if receipt else None,loaded_kg=loaded,
                received_kg=mass_received,remaining_reserved_or_transit_kg=current,decay_kg=radioactive_loss,transport_loss_kg=loss,
                final_phase='received' if receipt else ('reserved_during_construction' if horizon<dispatch else 'in_transit'),
                donor_after_reservation_kg=e['donor_remaining_kg'],donor_floor_kg=e['donor_floor_kg'],
                opportunity_value_USD=e['illustrative_external_sale_value_foregone_USD'],actual_transfer_receipts_USD=None))
        timing.append(dict(scenario=scenario,commissioned_by_horizon=check['commissioned_modules'],
            first_successor_commission_year=commissions[0]['day']/365.25 if commissions else None,
            last_successor_commission_year=commissions[-1]['day']/365.25 if commissions else None,
            commissioned_50_year=next((e['day']/365.25 for e in commissions if e['module']==50),None),
            max_pool_mass_residual_kg=check.get('max_pool_mass_residual_kg'),
            donor_floor_violations=check.get('donor_reserve_floor_violations'),physical_validation=False))
    if custody:write(out/'fuel_custody.csv',custody)
    if projects:write(out/'project_financing.csv',projects)
    write(out/'rollout_comparison.csv',timing)
    # Custody derivation must independently reproduce the controller pool totals.
    for check in execution['checks']:
        if 'fuel_reserved_sent_kg' not in check:continue
        match=[r for r in custody if r['scenario']==check['scenario']]
        for key,field in [('fuel_reserved_sent_kg','loaded_kg'),('fuel_received_kg','received_kg'),
                          ('escrow_transport_decay_kg','decay_kg'),('transport_loss_kg','transport_loss_kg'),
                          ('reserved_and_transit_inventory_kg','remaining_reserved_or_transit_kg')]:
            if not math.isclose(sum(r[field] for r in match),check[key],rel_tol=1e-9,abs_tol=1e-7):
                raise ArithmeticError('custody reconciliation: '+key)
    render(typed(read(out/'annual_finance.csv')),typed(read(out/'fleet_inventory.csv')),timing,out/'dashboard.html')
    print(json.dumps(timing,indent=2));print('Independent shipment/custody sums reconcile.')

if __name__=='__main__':main()
