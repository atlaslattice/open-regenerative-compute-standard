#!/usr/bin/env python3
"""Reproduce offline scenarios and exercise HTTP endpoints; no external calls."""
import csv, datetime, hashlib, json, pathlib, platform, threading, urllib.request, urllib.error
from http.server import ThreadingHTTPServer
import model, server, live_feeds
ROOT=pathlib.Path(__file__).resolve().parent

def main():
    out=ROOT/'results';out.mkdir(exist_ok=True)
    p,configs=model.read_inputs();summary=[]
    for name in configs:
        annual=model.annual_run(name,p,configs)
        dispatch=model.dispatch_168h(name,p=p,configs=configs)
        run={'annual_model':annual,'dispatch':dispatch}
        (out/(name+'.json')).write_text(json.dumps(run,indent=2,allow_nan=False)+'\n')
        summary.append({'scenario':name,'npv_screening_dollars':annual['npv_30yr_dollars'],
            'initial_capex_incomplete_dollars':annual['initial_capex_dollars'],
            'water_substitution_mgd':annual['last_year']['potable_substitution_mgd_potential'],
            'diverted_short_tpy':annual['last_year']['landfill_diversion_short_t'],
            'weekly_grid_import_mwh':dispatch['grid_import_mwh'],
            'weekly_grid_export_mwh':dispatch['grid_export_mwh'],
            'weekly_critical_unserved_mwh':dispatch['critical_unserved_mwh'],
            'weekly_flexible_unserved_mwh':dispatch['flexible_unserved_mwh'],
            'origin':dispatch['data_origin']})
    with (out/'scenario_comparison.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(summary[0]));writer.writeheader();writer.writerows(summary)
    cache_path=ROOT/'live'/'latest.json'
    if cache_path.exists():
        cache=json.loads(cache_path.read_text());weather=live_feeds.usable_weather(cache)
        if weather:
            run=model.dispatch_168h('hybrid_compute',weather)
            (out/'forecast_dispatch.json').write_text(json.dumps(run,indent=2)+'\n')
    http=ThreadingHTTPServer(('127.0.0.1',0),server.Handler)
    thread=threading.Thread(target=http.serve_forever,daemon=True);thread.start()
    base='http://127.0.0.1:'+str(http.server_port);receipts=[]
    try:
        for path,status in [('/',200),('/api/catalog',200),('/api/live',200),('/api/compare',200),
            ('/api/annual?scenario=hybrid_compute',200),('/api/dispatch?scenario=storm_outage',200),
            ('/api/dispatch?scenario=hybrid_compute',200),('/api/annual?scenario=missing',400),
            ('/api/annual?solar_mw=-1',400),('/api/annual?ad_share=.8&htl_share=.5',400)]:
            try:
                with urllib.request.urlopen(base+path) as r:code=r.status;body=r.read()
            except urllib.error.HTTPError as e:code=e.code;body=e.read()
            assert code==status,(path,code,status)
            receipts.append({'path':path,'expected':status,'actual':code,'bytes':len(body),
                'sha256':hashlib.sha256(body).hexdigest()})
        request=urllib.request.Request(base+'/api/annual',data=b'{}',method='POST')
        try:urllib.request.urlopen(request);raise AssertionError('POST unexpectedly accepted')
        except urllib.error.HTTPError as e:assert e.code==405
        receipts.append({'path':'/api/annual','method':'POST','actual':405})
    finally:http.shutdown();http.server_close();thread.join()
    (out/'http_receipts.json').write_text(json.dumps({'tested_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'python':platform.python_version(),'checks':receipts},indent=2)+'\n')
    hashes={str(path.relative_to(ROOT)):hashlib.sha256(path.read_bytes()).hexdigest()
        for path in [ROOT/'model.py',ROOT/'server.py',ROOT/'live_feeds.py',ROOT/'data/assumptions.json',ROOT/'data/scenarios.json']}
    (out/'model_input_hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
    print(json.dumps({'scenario_runs':len(summary),'http_checks':len(receipts),'summary':summary},indent=2))
if __name__=='__main__':main()
