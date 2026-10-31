"""Signed terminal V*I accounting; no generic fusion-to-electric efficiency."""
import math

def number(x):
 if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x):raise ValueError('finite numeric value required')
 return x

def terminal_ledger(terminals,incident_W=None):
 if incident_W is not None and number(incident_W)<0:raise ValueError('negative incident power')
 ids=set();powers=[]
 for t in terminals:
  if not isinstance(t['id'],str) or not t['id'] or t['id'] in ids:raise ValueError('unique terminal IDs required')
  ids.add(t['id']);V=number(t['voltage_V']);I=number(t['net_positive_charge_current_into_electrode_A'])
  powers.append({'id':t['id'],'signed_power_out_W':V*I})
 net=math.fsum(t['signed_power_out_W'] for t in powers)
 return {'terminal_powers':powers,'terminal_gross_out_W':math.fsum(max(0.,t['signed_power_out_W']) for t in powers),'terminal_external_draw_W':-math.fsum(min(0.,t['signed_power_out_W']) for t in powers),'net_terminal_out_W':net,'net_fraction_of_declared_incident_power':None if incident_W is None or incident_W==0 else net/incident_W,'incident_minus_net_terminal_W':None if incident_W is None else incident_W-net,'remainder_interpretation':'Arithmetic remainder; not automatically heat. Missing loss channels and boundary definition must be resolved.','wall_plug_net_power_W':None}
