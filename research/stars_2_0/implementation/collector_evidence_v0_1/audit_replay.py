"""Check saved source recovery replay without downloading the source paper."""
import hashlib,json,csv
from pathlib import Path
root=Path(__file__).resolve().parent;checks=[]
def check(name,ok):
 checks.append({'name':name,'passed':bool(ok)})
 if not ok:raise AssertionError(name)
for name in ['RESULTS.json','FIGURE15_COLLECTOR_POINTS.csv','FIGURE15_RECOVERY.png']:
 check(name+'_byte_exact_replay',(root/'run001'/name).read_bytes()==(root/'run002'/name).read_bytes())
for run in ['run001','run002']:
 r=json.loads((root/run/'RESULTS.json').read_text());check(run+'_source_checks',all(c['passed'] for c in r['checks']));check(run+'_no_pB_net_claim',r['STARS_pB_net_wall_plug_W'] is None)
 rows=list(csv.DictReader((root/run/'FIGURE15_COLLECTOR_POINTS.csv').open()));check(run+'_preserves_19_markers',len(rows)==19)
 for i,row in enumerate(rows):
  V=float(row['voltage_V']);I=float(row['net_collector_current_A']);check(run+'_'+str(i)+'_digitization_bounds',float(row['digitization_low_V'])<=V<=float(row['digitization_high_V']) and float(row['digitization_low_A'])<=I<=float(row['digitization_high_A']))
(root/'REPLAY_AUDIT.json').write_text(json.dumps({'status':'PASS','checks_passed':len(checks),'checks':checks},indent=2)+'\n');print('replay checks',len(checks),'PASS')
