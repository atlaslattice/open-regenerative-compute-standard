"""Fetch exact CC0 primary dataset; no silent replacement of existing files."""
import hashlib,json,urllib.request
from pathlib import Path
root=Path(__file__).resolve().parent
url='https://raw.githubusercontent.com/openPMD/openPMD-example-datasets/11e1a9d8281044c7e01dea9977291c871273da3f/example-femm-3d.h5'
b=urllib.request.urlopen(url,timeout=45).read();blob=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
assert blob=='fddd0a849d8f5ffc8ce9cd00fdc3dedd4ff62161'
with (root/'example-femm-3d.original.h5').open('xb') as f:f.write(b)
with (root/'DATASET_FETCH_RECEIPT.json').open('x') as f:json.dump(dict(url=url,git_blob_sha=blob,sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),license='CC0; upstream/openpmd/LICENSE'),f,indent=2);f.write('\n')
