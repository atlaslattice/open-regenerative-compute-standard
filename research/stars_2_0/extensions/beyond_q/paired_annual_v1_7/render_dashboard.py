"""Offline research dashboard from CSVs. No network or runtime dependencies."""
import json
import compare as c

def normalize(row):
    result={}
    for k,v in row.items():
        if v=='':result[k]=None
        else:
            try:result[k]=float(v)
            except ValueError:result[k]=v
    return result

def main():
    data={k:[normalize(r) for r in c.readcsv(c.OUT/f)] for k,f in [('source','annual_isotopes.csv'),('energy','annual_energy.csv'),('daily','daily_reference.csv')]}
    keep_source={'configuration','blanket_mode','schedule','T_unserved_B_burn_kg','A_primary_DD_flattop_MW','B_DT_flattop_MW','B_gross_TBR_assumed','year_T_DD_birth_kg','year_T_B_burn_kg','year_T_inventory_change_kg','T_final_total_kg','T_final_B_storage_kg','He3_stored_candidate_kg','He4_stored_candidate_kg','He3_sale_candidate_kg'}
    data['source']=[{k:v for k,v in r.items() if k in keep_source} for r in data['source']]
    keep_energy={'configuration','blanket_mode','schedule','energy_case','mean_net_MW','year_mean_net_MW','startup_import_kWh','year_import_kWh'}
    data['energy']=[{k:v for k,v in r.items() if k in keep_energy} for r in data['energy']]
    data['daily']=[r for r in data['daily'] if r['time_hours']%168==0 or r['time_hours']==8934]
    html='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Beyond Q paired annual accounting</title>
