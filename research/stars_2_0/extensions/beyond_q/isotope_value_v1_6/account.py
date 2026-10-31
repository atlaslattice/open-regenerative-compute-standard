"""Conditional isotope accountancy and price thresholds; no reactor validation."""
from pathlib import Path
import csv,hashlib,json,math,sys
ROOT=Path(__file__).resolve().parent;PARENT=ROOT.parent;OUT=ROOT/'outputs'
sys.path.insert(0,str(PARENT/'wallplug_year_v1_5_1'))
import year
from fuelcycle.inventory import advance
from fuelcycle.physics import T_KG_PER_ATOM,AVOGADRO,MEV_J,probability,nonnegative
HE3_KG_PER_ATOM=.0030160293201/AVOGADRO
SOURCE_COMMIT='bcc987d7ea9f796e3aae949dcddfdeb79d094d1a'

def helium(rows,collection_day,capture_fraction):
    """Direct DD He3 -> collection -> stored; T-decay He3 is born but inaccessible.
    No D-He3 consumption is modeled: conditional upper-source survival scenario.
    """
    nonnegative(collection_day=collection_day);probability('capture_fraction',capture_fraction)
    mobile=stored=loss=direct=decay_born=0.;prior={};trajectory=[]
    for r in rows:
        hours=r['time_hours']-prior.get('time_hours',0.)
        atoms=(r['dd_events']-r['dd_t_atoms'])-(prior.get('dd_events',0.)-prior.get('dd_t_atoms',0.))
        decays=(r['decay']-prior.get('decay',0.))/T_KG_PER_ATOM
        if atoms < -1e-6 or decays < -1e-6:raise ValueError('source counter decreased')
        birth=max(0.,atoms)*HE3_KG_PER_ATOM;db=max(0.,decays)*HE3_KG_PER_ATOM
        mobile,exits=advance(mobile,birth/(hours/24),{'collection':collection_day},hours/24)
        collected=exits['collection'];stored+=collected*capture_fraction;loss+=collected*(1-capture_fraction)
        direct+=birth;decay_born+=db
        residual=direct+decay_born-mobile-stored-loss-decay_born
        if abs(residual)>1e-8:raise ArithmeticError('He3 source/storage closure failed')
        trajectory.append(dict(time_hours=r['time_hours'],He3_direct_born_kg=direct,He3_T_decay_born_kg=decay_born,
           He3_mobile_kg=mobile,He3_stored_candidate_kg=stored,He3_capture_loss_kg=loss,He3_inaccessible_decay_kg=decay_born,He3_residual_kg=residual))
        prior=r
    return trajectory

def terminal_allocation(r,h,reserve_T_kg,retain_He3_fraction,quality_acceptance):
    nonnegative(reserve_T_kg=reserve_T_kg);probability('retain_He3_fraction',retain_He3_fraction);probability('quality_acceptance',quality_acceptance)
    available=r['a_store']+r['b_store']
    T_candidate=max(0.,available-reserve_T_kg)
    return dict(T_storage_before_kg=available,T_terminal_sale_candidate_kg=T_candidate,T_storage_after_sale_kg=available-T_candidate,
      T_actual_qualified_sale_kg=None,T_pipeline_held_kg=r['total_inventory']-available,He3_stored_before_kg=h['He3_stored_candidate_kg'],
      He3_retained_kg=h['He3_stored_candidate_kg']*retain_He3_fraction,
      He3_quality_held_kg=h['He3_stored_candidate_kg']*(1-retain_He3_fraction)*(1-quality_acceptance),
      He3_terminal_sale_candidate_kg=h['He3_stored_candidate_kg']*(1-retain_He3_fraction)*quality_acceptance,
      He3_actual_qualified_sale_kg=None)

def realized_revenue(candidate_kg,qualified_kg,demand_kg,price_USD_per_kg):
    """Unknown qualification/demand/price stays unknown, never gross-birth revenue."""
    nonnegative(candidate_kg=candidate_kg)
    if any(x is None for x in (qualified_kg,demand_kg,price_USD_per_kg)):return None
    nonnegative(qualified_kg=qualified_kg,demand_kg=demand_kg,price_USD_per_kg=price_USD_per_kg)
    if qualified_kg>candidate_kg+1e-12:raise ValueError('qualification exceeds disjoint sale allocation')
    return min(candidate_kg,qualified_kg,demand_kg)*price_USD_per_kg

