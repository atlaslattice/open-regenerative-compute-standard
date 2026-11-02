"""He3 sequential compartment accounting in mol and days; not plasma physics.

Each scalar compartment is integrated exactly for constant source/hazards.
Sequential coupling averages upstream flow over the step: positive, conservative,
but only timestep-refined, not an exact coupled-system solution. No T/DT or
energy result is inferred from this He3 interface calculation.
"""
import math

MOLAR_STP_L = 22.414


def valid_fraction(value):
    if not math.isfinite(value) or not 0 <= value <= 1:
        raise ValueError('fraction outside [0,1]')
    return value


def advance(inventory, source_per_day, hazards_per_day, dt):
    values = [inventory, source_per_day, *hazards_per_day.values()]
    if any(not math.isfinite(v) or v < 0 for v in values) or not math.isfinite(dt) or dt <= 0:
        raise ValueError('nonnegative finite state/source/rates and positive finite step required')
    k = sum(hazards_per_day.values())
    if k == 0:
        return inventory + source_per_day * dt, {name: 0.0 for name in hazards_per_day}
    z = k * dt
    phi = -math.expm1(-z) / k
    # Integrated inventory; series avoids cancellation at tiny hazards.
    psi = dt * dt * (.5-z/6+z*z/24-z*z*z/120) if z < 1e-4 else (dt-phi)/k
    integral = inventory * phi + source_per_day * psi
    return inventory * math.exp(-z) + source_per_day * phi, {name: rate * integral for name, rate in hazards_per_day.items()}


def required_downstream(overall_target, plasma_survival):
    valid_fraction(overall_target); valid_fraction(plasma_survival)
    if plasma_survival == 0:
        return {'required_fraction': None, 'feasible': overall_target == 0}
    required = overall_target / plasma_survival
    return {'required_fraction': required, 'feasible': required <= 1.0}


def simulate(p, *, dt=.25, days=365.25):
    """Externally supplied source and assumed rate interface.

    Source is mol He3/day, not DD reactor power. Plasma burn destroys He3 and
    records one D-He3 reaction and one He4 birth per He3 atom consumed. Those
    counts require one D atom each; no wall-plug or heating calculation is made.
    Stage losses are assumed permanent; delayed but retained atoms remain stock.
    Qualified output is always unknown absent an external assay specification.
    """
    count = round(days/dt)
    if not math.isfinite(days) or days <= 0 or dt <= 0 or abs(count*dt-days)>1e-8:
        raise ValueError('step must divide positive horizon')
    for key in ['birth_mol_day', 'plasma_burn_day', 'plasma_exhaust_day',
                'pump_release_day', 'purifier_release_day']:
        if not math.isfinite(p[key]) or p[key]<0:
            raise ValueError(key)
    for key in ['exhaust_delivery_fraction','pump_capture_regeneration_fraction','purifier_yield']:
        valid_fraction(p[key])
    for key in ['source_off', 'pump_off', 'purifier_off']:
        for begin,end in p.get(key,[]):
            if not 0<=begin<end<=days:
                raise ValueError('invalid outage interval')
    stock = dict(plasma=0.0, pump=0.0, purifier=0.0, candidate_storage=0.0)
    cumulative = dict(born=0.0, secondary_burn=0.0, exhaust_loss=0.0, pump_loss=0.0,
                      purification_loss=0.0, exhausted=0.0, pump_released=0.0, purified=0.0)
    rows=[]
    def on(key,t):
        return not any(begin<=t<end for begin,end in p.get(key,[]))
    max_residual=0.0
    for i in range(count):
        t=i*dt
        active=on('source_off',t)
        source=p['birth_mol_day'] if active else 0.0
        cumulative['born']+=source*dt
        stock['plasma'],flow=advance(stock['plasma'],source,
            {'burn':p['plasma_burn_day'] if active else 0.0,'exhaust':p['plasma_exhaust_day']},dt)
        cumulative['secondary_burn']+=flow['burn']
        cumulative['exhausted']+=flow['exhaust']
        delivered=flow['exhaust']*p['exhaust_delivery_fraction']
        cumulative['exhaust_loss']+=flow['exhaust']-delivered
        stock['pump'],flow=advance(stock['pump'],delivered/dt,
            {'release':p['pump_release_day'] if on('pump_off',t) else 0.0},dt)
        cumulative['pump_released']+=flow['release']
        captured=flow['release']*p['pump_capture_regeneration_fraction']
        cumulative['pump_loss']+=flow['release']-captured
        stock['purifier'],flow=advance(stock['purifier'],captured/dt,
            {'release':p['purifier_release_day'] if on('purifier_off',t) else 0.0},dt)
        candidate=flow['release']*p['purifier_yield']
        cumulative['purification_loss']+=flow['release']-candidate
        cumulative['purified']+=candidate
        stock['candidate_storage']+=candidate
        removed=sum(cumulative[k] for k in ['secondary_burn','exhaust_loss','pump_loss','purification_loss'])
        residual=cumulative['born']-sum(stock.values())-removed
        max_residual=max(max_residual,abs(residual))
        if i%max(1,round(1/dt))==0 or i==count-1:
            rows.append(dict(day=t+dt,**{k+'_mol':v for k,v in stock.items()},
                             **{k+'_mol':v for k,v in cumulative.items()},residual_mol=residual))
    burn=cumulative['secondary_burn']
    return {'stocks_mol':stock,'cumulative_mol':cumulative,'max_abs_residual_mol':max_residual,
            'candidate_product_STP_L':stock['candidate_storage']*MOLAR_STP_L,
            'qualified_product_STP_L':None,'additional_He4_born_mol':burn,
            'additional_deuterium_consumed_mol':burn,'DHe3_reactions_mol':burn,
            'energy_J':None,'evidence':'POTENTIAL-DERIVED assumed compartment response; NOT PLASMA CALIBRATION',
            'rows':rows}
