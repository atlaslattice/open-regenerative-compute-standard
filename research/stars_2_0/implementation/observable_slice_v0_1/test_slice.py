import hashlib
import json
import unittest
from dataclasses import replace
from decimal import Decimal as D
import numpy as np
from observables import Source, SourceRegistry, Quantity, Frame, import_csv, covariance, strict_json, measured_outcome, ratio
from identifiability import diagnose, fit, experiments

HEADER = 'E_lab_MeV,sigma_b,stat_err_b,sys_target_thickness_fraction,exfor_subentry,reaction,source_DOI'
BODY = '0.675,1.0,0.1,0.036,SYNTHETIC,synthetic,synthetic-not-a-DOI'


def source(raw):
    return Source('SYNTHETIC','synthetic-independent-fixture',hashlib.sha256(raw).hexdigest(),
        'synthetic://fixture','synthetic',Quantity.REPORTED_ALPHA_CROSS_SECTION,Frame.LAB,
        'synthetic acceptance only','not physical data','synthetic fixture under repository license')


def fixture(de=None, second=False):
    raw = (HEADER + (',dE_lab_MeV' if de is not None else '') + '\n' + BODY +
           (','+str(de) if de is not None else '') + '\n').encode()
    if second:
        raw += (BODY.replace('0.675','0.700') + (','+str(de) if de is not None else '') + '\n').encode()
    return raw, source(raw)


class ObservableTests(unittest.TestCase):
    def test_energy_uncertainty_and_decimal_roundtrip(self):
        raw,s = fixture('0.0012300')
        rows = import_csv(raw,s,'target')
        self.assertEqual(rows[0].energy_unc_mev,D('0.0012300'))
        obj=json.loads(strict_json(rows))
        self.assertEqual(obj[0]['energy_unc_mev'],'0.0012300')
        self.assertEqual(obj[0]['source']['frame'],'LAB')

    def test_unknown_is_not_zero(self):
        raw,s=fixture(); a=import_csv(raw,s,'target')[0]
        raw,s=fixture('0'); b=import_csv(raw,s,'target')[0]
        self.assertIsNone(a.energy_unc_mev)
        self.assertEqual(a.energy_unc_status,'not_reported')
        self.assertEqual(b.energy_unc_mev,D(0))
        self.assertEqual(b.energy_unc_status,'reported')

    def test_event_relabel_and_frame_conversion_blocked(self):
        raw,s=fixture()
        with self.assertRaises(ValueError):
            import_csv(raw,replace(s,quantity=Quantity.FUSION_EVENT_CROSS_SECTION),'target')
        with self.assertRaises(ValueError):
            import_csv(raw,replace(s,frame=Frame.CM),'target')
        row=import_csv(raw,s,'target')[0]
        with self.assertRaises(ValueError):
            row.require_quantity(Quantity.FUSION_EVENT_CROSS_SECTION)

    def test_hash_mutation_detected(self):
        raw,s=fixture()
        with self.assertRaises(ValueError):
            import_csv(raw.replace(b'1.0',b'2.0'),s,'target')

    def test_schema_mutations_and_invalid_numbers(self):
        raw,_=fixture()
        for bad in (raw.replace(b'E_lab_MeV',b'E_lab_keV'),
                    raw.replace(b'stat_err_b',b'stat_err_mb'),
                    raw.replace(b'0.675',b'NaN'), raw.replace(b'0.675',b'-1'),
                    raw.replace(b'0.675',b'Infinity'),
                    (HEADER+',unexpected\n'+BODY+',1\n').encode()):
            with self.subTest(raw=bad), self.assertRaises(ValueError):
                import_csv(bad,source(bad),'target')

    def test_shared_covariance_does_not_average_away(self):
        raw,s=fixture(second=True)
        rows=import_csv(raw,s,'target')
        C=covariance(rows)
        self.assertAlmostEqual(C[0,1],.036**2)
        w=np.array([.5,.5])
        self.assertAlmostEqual(w@C@w,.1**2/2+.036**2)
        # A deliberate wrong implementation diagonalizes the shared nuisance.
        wrong=np.diag(np.diag(C))
        self.assertGreater(abs(w@C@w-w@wrong@w),1e-4)

    def test_shared_group_across_different_sources(self):
        raw,s=fixture()
        a=import_csv(raw,s,'calibration')[0]
        b=replace(a,observation_id='OTHER:1',source=replace(s,source_id='OTHER',evidence_id='independent'))
        self.assertAlmostEqual(covariance([a,b])[0,1],.036**2)
        independent=replace(b,common_loadings_b=(('other-calibration',D('.036')),))
        self.assertEqual(covariance([a,independent])[0,1],0)

    def test_duplicate_evidence_and_registry_conflicts(self):
        raw,s=fixture(); rows=import_csv(raw,s,'target')
        with self.assertRaises(ValueError): covariance(rows+rows)
        alias=replace(rows[0],source=replace(s,source_id='ALIAS'),observation_id='ALIAS:1')
        with self.assertRaises(ValueError): covariance(rows+[alias])
        registry=SourceRegistry({}); self.assertEqual(registry.register(s),[])
        self.assertEqual(registry.register(alias.source),['SYNTHETIC'])
        with self.assertRaises(ValueError): registry.register(replace(s,sha256='0'*64))

    def test_missing_censored_zero_and_undefined_ratios(self):
        self.assertEqual(measured_outcome('measured','0')['value'],D(0))
        for status in ('missing','censored','invalid'):
            self.assertIsNone(measured_outcome(status,reason='fixture')['value'])
            with self.assertRaises(ValueError): measured_outcome(status,'0','fixture')
        self.assertEqual(json.loads(strict_json(ratio(0,0))),{'value':None,'reason':'zero_denominator'})
        self.assertEqual(ratio(0,1)['value'],D(0))
        with self.assertRaises(ValueError): strict_json({'invalid':float('nan')})


