"""Optional public-source acquisition; saves only to caller's chosen output path.

python fetch_precursor.py /tmp/CoSCD1980.pdf
No authentication or publisher access-control bypass is used.
"""
import hashlib
from pathlib import Path
import sys
import urllib.request

URL='https://www.osti.gov/servlets/purl/6712040'


if __name__=='__main__':
    if len(sys.argv)!=2:
        raise SystemExit('Usage: python fetch_precursor.py OUTPUT_PDF')
    with urllib.request.urlopen(URL,timeout=30) as response:
        data=response.read()
    if not data.startswith(b'%PDF'):
        raise SystemExit('Response was not PDF; no file written')
    Path(sys.argv[1]).write_bytes(data)
    print('SHA256',hashlib.sha256(data).hexdigest(),'bytes',len(data))
