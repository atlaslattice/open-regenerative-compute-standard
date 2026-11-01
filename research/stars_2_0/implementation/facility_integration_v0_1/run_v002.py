"""One-command fixed-source replay → finite alpha escape → planar collector → facility bounds."""
import argparse,hashlib,json,sys,platform
from pathlib import Path
import numpy as np
from accounting_v002 import energy_frontier,conditional_facility
p=argparse.ArgumentParser();p.add_argument('--models',required=True);p.add_argument('--profile',required=True);p.add_argument('--out',required=True);a=p.parse_args();root=Path(a.models).resolve();package=Path(__file__).resolve().parent;out=Path(a.out).resolve();out.mkdir(parents=True,exist_ok=False);profile=json.loads(Path(a.profile).read_text())
if profile['run_class']!='INTEGRATED_CONDITIONAL_INTERFACE_CONTROL_NOT_PHYSICAL_APPARATUS':raise ValueError('unqualified physical-apparatus run rejected')
for row in json.loads((package/'DEPENDENCY_LOCK.json').read_text()):
 if hashlib.sha256((root/row['path']).read_bytes()).hexdigest()!=row['sha256']:raise ValueError('dependency mismatch: '+row['path'])
sys.path.insert(0,str(root/'finite_alpha_transport_v0_1'));from geometry import exit_box,energy_through_column
sys.path.insert(0,str(root/'planar_collector_v0_1'));from collector import planar
sys.path.insert(0,str(root/'particle_handoff_v0_1'));from handoff import Engine
engine=Engine();physics=engine.p;model,tables=physics.load_model();floor=model.PROJECTILES['alpha'][1]/1000
fn=lambda E:model.stopping(tables,model='srim13',projectile='alpha',material='B11',E_MeV=E,bn_electronic_multiplier=None,nuclear_variant='ZBL_SIMNRA_7_04')['total_eV_cm2_per_average_atom'];coordinate=physics.Coordinate(fn,floor,12.,steps=16384)
receiver=json.loads((root/'warpx_target_handoff_v0_2/run001/RESULTS.json').read_text());case=next(x for x in receiver['results'] if x['case']=='field_on');fixture=json.loads((root/'warpx_target_handoff_v0_2/run001/FIXTURE.json').read_text());beam=fixture['kinetic_MeV']*sum(fixture['weights']);N=case['target']['normal_atoms_cm2'];u=np.array(case['receiver']['stage_records'][0]['input']['unit_direction_LAB'])
bank=np.load(root/'alpha_birth_escape_v0_1/run003/EVENT_BANK.npz');source=json.loads((root/'alpha_birth_escape_v0_1/run003/RESULTS.json').read_text());lab=bank['alpha_LAB_four_vectors_MeV'];M=json.loads((root/'coupled_reference_v0_5/MASS_SOURCE.json').read_text())['alpha_MeV'];T=lab[:,:,0]-M;directions=lab[:,:,1:]/np.linalg.norm(lab[:,:,1:],axis=2)[:,:,None];depth=bank['normal_depth_atoms_cm2'];positions=np.column_stack([depth*u[0]/u[2],depth*u[1]/u[2],depth]);aspect=profile['finite_box_width_over_normal_thickness'];bias=profile['ideal_rear_collector_bias_MV'];charge=profile['hypothetical_exit_charge_e']
if isinstance(aspect,bool) or not isinstance(aspect,(int,float)) or not np.isfinite(aspect) or aspect<2 or aspect>1e6:raise ValueError('supported finite-box control aspect required')
if bias<0 or charge!=2:raise ValueError('this integration lane uses positive-bias hypothetical He2+ controls only')
lo=[-aspect*N/2,-aspect*N/2,0.];hi=[aspect*N/2,aspect*N/2,N];escape=np.zeros_like(T);mat=np.zeros_like(T);tail=np.zeros_like(T);circuit=np.zeros_like(T);heat=np.zeros_like(T);returned=np.zeros_like(T);bypass=np.zeros_like(T);deferred=np.zeros_like(T)
for i in range(len(lab)):
 for j in range(3):
  hit=exit_box(positions[i],directions[i,j],lo,hi);tr=energy_through_column(float(T[i,j]),hit['path_column_atoms_cm2'],coordinate);mat[i,j]=tr['material_lower'];tail[i,j]=tr['unresolved_E']
  if tr['escaped_E'] is None:continue
  escape[i,j]=tr['escaped_E']
  if hit['faces']!=['Z+']:bypass[i,j]=escape[i,j];continue
  r=planar(float(escape[i,j]),float(directions[i,j,2]),charge,bias,M);circuit[i,j]=r['circuit_work_MeV'];heat[i,j]=r['electrode_heat_MeV'];returned[i,j]=r['returned_kinetic_MeV'];deferred[i,j]=r['deferred_kinetic_MeV']
