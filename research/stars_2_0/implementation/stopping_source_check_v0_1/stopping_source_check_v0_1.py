"""Strict candidate-source audit; mirror identity is not primary verification.
External inputs are not vendored or relicensed. Output directory must be new.
"""
import argparse
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
from decimal import Decimal as D
import platform
import sys
import unittest

AL_HASH='3fe6459ec4abde6052bcb63f427ea856bbc35dd8506014191145b4eb9253db5e'
B_HASH='ab93971d116d0ef37ce64fa0f83153daf771ab46eba98ee72510dd84b16a7c97'
TRANSPORT_HASH='f3a43e6781da00bdc47b9f31605817e11fe28a5ae12149538f2787e5a8d6439e'
PIN='83e2babc0612dbac733705c02973418ef87e210e'


def check_hash(raw,expected):
    if hashlib.sha256(raw).hexdigest()!=expected:raise ValueError('Source hash mismatch')


def rounding_radius(d):
    return D(5)*(D(10)**(d.as_tuple().exponent-1))


def parse_pstar_aluminum(raw,expected_hash=AL_HASH):
    check_hash(raw,expected_hash)
    lines=raw.decode('ascii').splitlines()
    if lines[0]!='PSTAR: Stopping Powers and Range Tables for Protons' or lines[2].strip()!='ALUMINUM':
        raise ValueError('Wrong projectile/table/material')
    if lines[4].split()!=['Kinetic','Electron.','Nuclear','Total','CSDA','Projected','Detour']:
        raise ValueError('Column semantics changed')
    if lines[6].split()!=['MeV','MeV','cm2/g','MeV','cm2/g','MeV','cm2/g','g/cm2','g/cm2']:
        raise ValueError('Source unit line changed')
    rows=[]
    for line in lines[8:]:
        if not line.strip():continue
        fields=line.split()
        if len(fields)!=7:raise ValueError('Expected seven source columns')
        row=tuple(D(x) for x in fields)
        if any(not x.is_finite() or x<=0 for x in row):raise ValueError('Invalid positive source row')
        # Check printed-column closure against a bound derived from decimal rounding.
        se,sn,st=row[1:4]
        if abs(se+sn-st)>sum(rounding_radius(x) for x in (se,sn,st)):
            raise ValueError('Stopping components exceed source rounding budget')
        rc,rp,det=row[4:]
        bound=rounding_radius(rp)+abs(det)*rounding_radius(rc)+abs(rc)*rounding_radius(det)+rounding_radius(rc)*rounding_radius(det)
        if rp>rc or det>1 or abs(rp-det*rc)>bound:
            raise ValueError('Projected/CSDA/detour mismatch')
        rows.append(row)
    if len(rows)<2 or any(b[0]<=a[0] or b[4]<=a[4] for a,b in zip(rows,rows[1:])):
        raise ValueError('Nonmonotone or empty source table')
    return rows


def quarantine_boron(raw):
    check_hash(raw,B_HASH)
    records=[]
    for line in raw.decode('ascii').splitlines():
        fields=line.split()
        if len(fields)!=3 or fields[2] not in 'ABCD' or len(fields[2])!=1:
            raise ValueError('Unknown mirror row format')
        x,y=map(D,fields[:2])
        if not x.is_finite() or not y.is_finite() or x<=0 or y<=0:raise ValueError('Invalid mirror number')
        records.append((x,y,fields[2]))
    return {'rows':len(records),'groups':{g:sum(r[2]==g for r in records) for g in 'ABCD'},
        'source_sha256':B_HASH,'units':'UNRESOLVED_FROM_HEADERLESS_FILE',
        'group_reference_mapping':'UNRESOLVED','status':'QUARANTINED_NOT_TRANSPORT_INPUT',
        'prohibited_promotions':['not total stopping','not CSDA range','not BN','not an independent calibrated benchmark']}


