"""Stoichiometric source bookkeeping, SI units; rounded v1 nuclear energies.

Sources: inherited v1 §3/6; exact J/eV and Avogadro constant (SI).
No reactivity, confinement or transport solver is present.
"""
from math import expm1, isfinite, isinf

MEV_J = 1.602176634e-13
AVOGADRO = 6.02214076e23
T_KG_PER_ATOM = .00301604928 / AVOGADRO
FPY_S = 365.25 * 86400
DT_MEV = 17.6

def nonnegative(**values):
    for name, value in values.items():
        if not isfinite(value) or value < 0:
            raise ValueError(f'{name} must be finite and nonnegative')

def probability(name, value):
    nonnegative(**{name: value})
    if value > 1:
        raise ValueError(f'{name} must be <= 1')

def dd_source(power_mw=20., t_branch=.5):
    """Total reactions/s; T and neutron branches are exclusive outcomes."""
    nonnegative(power_mw=power_mw)
    probability('t_branch', t_branch)
    mean_q = t_branch * 4.03 + (1-t_branch)*3.27
    events = power_mw * 1e6 / (mean_q * MEV_J)
    return dict(events_s=events, t_atoms_s=events*t_branch,
                n_atoms_s=events*(1-t_branch), mean_q_mev=mean_q)

def dt_events(power_mw):
    nonnegative(power_mw=power_mw)
    return power_mw * 1e6 / (DT_MEV * MEV_J)

def fixed_exposure_burn_fraction(n_d_m3, reactivity_m3_s, residence_s):
    """GENERIC candidate only, not attributed to Argon: 1-exp(-n<σv>τ).

    Homogeneous stationary density, fixed exposure; no slowing down, spatial
    escape distribution, depletion or coupled power balance. Dimensionless
    n[m^-3]*<σv>[m^3/s]*τ[s]. Do not use a Maxwellian rate for a fast T population
    without justification. Exact Argon proposal is pending receipt.
    """
    nonnegative(n_d_m3=n_d_m3, reactivity_m3_s=reactivity_m3_s,
                residence_s=residence_s)
    return -expm1(-n_d_m3*reactivity_m3_s*residence_s)

def competing_escape_burn_fraction(reaction_s, escape_s):
    """Steady competing exponential hazards; differs from fixed exposure."""
    nonnegative(reaction_s=reaction_s, escape_s=escape_s)
    return reaction_s/(reaction_s+escape_s) if reaction_s+escape_s else 0.

def argon_burn_fraction(f_fast, n_d_m3, reactivity_m3_s, residence_s):
    """Argon proposal received 2026-10-29; conditional two-stage model.

    f_fast+(1-f_fast)*x/(1+x), x=n_D*<sigma v>*tau_p.
    Thermal residence is exponentially distributed; no extra D-D symmetry
    factor for unlike D/T ions. f_fast must be the fraction of newborn tritons
    burned BEFORE thermalization, not an overlapping total burn estimate.
    This is not a slowing-down/plasma solution; f_fast is still an input.
    """
    probability('f_fast',f_fast)
    nonnegative(n_d_m3=n_d_m3,reactivity_m3_s=reactivity_m3_s,residence_s=residence_s)
    x=n_d_m3*reactivity_m3_s*residence_s
    thermal=1. if isinf(x) else x/(1+x)
    return f_fast+(1-f_fast)*thermal

def argon_extraction(epsilon, loop_minutes, permeation_day, half_life_years,
                     iss_loss, birth_kg_day):
    """Well-mixed continuous removal candidate k_ext=epsilon/tau_loop.

    Returns steady salt stock and eventual once-through ISS recovery.
    Does NOT include later storage/processing decay or repeated B fuel cycles.
    Deterministic discrete-pass extraction instead has k=-ln(1-eps)/tau
    for matching survival per pass (infinite at eps=1). These are distinct
    residence-time assumptions, especially at high epsilon.
    """
    import math
    probability('epsilon',epsilon);probability('iss_loss',iss_loss)
    nonnegative(loop_minutes=loop_minutes,permeation_day=permeation_day,
                half_life_years=half_life_years,birth_kg_day=birth_kg_day)
    if loop_minutes==0 or half_life_years==0:raise ValueError('positive times required')
    k=epsilon/(loop_minutes/1440.)
    decay=math.log(2)/(half_life_years*365.25)
    total=k+decay+permeation_day
    return dict(k_extract_day=k,inventory_ss_kg=birth_kg_day/total,
                eta_salt_and_one_iss=k/total*(1-iss_loss))

def reaction_ledger(dd_events, dd_t_atoms, a_dt_atoms, b_dt_atoms,
                    blanket_a_t_atoms=0., blanket_b_t_atoms=0.,
                    li6_fraction=1.):
    """Source-neutron and nuclear-energy ledger; not a transport tally.

    Fusion charged+neutron energies partition fusion Q, never added to it.
    Li-6 Q=4.78 MeV; Li-7 Q=-2.47 MeV. Fractions ASSUMED unless tallied.
    Neutron multiplication/leakage/capture/heat deposition remain unresolved.
    All output energies J. Other capture Q and decay heat unmodeled.
    """
    nonnegative(dd_events=dd_events, dd_t_atoms=dd_t_atoms,
                a_dt_atoms=a_dt_atoms, b_dt_atoms=b_dt_atoms,
                blanket_a_t_atoms=blanket_a_t_atoms,
                blanket_b_t_atoms=blanket_b_t_atoms)
    probability('li6_fraction', li6_fraction)
    if dd_t_atoms > dd_events*(1+1e-12):
        raise ValueError('DD T branch exceeds total events')
    dd_n = max(0., dd_events-dd_t_atoms)
    dt = a_dt_atoms+b_dt_atoms
    fusion = (dd_t_atoms*4.03+dd_n*3.27+dt*17.6)*MEV_J
    neutron = (dd_n*2.45+dt*14.1)*MEV_J
    charged = fusion-neutron
    q = (blanket_a_t_atoms+blanket_b_t_atoms)*(
         li6_fraction*4.78+(1-li6_fraction)*(-2.47))*MEV_J
    return dict(dd_neutrons=dd_n, a_dt_neutrons=a_dt_atoms,
                b_dt_neutrons=b_dt_atoms, total_source_neutrons=dd_n+dt,
                neutron_fate_status='UNRESOLVED: no transport',
                fusion_j=fusion, fusion_neutron_j=neutron,
                fusion_charged_j=charged, assumed_blanket_reaction_q_j=q,
                nuclear_release_j=fusion+q,
                deposited_heat_status='UNRESOLVED', net_electric_status='UNRESOLVED')
