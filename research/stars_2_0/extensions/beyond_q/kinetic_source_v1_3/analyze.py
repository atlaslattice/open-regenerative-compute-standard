"""Weighted reaction ledgers, independent rate integration and source spectra.

Bosch-Hale coefficients cited to Nucl.Fusion32(1992)611 and pinned WarpX.
Shared cross-section physics: agreement is numerical verification, not empirical validation.
"""
from pathlib import Path
import argparse,csv,json,re,hashlib,math
import numpy as np
from scipy.constants import e,c,m_u,m_e,alpha,pi
from scipy.integrate import quad
ROOT=Path(__file__).resolve().parent
M={'D':2.01410177812*m_u-m_e,'T':3.0160492779*m_u-m_e}
Q={'DDT':4.032653948e6*e,'DDN':3.26891111e6*e,'DT':17.58929696e6*e}

def cross_section(E_keV,reaction):
    E=np.asarray(E_keV,dtype=float);safe=np.maximum(E,.5)
    if reaction=='DDT':a=[5.5576e4,2.1054e2,-3.2638e-2,1.4987e-6,1.8181e-10];b=[0,0,0,0];mu=M['D']/2
    elif reaction=='DDN':a=[5.3701e4,3.3027e2,-1.2706e-1,2.9327e-5,-2.5151e-9];b=[0,0,0,0];mu=M['D']/2
    elif reaction=='DT':a=[6.927e4,7.454e8,2.050e6,5.2002e4,0];b=[6.38e1,-9.95e-1,6.981e-5,1.728e-4];mu=M['D']*M['T']/(M['D']+M['T'])
    else:raise ValueError(reaction)
    gamow=pi*alpha*np.sqrt(2*mu*c*c/(1e3*e))
    S=np.polynomial.polynomial.polyval(safe,a)/(1+safe*np.polynomial.polynomial.polyval(safe,b))
    return np.where(E>=.5,1e-31*S/safe*np.exp(-gamow/np.sqrt(safe)),0.)

def thermal_reactivity(T_keV,reaction):
    mu=M['D']/2 if reaction!='DT' else M['D']*M['T']/(M['D']+M['T'])
    integral,_=quad(lambda x:float(cross_section(x*T_keV,reaction))*x*np.exp(-x)*1e28,.5/T_keV,50,epsabs=1e-9)
    return np.sqrt(8*T_keV*1e3*e/(pi*mu))*integral*1e-28

def read_reduced(path):
    header=path.read_text().splitlines()[0]
    keys=re.findall(r'\[\d+\]([^\s]+)',header)
    data=np.atleast_2d(np.loadtxt(path))
    if data.shape[1]!=len(keys):raise ValueError('reduced diagnostic schema mismatch')
    return {key:data[:,i] for i,key in enumerate(keys)}

