"""Straight-track planar CSDA reference kernel. No nuclear-rate inference.
Energy: MeV; normal areal mass: g/cm2. No scattering or straggling.
"""
from dataclasses import dataclass
from bisect import bisect_right
import hashlib
import csv
import io
import math


class DomainError(ValueError):
    pass


def finite_nonnegative(x, label):
    x = float(x)
    if not math.isfinite(x) or x < 0:
        raise ValueError(label+' must be finite and nonnegative')
    return x


def cosine(mu, positive=False):
    mu=float(mu)
    if not math.isfinite(mu) or abs(mu)>1 or mu==0 or (positive and mu<0):
        raise ValueError('Nonzero direction cosine in [-1,1] required; incoming beam must have mu>0')
    return mu


@dataclass(frozen=True)
class RangeTable:
    dataset_id: str
    material_id: str
    species: str
    source_sha256: str
    evidence_state: str
    energies_mev: tuple
    csda_ranges_g_cm2: tuple

    def __post_init__(self):
        if not self.dataset_id or not self.material_id or self.species not in {'proton','alpha'}:
            raise ValueError('Dataset, material and supported species are required')
        if len(self.source_sha256)!=64 or any(c not in '0123456789abcdef' for c in self.source_sha256):
            raise ValueError('SHA-256 required')
        if self.evidence_state not in {'SYNTHETIC','SOURCE_TRACED','CALIBRATED'}:
            raise ValueError('Explicit evidence state required')
        if len(self.energies_mev)!=len(self.csda_ranges_g_cm2) or len(self.energies_mev)<2:
            raise ValueError('Matching range columns with at least two points required')
        for label,seq in [('energy',self.energies_mev),('range',self.csda_ranges_g_cm2)]:
            vals=[finite_nonnegative(x,label) for x in seq]
            if any(b<=a for a,b in zip(vals,vals[1:])):
                raise ValueError('Range and energy must be strictly increasing')
        object.__setattr__(self, 'energies_mev', tuple(float(x) for x in self.energies_mev))
        object.__setattr__(self, 'csda_ranges_g_cm2', tuple(float(x) for x in self.csda_ranges_g_cm2))
        if (self.energies_mev[0]==0)!=(self.csda_ranges_g_cm2[0]==0):
            raise ValueError('A zero-energy anchor requires exactly zero range and vice versa')

    @classmethod
    def from_csv(cls, raw, *, dataset_id, material_id, species, sha256, evidence_state):
        if hashlib.sha256(raw).hexdigest()!=sha256:
            raise ValueError('Range source hash mismatch')
        reader=csv.DictReader(io.StringIO(raw.decode('utf-8-sig')))
        if reader.fieldnames!=['energy_MeV','csda_range_g_cm2']:
            raise ValueError('Only explicit energy_MeV and csda_range_g_cm2 supported; no projected range')
        rows=list(reader)
        if any(None in r or any(v is None for v in r.values()) for r in rows):
            raise ValueError('Malformed range CSV')
        return cls(dataset_id,material_id,species,sha256,evidence_state,
                   tuple(float(r['energy_MeV']) for r in rows),
                   tuple(float(r['csda_range_g_cm2']) for r in rows))

    @staticmethod
    def interpolate(x,xs,ys):
        if x<xs[0] or x>xs[-1]:
            raise DomainError('Outside qualified table domain; extrapolation prohibited')
        j=min(max(bisect_right(xs,x)-1,0),len(xs)-2)
        return ys[j]+(x-xs[j])*(ys[j+1]-ys[j])/(xs[j+1]-xs[j])

    def residual(self, energy_mev, path_g_cm2):
        E=finite_nonnegative(energy_mev,'energy')
        path=finite_nonnegative(path_g_cm2,'path areal mass')
        if E==0: return 0.
        R=self.interpolate(E,self.energies_mev,self.csda_ranges_g_cm2)
        if path==0: return E
        if path>=R: return 0.
        # If residual range falls below the first reported knot, it is unresolved,
        # not permission to invent a low-energy extrapolation to zero.
        return self.interpolate(R-path,self.csda_ranges_g_cm2,self.energies_mev)


