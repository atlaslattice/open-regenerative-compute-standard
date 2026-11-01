"""Run: python run.py [--years N] [--modules 1 50] [--step-days .25]."""
from pathlib import Path
import argparse,csv,json,hashlib,platform,time
import numpy as np
from model import simulate
from finance import connected_financials

ROOT=Path(__file__).resolve().parent
def write(path,rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def dashboard(rows,path):
    # Self-contained, no network dependencies; money is conditional, never profit.
    payload=json.dumps(rows).replace('</','<\\/')
    path.write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><title>Beyond Q module/fleet v2.0</title>
<style>body{font:16px system-ui;margin:28px;max-width:1200px;background:#f5f7fa;color:#192f43}select{padding:8px}canvas{background:white;width:100%;height:350px}table{border-collapse:collapse;width:100%}td,th{padding:8px;border-bottom:1px solid #ccd}p{max-width:1000px}</style>
<h1>Beyond Q: reactor and isotope fleet</h1><p>ASSUMED SCENARIOS — G1–G5 OPEN. No GPU/QPU revenue. Product quantities and revenue are conditional; housing and operating costs remain unresolved. Recovery scenarios include lumped losses once.</p>
<label>Modules <select id="fleet"></select></label> <label>Overall He-3 recovery <select id="recovery"></select></label> <label>Plot <select id="metric"><option value="He3_product_candidate_STP_L">He-3 product candidate (STP L/year)</option><option value="electricity_net_MWh">Net electricity (MWh/year)</option><option value="T_stock_end_kg">Tritium stock (kg)</option><option value="revenue_less_known_charges_USD">Revenue less known charges ($/year; NOT profit)</option></select></label>
<canvas id="plot" width="1100" height="350"></canvas><div id="detail"></div><script>const data='''+payload+''';
const $=id=>document.getElementById(id);for(const v of [...new Set(data.map(x=>x.fleet_modules))])$('fleet').add(new Option(v,v));for(const v of [...new Set(data.map(x=>x.He3_overall_recovery_assumed))])$('recovery').add(new Option((100*v)+'%',v));$('recovery').value='0.75';
function draw(){const rows=data.filter(x=>x.price_case=='requested_prices'&&x.offtake_case=='fleet_cap_stress'&&x.fleet_modules==$('fleet').value&&x.He3_overall_recovery_assumed==$('recovery').value),k=$('metric').value,c=$('plot').getContext('2d');c.clearRect(0,0,1100,350);let lo=Math.min(0,...rows.map(x=>x[k])),hi=Math.max(1,...rows.map(x=>x[k]));c.font='13px system-ui';for(let j=0;j<=4;j++){let y=300-65*j;c.strokeStyle='#ccd';c.beginPath();c.moveTo(100,y);c.lineTo(1080,y);c.stroke();c.fillText((lo+(hi-lo)*j/4).toLocaleString(undefined,{maximumFractionDigits:0}),4,y);}c.strokeStyle='#247a73';c.lineWidth=2;c.beginPath();rows.forEach((r,i)=>{let x=100+i/Math.max(1,rows.length-1)*980,y=300-(r[k]-lo)/(hi-lo)*260;i?c.lineTo(x,y):c.moveTo(x,y)});c.stroke();c.fillStyle='#192f43';c.fillText('Year 1',100,330);c.fillText('Year '+rows.length,1000,330);$('detail').innerHTML='<table><tr><th>Year</th><th>He-3 candidate L</th><th>T export scenario kg</th><th>Net MWh</th><th>Import MWh</th><th>Actual profit</th></tr>'+rows.filter((x,i)=>i==0||[9,29,30,59].includes(i)).map(r=>'<tr><td>'+r.year+'</td><td>'+Math.round(r.He3_product_candidate_STP_L).toLocaleString()+'</td><td>'+r.T_external_export_scenario_kg.toFixed(1)+'</td><td>'+Math.round(r.electricity_net_MWh).toLocaleString()+'</td><td>'+Math.round(r.electricity_import_MWh).toLocaleString()+'</td><td>UNRESOLVED</td></tr>').join('')+'</table>'}for(const id of ['fleet','recovery','metric'])$(id).onchange=draw;draw();</script></html>''')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--years',type=int);ap.add_argument('--modules',type=int,nargs='+');ap.add_argument('--step-days',type=float);ap.add_argument('--inputs',default=str(ROOT/'inputs.json'));ap.add_argument('--out',default='outputs');a=ap.parse_args()
    p=json.loads(Path(a.inputs).read_text())
    if a.years:p['years']=a.years
    if a.step_days:p['step_days']=a.step_days
    out=ROOT/a.out;out.mkdir(exist_ok=True);all_fin=[];checks=[];start=time.time()
    for n in a.modules or p['module_counts']:
        raw,checkpoints,check=simulate(p,n)
        write(out/f'module_ledger_{n}.csv',raw);write(out/f'fleet_inventory_{n}.csv',checkpoints)
        for r in p['He3_overall_recovery_cases']:
            for full in [False,True]:
                market=dict(p,offtake_case='He3_full_offtake_sensitivity' if full else 'fleet_cap_stress',
                    He3_market_cap_STP_L_per_year_fleet=None if full else p['He3_market_cap_STP_L_per_year_fleet'])
                all_fin+=connected_financials(raw,market,r)
                pressure=dict(market,price_case='price_pressure_500',He3_price_USD_per_STP_L=500.,T_price_USD_per_gram=500.)
                all_fin+=connected_financials(raw,pressure,r)
        checks.append(dict(modules=n,**check));print(json.dumps(checks[-1]),flush=True)
    write(out/'annual_products_finance.csv',all_fin);dashboard(all_fin,out/'dashboard.html')
    (out/'execution.json').write_text(json.dumps(dict(python=platform.python_version(),numpy=np.__version__,runtime_seconds=time.time()-start,checks=checks,inputs=p),indent=2)+'\n')
    paths=[Path(a.inputs),ROOT/'model.py',ROOT/'finance.py',ROOT/'run.py']
    (out/'input_code_hashes.json').write_text(json.dumps({path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in paths},indent=2)+'\n')
    print(f'Wrote {len(all_fin)} annual product/finance rows; {time.time()-start:.1f}s',flush=True)
if __name__=='__main__':main()
