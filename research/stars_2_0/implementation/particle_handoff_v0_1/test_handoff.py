import copy,json,math,unittest
from pathlib import Path
from handoff import Engine,execute,number
R=Path(__file__).resolve().parent
class HandoffTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.engine=Engine()
    def setUp(self):
        self.c=json.loads((R/'examples/C_conditional_reference.json').read_text());self.a=copy.deepcopy(self.c['attempts'][0]);self.s=copy.deepcopy(self.c['stages'])
    def run_attempt(self):return self.engine.attempt(self.a,self.s)
    def test_primary_particle_and_energy_closure(self):
        r=self.run_attempt();m=r['metrics'];self.assertLess(abs(m['particle_residual']),1e-8);self.assertLess(abs(m['energy_residual_MeV']),1e-8)
        self.assertAlmostEqual(m['expected_alpha_births'],3*m['events']);self.assertAlmostEqual(m['expected_B11_consumed'],m['events'])
        self.assertAlmostEqual(m['source_protons'],m['remaining_protons']+m['events']);self.assertIsNone(m['net_electricity_J'])
    def test_hazard_matches_previous_independent_integrator(self):
        m=self.run_attempt()['metrics'];old=self.engine.p.reactions(self.engine.coordinate,self.engine.rows,.675,1e18,1.,16)
        self.assertAlmostEqual(m['events'],10000*old['probability'],places=12)
    def test_zero_reactions_does_not_remove_stopping(self):
        self.s[0]['reaction_model']='REACTIONS_OFF_CONTROL';m=self.run_attempt()['metrics']
        self.assertEqual(m['events'],0);self.assertEqual(m['alpha_birth_kinetic_MeV'],0);self.assertGreater(m['material_transfer_MeV'],0);self.assertEqual(m['source_protons'],m['remaining_protons'])
    def test_zero_column_preserves_energy(self):
        self.s[0]['normal_atoms_cm2']=0;m=self.run_attempt()['metrics'];self.assertEqual(m['events'],0);self.assertEqual(m['material_transfer_MeV'],0)
    def test_two_stage_survival_is_not_independent_full_source(self):
        first=self.run_attempt()['metrics']['events'];self.s.append(copy.deepcopy(self.s[0]));self.s[1]['stage_id']='visit2'
        r=self.run_attempt();self.assertEqual(r['status'],'CONDITIONAL_HANDOFF_COMPLETE');second=r['stage_records'][1]
        self.assertLess(second['input']['weight'],10000);self.assertLess(second['input']['kinetic_MeV'],.675)
        self.assertEqual(second['input'],r['stage_records'][0]['output']);self.assertGreater(r['metrics']['events'],first)
    def test_split_equal_column_matches_one_slab(self):
        a=self.run_attempt()['metrics'];self.s[0]['normal_atoms_cm2']=5e17;self.s[0]['depth_cells']=8
        s=copy.deepcopy(self.s[0]);s['stage_id']='slab2';s['physical_instance_id']='slab2';self.s.append(s);b=self.run_attempt()['metrics']
        self.assertTrue(math.isclose(a['events'],b['events'],rel_tol=1e-10));self.assertAlmostEqual(a['remaining_proton_kinetic_MeV'],b['remaining_proton_kinetic_MeV'],places=8)
    def test_missing_source_is_not_zero(self):
        self.a['source_packets']=None;r=self.run_attempt();self.assertIsNone(r['metrics']);self.assertEqual(r['status'],'MISSING_SOURCE_OUTCOME')
    def test_known_zero_source_is_retained(self):
        self.a['source_packets']=[];r=self.run_attempt();self.assertEqual(r['metrics']['events'],0)
    def test_wrong_frame_rejected(self):
        self.a['source_frame']='CM'
        with self.assertRaises(ValueError):self.run_attempt()
    def test_wrong_units_rejected(self):
        self.a['source_energy_unit']='keV'
        with self.assertRaises(ValueError):self.run_attempt()
    def test_nonunit_direction_rejected(self):
        self.a['source_packets'][0]['unit_direction_LAB']=[0,0,2]
        with self.assertRaises(ValueError):self.run_attempt()
    def test_duplicate_packets_rejected(self):
        self.a['source_packets']*=2
        with self.assertRaises(ValueError):self.run_attempt()
    def test_duplicate_stage_does_not_double_credit(self):
        self.s*=2;r=self.run_attempt();self.assertIsNone(r['metrics']);self.assertIn('Duplicate stage',r['reason'])
    def test_target_identity_cannot_change(self):
        self.s.append(copy.deepcopy(self.s[0]));self.s[1].update(stage_id='visit2',normal_atoms_cm2=2e18)
        r=self.run_attempt();self.assertIsNone(r['metrics']);self.assertIn('inconsistent inventories',r['reason'])
    def test_depletion_rejected(self):
        self.s[0]['illuminated_area_cm2']=1e-22;r=self.run_attempt();self.assertIsNone(r['metrics']);self.assertIn('depletion',r['reason'])
    def test_no_bn_transfer(self):
        self.s[0]['material']='BN';r=self.run_attempt();self.assertIsNone(r['metrics']);self.assertIn('cannot transfer',r['reason'])
    def test_stopping_floor_not_zero_energy(self):
        self.s[0]['normal_atoms_cm2']=1e30;r=self.run_attempt();self.assertIsNone(r['metrics']);self.assertIn('unresolved, not zero',r['reason'])
    def test_enn_energy_kernel_domain_blocks(self):
        self.a['source_packets'][0]['kinetic_MeV']=.162;r=self.run_attempt();self.assertIsNone(r['metrics']);self.assertIn('REACTION_ENERGY_COVERAGE_MISSING',r['reason'])
    def test_hollow_cutoff_cannot_substitute_for_supported_source(self):
        self.a['source_packets'][0]['kinetic_MeV']=53.;r=self.run_attempt();self.assertIsNone(r['metrics']);self.assertIn('COVERAGE_MISSING',r['reason'])
    def work(self,w):self.s=[dict(stage_id='field',physical_instance_id='field',type='specified_field_work',work_on_each_proton_MeV=w,evidence='ASSUMED_VERIFICATION')]
    def test_positive_field_work_is_energy_input(self):
        self.work(.1);m=self.run_attempt()['metrics'];self.assertAlmostEqual(m['external_work_MeV'],1000);self.assertLess(abs(m['energy_residual_MeV']),1e-9)
    def test_negative_field_work_not_automatic_electricity(self):
        self.work(-.1);m=self.run_attempt()['metrics'];self.assertAlmostEqual(m['external_work_MeV'],-1000);self.assertIsNone(m['load_electricity_J'])
    def test_excessive_field_extraction_rejected(self):
        self.work(-1.);r=self.run_attempt();self.assertIsNone(r['metrics'])
    def mirror(self):return dict(stage_id='mirror',physical_instance_id='mirror',type='adiabatic_mirror_boundary',mirror_ratio=5.,throat_potential_energy_rise_MeV=.03,axis_LAB=[0,0,1],evidence='ASSUMED_ANALYTIC_BOUNDARY')
    def test_passing_mirror_accounts_barrier_work(self):
        self.s=[self.mirror()];m=self.run_attempt()['metrics'];self.assertEqual(m['escaped_protons'],10000);self.assertAlmostEqual(m['external_work_MeV'],-300);self.assertLess(abs(m['energy_residual_MeV']),1e-9)
    def test_trapped_pitch_not_reisotropized_each_visit(self):
        self.a['source_packets'][0]['unit_direction_LAB']=[.8,0,.6];self.s=[self.mirror(),dict(self.mirror(),stage_id='mirror_return')]
        r=self.run_attempt();self.assertEqual(r['metrics']['remaining_protons'],10000);self.assertEqual(r['metrics']['escaped_protons'],0)
        self.assertEqual(r['remaining_packets'][0]['unit_direction_LAB'],[.8,0,.6])
    def test_throat_barrier_uses_division_by_mirror_ratio(self):
        self.a['source_packets'][0]['kinetic_MeV']=.2
        self.a['source_packets'][0]['unit_direction_LAB']=[math.sqrt(.1),0,math.sqrt(.9)]
        self.s=[self.mirror()];r=self.run_attempt();self.assertEqual(r['metrics']['escaped_protons'],10000)
        # Correct threshold is .83, while archived V/E gives .95 and would reflect this packet.
    def test_below_correct_loss_cone_threshold_reflects(self):
        self.a['source_packets'][0]['kinetic_MeV']=.2
        self.a['source_packets'][0]['unit_direction_LAB']=[math.sqrt(.2),0,math.sqrt(.8)]
        self.s=[self.mirror()];r=self.run_attempt();self.assertEqual(r['metrics']['escaped_protons'],0)
    def test_alpha_production_kernel_cannot_be_used_as_events(self):
        saved=self.engine.rows;self.engine.rows=copy.deepcopy(saved);self.engine.rows[0]['observable']='DETECTED_ALPHA_PRODUCTION'
        try:self.assertIsNone(self.run_attempt()['metrics'])
        finally:self.engine.rows=saved
    def test_nonfinite_and_bool_rejected(self):
        for n in [True,float('nan'),float('inf')]:
            with self.assertRaises(ValueError):number(n)
    def test_all_attempt_missing_outcome_blocks_unconditional_total(self):
        self.c['attempts'][0]['source_packets']=None;r=execute(self.c);self.assertEqual(r['attempt_count'],3);self.assertIsNone(r['expected_events_all_attempts']);self.assertIsNone(r['physical_success_probability'])
    def test_a_profile_retains_explicit_gaps(self):
        a=json.loads((R/'examples/A_apparatus_profile.json').read_text());r=execute(a);self.assertIsNone(r['metrics']);self.assertTrue(r['blockers'])
    def test_fresh_target_assumption_required(self):
        self.c['target_inventory_scope']='UNKNOWN'
        with self.assertRaises(ValueError):execute(self.c)
    def test_fake_calibrated_run_rejected(self):
        self.c['run_class']='CALIBRATED_APPARATUS'
        with self.assertRaises(ValueError):execute(self.c)
if __name__=='__main__':unittest.main()