def interpolate(x,rows,col):
    if x<float(rows[0][0]) or x>float(rows[-1][0]):raise ValueError('No extrapolation')
    for a,b in zip(rows,rows[1:]):
        lo,hi=float(a[0]),float(b[0])
        if lo<=x<=hi:return float(a[col])+(x-lo)*(float(b[col])-float(a[col]))/(hi-lo)
    raise ValueError('Interpolation segment missing')


def integrate_reciprocal_stopping(low,high,rows):
    """Exact integral for a separately defined piecewise-linear total S(E).
    This does not reuse the range column or range inversion kernel.
    """
    if low<rows[0][0] or high>rows[-1][0] or low>high:raise ValueError('Invalid integration domain')
    knots=[low]+[float(r[0]) for r in rows if low<r[0]<high]+[high]
    values=[]
    for lo,hi in zip(knots,knots[1:]):
        s0,s1=interpolate(lo,rows,3),interpolate(hi,rows,3)
        if hi==lo:continue
        slope=(s1-s0)/(hi-lo)
        values.append((hi-lo)/s0 if slope==0 else math.log(s1/s0)/slope)
    return math.fsum(values)


def stopping_integral_residual(E,path,rows):
    # These comparisons deliberately stay above 1 keV; no end-of-range tail supplied.
    lo=float(rows[0][0]);hi=E
    if path>integrate_reciprocal_stopping(lo,E,rows):raise ValueError('Below available stopping domain')
    for _ in range(60):
        mid=(lo+hi)/2
        if integrate_reciprocal_stopping(mid,E,rows)>path:lo=mid
        else:hi=mid
    return (lo+hi)/2


