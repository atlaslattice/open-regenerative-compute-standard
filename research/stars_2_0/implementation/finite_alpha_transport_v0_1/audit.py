"""Saved finite-geometry audit, including exact same-input replay."""
from pathlib import Path
import argparse,hashlib,json
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--package',default=str(Path(__file__).resolve().parent));a=p.parse_args();root=Path(a.package);checks=[]
def check(name,passed):
 checks.append({'name':name,'passed':bool(passed)})
 if not passed:raise AssertionError(name)
for run in ['run002','run003']:
 r=json.loads((root/run/'RESULTS.json').read_text());receipt=json.loads((root/run/'RECEIPT.json').read_text())
 check(run+'_reported_checks',all(x['passed'] for x in r['checks']))
 for ctrl in r['controls']:
  aspect=ctrl['aspect_ratio_width_to_normal_thickness'];f=root/run/('aspect_'+str(aspect)+'.npz');b=np.load(f);label=run+'_'+str(aspect)
  check(label+'_hash',hashlib.sha256(f.read_bytes()).hexdigest()==receipt['outputs_sha256'][f.name])
  mask=b['resolved_escape_mask'];resolved=b['resolved_exit_column_positions_atoms_cm2'];candidate=b['candidate_boundary_column_positions_atoms_cm2']
  check(label+'_unresolved_has_no_exit',np.isnan(resolved[~mask]).all())
  check(label+'_resolved_exit_matches_candidate',np.array_equal(resolved[mask],candidate[mask]))
  check(label+'_unresolved_escape_energy_zero_placeholder',np.all(b['escaped_energy_MeV'][~mask]==0))
  for row in ctrl['rows']:
   check(label+'_'+row['source']+'_count_budget',abs(row['alpha_birth_weight']-row['alpha_resolved_escape_weight']-row['alpha_unresolved_weight'])<1e-12)
   check(label+'_'+row['source']+'_energy_budget',abs(row['budget_residual_MeV'])<1e-10)
   check(label+'_'+row['source']+'_not_electricity',row['net_electricity_J'] is None and row['collector_electricity_J'] is None)
 # Exact faces may have multiple membership; face_code0 means an edge/corner, not unknown energy.
 check(run+'_app_is_blocked',r['original_pocket_gate']['status']=='BLOCKED_MISSING_APPARATUS_INPUTS')
x=json.loads((root/'run002/RESULTS.json').read_text());y=json.loads((root/'run003/RESULTS.json').read_text())
for r in [x,y]:r.pop('runtime_seconds')
check('same_input_scientific_json_exact',x==y)
for f in (root/'run002').glob('*.npz'):
 a=np.load(f);b=np.load(root/'run003'/f.name)
 check('same_input_arrays_'+f.name,a.files==b.files and all(np.array_equal(a[k],b[k],equal_nan=True) for k in a.files))
(root/'AUDIT.json').write_text(json.dumps({'status':'PASS','checks_passed':len(checks),'checks':checks},indent=2)+'\n');print('audit',len(checks),'PASS')
