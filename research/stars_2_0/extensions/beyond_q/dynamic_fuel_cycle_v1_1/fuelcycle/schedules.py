"""Exogenous reproducible daily schedules, no claim of plant reliability.

Common outage plus independent reactor outages, all Bernoulli per day.
Shared shock induces correlation; planned windows and arbitrary schedules
are supported. Coarse daily hazards do not model outage duration distributions.
"""
import random
from .physics import probability

def generate(days, seed, availability_a, availability_b, common_outage,
             planned_a=(), planned_b=()):
    for name, v in [('availability_a',availability_a),('availability_b',availability_b),
                    ('common_outage',common_outage)]:
        probability(name,v)
    rng = random.Random(seed)
    result = []
    for day in range(days):
        common = rng.random() < common_outage
        a = rng.random() < availability_a
        b = rng.random() < availability_b
        result.append((int(a and not common and day not in planned_a),
                       int(b and not common and day not in planned_b)))
    return result
