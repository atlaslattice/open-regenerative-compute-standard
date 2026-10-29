"""Expected counts under an explicit single-hit response matrix.
Columns = true bins; rows = measured bins. Column deficit is non-detection.
No unmeasured response, inverse unfolding, or physical source is invented.
"""
from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class Response:
    response_id: str
    species: str
    true_edges_mev: tuple
    measured_edges_mev: tuple
    probabilities: tuple
    evidence_state: str

    def arrays(self):
        if not self.response_id or self.species not in {'proton','alpha'}:
            raise ValueError('Explicit response and species required')
        if self.evidence_state not in {'SYNTHETIC','SOURCE_TRACED','CALIBRATED'}:
            raise ValueError('Evidence state required')
        edges=[np.asarray(e,dtype=float) for e in (self.true_edges_mev,self.measured_edges_mev)]
        if any(e.ndim!=1 or len(e)<2 or not np.isfinite(e).all() or np.any(e<0) or np.any(np.diff(e)<=0) for e in edges):
            raise ValueError('Finite increasing nonnegative MeV bin edges required')
        R=np.asarray(self.probabilities,dtype=float)
        if R.shape!=(len(edges[1])-1,len(edges[0])-1) or not np.isfinite(R).all() or np.any(R<0) or np.any(R.sum(axis=0)>1):
            raise ValueError('Single-hit response columns must be nonnegative and sum <=1')
        return R

    def fold(self,species,true_counts,background_counts=None,*,calibrated=False):
        R=self.arrays()
        if species!=self.species: raise ValueError('Species/response mismatch')
        if calibrated and self.evidence_state!='CALIBRATED':
            raise ValueError('Response is not calibrated')
        x=np.asarray(true_counts,dtype=float)
        b=np.zeros(R.shape[0]) if background_counts is None else np.asarray(background_counts,dtype=float)
        if x.shape!=(R.shape[1],) or b.shape!=(R.shape[0],) or any(not np.isfinite(v).all() or np.any(v<0) for v in (x,b)):
            raise ValueError('Expected nonnegative finite counts in declared bins')
        try:
            with np.errstate(over='raise',invalid='raise'):
                signal=R@x
                missed=(1-R.sum(axis=0))@x
                total=signal+b
                true_total=x.sum()
        except FloatingPointError as exc:
            raise ValueError('Response/count overflow') from exc
        if not all(np.isfinite(v).all() for v in (signal,missed,total,true_total)):
            raise ValueError('Response/count overflow')
        return {'response_id':self.response_id,'species':species,'signal_expected_counts':signal.tolist(),
            'background_expected_counts':b.tolist(),'total_expected_counts':total.tolist(),
            'undetected_expected_counts':float(missed),'true_expected_counts':float(true_total),
            'count_closure_residual':float(true_total-signal.sum()-missed),
            'statistical_scope':'expected values only; no Poisson-independence or calibrated likelihood asserted'}
