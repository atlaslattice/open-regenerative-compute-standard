"""One offline verification workflow; not an implemented p–B event/burn solver."""
import hashlib
import importlib.metadata
import json
import math
import platform
from pathlib import Path
import numpy as np
from .vendor.transport import RangeTable, Layer, transmit_proton, escape_alpha
from .vendor.detector import Response
from .vendor import observables, identifiability, reporting, screen, costs


def encoded(x):
    return json.dumps(x, indent=2, allow_nan=False, sort_keys=True)+'\n'


def read_json(path):
    def unique(pairs):
        d={}
        for k,v in pairs:
            if k in d:raise ValueError('duplicate JSON key: '+k)
            d[k]=v
        return d
    def invalid(x):raise ValueError('nonfinite JSON constant: '+x)
    return json.loads(Path(path).read_text(),object_pairs_hook=unique,parse_constant=invalid)


def hash_bytes(b):return hashlib.sha256(b).hexdigest()


def run(config_path, out):
    config_path=Path(config_path).resolve(); c=read_json(config_path)
    out=Path(out)
    # Reserve first, then preserve errors. An existing run is never replaced.
    out.mkdir(parents=True,exist_ok=False)
    try:
        return execute(c,config_path,out)
    except Exception as exc:
        (out/'FAILURE.json').write_text(encoded({'status':'FAILED','error_type':type(exc).__name__,'reason':str(exc),'config_sha256':hash_bytes(config_path.read_bytes())}))
        raise


