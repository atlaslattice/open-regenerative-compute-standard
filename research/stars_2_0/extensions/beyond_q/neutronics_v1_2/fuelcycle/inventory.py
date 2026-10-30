"""Positivity-preserving first-order compartment operator, mass in kg-T.

For constant hazards r_j [1/day] and source s [kg/day]:
dx/dt=s-Kx, K=sum(r_j); exact integrated exit_j=r_j*integral(x dt).
Source and each exit explicitly counted. Other compartments are advanced by
operator splitting; their coupling has timestep error, tested by refinement.
"""
import math
from .physics import nonnegative

def advance(x, source, hazards, days):
    nonnegative(x=x, source=source, days=days, **hazards)
    k = sum(hazards.values())
    if not k:
        return x+source*days, {name: 0. for name in hazards}
    z = k*days
    phi = -math.expm1(-z)/k
    # Stable source integral as z -> 0.
    psi = days*days*(.5-z/6+z*z/24-z*z*z/120) if z < 1e-4 else (days-phi)/k
    integral = x*phi + source*psi
    remaining = x*math.exp(-z)+source*phi
    exits = {name: rate*integral for name, rate in hazards.items()}
    if abs(x+source*days-remaining-sum(exits.values())) > 1e-10*max(1., x+source*days):
        raise ArithmeticError('compartment conservation failure')
    return remaining, exits
