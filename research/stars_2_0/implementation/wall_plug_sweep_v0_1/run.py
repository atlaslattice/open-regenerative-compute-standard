"""Conditional wall-plug sweep of the pinned PR64 cold single-pass control.
No new PIC run, apparatus calibration, or sustained-burn calculation.
"""
import argparse, copy, csv, hashlib, importlib.util, itertools, json, math, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
PARENT=ROOT.parent/'facility_integration_v0_1'
SPEC=importlib.util.spec_from_file_location('pinned_accounting',PARENT/'accounting_v004.py')
ACCOUNT=importlib.util.module_from_spec(SPEC);SPEC.loader.exec_module(ACCOUNT)

def control():
    saved=json.loads((PARENT/'pipeline_run004/integrated/RESULTS.json').read_text())
    source=next(x for x in saved['results'] if x['source_model']=='COHERENT_L1_L3_RAW')['frontier']
    factor=1/source['beam_kinetic_input_J']
    frontier=ACCOUNT.energy_frontier(1.,source['nuclear_release_J']*factor,source['alpha_birth_kinetic_J']*factor,source['ideal_alpha_circuit_J']*factor)
    profile=json.loads((PARENT/'PROFILE_v003.json').read_text())['facility']
    return frontier,profile

def scenario(eta_laser,eta_beam,source_refund,downstream,rate=1.,fired=1.,hold_W=0.,coil_optical_J=0.,coil_eta=.1):
    for v,n in [(hold_W,'containment hold power'),(coil_optical_J,'coil laser optical energy')]: ACCOUNT.nonnegative(v,n)
    ACCOUNT.fraction(coil_eta,'coil wall-to-optical efficiency',True)
    if hold_W and coil_optical_J: raise ValueError('choose explicit containment alternative')
    frontier,f=control(); f=copy.deepcopy(f)
    f.update(wall_to_beam_fraction=None,wall_to_laser_fraction=eta_laser,laser_to_beam_fraction=eta_beam,
             fired_fraction_per_attempt=fired,attempt_rate_Hz=rate,other_alpha_electric_recovery_fraction=downstream,
             non_alpha_electric_recovery_fraction=downstream,source_conversion_loss_electric_recovery_fraction=source_refund,
             source_driver_idle_preparation_wall_J_per_attempt=0.,source_idle_loss_electric_recovery_fraction=0.,stored_energy_change_J_per_attempt=0.)
    # All original loads are explicitly excluded in this FAVORABLE scenario except
    # the separately supplied containment budget. These are not measured zeros.
    for l in f['loads']: l.update(wall_J_per_attempt=0.,wall_J_per_fired=0.,own_wall_loss_electric_recovery_fraction=0.)
    if rate<=0: raise ValueError('positive attempt rate required for fixed-power budget')
    magnet=next(l for l in f['loads'] if l['physical_instance_id']=='magnet_supply')
    magnet.update(wall_J_per_attempt=hold_W/rate,wall_J_per_fired=coil_optical_J/coil_eta)
    result=ACCOUNT.conditional_facility(frontier,f)
    if result['missing']: raise RuntimeError(result['missing'])
    laser_optical=1./eta_beam; laser_wall=laser_optical/eta_laser
    q=frontier['nuclear_release_J']; remainder=laser_wall-1.
    containment_per_fired=None if fired==0 else hold_W/(rate*fired)+coil_optical_J/coil_eta
    required_refund=None if remainder==0 or containment_per_fired is None else 1.+(containment_per_fired-q)/remainder
    return dict(beam_J_per_fired=1.,wall_to_laser=eta_laser,laser_to_proton=eta_beam,
                laser_optical_J_per_fired=laser_optical,main_laser_wall_J_per_fired=laser_wall,
                main_driver_conversion_remainder_J=laser_wall-1.,source_remainder_electric_refund=source_refund,
                remaining_downstream_recovery=downstream,attempt_rate_Hz=rate,fired_fraction=fired,
                containment_hold_W=hold_W,coil_optical_J_per_fired=coil_optical_J,coil_wall_to_laser=coil_eta,
                containment_wall_J_per_fired=coil_optical_J/coil_eta,nuclear_J_per_fired=q,
                nuclear_W=rate*fired*q,
                gross_wall_W=rate*result['wall_electric_J_per_attempt'],
                output_electric_W=rate*result['output_electric_J_per_attempt'],
                net_electric_W=result['storage_neutral_net_W'],
                required_source_remainder_refund_if_downstream_perfect=required_refund,
                required_refund_scope='Includes selected containment budget; excludes other loads; values above1 are impossible refunds.',
                scenario_evidence='CONDITIONAL_NOT_CALIBRATED',
                source_refund_one_is_formal_bound_only=(source_refund==1.),
                excluded_loads_are_not_measured_zero=True)

def main():
    p=argparse.ArgumentParser();p.add_argument('--out',required=True);a=p.parse_args()
    out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
    rows=[scenario(*x) for x in itertools.product([.01,.05,.1,.2],[.01,.1,.15],[0.,.3,1.],[0.,.4,1.])]
    ops=[]
    for rate,fired in itertools.product([.1,1.,10.],[.5,.9,1.]):
        for hold,coil in [(0.,0.),(1000.,0.),(10000.,0.),(0.,500.)]:
            # Perfect downstream energy return is a favorable mathematical case.
            ops.append(scenario(.1,.1,0.,1.,rate,fired,hold,coil,.1))
    for name,data in [('EFFICIENCY_SWEEP.csv',rows),('OPERATIONS_SWEEP.csv',ops)]:
        with (out/name).open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
    no_refund=[r for r in rows if r['source_remainder_electric_refund']==0]
    sample=scenario(.1,.1,0.,1.)
    coil=scenario(.1,.1,0.,1.,coil_optical_J=500.,coil_eta=.1)
    hold=scenario(.1,.1,0.,1.,hold_W=1000.)
    summary={'status':'EXECUTED_CONDITIONAL_WALL_PLUG_SWEEP_NOT_NEW_PHYSICS','efficiency_rows':len(rows),'operations_rows':len(ops),
             'nuclear_J_per_beam_J':sample['nuclear_J_per_fired'],'source_remainder_uncredited_positive_cases':sum(r['net_electric_W']>0 for r in no_refund),
             'source_remainder_uncredited_cases':len(no_refund),'main_laser_wall_J_per_beam_J_range':[min(r['main_laser_wall_J_per_fired'] for r in rows),max(r['main_laser_wall_J_per_fired'] for r in rows)],
             'favorable_10percent_10percent_no_aux':sample,'separate_500J_optical_coil_case':coil,'continuous_1kW_containment_budget_case':hold,
             'physical_apparatus_net_W':None,'warning':'Every efficiency, repetition rate, recovery and load in these sweeps is a conditional scenario, not calibrated STARS hardware. Perfect recovery is energy-only, not thermodynamic feasibility. Linear normalization preserves the inherited control; no plasma or geometry extrapolation is solved.'}
    (out/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
    inputs=[PARENT/'accounting_v004.py',PARENT/'PROFILE_v003.json',PARENT/'pipeline_run004/integrated/RESULTS.json',ROOT/'run.py']
    receipt={'python':sys.version,'input_sha256':{str(f.relative_to(ROOT.parent)):hashlib.sha256(f.read_bytes()).hexdigest() for f in inputs},'output_sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in sorted(out.iterdir()) if f.is_file()},'fresh_PIC_executed':False,'parent_commit':'604158962fada3c5605339ce67539432ec94b2a7'}
    (out/'RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__': main()
