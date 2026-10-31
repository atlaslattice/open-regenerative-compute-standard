"""Ideal absorbing planar electrostatic retarder, NOT a collector hardware model.
Relativistic test particle with nominal alpha mass. MV * elementary charge = MeV.
"""
import math

def planar(T,mu,charge_e,deltaV_MV,mass_MeV):
 for x in [T,mu,charge_e,deltaV_MV,mass_MeV]:
  if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x):raise ValueError('finite scalar required')
 if T<0 or not 0<mu<=1 or charge_e<0 or mass_MeV<=0:raise ValueError('invalid incoming particle')
 p2=T*(T+2*mass_MeV);total=mass_MeV+T
 transverse_mass=math.sqrt(mass_MeV**2+p2*(1-mu**2))
 available=p2*mu**2/(total+transverse_mass)
 barrier=charge_e*deltaV_MV;difference=available-barrier
 tol=64*math.ulp(1.)*max(1.,T,abs(barrier))
 common={'normal_available_MeV':available,'barrier_MeV':barrier,'temporary_turning_transfer_MeV':0.}
 if abs(difference)<=tol:
  return dict(common,status='MARGINAL_NOT_COLLECTED',circuit_work_MeV=0.,electrode_heat_MeV=0.,returned_kinetic_MeV=0.,deferred_kinetic_MeV=T,exit_normal_momentum_MeV=None)
 if difference<0:
  # Positive retarder: after an ideal return to the launch potential, the field
  # gives back its temporary energy transfer. Net circuit work is ZERO.
  return dict(common,status='REFLECTED_AND_RETURNED',circuit_work_MeV=0.,electrode_heat_MeV=0.,returned_kinetic_MeV=T,deferred_kinetic_MeV=0.,exit_normal_momentum_MeV=-math.sqrt(p2)*mu,temporary_turning_transfer_MeV=available)
 residual=T-barrier
 pz=math.sqrt(max(0.,difference*(total-barrier+transverse_mass)))
 return dict(common,status='COLLECTED_IDEAL_PLANE',circuit_work_MeV=barrier,electrode_heat_MeV=residual,returned_kinetic_MeV=0.,deferred_kinetic_MeV=0.,exit_normal_momentum_MeV=pz)

def midpoint_potential_gain(T,mu,mass,steps):
 """Independent quadrature of dz/dt = pz/E during a uniform-E turning leg.
 Integration variable s is lost normal momentum: dpz/ds=-1, d(qPhi)/ds=pz/E.
 No physical gap, time or field magnitude inferred.
 """
 p=math.sqrt(T*(T+2*mass));pz=p*mu;pt2=p*p*(1-mu*mu);h=pz/steps
 return sum((pz-(i+.5)*h)/math.sqrt(mass*mass+pt2+(pz-(i+.5)*h)**2)*h for i in range(steps))

def apparatus_gate():
 return {'status':'BLOCKED_UNSPECIFIED_COLLECTOR_AND_SOURCE_INTERFACES','missing':['actual_target_birth_exit_space_time','post_material_charge_state_distribution','electrode_geometry_and_apertures','self_consistent_E_B_field_and_sheaths','space_charge_electrons_and_secondary_emission','circuit_load_bias_startup_and_leakage','material_electrode_losses_and_thermal_recovery','absolute_shot_source_and_all_facility_inputs'],'net_wall_plug_J':None}
