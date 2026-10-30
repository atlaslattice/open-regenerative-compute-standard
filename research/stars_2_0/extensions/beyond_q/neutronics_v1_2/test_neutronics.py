"""Regression + actual recorded-run acceptance checks. No physics-validation claim."""
import unittest,json,math,tempfile
from pathlib import Path
from transport import case,build
from integrate import response,apply_responses
from fuelcycle.physics import dd_source,dt_events,reaction_ledger
from fuelcycle.model import simulate

ROOT=Path(__file__).resolve().parent

class Software(unittest.TestCase):
    def test_invalid_inputs(self):
        for args in [dict(li6=-1),dict(port_fraction=.9),dict(source='mixed'),dict(blanket_cm=0)]:
            with self.assertRaises(ValueError):case(**args)

    def test_source_event_normalization(self):
        dd=dd_source(20)
        self.assertAlmostEqual(dd['n_atoms_s']/dd['events_s'],.5)
        self.assertAlmostEqual(dt_events(1130)/dt_events(1),1130)

    def test_synthetic_response_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'result.json').write_text(json.dumps({'kind':'NOT A TRANSPORT RESULT'}))
            (p/'provenance.json').write_text('{}')
            with self.assertRaisesRegex(ValueError,'NOT A TRANSPORT RESULT'):response(p)

    def test_missing_statepoint_rejected(self):
        import shutil
        origin=ROOT/'outputs/runs/DT_Li0.075_cm90'
        if not origin.exists():self.skipTest('recorded run files not yet available')
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            for name in ['result.json','provenance.json']:shutil.copyfile(origin/name,p/name)
            with self.assertRaisesRegex(ValueError,'raw statepoint'):response(p)

    def test_changed_tally_rejected(self):
        import shutil,zipfile
        origin=ROOT/'outputs/runs/DT_Li0.075_cm90'
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)
            for f in origin.iterdir():
                if f.is_file():shutil.copyfile(f,p/f.name)
            with zipfile.ZipFile(ROOT/'outputs/raw_statepoints.zip') as z:
                (p/'statepoint.30.h5').write_bytes(z.read('DT_Li0.075_cm90/statepoint.30.h5'))
            r=json.loads((p/'result.json').read_text())
            r['tallies']['salt_T_tracklength:H3-production']['mean']+=.1
            (p/'result.json').write_text(json.dumps(r))
            with self.assertRaisesRegex(ValueError,'does not match raw statepoint'):response(p)

    def test_energy_ledger_boundaries(self):
        import csv
        rows=list(csv.DictReader((ROOT/'outputs/neutron_thermal_energy_ledger.csv').read_text().splitlines()))
        for r in rows:
            self.assertAlmostEqual(float(r['fusion_Q_J'])/(float(r['fusion_neutron_initial_J'])+float(r['fusion_charged_initial_J'])),1)
            self.assertEqual(r['deposited_heat_J'],'')
            self.assertEqual(r['net_electric_J'],'')

    def test_no_double_count_fusion_neutron_energy(self):
        e=reaction_ledger(100,50,20,30)
        self.assertAlmostEqual(e['fusion_j'],e['fusion_neutron_j']+e['fusion_charged_j'])
        self.assertEqual(e['net_electric_status'],'UNRESOLVED')