def execute(c, config_path, out):
    expected={'schema_version','experiment_id','run_class','scientific_outcome','economic_as_of','layers','ranges','protons','alpha_fixture','detector','source_audit','operating_track','energy_scenario','components','products','costs_USD'}
    if set(c)!=expected or c['schema_version']!='0.1':raise ValueError('unsupported configuration schema/fields')
    if c['run_class']!='VERIFICATION_DEMO':
        raise ValueError('Only VERIFICATION_DEMO implemented; exploratory/calibrated modes blocked')
    if c['scientific_outcome']!='NOT_TESTED':raise ValueError('fixture cannot assign a physical hypothesis verdict')
    root=Path(__file__).parent
    lock=read_json(root/'VENDOR_LOCK.json')
    for entry in lock:
        if hash_bytes((root/'vendor'/entry['module']).read_bytes())!=entry['sha256']:
            raise ValueError('vendored module hash mismatch: '+entry['module'])
    tables={}; sources=[]
    for r in c['ranges']:
        key=(r['material_id'],r['species'])
        if key in tables:raise ValueError('duplicate range identity')
        if not r['material_id'].startswith('SYNTHETIC_'):raise ValueError('fixture materials must be explicitly synthetic')
        h=hash_bytes(encoded(r).encode())
        tables[key]=RangeTable('fixture:'+':'.join(key),*key,h,'SYNTHETIC',tuple(r['energy_MeV']),tuple(r['csda_range_g_cm2']))
        sources.append({'id':':'.join(key),'sha256':h,'evidence':'SYNTHETIC'})
    layers=[Layer(**x) for x in c['layers']]
    transmission=[transmit_proton(x['energy_MeV'],x['mu'],layers,tables) for x in c['protons']]
    d=dict(c['detector']);background=d.pop('background_counts');response=Response(**d)
    if response.evidence_state!='SYNTHETIC':raise ValueError('fixture response must be synthetic')
    response.arrays();counts=np.zeros(len(response.true_edges_mev)-1);alphas=[];ids=set();stopped=0.
    for x in c['alpha_fixture']:
        if x['fixture_id'] in ids:raise ValueError('duplicate alpha fixture identity')
        ids.add(x['fixture_id']);w=float(x['weight'])
        if not math.isfinite(w) or w<0:raise ValueError('invalid alpha fixture weight')
        a=escape_alpha(x['energy_MeV'],x['mu'],x['birth_layer_index'],x['birth_depth_fraction'],layers,tables)
        a.update(fixture_id=x['fixture_id'],weight=w);alphas.append(a)
        e=a['output_energy_MeV']
        if e==0:stopped+=w;continue
        if not response.true_edges_mev[0]<=e<=response.true_edges_mev[-1]:raise ValueError('escaping alpha outside detector true-bin coverage')
        k=min(int(np.searchsorted(response.true_edges_mev,e,side='right')-1),len(counts)-1)
        counts[k]+=w
    detector=response.fold('alpha',counts,background)
    audit=c['source_audit'];audit_result={'status':'NOT_RUN_NO_SOURCE_FILE','event_normalization':'BLOCKED'}
    if audit['raw_csv_path'] is not None:
        p=(config_path.parent/audit['raw_csv_path']).resolve();raw=p.read_bytes()
        source=observables.Source('C2973002','EXFOR:C2973002',audit['sha256'],p.as_uri(),'11B(p,a)8Be',observables.Quantity.REPORTED_ALPHA_CROSS_SECTION,observables.Frame.LAB,'source-defined alpha window','reported alpha observable; not event cross section','upstream reuse terms require qualification')
        obs=observables.import_csv(raw,source,'C2973:target');cov=observables.covariance(obs)
        (out/'SOURCE_OBSERVATIONS.json').write_text(observables.strict_json(obs))
        (out/'SOURCE_COVARIANCE.json').write_text(encoded(cov.tolist()))
        audit_result={'status':'IMPORTED_REPORTED_ALPHA_OBSERVABLE','rows':len(obs),'sha256':hash_bytes(raw),'event_normalization':'BLOCKED_NO_QUALIFIED_TRANSFORMATION'}
        sources.append({'id':'EXFOR:C2973002','sha256':hash_bytes(raw),'evidence':'SOURCE_TRACED_NUMERIC_IMPORT_ONLY'})
    # Explicit standalone synthetic design, not a fit to the transported spectra.
    J=[[1,1,0,0,0],[1,0,1,0,0],[1,0,0,1,1]]
    base=identifiability.diagnose(J,np.diag(np.array([.03,.05,.08])**2),[1]*5)
    calibrated=identifiability.diagnose(J+[[1,0,0,0,0],[0,0,0,0,1]],np.diag(np.array([.03,.05,.08,.02,.04])**2),[1]*5)
    track=c['operating_track']
    mapping={'SINGLE_PASS_DRIVEN':'SINGLE_PASS_DRIVEN','EXTERNALLY_DRIVEN':'CONTINUOUSLY_DRIVEN','STARTUP_THEN_BURN_HYPOTHESIS':'STARTUP_THEN_BURN_HYPOTHESIS','GRID_ASSISTED_BURN_HYPOTHESIS':'CONTINUOUSLY_DRIVEN'}
    if track not in mapping:raise ValueError('unknown operating track')
    energy=screen.screen(mapping[track],**c['energy_scenario']);energy['requested_track']=track
    energy['connection_to_transport']='NONE: separate assumed energy scenario, NOT derived from alpha fixture'
    economic=reporting.report(c['experiment_id'],c['scientific_outcome'],c['economic_as_of'],c['products'],c['costs_USD'])
    capital=costs.installed_capex(c['components'])
    outcomes=[observables.measured_outcome('measured',0),observables.measured_outcome('missing',reason='synthetic missing-outcome illustration')]
    result={'status':'VERIFICATION_DEMO_COMPLETED','physical_prediction':'BLOCKED_UNQUALIFIED_NUCLEAR_SOURCE_STOPPING_BEAM_AND_RESPONSE',
            'scientific_outcome':'NOT_TESTED','transmission':transmission,'transported_alpha_fixtures':alphas,
            'alpha_fixture_scope':'externally supplied independent weighted rays; NOT correlated reaction events',
            'stopped_alpha_fixture_weight':stopped,'detector':detector,'source_audit':audit_result,
            'synthetic_identifiability':{'joint_rank':base,'with_calibration_rank':calibrated,'scope':'independent scalar log-linear toy, not spectral calibration'},
            'energy_scenario':energy,'economic_scenario':economic,'capital':capital,
            'missing_vs_zero_fixture':outcomes,'zero_ratio_fixture':observables.ratio(0,0),
            'unimplemented':['physical mass-correct correlated event generation','connected nuclear event rates','scattering/straggling','dynamic burn and ignition','all-shot causal inference','grouped experimental validation','full-cycle storage ledger','complete reaction/decay/recovery network','qualified market prices and full CAPEX']}
    (out/'CONFIG.json').write_text(encoded(c))
    (out/'RESULTS.json').write_text(observables.strict_json(result))
    text=make_report(c,result)
    (out/'REPORT.md').write_text(text)
    (out/'transmission.svg').write_text(plot(transmission))
    manifest={'package_version':'1.0.0','python':platform.python_version(),'numpy':np.__version__,
              'input_config_sha256':hash_bytes(config_path.read_bytes()),'sources':sources,'randomness':'none',
              'code_sha256':{str(p.relative_to(root)):hash_bytes(p.read_bytes()) for p in sorted(root.rglob('*')) if p.is_file() and '__pycache__' not in str(p)},
              'output_sha256':{p.name:hash_bytes(p.read_bytes()) for p in sorted(out.iterdir()) if p.is_file()}}
    (out/'MANIFEST.json').write_text(encoded(manifest));return result


