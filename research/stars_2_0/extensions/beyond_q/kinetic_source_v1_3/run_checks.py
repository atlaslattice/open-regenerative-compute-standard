"""Visible numerical-regression results; no older release outputs overwritten."""
from pathlib import Path
import sys,subprocess,json,argparse
ROOT=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--reference-python',default=sys.executable);args=ap.parse_args()
checks=[]
for label,cwd,module in [('v1.3',ROOT,'test_benchmark'),('v1.2',ROOT.parent/'neutronics_v1_2','test_neutronics')]:
 p=subprocess.run([args.reference_python if label=='v1.2' else sys.executable,'-m','unittest',module,'-v'],cwd=cwd,text=True,capture_output=True)
 (ROOT/'outputs'/('checks_'+label+'.txt')).write_text(p.stdout+p.stderr)
 checks.append(dict(suite=label,passed=p.returncode==0,exit_code=p.returncode))
(ROOT/'outputs/check_status.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
if not all(r['passed'] for r in checks):raise SystemExit(1)
