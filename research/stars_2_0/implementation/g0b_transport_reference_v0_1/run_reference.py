"""Offline synthetic verification only. New output directory required.
Run: OPENBLAS_NUM_THREADS=1 python run_reference.py --out NEW_DIRECTORY
"""
import argparse
import hashlib
import io
import json
from pathlib import Path
import platform
import unittest
import numpy as np
from transport import Layer,transmit_proton,escape_alpha
from test_transport import synthetic_table,response


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();a.out.mkdir(parents=True,exist_ok=False)
    root=Path(__file__).parent
    suite=unittest.defaultTestLoader.discover(str(root),pattern='test_transport.py')
    stream=io.StringIO();result=unittest.TextTestRunner(stream=stream,verbosity=2).run(suite)
    a.out.joinpath('test_log.txt').write_text(stream.getvalue())
    tables={(m,s):synthetic_table(m,s,S=S) for m,S in [('TEST_A',2),('TEST_B',3)] for s in ('proton','alpha')}
    layers=[Layer('L1','TEST_A',.2),Layer('L2','TEST_B',.3)]
    transmission=[]
    for E in (1.,2.,4.):
        for mu in (.5,1.):
            predicted=transmit_proton(E,mu,layers,tables)
            expected=max(0,E-(2*.2+3*.3)/mu)
            transmission.append({'energy_MeV':E,'mu':mu,'predicted':predicted,
                                 'independent_constant_stopping_oracle_MeV':expected})
    convergence=[]
    alpha=synthetic_table(species='alpha',S=1.)
    for n in (30,60,120):
        for L,R in ((.5,2.),(2.,2.),(4.,2.)):
            hit=0
            for j in range(n):
                for k in range(n):
                    x=escape_alpha(R,(k+.5)/n,0,(j+.5)/n,[Layer('L','TEST_A',L)],{('TEST_A','alpha'):alpha})
                    hit+=x['output_energy_MeV']>0
            p=hit/(n*n);oracle=1-L/(2*R) if L<=R else R/(2*L)
            convergence.append({'grid_per_axis':n,'slab_areal_mass_g_cm2':L,'range_g_cm2':R,
                'both_face_escape_probability':p,'analytic_oracle':oracle,'absolute_error':abs(p-oracle)})
    physical_attempt=None
    try:
        transmit_proton(1,1,[Layer('candidate_BN','BN_UNQUALIFIED',.001)],{},calibrated=True)
    except ValueError as exc:
        physical_attempt={'status':'BLOCKED','reason':str(exc),'physical_prediction':None}
    receipt={
        'software_verification':'PASS' if result.wasSuccessful() else 'FAIL',
        'physical_G0B_prediction':'BLOCKED_UNQUALIFIED_INPUTS',
        'data_class':'SYNTHETIC_ONLY_NOT_BORON_OR_BN',
        'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
        'environment':{'python':platform.python_version(),'numpy':np.__version__},
        'random_seed':None,'randomness':'none; deterministic fixtures and quadrature',
        'tolerances':{'constant_stopping_oracle':'13 decimal places in MeV for fixture scale',
            'slab_escape_probability':'absolute error <2/n, conservative grid-cell sanity bound',
            'calibration':'none asserted; facility thresholds require measured uncertainties'},
        'source_input_sha256':{f'{m}:{s}':t.source_sha256 for (m,s),t in tables.items()},
        'code_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(root.glob('*.py'))},
        'test_log_sha256':hashlib.sha256(a.out.joinpath('test_log.txt').read_bytes()).hexdigest(),
        'transmission_cases':transmission,'slab_grid_checks':convergence,
        'detector_example':response(((.7,.1),(.2,.6))).fold('alpha',[100,50],[3,4]),
        'missing_BN_refusal':physical_attempt,
        'method_sources':['https://physics.nist.gov/PhysRefData/Star/Text/appendix.html',
                          'https://physics.nist.gov/PhysRefData/Star/Text/programs.html'],
        'source_acquisition_attempt':{'url':'https://physics.nist.gov/PhysRefData/Star/Text/PSTAR-t.html',
            'direct_urllib_result':'HTTP 403 Forbidden; no stopping table acquired',
            'note':'Public documentation was retrieved through web search; this failed request is not proof that BN data do not exist.'},
        'limitations':['No physical stopping tables or measured beam/response ingested',
          'Planar infinite slab; no scattering, straggling or lateral escape',
          'No nuclear reaction probability or alpha birth generator',
          'Linear range interpolation; no domain extrapolation or invented low-energy tail',
          'Primary energy loss not equated to local heat or recoverable energy',
          'Single-hit response expected counts only; no calibrated counting likelihood',
          'Source evidence labels are supplied declarations, not independent certification',
          'Full covariance propagation and independent physical holdouts remain unimplemented']}
    a.out.joinpath('REFERENCE_RUN_SYNTHETIC_ONLY.json').write_text(json.dumps(receipt,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'software_verification':receipt['software_verification'],'tests':result.testsRun,
          'physical_G0B_prediction':receipt['physical_G0B_prediction'],
          'max_constant_stopping_error_MeV':max(abs(x['predicted']['output_energy_MeV']-x['independent_constant_stopping_oracle_MeV']) for x in transmission),
          'slab_grid_checks':convergence,'detector':receipt['detector_example']},indent=2,allow_nan=False))
    raise SystemExit(0 if result.wasSuccessful() else 1)


if __name__=='__main__':main()
