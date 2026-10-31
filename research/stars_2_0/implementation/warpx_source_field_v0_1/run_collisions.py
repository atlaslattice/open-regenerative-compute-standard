"""Unchanged upstream collision operator verification, not pB apparatus calibration."""
import os,json,subprocess,time
from pathlib import Path
root=Path(__file__).resolve().parent
runtime=Path(os.environ.get('STELLAR_WARPX_ENV',str(root.parent/'warpx_runtime_v0_1/env')))/'bin'
cases=[('conservation','inputs_test_1d_collision_z_correct_conservation','analysis_collision_1d_correct_conservation.py',['diags/diag1000000','diags/diag1000010']),('relaxation','inputs_test_1d_collision_z','analysis_collision_1d.py',['diags/diag1000600'])]
results=[]
for name,inp,analysis,args in cases:
 out=root/'receipts'/name;out.mkdir(parents=True,exist_ok=False)
 fixture=root/'upstream/warpx/Examples/Tests/collision'
 steps=[]
 for label,cmd in [('RUN',[str(runtime/'warpx.1d'),str(fixture/inp)]),('ANALYSIS',[str(runtime/'python'),str(fixture/analysis),*args])]:
  start=time.time()
  with (out/(label+'.log')).open('x') as f:r=subprocess.run(cmd,cwd=out,env={**os.environ,'OMP_NUM_THREADS':'2'},stdout=f,stderr=subprocess.STDOUT)
  steps.append(dict(stage=label,returncode=r.returncode,elapsed_s=time.time()-start))
  if r.returncode:break
 results.append(dict(case=name,steps=steps))
 print(name,steps,flush=True)
(root/'receipts/COLLISION_RECEIPT.json').write_text(json.dumps(results,indent=2)+'\n')
assert all(len(c['steps'])==2 and all(s['returncode']==0 for s in c['steps']) for c in results)
