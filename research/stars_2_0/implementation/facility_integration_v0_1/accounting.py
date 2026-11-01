"""Conditional source/collector/facility accounting with explicit missing values."""
import math

def finite(x,name):
 if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x):raise ValueError('finite '+name+' required')
 return x

def nonnegative(x,name):
 if finite(x,name)<0:raise ValueError('negative '+name)
 return x

def fraction(x,name,positive=False):
 finite(x,name)
 if not (0<x<=1 if positive else 0<=x<=1):raise ValueError('invalid fraction '+name)
 return x

def energy_frontier(beam_J,nuclear_Q_J,alpha_birth_J,ideal_circuit_J):
 for key,value in [('beam',beam_J),('Q',nuclear_Q_J),('alpha birth',alpha_birth_J),('ideal circuit',ideal_circuit_J)]:nonnegative(value,key)
 if beam_J<=0 or alpha_birth_J>beam_J+nuclear_Q_J or ideal_circuit_J>alpha_birth_J:raise ValueError('inconsistent energy partition')
 max_total=beam_J+nuclear_Q_J
 eta_all=beam_J/max_total
 return {'beam_kinetic_input_J':beam_J,'nuclear_release_J':nuclear_Q_J,'alpha_birth_kinetic_J':alpha_birth_J,'ideal_alpha_circuit_J':ideal_circuit_J,'non_alpha_energy_by_conservation_J':max_total-alpha_birth_J,'maximum_all_energy_output_J':max_total,'nuclear_release_over_beam_kinetic':nuclear_Q_J/beam_J,'necessary_wall_to_beam_efficiency_for_nonnegative_net_optimistic':eta_all,'strict_positive_requires_efficiency_greater_than_threshold':True,'alpha_direct_only_required_source_efficiency':None if ideal_circuit_J==0 else beam_J/ideal_circuit_J,'alpha_direct_only_possible_with_efficiency_at_most_one':ideal_circuit_J>beam_J,'scope':'Best-case bounds for this fixed fired-source control, zero auxiliary draw, zero storage change, all source energy enclosed/recovered; not a calibrated apparatus prediction'}

def conditional_facility(frontier,facility):
 # Every cost is a wall-electric draw. Unique physical instances prevent silent
 # duplicate hardware charges; direct source drive is booked only via efficiency.
 direct=facility['wall_to_beam_fraction'];optical=facility['wall_to_laser_fraction'];coupling=facility['laser_to_beam_fraction']
 if direct is not None and (optical is not None or coupling is not None):raise ValueError('choose direct or optical-chain source accounting, not both')
 for name,value in [('wall_to_beam',direct),('wall_to_laser',optical),('laser_to_beam',coupling)]:
  if value is not None:fraction(value,name,True)
 eta=direct if direct is not None else (None if optical is None or coupling is None else optical*coupling)
 p=facility['fired_fraction_per_attempt'];rate=facility['attempt_rate_Hz'];ra=facility['other_alpha_electric_recovery_fraction'];rb=facility['non_alpha_electric_recovery_fraction'];du=facility['stored_energy_change_J_per_attempt']
 for name,value in [('fired_fraction',p),('other_alpha_recovery',ra),('non_alpha_recovery',rb)]:
  if value is not None:fraction(value,name)
 if rate is not None:nonnegative(rate,'attempt rate')
 if du is not None:finite(du,'stored energy change')
 loads=facility['loads'];ids=set();missing=[];base=0.;perfire=0.
 for l in loads:
  instance=l['physical_instance_id']
  if instance in ids or instance==facility['source_driver_physical_instance_id']:raise ValueError('duplicate physical-instance/source energy accounting')
  ids.add(instance)
  for name in ['wall_J_per_attempt','wall_J_per_fired']:
   value=l[name]
   if value is None:missing.append(instance+'.'+name)
   else:
    nonnegative(value,name)
    if name=='wall_J_per_attempt':base+=value
    else:perfire+=value
 missing += [name for name,value in [('wall_to_beam_efficiency_or_complete_chain',eta),('fired_fraction_per_attempt',p),('attempt_rate_Hz',rate),('other_alpha_recovery',ra),('non_alpha_recovery',rb),('stored_energy_change',du)] if value is None]
 eb=frontier['beam_kinetic_input_J'];q=frontier['nuclear_release_J'];ab=frontier['alpha_birth_kinetic_J'];d=frontier['ideal_alpha_circuit_J']
 # Unknown p=0 or recovery=0 terms may be mathematically immaterial, but retain
 # a complete-data gate so a physically unspecified profile never becomes valid.
 output_per_fired=None if ra is None or rb is None else d+ra*(ab-d)+rb*(eb+q-ab)
 wall_per_attempt=None if eta is None or p is None or any('.wall_' in x for x in missing) else base+p*(eb/eta+perfire)
 output_per_attempt=None if p is None or output_per_fired is None else p*output_per_fired
 raw_net=None if output_per_attempt is None or wall_per_attempt is None else output_per_attempt-wall_per_attempt
 adjusted=None if raw_net is None or du is None else raw_net+du
 return {'status':'INCOMPLETE_FACILITY_INPUTS' if missing else 'CONDITIONAL_SUPPLIED_SCENARIO_NOT_VALIDATED','missing':missing,'source_efficiency':eta,'known_auxiliary_wall_subtotal_J_per_attempt':base,'known_auxiliary_wall_subtotal_J_per_fired':perfire,'output_electric_J_per_fired':output_per_fired,'wall_electric_J_per_attempt':wall_per_attempt,'output_electric_J_per_attempt':output_per_attempt,'raw_net_electric_J_per_attempt':raw_net,'storage_neutral_net_J_per_attempt':adjusted,'storage_neutral_net_W':None if adjusted is None or rate is None else adjusted*rate,'readiness_interpretation':'Firing fraction changes throughput and amortizes attempt costs. This fixed per-fired event bank has no inferred acoustic/jitter gain. A changed source/target state requires a new physics run.'}
