"""Build archive-pinned Michel Coulomb backend; upstream source stays in build output."""
import argparse,hashlib,io,json,subprocess,urllib.request,zipfile
from pathlib import Path
from compare_coulomb import URL,SHA

WRAPPER=r'''#include <cpc/cwfcomp.h>
#include <cmath>
extern "C" int cpc_fg(int l,double eta,double rho,double*out){
try{Coulomb_wave_functions c(true,std::complex<double>(l,0),std::complex<double>(eta,0));
std::complex<double> F,dF,G,dG;c.F_dF(rho,F,dF);c.G_dG(rho,G,dG);
out[0]=F.real();out[1]=dF.real();out[2]=G.real();out[3]=dG.real();
for(int i=0;i<4;++i)if(!std::isfinite(out[i]))return 2;return 0;}catch(...){return 1;}}
'''

def main():
    p=argparse.ArgumentParser();p.add_argument('--archive',type=Path,required=True);p.add_argument('--download',action='store_true');p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    if a.out.exists():raise FileExistsError('choose a new build directory')
    if a.download and not a.archive.exists():
        data=urllib.request.urlopen(URL,timeout=30).read()
        if hashlib.sha256(data).hexdigest()!=SHA:raise ValueError('upstream archive identity mismatch')
        a.archive.parent.mkdir(parents=True,exist_ok=True);a.archive.write_bytes(data)
    data=a.archive.read_bytes()
    if hashlib.sha256(data).hexdigest()!=SHA:raise ValueError('upstream archive identity mismatch')
    a.out.mkdir(parents=True,exist_ok=False);z=zipfile.ZipFile(io.BytesIO(data))
    for n in z.namelist():
        if Path(n).is_absolute() or '..' in Path(n).parts:raise ValueError('unsafe archive member')
    z.extractall(a.out/'upstream');root=next((a.out/'upstream').iterdir());base=root/'external/cpc'
    cpp=a.out/'wrapper.cpp';cpp.write_text(WRAPPER);library=a.out/'libcpc.so'
    command=['c++','-std=c++11','-O2','-shared','-fPIC','-I'+str(base/'include'),str(cpp),str(base/'src/cwfcomp.cpp'),'-o',str(library)]
    r=subprocess.run(command,capture_output=True,text=True);(a.out/'COMPILE_LOG.txt').write_text(r.stdout+r.stderr)
    if r.returncode:raise RuntimeError('Coulomb backend build failed')
    record=dict(upstream_url=URL,upstream_archive_sha256=SHA,library_sha256=hashlib.sha256(library.read_bytes()).hexdigest(),
        compiler=subprocess.run(['c++','--version'],capture_output=True,text=True).stdout.splitlines()[0],
        source_sha256={str(f.relative_to(root)):hashlib.sha256(f.read_bytes()).hexdigest() for f in [base/'src/cwfcomp.cpp',base/'include/cpc/cwfcomp.h',base/'include/cpc/complex_functions.h',root/'LICENSE']},
        wrapper_sha256=hashlib.sha256(cpp.read_bytes()).hexdigest(),license='upstream ORM archive GPL3-or-later; upstream files kept with their notices',GSL_coulomb_used=False)
    (a.out/'BUILD_RECEIPT.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record))

if __name__=='__main__':main()
