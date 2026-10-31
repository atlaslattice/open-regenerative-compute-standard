"""Fetch the public author-hosted paper and require the recovered source hash."""
import argparse,hashlib,json,urllib.request
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--out',required=True);a=p.parse_args();root=Path(__file__).resolve().parent;meta=json.loads((root/'DOWNLOAD.json').read_text());dest=Path(a.out)
if dest.exists():
 if hashlib.sha256(dest.read_bytes()).hexdigest()!=meta['sha256']:raise ValueError('refusing to replace existing file')
 print('existing source hash verified')
else:
 b=urllib.request.urlopen(meta['url'],timeout=30).read()
 if hashlib.sha256(b).hexdigest()!=meta['sha256']:raise ValueError('remote source changed; no file saved')
 dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(b);print('source downloaded; hash verified')