class RecordedRuns(unittest.TestCase):
    def setUp(self):
        self.runs={p.parent.name:json.loads(p.read_text()) for p in (ROOT/'outputs/runs').glob('*/result.json')}
    def test_actual_run_count_and_provenance(self):
        self.assertEqual(len(self.runs),44)
        self.assertTrue(all(r['kind']=='ACTUAL_OPENMC_TRANSPORT_IN_ASSUMED_GEOMETRY' and not r['physical_validation'] for r in self.runs.values()))
    def test_neutron_balances(self):
        for name,r in self.runs.items():
            self.assertTrue(r['particle_balance_pass'],name)
            self.assertLess(abs(r['neutron_balance_residual']),1e-8,name)
    def test_two_numerical_estimators(self):
        self.assertTrue(all(r['estimators_agree'] for r in self.runs.values()))
    def test_vacuum_analytic_particle_and_energy(self):
        for name in ('DD_vacuum','DT_vacuum'):
            r=self.runs[name];t=r['tallies']
            self.assertAlmostEqual(t['leakage:current']['mean'],1)
            self.assertEqual(t['global_balance:absorption']['mean'],0)
            self.assertEqual(t['global_T:H3-production']['mean'],0)
            self.assertEqual(t['global_heat:heating']['mean'],0)
            expected=2.45e6 if name.startswith('DD') else 14.1e6
            self.assertAlmostEqual(expected*t['leakage:current']['mean'],expected)
            self.assertAlmostEqual(t['probe_flux:flux']['mean'],r['case']['probe_cm'])
    def test_isotope_negative_controls(self):
        for source in ('DD','DT'):
            self.assertEqual(self.runs[source+'_Li6_zero']['tallies'].get('Li6_T:H3-production',{'mean':0})['mean'],0)
            self.assertEqual(self.runs[source+'_Li7_zero']['tallies'].get('Li7_T:H3-production',{'mean':0})['mean'],0)
            self.assertEqual(self.runs[source+'_A0_both_Li_zero']['tallies']['salt_T_tracklength:H3-production']['mean'],0)
        # Li-free shield can create nonrecoverable T in other nuclides.
        self.assertGreater(self.runs['DT_A0_both_Li_zero']['tallies']['global_T:H3-production']['mean'],0)
    def test_port_reduction_is_not_scalar_dilution(self):
        baseline=self.runs['DT_Li0.075_cm90']['tallies']['salt_T_tracklength:H3-production']['mean']
        port=self.runs['DT_port10']['tallies']['salt_T_tracklength:H3-production']['mean']
        self.assertLess(port,baseline)
        self.assertGreater(abs(port-.9*baseline),.02)
    def test_repeat_and_history_convergence(self):
        ref=self.runs['DT_Li0.075_cm90']['tallies']['salt_T_tracklength:H3-production']
        for name in ['DT_independent_seed','DT_more_histories']:
            alt=self.runs[name]['tallies']['salt_T_tracklength:H3-production']
            self.assertLessEqual(abs(ref['mean']-alt['mean']),3*(ref['se_bound']+alt['se_bound']))
        self.assertLess(self.runs['DT_more_histories']['tallies']['salt_T_tracklength:H3-production']['se_bound'],ref['se_bound'])
    def test_analytic_absorber_benchmark(self):
        r=json.loads((ROOT/'outputs/analytic_benchmark/benchmark_result.json').read_text())
        self.assertTrue(r['passes_4se']);self.assertLess(abs(r['particle_residual']),1e-12)
        self.assertLess(abs(r['source_energy_partition_residual_eV']),1e-6)

    def test_raw_statepoint_archive_hashes(self):
        import zipfile,hashlib
        p=ROOT/'outputs/raw_statepoints.zip'
        meta=json.loads((ROOT/'outputs/raw_archive_manifest.json').read_text())
        self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),meta['archive_sha256'])
        with zipfile.ZipFile(p) as z:
            for name,r in self.runs.items():
                data=z.read(f"{name}/statepoint.{r['case']['batches']}.h5")
                self.assertEqual(hashlib.sha256(data).hexdigest(),r['statepoint_sha256'])

    def test_integrated_results_remain_unqualified(self):
        import csv
        rows=list(csv.DictReader((ROOT/'outputs/integrated_cases.csv').read_text().splitlines()))
        self.assertEqual(len(rows),48)
        self.assertTrue(all(r['qualified_usable_surplus_kg']=='' for r in rows))
        self.assertTrue(all(abs(float(r['mass_residual_kg']))<1e-8 for r in rows))
        cold=[r for r in rows if r['condition']=='cold_start']
        self.assertTrue(all(float(r['unserved_burn_kg'])>0 for r in cold))

if __name__=='__main__':unittest.main()
