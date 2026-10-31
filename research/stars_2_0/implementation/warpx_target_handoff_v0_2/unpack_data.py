import argparse,tarfile,json,hashlib
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--out',required=True);a=p.parse_args()
root=Path(__file__).resolve().parent;dest=Path(a.out);dest.mkdir(parents=True,exist_ok=False)
with tarfile.open(root/'raw_diagnostics.tar.gz') as t:
 for m in t.getmembers():assert m.isfile() and not Path(m.name).is_absolute() and '..' not in Path(m.name).parts
 t.extractall(dest,filter='data')
for r in json.loads((root/'RAW_INDEX.json').read_text()):assert hashlib.sha256((dest/r['path']).read_bytes()).hexdigest()==r['sha256']
print('All raw diagnostic files verified.')
