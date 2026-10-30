"""Two distinct apparatus: D-D isotope generator A, sustained D-T generator B.
Synthetic-only reference ledger; WarpX outputs must be separately validated.
"""
import json, math, argparse
from pathlib import Path
EV_J=1.602176634e-19
MEV_J=1e6*EV_J
DD_Q_TP_MEV=4.033
DD_Q_HE3N_MEV=3.269
DT_Q_MEV=17.589
def evaluate(c):
    a=float(c["reactor_a_dd_fusion_power_w"]);b=float(c["reactor_b_dt_fusion_power_w"])
    frac=float(c.get("dd_tritium_branch_fraction",.5))
    extract=float(c.get("dd_tritium_delivery_fraction",1))
    tbr=float(c.get("effective_b_blanket_tritium_per_dt_reaction",0))
    assert a>=0 and b>=0 and 0<=frac<=1 and 0<=extract<=1 and tbr>=0
    qdd=frac*DD_Q_TP_MEV+(1-frac)*DD_Q_HE3N_MEV
    reactions_a=a/(qdd*MEV_J) if qdd else 0.
    tritium_a=reactions_a*frac*extract
    he3_a=reactions_a*(1-frac)
    reactions_b=b/(DT_Q_MEV*MEV_J)
    blanket=reactions_b*tbr
    losses=float(c.get("additional_tritium_loss_atoms_per_s",0))
    assert losses>=0
    deficit=reactions_b+losses-tritium_a-blanket
    return {"status":"ILLUSTRATIVE_STEADY_STATE_ARITHMETIC_NOT_VALIDATED","reactor_a_dd_reactions_per_s":reactions_a,"reactor_a_he3_produced_atoms_per_s":he3_a,"reactor_a_tritium_delivered_atoms_per_s":tritium_a,"reactor_b_dt_reactions_per_s":reactions_b,"reactor_b_tritium_consumption_atoms_per_s":reactions_b,"reactor_b_blanket_tritium_produced_atoms_per_s":blanket,"required_external_tritium_atoms_per_s":max(deficit,0),"net_tritium_surplus_atoms_per_s":-deficit,"dd_only_coverage_fraction":tritium_a/reactions_b if reactions_b else None,"minimum_effective_tbr_for_balance":max(0,(reactions_b+losses-tritium_a)/reactions_b) if reactions_b else None,"assumptions":"effective TBR models recovered usable tritium; no reactor startup inventory, decay, purification delay, burn fraction, blanket neutron physics, electric conversion, or logistics modeled"}
def main():
 p=argparse.ArgumentParser();p.add_argument("scenario",type=Path);z=p.parse_args()
 print(json.dumps(evaluate(json.loads(z.scenario.read_text())),indent=2))
if __name__=="__main__":main()
