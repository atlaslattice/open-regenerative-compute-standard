"""Execute the seven frozen field fixtures in a new output root."""
import argparse,json,os,subprocess,time,hashlib
from pathlib import Path
root=Path(__file__).resolve().parent
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--executable',required=True);p.add_argument('--out',required=True);a=p.parse_args()
out=Path(a.out).resolve();out.mkdir(parents=True,exist_ok=False)
rows=[]
for case in json.loads((root/'ORBIT_CASES_v003.json').read_text()):
 name=case['case'];inp=root/'inputs_v002'/name;dest=out/(name+'002');dest.mkdir()
 t=time.time()
 with (dest/'RUN.log').open('x') as f:r=subprocess.run([str(Path(a.executable).resolve()),str(inp)],cwd=dest,env={**os.environ,'OMP_NUM_THREADS':'2'},stdout=f,stderr=subprocess.STDOUT)
 rows.append(dict(case=name,returncode=r.returncode,input_sha256=hashlib.sha256(inp.read_bytes()).hexdigest(),elapsed_s=time.time()-t))
 if r.returncode:break
with (out/'EXECUTION_RECEIPT.json').open('x') as f:json.dump(rows,f,indent=2);f.write('\n')
assert len(rows)==7 and all(r['returncode']==0 for r in rows)
