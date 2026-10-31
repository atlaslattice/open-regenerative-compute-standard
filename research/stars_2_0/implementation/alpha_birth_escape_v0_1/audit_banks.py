"""Audit saved banks without the Coulomb backend or a new PIC execution."""
import argparse,json,hashlib
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--package',default=str(Path(__file__).resolve().parent));a=p.parse_args();root=Path(a.package)
identity=json.loads((root/'INPUT_IDENTITY.json').read_text());MA=identity['masses']['alpha_MeV']
checks=[]
def check(name,value):
 checks.append({'name':name,'passed':bool(value)})
 if not value:raise AssertionError(name)
for run in ['run001','run002','run003','run004']:
 r=json.loads((root/run/'RESULTS.json').read_text());receipt=json.loads((root/run/'RECEIPT.json').read_text());b=np.load(root/run/'EVENT_BANK.npz')
 check(run+'_bank_hash',hashlib.sha256((root/run/'EVENT_BANK.npz').read_bytes()).hexdigest()==receipt['event_bank_sha256'])
 check(run+'_finite_arrays',all(np.isfinite(b[k]).all() for k in b.files))
 check(run+'_weights_nonnegative',np.all(b['conditional_event_weights']>=0))
 check(run+'_energy_budget',np.max(np.abs((b['alpha_LAB_four_vectors_MeV'][:,:,0]-MA)-b['escaped_energy_MeV']-b['material_transfer_lower_MeV']-b['unresolved_energy_MeV']))<1e-10)
 for idx,row in enumerate(r['results']):
  w=b['conditional_event_weights'][:,idx,None]
  for key,arr in [('resolved_escape_kinetic_MeV','escaped_energy_MeV'),('material_transfer_lower_MeV','material_transfer_lower_MeV'),('unresolved_kinetic_budget_MeV','unresolved_energy_MeV')]:
   check(run+'_'+row['source']+'_'+key,abs(np.sum(w*b[arr])-row[key])<1e-13)
# Compare content, not ZIP timestamps or elapsed runtime.
r2=json.loads((root/'run002/RESULTS.json').read_text());r4=json.loads((root/'run004/RESULTS.json').read_text())
for r in [r2,r4]:r.pop('runtime_seconds')
check('same_seed_scientific_json_exact',r2==r4)
b2=np.load(root/'run002/EVENT_BANK.npz');b4=np.load(root/'run004/EVENT_BANK.npz')
check('same_seed_all_arrays_exact',b2.files==b4.files and all(np.array_equal(b2[k],b4[k]) for k in b2.files))
r3=json.loads((root/'run003/RESULTS.json').read_text());comparison=[]
for x,y in zip(r2['results'],r3['results']):
 comparison.append({'source':x['source'],'escape_run002_MeV':x['resolved_escape_kinetic_MeV'],'escape_run003_MeV':y['resolved_escape_kinetic_MeV'],'relative_difference':(y['resolved_escape_kinetic_MeV']-x['resolved_escape_kinetic_MeV'])/x['resolved_escape_kinetic_MeV']})
result={'status':'PASS','checks':checks,'checks_passed':len(checks),'seed_and_sample_sensitivity':comparison,'interpretation':'Different seed AND doubled sample count: sensitivity diagnostic, not isolated convergence rate or confidence interval. No source ranking established.'}
(root/'BANK_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n');print('bank checks',len(checks),'PASS')
