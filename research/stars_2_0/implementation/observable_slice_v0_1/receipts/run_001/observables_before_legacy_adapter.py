"""Append-only A1/A2 research prototype. No event-cross-section inference."""
from dataclasses import dataclass, asdict
from decimal import Decimal, InvalidOperation
from enum import Enum
import csv
import hashlib
import io
import json
import re
import numpy as np


class Quantity(str, Enum):
    REPORTED_ALPHA_CROSS_SECTION = 'reported_alpha_cross_section'
    FUSION_EVENT_CROSS_SECTION = 'fusion_event_cross_section'


class Frame(str, Enum):
    LAB = 'LAB'
    CM = 'CM'


def decimal(value):
    try:
        x = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError('Invalid decimal') from exc
    if not x.is_finite() or x < 0:
        raise ValueError('Expected finite nonnegative quantity')
    return x


@dataclass(frozen=True)
class Source:
    source_id: str
    evidence_id: str
    sha256: str
    uri: str
    reaction: str
    quantity: Quantity
    frame: Frame
    acceptance: str
    interpretation: str
    license_status: str

    def __post_init__(self):
        if not re.fullmatch(r'[0-9a-f]{64}', self.sha256):
            raise ValueError('Expected SHA-256')
        if not isinstance(self.quantity, Quantity) or not isinstance(self.frame, Frame):
            raise ValueError('Use explicit quantity and frame enums')
        if any(not getattr(self, f) for f in ('source_id', 'evidence_id', 'uri', 'reaction', 'acceptance', 'interpretation', 'license_status')):
            raise ValueError('Source semantics must be explicit')


@dataclass(frozen=True)
class Observation:
    observation_id: str
    source: Source
    energy_mev: Decimal
    energy_unc_mev: Decimal | None
    energy_unc_status: str
    value_b: Decimal
    stat_unc_b: Decimal
    common_loadings_b: tuple[tuple[str, Decimal], ...]
    transformations: tuple[str, ...]

    def __post_init__(self):
        if not self.observation_id or not self.transformations:
            raise ValueError('Row identity and transformation record required')
        for x in (self.energy_mev, self.value_b, self.stat_unc_b):
            if not isinstance(x, Decimal):
                raise ValueError('Exact decimal inputs required')
            decimal(x)
        if self.energy_unc_mev is None:
            if self.energy_unc_status != 'not_reported':
                raise ValueError('Missing uncertainty must be marked not_reported')
        elif self.energy_unc_status != 'reported' or not isinstance(self.energy_unc_mev, Decimal):
            raise ValueError('Reported uncertainty needs an exact decimal')
        else:
            decimal(self.energy_unc_mev)
        for _, loading in self.common_loadings_b:
            if not isinstance(loading, Decimal) or not loading.is_finite():
                raise ValueError('Finite decimal nuisance loading required')

    def require_quantity(self, requested):
        if requested != self.source.quantity:
            raise ValueError('Observable conversion requires an independently qualified model; no implicit /3')
        return self.value_b


@dataclass
class SourceRegistry:
    """Aliases may be registered, but a table cannot be counted twice as evidence."""
    sources: dict

    def register(self, source):
        previous = self.sources.get(source.source_id)
        if previous is not None and previous != source:
            raise ValueError('Source identifier reused with different bytes or semantics')
        aliases = [s.source_id for s in self.sources.values() if s.sha256 == source.sha256 and s.source_id != source.source_id]
        self.sources[source.source_id] = source
        return aliases


