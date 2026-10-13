from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import urllib.request,json,hashlib
from datetime import datetime,timezone
retrieved=datetime.now(timezone.utc).isoformat()
p=Path(__file__).resolve().parent;d=p/'receipts';d.mkdir(exist_ok=True)
urls={'usgs_quakes':'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson','noaa_space_weather':'https://services.swpc.noaa.gov/products/noaa-planetary-k-index.json','nws_weather':'https://api.weather.gov/points/30.2672,-97.7431','fema_disasters':'https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries?$top=1'}
def probe(pair):
 id,url=pair
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'AtlasLattice-Public-Research/0.2'})
  with urllib.request.urlopen(req,timeout=15) as r:b=r.read(2000000);status=r.status
  parsed=json.loads(b);(d/(id+'.json')).write_bytes(b)
  return {'id':id,'url':url,'http_status':status,'status':'FETCHED_JSON_SNAPSHOT','bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'retrieved_utc':retrieved,'browser_acceptance':'NOT_TESTED'}
 except Exception as e:return {'id':id,'url':url,'status':'FAILED_THIS_ENVIRONMENT','error':str(e)[:200],'retrieved_utc':retrieved}
r=list(ThreadPoolExecutor(max_workers=4).map(probe,urls.items()));(p/'public_feed_probe_receipts.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
