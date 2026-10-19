import sys,pathlib,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
import model

class MauiSimulatorContractTests(unittest.TestCase):
  @classmethod
  def setUpClass(cls):cls.p,cls.scenarios=model.read_inputs()
  def test_thirty_years_is_thirty(self):
    r=model.annual_run('hybrid_compute',self.p,self.scenarios)
    self.assertEqual(len(r['annual']),30)
    self.assertEqual([r['annual'][0]['year'],r['annual'][-1]['year']],[2026,2055])
  def test_counterfactual_zero_increment(self):
    r=model.annual_run('status_quo',self.p,self.scenarios)
    self.assertEqual(r['npv_30yr_dollars'],0)
  def test_feedstock_splitting_no_double_count(self):
    s=model.resolve_scenario('hybrid_compute',self.scenarios)
    y=model.compute_year(2029,s,self.p,'hybrid_compute')
    incoming_food=y['food_short_t']+y['farm_short_t']
    allocated=y['rescued_food_short_t']+y['ad_feed_short_t']+y['htl_food_short_t']+y['food_compost_short_t']
    self.assertAlmostEqual(incoming_food,allocated,delta=.1)
    self.assertLessEqual(s['ad_share']+s['htl_share'],1)
  def test_biosolids_not_counted_again_as_landfill_food(self):
    a=model.compute_year(2029,model.resolve_scenario('hybrid_compute',self.scenarios),self.p,'hybrid_compute')
    self.assertEqual(a['landfill_diversion_short_t'],a['food_short_t']+a['green_short_t'])
    self.assertGreater(a['biosolids_htl_wet_short_t'],0)
  def test_conditional_biofuel_excluded_from_cashflows(self):
    y=model.compute_year(2029,model.resolve_scenario('hybrid_htl',self.scenarios),self.p,'hybrid_htl')
    self.assertGreater(y['conditional_fuel_value_excluded_dollars'],0)
    self.assertIn('NOT CERTIFIED',y['certification'])
  def test_live_weather_forecast_changes_week_output(self):
    weather={'time':['2030-01-01T01:00']*168,'shortwave_radiation':[900]*168}
    with_weather=model.dispatch_168h('hybrid_compute',weather,self.p,self.scenarios)
    offline=model.dispatch_168h('hybrid_compute',None,self.p,self.scenarios)
    self.assertEqual(with_weather['data_origin'],'MIXED FORECAST/SYNTHETIC')
    self.assertNotEqual(with_weather['grid_export_mwh'],offline['grid_export_mwh'])
  def test_storm_outage_and_unserved_load(self):
    x=model.dispatch_168h('storm_outage',None,self.p,self.scenarios)
    self.assertEqual(x['outage_hours'],72)
    self.assertGreater(x['unserved_critical_and_flexible_mwh'],0)
  def test_all_domains_unverified_until_measured(self):
    x=model.annual_run('hybrid_compute',self.p,self.scenarios)
    self.assertEqual(x['gates']['net_positive_everything'],'NOT DEMONSTRATED')
    self.assertEqual(x['gates']['ecology'],'UNVERIFIED')
  def test_override_changes_results(self):
    a=model.annual_run('hybrid_compute',self.p,self.scenarios)
    b=model.annual_run('hybrid_compute',self.p,self.scenarios,{'solar_mw':40})
    self.assertGreater(b['last_year']['solar_mwh'],a['last_year']['solar_mwh'])

if __name__=='__main__':unittest.main()
