"""Verify pinned external input bytes; package hashes cover local implementation."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def verify():
    rows=json.loads((ROOT/'source_manifest.json').read_text());result={}
    for r in rows:
        b=(ROOT.parent/r['path']).read_bytes()
        sha=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
        if sha!=r['git_blob_sha1']:raise ValueError('pinned source changed: '+r['path'])
        result[r['path']]=dict(git_blob_sha1=sha,sha256=hashlib.sha256(b).hexdigest())
    return result
