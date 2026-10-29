from pathlib import Path
import hashlib,json
from . import acoustics, evidence
from .vendor import measurement_design, stopping_source_check


def additions(c,config_path):
    acoustic=acoustics.run(c.get('acoustic'))
    # Require intended acoustic wall cost to be explicitly included in the assumed
    # energy ledger, not silently added on top of a possibly already inclusive bill.
    if c.get('acoustic') and c['energy_scenario']['auxiliary_wall_J']<c['acoustic']['driver_wall_J']:
        raise ValueError('acoustic driver wall cost exceeds declared auxiliary total')
    references={'status':'NOT_REQUESTED'}
    audits=c.get('reference_audits',{})
    if set(audits)-{'pstar_aluminum_path','boron_quarantine_path'}:raise ValueError('unknown reference audit')
    if audits:
        references={}
        for key,path in audits.items():
            if path is None:references[key]={'status':'NOT_REQUESTED'};continue
            raw=(config_path.parent/path).resolve().read_bytes()
            if key=='pstar_aluminum_path':
                rows=stopping_source_check.parse_pstar_aluminum(raw)
                cases=[]
                from .vendor.transport import RangeTable
                t=RangeTable('candidate-mirror','Al','proton',stopping_source_check.AL_HASH,'SOURCE_TRACED',tuple(float(r[0]) for r in rows),tuple(float(r[4]) for r in rows))
                for E in [.5,.675,1,2]:
                    for mass in [.0001,.0005,.001]:
                        a=t.residual(E,mass);b=stopping_source_check.stopping_integral_residual(E,mass,rows)
                        cases.append({'incident_MeV':E,'path_g_cm2':mass,'range_method_MeV':a,'stopping_method_MeV':b,'difference_MeV':abs(a-b)})
                references[key]={'status':'CANDIDATE_MIRROR_NOT_PRIMARY_RECONCILED','rows':len(rows),'sha256':hashlib.sha256(raw).hexdigest(),'cases':cases,'physical_calibration':'NOT_VALIDATED','grid_completeness':'132 versus documented default 133 unresolved'}
            else:references[key]=stopping_source_check.quarantine_boron(raw)
    root=Path(__file__).parent
    return {'acoustic':acoustic,
            'dependency_evidence':evidence.dependencies([{'id':'acoustic_input','maturity':'NOT_ASSESSED','provenance':'SYNTHETIC_TEST','depends_on':[]},{'id':'mechanical_response','maturity':'NOT_ASSESSED','provenance':'MODEL_PREDICTION','depends_on':['acoustic_input']}],'mechanical_response'),…4569 tokens truncated…ent=JSON.stringify({status:r.status,physical_prediction:r.physical_prediction,scientific_outcome:r.scientific_outcome,acoustic_status:a?.status,location:a?.configuration?.location,peak_displacement_m:a?.peak_displacement_m,net_energy_scenario_J:r.energy_scenario?.net_electric_J,energy_scope:r.energy_scenario?.connection_to_transport,economic_scenario:r.economic_scenario,capital:r.capital},null,2);if(a?.trace?.length){const trace=a.trace;const xs=trace.map(x=>x[0]),ys=trace.map(x=>x[2]);if(![...xs,...ys].every(Number.isFinite))throw Error('Nonfinite trace');const lo=Math.min(...xs),hi=Math.max(...xs);const ymax=Math.max(...ys.map(Math.abs),1e-30);const pts=trace.map((x,i)=>(30+840*(x[0]-lo)/(hi-lo||1))+','+(95-65*ys[i]/ymax)).join(' ');$('plot').replaceChildren();const ns='http://www.w3.org/2000/svg';const line=document.createElementNS(ns,'polyline');line.setAttribute('points',pts);line.setAttribute('fill','none');line.setAttribute('stroke','#1b67a5');line.setAttribute('stroke-width','2');$('plot').append(line);const label=document.createElementNS(ns,'text');label.setAttribute('x','30');label.setAttribute('y','180');label.textContent='time '+lo.toPrecision(3)+' to '+hi.toPrecision(3)+' s; displacement ±'+ymax.toPrecision(3)+' m (synthetic)';$('plot').append(label);}}catch(x){error(x);}};
</script></html>'''.replace('__CONFIG__',data)
    with Path(out).open('x') as f:f.write(html)
