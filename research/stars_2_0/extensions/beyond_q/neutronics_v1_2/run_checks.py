"""Run isolated regression suites; write evidence only in this release."""
from pathlib import Path
import json,subprocess,sys
ROOT=Path(__file__).resolve().parent
suites=[('v1.1',ROOT.parent/'dynamic_fuel_cycle_v1_1',['discover','-s','tests','-v']),
        ('v1.1.1',ROOT.parent/'verification_v1_1_1',['test_verification','-v']),
        ('v1.1.2',ROOT.parent/'review_reconciliation_v1_1_2',['test_review','-v']),
        ('v1.2',ROOT,['test_neutronics','-v'])]
results=[]
for label,cwd,args in suites:
    proc=subprocess.run([sys.executable,'-m','unittest',*args],cwd=cwd,text=True,capture_output=True)
    (ROOT/'outputs'/f'checks_{label}.txt').write_text(proc.stdout+proc.stderr)
    results.append(dict(suite=label,exit_code=proc.returncode,passed=proc.returncode==0))
(ROOT/'outputs/check_status.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
if any(not r['passed'] for r in results):raise SystemExit(1)
