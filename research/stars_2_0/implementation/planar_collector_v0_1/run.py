"""Conditional fixed-bank rear-port ideal-retarder accounting."""
import argparse,hashlib,json,sys,time
from pathlib import Path
import numpy as np
from collector import planar,apparatus_gate
p=argparse.ArgumentParser();p.add_argument('--models',required=True);p.add_argument('--out',required=True);a=p.parse_args();root=Path(a.models).resolve();package=Path(__file__).resolve().parent;out=Path(a.out).resolve();out.mkdir(exist_ok=False,parents=True);start=time.time()
for row in json.loads((package/'DEPENDENCY_LOCK.json').read_text()):
 if hashlib.sha256((root/row['path']).read_bytes()).hexdigest()!=row['sha256']:raise ValueError('dependency mismatch: '+row['path'])
bank=np.load(root/'alpha_birth_escape_v0_1/run003/EVENT_BANK.npz');source=json.loads((root/'alpha_birth_escape_v0_1/run003/RESULTS.json').read_text());weights=bank['conditional_event_weights'];mu=bank['alpha_LAB_four_vectors_MeV'][:,:,3]/np.linalg.norm(bank['alpha_LAB_four_vectors_MeV'][:,:,1:],axis=2);M=json.loads((root/'coupled_reference_v0_5/MASS_SOURCE.json').read_text())['alpha_MeV'];birth=bank['alpha_LAB_four_vectors_MeV'][:,:,0]-M
voltages=[-.25,0.,.1,.25,.5,1.,1.5,2.,3.,5.];results=[];checks=[]
for aspect in [2.,10.,100.,1e6]:
 path=root/'finite_alpha_transport_v0_1/run002'/('aspect_'+str(aspect)+'.npz');b=np.load(path);mask=b['resolved_escape_mask'];rear=mask&(b['geometric_boundary_face_codes']==1);bypass=mask&(~rear);Tin=b['escaped_energy_MeV'];unresolved=b['unresolved_energy_MeV'];material=b['material_transfer_lower_MeV']
 if np.any(mu[rear]<=0):raise ValueError('rear port direction inconsistent')
 for V,charge,kind in [(V,2.,'HYPOTHETICAL_HE2_PLUS') for V in voltages]+[(5.,0.,'ZERO_CHARGE_FORCE_NULL_NOT_NEUTRAL_HELIUM')]:
  work=np.zeros_like(Tin);heat=np.zeros_like(Tin);returned=np.zeros_like(Tin);deferred=np.zeros_like(Tin);collected=np.zeros_like(mask);reflected=np.zeros_like(mask);marginal=np.zeros_like(mask);naive_wrong=np.zeros_like(mask)
  for i,j in zip(*np.nonzero(rear)):
   r=planar(float(Tin[i,j]),float(mu[i,j]),charge,V,M);work[i,j]=r['circuit_work_MeV'];heat[i,j]=r['electrode_heat_MeV'];returned[i,j]=r['returned_kinetic_MeV'];deferred[i,j]=r['deferred_kinetic_MeV'];collected[i,j]=r['status']=='COLLECTED_IDEAL_PLANE';reflected[i,j]=r['status']=='REFLECTED_AND_RETURNED';marginal[i,j]=r['status']=='MARGINAL_NOT_COLLECTED';naive_wrong[i,j]=r['status']=='REFLECTED_AND_RETURNED' and Tin[i,j]>r['barrier_MeV']
  checks.append({'name':str((aspect,V,charge))+'_each_alpha_energy_ledger','passed':bool(np.max(abs(birth-material-unresolved-work-heat-returned-deferred-Tin*bypass))<1e-10)})
  checks.append({'name':str((aspect,V,charge))+'_each_alpha_status_partition','passed':bool(np.all((~mask).astype(int)+bypass+collected+reflected+marginal==1))})
  rows=[]
  for k,name in enumerate(source['source_cases']):
   w=weights[:,k,None];weighted=lambda x:float(np.sum(w*x))
   rows.append({'source':name,'expected_reactions':float(weights[:,k].sum()),'birth_kinetic_MeV':weighted(birth),'resolved_escape_kinetic_MeV':weighted(Tin),'material_transfer_lower_MeV':weighted(material),'upstream_unresolved_kinetic_MeV':weighted(unresolved),'ideal_circuit_transfer_MeV':weighted(work),'ideal_electrode_heat_MeV':weighted(heat),'returned_kinetic_MeV':weighted(returned),'bypass_kinetic_MeV':weighted(Tin*bypass),'marginal_deferred_kinetic_MeV':weighted(deferred),'collected_alpha_weight':weighted(collected),'reflected_alpha_weight':weighted(reflected),'bypassed_alpha_weight':weighted(bypass),'unresolved_alpha_weight':weighted(~mask),'marginal_alpha_weight':weighted(marginal),'wrongly_accepted_by_total_energy_test_alpha_weight':weighted(naive_wrong),'apparatus_recovered_electricity_J':None,'facility_net_electricity_J':None})
  results.append({'aspect_ratio':aspect,'bias_MV':V,'charge_e':charge,'charge_grade':kind,'rows':rows})
checks.append({'name':'no_force_null_has_no_circuit_work','passed':all(abs(row['ideal_circuit_transfer_MeV'])<1e-15 for c in results if c['charge_e']==0 for row in c['rows'])})
checks.append({'name':'zero_bias_has_no_circuit_work','passed':all(abs(row['ideal_circuit_transfer_MeV'])<1e-15 for c in results if c['bias_MV']==0 for row in c['rows'])})
checks.append({'name':'negative_bias_debits_circuit','passed':all(row['ideal_circuit_transfer_MeV']<0 for c in results if c['bias_MV']<0 for row in c['rows'])})
report={'status':'IDEAL_PLANAR_REAR_PORT_CONDITIONAL_CONTROL_NOT_HARDWARE_PREDICTION','controls':results,'checks':checks,'apparatus_gate':apparatus_gate(),'physical_time_s':None,'current_A':None,'electrical_power_W':None,'physical_uncertainty':'NOT_PROPAGATED; unknown charge state, finite geometry, source conventions, space charge, circuit and material properties','runtime_s':time.time()-start}
(out/'RESULTS.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n');(out/'RECEIPT.json').write_text(json.dumps({'python':sys.version,'numpy':np.__version__,'code_sha256':{n:hashlib.sha256((package/n).read_bytes()).hexdigest() for n in ['run.py','collector.py']}},indent=2)+'\n');print('checks',sum(x['passed'] for x in checks),'/',len(checks));assert all(x['passed'] for x in checks)
