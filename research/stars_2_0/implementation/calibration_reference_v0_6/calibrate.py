"""Source-specific descriptive fit to measured proton stopping, not STARS calibration."""
import argparse,hashlib,importlib.util,itertools,json,math,platform,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
MATERIAL='OVERLEY_B10_ENRICHED'

def encoded(x):return json.dumps(x,indent=2,sort_keys=True,allow_nan=False)+'\n'

def check_dependencies():
    for r in json.loads((ROOT/'DEPENDENCY_LOCK.json').read_text()):
        if hashlib.sha256((ROOT/r['file']).read_bytes()).hexdigest()!=r['sha256']:
            raise ValueError('dependency mismatch: '+r['file'])

def model_module():
    check_dependencies()
    spec=importlib.util.spec_from_file_location('cold_model_v04',ROOT.parent/'stopping_models_v0_4/model.py')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod

def fit_scale(observed,predicted):
    if len(observed)!=len(predicted) or not observed:raise ValueError('matching nonempty data required')
    if any(not math.isfinite(x) or x<=0 for x in [*observed,*predicted]):raise ValueError('positive finite stopping required')
    return math.exp(sum(math.log(y/x) for y,x in zip(observed,predicted))/len(observed))

def metrics(observed,predicted):
    r=[x/y-1 for y,x in zip(observed,predicted)]
    return dict(points=len(r),rms_fractional_discrepancy=math.sqrt(sum(x*x for x in r)/len(r)),
        mean_fractional_discrepancy=sum(r)/len(r),max_absolute_fractional_discrepancy=max(map(abs,r)))

def adjusted_stopping(model,tables,fit,*,projectile,material,E_MeV):
    """Fail closed on transfer of this source-specific TOTAL-stopping scale."""
    if projectile!='proton' or material!=MATERIAL:raise ValueError('fit is not calibrated for this projectile/material')
    lo,hi=fit['energy_domain_LAB_MeV']
    if not math.isfinite(E_MeV) or not lo<=E_MeV<=hi:raise ValueError('fit energy domain exceeded')
    if fit['status']!='SOURCE_SPECIFIC_DESCRIPTIVE_CALIBRATION' or fit['model'] not in ('srim96','srim13') or fit['material']!=MATERIAL or fit['projectile']!='proton':
        raise ValueError('unsupported fit identity')
    scale=fit['total_stopping_scale']
    if not math.isfinite(scale) or scale<=0:raise ValueError('invalid scale')
    base=model.stopping(tables,model=fit['model'],projectile=projectile,material=material,E_MeV=E_MeV)
    # The measured curve resolves total energy loss only; no fitted Se/Sn decomposition.
    return dict(E_proton_LAB_MeV=E_MeV,epsilon_total_eV_cm2_atom=scale*base['total_eV_cm2_per_average_atom'],
        status=fit['status'],material=material,total_stopping_scale=scale,
        energy_domain_LAB_MeV=[lo,hi],independent_validation=False,
        fitted_Se_Sn_decomposition=None,confidence_interval=None)

def analyse():
    model=model_module();tables=model.load_tables()
    fixture=json.loads((ROOT/'OVERLEY_BENCHMARK.json').read_text());rows=fixture['points']
    energies=[r['E_proton_LAB_MeV'] for r in rows];observed=[r['epsilon_eV_cm2_atom'] for r in rows]
    # Retrospective diagnostic energy blocks, deliberately not random point splitting.
    blocks=[list(range(0,9)),list(range(9,18)),list(range(18,27))]
    results=[]
    for name in ['srim96','srim13']:
        def base(E):return model.stopping(tables,model=name,projectile='proton',material=MATERIAL,E_MeV=E)['total_eV_cm2_per_average_atom']
        predicted=list(map(base,energies));scale=fit_scale(observed,predicted)
        fit=dict(model=name,material=MATERIAL,projectile='proton',total_stopping_scale=scale,
            energy_domain_LAB_MeV=[min(energies),max(energies)],status='SOURCE_SPECIFIC_DESCRIPTIVE_CALIBRATION',
            objective='unweighted mean squared log(observed / (scale * total_model)); one positive parameter',
            statistical_likelihood=None,parameter_confidence_interval=None,independent_validation=False)
        folds=[]
        for held in blocks:
            train=[i for i in range(len(rows)) if i not in held]
            fitted=fit_scale([observed[i] for i in train],[predicted[i] for i in train])
            folds.append(dict(held_out_indices=held,training_indices=train,total_stopping_scale=fitted,
                held_out_LAB_energy_range_MeV=[energies[held[0]],energies[held[-1]]],
                before=metrics([observed[i] for i in held],[predicted[i] for i in held]),
                after=metrics([observed[i] for i in held],[fitted*predicted[i] for i in held]),
                status='RETROSPECTIVE_WITHIN_SOURCE_ENERGY_BLOCK_DIAGNOSTIC_NOT_INDEPENDENT_CAMPAIGN_HOLDOUT'))
        stress=[]
        for norm,offset,shift in itertools.product([.96,1.04],[-.08e-15,.08e-15],[-.008,.008]):
            shifted=[E+shift for E in energies]
            y=[norm*x+offset for x in observed]
            stress.append(dict(coherent_source_scale=norm,coherent_stopping_offset_eV_cm2_atom=offset,
                coherent_energy_shift_MeV=shift,total_stopping_scale=fit_scale(y,list(map(base,shifted)))))
        results.append(dict(fit=fit,before=metrics(observed,predicted),after=metrics(observed,[scale*x for x in predicted]),
            residuals=[dict(E_proton_LAB_MeV=E,observed_eV_cm2_atom=y,base_total_eV_cm2_atom=x,
                adjusted_total_eV_cm2_atom=scale*x,adjusted_fractional_discrepancy=scale*x/y-1)
                for E,y,x in zip(energies,observed,predicted)],energy_block_diagnostics=folds,
            coherent_stress_cases=stress,stress_scale_range=[min(s['total_stopping_scale'] for s in stress),max(s['total_stopping_scale'] for s in stress)]))
    return dict(source_doi='10.7907/XZP6-5P63',source_figure='Figure 7, printed p82 / PDF p87',
        measurements=27,source_target='95.96 atom% B10 and 4.04 atom% B11; historical cold boron foil',
        uncertainty='4% reported probable error is NOT converted to Gaussian sigma; full covariance unknown. +/-0.008 MeV and +/-0.08e-15 digitization allowances are analysis choices. Stress range is NOT a confidence interval.',
        independence='single historical campaign; potential SRIM training ancestry; no independent validation claimed',
        transfer_to_B11_BN_alpha_or_hot_targets='BLOCKED',models=results)

def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError('preserve earlier run; choose new output directory')
    r=analyse();a.out.mkdir(parents=True,exist_ok=False)
    (a.out/'CALIBRATION.json').write_text(encoded(r))
    (a.out/'FITS.json').write_text(encoded([x['fit'] for x in r['models']]))
    (a.out/'RECEIPT.json').write_text(encoded(dict(python=platform.python_version(),seed=None,
        optimizer='analytic geometric-mean scale; deterministic',tests_not_run_by_this_command=True,
        hashes={f:hashlib.sha256((ROOT/f).read_bytes()).hexdigest() for f in ['calibrate.py','OVERLEY_BENCHMARK.json','DEPENDENCY_LOCK.json']})))
    print(encoded({x['fit']['model']:dict(scale=x['fit']['total_stopping_scale'],before=x['before'],after=x['after'],stress_range=x['stress_scale_range']) for x in r['models']}))

if __name__=='__main__':main()