def make_report(c,r):
    lines=['# Stellar Forge Reference v.1 — verification demo','',f"Experiment: {c['experiment_id']}",'',
           '**SYNTHETIC FIXTURES. No calibrated p–B prediction, ignition or net-power result.**','',
           'Transported alpha fixture spectra are connected to the detector response. Nuclear births are externally supplied rays. The energy scenario and identifiability toy are separate calculations, not predictions from that transport.','',
           '| Proton fixture | Input MeV | Transmitted MeV | Primary loss MeV |','|---|---:|---:|---:|']
    for i,x in enumerate(r['transmission']):lines.append(f"| {i+1} | {x['input_energy_MeV']:.6g} | {x['output_energy_MeV']:.6g} | {x['primary_energy_loss_MeV']:.6g} |")
    lines+=['','![Synthetic transmission](transmission.svg)','',
            f"Detector expected counts: {r['detector']['total_expected_counts']}; undetected weight: {r['detector']['undetected_expected_counts']}. No random shot counts generated.",'',
            f"Standalone assumed energy scenario: {r['energy_scenario']['net_electric_J']} J net; ignition NOT EVALUATED.",'',
            f"Installed CAPEX: {r['capital']['total_installed_capex_USD'] or 'UNRESOLVED'} USD. Source audit: {r['source_audit']['status']}.",'',
            reporting.footer(r['economic_scenario']),'','## Unimplemented physical and experimental gates','']
    lines += ['- '+x for x in r['unimplemented']]
    return '\n'.join(lines)+'\n'


def plot(rows):
    # Exact data labels; SVG is a small scientific chart, no external plotting dependency.
    bars=[]
    for i,r in enumerate(rows):
        y=45+i*50
        for offset,key,color in [(0,'input_energy_MeV','#64748b'),(15,'output_energy_MeV','#2563eb')]:
            bars.append(f'<rect x="150" y="{y+offset}" width="{80*r[key]}" height="12" fill="{color}"/><text x="{155+80*r[key]}" y="{y+offset+11}" font-size="12">{r[key]:.6g} MeV</text>')
        bars.append(f'<text x="10" y="{y+15}">Fixture {i+1}</text>')
    return '<svg xmlns="http://www.w3.org/2000/svg" width="650" height="'+str(90+50*len(rows))+'"><rect width="100%" height="100%" fill="white"/><text x="10" y="22">Synthetic proton transmission: gray input, blue output</text>'+''.join(bars)+'</svg>\n'
