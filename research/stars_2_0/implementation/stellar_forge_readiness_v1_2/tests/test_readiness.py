import copy,json,subprocess,sys,tempfile,unittest
from pathlib import Path
from stellar_forge_readiness.readiness import evaluate,batch
ROOT=Path(__file__).resolve().parents[1]
class Readiness(unittest.TestCase):
    def fixture(self):return json.loads((ROOT/'examples/readiness_attempts.json').read_text())['attempts'][0]
    def test_ready_time_and_independent_energy(self):
        r=evaluate(self.fixture());self.assertEqual(r['status'],'READY_IN_TRACE');self.assertEqual(r['first_qualifying_sample_s'],2);self.assertEqual(r['first_confirmed_readiness_s'],3);self.assertAlmostEqual(r['driver_wall_energy_J'],.6)
    def test_all_attempts_kept(self):
        a=json.loads((ROOT/'examples/readiness_attempts.json').read_text())['attempts'];r=batch(a)
        self.assertEqual(r['summary']['all_attempts'],4);self.assertEqual(r['summary']['ready_attempts'],2);self.assertEqual(r['summary']['status_counts']['TIMEOUT_NOT_READY'],1);self.assertEqual(r['summary']['status_counts']['ABORTED'],1)
    def test_missing_metric_resets_hold(self):
        a=self.fixture();a['observations'][5]['metrics']['envelope_fraction']=None;r=evaluate(a);self.assertEqual(r['first_confirmed_readiness_s'],4)
    def test_dropouts_reset_hold(self):
        a=self.fixture();del a['observations'][5];r=evaluate(a);self.assertEqual(r['first_confirmed_readiness_s'],4)
    def test_abort_priority_same_time(self):
        a=self.fixture();a.update(abort_at_s=3,abort_reason='fixture abort');r=evaluate(a);self.assertEqual(r['status'],'ABORTED');self.assertEqual(r['attempt_end_s'],3)
    def test_incomplete_trace(self):
        a=self.fixture();a['observations']=a['observations'][:3];r=evaluate(a);self.assertEqual(r['status'],'INCOMPLETE_TRACE');self.assertIsNone(r['first_confirmed_readiness_s'])
    def test_fixed_duration_does_not_pretend_ready(self):
        a=self.fixture();a.update(mode='FIXED_DURATION',fixed_duration_s=1);r=evaluate(a);self.assertEqual(r['status'],'FIXED_WINDOW_COMPLETED');self.assertIsNone(r['first_confirmed_readiness_s'])
    def test_long_window_not_artificially_saturated(self):
        a=self.fixture();a.update(timeout_s=60,hold_s=2,max_sample_gap_s=1.1)
        a['observations']=[{'time_s':i,'metrics':{'envelope_fraction':1 if i>=40 else .5,'temperature_C':20},'driver_power_W':.2} for i in range(61)]
        r=evaluate(a);self.assertEqual(r['first_confirmed_readiness_s'],42)
    def test_bad_time_and_power(self):
        for change in ['timestamp','power']:
            a=self.fixture()
            if change=='timestamp':a['observations'][1]['time_s']=0
            else:a['observations'][1]['driver_power_W']=-1
            with self.assertRaises(ValueError):evaluate(a)
    def test_invalid_sensor_and_units(self):
        a=self.fixture();a['criteria'][0]['sensor_id']='absent'
        with self.assertRaises(ValueError):evaluate(a)
    def test_duplicate_attempt_identity(self):
        with self.assertRaises(ValueError):batch([self.fixture(),self.fixture()])
    def test_outcomes_not_inferred(self):
        r=evaluate(self.fixture());self.assertIsNone(r['subsequent_outcomes']['fusion_events']);self.assertEqual(r['laser_trigger'],'NONE_NO_HARDWARE_INTERFACE')
    def test_cli_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as t:
            cmd=[sys.executable,'-m','stellar_forge_readiness.cli','evaluate',str(ROOT/'examples/readiness_attempts.json'),'--out',str(Path(t)/'run')]
            r=subprocess.run(cmd,capture_output=True,text=True);self.assertEqual(r.returncode,0,r.stderr)
            logs=(Path(t)/'run/ATTEMPTS.jsonl').read_text().splitlines();self.assertEqual(len(logs),4)
            self.assertNotEqual(subprocess.run(cmd,capture_output=True).returncode,0)
if __name__=='__main__':unittest.main()