def write(name,rows):
    with (ROOT/'outputs'/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--cache',type=Path,required=True);a=ap.parse_args()
    import yt
    yt.set_log_level(40)
    summaries=[];spectra=[];ledgers=[];source_archive={};moments={}
    for dest in sorted((ROOT/'outputs/runs').iterdir()):
        if not dest.is_dir():continue
        name=dest.name;n=read_reduced(dest/'number.txt');en=read_reduced(dest/'energy.txt');pm=read_reduced(dest/'momentum.txt')
        w=lambda species:n[species+'_weight()']
        born=w('P');ddn=w('He3');burn=w('He4');T=w('T');D=w('D');D0=D[0]
        t_res=T+burn-born
        n_res=w('nDD')-ddn+w('nDT')-burn
        D_res=D0-D-2*(born+ddn)-burn
        charge=D+T+w('P')+2*w('He3')+2*w('He4')-D0
        baryon=2*D+3*T+w('P')+3*w('He3')+4*w('He4')+w('nDD')+w('nDT')-2*D0
        released=born*Q['DDT']+ddn*Q['DDN']+burn*Q['DT']
        eres=en['total(J)']-en['total(J)'][0]-released
        momentum=max(float(np.max(abs(pm['total_'+axis+'(kg*m/s)']-pm['total_'+axis+'(kg*m/s)'][0]))) for axis in ('x','y','z'))
        end_time=n['time(s)'][-1];dt=n['time(s)'][1]-n['time(s)'][0];steps=len(born)-1
        rateT=thermal_reactivity(20,'DDT');rateN=thermal_reactivity(20,'DDN');volume=(.002)**3;density=1e26
        expectT=.5*density*density*volume*rateT*end_time;expectN=.5*density*density*volume*rateN*end_time
        f=float(burn[-1]/born[-1]) if born[-1] else 0
        for i in range(len(born)):
            ledgers.append(dict(case=name,step=int(n['step()'][i]),time_s=n['time(s)'][i],DD_T_birth_atoms=born[i],DD_neutron_branch_atoms=ddn[i],secondary_DT_burn_atoms=burn[i],remaining_T_atoms=T[i],
                T_residual_atoms=t_res[i],D_consumption_residual_atoms=D_res[i],neutron_residual_atoms=n_res[i],charge_residual_e=charge[i],baryon_residual=baryon[i],reaction_Q_J=released[i],kinetic_energy_change_J=en['total(J)'][i]-en['total(J)'][0],energy_residual_J=eres[i]))
        # Full final plotfile reads are used only for weighted daughter diagnostics.
        final=sorted((a.cache/name/'diags').glob('diag1[0-9]*'))[-1]
        ds=yt.load(str(final));ad=ds.all_data();moment={};T_arrays=None
        Dweights=ad['D','particle_weight'].to_ndarray()
        Dfinal_fsum=math.fsum(Dweights)
        initial=sorted((a.cache/name/'diags').glob('diag1[0-9]*'))[0]
        initial_ds=yt.load(str(initial));initial_ad=initial_ds.all_data()
        Dinitial_weights=initial_ad['D','particle_weight'].to_ndarray()
        Dinitial_fsum=math.fsum(Dinitial_weights)
        compensated_D_residual=Dinitial_fsum-Dfinal_fsum-2*(born[-1]+ddn[-1])-burn[-1]
        if name=='chain_on':
            source_archive['D_initial_weights']=Dinitial_weights
            source_archive['D_final_weights']=Dweights

        for species in ('T','P','He3','nDD','nDT'):
            if (species,'particle_weight') not in ds.field_list:continue
            weights=ad[species,'particle_weight'].to_ndarray()
            if not len(weights):continue
            ps=np.vstack([ad[species,'particle_momentum_'+axis].to_ndarray() for axis in ('x','y','z')]).T
            mass=M['T'] if species=='T' else float(ad[species,'particle_mass'][0]) if (species,'particle_mass') in ds.field_list else None
            # Species mass is not always exported; standard WarpX mass conventions.
            if mass is None:
                mass={'P':1.007276466621*m_u,'He3':3.016029*m_u-2*m_e,'nDD':1.0013784193052508*1.67262192369e-27,'nDT':1.0013784193052508*1.67262192369e-27}[species]
            p2=(ps*ps).sum(axis=1);gamma=np.sqrt(1+p2/(mass*c)**2)
            energy=p2/(mass*(gamma+1))/e
            moment[species]=dict(macroparticles=len(weights),sum_weight=float(weights.sum()),sum_weight_squared=float((weights**2).sum()),weighted_mean_energy_eV=float(np.average(energy,weights=weights)))
            if name=='chain_on':
                source_archive[species+'_weight']=weights;source_archive[species+'_momentum_kg_m_s']=ps
            if species=='T':T_arrays=(weights,ps,mass)
            if species in ('nDD','nDT','T'):
                hist,edges=np.histogram(energy,bins=100,weights=weights)
                for lo,hi,value in zip(edges[:-1],edges[1:],hist):spectra.append(dict(case=name,species=species,energy_low_eV=lo,energy_high_eV=hi,physical_atoms=value))
        moments[name]=moment
        hazard=0.;f_cont=0.;f_discrete=0.
        if T_arrays:
            weights,ps,mass=T_arrays;rng=np.random.default_rng(7119)
            idx=rng.choice(len(weights),size=100000,p=weights/weights.sum())
            pT=ps[idx];vT=pT/(mass*np.sqrt(1+(pT*pT).sum(axis=1)[:,None]/(mass*c)**2))
            vD=rng.normal(0,np.sqrt(20e3*e/M['D']),size=vT.shape)
            speed=np.linalg.norm(vD-vT,axis=1);mu=M['D']*M['T']/(M['D']+M['T'])
            # Nonrelativistic comparison estimator, disclosed approximation.
            hazard=density*float(np.mean(cross_section(.5*mu*speed**2/(1e3*e),'DT')*speed))
            H=hazard*end_time
            f_cont=H/2-H*H/6+H**3/24 if H<1e-3 else 1+np.expm1(-H)/H
            f_discrete=hazard*dt*(steps+1)/2 # small-H, births-before-DT update
        sigmaT=np.sqrt(2*moment.get('P',{}).get('sum_weight_squared',0));sigmaN=np.sqrt(2*moment.get('He3',{}).get('sum_weight_squared',0))
        summary=dict(case=name,steps=steps,elapsed_s=end_time,dt_s=dt,DD_T_birth_atoms=float(born[-1]),DD_n_birth_atoms=float(ddn[-1]),DT_burn_atoms=float(burn[-1]),remaining_T_atoms=float(T[-1]),
            secondary_burn_fraction=f,T_branch_fraction=float(born[-1]/(born[-1]+ddn[-1])) if born[-1]+ddn[-1] else None,
            expected_thermal_DDT_atoms=expectT,expected_thermal_DDN_atoms=expectN,
            DDT_relative_error=float(born[-1]/expectT-1),DDN_relative_error=float(ddn[-1]/expectN-1),DDT_sampling_SE_proxy_atoms=float(sigmaT),DDN_sampling_SE_proxy_atoms=float(sigmaN),
            fast_T_DT_hazard_s=hazard,continuous_constant_birth_f=f_cont,discrete_birth_first_f=f_discrete,
            max_T_residual_atoms=float(max(abs(t_res))),max_neutron_residual_atoms=float(max(abs(n_res))),
            compensated_final_D_residual_atoms=compensated_D_residual,D_initial_fsum=Dinitial_fsum,D_final_fsum=Dfinal_fsum,
            max_D_residual_atoms=float(max(abs(D_res))),max_charge_residual_e=float(max(abs(charge))),max_baryon_residual=float(max(abs(baryon))),
            max_energy_residual_J=float(max(abs(eres))),energy_residual_fraction_released=float(max(abs(eres))/max(released[-1],1e-30)),
            max_momentum_residual_kg_m_s=momentum,qualified_surplus_kg=None,physical_validation=False)
        summaries.append(summary)
        (dest/'analysis.json').write_text(json.dumps(summary,indent=2)+'\n')
        print(name,'f=',f,'T error',summary['DDT_relative_error'],'energy err/Q',summary['energy_residual_fraction_released'],flush=True)
    write('benchmark_summary.csv',summaries);write('weighted_reaction_ledger.csv',ledgers);write('weighted_spectra.csv',spectra)
    (ROOT/'outputs/particle_moments.json').write_text(json.dumps(moments,indent=2)+'\n')
    np.savez_compressed(ROOT/'outputs/baseline_daughter_particles.npz',**source_archive)
    # Independent replay in material kg, using observed sources and sinks, no imported/duplicated T.
    kg_atom=.00301604928/6.02214076e23
    replay=[]
    for row in summaries:
        replay.append(dict(case=row['case'],born_kg=row['DD_T_birth_atoms']*kg_atom,consumed_kg=row['DT_burn_atoms']*kg_atom,
            remaining_kg=row['remaining_T_atoms']*kg_atom,source_minus_consumed_minus_remaining_kg=(row['DD_T_birth_atoms']-row['DT_burn_atoms']-row['remaining_T_atoms'])*kg_atom,
            scope='Finite-box source/sink replay, not annual reactor inventory or qualified export'))
    write('fuel_cycle_replay.csv',replay)
if __name__=='__main__':main()
