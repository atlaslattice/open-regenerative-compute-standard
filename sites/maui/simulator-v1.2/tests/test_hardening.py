import copy, datetime, math, unittest
from unittest.mock import patch
import model, live_feeds

class HardenedContracts(unittest.TestCase):
    def setUp(self):
        self.p,self.configs=model.read_inputs()
        self.now=datetime.datetime(2026,10,19,14,tzinfo=datetime.timezone.utc)
        hst=datetime.timezone(datetime.timedelta(hours=-10))
        start=self.now.astimezone(hst).replace(hour=0)
        self.cache={'feeds':{'forecast':{'status':'LIVE_RETRIEVED','fetched_utc':self.now.isoformat(),
            'result':{'product_type':'FORECAST (not measured observations)','units':{'shortwave_radiation':'W/m²'},
            'hourly':{'time':[(start+datetime.timedelta(hours=i)).isoformat() for i in range(168)],
            'shortwave_radiation':[100.0]*168}}}}}
    def test_impossible_inputs_rejected_every_entry(self):
        for changes in ({'battery_mwh':-1},{'solar_mw':float('nan')},{'food_capture':1.1},{'ad_share':.8,'htl_share':.7}):
            for fn in (model.annual_run,model.dispatch_168h):
                with self.subTest(changes=changes,fn=fn.__name__),self.assertRaises(ValueError):
                    fn('hybrid_compute',p=self.p,configs=self.configs,overrides=changes)
    def test_islanded_grid_never_exports(self):
        r=model.dispatch_168h('storm_outage',overrides={'solar_mw':100,'battery_mwh':0})
        self.assertTrue(any(x['curtailed_mwh']>0 for x in r['rows']))
        for x in r['rows']:
            if x['grid_outage']:
                self.assertEqual(x['grid_export_mwh'],0)
                self.assertEqual(x['grid_import_mwh'],0)
    def test_hourly_electric_balance_and_storage(self):
        for name in self.configs:
            r=model.dispatch_168h(name)
            for row in r['rows']:
                supply=row['solar_mw']+row['bio_mw']+row['grid_import_mwh']+row['battery_discharge_mwh']
                uses=row['demand_mw']-row['unserved_mwh']+row['grid_export_mwh']+row['battery_charge_mwh']+row['curtailed_mwh']
                self.assertAlmostEqual(supply,uses,delta=.004)
                expected=row['battery_soc_before_mwh']+.92*row['battery_charge_mwh']-row['battery_discharge_mwh']/.92
                self.assertAlmostEqual(expected,row['battery_soc_mwh'],delta=.001)
                self.assertGreaterEqual(row['battery_soc_mwh'],0)
    def test_critical_priority_and_deficit_split(self):
        r=model.dispatch_168h('storm_outage')
        self.assertAlmostEqual(r['critical_unserved_mwh']+r['flexible_unserved_mwh'],r['unserved_critical_and_flexible_mwh'],delta=.02)
        for x in r['rows']:
            self.assertLessEqual(x['critical_unserved_mwh'],x['critical_mw']+.001)
            if x['critical_unserved_mwh']>0:
                self.assertAlmostEqual(x['flexible_unserved_mwh'],x['demand_mw']-x['critical_mw'],delta=.002)
    def test_bioenergy_matches_annual_budget(self):
        d=model.dispatch_168h('hybrid_compute')
        a=model.annual_run('hybrid_compute')['annual'][3]
        self.assertAlmostEqual(d['rows'][0]['bio_mw']*8760,a['ad_electric_mwh'],delta=5)
    def test_stale_and_future_cache_rejected(self):
        for age in (25,-1):
            cache=copy.deepcopy(self.cache)
            cache['feeds']['forecast']['fetched_utc']=(self.now-datetime.timedelta(hours=age)).isoformat()
            self.assertIsNone(live_feeds.usable_weather(cache,self.now))
    def test_schema_units_and_timestamps_rejected(self):
        for kind in ('units','gaps','negative','nan'):
            c=copy.deepcopy(self.cache);d=c['feeds']['forecast']['result']
            if kind=='units':d['units']['shortwave_radiation']='kWh/m2'
            if kind=='gaps':d['hourly']['time'][8]=d['hourly']['time'][7]
            if kind=='negative':d['hourly']['shortwave_radiation'][8]=-5
            if kind=='nan':d['hourly']['shortwave_radiation'][8]=math.nan
            self.assertIsNone(live_feeds.usable_weather(c,self.now))
    def test_forecast_starts_current_hst_hour(self):
        w=live_feeds.usable_weather(self.cache,self.now)
        self.assertEqual(w['time'][0],'2026-10-19T04:00:00-10:00')
        self.assertEqual(len(w['time']),164)
    def test_failed_refresh_retains_cache_as_stale(self):
        import tempfile,pathlib,json
        with tempfile.TemporaryDirectory() as directory:
            cache=pathlib.Path(directory)/'latest.json';cache.write_text(json.dumps(self.cache))
            with patch.object(live_feeds,'CACHE',cache),patch.dict(live_feeds.FUNCTIONS,{'forecast':lambda: (_ for _ in ()).throw(OSError('test provider unavailable'))},clear=True):
                result=live_feeds.refresh()
            self.assertEqual(result['feeds']['forecast']['status'],'STALE_CACHE')
            self.assertIsNone(result['forecast'])
    def test_empty_weather_does_not_claim_forecast(self):
        self.assertEqual(model.dispatch_168h(weather={'shortwave_radiation':[]})['data_origin'],'SYNTHETIC')

if __name__=='__main__':unittest.main()
