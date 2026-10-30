"""Actual WarpX collision-network benchmark; no reactor-performance inference."""
from pathlib import Path
import argparse,subprocess,os,json,hashlib,csv,shutil
ROOT=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def specification():
 return {
  'chain_on':{},'seed_219':{'warpx.random_seed':'219'},'seed_319':{'warpx.random_seed':'319'},
  'secondary_off':{'collisions.collision_names':'DDT DDN'},
  'no_T_birth':{'collisions.collision_names':'DDN DT'},
  'no_reactions':{'collisions.collision_names':'DDT','DDT.create_products':'0'},
  'half_dt':{'warpx.const_dt':'5.e-14','max_step':'40','diag1.intervals':'40'},
  'double_ppc':{'D.num_particles_per_cell':'2000'},
  'lower_multiplier':{'DDT.event_multiplier':'1.e9','DDN.event_multiplier':'1.e9','DT.event_multiplier':'1.e9'}
 }

def run(exe,cache,name,overrides):
 directory=cache/name;directory.mkdir(parents=True,exist_ok=True)
 args=[str(exe),str(ROOT/'inputs/dd_dt_chain')]+[k+'='+v for k,v in overrides.items()]
 dest=ROOT/'outputs/runs'/name;dest.mkdir(parents=True,exist_ok=True)
 proc=subprocess.run(args,cwd=directory,text=True,capture_output=True,env=dict(os.environ,OMP_NUM_THREADS='2',OPENBLAS_NUM_THREADS='1'))
 (dest/'stdout.txt').write_text(proc.stdout);(dest/'stderr.txt').write_text(proc.stderr)
 if proc.returncode:raise RuntimeError(f'{name}: WarpX exit {proc.returncode}, see logs')
 shutil.copyfile(directory/'warpx_used_inputs',dest/'warpx_used_inputs')
 for file in (directory/'diags/reducedfiles').glob('*.txt'):shutil.copyfile(file,dest/file.name)
 meta=dict(case=name,kind='ACTUAL_WARPX_COLLISION_NETWORK_BENCHMARK',package_version='26.10',
   upstream_tag_commit='ec1660d961696c865c87c26728b7e248b5454082',
   binary_version_banner='WarpX (Unknown); conda package pins release26.10, not an embedded source hash',
   executable_sha256=sha(exe),input_sha256=sha(ROOT/'inputs/dd_dt_chain'),overrides=overrides,threads=2,
   argv=args,input_hashes={x.name:sha(x) for x in dest.iterdir() if x.is_file()},
   physical_validation=False,reactor_A_primary_DD_reference_MW=20,reactor_B_DT_reference_MW=1130,
   reference_power_application='NOT imposed in this microscopic box; post-normalization only, no achievable-power claim')
 (dest/'provenance.json').write_text(json.dumps(meta,indent=2)+'\n')
 print(name,'completed',flush=True)

def main():
 p=argparse.ArgumentParser();p.add_argument('--executable',type=Path,required=True);p.add_argument('--cache',type=Path,required=True);p.add_argument('--only',nargs='*');a=p.parse_args()
 a.executable=a.executable.resolve();a.cache=a.cache.resolve();fail=[]
 for name,overrides in specification().items():
  if a.only and name not in a.only:continue
  try:run(a.executable,a.cache,name,overrides)
  except Exception as e:fail.append(dict(case=name,error=str(e)));print('FAILED',name,str(e),flush=True)
 (ROOT/'outputs/campaign_failures.json').write_text(json.dumps(fail,indent=2)+'\n')
 if fail:raise SystemExit(1)
if __name__=='__main__':main()
