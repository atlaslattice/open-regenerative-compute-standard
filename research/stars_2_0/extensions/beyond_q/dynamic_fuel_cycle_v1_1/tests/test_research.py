import csv
import json
import hashlib
import math
import subprocess
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from fuelcycle.physics import *
from fuelcycle.inventory import advance
from fuelcycle.model import simulate, validate
from fuelcycle.schedules import generate

def inputs():
    p=json.loads((ROOT/'inputs/reference_v1_1.json').read_text())
    p.update(days=10,step_days=.125)
    return p

class Acceptance(unittest.TestCase):
    def test_v1_snapshot_exact_git_blobs(self):
        expected={'APPENDIX_SOURCES_AND_PROVENANCE.md':'f534da37a286496460aa534c775027cccded465f',
          'README.md':'006b9e186234ee2aa0753ae517217aa5fc2b007c',
          'SCENARIOS.csv':'b2fc576ab6fccf4ee7923ea9faed4416c18172b4',
          'WHITE_PAPER.md':'0d3cfc6c79b0f1e433f239137f91b1eff20b9fdb',
          'research_metadata.json':'8116c824cf7609d389bb414241fe7d01fde077a5',
          'tritium_ledger.py':'9b706ce67818df24a4af732434eeaab817e85e09'}
        for name,sha in expected.items():
            b=(ROOT/'baseline_v1'/name).read_bytes()
            actual=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
            self.assertEqual(actual,sha)

    def test_v1_all_scenarios(self):
        for r in csv.DictReader((ROOT/'baseline_v1/SCENARIOS.csv').read_text().splitlines()):
            net=float(r['a_preprocessing_kg_fpy'])+float(r['eta_b'])*float(r['tbr_b'])*float(r['burn_kg_fpy'])-float(r['burn_kg_fpy'])
            self.assertLessEqual(abs(net-float(r['net_kg_fpy'])),.000051)

    def test_v1_original_script(self):
        for e in ('.85','1'):
            subprocess.run([sys.executable,str(ROOT/'baseline_v1/tritium_ledger.py'),'--efficiency',e],check=True,capture_output=True)

    def test_sources(self):
        s=dd_source()
        self.assertAlmostEqual(s['t_atoms_s']/s['events_s'],.5)
        self.assertAlmostEqual(s['n_atoms_s']/1.71e19,1,delta=.002)
        self.assertAlmostEqual(dt_events(1130)*FPY_S*T_KG_PER_ATOM,63.1,delta=.3)

    def test_no_source_no_creation(self):
        p=inputs();p.update(initial_b_kg=0,initial_a_kg=0)
        rows,s=simulate(p,[(0,1)]*p['days'])
        self.assertEqual(s['final_kg'],0)
        self.assertEqual(rows[-1]['b_burn'],0)

    def test_global_conservation_and_no_consumed_delivery(self):
        p=inputs();rows,s=simulate(p,[(1,1)]*p['days'])
        r=rows[-1]
        sources=s['initial_kg']+r['dd_birth']+r['blanket_a_birth']+r['blanket_b_birth']
        sinks=r['a_burn']+r['b_burn']+r['decay']+r['permeation']+r['process_loss']
        self.assertAlmostEqual(sources,sinks+s['final_kg'],places=10)
        self.assertLessEqual(r['a_burn'],r['dd_birth'])
        self.assertAlmostEqual(r['b_feed'],r['b_burn']+r['b_recirculated'],places=10)
        self.assertLess(s['maximum_mass_residual_kg'],1e-10)

    def test_consumed_atom_cannot_escape(self):
        end,e=advance(1,0,{'burn':1e9,'escape':0},1)
        self.assertEqual(end,0)
        self.assertAlmostEqual(e['burn'],1)
        self.assertEqual(e['escape'],0)

    def test_thermal_partition(self):
        l=reaction_ledger(100,50,20,10,2,3)
        self.assertAlmostEqual(l['fusion_j'],l['fusion_neutron_j']+l['fusion_charged_j'])
        self.assertAlmostEqual(l['nuclear_release_j'],l['fusion_j']+l['assumed_blanket_reaction_q_j'])
        self.assertEqual(l['total_source_neutrons'],80)

    def test_steady_compartment_and_exact_decay(self):
        x,e=advance(5,1,{'extract':.2},20)
        self.assertAlmostEqual(x,5)
        self.assertAlmostEqual(e['extract'],20)
        x,e=advance(1,0,{'decay':math.log(2)/10},10)
        self.assertAlmostEqual(x,.5)
        self.assertAlmostEqual(e['decay'],.5)

    def test_recirculation_retains_unextracted_material(self):
        x,e=advance(1,0,{'extract':.15},1)
        self.assertAlmostEqual(x+e['extract'],1)
        self.assertGreater(x,.8)

    def test_stiff_and_small_hazards(self):
        for k in (0.,1e-16,1e-6,1,1e9):
            x,e=advance(2,3,{'exit':k},.001)
            self.assertGreaterEqual(x,0)
            self.assertAlmostEqual(x+e['exit'],2.003)

    def test_candidate_dimensions_and_bounds(self):
        self.assertAlmostEqual(fixed_exposure_burn_fraction(1e20,1e-22,100),1-math.exp(-1))
        self.assertEqual(fixed_exposure_burn_fraction(0,1,1),0)
        self.assertEqual(fixed_exposure_burn_fraction(1e100,1e100,1),1)
        self.assertEqual(competing_escape_burn_fraction(1,1),.5)
        with self.assertRaises(ValueError): fixed_exposure_burn_fraction(-1,1,1)

    def test_argon_two_stage_model(self):
        self.assertAlmostEqual(argon_burn_fraction(.2,1e20,1e-22,100),.6)
        self.assertEqual(argon_burn_fraction(1,0,0,0),1)
        self.assertEqual(argon_burn_fraction(0,0,1,1),0)
        p=inputs();p['a_fast_fraction']=1
        r,s=simulate(p,[(1,0)]*p['days'])
        self.assertAlmostEqual(r[-1]['a_burn'],r[-1]['dd_birth'])
        self.assertEqual(r[-1]['a_plasma'],0)

    def test_argon_extraction_table(self):
        for eps,minutes,loss,grams in [(.85,10,.005,1.44),(.5,10,.01,2.45),(.25,15,.025,7.34),(.1,30,.058,36.7)]:
            r=argon_extraction(eps,minutes,0,12.32,loss,64.362/365.25)
            self.assertAlmostEqual(r['inventory_ss_kg']*1000,grams,delta=.04)
            self.assertLess(r['eta_salt_and_one_iss'],1-loss)
            x,e=advance(r['inventory_ss_kg'],64.362/365.25,
                {'extract':r['k_extract_day'],'decay':math.log(2)/(12.32*365.25)},1)
            self.assertAlmostEqual(x,r['inventory_ss_kg'])

    def test_fail_invalid_config(self):
        for key,val in [('power_b_dt_mw',525),('step_days',0),('tbr_b',-1),('process_recovery',1.1),('a_escape_day',float('nan'))]:
            p=inputs();p[key]=val
            with self.assertRaises(ValueError):validate(p)
        p=inputs();p['case']='A0'
        with self.assertRaises(ValueError):validate(p)

    def test_outage_sources_stop_but_decay_continues(self):
        p=inputs();r,s=simulate(p,[(0,0)]*p['days'])
        self.assertEqual(r[-1]['dd_birth'],0)
        self.assertEqual(r[-1]['b_burn'],0)
        self.assertLess(s['final_kg'],s['initial_kg'])

    def test_schedule_seed_and_common_outage(self):
        a=generate(100,119,.9,.9,.05)
        self.assertEqual(a,generate(100,119,.9,.9,.05))
        self.assertEqual(generate(5,1,1,1,1),[(0,0)]*5)

    def test_bidirectional_transfer_conserves(self):
        p=inputs();p['reverse_transfer_kg_day']=1
        r,s=simulate(p,[(0,0)]*p['days'])
        self.assertGreater(r[-1]['b_to_a'],0)
        self.assertLess(s['maximum_mass_residual_kg'],1e-10)

    def test_no_qualification_from_arithmetic(self):
        p=inputs();r,s=simulate(p,[(1,1)]*p['days'])
        self.assertIsNone(s['qualified_usable_surplus_kg'])
        self.assertEqual(s['self_sufficiency'],'UNRESOLVED')

    def test_time_refinement(self):
        p=inputs();p['days']=60
        vals=[]
        for h in (.5,.25,.125,.0625):
            p['step_days']=h
            _,s=simulate(p,[(1,1)]*p['days'])
            vals.append(s['final_kg'])
        errors=[abs(v-vals[-1]) for v in vals[:-1]]
        self.assertGreater(errors[0],errors[1]);self.assertGreater(errors[1],errors[2])

if __name__=='__main__':unittest.main()
