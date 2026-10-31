"""Verify pinned code, inputs and the independently updated ARC design lock."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent

def verify():
    out={}
    for x in json.loads((ROOT/'source_manifest.json').read_text()):
        b=(ROOT.parent/x['path']).read_bytes()
        sha=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
        if sha!=x['git_blob_sha1']:raise ValueError('pinned input changed: '+x['path'])
        out[x['path']]=dict(git_blob_sha1=sha,sha256=hashlib.sha256(b).hexdigest())
    return out
if __name__=='__main__':
    (ROOT/'outputs/source_sha256.json').write_text(json.dumps(verify(),indent=2)+'\n')