def threshold(cost,kg):
    nonnegative(cost=cost,kg=kg)
    return cost/kg if kg else (0. if cost==0 else None)

def write(name,rows):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def source_comparison():
    sample=next(r for r in csv.DictReader((PARENT/'kinetic_source_v1_3/outputs/benchmark_summary.csv').read_text().splitlines()) if r['case']=='chain_on')
    t=float(sample['DD_T_birth_atoms']);he=float(sample['DD_n_birth_atoms'])
    result=[]
    for label,T,H,qt,qh,scope in [
      ('inherited_equal_branch_DD',1.,1.,4.03,3.27,'prescribed DD scenario convention; neither ARC nor laser prediction'),
      ('archived_WarpX_20keV_frozen_box',t,he,4.032653948,3.26891111,'actual 2ps collision sample; no laser drive, confinement or He3 secondary burn')]:
        J=(T*qt+H*qh)*MEV_J
        result.append(dict(source=label,T_branch_fraction=T/(T+H),He3_atoms_per_primary_DD_J=H/J,T_atoms_per_primary_DD_J=T/J,
          He3_gross_kg_per_primary_DD_GJ=H/J*HE3_KG_PER_ATOM*1e9,T_gross_kg_per_primary_DD_GJ=T/J*T_KG_PER_ATOM*1e9,
          reactor_annual_output_kg=None,scope=scope))
    write('source_comparison.csv',result)
    return result

