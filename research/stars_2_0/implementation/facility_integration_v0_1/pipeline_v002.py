"""Execute fresh source PIC, receiving target, coherent alpha bank and facility control.
Requires restored dependencies. All stages are recorded; no scientific freeze.
"""
import argparse,hashlib,json,os,subprocess,sys,time
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--models',required=True);p.add_argument('--runtime',required=True);p.add_argument('--map',required=True);p.add_argument('--profile',required=True);p.add_argument('--out',required=True);a=p.parse_args();models=Path(a.models).resolve();runtime=Path(a.runtime).resolve();field=Path(a.map).resolve();profile=Path(a.profile).resolve();out=Path(a.out).resolve();out.mkdir(parents=True,exist_ok=False);package=Path(__file__).resolve().parent;stages=[]
def run(stage,args):
 with (out/(stage+'.log')).open('x') as f:
  start=time.time();r=subprocess.run(args,stdout=f,stderr=subprocess.STDOUT,env={**os.environ,'OMP_NUM_THREADS':'2'})
 stages.append({'stage':stage,'command':args,'returncode':r.returncode,'elapsed_s':time.time()-start});(out/'STAGES.json').write_text(json.dumps(stages,indent=2)+'\n');print(stage,r.returncode,flush=True)
 if r.returncode:raise RuntimeError('stage failed; original outputs retained: '+stage)
run('source_target',[sys.executable,str(models/'warpx_target_handoff_v0_2/run.py'),'--runtime',str(runtime),'--map',str(field),'--handoff-dir',str(models/'particle_handoff_v0_1'),'--out',str(out/'source_target')])
run('alpha',[sys.executable,str(models/'alpha_birth_escape_v0_1/run_refined.py'),'--receiver',str(out/'source_target/RESULTS.json'),'--models',str(models),'--samples-per-cell','256','--seed','20261101','--out',str(out/'alpha')])
run('facility',[sys.executable,str(package/'run_v004.py'),'--models',str(models),'--profile',str(profile),'--receiver',str(out/'source_target/RESULTS.json'),'--bank',str(out/'alpha/EVENT_BANK.npz'),'--out',str(out/'integrated')])
report={'status':'PASS_FRESH_CONDITIONAL_CONTROL_PIPELINE','profile_sha256':hashlib.sha256(profile.read_bytes()).hexdigest(),'map_sha256':hashlib.sha256(field.read_bytes()).hexdigest(),'executable_sha256':hashlib.sha256((runtime/'bin/warpx.3d').read_bytes()).hexdigest(),'outputs_sha256':{n:hashlib.sha256((out/n).read_bytes()).hexdigest() for n in ['source_target/RESULTS.json','alpha/RESULTS.json','alpha/EVENT_BANK.npz','integrated/RESULTS.json','integrated/PARTITION.npz']},'scientific_freeze':False,'actual_apparatus_net_power_W':None}
(out/'PIPELINE_RECEIPT.json').write_text(json.dumps(report,indent=2)+'\n');print(report['status'])
