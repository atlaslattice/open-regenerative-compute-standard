import copy
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from stellar_forge_reference.runner import run,read_json
from stellar_forge_reference.vendor import observables as o

ROOT=Path(__file__).resolve().parents[1]
CONFIG=ROOT/'examples/pb11_reference.json'
class Integration(unittest.TestCase):
    def scenario(self,change=None):
        temp=tempfile.TemporaryDirectory();self.addCleanup(temp.cleanup);p=Path(temp.name)
        c=read_json(CONFIG)
        if change:change(c)
        f=p/'config.json';f.write_text(json.dumps(c));return f,p/'out'
    def test_connected_pipeline_and_independent_oracles(self):
        f,p=self.scenario();r=run(f,p)
        self.assertAlmostEqual(r['transmission'][0]['output_energy_MeV'],.6)
        self.assertAlmostEqual(r['transmission'][1]['output_energy_MeV'],1.2)
        self.assertEqual(r['detector']['total_expected_counts'],[78.,54.])
        self.assertAlmostEqual(r['detector']['undetected_expected_counts'],25)
        self.assertEqual(r['synthetic_identifiability']['joint_rank']['rank'],3)
        self.assertEqual(r['synthetic_identifiability']['with_calibration_rank']['rank'],5)
        self.assertEqual(r['energy_scenario']['net_electric_J'],-100)
        self.assertIsNone(r['capital']['total_installed_capex_USD'])
        self.assertIsNone(r['economic_scenario']['potential_net_USD'])
    def test_manifest_hashes_and_report(self):
        f,p=self.scenario();run(f,p);m=read_json(p/'MANIFEST.json')
        for name,h in m['output_sha256'].items():self.assertEqual(hashlib.sha256((p/name).read_bytes()).hexdigest(),h)
        self.assertIn('No calibrated', (p/'REPORT.md').read_text())
        self.assertTrue((p/'transmission.svg').read_text().startswith('<svg'))
    def test_repeat_deterministic_results(self):
        f,p=self.scenario();run(f,p);q=p.parent/'other';run(f,q)
        self.assertEqual((p/'RESULTS.json').read_bytes(),(q/'RESULTS.json').read_bytes())
    def test_no_overwrite(self):
        f,p=self.scenario();run(f,p)
        with self.assertRaises(FileExistsError):run(f,p)
    def test_refuses_physical_mode_and_preserves_failure(self):
        f,p=self.scenario(lambda c:c.update(run_class='CALIBRATED'))
        with self.assertRaises(ValueError):run(f,p)
        self.assertTrue((p/'FAILURE.json').exists())
    def test_unknown_fields_refused(self):
        f,p=self.scenario(lambda c:c.update(assumed_gain=2))
        with self.assertRaises(ValueError):run(f,p)
    def test_synthetic_material_guard(self):
        def change(c):c['ranges'][0]['material_id']='BN'
        f,p=self.scenario(change)
        with self.assertRaises(ValueError):run(f,p)
    def test_domain_mutation_detected(self):
        def change(c):c['protons'][0]['energy_MeV']=100
        f,p=self.scenario(change)
        with self.assertRaises(ValueError):run(f,p)
    def test_stopped_alphas_do_not_become_counts(self):
        def change(c):
            c['layers'][0]['areal_mass_g_cm2']=10
        f,p=self.scenario(change);r=run(f,p)
        self.assertEqual(r['detector']['signal_expected_counts'],[0,0])
        self.assertEqual(r['detector']['total_expected_counts'],[3,4])
        self.assertEqual(r['stopped_alpha_fixture_weight'],150)
    def test_detector_overflow_bins_refused(self):
        def change(c):c['alpha_fixture'][0]['energy_MeV']=4;c['detector']['true_edges_mev'][-1]=3
        f,p=self.scenario(change)
        with self.assertRaises(ValueError):run(f,p)
    def test_alpha_partition_guard(self):
        def change(c):c['energy_scenario']['alpha_self_heat_fraction']=.8
        f,p=self.scenario(change)
        with self.assertRaises(ValueError):run(f,p)
    def test_drive_off_guard(self):
        f,p=self.scenario(lambda c:c.update(operating_track='STARTUP_THEN_BURN_HYPOTHESIS'))
        with self.assertRaises(ValueError):run(f,p)
    def test_missing_zero_distinct(self):
        f,p=self.scenario();r=run(f,p)
        self.assertEqual(r['missing_vs_zero_fixture'][0]['value'],Decimal(0))
        self.assertIsNone(r['missing_vs_zero_fixture'][1]['value'])
        self.assertIsNone(r['zero_ratio_fixture']['value'])
    def test_duplicate_json_and_nonfinite_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            f=Path(tmp)/'bad.json'
            for s in ['{"a":1,"a":2}','{"a":NaN}']:
                f.write_text(s)
                with self.assertRaises(ValueError):read_json(f)
    def test_importer_integration_and_quantity_guard(self):
        f,p=self.scenario();c=read_json(f)
        raw=b'E_lab_MeV,sigma_b,stat_err_b,sys_target_thickness_fraction,exfor_subentry,reaction,source_DOI,dE_lab_MeV\n0.675,1,0.1,0.036,C2973002,"11B(p,a)8Be",fixture,0.002\n0.7,2,0.2,0.036,C2973002,"11B(p,a)8Be",fixture,0.003\n'
        (f.parent/'fixture.csv').write_bytes(raw)
        c['source_audit']={'raw_csv_path':'fixture.csv','sha256':hashlib.sha256(raw).hexdigest()};f.write_text(json.dumps(c))
        r=run(f,p);self.assertEqual(r['source_audit']['rows'],2)
        cov=read_json(p/'SOURCE_COVARIANCE.json');self.assertAlmostEqual(cov[0][1],.036*.072)
        obs=read_json(p/'SOURCE_OBSERVATIONS.json');self.assertEqual(obs[0]['energy_unc_mev'],'0.002')
        source=o.Source('fixture','fixture','0'*64,'fixture','reaction',o.Quantity.REPORTED_ALPHA_CROSS_SECTION,o.Frame.LAB,'window','reported','unknown')
        obj=o.Observation('fixture:1',source,Decimal(1),None,'not_reported',Decimal(1),Decimal('.1'),(),('fixture',))
        with self.assertRaises(ValueError):obj.require_quantity(o.Quantity.FUSION_EVENT_CROSS_SECTION)
    def test_duplicate_shared_asset_refused(self):
        def change(c):c['components']*=2
        f,p=self.scenario(change)
        with self.assertRaises(ValueError):run(f,p)
    def test_cli(self):
        f,p=self.scenario();r=subprocess.run([sys.executable,'-m','stellar_forge_reference.cli','run',str(f),'--out',str(p)],capture_output=True,text=True)
        self.assertEqual(r.returncode,0,r.stderr);self.assertIn('physical prediction BLOCKED',r.stdout)
if __name__=='__main__':unittest.main()