class AdapterTests(unittest.TestCase):
    def test_hash_mutation_refused(self):
        with self.assertRaises(ValueError):check_hash(b'changed',AL_HASH)

    def test_independent_integral_constant_stopping(self):
        rows=[tuple(map(D,map(str,r))) for r in [(1,2,1,3,1,1,1),(2,2,1,3,2,2,1)]]
        self.assertAlmostEqual(integrate_reciprocal_stopping(1,2,rows),1/3)

    def test_independent_integral_linear_stopping(self):
        rows=[tuple(map(D,map(str,r))) for r in [(1,1,1,2,1,1,1),(2,3,1,4,2,2,1)]]
        self.assertAlmostEqual(integrate_reciprocal_stopping(1,2,rows),math.log(2)/2)

    def fixture(self):
        # Artificial rows with source-style headers; not physical data.
        return ('PSTAR: Stopping Powers and Range Tables for Protons\n\nALUMINUM\n\n'
            'Kinetic Electron. Nuclear Total CSDA Projected Detour\n'
            'Energy Stp. Pow. Stp. Pow. Stp. Pow. Range Range Factor\n'
            'MeV MeV cm2/g MeV cm2/g MeV cm2/g g/cm2 g/cm2\n\n'
            '1.000 2.000 1.000 3.000 1.000 0.500 0.500\n'
            '2.000 2.000 1.000 3.000 2.000 1.000 0.500\n').encode()

    def test_semantic_mutations_with_recomputed_hash(self):
        raw=self.fixture()
        self.assertEqual(len(parse_pstar_aluminum(raw,hashlib.sha256(raw).hexdigest())),2)
        for bad in (raw.replace(b'ALUMINUM',b'BORON'),raw.replace(b'for Protons',b'for Alphas'),
                    raw.replace(b'MeV MeV cm2/g',b'keV MeV cm2/g'),
                    raw.replace(b'CSDA Projected',b'Projected CSDA')):
            with self.subTest(bad=bad),self.assertRaises(ValueError):
                parse_pstar_aluminum(bad,hashlib.sha256(bad).hexdigest())

    def test_source_rounding_semantic_mutations(self):
        raw=self.fixture()
        for bad in (raw.replace(b'3.000',b'4.000'),raw.replace(b'0.500 0.500',b'0.600 0.500')):
            with self.subTest(bad=bad),self.assertRaises(ValueError):
                parse_pstar_aluminum(bad,hashlib.sha256(bad).hexdigest())

    def test_rounding_budget(self):
        self.assertEqual(rounding_radius(D('1.720E+02')),D('.05'))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--al-mirror',type=Path,required=True)
    ap.add_argument('--b-mirror',type=Path,required=True)
    ap.add_argument('--transport-file',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();args.out.mkdir(parents=True,exist_ok=False)
    al=args.al_mirror.read_bytes();boron=args.b_mirror.read_bytes()
    rows=parse_pstar_aluminum(al);b_quarantine=quarantine_boron(boron)
    check_hash(args.transport_file.read_bytes(),TRANSPORT_HASH)
    spec=importlib.util.spec_from_file_location('g0b_reference',args.transport_file)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
    # Preserve source bytes and selected column identity in input provenance.
    table=module.RangeTable('PSTAR_AL_MIRROR_CANDIDATE','ALUMINUM_REFERENCE','proton',AL_HASH,
        'SOURCE_TRACED',tuple(float(r[0]) for r in rows),tuple(float(r[4]) for r in rows))
    cases=[]
    for E in (.5,.675,1.,2.):
        for path in (.0001,.0005,.001):
            r=module.transmit_proton(E,1,[module.Layer('foil','ALUMINUM_REFERENCE',path)],{('ALUMINUM_REFERENCE','proton'):table})
            independent=stopping_integral_residual(E,path,rows)
            cases.append({'input_energy_MeV':E,'areal_mass_g_cm2':path,
                'range_column_output_MeV':r['output_energy_MeV'],'integrated_stopping_output_MeV':independent,
                'absolute_difference_MeV':abs(r['output_energy_MeV']-independent),
                'primary_closure_residual_MeV':r['closure_residual_MeV']})
    suite=unittest.defaultTestLoader.loadTestsFromTestCase(AdapterTests)
    log=io.StringIO();test=unittest.TextTestRunner(stream=log,verbosity=2).run(suite)
    args.out.joinpath('test_log.txt').write_text(log.getvalue())
    source_manifest={'repository':'dedx-erpa/dedx','revision':PIN,
        'al_path':'data/Al/pstar.txt','boron_path':'data/iaea/B.txt',
        'mirror_identity':'Pinned GitHub bytes; primary NIST/IAEA byte identity not established',
        'al_sha256':AL_HASH,'boron_sha256':B_HASH,'source_class':'MIRROR_CANDIDATE_NOT_CALIBRATED',
        'raw_data_distribution':'External inputs only; no upstream raw files vendored or relicensed'}
    receipt={'status':'SOURCE_ADAPTER_CHECKS_PASS' if test.wasSuccessful() else 'FAIL',
        'physical_validation':'NOT_RUN_NO_INDEPENDENT_TRANSMISSION_DATA',
        'al_source_rows':len(rows),'al_energy_domain_MeV':[str(rows[0][0]),str(rows[-1][0])],
        'al_source_column_definition':'energy column 0; total stopping column 3; CSDA column 4; projected range column 5 retained separately',
        'source_rounding_checks':'Every row: electronic+nuclear=total and projected=detour*CSDA within decimal rounding bounds',
        'tests_run':test.testsRun,'source_manifest':source_manifest,'boron_quarantine':b_quarantine,
        'comparison_scope':'Same-source numerical consistency under two interpolation formulations; not independent physical validation',
        'aluminum_cases':cases,'max_absolute_formulation_difference_MeV':max(c['absolute_difference_MeV'] for c in cases),
        'transport_sha256':TRANSPORT_HASH,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'test_log_sha256':hashlib.sha256(args.out.joinpath('test_log.txt').read_bytes()).hexdigest(),
        'python':platform.python_version(),'randomness':'none',
        'calibration_threshold':None,'interpretation':'Formulation differences are recorded, not fitted away; no empirical acceptance implied'}
    args.out.joinpath('SOURCE_CHECK_RECEIPT_v0_1.json').write_text(json.dumps(receipt,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:receipt[k] for k in ['status','al_source_rows','boron_quarantine','max_absolute_formulation_difference_MeV','physical_validation']},indent=2))
    raise SystemExit(0 if test.wasSuccessful() else 1)


if __name__=='__main__':main()
