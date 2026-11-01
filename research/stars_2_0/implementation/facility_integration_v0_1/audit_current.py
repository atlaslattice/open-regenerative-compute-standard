"""Current facility boundary audit; earlier audits remain historical numerical checks."""
import argparse,json,hashlib
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--package',default=str(Path(__file__).resolve().parent));a=p.parse_args();root=Path(a.package);out=root/'pipeline_run004';checks=[]
def check(n,v):
 checks.append({'name':n,'passed':bool(v)})
 if not v:raise AssertionError(n)
r=json.loads((out/'integrated/RESULTS.json').read_text());receipt=json.loads((out/'integrated/RECEIPT.json').read_text());b=np.load(out/'integrated/PARTITION.npz');old=np.load(root/'pipeline_run002/integrated/PARTITION.npz')
check('all_21_integration_checks',all(c['passed'] for c in r['checks']));check('partition_hash',hashlib.sha256((out/'integrated/PARTITION.npz').read_bytes()).hexdigest()==receipt['partition_sha256']);check('particle_physics_unchanged_by_boundary_correction',b.files==old.files and all(np.array_equal(b[k],old[k]) for k in b.files))
check('alpha_budget',np.max(abs(b['alpha_birth_MeV']-sum(b[k] for k in ['material_lower_MeV','unresolved_MeV','circuit_MeV','terminal_heat_MeV','returned_MeV','bypass_MeV','marginal_MeV'])))<1e-10)
for row in r['results']:
 f=row['frontier'];name=row['source_model'];check(name+'_restricted_threshold_identity',abs(f['source_loss_uncredited_necessary_eta_for_nonnegative_net']*(f['beam_kinetic_input_J']+f['nuclear_release_J'])-f['beam_kinetic_input_J'])<1e-22);check(name+'_whole_cycle_energy_only_bound_Q',f['all_input_recovery_energy_only_net_upper_bound_J']==f['nuclear_release_J']);check(name+'_30_missing_inputs_not_zero',len(row['facility']['missing'])==30);check(name+'_no_apparatus_power_promotion',row['facility']['storage_neutral_net_W'] is None and r['actual_apparatus_net_power_W'] is None)
for stage in ['source_target','alpha']:
 s=json.loads((out/stage/'RESULTS.json').read_text());check(stage+'_checks_pass',all(x['passed'] for x in s['checks']))
check('fresh_source_and_bank_reproduce',all(json.loads((out/'FRESH_REPLAY_CHECK.json').read_text())[k] for k in ['saved_source_target_exact','alpha_scientific_exact_except_runtime','alpha_arrays_exact']))
(root/'AUDIT_CURRENT.json').write_text(json.dumps({'status':'PASS','checks_passed':len(checks),'checks':checks},indent=2)+'\n');print('current audit',len(checks),'PASS')
