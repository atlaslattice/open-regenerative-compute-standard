#!/usr/bin/env python3
"""Local-only, read-only Maui ORCS research dashboard; NOT a facility control server."""
import argparse,datetime,json,pathlib,urllib.parse
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
import model
from live_feeds import feed_view, usable_weather
ROOT=pathlib.Path(__file__).resolve().parent
DASH=ROOT/'dashboard.html'
FEEDS=ROOT/'live'/'latest.json'
ITEMS=json.loads((ROOT/'data'/'feed_inventory.json').read_text())

ALLOWED={'solar_mw':(0,75),'food_capture':(0,1),'green_capture':(0,1),
  'farm_short_tpy':(0,30000),'biosolids_wet_short_tpy':(0,30000),
  'ad_share':(0,1),'htl_share':(0,1),'reuse_target_fraction':(0,1),
  'desal_mgd':(0,28),'it_mw':(0,15),'battery_mwh':(0,400)}


def parsed(query):
    name=query.get('scenario',['hybrid_compute'])[0]
    p,scenarios=model.read_inputs()
    if name not in scenarios:raise ValueError('Unknown scenario')
    overrides={}
    for k,values in query.items():
        if k not in ALLOWED:continue
        x=float(values[0]);lo,hi=ALLOWED[k]
        if not lo<=x<=hi:raise ValueError(f'{k} must be between {lo} and {hi}')
        overrides[k]=x
    template=model.resolve_scenario(name,scenarios)
    template.update(overrides)
    if template['ad_share']+template['htl_share']>1.0:raise ValueError('Food feedstock shares AD+HTL > 1.0')
    return name,p,scenarios,overrides

class Handler(BaseHTTPRequestHandler):
  def send_json(self,obj,status=200):
    raw=json.dumps(obj,allow_nan=False).encode('utf-8')
    self.send_response(status);self.send_header('Content-Type','application/json; charset=utf-8')
    self.send_header('Cache-Control','no-store');self.send_header('Content-Length',str(len(raw)))
    self.end_headers();self.wfile.write(raw)
  def do_GET(self):
    parsedurl=urllib.parse.urlsplit(self.path)
    path=parsedurl.path
    q=urllib.parse.parse_qs(parsedurl.query,keep_blank_values=False)
    try:
      if path in ('/','/index.html'):
        b=DASH.read_bytes();self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.send_header('Content-Length',str(len(b)));self.end_headers();self.wfile.write(b);return
      if path=='/api/catalog':
        p,configs=model.read_inputs()
        return self.send_json({'scenario_options':{name:x.get('description',model.resolve_scenario(name,configs).get('description')) for name,x in configs.items()},'feed_inventory':ITEMS,'assumptions':p,'scenario_parameters':{n:model.resolve_scenario(n,configs) for n in configs}})
      if path=='/api/live':
        if FEEDS.exists():return self.send_json(feed_view(json.loads(FEEDS.read_text())))
        return self.send_json({'status':'NO LIVE FETCH ATTEMPT','feeds':{},'note':'To fetch public feeds, explicitly run python live_feeds.py; never synthetic live observations.'})
      if path.startswith('/api/'):
        name,p,scenarios,overrides=parsed(q)
        if path=='/api/annual':
          res=model.annual_run(name,p,scenarios,overrides)
          return self.send_json(res)
        if path=='/api/dispatch':
          weather=None
          if FEEDS.exists():
            cache=json.loads(FEEDS.read_text())
            weather=usable_weather(cache)
          return self.send_json(model.dispatch_168h(name,weather,p,scenarios,overrides))
        if path=='/api/compare':
          summary=[]
          for n in scenarios:
            r=model.annual_run(n,p,scenarios)
            summary.append({'name':n,'npv_dollars':r['npv_30yr_dollars'],
              'water_substitution_mgd':r['last_year']['potable_substitution_mgd_potential'],
              'net_electricity_mwh':r['last_year']['annual_net_generation_mwh_proxy'],
              'waste_diversion_short_t':r['last_year']['landfill_diversion_short_t']})
          return self.send_json({'comparison':'SIMULATED','data':summary})
      self.send_error(404,'Path not found')
    except (ValueError,KeyError,TypeError,ZeroDivisionError) as exc:
      self.send_json({'error':str(exc)},400)
    except Exception as exc:
      self.send_json({'error':'Failed to load local research model or cache: '+str(exc)[:200]},500)
  def do_POST(self):self.send_error(405,'Research interface is read-only')
  def log_message(self,format,*args):pass

def main():
  ap=argparse.ArgumentParser(description=__doc__)
  ap.add_argument('--port',type=int,default=8765)
  args=ap.parse_args()
  print(f'Open http://127.0.0.1:{args.port} in your browser (synthetic model by default).')
  print('Feed retrieval is explicit: python live_feeds.py')
  ThreadingHTTPServer(('127.0.0.1',args.port),Handler).serve_forever()
if __name__=='__main__':main()
