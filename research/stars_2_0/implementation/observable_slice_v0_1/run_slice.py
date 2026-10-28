"""Run exact source reconciliation, tests and synthetic experiments without network.
Output directory must not exist. Raw EXFOR is an external, hash-checked input.
"""
import argparse
import csv
from decimal import Decimal as D
import hashlib
import io
import json
from pathlib import Path
import platform
import unittest
import numpy as np
from observables import Source, Quantity, Frame, SourceRegistry, import_csv, covariance, strict_json
from identifiability import experiments

CSV_HASH='e56d240ea05fb8663debbb42cef99a93ef466d309eec3dbeb239f77509a6d089'
X4_HASH='e6bb8289bf67c485af9a97c212d5604421dae7ab5aad91bbf7064618277d0efb'
BASE='9bfe5e6bace4e7cc1bc9b64962ab99325ebd462f'
CSV_PATH='research/stars_2_0/wp_b/revised/data/EXFOR_C2973002_SPRAKER_2012_41PT_CROSS_SECTION_SOURCE_NORMALIZED_2026-10-27.csv'


def reconcile_x4(raw, rows):
    """Independent fixed-width reader, deliberately only this pinned EXFOR table."""
    if hashlib.sha256(raw).hexdigest()!=X4_HASH:
        raise ValueError('EXFOR fixture bytes differ; qualify new source in a new version')
    lines=raw.decode().splitlines()
    start=next(i for i,s in enumerate(lines) if s.startswith('SUBENT') and 'C2973002' in s)
    stop=next(i for i in range(start+1,len(lines)) if lines[i].startswith('ENDSUBENT'))
    block=lines[start:stop]
    if not any('(5-B-11(P,A)4-BE-8,,SIG)' in s for s in block):
        raise ValueError('Unexpected reaction')
    di=next(i for i,s in enumerate(block) if s.startswith('DATA '))
    if block[di+1].split()!=['EN','DATA','ERR-S'] or block[di+2].split()!=['MEV','MB','MB']:
        raise ValueError('Unexpected source units or columns')
    triples=[]
    for line in block[di+3:]:
        if line.startswith('ENDDATA'): break
        a,b,c=[D(line[j:j+11].strip()) for j in (0,11,22)]
        triples.append((a,b/D(1000),c/D(1000)))
    if len(triples)!=41 or len(rows)!=41:
        raise ValueError('Expected exactly 41 rows')
    for original, normalized in zip(triples,rows):
        if original != (normalized.energy_mev,normalized.value_b,normalized.stat_unc_b):
            raise ValueError('Exact decimal source comparison failed')
    return {'rows':41,'numeric_cells':123,'comparison':'exact Decimal; MB to barn /1000',
            'result':'PASS','energy_uncertainty':'not reported in this table; not assumed zero'}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--csv',required=True,type=Path)
    ap.add_argument('--exfor',required=True,type=Path)
    ap.add_argument('--out',required=True,type=Path)
    args=ap.parse_args()
    args.out.mkdir(parents=True,exist_ok=False)
    raw=args.csv.read_bytes()
    src=Source('C2973002','EXFOR:C2973002:Spraker2012',CSV_HASH,
        f'https://github.com/atlaslattice/open-regenerative-compute-standard/blob/{BASE}/{CSV_PATH}',
        '11B(p,a)8Be',Quantity.REPORTED_ALPHA_CROSS_SECTION,Frame.LAB,
        'INTAD per EXFOR; angular and detector acceptance not reconstructed here',
        'Preserve reported alpha observable; event normalization unresolved; DOI 10.1007/s10894-011-9473-5',
        'Third-party source rights not independently qualified; repository license does not relicense data')
    registry=SourceRegistry({}); registry.register(src)
    rows=import_csv(raw,src,'Spraker2012:target-thickness')
    reconciliation=reconcile_x4(args.exfor.read_bytes(),rows)
    report=experiments()
    suite=unittest.defaultTestLoader.discover(str(Path(__file__).parent),pattern='test_slice.py')
    log=io.StringIO(); result=unittest.TextTestRunner(stream=log,verbosity=2).run(suite)
    files={'normalized_observations.json':strict_json(rows),
        'observable_covariance.json':strict_json({'units':'barn^2','conditional_on':'reported incident energies',
          'assumptions':'independent statistical standard deviations; shared linear unit-variance target nuisance; energy uncertainty not propagated',
          'matrix':covariance(rows).tolist()}),
        'identifiability_receipt.json':strict_json(report),
        'test_log.txt':log.getvalue()}
    for name,body in files.items():
        (args.out/name).write_text(body)
    receipt={'status':'PASS' if result.wasSuccessful() else 'FAIL',
        'scope':'A1/A2 prototype and exploratory linear identifiability only',
        'authorization':'Project lead explicitly authorized limited v0.3 scope in conversation; no merge/freeze authorization',
        'source_reconciliation':reconciliation,'tests_run':result.testsRun,
        'failures':len(result.failures),'errors':len(result.errors),
        'environment':{'python':platform.python_version(),'numpy':np.__version__},
        'inputs':{'csv_sha256':CSV_HASH,'exfor_sha256':X4_HASH,
          'exfor_url':'https://github.com/IAEA-NDS/exfor_master/blob/main/exforall/C29/C2973.x4',
          'exfor_identity_note':'URL is a locator; SHA-256 pins the required bytes'},
        'code_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(Path(__file__).parent.glob('*.py'))},
        'output_sha256':{n:hashlib.sha256((args.out/n).read_bytes()).hexdigest() for n in files},
        'limits':['No general EXFOR parser','No LAB/CM transform','No alpha/event conversion',
          'No physical detector/transport model','No empirical noise calibration','No material or spectral control validation',
          'Energy errors preserved but not propagated through an errors-in-variables likelihood',
          'Cross-group nuisance correlations require a future explicit joint covariance model',
          'Campaign holdouts and independent nonlinear oracle remain future qualification gates']}
    (args.out/'run_receipt.json').write_text(strict_json(receipt))
    print(strict_json({'status':receipt['status'],'tests_run':result.testsRun,'source_reconciliation':reconciliation,
      'nominal_coverage':report['nominal_95pct_coverage'],'misspecified_coverage':report['misspecified_95pct_coverage'],
      'weak_parameter_sd':report['narrow_design']['scaled_parameter_sd'],'wide_parameter_sd':report['wide_design']['scaled_parameter_sd']}))
    raise SystemExit(0 if result.wasSuccessful() else 1)


if __name__=='__main__': main()
