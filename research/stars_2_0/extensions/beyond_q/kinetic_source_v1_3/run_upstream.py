"""Run unmodified WarpX26.10 DD/DT inputs and their supplied analysis."""
from pathlib import Path
import os,subprocess,json,hashlib,argparse,sys
ROOT=Path(__file__).resolve().parent

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--executable',type=Path,required=True);ap.add_argument('--cache',type=Path,required=True);a=ap.parse_args()
 exe=a.executable.resolve();cache=a.cache.resolve();out=ROOT/'outputs';out.mkdir(exist_ok=True)
 env=dict(os.environ,OMP_NUM_THREADS='2',OPENBLAS_NUM_THREADS='1',PYTHONPATH=str(ROOT/'upstream/Tools/Parser'))
 results=[]
 for reaction in ('deuterium_deuterium','deuterium_tritium'):
  case=cache/('upstream_'+reaction);case.mkdir(parents=True,exist_ok=True)
  inp=ROOT/'upstream/Examples/Tests/nuclear_fusion'/('inputs_test_3d_'+reaction+'_fusion')
  p=subprocess.run([str(exe),str(inp)],cwd=case,env=env,text=True,capture_output=True)
  (out/(reaction+'_stdout.txt')).write_text(p.stdout);(out/(reaction+'_stderr.txt')).write_text(p.stderr)
  status=dict(reaction=reaction,run_exit=p.returncode,upstream_input_overrides=[],
    input_sha256=hashlib.sha256(inp.read_bytes()).hexdigest(),executable_sha256=hashlib.sha256(exe.read_bytes()).hexdigest())
  if not p.returncode:
   q=subprocess.run([sys.executable,str(ROOT/'upstream/Examples/Tests/nuclear_fusion/analysis_two_product_fusion.py'),str(case/'diags/diag1000001')],cwd=case,env=env,text=True,capture_output=True)
   (out/(reaction+'_analysis.txt')).write_text(q.stdout+q.stderr)
   status.update(analysis_exit=q.returncode,passed=q.returncode==0)
  else:status['passed']=False
  results.append(status);print(reaction,status,flush=True)
 (out/'upstream_status.json').write_text(json.dumps(results,indent=2)+'\n')
 if not all(r['passed'] for r in results):raise SystemExit(1)
if __name__=='__main__':main()
