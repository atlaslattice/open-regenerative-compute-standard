"""GSL Coulomb functions with fail-closed error handling; no silent zero substitution."""
import ctypes as C
import ctypes.util,math
from functools import lru_cache

class Result(C.Structure):_fields_=[('val',C.c_double),('err',C.c_double)]
_path=ctypes.util.find_library('gsl')
if not _path:raise ImportError('GNU GSL shared library required; tested GSL2.7.1')
lib=C.CDLL(_path);lib.gsl_set_error_handler_off()
VERSION=C.c_char_p.in_dll(lib,'gsl_version').value.decode()
_fg=lib.gsl_sf_coulomb_wave_FG_e
_fg.argtypes=[C.c_double,C.c_double,C.c_double,C.c_int,*([C.POINTER(Result)]*4),C.POINTER(C.c_double),C.POINTER(C.c_double)]
_fg.restype=C.c_int
_w3=lib.gsl_sf_coupling_3j;_w3.argtypes=[C.c_int]*6;_w3.restype=C.c_double

@lru_cache(maxsize=100000)
def waves(l,eta,rho):
    if isinstance(l,bool) or not isinstance(l,int) or l<0 or not math.isfinite(eta) or eta<0 or not math.isfinite(rho) or rho<=0:
        raise ValueError('valid l, eta>=0, rho>0 required')
    F,Fp,G,Gp=[Result() for _ in range(4)];ef,eg=C.c_double(),C.c_double()
    status=_fg(eta,rho,float(l),0,C.byref(F),C.byref(Fp),C.byref(G),C.byref(Gp),C.byref(ef),C.byref(eg))
    if status or ef.value or eg.value:raise ArithmeticError(f'Coulomb status/scaling unsupported: {status}, {ef.value}, {eg.value}; event not dropped')
    vals=[r.val for r in [F,Fp,G,Gp]]
    if not all(map(math.isfinite,vals)):raise ArithmeticError('nonfinite Coulomb result')
    D=F.val*F.val+G.val*G.val
    if not math.isfinite(D) or D<=0:raise ArithmeticError('Coulomb denominator overflow/underflow')
    wr=Fp.val*G.val-F.val*Gp.val
    if abs(wr-1)>1e-8:raise ArithmeticError('Coulomb Wronskian check failed')
    return dict(F=F.val,Fp=Fp.val,G=G.val,Gp=Gp.val,P=rho/D,
        S=rho*(F.val*Fp.val+G.val*Gp.val)/D,phi=math.atan2(F.val,G.val),wronskian=wr)

@lru_cache(maxsize=None)
def cg(j1,m1,j2,m2,J,M):
    if m1+m2!=M or abs(m1)>j1 or abs(m2)>j2 or abs(M)>J:return 0.
    return (-1.)**(j1-j2+M)*math.sqrt(2*J+1)*_w3(2*j1,2*j2,2*J,2*m1,2*m2,-2*M)
