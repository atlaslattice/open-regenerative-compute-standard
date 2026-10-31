# Recovery and evidence boundary

The preceding conversation recorded a completed v0.1 source–field–target test,
including25 coupled checks,19 tests and field-on expected reactions
0.016280331463329765. Its files had not yet been committed when the scratch
workspace reset. That unpublished package and its original raw receipts were
not found in the restored workspace. Published PR50 and PR53 remain available.

This v0.2 reconstructs the numerical scenario and interface from the visible
source/protocol record, then executes it again. It is a new artifact, not a
claim that the lost files were recovered byte-for-byte. The receiver source and
its dependency lock match the previously recorded SHA256s. WarpX26.10 is restored
from the published package URL lock. The public FEMM dataset is recovered by its
pinned Git blob; its canonical-mm interpretation is regenerated with PR53 code.

Two fresh v0.2 runs pass. The current field-on result0.01628033146332977 differs
from the transcribed prior scalar by3.47e-18, consistent with numerical arithmetic.
This is a comparison to a prior reported scalar, not independent validation or
verification of the lost v0.1 raw files. Fresh v0.2 raw boundary fields, reduced
diagnostics, reaction totals and conservation residuals do reproduce between
run001 and run002; those data and receipts are preserved here.

The original protocol's openPMD iteration API failure is known from the
conversation, but no lost failure log is fabricated. The rebuilt extractor uses
explicit iteration keys supported by the installed API.