@dataclass(frozen=True)
class Layer:
    layer_id: str
    material_id: str
    areal_mass_g_cm2: float

    def __post_init__(self):
        if not self.layer_id or not self.material_id:
            raise ValueError('Named layer and material required')
        finite_nonnegative(self.areal_mass_g_cm2,'layer areal mass')


def normal_areal_mass(thickness_um,density_g_cm3):
    """Explicit conversion; density is a supplied specimen input, not a default."""
    return finite_nonnegative(thickness_um,'thickness')*1e-4*finite_nonnegative(density_g_cm3,'density')


def through_path(energy_mev, species, mu_abs, layers, tables, *, calibrated=False):
    E=finite_nonnegative(energy_mev,'energy'); mu=cosine(mu_abs,positive=True)
    if species not in {'proton','alpha'}: raise ValueError('Unsupported species')
    layers=tuple(layers)
    if len({x.layer_id for x in layers})!=len(layers):
        raise ValueError('Layer IDs must be unique')
    # Validate all nonempty layer inputs even if a particle will stop earlier.
    for layer in layers:
        if layer.areal_mass_g_cm2==0: continue
        key=(layer.material_id,species)
        if key not in tables: raise ValueError('Missing material/species range table: '+str(key))
        tab=tables[key]
        if (tab.material_id,tab.species)!=key:
            raise ValueError('Table identity does not match layer/species')
        if calibrated and tab.evidence_state!='CALIBRATED':
            raise ValueError('Uncalibrated stopping input; calibrated transport prohibited')
    ledger=[]
    for layer in layers:
        incoming=E
        path=finite_nonnegative(layer.areal_mass_g_cm2/mu,'path areal mass')
        if path>0 and E>0:
            E=tables[(layer.material_id,species)].residual(E,path)
        ledger.append({'layer_id':layer.layer_id,'material_id':layer.material_id,
            'normal_areal_mass_g_cm2':layer.areal_mass_g_cm2,'path_areal_mass_g_cm2':path,
            'input_energy_MeV':incoming,'output_energy_MeV':E,'primary_energy_loss_MeV':incoming-E,
            'range_dataset_id':tables[(layer.material_id,species)].dataset_id if path>0 else None})
    deposited=math.fsum(x['primary_energy_loss_MeV'] for x in ledger)
    return {'species':species,'input_energy_MeV':float(energy_mev),'output_energy_MeV':E,
        'primary_energy_loss_MeV':deposited,'closure_residual_MeV':float(energy_mev)-E-deposited,
        'layer_ledger':ledger,'model':'planar straight-track CSDA, linear range interpolation',
        'scope':'conditional primary transport only; primary energy loss is not measured heat; secondary escape/storage unresolved; no nuclear reactions, scattering or straggling'}


def transmit_proton(energy_mev,mu,layers,tables,*,calibrated=False):
    return through_path(energy_mev,'proton',cosine(mu,positive=True),layers,tables,calibrated=calibrated)


def escape_alpha(energy_mev,mu,birth_layer_index,birth_depth_fraction,layers,tables,*,calibrated=False):
    """Depth is measured from upstream surface of birth layer; signed mu relative
    to incident beam. Infinite lateral extent means no side face is modeled.
    Alpha birth is an external supplied input, not generated from a cross section.
    """
    mu=cosine(mu); layers=tuple(layers)
    if isinstance(birth_layer_index,bool) or not isinstance(birth_layer_index,int) or not 0<=birth_layer_index<len(layers):
        raise ValueError('Invalid birth layer')
    d=float(birth_depth_fraction)
    if not math.isfinite(d) or not 0<=d<=1: raise ValueError('Birth depth must be in [0,1]')
    birth=layers[birth_layer_index]
    if mu>0:
        path=(Layer(birth.layer_id,birth.material_id,(1-d)*birth.areal_mass_g_cm2),)+layers[birth_layer_index+1:]
        face='beam_downstream'
    else:
        path=(Layer(birth.layer_id,birth.material_id,d*birth.areal_mass_g_cm2),)+tuple(reversed(layers[:birth_layer_index]))
        face='beam_upstream'
    result=through_path(energy_mev,'alpha',abs(mu),path,tables,calibrated=calibrated)
    result.update({'exit_face':face if result['output_energy_MeV']>0 else None,
        'geometric_direction_face':face,'birth_layer_id':birth.layer_id,'birth_depth_fraction':d})
    return result
