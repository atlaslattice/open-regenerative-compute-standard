"""Audit integrated partitions and replay; no external solver invocation."""
import argparse,json,hashlib
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--package',default=str(Path(__file__).resolve().parent));a=p.parse_args();root=Path(a.package);checks=[]
def check(name,ok):
 checks.append({'name':name,'passed':bool(ok)})
 if not ok:raise AssertionError(name)
for run in ['run001','run002','run003','pipeline_run001/integrated','pipeline_run002/integrated']:
 r=json.loads((root/run/'RESULTS.json').read_text());receipt=json.loads((root/run/'RECEIPT.json').read_text());b=np.load(root/run/'PARTITION.npz')
 check(run+'_checks_pass',all(c['passed'] for c in r['checks']));check(run+'_partition_hash',hashlib.sha256((root/run/'PARTITION.npz').read_bytes()).hexdigest()==receipt['partition_sha256'])
 total=sum(b[k] for k in ['material_lower_MeV','unresolved_MeV','circuit_MeV','terminal_heat_MeV','returned_MeV','bypass_MeV','marginal_MeV']);check(run+'_per_alpha_partition',np.max(abs(b['alpha_birth_MeV']-total))<1e-10)
 for row in r['results']:
  f=row['frontier'];check(run+'_'+row['source_model']+'_no_actual_net_claim',r['actual_apparatus_net_power_W'] is None and row['facility']['storage_neutral_net_W'] is None)
  eta=f['necessary_wall_to_beam_efficiency_for_nonnegative_net_optimistic'];check(run+'_'+row['source_model']+'_threshold_reconstruction',abs(f['maximum_all_energy_output_J']-f['beam_kinetic_input_J']/eta)<1e-22)
  check(run+'_'+row['source_model']+'_unknown_loads_remain_unknown',len(row['facility']['missing'])==20)
x=json.loads((root/'run002/RESULTS.json').read_text());y=json.loads((root/'run003/RESULTS.json').read_text());check('integrated_same_code_replay_json_exact',x==y)
a=np.load(root/'run002/PARTITION.npz');b=np.load(root/'run003/PARTITION.npz');check('integrated_same_code_replay_arrays_exact',a.files==b.files and all(np.array_equal(a[k],b[k]) for k in a.files))
fresh=json.loads((root/'pipeline_run001/integrated/RESULTS.json').read_text());fresh.pop('input_artifact_sha256');check('fresh_chain_matches_saved_input_integration',fresh==y)
second=json.loads((root/'pipeline_run002/integrated/RESULTS.json').read_text());check('fresh_pipeline_replay_exact',second==json.loads((root/'pipeline_run001/integrated/RESULTS.json').read_text()))
(root/'AUDIT.json').write_text(json.dumps({'status':'PASS','checks_passed':len(checks),'checks':checks},indent=2)+'\n');print('audit',len(checks),'PASS')
