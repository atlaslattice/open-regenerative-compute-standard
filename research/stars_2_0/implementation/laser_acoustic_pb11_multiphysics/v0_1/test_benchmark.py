import copy
import json
import math
from pathlib import Path
import unittest
from benchmark import summarize, geometry_gaps, WALL_CATEGORIES


def shot(i, events=10, arm='REF_OFF'):
    return dict(shot_id=str(i), apparatus_id='SF_C_ORIGINAL_STARS_V0_1', arm=arm,
                campaign_id='verification_only', batch_id='fixture_batch',
                evidence_class='SYNTHETIC_FIXTURE', source_ref='test_benchmark.py',
                event_semantics='REALIZED_COUNT',
                fusion_events=events, alpha_birth_energy_J=None, alpha_escape_energy_J=None,
                detected_alpha_count=None, useful_electricity_J=0,
                elapsed_s=10, firing_time_error_s=None,
                wall_input_J={k:0 for k in WALL_CATEGORIES})


class TestAccounting(unittest.TestCase):
    def test_success_and_nonzero_failures(self):
        r=summarize([shot(0,20),shot(1,2)],10)[0]
        self.assertEqual(r['events_per_attempt'],11)
        self.assertEqual(r['success_fraction'],.5)
        self.assertEqual(r['events_per_unsuccessful_shot'],2)
        self.assertEqual(.5*20+.5*2,r['events_per_attempt'])

    def test_reliability_increases_unconditional_yield(self):
        a=summarize([shot(i,v) for i,v in enumerate([20,20,0,0])],10)[0]
        b=summarize([shot(i,v) for i,v in enumerate([20,20,20,0])],10)[0]
        self.assertEqual(a['events_per_success'],b['events_per_success'])
        self.assertEqual(a['events_per_attempt'],10)
        self.assertEqual(b['events_per_attempt'],15)

    def test_selection_can_look_better_and_reduce_yield(self):
        a=summarize([shot(i,v) for i,v in enumerate([20,20,20,0])],10)[0]
        b=summarize([shot(i,v) for i,v in enumerate([40,0,0,0])],10)[0]
        self.assertGreater(b['events_per_success'],a['events_per_success'])
        self.assertLess(b['events_per_attempt'],a['events_per_attempt'])

    def test_missing_is_not_zero(self):
        r=summarize([shot(0,20),shot(1,None)],10)[0]
        self.assertIsNone(r['events_per_attempt'])
        self.assertIsNone(r['success_fraction'])
        self.assertEqual(r['success_fraction_missing_data_bounds'],[.5,1])

    def test_zero_is_known(self):
        r=summarize([shot(0,0)],10)[0]
        self.assertEqual(r['events_per_attempt'],0)
        self.assertEqual(r['success_fraction'],0)
        self.assertIsNone(r['events_per_success'])

    def test_failed_attempt_costs_count(self):
        rows=[shot(0,20),shot(1,0)]
        rows[0]['wall_input_J']['laser']=100
        rows[1]['wall_input_J']['acoustic']=20
        rows[0]['useful_electricity_J']=10
        r=summarize(rows,10)[0]
        self.assertEqual(r['net_electricity_J'],-110)
        self.assertEqual(r['average_net_power_W'],-5.5)

    def test_unknown_cost_blocks_net(self):
        s=shot(0);s['wall_input_J']['vacuum']=None
        self.assertIsNone(summarize([s],10)[0]['net_electricity_J'])

    def test_missing_wall_category_rejected(self):
        s=shot(0);del s['wall_input_J']['vacuum']
        with self.assertRaises(ValueError):summarize([s],10)

    def test_no_detector_to_reaction_substitution(self):
        s=shot(0,None);s['detected_alpha_count']=30
        r=summarize([s],10)[0]
        self.assertIsNone(r['total_fusion_events'])
        self.assertEqual(r['detected_alpha_count'],30)

    def test_expected_population_does_not_predict_success(self):
        s=shot(0,20);s['event_semantics']='EXPECTED_POPULATION'
        r=summarize([s],10)[0]
        self.assertEqual(r['events_per_attempt'],20)
        self.assertIsNone(r['success_fraction'])
        self.assertEqual(r['success_fraction_missing_data_bounds'],[0,1])

    def test_invalid_numeric_values(self):
        for value in [True,-1,math.nan,math.inf,'10']:
            with self.subTest(value=value),self.assertRaises(ValueError):summarize([shot(0,value)],10)

    def test_duplicate_attempt_rejected(self):
        with self.assertRaises(ValueError):summarize([shot(0),shot(0)],10)

    def test_no_dd_dt_identity(self):
        s=shot(0);s['apparatus_id']='BEYOND_Q_REACTOR_A'
        with self.assertRaises(ValueError):summarize([s],10)

    def test_evidence_classes_not_pooled(self):
        a,b=shot(0),shot(1);b['evidence_class']='MEASURED'
        self.assertEqual(len(summarize([a,b],10)),2)

    def test_arms_not_pooled(self):
        self.assertEqual(len(summarize([shot(0),shot(1,arm='REF_ON')],10)),2)

    def test_escape_energy_requires_field_accounting(self):
        s=shot(0);s['alpha_birth_energy_J']=1;s['alpha_escape_energy_J']=2
        with self.assertRaises(ValueError):summarize([s],10)

    def test_jitter_bias_and_missingness_separate(self):
        rows=[shot(i) for i in range(3)]
        rows[0]['firing_time_error_s']=-2;rows[1]['firing_time_error_s']=2
        r=summarize(rows,10)[0]
        self.assertEqual(r['timing_missing_n'],1)
        self.assertEqual(r['observed_timing_bias_s'],0)
        self.assertEqual(r['observed_timing_population_sd_s'],2)

    def test_no_threshold_tuning_default(self):
        for threshold in [None,0,-1,math.nan,True]:
            with self.subTest(threshold=threshold),self.assertRaises(ValueError):summarize([shot(0)],threshold)

    def test_empty_ensemble_no_nan(self):
        self.assertEqual(summarize([],10),[])

    def test_pocket_placeholder_is_blocked(self):
        d=json.loads((Path(__file__).parent/'geometry_template.json').read_text())
        gaps=geometry_gaps(d)
        self.assertIn('boron_form',gaps)
        self.assertIn('pocket_inner_dimensions_m',gaps)

    def test_removing_critical_geometry_does_not_pass(self):
        self.assertIn('ceramic_composition',geometry_gaps({'schema_version':'SF_GEOMETRY_0_1','parameters':{}}))

    def test_resolved_geometry_requires_source(self):
        d={'schema_version':'SF_GEOMETRY_0_1','parameters':{'x':{'unit':'m','value':1,'status':'DERIVED','source_ref':None}}}
        with self.assertRaises(ValueError):geometry_gaps(d)


if __name__=='__main__':unittest.main()
