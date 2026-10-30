#!/usr/bin/env python3
import argparse,hashlib,json,platform
from pathlib import Path
import numpy as np
from handoff import execute

def encoded(x):return json.dumps(x,indent=2,sort_keys=True,allow_nan=False)+'\n'
def main():
 p=argparse.ArgumentParser();p.add_argument('config',type=Path);p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
 raw=a.config.read_bytes();(a.out/'CONFIG.json').write_bytes(raw)
 try:
  result=execute(json.loads(raw));(a.out/'RESULTS.json').write_text(encoded(result))
  receipt={'python':platform.python_version(),'numpy':np.__version__,'config_sha256':hashlib.sha256(raw).hexdigest(),'code_hashes':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in (Path(__file__).parent/n for n in ('handoff.py','run.py','test_handoff.py','verify_release.py'))},'dependency_lock_sha256':hashlib.sha256((Path(__file__).parent/'DEPENDENCY_LOCK.json').read_bytes()).hexdigest(),'result_sha256':hashlib.sha256((a.out/'RESULTS.json').read_bytes()).hexdigest(),'seed':None,'randomness':'Deterministic expected-weight integration; not physical shot sampling','status':result['status'],'scientific_freeze':False}
  (a.out/'RECEIPT.json').write_text(encoded(receipt));print(encoded({'status':result['status'],'architecture_id':result['architecture_id'],'expected_events_all_attempts':result.get('expected_events_all_attempts')}))
 except Exception as e:
  (a.out/'FAILURE.json').write_text(encoded({'error':type(e).__name__,'reason':str(e)}));raise
if __name__=='__main__':main()
