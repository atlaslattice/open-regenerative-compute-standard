import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parent
for r in json.loads((root/'SOURCE_INDEX.json').read_text())['files']:
 b=(root/'upstream'/r['path']).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==r['sha'],r['path']
print('Pinned upstream text files match their Git blob identities.')
