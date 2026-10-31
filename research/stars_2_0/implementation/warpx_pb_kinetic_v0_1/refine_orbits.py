"""Refine failed mirror phase-accuracy cases without relaxing the original 2% check."""
import json,subprocess,os,time
from pathlib import Path
root=Path(__file__).resolve().parent
cases=json.loads((root/'ORBIT_CASES_v002.json').read_text())
extras=[]
for stem in ['mirror_losscone','mirror_reflect']:
 cfg=next(c for c in cases if c['case']==stem).copy();name=stem+'_fine'
 cfg.update(case=name,dt_s=5e-11,steps=24000)
 s=(root/'inputs_v002'/stem).read_text().replace('max_step = 6000','max_step = 24000').replace('warpx.const_dt = 2e-10','warpx.const_dt = 5e-11')
 with (root/'inputs_v002'/name).open('x') as f:f.write(s)
 out=root/'receipts'/(name+'002');out.mkdir(exist_ok=False)
 t=time.time()
 with (out/'RUN.log').open('x') as f:
  r=subprocess.run([str(root.parent/'warpx_runtime_v0_1/env/bin/warpx.3d'),str(root/'inputs_v002'/name)],cwd=out,env={**os.environ,'OMP_NUM_THREADS':'2'},stdout=f,stderr=subprocess.STDOUT)
 cfg.update(returncode=r.returncode,runtime_s=time.time()-t)
 assert r.returncode==0
 print(name,r.returncode,flush=True);extras.append(cfg)
with (root/'ORBIT_CASES_v003.json').open('x') as f:json.dump(cases+extras,f,indent=2);f.write('\n')
