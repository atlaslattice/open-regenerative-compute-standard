"""Safely extract archived event banks without replacing existing files."""
import tarfile
from pathlib import Path
root=Path(__file__).resolve().parent
with tarfile.open(root/'event_banks.tar.gz','r:gz') as t:
 for member in t:
  p=Path(member.name)
  if len(p.parts)!=2 or p.parts[0] not in ['run001','run002','run003','run004'] or p.parts[1]!='EVENT_BANK.npz' or not member.isfile():raise ValueError('unexpected archive entry')
  dest=root/p
  payload=t.extractfile(member).read()
  if dest.exists():
   if dest.read_bytes()!=payload:raise ValueError('refusing replacement: '+str(dest))
  else:
   dest.parent.mkdir(exist_ok=True);dest.write_bytes(payload)
print('event banks available; existing files preserved')
