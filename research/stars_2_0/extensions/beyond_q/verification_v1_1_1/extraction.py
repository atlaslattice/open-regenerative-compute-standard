"""Two distinct residence/flow hypotheses; constant source S in kg/day."""
import math
from fuelcycle.inventory import advance

def compare(epsilon,loop_minutes,source_kg_day,loss_day):
    if not 0<epsilon<=1 or loop_minutes<=0 or source_kg_day<=0 or loss_day<0:
        raise ValueError('invalid extraction parameters')
    tau=loop_minutes/1440;k=epsilon/tau;S=source_kg_day
    mixed=S/(k+loss_day)
    survival=math.exp(-loss_day*tau)
    phi=-math.expm1(-loss_day*tau)/loss_day if loss_day else tau
    post=(1-epsilon)*S*phi/(1-(1-epsilon)*survival)
    pre=post*survival+S*phi
    # Exact integral of stock over a cycle, using integral of ODE if L>0.
    if loss_day:
        mean=post*phi/tau+S*(tau-phi)/(loss_day*tau)
    else:mean=post+S*tau/2
    return dict(epsilon=epsilon,loop_minutes=loop_minutes,
        mixed_stock_kg=mixed,discrete_post_kg=post,discrete_pre_kg=pre,
        discrete_mean_kg=mean,mixed_recovery=k/(k+loss_day),
        discrete_recovery=epsilon*pre/(S*tau),
        note='Constant-source steady candidates; no processing or storage qualification')