<style>body{font:16px system-ui;margin:24px auto;padding:0 18px;max-width:1100px;color:#142e3e;background:#f6f8fa}h1{font-size:28px}select{padding:8px;max-width:100%;margin:5px}table{border-collapse:collapse;width:100%;background:white;margin:15px 0}td,th{text-align:left;padding:9px;border-bottom:1px solid #dde4e9}th{font-size:14px}canvas{width:100%;background:white;border:1px solid #dde4e9}aside{padding:14px;background:#e7eef3;border-left:4px solid #436a80}small{color:#455965}a{color:#176686}#status{font-weight:600}</style>
<h1>Beyond Q — paired annual accounting</h1><aside>Conditional research scenarios. Fusion power, retrofit demand and recovery remain unvalidated. B's default lithium breeding replaces its burn before losses; A supplies startup and loss makeup. Tritium sales are disabled. All physical gates remain open.</aside>
<p><label>Configuration <select id="config"></select></label><label>Blanket <select id="blanket"></select></label><label>Schedule <select id="schedule"></select></label></p>
<p id="status"></p><div id="isotopes"></div><h2>Electricity sensitivities</h2><p>Mean net power includes startup and the following year. Positive energy is before export qualification. ARC A draw is a net retrofit-load assumption; laser gains are assumptions.</p><div id="energy"></div><h2>Continuous-reference stocks</h2><canvas id="chart" width="1100" height="350" aria-label="Stored isotope masses over time"></canvas><p id="chartnote"></p>
<p><a href="REPORT.md">Technical report</a> · <a href="outputs/annual_isotopes.csv">Isotope CSV</a> · <a href="outputs/annual_energy.csv">Electricity CSV</a> · <a href="outputs/economics_sensitivity.csv">Economic assumptions CSV</a></p><small>365.25-day calendar year; 7-day A-only precharge except cold startup. ARC duty 15/16 is cycle averaged; matched laser duty is a normalization control. He-4 is candidate recovered feedstock, not certified research grade or free cooling.</small>
<script>const DATA=__DATA__;
const $=x=>document.getElementById(x),fmt=x=>x===null||x===undefined?'UNRESOLVED':Number(x).toLocaleString(undefined,{maximumFractionDigits:3});
for(const [id,key] of [['config','configuration'],['blanket','blanket_mode'],['schedule','schedule']]){for(const v of [...new Set(DATA.source.map(r=>r[key]))]){const o=document.createElement('option');o.value=v;o.textContent=v;$(id).appendChild(o);}$(id).onchange=draw;}
function draw(){const match=r=>r.configuration===$('config').value&&r.blanket_mode===$('blanket').value&&r.schedule===$('schedule').value;const r=DATA.source.find(match);$('status').textContent='Unserved B tritium: '+fmt(r.T_unserved_B_burn_kg)+' kg — '+(r.T_unserved_B_burn_kg>1e-8?'fuel shortfall in this scenario':'no modeled fuel shortfall; physical qualification unresolved');
const fields=[['A primary DD / B DT flattop MW',fmt(r.A_primary_DD_flattop_MW)+' / '+fmt(r.B_DT_flattop_MW)],['B assumed gross TBR',fmt(r.B_gross_TBR_assumed)],['Operating-year direct T birth / B burn (kg)',fmt(r.year_T_DD_birth_kg)+' / '+fmt(r.year_T_B_burn_kg)],['Operating-year T stock change (kg)',fmt(r.year_T_inventory_change_kg)],['Final T stock / B storage (kg)',fmt(r.T_final_total_kg)+' / '+fmt(r.T_final_B_storage_kg)],['Captured He-3 / plasma He-4 candidate (kg)',fmt(r.He3_stored_candidate_kg)+' / '+fmt(r.He4_stored_candidate_kg)],['He-3 terminal sale candidate (kg)',fmt(r.He3_sale_candidate_kg)],['Qualified isotope output / actual profit','UNRESOLVED']];$('isotopes').innerHTML='<table>'+fields.map(a=>'<tr><th>'+a[0]+'</th><td>'+a[1]+'</td></tr>').join('')+'</table>';
$('energy').innerHTML='<table><tr><th>Assumed case</th><th>Window mean MW</th><th>B-year mean MW</th><th>Startup import GWh</th><th>Year import GWh</th></tr>'+DATA.energy.filter(match).map(e=>'<tr><td>'+e.energy_case+'</td><td>'+fmt(e.mean_net_MW)+'</td><td>'+fmt(e.year_mean_net_MW)+'</td><td>'+fmt(e.startup_import_kWh===null?null:e.startup_import_kWh/1e6)+'</td><td>'+fmt(e.year_import_kWh===null?null:e.year_import_kWh/1e6)+'</td></tr>').join('')+'</table>';
const ctx=$('chart').getContext('2d');ctx.clearRect(0,0,1100,350);const rows=DATA.daily.filter(d=>d.configuration===r.configuration&&d.blanket_mode===r.blanket_mode);if(r.schedule!=='continuous'){$('chartnote').textContent='Daily plots are saved for the continuous reference only. Selected outage results are in the tables above.';return;}$('chartnote').textContent='Retained T total (blue), captured He-3 candidate (green), captured plasma He-4 candidate (orange), kg. Includes A-only startup; weekly samples, full daily values in CSV.';
const series=[['T_total_kg','#315d87'],['He3_stored_candidate_kg','#387951'],['He4_stored_candidate_kg','#aa6639']];const maxY=Math.max(1,...rows.flatMap(d=>series.map(([k])=>d[k])))*1.08,maxX=rows[rows.length-1].time_hours/24;ctx.font='14px system-ui';ctx.fillStyle='#142e3e';ctx.strokeStyle='#ccd5dc';for(let j=0;j<=4;j++){let y=300-j*65;ctx.beginPath();ctx.moveTo(65,y);ctx.lineTo(1070,y);ctx.stroke();ctx.fillText((maxY*j/4).toFixed(0)+' kg',5,y+5);}for(const [key,color] of series){ctx.strokeStyle=color;ctx.lineWidth=2.5;ctx.beginPath();rows.forEach((d,i)=>{const x=65+d.time_hours/24/maxX*1005,y=300-d[key]/maxY*260;i?ctx.lineTo(x,y):ctx.moveTo(x,y);});ctx.stroke();}ctx.fillStyle='#142e3e';ctx.fillText('Day 0',65,330);ctx.fillText('Day '+maxX.toFixed(1),980,330);}
draw();</script></html>'''
    (c.ROOT/'dashboard.html').write_text(html.replace('__DATA__',json.dumps(data,separators=(',',':')).replace('</','<\\/')))
if __name__=='__main__':main()
