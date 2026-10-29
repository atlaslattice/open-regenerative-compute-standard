"""Compare GSL with independent Michel Coulomb code recovered from the ORM archive.
Downloads upstream source without vendoring/relicensing it; requires a C++ compiler.
"""
import argparse,hashlib,io,json,subprocess,zipfile,urllib.request
from pathlib import Path
from gsl_reference import waves,VERSION

URL='https://zenodo.org/records/1174079/files/ORM-v1.0-be2fbae9fe05ddb3647071f29c3b963359e65103.zip'
SHA='12a2d7de9f8ece865a4c87987b16bf8e3e921b01f5334cf94acc4b69743f7e3c'
WRAPPER=r'''#include <cpc/cwfcomp.h>
#include <iostream>
#include <iomanip>
int main(){double l,eta,rho;std::cout<<std::setprecision(17);
while(std::cin>>l>>eta>>rho){Coulomb_wave_functions c(true,std::complex<double>(l,0),std::complex<double>(eta,0));
std::complex<double> F,dF,G,dG;c.F_dF(rho,F,dF);c.G_dG(rho,G,dG);
std::cout<<F.real()<<" "<<dF.real()<<" "<<G.real()<<" "<<dG.real()<<"\n";}}
'''

def main():
    p=argparse.ArgumentParser();p.add_argument('--archive',type=Path,required=True);p.add_argument('--download',action='store_true');p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError('preserve previous comparison')
    if a.download and not a.archive.exists():
        data=urllib.request.urlopen(URL,timeout=30).read()
        if hashlib.sha256(data).hexdigest()!=SHA:raise ValueError('upstream archive hash mismatch')
        a.archive.parent.mkdir(parents=True,exist_ok=True);a.archive.write_bytes(data)
    data=a.archive.read_bytes()
    if hashlib.sha256(data).hexdigest()!=SHA:raise ValueError('upstream archive hash mismatch')
    a.out.mkdir(parents=True,exist_ok=False);z=zipfile.ZipFile(io.BytesIO(data))
    for name in z.namelist():
        path=Path(name)
        if path.is_absolute() or '..' in path.parts:raise ValueError('unsafe upstream member')
    z.extractall(a.out/'upstream')
    base=next((a.out/'upstream').iterdir())/'external/cpc'
    cpp=a.out/'compare.cpp';cpp.write_text(WRAPPER);exe=(a.out/'compare').resolve()
    command=['c++','-std=c++11','-O2','-I'+str(base/'include'),str(cpp),str(base/'src/cwfcomp.cpp'),'-o',str(exe)]
    compile_run=subprocess.run(command,capture_output=True,text=True)
    (a.out/'COMPILE_LOG.txt').write_text(compile_run.stdout+compile_run.stderr)
    if compile_run.returncode:raise RuntimeError('independent Coulomb compilation failed')
    points=[(l,e,r) for l in [0,1,2,3] for e in [0.,.5,1.,2.,5.] for r in [.5,1.,2.,5.]]
    r=subprocess.run([str(exe)],input=''.join(f'{l} {e} {rho}\n' for l,e,rho in points),capture_output=True,text=True,check=True)
    lines=r.stdout.splitlines()
    if len(lines)!=len(points):raise ValueError('independent output row mismatch')
    rows=[]
    for (l,e,rho),line in zip(points,lines):
        F,Fp,G,Gp=map(float,line.split());D=F*F+G*G
        native=dict(P=rho/D,S=rho*(F*Fp+G*Gp)/D)
        gsl=waves(l,e,rho)
        rows.append(dict(l=l,eta=e,rho=rho,independent=native,GSL={key:gsl[key] for key in ['P','S']},
            P_relative_error=abs(gsl['P']/native['P']-1),S_absolute_error=abs(gsl['S']-native['S'])))
    result=dict(archive_sha256=SHA,GSL_version=VERSION,comparison_points=len(rows),
        max_P_relative_error=max(x['P_relative_error'] for x in rows),max_S_absolute_error=max(x['S_absolute_error'] for x in rows),
        scope='Coulomb numerical routines only; no full ORM suite, source-amplitude reproduction or physics calibration claimed',rows=rows)
    result['passed']=result['max_P_relative_error']<1e-7 and result['max_S_absolute_error']<1e-7
    (a.out/'COMPARISON.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({key:value for key,value in result.items() if key!='rows'}))
    if not result['passed']:raise ValueError('independent numerical gate failed; receipt retained')

if __name__=='__main__':main()
