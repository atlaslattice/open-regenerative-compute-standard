"""Audit saved summaries and numerical trajectory receipts; no solver execution."""
import json,argparse
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--package',default=str(Path(__file__).resolve().parent));a=p.parse_args();root=Path(a.package);checks=[]
def check(name,passed):
 checks.append({'name':name,'passed':bool(passed)})
 if not passed:raise AssertionError(name)
for run in ['run001','run002']:
 r=json.loads((root/run/'RESULTS.json').read_text());check(run+'_checks_pass',all(c['passed'] for c in r['checks']))
 for idx,c in enumerate(r['controls']):
  for row in c['rows']:
   pre=run+'_'+str(idx)+'_'+row['source'];total=sum(row[k] for k in ['material_transfer_lower_MeV','upstream_unresolved_kinetic_MeV','ideal_circuit_transfer_MeV','ideal_electrode_heat_MeV','returned_kinetic_MeV','bypass_kinetic_MeV','marginal_deferred_kinetic_MeV']);check(pre+'_energy',abs(total-row['birth_kinetic_MeV'])<1e-10)
   count=sum(row[k] for k in ['collected_alpha_weight','reflected_alpha_weight','bypassed_alpha_weight','unresolved_alpha_weight','marginal_alpha_weight']);check(pre+'_count',abs(count-3*row['expected_reactions'])<1e-12)
 x=r.copy();x.pop('runtime_s')
 if run=='run001':first=x
 else:check('bank_scientific_replay_exact',first==x)
for run in ['warpx_run002','warpx_run003']:
 r=json.loads((root/run/'RESULTS.json').read_text());check(run+'_checks_pass',all(c['passed'] for c in r['checks']))
 for row in r['results']:
  f=root/run/row['case']/'diags/reducedfiles/number.txt';n=np.loadtxt(f);check(run+'_'+row['case']+'_particle_and_weight_retained',np.all(n[:,2:]==1.))
 for row in r['results']:row.pop('runtime_s')
 if run=='warpx_run002':original=r
 else:check('warpx_summary_replay_exact',r==original)
for label in [r['case'] for r in original['results']]:
 for name in ['extrema','number']:
  a=root/'warpx_run002'/label/'diags/reducedfiles'/(name+'.txt');b=root/'warpx_run003'/label/'diags/reducedfiles'/(name+'.txt');check(label+'_'+name+'_raw_replay_exact',a.read_bytes()==b.read_bytes())
(root/'AUDIT.json').write_text(json.dumps({'status':'PASS','checks_passed':len(checks),'checks':checks},indent=2)+'\n');print(len(checks),'audit checks PASS')
