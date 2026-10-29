"""Synthetic forced-mode benchmark; no acoustic-to-nuclear coupling."""
import math

LOCATIONS={'pitcher','catcher','support','beamline_component'}

def validate(c):
    required={'location','arm','waveform','carrier_Hz','deviation_Hz','modulation_Hz','phase_rad','acceleration_m_s2','duration_s','start_before_shot_s','samples','mode_Hz','damping_ratio','driver_wall_J'}
    if set(c)!=required:raise ValueError('acoustic schema fields mismatch')
    if c['location'] not in LOCATIONS or c['arm'] not in {'REFERENCE','OFF','SHAM','ON'}:raise ValueError('invalid acoustic location/arm')
    if c['waveform'] not in {'tone','sinusoidal_FM','linear_chirp'}:raise ValueError('unknown waveform')
    for k in required-{'location','arm','waveform','samples'}:
        if isinstance(c[k],bool) or not isinstance(c[k],(int,float)) or not math.isfinite(c[k]):raise ValueError('finite acoustic numbers required')
    if type(c['samples'])!=int or not 100<=c['samples']<=20000:raise ValueError('acoustic sample limit 100..20000')
    for k in ['carrier_Hz','duration_s','mode_Hz']:
        if c[k]<=0:raise ValueError('positive '+k+' required')
    for k in ['deviation_Hz','modulation_Hz','acceleration_m_s2','start_before_shot_s','driver_wall_J']:
        if c[k]<0:raise ValueError('nonnegative '+k+' required')
    if not 0<c['damping_ratio']<=1:raise ValueError('benchmark supports 0<damping<=1')
    if c['carrier_Hz']<c['deviation_Hz']:raise ValueError('instantaneous frequency must be nonnegative')
    if c['waveform']=='tone' and c['deviation_Hz']!=0:raise ValueError('tone deviation must be zero')
    if c['waveform']=='sinusoidal_FM' and c['modulation_Hz']<=0:raise ValueError('positive modulation frequency required')
    if c['duration_s']>c['start_before_shot_s']:raise ValueError('benchmark actuation must end no later than shot arrival')
    dt=c['duration_s']/c['samples']
    if dt*max(c['carrier_Hz']+c['deviation_Hz'],c['mode_Hz'],c['modulation_Hz'])>1/40:
        raise ValueError('FAIL_NONCONVERGENCE: insufficient time sampling')
    if c['arm'] in {'REFERENCE','OFF'} and c['driver_wall_J']!=0:raise ValueError('reference/OFF intended drive must be zero')


def acceleration(c,t):
    if c['arm']!='ON':return 0.
    f=c['carrier_Hz'];d=c['deviation_Hz'];m=c['modulation_Hz']
    phase=2*math.pi*f*t+c['phase_rad']
    if c['waveform']=='sinusoidal_FM':phase+=d/m*(1-math.cos(2*math.pi*m*t))
    if c['waveform']=='linear_chirp':phase+=2*math.pi*(-d*t+d*t*t/c['duration_s'])
    return c['acceleration_m_s2']*math.sin(phase)


def integrate(c,n):
    dt=c['duration_s']/n;w=2*math.pi*c['mode_Hz'];g=2*c['damping_ratio']*w
    x=v=0.;rows=[]
    def rhs(t,x,v):return v,acceleration(c,t)-g*v-w*w*x
    for i in range(n+1):
        t=i*dt
        rows.append([t-c['start_before_shot_s'],acceleration(c,t),x,v])
        if i==n:break
        a,b=rhs(t,x,v);d,e=rhs(t+dt/2,x+dt*a/2,v+dt*b/2)
        f,h=rhs(t+dt/2,x+dt*d/2,v+dt*e/2);j,k=rhs(t+dt,x+dt*f,v+dt*h)
        x+=dt*(a+2*d+2*f+j)/6;v+=dt*(b+2*e+2*h+k)/6
        if not math.isfinite(x+v):raise ValueError('acoustic numerical overflow')
    return rows


def run(c):
    if c is None:return {'status':'NOT_CONFIGURED','nuclear_feedback':'NONE'}
    validate(c);a=integrate(c,c['samples']);b=integrate(c,2*c['samples'])
    err=max(abs(x[2]-y[2]) for x,y in zip(a,b[::2]))
    peak=max(abs(x[2]) for x in b)
    # Numerical consistency gate only, not a specimen tolerance.
    if err>1e-12+1e-3*peak:raise ValueError('FAIL_NONCONVERGENCE: coarse/fine displacement disagreement')
    stride=max(1,len(b)//500)
    trace=b[::stride]
    if trace[-1]!=b[-1]:trace.append(b[-1])
    return {'status':'SYNTHETIC_LINEAR_MODE_ONLY','configuration':c,'equation':'x_ddot + 2*zeta*omega0*x_dot + omega0^2*x = prescribed acceleration(t)',
            'peak_displacement_m':peak,'rms_displacement_m':math.sqrt(sum(r[2]**2 for r in b)/len(b)),
            'coarse_fine_max_error_m':err,'trace_columns':['time_relative_to_shot_s','acceleration_m_s2','displacement_m','velocity_m_s'],
            'trace':trace,'nuclear_feedback':'NONE','stress_fatigue':'NOT_INFERRED_FROM_DISPLACEMENT',
            'driver_wall_accounting':'declared separately; no inferred electromechanical efficiency',
            'limitations':['synthetic single mode; no measured transfer function','location is metadata, not a distinct physical plant','SHAM zero coherent forcing does not model its thermal/EM effects','residual vibration after actuation is not evolved to shot time if actuation ends earlier']}
