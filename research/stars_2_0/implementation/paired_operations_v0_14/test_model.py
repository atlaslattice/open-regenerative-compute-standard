import io,json,math,pickle,tempfile,unittest
from pathlib import Path
from model import attempt_accounting,overlap_probability,tail_models,full_detector_response
from recover_stability import NumericUnpickler
from run import run

ROOT=Path(__file__).parent

class AccountingTests(unittest.TestCase):
    def test_all_attempt_denominator_and_nonzero_failed_output(self):
        a=attempt_accounting(ready_probability=.8,fire_given_ready=.5,physical_success_given_fired=.25,failed_fired_energy_fraction=.2,success_energy_J=10)
        self.assertAlmostEqual(a['physical_success_per_attempt'],.1)
        self.assertAlmostEqual(a['energy_J_per_attempt'],1.6)
        self.assertAlmostEqual(a['physical_success_per_attempt']+a['unsuccessful_fired_per_attempt']+a['not_fired_per_attempt'],1)

    def test_nuclear_energy_not_assumed_electricity(self):
        a=attempt_accounting(ready_probability=1,fire_given_ready=1,physical_success_given_fired=1,success_energy_J=10)
        self.assertIsNone(a['load_J_per_attempt']);self.assertIsNone(a['net_electrical_J_per_attempt'])

    def test_abort_keeps_preparation_cost(self):
        a=attempt_accounting(ready_probability=0,fire_given_ready=1,physical_success_given_fired=1,success_energy_J=10,prep_wall_J=2,laser_wall_J_per_fired=10,allocated_aux_wall_J=3,load_J_per_success=4,load_J_per_failed_fired=0)
        self.assertEqual(a['energy_J_per_attempt'],0);self.assertEqual(a['wall_J_per_attempt'],5);self.assertEqual(a['net_electrical_J_per_attempt'],-5)

    def test_missing_wall_energy_not_zero(self):
        a=attempt_accounting(ready_probability=1,fire_given_ready=1,physical_success_given_fired=1,prep_wall_J=1)
        self.assertIsNone(a['wall_J_per_attempt']);self.assertEqual(a['known_wall_subtotal_J_per_attempt'],1)

    def test_narrowing_can_harm_misaligned_mean(self):
        self.assertLess(overlap_probability(.5,1,bias=2),overlap_probability(1,1,bias=2))

    def test_gaussian_limit_and_wide_window(self):
        self.assertEqual(overlap_probability(0,1),1)
        self.assertEqual(overlap_probability(0,1,2),0)
        self.assertAlmostEqual(overlap_probability(1,100),1)
        self.assertAlmostEqual(overlap_probability(1,1),.6826894921370859)

    def test_variance_alone_does_not_force_mean_gain(self):
        a=attempt_accounting(ready_probability=1,fire_given_ready=1,physical_success_given_fired=.4,failed_fired_energy_fraction=1)
        b=attempt_accounting(ready_probability=1,fire_given_ready=1,physical_success_given_fired=.9,failed_fired_energy_fraction=1)
        self.assertEqual(a['normalized_energy_per_attempt'],b['normalized_energy_per_attempt'])

    def test_no_firing_means_no_nuclear_energy(self):
        a=attempt_accounting(ready_probability=1,fire_given_ready=0,physical_success_given_fired=1,success_energy_J=10)
        self.assertEqual(a['energy_J_per_attempt'],0)

    def test_bad_probabilities_rejected(self):
        for r in [-.1,1.1,float('nan'),True]:
            with self.assertRaises(ValueError):attempt_accounting(ready_probability=r,fire_given_ready=1,physical_success_given_fired=1)

    def test_tail_anchor_reproduction_and_coverage(self):
        for y in tail_models(2.25).values():self.assertAlmostEqual(y,.639)
        for y in tail_models(4.52).values():self.assertAlmostEqual(y,.611)
        with self.assertRaises(ValueError):tail_models(10)
        with self.assertRaises(ValueError):full_detector_response(7.5)

    def test_pickle_global_rejected(self):
        with self.assertRaises(ValueError):NumericUnpickler(io.BytesIO(b'cos\nsystem\n.')).load()

    def test_no_overwrite_and_repeat(self):
        p=ROOT/'receipts/stability001/STABILITY_DATA.json'
        with tempfile.TemporaryDirectory() as tmp:
            a=Path(tmp)/'a';b=Path(tmp)/'b';run(p,a);run(p,b)
            self.assertEqual((a/'RESULTS.json').read_bytes(),(b/'RESULTS.json').read_bytes())
            with self.assertRaises(FileExistsError):run(p,a)

    def test_recovered_statistics_match_published_notebook_rounding(self):
        s=json.loads((ROOT/'receipts/stability001/STABILITY_DATA.json').read_text())['summary']
        for key,expected,decimals in [('peak_dose_mean_Gy',40.7,1),('peak_dose_population_SD_Gy',4.6,1),('minor_divergence_mean_mrad',23.48,2),('minor_divergence_population_SD_mrad',2.35,2),('major_divergence_mean_mrad',40.,2),('major_divergence_population_SD_mrad',3.16,2)]:self.assertEqual(round(s[key],decimals),expected)
        self.assertEqual(s['dose_at_or_below_threshold_in_window'],17)
        self.assertIsNone(s['all_preparation_attempt_success_probability'])

if __name__=='__main__':unittest.main(verbosity=2)