def main():
    OUT.mkdir(exist_ok=True)
    source_hashes={}
    for f in json.loads((ROOT/'source_manifest.json').read_text()):
        raw=(PARENT/f['path']).read_bytes()
        blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if blob!=f['git_blob_sha1']:raise ValueError('source bytes differ from pinned Git input: '+f['path'])
        source_hashes[f['path']]=dict(git_blob_sha1=blob,sha256=hashlib.sha256(raw).hexdigest())
    (OUT/'source_sha256.json').write_text(json.dumps(source_hashes,indent=2)+'\n')
    policies=list(csv.DictReader((PARENT/'startup_year_v1_4_1/outputs/startup_policies.csv').read_text().splitlines()))
    energy_inputs=json.loads((PARENT/'wallplug_checkpoint_v1_5/inputs.json').read_text())
    inputs=json.loads((ROOT/'inputs.json').read_text())
    ledgers=[];allocations=[];frontiers=[];phase_rows=[];daily=[];checks=[]
    for case in ('A0','A1','A2'):
        policy=next(x for x in policies if x['case']==case and x['policy'].startswith('A continues'))
        pre=int(policy['refined_fuel_available_start_hours']);p=year.base(case);p['step_days']=1/96
        rows,summary=year.run(p,pre);last=rows[-1]
        for phase,start,end in [('A_only_startup',{},rows[pre-1]),('B_operating_year',rows[pre-1],last)]:
            diff=lambda k:end[k]-start.get(k,0.)
            ledgers.append(dict(A_case=case,phase=phase,hours=end['time_hours']-start.get('time_hours',0.),
               T_DD_gross_birth_kg=diff('dd_birth'),T_A_blanket_gross_birth_kg=diff('blanket_a_birth'),T_B_blanket_gross_birth_kg=diff('blanket_b_birth'),
               T_A_internal_burn_kg=diff('a_burn'),T_B_burn_kg=diff('b_burn'),T_decay_kg=diff('decay'),T_processing_loss_kg=diff('process_loss'),T_permeation_kg=diff('permeation'),
               T_A_to_B_transfer_kg=diff('a_to_b'),T_mobile_inventory_change_kg=end['total_inventory']-start.get('total_inventory',0.),
               He3_DD_gross_birth_kg=(diff('dd_events')-diff('dd_t_atoms'))*HE3_KG_PER_ATOM,He3_T_decay_gross_birth_kg=diff('decay')/T_KG_PER_ATOM*HE3_KG_PER_ATOM,
               qualified_T_surplus_kg=None,qualified_He3_surplus_kg=None))
        energy_totals=[]
        for q in energy_inputs:
            total_import=total_A=net=0.;prior={}
            for r in rows:
                e=year.wallplug.electricity(year.delta_input(r,prior,p),q)
                total_import+=e['imported_electric_kWh'];total_A+=e['A_laser_electric_J']/3.6e6;net+=e['net_electric_J'];prior=r
            energy_totals.append(dict(energy_case=q['case_id'],import_kWh=total_import,A_laser_input_kWh=total_A,net_electric_J=net))
        for hcase in inputs['helium_cases']:
            hs=helium(rows,hcase['collection_day'],hcase['capture_fraction']);h=hs[-1]
            if case=='A1' and hcase['case_id']=='capture90':
                daily=[dict(A_case=case,**r) for i,r in enumerate(hs) if (i+1)%24==0 or i==len(hs)-1]
            for reserve in inputs['terminal_T_reserve_kg']:
                a=terminal_allocation(last,h,reserve,inputs['retain_He3_fraction'],inputs['quality_acceptance'])
                aid=dict(A_case=case,He3_case=hcase['case_id'],reserve_T_kg=reserve)
                allocations.append(dict(**aid,**h,**a,realized_He3_revenue_USD=realized_revenue(a['He3_terminal_sale_candidate_kg'],None,None,None),realized_T_revenue_USD=None,
                  physical_validation=False,status='POTENTIAL-DERIVED terminal allocation; no sales during modeled year'))
                for e in energy_totals:
                    for price in inputs['assumed_import_prices_USD_per_kWh']:
                        cost=e['import_kWh']*price
                        frontiers.append(dict(**aid,energy_case=e['energy_case'],assumed_electricity_price_USD_per_kWh=price,
                          campus_import_charge_USD=cost,A_laser_only_input_charge_USD=e['A_laser_input_kWh']*price,
                          net_electric_GWh=e['net_electric_J']/3.6e12,
                          He3_only_required_USD_per_kg_full_sale=threshold(cost,a['He3_terminal_sale_candidate_kg']),
                          T_only_required_USD_per_kg_full_sale=threshold(cost,a['T_terminal_sale_candidate_kg']),
                          A_laser_only_He3_required_USD_per_kg_full_sale=threshold(e['A_laser_input_kWh']*price,a['He3_terminal_sale_candidate_kg']),
                          profit_USD=None,price_evidence='ASSUMED import price; isotope thresholds are algebra, not price forecasts'))
        checks.append(dict(A_case=case,startup_hours=pre,full_B_year_hours=8766,unserved_B_burn_kg=summary['b_unserved_burn_kg'],max_T_mass_residual_kg=summary['maximum_mass_residual_kg']))
        print(case,ledgers[-1],flush=True)
    write('isotope_birth_sink_ledger.csv',ledgers);write('terminal_allocations.csv',allocations);write('revenue_thresholds.csv',frontiers);write('He3_daily_reference.csv',daily)
    comparisons=source_comparison()
    (OUT/'checks.json').write_text(json.dumps(dict(cases=checks,physical_validation=False,all_physical_gates='OPEN',isotope_revenue_USD=None,profit_USD=None,
       ARC_vs_laser_yield_ratio=None,He3_D_burn='UNRESOLVED; omitted in candidate survival scenario',source_commit=SOURCE_COMMIT),indent=2)+'\n')
    print('rows',len(ledgers),len(allocations),len(frontiers),flush=True)
    print('He3 ratio at matched primary DD Q',comparisons[1]['He3_atoms_per_primary_DD_J']/comparisons[0]['He3_atoms_per_primary_DD_J'],flush=True)
    for r in frontiers:
        if r['A_case']=='A1' and r['He3_case']=='capture90' and r['reserve_T_kg']==10 and r['energy_case']=='gain10_eta0.2' and r['assumed_electricity_price_USD_per_kWh']==.1:print('REFERENCE',json.dumps(r),flush=True)
if __name__=='__main__':main()
