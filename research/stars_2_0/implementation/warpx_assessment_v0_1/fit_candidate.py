# Copyright 2021 Neil Zaim (upstream formulas); assessment wrapper adapted for Stellar Forge.
"""Standalone candidate-model audit, not a calibrated event kernel or PIC calculation.
Coefficients and expressions adapted from pinned WarpX source (Neil Zaim, 2021).
See vendor/LICENSE.txt for retained BSD-3-Clause-LBNL terms and original headers.
"""
import math
QE=1.602176634e-19; C=299792458.; EPS=8.8541878188e-12; HBAR=1.0545718176461565e-34
MP=1.67262192595e-27; ME=9.1093837139e-31; MU=1.66053906892e-27
MB=11.00930536*MU-5*ME
REDUCED=MP*MB/(MP+MB)
GAMOW_MEV=REDUCED/2*(QE*QE*5/(2*EPS*HBAR))**2*1e-6/QE

def positive(x):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x) or x<0:raise ValueError('Finite nonnegative numeric energy required')

def sigma_cm_m2(E_keV,*,allow_buck_tail=False):
    positive(E_keV)
    if E_keV==0:return 0.
    if E_keV>9760:
        if not allow_buck_tail:raise ValueError('Above Tentori fit domain: explicit high-energy tail scenario required')
        return .01277998*(E_keV/9760)**(-2.661840717596765)*1e-28
    E_MeV=E_keV*.001
    if E_keV<400:
        S=197+.269*E_keV+2.54e-4*E_keV**2+1.82e4/((E_keV-148)**2+2.35**2)
    elif E_keV<668:
        z=(E_keV-400)*.01;S=346+150*z-59.9*z*z-.460*z**5
    else:
        S=sum(a/((E_keV-e)**2+d*d) for a,e,d in [(1.98e6,640.9,85.5),(3.89e6,1211,414),(1.36e6,2340,221),(3.71e6,3294,351)])+.381
    return S/E_MeV*math.exp(-math.sqrt(GAMOW_MEV/E_MeV))*1e-28

def stationary_boron_lab_to_cm_keV(E_lab_keV):
    """Relativistic invariant pair kinetic energy; stationary B11 ONLY."""
    positive(E_lab_keV);T=E_lab_keV*1000*QE
    rest=(MP+MB)*C*C
    cm=2*MB*C*C*T/(math.sqrt(rest*rest+2*MB*C*C*T)+rest)
    return cm/(1000*QE)
