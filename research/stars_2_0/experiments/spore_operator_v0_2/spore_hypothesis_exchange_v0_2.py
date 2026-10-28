"""Atlas Intelligence spore hypothesis exchange v0.2 (pure Python, no side effects).
NOT a live agent network, a semantic verifier or permission to act externally.
"""
from dataclasses import dataclass, field
import hashlib,json,re
HSN=re.compile(r"^H(?:0[1-9]|1[0-2])[.]S(?:0[1-9]|1[0-2])[.]N(?:0[1-9]|1[0-2])$")
@dataclass(frozen=True)
class Spore:
    origin: str
    claim: str
    sources: tuple
    uncertainty: str
    ttl: int=3
    budget: int=6
    kind: str="HYPOTHESIS_NON_CANON"
    def validate(self):
        if not HSN.fullmatch(self.origin): raise ValueError("invalid HSN")
        if not self.claim.strip() or not self.sources or any(not s for s in self.sources): raise ValueError("unattributed claim")
        if not (0<=self.ttl<=12 and 0<=self.budget<=144): raise ValueError("unbounded propagation")
        if self.kind!="HYPOTHESIS_NON_CANON": raise ValueError("cannot spoof Canon")
    def receipt_id(self):
        self.validate()
        return hashlib.sha256(json.dumps(self.__dict__,sort_keys=True,default=list).encode()).hexdigest()
def invitational_propagate(spore,neighbors,relevance,blocked=frozenset()):
    """Produce explicit candidate invitations: no network sends and no mutation.
    neighbors: dict HSN->[HSN]; relevance: dict HSN->validated selector score.
    Missing scores default to zero. Preserve budget and TTL.
    """
    spore.validate()
    if spore.ttl==0 or spore.budget==0: return {"invited":[],"kind":"RESEARCH_ONLY"}
    frontier=[spore.origin];seen={spore.origin};selected=[]
    for depth in range(spore.ttl):
        candidates=[]
        for u in frontier:
            for v in neighbors.get(u,()):
                if v in seen or v in blocked or not HSN.fullmatch(v):continue
                seen.add(v)
                candidates.append(v)
        candidates.sort(key=lambda n:(-float(relevance.get(n,0)),n))
        remaining=spore.budget-len(selected)
        if remaining<=0:break
        frontier=candidates[:remaining]
        selected.extend(frontier)
        if not frontier:break
    return {"spore_receipt":spore.receipt_id(),"invited":selected,"kind":"RESEARCH_ONLY",
            "external_action_executed":False,"e145authorization":False,
            "canon_promoted":False,"dissent_preserved":True}
