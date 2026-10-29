"""Conditional fixed-energy event-yield screen; not a target/laser/burn model."""
from decimal import Decimal
import math


def expected_events(rows, *, E_lab_MeV, incident_protons, B11_atoms_cm2):
    if isinstance(incident_protons,bool) or not isinstance(incident_protons,int) or incident_protons<0:raise ValueError('nonnegative integer proton count required')
    if isinstance(B11_atoms_cm2,bool) or not math.isfinite(B11_atoms_cm2) or B11_atoms_cm2<0:raise ValueError('finite nonnegative B11 areal inventory required')
    match=[r for r in rows if Decimal(r['E_lab_MeV'])==Decimal(str(E_lab_MeV))]
    if len(match)!=1:raise ValueError('Only exact source nodes supported; no invented interpolation/resonance')
    r=match[0]
    if r['observable']!='PUBLICATION_MODEL_EXTRAPOLATED_FUSION_EVENT_CROSS_SECTION':raise ValueError('event-cross-section semantics required')
    tau=r['sigma_event_b']*1e-24*B11_atoms_cm2
    p=-math.expm1(-tau)
    return {'E_lab_MeV':str(E_lab_MeV),'incident_protons':incident_protons,'B11_atoms_cm2':B11_atoms_cm2,
            'sigma_event_b':r['sigma_event_b'],'per_proton_event_probability':p,
            'expected_fusion_events':incident_protons*p,'expected_primary_alpha_births':3*incident_protons*p,
            'probability_at_least_one_event_per_attempt':-math.expm1(-incident_protons*tau),
            'status':'CONDITIONAL_FIXED_ENERGY_SCENARIO_NOT_CALIBRATED_STARS_PREDICTION',
            'assumptions':['stationary target and constant projectile energy along specified column','independent protons; one reaction removes each proton','no competing channels, target changes, scattering or collective amplification','areal inventory and proton number are supplied scenario inputs','no acoustic effect assigned','birth alpha count is not an escaping/detected product count'],
            'net_energy':'NOT_CALCULATED_NO_COMPLETE_TRANSPORT_OR_WALL_LEDGER'}
