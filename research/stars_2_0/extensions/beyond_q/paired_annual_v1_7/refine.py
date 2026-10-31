"""Temporal disagreement screen; not parameter calibration or physical validation."""
import json
import compare as c
from pairedcycle.model import simulate

def main():
    i=json.loads((c.ROOT/'inputs.json').read_text());rows=[]
    for config in (i['configurations'][0],i['configurations'][2]):
        pre=i['precharge_hours'];schedule=c.schedules('A_90day',pre,8766)
        finals=[]
        for step in (1/96,1/192):
            p=c.parameters(config,'zero_breeding',pre,8766,step);tr,s=simulate(p,schedule)
            finals.append(dict(step_minutes=step*1440,unserved_T_kg=s['b_unserved_burn_kg'],final_T_kg=tr[-1]['total_inventory']))
        rows.append(dict(configuration=config['id'],coarse=finals[0],fine=finals[1],unserved_difference_kg=finals[1]['unserved_T_kg']-finals[0]['unserved_T_kg'],final_T_difference_kg=finals[1]['final_T_kg']-finals[0]['final_T_kg']))
    (c.OUT/'timestep_comparison.json').write_text(json.dumps(rows,indent=2)+'\n')
    print(json.dumps(rows,indent=2))
if __name__=='__main__':main()
