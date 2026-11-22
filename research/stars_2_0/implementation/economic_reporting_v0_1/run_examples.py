import argparse, hashlib, json, platform, subprocess, sys
from pathlib import Path
from reporting import report, footer
from test_reporting import P, COSTS

p=argparse.ArgumentParser();p.add_argument('--out',required=True);a=p.parse_args()
out=Path(a.out);out.mkdir(parents=True,exist_ok=False)
tests=subprocess.run([sys.executable,'-m','unittest','-v'],cwd=Path(__file__).parent,capture_output=True,text=True)
(out/'testlog.txt').write_text(tests.stdout+tests.stderr)
if tests.returncode: raise SystemExit(tests.returncode)
cases=[report('synthetic-failed-hypothesis','FAIL','2026-10-28',[P],dict(COSTS,electricity='2')),
       report('g0b-design-v0.1-economic-placeholder','NOT_TESTED','2026-10-28',[],{k:None for k in COSTS})]
for n,r in enumerate(cases):
    (out/f'example_{n+1}.json').write_text(json.dumps(r,indent=2,allow_nan=False)+'\n')
    (out/f'example_{n+1}.md').write_text(footer(r))
receipt={'python':platform.python_version(),'randomness':'none','tests_returncode':tests.returncode,
         'physical_validation':'NOT_RUN','actual_market_quotes_ingested':0,
         'code_sha256':{f:hashlib.sha256((Path(__file__).parent/f).read_bytes()).hexdigest()
                        for f in ['reporting.py','test_reporting.py','run_examples.py']}}
(out/'RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
