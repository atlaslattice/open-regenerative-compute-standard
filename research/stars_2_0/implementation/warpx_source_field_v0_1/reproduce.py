"""Reproduce in a NEW work tree; recorded receipt paths are never overwritten."""
import argparse,os,shutil,subprocess,json
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--runtime',required=True);p.add_argument('--out',required=True);a=p.parse_args()
source=Path(__file__).resolve().parent;out=Path(a.out).resolve();out.mkdir(parents=True,exist_ok=False)
for f in source.glob('*.py'):
 if f.name!='reproduce.py':shutil.copyfile(f,out/f.name)
shutil.copytree(source/'upstream',out/'upstream');shutil.copyfile(source/'SOURCE_INDEX.json',out/'SOURCE_INDEX.json')
# Reuse the hash-pinned cached source if present; otherwise fetch the same pinned blob.
if (source/'example-femm-3d.original.h5').exists():shutil.copyfile(source/'example-femm-3d.original.h5',out/'example-femm-3d.original.h5')
runtime=Path(a.runtime).resolve();env={**os.environ,'STELLAR_WARPX_ENV':str(runtime),'OMP_NUM_THREADS':'2'}
stages=[]
commands=[]
if not (out/'example-femm-3d.original.h5').exists():commands.append(['fetch_dataset.py'])
commands += [['verify_sources.py'],['prepare_maps.py'],['run_collisions.py'],['run_maps.py'],['run_adapter_fixture.py'],['analyze_maps_v002.py'],['-m','unittest','test_admission','-v']]
for i,cmd in enumerate(commands):
 with (out/f'REPRO_STAGE_{i}.log').open('x') as f:r=subprocess.run([str(runtime/'bin/python'),*cmd],cwd=out,env=env,stdout=f,stderr=subprocess.STDOUT)
 stages.append({'command':cmd,'returncode':r.returncode})
 print(cmd,r.returncode,flush=True)
 if r.returncode:break
(out/'REPRODUCTION.json').write_text(json.dumps({'runtime':str(runtime),'stages':stages},indent=2)+'\n')
assert len(stages)==len(commands) and all(s['returncode']==0 for s in stages)
