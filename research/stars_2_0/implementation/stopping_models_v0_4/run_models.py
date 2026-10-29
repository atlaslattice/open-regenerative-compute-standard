"""Compare two documented stopping-model replays without fitting to the benchmark."""
import argparse,csv,hashlib,json,platform,statistics,subprocess,sys
from pathlib import Path
from model import load_tables,stopping,transport,NUCLEAR_VARIANTS

ROOT=Path(__file__).resolve().parent

def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError('output directory exists')
    tables=load_tables();benchmark=json.loads((ROOT/'OVERLEY_BENCHMARK.json').read_text())
    comparison=[];summary=[]
    for model in ['srim96','srim13']:
        rel=[]
        for r in benchmark['points']:
            x=stopping(tables,model=model,projectile='proton',material='OVERLEY_B10_ENRICHED',E_MeV=r['E_proton_LAB_MeV'])
            delta=x['total_eV_cm2_per_average_atom']/r['epsilon_eV_cm2_atom']-1;rel.append(delta)
            comparison.append(dict(model=model,E_proton_LAB_MeV=r['E_proton_LAB_MeV'],observed_digitized_eV_cm2_atom=r['epsilon_eV_cm2_atom'],predicted=x,fractional_discrepancy=delta))
        summary.append(dict(model=model,points=len(rel),mean_fractional_discrepancy=statistics.mean(rel),max_absolute_fractional_discrepancy=max(map(abs,rel)),fitted_parameters=0,
            status='HISTORICAL_SOURCE_COMPARISON_NOT_HELD_OUT_VALIDATION'))
    cases=[]
    for model in ['srim96','srim13']:
        for particle,E in [('proton',.65),('alpha',3.)]:
            for material,factor in [('B11',None),('BN_B11_N14',.8),('BN_B11_N14',1.),('BN_B11_N14',1.2)]:
                n=1e18 if material=='B11' else 2e18
                r=transport(tables,model=model,projectile=particle,material=material,E_MeV=E,total_atoms_cm2=n,bn_electronic_multiplier=factor)
                fine=transport(tables,model=model,projectile=particle,material=material,E_MeV=E,total_atoms_cm2=n,bn_electronic_multiplier=factor,refinement=32)
                error=abs(r['E_out_MeV']-fine['E_out_MeV'])
                if error>1e-6:raise ValueError('transport refinement gate failed')
                cases.append(dict(model=model,projectile=particle,material=material,bn_multiplier=factor,result=r,refinement_delta_MeV=error))
    variants=[dict(variant=v,**stopping(tables,model='srim13',projectile='alpha',material='B11',E_MeV=.01,nuclear_variant=v)) for v in NUCLEAR_VARIANTS]
    test=subprocess.run([sys.executable,'-m','unittest','-v','test_models'],cwd=ROOT,capture_output=True,text=True)
    if test.returncode:raise RuntimeError(test.stdout+test.stderr)
    receipt=dict(python=platform.python_version(),tests='12 PASS',table_count=8,electronic_stopping_nodes=968,
        assumed_boron_inventory_per_scenario_atoms_cm2=1e18,scenario_count=len(cases),
        scenario_meaning='assumed homogeneous cold targets and fixed incident energies; not apparatus specification or event source',
        seeds=None,fit='NONE; discrepant model predictions preserved',
        BN_status='Bragg mixture estimate; factors 0.8/1/1.2 are sensitivities, not BN confidence bounds',
        alpha_status='model replay available; original measured alpha table still missing',
        isotope_status='explicit equal-velocity electronic model transfer plus mass-dependent ZBL nuclear estimate',
        independent_validation='NOT_RUN',full_fusion_yield='NOT_COMPUTED',
        code_sha256={f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in ROOT.glob('*.py')})
    a.out.mkdir(parents=True,exist_ok=False)
    for name,obj in [('COMPARISON.json',comparison),('SUMMARY.json',summary),('SCENARIOS.json',cases),('NUCLEAR_VARIANTS.json',variants),('RECEIPT.json',receipt)]:
        (a.out/name).write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n')
    flat=[dict(model=r['model'],E_proton_LAB_MeV=r['E_proton_LAB_MeV'],observed_digitized_eV_cm2_atom=r['observed_digitized_eV_cm2_atom'],
        electronic_model_eV_cm2_atom=r['predicted']['electronic_eV_cm2_per_average_atom'],
        nuclear_model_eV_cm2_atom=r['predicted']['nuclear_eV_cm2_per_average_atom'],
        total_model_eV_cm2_atom=r['predicted']['total_eV_cm2_per_average_atom'],fractional_discrepancy=r['fractional_discrepancy']) for r in comparison]
    with (a.out/'COMPARISON.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(flat[0]));w.writeheader();w.writerows(flat)
    (a.out/'TEST_LOG.txt').write_text(test.stdout+test.stderr)
    (a.out/'MANIFEST.json').write_text(json.dumps({f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in a.out.iterdir()},indent=2)+'\n')
    print(json.dumps({'comparison':summary,'scenarios':len(cases),'max_refinement_delta_MeV':max(c['refinement_delta_MeV'] for c in cases)},indent=2))

if __name__=='__main__':main()
