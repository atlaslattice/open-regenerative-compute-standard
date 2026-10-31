"""Unpack bundled raw reduced diagnostics into a NEW directory."""
import argparse,tarfile
from pathlib import Path
p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',required=True);a=p.parse_args()
out=Path(a.out).resolve();out.mkdir(parents=True,exist_ok=False)
with tarfile.open(Path(__file__).resolve().parent/'diagnostics_reduced.tar.gz') as tf:
 for m in tf.getmembers():
  assert m.isfile() and not Path(m.name).is_absolute() and '..' not in Path(m.name).parts
 tf.extractall(out,filter='data')
