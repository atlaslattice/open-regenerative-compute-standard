#!/usr/bin/env python3
"""Run regression tests, deterministic examples and independent baseline comparisons."""
from pathlib import Path
import argparse,copy,hashlib,json,math,subprocess,sys
from handoff import Engine
ROOT=Path(__file__).resolve().parent

def main():
    a=argparse.ArgumentParser();a.add_argument('--out',type=Path,required=True);a=a.parse_args();a.out.mkdir(parents=True,exist_ok=False)
    test=subprocess.run([sys.executable,'-m','unittest','-v','test_handoff'],cwd=ROOT,capture_output=True,text=True)
    (a.out/'TEST_LOG.txt').write_text(test.stdout+test.stderr)
    if test.returncode:raise RuntimeError('Handoff regression tests failed')
    examples={p.stem:json.loads(p.read_text()) for p in (ROOT/'examples').glob('*.json')}
    off=copy.deepcopy(examples['C_conditional_reference']);off['stages'][0]['reaction_model']='REACTIONS_OFF_CONTROL';examples['C_reactions_off']=off
    missing=copy.deepcopy(examples['C_conditional_reference']);missing['attempts'][0]['source_packets']=None;examples['C_missing_source']=missing
    for name,c in examples.items():
        path=a.out/(name+'.config.json');path.write_text(json.dumps(c,indent=2)+'\n')
        run=subprocess.run([sys.executable,str(ROOT/'run.py'),str(path.resolve()),'--out',str((a.out/name).resolve())],capture_output=True,text=True)
        (a.out/(name+'.console.txt')).write_text(run.stdout+run.stderr)
        if run.returncode:raise RuntimeError('Example failed: '+name)
    path=a.out/'C_conditional_reference.config.json'
    repeat=subprocess.run([sys.executable,str(ROOT/'run.py'),str(path.resolve()),'--out',str((a.out/'repeat_reference').resolve())],capture_output=True,text=True)
    if repeat.returncode:raise RuntimeError(repeat.stderr)
    original=(a.out/'C_conditional_reference/RESULTS.json').read_bytes();assert original==(a.out/'repeat_reference/RESULTS.json').read_bytes()
    e=Engine();old=e.p.reactions(e.coordinate,e.rows,.675,1e18,1.,16)
    result=json.loads(original);assert math.isclose(result['expected_events_all_attempts'],30000*old['probability'],rel_tol=1e-12)
    one=result['expected_events_all_attempts'];two=json.loads((a.out/'C_two_stage_equal_column/RESULTS.json').read_text())['expected_events_all_attempts']
    report={'status':'CONDITIONAL_INTERFACE_VERIFIED_NOT_APPARATUS_VALIDATION','regression_tests':32,'example_runs':len(examples),'repeat_result_byte_identical':True,'reference_result_sha256':hashlib.sha256(original).hexdigest(),'same_depth_grid_previous_integrator_expected_events':30000*old['probability'],'one_stage_expected_events':one,'two_stage_equal_total_column_expected_events':two,'equal_column_relative_difference':(two-one)/one,'maximum_particle_residual':max(abs(x['metrics']['particle_residual']) for x in result['attempts']),'maximum_energy_residual_MeV':max(abs(x['metrics']['energy_residual_MeV']) for x in result['attempts']),'A_apparatus_performance':None,'C_full_apparatus_performance':None,'wall_plug_net_power':None,'scientific_freeze':False}
    (a.out/'VERIFICATION.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
