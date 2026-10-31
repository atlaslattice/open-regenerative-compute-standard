"""Extract saved WarpX text traces without replacing any artifact."""
import tarfile
from pathlib import Path
root=Path(__file__).resolve().parent
with tarfile.open(root/'warpx_traces.tar.xz','r:xz') as t:
 for m in t:
  p=Path(m.name)
  if not m.isfile() or p.is_absolute() or '..' in p.parts or p.parts[0] not in ['warpx_run001','warpx_run002','warpx_run003']:raise ValueError('unexpected archive entry')
  dest=root/p;payload=t.extractfile(m).read()
  if dest.exists():
   if dest.read_bytes()!=payload:raise ValueError('refusing replacement: '+str(dest))
  else:dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(payload)
print('traces available; original artifacts preserved')
