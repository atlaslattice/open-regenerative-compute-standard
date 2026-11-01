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
 return {'beam_kinetic_input_J':beam_J,'nuclear_release_J':nuclear_Q_J,'alpha_birth_kinetic_J':alpha_birth_J,'ideal_alpha_circuit_J':ideal_circuit_J,'non_alpha_energy_by_conservation_J':beam_J+nuclear_Q_J-alpha_birth_J,'maximum_downstream_beam_plus_nuclear_output_J':beam_J+nuclear_Q_J,'nuclear_release_over_beam_kinetic':nuclear_Q_J/beam_J,'source_loss_uncredited_necessary_eta_for_nonnegative_net':beam_J/(beam_J+nuclear_Q_J),'source_loss_uncredited_threshold_scope':'Downstream recovery perfect, source-conversion-loss electric credit zero, auxiliary net draw zero, cyclic storage; not universal whole-facility bound','all_input_recovery_energy_only_net_upper_bound_J':nuclear_Q_J,'all_input_recovery_scope':'Perfect electrical return of source/auxiliary conversion losses AND all downstream beam energy, no stored-energy depletion, no unmodeled energy sources. Energy-only upper bound; thermal/exergy feasibility NOT established.','alpha_direct_only_no_other_credits_required_source_efficiency':None if ideal_circuit_J==0 else beam_J/ideal_circuit_J,'alpha_direct_only_possible_even_if_source_losses_fully_electrically_recovered':ideal_circuit_J>beam_J}

def conditional_facility(frontier,facility):
 direct=facility['wall_to_beam_fraction'];optical=facility['wall_to_laser_fraction'];coupling=facility['laser_to_beam_fraction']
 if direct is not None and (optical is not None or coupling is not None):raise ValueError('choose direct or optical-chain source accounting, not both')
 for name,value in [('wall_to_beam',direct),('wall_to_laser',optical),('laser_to_beam',coupling)]:
  if value is not None:fraction(value,name,True)
 eta=direct if direct is not None else (None if optical is None or coupling is None else optical*coupling)
 p=facility['fired_fraction_per_attempt'];rate=facility['attempt_rate_Hz'];ra=facility['other_alpha_electric_recovery_fraction'];rb=facility['non_alpha_electric_recovery_fraction'];rs=facility.get('source_conversion_loss_electric_recovery_fraction');du=facility['stored_energy_change_J_per_attempt']
 for name,value in [('fired_fraction',p),('other_alpha_recovery',ra),('non_alpha_recovery',rb),('source_conversion_loss_recovery',rs)]:
  if value is not None:fraction(value,name)
 if rate is not None:nonnegative(rate,'attempt rate')
 if du is not None:finite(du,'stored energy change')
 idle=facility.get('source_driver_idle_preparation_wall_J_per_attempt');idle_r=facility.get('source_idle_loss_electric_recovery_fraction')
 if idle is not None:nonnegative(idle,'source idle/preparation wall draw')
 if idle_r is not None:fraction(idle_r,'source idle recovery')
 ids=set();missing=[];base=0.;perfire=0.;base_recovery=0.;fire_recovery=0.
 for load in facility['loads']:
  instance=load['physical_instance_id']
  if instance in ids or instance==facility['source_driver_physical_instance_id']:raise ValueError('duplicate physical-instance/source energy accounting')
  ids.add(instance);r=load.get('own_wall_loss_electric_recovery_fraction')
  if r is None:missing.append(instance+'.own_wall_loss_electric_recovery_fraction')
  else:fraction(r,instance+' own-loss recovery')
  for name in ['wall_J_per_attempt','wall_J_per_fired']:
   value=load[name]
   if value is None:missing.append(instance+'.'+name)
   else:
    nonnegative(value,name)
    if name=='wall_J_per_attempt':
     base+=value
     if r is not None:base_recovery+=r*value
    else:
     perfire+=value
     if r is not None:fire_recovery+=r*value
 missing += [name for name,value in [('wall_to_beam_efficiency_or_complete_chain',eta),('fired_fraction_per_attempt',p),('attempt_rate_Hz',rate),('other_alpha_recovery',ra),('non_alpha_recovery',rb),('source_conversion_loss_recovery',rs),('source_driver_idle_preparation_wall',idle),('source_idle_loss_recovery',idle_r),('stored_energy_change',du)] if value is None]
 eb=frontier['beam_kinetic_input_J'];q=frontier['nuclear_release_J'];ab=frontier['alpha_birth_kinetic_J'];d=frontier['ideal_alpha_circuit_J']
 downstream=None if ra is None or rb is None else d+ra*(ab-d)+rb*(eb+q-ab)
 source_wall=None if eta is None else eb/eta;source_remainder=None if source_wall is None else source_wall-eb
 source_recovered=None if rs is None or source_remainder is None else rs*source_remainder
 load_complete=not any('.wall_' in x or '.own_wall_' in x for x in missing)
 wall=None if source_wall is None or p is None or idle is None or not load_complete else idle+base+p*(source_wall+perfire)
 output=None if p is None or downstream is None or source_recovered is None or idle is None or idle_r is None or not load_complete else idle*idle_r+base_recovery+p*(downstream+source_recovered+fire_recovery)
 raw=None if wall is None or output is None else output-wall
 formal=None if raw is None or du is None else raw+du;adapter=du is not None and du!=0;adjusted=raw if raw is not None and du==0 else None
 return {'status':'INCOMPLETE_FACILITY_INPUTS' if missing else 'NONCYCLIC_STORAGE_REQUIRES_FLOW_ADAPTER' if adapter else 'CONDITIONAL_SUPPLIED_SCENARIO_NOT_VALIDATED','missing':missing,'source_driver_idle_preparation_wall_J_per_attempt':idle,'source_idle_electric_recovery_J_per_attempt':None if idle is None or idle_r is None else idle*idle_r,'source_efficiency':eta,'source_gross_wall_J_per_fired':source_wall,'source_conversion_energy_remainder_J_per_fired':source_remainder,'source_conversion_electric_recovery_J_per_fired':source_recovered,'downstream_electric_J_per_fired':downstream,'known_auxiliary_wall_subtotal_J_per_attempt':base,'known_auxiliary_wall_subtotal_J_per_fired':perfire,'known_auxiliary_own_loss_recovery_J_per_attempt':base_recovery,'known_auxiliary_own_loss_recovery_J_per_fired':fire_recovery,'wall_electric_J_per_attempt':wall,'output_electric_J_per_attempt':output,'raw_net_electric_J_per_attempt':raw,'formal_storage_correction_if_all_flows_were_measured_J':formal,'noncyclic_storage_adapter_required':adapter,'storage_neutral_net_J_per_attempt':adjusted,'storage_neutral_net_W':None if adjusted is None or rate is None else adjusted*rate,'recovery_scope':'Source and auxiliary credits recover only their OWN wall-input remainder; do not re-credit beam/alpha heat here. No remainder is automatically heat or electricity. Thermal/exergy applicability remains unresolved.','readiness_interpretation':'Firing changes throughput and amortizes attempt costs; changed per-fired source/target conditions require a new physics run.'}