checks=[{'name':'per_alpha_budget','passed':bool(np.max(abs(T-mat-tail-circuit-heat-returned-bypass-deferred))<1e-10)}];results=[];MEV_J=1.602176634e-13
prior=json.loads((root/'planar_collector_v0_1/run001/RESULTS.json').read_text());match=next((x for x in prior['controls'] if x['aspect_ratio']==aspect and x['bias_MV']==bias and x['charge_e']==charge),None)
for k,name in enumerate(source['source_cases']):
 w=bank['conditional_event_weights'][:,k,None];ws=lambda x:float(np.sum(w*x));R=float(bank['conditional_event_weights'][:,k].sum());born=ws(T);D=ws(circuit)
 frontier=energy_frontier(beam*MEV_J,case['Q_MeV']*MEV_J,born*MEV_J,D*MEV_J);facility=conditional_facility(frontier,profile['facility'])
 # These are dimensionless mathematical probes, not measured device efficiencies.
 probes=[{'wall_to_beam_efficiency_probe':eta,'all_energy_ideal_net_upper_bound_J':beam*MEV_J+case['Q_MeV']*MEV_J-beam*MEV_J/eta,'probe_role':'NUMERICAL_BOUND_EVALUATION_NOT_APPARATUS_PARAMETER'} for eta in [1.,.5,.1]]
 row={'source_model':name,'expected_reactions':R,'alpha_birth_MeV':born,'alpha_resolved_escape_MeV':ws(escape),'ideal_alpha_circuit_MeV':D,'alpha_energy_partition_MeV':{'material_lower':ws(mat),'unresolved_tail':ws(tail),'terminal_heat':ws(heat),'returned':ws(returned),'bypass':ws(bypass),'marginal_deferred':ws(deferred)},'frontier':frontier,'facility':facility,'optimistic_bound_probes':probes};results.append(row)
 checks.extend([{'name':name+'_fixed_event_count','passed':abs(R-case['expected_reactions'])<1e-12},{'name':name+'_birth_matches_receiver','passed':abs(born-case['alpha_birth_kinetic_MeV'])<1e-10},{'name':name+'_saved_collector_reproduced','passed':match is None or abs(D-match['rows'][k]['ideal_circuit_transfer_MeV'])<1e-12},{'name':name+'_all_energy_partition','passed':abs((beam+case['Q_MeV'])-(frontier['non_alpha_energy_by_conservation_J']/MEV_J+born))<1e-8}])
report={'status':'EXECUTED_INTEGRATED_CONTROL_FACILITY_PREDICTION_INCOMPLETE','profile_id':profile['profile_id'],'architecture_parent':profile['architecture_parent'],'scope':profile['run_class'],'source_beam_kinetic_MeV':beam,'source_particle_weight':sum(fixture['weights']),'source_expected_reactions':case['expected_reactions'],'results':results,'checks':checks,'actual_apparatus_net_power_W':None,'physical_geometry_closure':'OPEN: finite alpha box in column coordinates is not embedded in the source PIC SI geometry; original pocket and real collector not recovered','storage_sign':'storage_neutral_net = load - wall + (U_end-U_start); discharging storage is not nuclear gain','new_source_or_full_hybrid_simulation':False}
(out/'INPUT.json').write_text(json.dumps(profile,indent=2)+'\n');(out/'RESULTS.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n');np.savez_compressed(out/'PARTITION.npz',alpha_birth_MeV=T,alpha_escape_MeV=escape,material_lower_MeV=mat,unresolved_MeV=tail,circuit_MeV=circuit,terminal_heat_MeV=heat,returned_MeV=returned,bypass_MeV=bypass,marginal_MeV=deferred)
(out/'RECEIPT.json').write_text(json.dumps({'python':platform.python_version(),'numpy':np.__version__,'code_sha256':{n:hashlib.sha256((package/n).read_bytes()).hexdigest() for n in [Path(__file__).name,'accounting_v002.py']},'partition_sha256':hashlib.sha256((out/'PARTITION.npz').read_bytes()).hexdigest(),'profile_sha256':hashlib.sha256(Path(a.profile).read_bytes()).hexdigest()},indent=2)+'\n');print('checks',sum(x['passed'] for x in checks),'/',len(checks));assert all(x['passed'] for x in checks)
