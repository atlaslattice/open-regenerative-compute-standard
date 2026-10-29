import argparse
import sys
from .runner import run

def main():
    p=argparse.ArgumentParser(description='Stars synthetic reference runner; calibrated modes blocked')
    sub=p.add_subparsers(dest='command',required=True)
    r=sub.add_parser('run');r.add_argument('configuration');r.add_argument('--out',required=True)
    u=sub.add_parser('ui');u.add_argument('configuration');u.add_argument('--out',required=True)
    a=p.parse_args()
    try:
        if a.command=='ui':
            from .ui import build
            from .runner import read_json
            build(read_json(a.configuration),a.out)
            print('Local editor created: '+a.out);return 0
        result=run(a.configuration,a.out)
    except (ValueError,KeyError,TypeError,OSError) as exc:
        print(f'Stars run failed: {exc}',file=sys.stderr);return 2
    print(f"{result['status']}; physical prediction BLOCKED; report: {a.out}/REPORT.md")
    return 0

if __name__=='__main__':raise SystemExit(main())
