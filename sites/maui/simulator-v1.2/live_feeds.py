#!/usr/bin/env python3
"""Read-only public feed adapters for Maui ORCS research dashboard.

Explicit invocation required: offline simulation never calls the network.
Failure is visible, not silently replaced with fabricated weather or alerts.
"""
import argparse, datetime, hashlib, math, json, pathlib, time, urllib.parse, urllib.request, urllib.error
ROOT=pathlib.Path(__file__).resolve().parent
CACHE=ROOT/'live'/'latest.json'
USER_AGENT='AtlasLattice-Maui-Research-v1.2 (prototype; contact: public research documentation)'
LAT,LON=20.8894,-156.4724 # Kahului proxy; NOT sanctuary monitoring station
TIMEOUT=12

def get_json(url):
    req=urllib.request.Request(url,headers={'User-Agent':USER_AGENT,'Accept':'application/geo+json, application/json'})
    with urllib.request.urlopen(req,timeout=TIMEOUT) as response:
        payload=response.read()
        parsed=json.loads(payload)
        digest=hashlib.sha256(payload).hexdigest()
        directory=ROOT/'live'/'raw';directory.mkdir(parents=True,exist_ok=True)
        (directory/(digest+'.json')).write_bytes(payload)
        (directory/(digest+'.receipt.json')).write_text(json.dumps({
            'url':url,'retrieved_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'http_status':response.status,'sha256':digest,'bytes':len(payload),
            'content_type':response.headers.get('Content-Type')},indent=2)+'\n')
        return parsed

def query(url,**params):
    return url+'?'+urllib.parse.urlencode(params, doseq=True)

def fetch_weather():
    u=query('https://api.open-meteo.com/v1/forecast',latitude=LAT,longitude=LON,
        hourly='temperature_2m,precipitation,wind_speed_10m,wind_gusts_10m,shortwave_radiation,relative_humidity_2m,cloud_cover',
        forecast_days=7,timezone='Pacific/Honolulu')
    raw=get_json(u)
    hours=raw.get('hourly',{})
    if not isinstance(hours.get('time'),list) or not isinstance(hours.get('shortwave_radiation'),list):
        raise ValueError('Required solar/weather hourly arrays missing')
    return {'url':u,'location':'Kahului reference point; local gradients not resolved',
      'units':raw.get('hourly_units',{}),
      'hourly':hours,'count':len(hours['time']),'product_type':'FORECAST (not measured observations)'}

def fetch_alerts():
    u='https://api.weather.gov/alerts/active?area=HI'
    x=get_json(u)
    events=[]
    for a in x.get('features',[])[:250]:
        d=a.get('properties',{})
        events.append({'event':d.get('event'),'severity':d.get('severity'),
           'headline':d.get('headline'),'description':(d.get('description') or '')[:550],
           'effective':d.get('effective'),'ends':d.get('ends'),
           'affected_zones':d.get('affectedZones',[])[:5]})
    return {'url':u,'scope':'STATE OF HAWAII, not necessarily Maui','events':events,
            'count':len(events),'product_type':'PUBLIC ALERTS'}

def fetch_tides():
    # NOAA CO-OPS Kahului Harbor Station 1615680; measured water-level, not sanctuary salinity.
    u=query('https://api.tidesandcurrents.noaa.gov/api/prod/datagetter',
            date='latest',station='1615680',product='water_level',
            datum='MLLW',units='metric',time_zone='gmt',format='json',application='maui_orcs')
    x=get_json(u)
    if x.get('error'):raise ValueError(str(x['error']))
    return {'url':u,'station':'Kahului Harbor 1615680','data':x.get('data',[])[:12],
            'metadata':x.get('metadata'), 'product_type':'OBSERVED WATER LEVEL'}

