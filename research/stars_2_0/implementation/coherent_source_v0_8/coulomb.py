"""Archive-pinned Michel Coulomb backend; GSL retained only for 3j coefficients."""
import ctypes as C,hashlib,json,math,os
from functools import lru_cache
from pathlib import Path
from gsl_reference import cg,VERSION

ROOT=Path(__file__).resolve().parent
BACKEND='MICHEL_CPC_FROM_ORM_ZENODO1174079'
_path=Path(os.environ.get('STELLAR_CPC_LIBRARY',str(ROOT/'build/libcpc.so')))
_record=json.loads((_path.parent/'BUILD_RECEIPT.json').read_text())
if _record['upstream_archive_sha256']!='12a2d7de9f8ece865a4c87987b16bf8e3e921b01f5334cf94acc4b69743f7e3c' or hashlib.sha256(_path.read_bytes()).hexdigest()!=_record['library_sha256']:
    raise ValueError('Coulomb backend build identity mismatch')
lib=C.CDLL(str(_path.resolve()));fn=lib.cpc_fg
fn.argtypes=[C.c_int,C.c_double,C.c_double,C.POINTER(C.c_double)];fn.restype=C.c_int

@lru_cache(maxsize=100000)
def waves(l,eta,rho):
    if isinstance(l,bool) or not isinstance(l,int) or l<0 or not math.isfinite(eta) or eta<0 or not math.isfinite(rho) or rho<=0:
        raise ValueError('valid l, eta>=0, rho>0 required')
    out=(C.c_double*4)();status=fn(l,eta,rho,out)
    if status:raise ArithmeticError('Michel Coulomb error; event not silently dropped')
    F,Fp,G,Gp=list(out);D=F*F+G*G;wr=Fp*G-F*Gp
    if not math.isfinite(D) or D<=0 or abs(wr-1)>1e-8:raise ArithmeticError('Coulomb denominator/Wronskian failed')
    return dict(F=F,Fp=Fp,G=G,Gp=Gp,P=rho/D,S=rho*(F*Fp+G*Gp)/D,phi=math.atan2(F,G),wronskian=wr)
