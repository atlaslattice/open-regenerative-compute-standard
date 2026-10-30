import unittest,json,csv,math
from pathlib import Path
from reconciliation import *
from fuelcycle.model import simulate,validate
from fuelcycle.physics import reaction_ledger,argon_burn_fraction
from fuelcycle.inventory import advance
ROOT=Path(__file__).resolve().parent
def parameters():
    p=json.loads((ROOT/'reference.json').read_text());p['days']=20
    return p

class Regression(unittest.TestCase):
    def test_C01_include_B_blanket_and_percent(self):
        r=static_balance(63.1,3.65,0,1,1,1.02,1)
        self.assertAlmostEqual(r['surplus_kg'],4.912)
        self.assertAlmostEqual(r['surplus_percent_B_burn'],100*4.912/63.1)

    def test_C02_configuration_lock(self):
        p=parameters();p['power_b_dt_mw']=525
        with self.assertRaises(ValueError):validate(p)

    def test_C03_stoichiometry_and_FPY(self):
        self.assertAlmostEqual(tritium_factor(),56.0490732962154,places=10)
        self.assertAlmostEqual(tritium_factor(fpy_days=365),tritium_factor()*365/365.25)
        self.assertGreater(tritium_factor(),55.8)

    def test_C04_consumption_subtracted(self):
        s=source_case(.3735,.52,.52)
        self.assertAlmostEqual(s['dd_birth_kg'],s['a_secondary_burn_kg']+s['plasma_net_kg'])

    def test_C05_midpoint(self):
        self.assertAlmostEqual(1.70+(1.3+2.6)/2,3.65)
        self.assertNotAlmostEqual(1.70+(1.3+2.6)/2,3.85)

    def test_C06_DD_neutron_factor_two(self):
        n=dd_source()['n_atoms_s']
        self.assertAlmostEqual(n/1.71e19,1,delta=.002)
        self.assertAlmostEqual(n/8.55e18,2,delta=.004)

    def test_C07_C08_nonduplicated_heat(self):
        l=reaction_ledger(100,50,20,10,5,7)
        self.assertAlmostEqual(l['fusion_j'],l['fusion_charged_j']+l['fusion_neutron_j'])
        self.assertAlmostEqual(l['nuclear_release_j'],l['fusion_j']+l['assumed_blanket_reaction_q_j'])
        self.assertEqual(20+18,38)
        self.assertEqual(l['net_electric_status'],'UNRESOLVED')

    def test_C10_single_pass_not_loss(self):
        end,e=advance(1,0,{'extract':.85},1)
        self.assertAlmostEqual(end+e['extract'],1)

    def test_C12_geometry_results_unresolved(self):
        rows=enrichment_plan()
        self.assertEqual(len(rows),24)
        self.assertTrue(all(r['tbr'] is None and r['optimized_geometry'] is None for r in rows))

    def test_legacy_28_scenarios(self):
        f=ROOT.parent/'dynamic_fuel_cycle_v1_1/baseline_v1/SCENARIOS.csv'
        for r in csv.DictReader(f.read_text().splitlines()):
            val=float(r['a_preprocessing_kg_fpy'])+float(r['eta_b'])*float(r['tbr_b'])*float(r['burn_kg_fpy'])-float(r['burn_kg_fpy'])
            self.assertLessEqual(abs(val-float(r['net_kg_fpy'])),.000051)

    def test_independent_A_recovery_paths(self):
        p=parameters();p.update(a_plasma_recovery=0,a_blanket_recovery=1)
        rows,s=simulate(p,[(1,0)]*p['days'])
        self.assertEqual(rows[-1]['a_plasma_processed'],0)
        self.assertGreater(rows[-1]['a_blanket_processed'],0)
        self.assertGreater(rows[-1]['a_plasma_process_loss'],0)
        p.update(a_plasma_recovery=1,a_blanket_recovery=0)
        rows,s=simulate(p,[(1,0)]*p['days'])
        self.assertGreater(rows[-1]['a_plasma_processed'],0)
        self.assertEqual(rows[-1]['a_blanket_processed'],0)

    def test_secondary_off_retains_primary_neutrons(self):
        p=parameters();p.update(a_reaction_day=0,a_fast_fraction=0)
        rows,s=simulate(p,[(1,0)]*p['days'])
        self.assertEqual(rows[-1]['a_burn'],0)
        self.assertGreater(s['dd_neutrons'],0)
        self.assertEqual(s['a_dt_neutrons'],0)
        self.assertAlmostEqual(rows[-1]['blanket_a_birth'],p['a_dd_blanket_yield']*s['dd_neutrons']*T_KG_PER_ATOM)

    def test_secondary_spectrum_yield_independence(self):
        no=source_case(0,.52,0);on=source_case(.4,.52,0)
        self.assertEqual(no['blanket_gross_kg'],on['blanket_gross_kg'])
        self.assertEqual(no['dd_neutrons'],on['dd_neutrons'])

    def test_no_source_no_T(self):
        p=parameters();p.update(initial_a_kg=0,initial_b_kg=0)
        rows,s=simulate(p,[(0,1)]*p['days'])
        self.assertEqual(s['final_kg'],0)
        self.assertEqual(rows[-1]['b_burn'],0)

    def test_split_processing_mass_closure(self):
        p=parameters();rows,s=simulate(p,[(1,1)]*p['days'])
        self.assertLess(s['maximum_mass_residual_kg'],1e-9)
        self.assertIsNone(s['qualified_usable_surplus_kg'])

    def test_427_is_only_conditional_arithmetic(self):
        self.assertAlmostEqual(constant_inventory_example(),426.96)

    def test_threshold_degrades_with_A_recovery(self):
        a=static_balance(63.335,1.7,1.95,1,1,1.02,.95)
        b=static_balance(63.335,1.7,1.95,.95,.9,1.02,.95)
        self.assertGreater(b['tbr_b_break_even'],a['tbr_b_break_even'])
        self.assertIsNone(b['qualified_usable_surplus_kg'])

if __name__=='__main__':unittest.main()
