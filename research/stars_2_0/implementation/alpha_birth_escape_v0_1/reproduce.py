"""Verify inherited files, then delegate explicit CLI arguments to refined runner."""
import hashlib,json,subprocess,sys
from pathlib import Path
p=Path(__file__).resolve().parent
root=p.parent
for row in json.loads((p/'DEPENDENCY_LOCK.json').read_text()):
 f=root/row['path']
 if hashlib.sha256(f.read_bytes()).hexdigest()!=row['sha256']:raise ValueError('dependency changed: '+row['path'])
subprocess.run([sys.executable,str(p/'run_refined.py'),*sys.argv[1:]],check=True)
