"""Extract saved arrays/traces without replacing original artifacts."""
import tarfile
from pathlib import Path
root=Path(__file__).resolve().parent
with tarfile.open(root/'replay_arrays_and_traces_current.tar.xz','r:xz') as t:
 for m in t:
  p=Path(m.name)
  if p.is_absolute() or '..' in p.parts or not m.isfile() or p.parts[0] not in ['run001','run002','run003','pipeline_run001','pipeline_run002','pipeline_run003','pipeline_run004','pipeline_run003_raw','pipeline_run004_raw','pipeline_run001_raw','pipeline_run002_raw','restoration']:raise ValueError('unexpected archive entry')
  f=root/p;b=t.extractfile(m).read()
  if f.exists():
   if f.read_bytes()!=b:raise ValueError('refusing replacement')
  else:f.parent.mkdir(parents=True,exist_ok=True);f.write_bytes(b)
print('arrays/traces restored; existing artifacts preserved')