def import_csv(raw: bytes, source: Source, common_group: str):
    """Strict adapter for the archived 41-point CSV plus optional dE_lab_MeV.

    Frame and observable interpretation are supplied explicitly by a reviewed Source.
    No frame conversion or interpolation occurs. Missing dE stays unknown.
    """
    if hashlib.sha256(raw).hexdigest() != source.sha256:
        raise ValueError('Source byte hash mismatch')
    if source.frame != Frame.LAB or not common_group:
        raise ValueError('This adapter supports LAB only and requires a common group')
    if source.quantity != Quantity.REPORTED_ALPHA_CROSS_SECTION:
        raise ValueError('This adapter cannot label the archived alpha observable as events')
    reader = csv.DictReader(io.StringIO(raw.decode('utf-8-sig')))
    required = {'E_lab_MeV','sigma_b','stat_err_b','sys_target_thickness_fraction','exfor_subentry','reaction','source_DOI'}
    fields = reader.fieldnames or []
    if len(fields) != len(set(fields)) or not required <= set(fields) or set(fields)-required-{'dE_lab_MeV'}:
        raise ValueError('Unsupported or duplicate CSV columns; do not silently discard uncertainty')
    out = []
    for i, r in enumerate(reader, 1):
        if None in r or any(v is None for v in r.values()):
            raise ValueError('Malformed CSV row')
        if r['exfor_subentry'] != source.source_id or r['reaction'] != source.reaction or not r['source_DOI']:
            raise ValueError('Row/source identity mismatch')
        e, y, stat, f = [decimal(r[k]) for k in ('E_lab_MeV','sigma_b','stat_err_b','sys_target_thickness_fraction')]
        de = None if not r.get('dE_lab_MeV', '').strip() else decimal(r['dE_lab_MeV'])
        out.append(Observation(f'{source.source_id}:{i}', source, e, de,
            'not_reported' if de is None else 'reported', y, stat,
            ((common_group, f*y),),
            ('source decimal preserved; units MeV and barn unchanged',
             'target fraction represented as a linear shared nuisance loading; distribution assumption external')))
    if not out:
        raise ValueError('Empty table')
    return out


def covariance(observations):
    """Linearized observable covariance in barn^2, conditional on energy.

    Statistical errors are treated as independent standard deviations; each named
    common group is one unit-variance nuisance shared across all its rows. This is
    an explicit working covariance model, not a recovered full experimental likelihood.
    """
    obs = list(observations)
    if not obs:
        raise ValueError('No observations')
    ids = [(o.source.evidence_id, o.observation_id.split(':')[-1]) for o in obs]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate source row/alias would double-count evidence')
    if len({(o.source.quantity, o.source.frame) for o in obs}) != 1:
        raise ValueError('Mixed quantities/frames need an explicit joint model')
    groups = {}
    for i, o in enumerate(obs):
        if len({g for g, _ in o.common_loadings_b}) != len(o.common_loadings_b):
            raise ValueError('Duplicate common nuisance in one row')
        for g, loading in o.common_loadings_b:
            if not g:
                raise ValueError('Unnamed nuisance')
            groups.setdefault(g, np.zeros(len(obs)))[i] = float(loading)
    C = np.diag([float(o.stat_unc_b)**2 for o in obs])
    for loading in groups.values():
        C += np.outer(loading, loading)
    if not np.isfinite(C).all():
        raise ValueError('Covariance overflow')
    return C


def strict_json(obj):
    def encode(x):
        if isinstance(x, Decimal):
            return str(x)
        if hasattr(x, '__dataclass_fields__'):
            return asdict(x)
        raise TypeError(type(x).__name__)
    return json.dumps(obj, default=encode, allow_nan=False, indent=2) + '\n'


def measured_outcome(status, value=None, reason=None):
    if status not in {'measured','missing','censored','invalid'}:
        raise ValueError('Unknown outcome state')
    if status == 'measured':
        if value is None:
            raise ValueError('Measured value required, including a real zero')
        value = decimal(value)
    elif value is not None or not reason:
        raise ValueError('Non-measured outcome needs reason and no invented value')
    return {'status':status, 'value':value, 'reason':reason}


def ratio(numerator, denominator):
    a, b = decimal(numerator), decimal(denominator)
    return {'value': None, 'reason': 'zero_denominator'} if b == 0 else {'value':a/b, 'reason':None}