class IdentifiabilityTests(unittest.TestCase):
    def test_rank_does_not_imply_precision(self):
        x=np.linspace(-1,1,9); C=.01*np.eye(9)
        wide=diagnose(np.column_stack([np.ones(9),x]),C,[1,1])
        weak=diagnose(np.column_stack([np.ones(9),.001*x]),C,[1,1])
        self.assertEqual(wide['rank'],weak['rank'])
        self.assertAlmostEqual(weak['scaled_parameter_sd'][1]/wide['scaled_parameter_sd'][1],1000)

    def test_degenerate_and_underdetermined_refuse_unique_fit(self):
        for J in (np.ones((3,2)),np.array([[1.,0.,0.]])):
            C=np.eye(len(J)); scales=np.ones(J.shape[1])
            d=diagnose(J,C,scales)
            self.assertIsNone(d['condition_number'])
            self.assertTrue(d['null_scaled_directions'])
            with self.assertRaises(ValueError): fit(J,C,np.ones(len(J)),scales)

    def test_parameter_unit_change_preserves_whitened_spectrum(self):
        J=np.array([[1,0],[1,1],[1,2]],float)
        a=diagnose(J,np.eye(3),[1,1])
        b=diagnose(J*np.array([1,1000]),np.eye(3),[1,.001])
        np.testing.assert_allclose(a['singular_values'],b['singular_values'],rtol=1e-13)

    def test_observable_coordinate_change_preserves_fit(self):
        J=np.array([[1,0],[1,1],[1,2]],float); C=np.eye(3); y=np.array([1.,3.,4.])
        # Invertible change of observation units, with covariance transformed too.
        T=np.diag([2.,3.,4.])
        a=fit(J,C,y,[1,1]); b=fit(T@J,T@C@T.T,T@y,[1,1])
        np.testing.assert_allclose(a[0],b[0],atol=1e-13)
        np.testing.assert_allclose(a[1],b[1],atol=1e-13)

    def test_bad_covariance_rejected(self):
        for C in (np.zeros((2,2)),np.array([[1.,2.],[0.,1.]]),np.diag([1.,-1.])):
            with self.assertRaises(ValueError): diagnose(np.eye(2),C,[1,1])

    def test_independent_oracle_and_monte_carlo(self):
        r=experiments()
        self.assertLess(r['oracle_max_abs_error'],1e-12)
        self.assertLess(r['oracle_covariance_max_abs_error'],1e-12)
        # Prespecified broad stochastic sanity bounds, not experimental gates.
        np.testing.assert_array_less(np.abs(np.array(r['bias'])),5*np.array(r['bias_standard_error']))
        np.testing.assert_array_less(np.abs(np.array(r['nominal_95pct_coverage'])-.95),5*r['coverage_binomial_se'])


if __name__=='__main__':
    unittest.main(verbosity=2)
