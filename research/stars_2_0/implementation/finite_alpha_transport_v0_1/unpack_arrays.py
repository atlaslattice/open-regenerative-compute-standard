"""Extract versioned result arrays without overwriting existing artifacts."""
import tarfile
from pathlib import Path
root=Path(__file__).resolve().parent
allowed={r+'/aspect_'+a+'.npz' for r in ['run001','run002','run003'] for a in ['2.0','10.0','100.0','1000000.0']}
with tarfile.open(root/'result_arrays.tar.xz','r:xz') as t:
 for m in t:
  if m.name not in allowed or not m.isfile():raise ValueError('unexpected archive entry')
  dest=root/m.name;payload=t.extractfile(m).read()
  if dest.exists():
   if dest.read_bytes()!=payload:raise ValueError('refusing replacement')
  else:dest.parent.mkdir(exist_ok=True);dest.write_bytes(payload)
print('result arrays available; existing artifacts preserved')
