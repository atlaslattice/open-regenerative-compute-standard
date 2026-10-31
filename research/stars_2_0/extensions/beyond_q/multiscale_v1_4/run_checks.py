from pathlib import Path
import subprocess,sys,json
ROOT=Path(__file__).resolve().parent;checks=[]
for name,cwd,module in [('v1.4',ROOT,'test_multiscale'),('v1.3',ROOT.parent/'kinetic_source_v1_3','test_benchmark')]:
 p=subprocess.run([sys.executable,'-m','unittest',module,'-v'],cwd=cwd,text=True,capture_output=True)
 (ROOT/'outputs'/('checks_'+name+'.txt')).write_text(p.stdout+p.stderr)
 checks.append(dict(suite=name,passed=p.returncode==0,exit_code=p.returncode))
(ROOT/'outputs/check_status.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
if not all(r['passed'] for r in checks):raise SystemExit(1)
