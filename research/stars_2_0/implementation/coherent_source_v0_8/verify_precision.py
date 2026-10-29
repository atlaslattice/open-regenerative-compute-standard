"""Three-way Coulomb comparison; arbitrary precision is independent of native backends."""
import argparse,json
from pathlib import Path
import mpmath as mp
from coulomb import waves
from gsl_reference import waves as gsl,VERSION

def main():
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError('preserve earlier comparison')
    mp.mp.dps=40;rows=[]
    for l in [0,1,2,3]:
        for eta in [0.,.5,1.,2.,5.]:
            for rho in [.5,1.,2.,5.]:
                F=mp.coulombf(l,eta,rho);G=mp.coulombg(l,eta,rho)
                Fp=mp.diff(lambda x:mp.coulombf(l,eta,x),rho);Gp=mp.diff(lambda x:mp.coulombg(l,eta,x),rho);D=F*F+G*G
                ref=dict(P=float(rho/D),S=float(rho*(F*Fp+G*Gp)/D));c=waves(l,eta,rho);g=gsl(l,eta,rho)
                rows.append(dict(l=l,eta=eta,rho=rho,mpmath=ref,Michel=dict(P=c['P'],S=c['S']),GSL=dict(P=g['P'],S=g['S']),
                    Michel_P_relative_error=abs(c['P']/ref['P']-1),Michel_S_absolute_error=abs(c['S']-ref['S']),
                    GSL_P_relative_error=abs(g['P']/ref['P']-1),GSL_S_absolute_error=abs(g['S']-ref['S'])))
    r=dict(mpmath_version=mp.__version__,decimal_digits=40,points=len(rows),
        max_Michel_P_relative_error=max(x['Michel_P_relative_error'] for x in rows),max_Michel_S_absolute_error=max(x['Michel_S_absolute_error'] for x in rows),
        max_GSL_P_relative_error=max(x['GSL_P_relative_error'] for x in rows),max_GSL_S_absolute_error=max(x['GSL_S_absolute_error'] for x in rows),
        GSL_version=VERSION,production_backend='Michel_CPC',rows=rows)
    r['passed_production_gate']=r['max_Michel_P_relative_error']<1e-7 and r['max_Michel_S_absolute_error']<1e-7
    a.out.mkdir(parents=True,exist_ok=False);(a.out/'COMPARISON.json').write_text(json.dumps(r,indent=2,allow_nan=False)+'\n')
    print(json.dumps({key:value for key,value in r.items() if key!='rows'}))
    if not r['passed_production_gate']:raise ValueError('production Coulomb gate failed')

if __name__=='__main__':main()