def fetch_earthquakes():
    # USGS API query bounding distance, recent 7 days. This is a hazard signal, NOT a tsunami forecast.
    start=(datetime.datetime.now(datetime.timezone.utc)-datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    u=query('https://earthquake.usgs.gov/fdsnws/event/1/query',format='geojson',
      latitude=LAT,longitude=LON,maxradiuskm=500,starttime=start,orderby='time',limit=100)
    x=get_json(u)
    items=[]
    for f in x.get('features',[]):
        z=f.get('properties',{})
        items.append({'magnitude':z.get('mag'),'place':z.get('place'),'time_unix_ms':z.get('time'),
                      'url':z.get('url'),'coordinates':(f.get('geometry') or {}).get('coordinates')})
    return {'url':u,'radius_km':500,'event_count':len(items),'recent':items[:25],
            'product_type':'MEASURED EARTHQUAKE EVENTS'}

def fetch_spaceweather():
    u='https://services.swpc.noaa.gov/products/noaa-scales.json'
    x=get_json(u)
    return {'url':u,'noaa_scales':x,'product_type':'SPACE WEATHER ACTIVITY (GLOBAL)'}

FUNCTIONS={'forecast':fetch_weather,'alerts':fetch_alerts,'coastal_water_level':fetch_tides,
           'earthquakes':fetch_earthquakes,'space_weather':fetch_spaceweather}

def feed_view(cache, now=None):
    """Derive freshness when read, rather than preserving yesterday's LIVE label."""
    import copy
    result=copy.deepcopy(cache)
    now=now or datetime.datetime.now(datetime.timezone.utc)
    for feed in result.get('feeds',{}).values():
        if feed.get('status')!='LIVE_RETRIEVED':continue
        try:
            age=(now-datetime.datetime.fromisoformat(feed['fetched_utc'])).total_seconds()
            feed['age_seconds']=round(age)
            # Forecast may be useful for 24h; alerts/observations require much fresher fetches.
            ttl=86400 if feed.get('result',{}).get('product_type','').startswith('FORECAST') else 3600
            if age < -300 or age >= ttl:feed['status']='STALE_CACHE'
        except (KeyError,TypeError,ValueError):feed['status']='STALE_CACHE'
    return result


def usable_weather(cache, now=None):
    """One freshness/schema/time/unit gate shared by CLI and HTTP dispatch."""
    now=now or datetime.datetime.now(datetime.timezone.utc)
    feed=feed_view(cache,now).get('feeds',{}).get('forecast',{})
    if feed.get('status')!='LIVE_RETRIEVED':return None
    data=feed.get('result') or {}
    if data.get('units',{}).get('shortwave_radiation')!='W/m²':return None
    hours=data.get('hourly') or {};times=hours.get('time',[]);rads=hours.get('shortwave_radiation',[])
    if not times or len(times)!=len(rads):return None
    hst=datetime.timezone(datetime.timedelta(hours=-10))
    start=now.astimezone(hst).replace(minute=0,second=0,microsecond=0)
    parsed=[]
    try:
        for t in times:
            stamp=datetime.datetime.fromisoformat(t)
            parsed.append(stamp.replace(tzinfo=hst) if stamp.tzinfo is None else stamp.astimezone(hst))
        if any((b-a).total_seconds()!=3600 for a,b in zip(parsed,parsed[1:])):return None
    except (TypeError,ValueError):return None
    indices=[i for i,t in enumerate(parsed) if t>=start][:168]
    if not indices or parsed[indices[0]]!=start:return None
    if any(isinstance(rads[i],bool) or not isinstance(rads[i],(int,float)) or not math.isfinite(rads[i]) or rads[i]<0 for i in indices):return None
    result={k:[values[i] if i<len(values) else None for i in indices] for k,values in hours.items() if isinstance(values,list)}
    result['time']=[parsed[i].isoformat() for i in indices]
    return result


def refresh(only=None):
    now=datetime.datetime.now(datetime.timezone.utc).isoformat()
    current={'created_utc':now,'mode':'LIVE FETCH ATTEMPT','purpose':'advisory only','feeds':{}}
    previous={}
    if CACHE.exists():
        try:previous=json.loads(CACHE.read_text()).get('feeds',{})
        except (OSError, ValueError):pass
    for key,func in FUNCTIONS.items():
        if only and key not in only:
            if key in previous:current['feeds'][key]=previous[key]
            else:current['feeds'][key]={'status':'UNAVAILABLE','error':'Not fetched; no cached data'}
            continue
        try:
            result=func()
            fetched=datetime.datetime.now(datetime.timezone.utc).isoformat()
            payload=json.dumps(result,sort_keys=True,allow_nan=False).encode()
            digest=hashlib.sha256(payload).hexdigest()
            receipt_dir=ROOT/'live'/'receipts';receipt_dir.mkdir(parents=True,exist_ok=True)
            (receipt_dir/(digest+'.json')).write_bytes(payload)
            current['feeds'][key]={'status':'LIVE_RETRIEVED','fetched_utc':fetched,'sha256':digest,'receipt_scope':'normalized adapter output, not original provider response','result':result}
            print(key, 'LIVE_RETRIEVED')
        except Exception as exc:
            old=previous.get(key)
            if old and old.get('status') in ('LIVE_RETRIEVED','STALE_CACHE'):
                current['feeds'][key]=dict(old,status='STALE_CACHE',error=str(exc)[:240]);print(key,'STALE_CACHE')
            else:
                current['feeds'][key]={'status':'UNAVAILABLE', 'fetched_utc':now,'error':str(exc)[:240]}
                print(key,'UNAVAILABLE:',str(exc)[:100])
    current['forecast']=current['feeds'].get('forecast',{}).get('result') if current['feeds'].get('forecast',{}).get('status')=='LIVE_RETRIEVED' else None
    current=feed_view(current)
    CACHE.parent.mkdir(parents=True,exist_ok=True)
    CACHE.write_text(json.dumps(current,indent=2,allow_nan=False)+'\n')
    return current

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--only',nargs='*',choices=list(FUNCTIONS))
    ap.add_argument('--output',default=str(CACHE))
    args=ap.parse_args()
    data=refresh(args.only)
    dest=pathlib.Path(args.output)
    if dest!=CACHE:dest.write_text(json.dumps(data,indent=2)+'\n')
    print('Saved',dest,'; active feeds:',sum(v.get('status')=='LIVE_RETRIEVED' for v in data['feeds'].values()))
if __name__=='__main__':main()
