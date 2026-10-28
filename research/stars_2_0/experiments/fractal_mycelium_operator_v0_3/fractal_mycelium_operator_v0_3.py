"""Fractal Path x Atlas Intelligence: offline mycelial operator v0.3.
Research-only components. No LLM agents, transmissions, deployments, authentication,
Canon promotions or external effects. Python 3.10+; standard library only.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Tuple
import hashlib, json, re
HSN = re.compile(r"^H(?:0[1-9]|1[0-2])\.S(?:0[1-9]|1[0-2])\.N(?:0[1-9]|1[0-2])$")
COUNCILS = ("MYCELIAL","KAERON","MANDOG","MIRROR","FOOL",
            "REVERSE_AUDIT","SUCCESS_DRIFT","SOPHIA","ORACLE_DEFENSE","PENDRAGON")
def canonical(obj):
    return json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def digest(obj):
    return hashlib.sha256(canonical(obj).encode("utf-8")).hexdigest()
def address(s):
    return isinstance(s,str) and bool(HSN.fullmatch(s))
@dataclass(frozen=True)
class Hypothesis:
    origin: str
    claim: str
    source_refs: Tuple[str,...]
    uncertainty: str
    dissent: Tuple[str,...] = ()
    domain_tags: Tuple[str,...] = ()
    consent_scope: str = "public-research"
    ttl: int = 3
    max_invites: int = 6
    classification: str = "RESEARCH_HYPOTHESIS"
    def validate(self):
        if not address(self.origin): raise ValueError("invalid HSN operator address")
        if not self.claim.strip() or not self.source_refs or not all(x.strip() for x in self.source_refs): raise ValueError("source-backed claim required")
        if not self.uncertainty.strip(): raise ValueError("uncertainty required")
        if not (0<=self.ttl<=12 and 0<=self.max_invites<=144): raise ValueError("bounded TTL/budget required")
        if self.classification!="RESEARCH_HYPOTHESIS": raise ValueError("no Canon/truth spoofing")
        if self.consent_scope not in ("public-research","isolated-research"): raise ValueError("no sensitive data propagation")
    @property
    def id(self):
        self.validate()
        return digest(self.__dict__)
@dataclass
class WitnessLedger:
    """Append-only in-memory hash-linked records; NOT a cryptographically signed permanent archive."""
    records: list = field(default_factory=list)
    def append(self,kind,subject_id,body):
        if kind not in ("HYPOTHESIS","DISSENT","REJECTION","OBSERVATION","REVIEW","REFLECTION","REVISION"):
            raise ValueError("unrecognized record")
        prev=self.records[-1]["hash"] if self.records else "GENESIS"
        entry={"index":len(self.records),"previous":prev,"kind":kind,
               "subject_id":subject_id,"body":body}
        entry["hash"]=digest(entry)
        self.records.append(entry)
        return entry["hash"]
    def verify(self):
        prev="GENESIS"
        for n,e in enumerate(self.records):
            bare={k:v for k,v in e.items() if k!="hash"}
            if e["index"]!=n or e["previous"]!=prev or digest(bare)!=e["hash"]:return False
            prev=e["hash"]
        return True
def spores(hypothesis,links,relevance,blocked=(),opted_in=()):
    """Produce ordered local candidate invitations. No network I/O and no powers.
    Critically, selection is not proof of truth or consent to external action.
    """
    hypothesis.validate()
    if hypothesis.consent_scope!="public-research":
        return {"status":"ISOLATED_NO_PROPAGATION","invited":[],
                "e145authorization":False,"external_action_executed":False}
    seen={hypothesis.origin};front=[hypothesis.origin];picked=[]
    permitted=set(opted_in);blocked=set(blocked)
    for _ in range(hypothesis.ttl):
        options=set()
        for u in front:
            for v in links.get(u,()):
                if address(v) and v not in seen and v not in blocked and v in permitted:
                    options.add(v)
        ranked=sorted(options,key=lambda v:(-float(relevance.get(v,0)),v))
        room=max(0,hypothesis.max_invites-len(picked))
        front=ranked[:room]
        seen.update(options);picked.extend(front)
        if not front:break
    return {"status":"SIMULATED_INVITATIONS","hypothesis_id":hypothesis.id,
            "invited":picked,"e145authorization":False,
            "external_action_executed":False,"canon_promoted":False}
def council_review(h,checks):
    """Roles are labels for independently authored assessments, not autonomous agents."""
    h.validate()
    checked={k:checks.get(k,"NOT_RUN") for k in COUNCILS}
    for k,v in checked.items():
        if v not in ("PASS","FLAG","NOT_RUN"):raise ValueError("invalid review result")
    halted=any(checked[k]=="FLAG" for k in ("MANDOG","MIRROR","REVERSE_AUDIT","SUCCESS_DRIFT"))
    return {"hypothesis_id":h.id,"roles":checked,
            "research_decision":"QUARANTINE_FOR_HUMAN_REVIEW" if halted else "RESEARCH_ONLY_NOT_VALIDATED",
            "e145authorization":False,"canon_promoted":False}
def reward_update(previous,independent_result,source_verified=False):
    """No voting-by-copy, no claimed reward from applause alone."""
    if independent_result not in ("VERIFIED_USEFUL","VERIFIED_FALSE","UNTESTED"):
        raise ValueError("invalid result")
    delta=1 if independent_result=="VERIFIED_USEFUL" and source_verified else -1 if independent_result=="VERIFIED_FALSE" and source_verified else 0
    return max(-3,min(3,int(previous)+delta))
def reverse_audit(before,after,limits):
    """Measured outcomes; no fabricated ecological metrics.
    A higher score may not compensate for violating explicit thresholds.
    """
    keys=("verified_discoveries","bytes_sent","compute_units","unresolved_harms","dissent_retained")
    if any(k not in before or k not in after for k in keys):raise ValueError("missing measured metric")
    exceeded={k:after[k] for k,limit in limits.items() if k in after and after[k]>limit}
    return {"metrics_before":{k:before[k] for k in keys},
            "metrics_after":{k:after[k] for k in keys},
            "threshold_breaches":exceeded,
            "apparent_success_with_drift":after["verified_discoveries"]>before["verified_discoveries"] and bool(exceeded),
            "review_required":bool(exceeded),"external_action_executed":False}
