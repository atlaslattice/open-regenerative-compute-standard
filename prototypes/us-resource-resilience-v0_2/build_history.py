from pathlib import Path
import json,shutil,re,hashlib
p=Path(__file__).resolve().parent;root=p.parents[1]
receipts=json.loads((root/'data/circular_economy_v0_6/mineral_43_chapter_receipts.json').read_text());chap={r['commodity']:r for r in receipts['chapters']}
# Manually reviewed row mapping. Arrays are validated against exact source-table tokens below.
mapping={
'refined_copper':('copper',{'consumption':[1750,1720,1580,1580,1700],'primary':[931,917,843,882,790],'secondary':[49,40,39,39,60],'imports':[919,732,771,903,1700],'exports':[48,27,29,72,110],'reported_inventory':[117,84,128,123,450]}),
'aluminum':('aluminum',{'consumption':[6240,6910,6210,5830,5700],'primary':[889,861,750,676,660],'secondary':[1520,1480,1560,1560,1600],'imports':[4940,5730,4900,4840,4400],'exports':[900,1040,1240,1360,890],'reported_inventory':[1870,2050,1820,1690,1800]}),
'potash':('potash',{'consumption':[6900,5100,5900,6200,5900],'primary':[480,430,390,410,500],'imports':[6480,4940,5620,5970,5600],'exports':[112,267,157,150,170]}),
'phosphate_rock':('phosphate',{'consumption':[24400,22300,22600,22500,21000],'primary':[21600,19800,19600,19400,20000],'imports':[2460,2500,2590,3390,3400],'reported_inventory':[10700,10600,9550,8740,8400]}),
'zinc_refined':('zinc',{'consumption':[908,974,921,808,820],'primary':[220]*5,'imports':[701,762,705,590,600],'exports':[13,8,3,2,2],'reported_inventory':[114,133,105,110,110]})}
base=json.loads((p/'national_ledger.json').read_text());byid={r['id']:r for r in base};history=[]
for id,(commodity,a) in mapping.items():
 receipt=chap[commodity]; text=receipt['salient_table_text'];tokens={float(x.replace(',','')) for x in re.findall(r'(?<!\w)[0-9][0-9,]*(?:\.[0-9]+)?',text)}
 for ar in a.values():
  assert all(float(v) in tokens for v in ar),(id,ar)
 scale=1000 if byid[id]['unit'].startswith('million') else .001
 # All source tables are thousand metric tons; million-tonne ledger rows divide by 1000.
 out=[(v+a.get('secondary',[0]*5)[i])/scale for i,v in enumerate(a['primary'])]
 assert abs(out[-1]-byid[id]['domestic_output_or_proxy'])<1e-8,(id,out[-1],byid[id])
 assert abs(a['consumption'][-1]/scale-byid[id]['annual_consumption'])<1e-8
 observations=[]
 for i,year in enumerate(range(2021,2026)):
  observations.append({'year':year,'consumption':a['consumption'][i]/scale,'domestic_output_or_proxy':out[i],**{k:(v[i]/scale) for k,v in a.items() if k in ['imports','exports','reported_inventory']},'status':'REPORTED / 2025 ESTIMATED' if year==2025 else 'REPORTED'})
 history.append({'id':id,'unit':byid[id]['unit'],'observations':observations,'consumption_cagr':(observations[-1]['consumption']/observations[0]['consumption'])**.25-1,'production_cagr':(out[-1]/out[0])**.25-1,'source':receipt,'certified_reserve':None,'limitations':'Archived original federal PDF; current federal byte equivalence unverified. Reported inventories are not certified deliverable reserves. Four-year CAGR is descriptive, not a long-term forecast.'})
(p/'historical_series.json').write_text(json.dumps(history,indent=2))
print('Five histories / 25 material-year observations validated against existing ledger endpoints.')
