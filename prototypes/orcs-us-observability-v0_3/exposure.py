"""Synthetic hazard-to-facility proximity candidate screening; NOT an outage forecast."""
from math import radians,sin,cos,asin,sqrt

def distance_km(a,b):
    x1,y1=a['lat'],a['lon'];x2,y2=b['lat'],b['lon']
    if not all(-90<=lat<=90 for lat in (x1,x2)) or not all(-180<=lon<=180 for lon in (y1,y2)):
        raise ValueError('Invalid coordinates')
    dlat=radians(x2-x1);dlon=radians(y2-y1)
    h=sin(dlat/2)**2+cos(radians(x1))*cos(radians(x2))*sin(dlon/2)**2
    return 12742*asin(min(1,sqrt(h)))

def proximity_candidates(events,assets,threshold_km):
    if threshold_km<0:raise ValueError('Negative threshold')
    items=[]
    for event in events:
        for asset in assets:
            dist=distance_km(event,asset)
            if dist<=threshold_km:
                items.append({'event':event['id'],'asset':asset['id'],'distance_km':round(dist,2),
                              'status':'HUMAN_EXPOSURE_REVIEW_REQUIRED','closure_verified':False,
                              'route_impairment_verified':False})
    return sorted(items,key=lambda x:(x['distance_km'],x['asset'],x['event']))

if __name__=='__main__':
    import json
    events=[{'id':'SYNTH_HAZARD','lat':29.75,'lon':-95.36}]
    assets=[{'id':'SYNTH_TX_TERMINAL','lat':29.8,'lon':-95.4},{'id':'SYNTH_EAST_ASSET','lat':40.7,'lon':-74.0}]
    print(json.dumps(proximity_candidates(events,assets,50),indent=2))
