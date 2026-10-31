"""Run byte-exact upstream pB input and analysis in an append-only output directory."""
import argparse,hashlib,json,os,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--executable',required=True);p.add_argument('--analysis-python',required=True);p.add_argument('--out',required=True);a=p.parse_args()
 out=Path(a.out).resolve();out.mkdir(parents=True,exist_ok=False)
 index=json.loads((ROOT/'UPSTREAM_SOURCE_INDEX.json').read_text())
 for f in index['fixtures']:
  b=(ROOT/'upstream'/f['path']).read_bytes()
  assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==f['git_blob_sha'],f['path']
 fixture=ROOT/'upstream/Examples/Tests/nuclear_fusion'
 inp=fixture/'inputs_test_3d_proton_boron_fusion'
 env={**os.environ,'OMP_NUM_THREADS':'2','PYTHONPATH':str(ROOT/'upstream/Tools/Parser')}
 commands=[[str(Path(a.executable).resolve()),str(inp)],[str(Path(a.analysis_python).resolve()),str(fixture/'analysis_proton_boron_fusion.py'),'diags/diag1000001']]
 records=[]
 for cmd,name in zip(commands,['RUN','ANALYSIS']):
  start=time.time()
  with (out/(name+'.log')).open('x') as f:r=subprocess.run(cmd,cwd=out,env=env,stdout=f,stderr=subprocess.STDOUT)
  records.append(dict(stage=name,command=cmd,returncode=r.returncode,wall_elapsed_s=time.time()-start))
  if r.returncode:break
 receipt=dict(status='PASS' if len(records)==2 and all(r['returncode']==0 for r in records) else 'FAILED',commands=records,source_commit=index['release_source_commit'],input_sha256=sha(inp),executable_sha256=sha(a.executable),analysis_python=str(Path(a.analysis_python).resolve()),input_parameter_overrides=[],layout='NOMPI, 2 OpenMP threads; upstream CMake calls for 2 MPI ranks',random_seed='upstream input/defaults; no override',no_confinement_validation=True)
 (out/'EXECUTION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
 print(json.dumps(receipt,indent=2))
 if receipt['status']!='PASS':sys.exit(1)
if __name__=='__main__':main()
