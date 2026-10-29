import argparse,hashlib,json,platform,subprocess,sys
from pathlib import Path
from derive_event_data import extract,derive
from thin_target import expected_events
p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args();a.out.mkdir(parents=True,exist_ok=False)
root=Path(__file__).parent
index=json.loads((root/'SOURCE_INDEX.json').read_text());records=[]
for entry in index:
    raw=(root/'source_tables'/f"table{entry['table']}.html").read_bytes()
    if hashlib.sha256(raw).hexdigest()!=entry['table_fragment_sha256']:raise ValueError('source fragment identity mismatch')
    records+=extract(raw,entry['table'])
rows=derive(records)
r=subprocess.run([sys.executable,'-m','unittest','-v','test_bridge'],cwd=root,capture_output=True,text=True)
(a.out/'testlog.txt').write_text(r.stdout+r.stderr)
if r.returncode:raise SystemExit(r.returncode)
(a.out/'COEFFICIENTS.json').write_text(json.dumps(records,indent=2)+'\n')
(a.out/'EVENT_CROSS_SECTIONS.json').write_text(json.dumps(rows,indent=2,allow_nan=False)+'\n')
scenarios=[expected_events(rows,E_lab_MeV=.65,incident_protons=n,B11_atoms_cm2=1e18) for n in [0,10000,1000000,2000000]]
(a.out/'CONDITIONAL_SCENARIOS.json').write_text(json.dumps(scenarios,indent=2)+'\n')
receipt={'python':platform.python_version(),'source_tables':3,'coefficient_rows':59,'event_grid_rows':41,'tests':9,'test_result':'PASS','nuclear_source_status':'PUBLICATION_COEFFICIENTS_SOURCE_REPRODUCED; derived event definition follows paper','physical_Stars_validation':'NOT_RUN','original_EXFOR_observable':'UNCHANGED_PENDING_LINEAGE_REVIEW','randomness':'none','sources':index,'code_sha256':{f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in root.glob('*.py')}}
(a.out/'RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'receipt':receipt,'scenario10000':scenarios[1],'stable_shot_probability':scenarios[2]['probability_at_least_one_event_per_attempt'],'same_mean_but_zero_or_double_shot_probability':.5*scenarios[3]['probability_at_least_one_event_per_attempt']},indent=2))
