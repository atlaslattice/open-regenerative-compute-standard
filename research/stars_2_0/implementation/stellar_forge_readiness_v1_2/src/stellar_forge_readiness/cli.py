import argparse,csv,hashlib,json,platform
from pathlib import Path
from .readiness import batch

def read(path):
    def bad(x):raise ValueError('nonfinite JSON constant '+x)
    def unique(pairs):
        d={}
        for k,v in pairs:
            if k in d:raise ValueError('duplicate JSON key')
            d[k]=v
        return d
    return json.loads(Path(path).read_text(),parse_constant=bad,object_pairs_hook=unique)

def dump(x):return json.dumps(x,indent=2,allow_nan=False)+'\n'

def main():
    p=argparse.ArgumentParser(description='Readiness policy evaluator, not hardware control')
    s=p.add_subparsers(dest='command',required=True)
    for name in ['evaluate','ui']:
        a=s.add_parser(name);a.add_argument('configuration');a.add_argument('--out',required=True)
    a=p.parse_args();out=Path(a.out)
    if a.command=='ui':
        from .ui import build
        build(read(a.configuration),out);print('Local readiness editor: '+str(out));return 0
    out.mkdir(parents=True,exist_ok=False)
    try:
        c=read(a.configuration)
        (out/'INPUT.json').write_text(dump(c))
        if c.get('schema_version')!='1.2':raise ValueError('schema 1.2 required')
        r=batch(c['attempts']);(out/'RESULTS.json').write_text(dump(r))
        # JSONL retains one complete attempt and result per line. New directory only.
        (out/'ATTEMPTS.jsonl').write_text(''.join(json.dumps({'input':i,'result':o},allow_nan=False)+'\n' for i,o in zip(c['attempts'],r['attempts'])))
        with (out/'SUMMARY.csv').open('w',newline='') as f:
            w=csv.writer(f);w.writerow(['attempt_id','status','first_qualifying_sample_s','first_confirmed_readiness_s','attempt_end_s','driver_wall_energy_J'])
            for x in r['attempts']:w.writerow([x[k] for k in ['attempt_id','status','first_qualifying_sample_s','first_confirmed_readiness_s','attempt_end_s','driver_wall_energy_J']])
        (out/'REPORT.md').write_text('# Stellar Forge readiness v.1.2\n\nObservation-policy evaluation only; no laser connection, saturation proof or fusion prediction.\n\n'+dump(r['summary'])+'\nAll attempted preparations, including timeouts and aborts, are retained in ATTEMPTS.jsonl. Raw sensor values, specimen and calibration metadata and subsequent-outcome placeholders are preserved.\n')
        manifest={'python':platform.python_version(),'input_sha256':hashlib.sha256(Path(a.configuration).read_bytes()).hexdigest(),'code_sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in Path(__file__).parent.glob('*.py')},'output_sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in out.iterdir() if f.is_file()},'hardware_control':'NONE','randomness':'none'}
        (out/'MANIFEST.json').write_text(dump(manifest))
        print(json.dumps(r['summary']));return 0
    except Exception as e:
        (out/'FAILURE.json').write_text(dump({'failure_code':'FAIL_READINESS_INPUT','error':str(e),'physical_action':'NONE'}))
        print(str(e));return 2

if __name__=='__main__':raise SystemExit(main())
