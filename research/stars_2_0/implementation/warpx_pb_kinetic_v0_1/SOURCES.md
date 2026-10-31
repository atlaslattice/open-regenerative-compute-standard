# Sources and provenance

- WarpX26.10 release-source pin ec1660d961696c865c87c26728b7e248b5454082:
  https://github.com/BLAST-WarpX/warpx/tree/ec1660d961696c865c87c26728b7e248b5454082
  Seven original fixtures/parser/notices are byte-exact by Git blob hashes in
  UPSTREAM_SOURCE_INDEX.json. Original LICENSE.txt and NOTICE.txt retained.
- Other thread's installation: ORCS PR48, pinned674eb174ff935bcfc9829109b57c1187d25dc710,
  research/stars_2_0/extensions/beyond_q/kinetic_source_v1_3/outputs/environment_explicit.txt.
  URL list transformed to a standard @EXPLICIT install file. Installation warnings
  about missing lock checksums remain in INSTALL.log; no safety checks disabled.
  Current installed metadata and critical binary SHA256s are separately recorded.
- Previous scalar assessment: PR47 at a37fa6601c085a29ac393b8d92e7652a6ef46707.
  Development source pin a389dc54a27136176bdd48f7bfd36da62a873a61. Cross-section,
  constants and license blobs inspected there match the26.10 source tree exactly.
  This is source-file equivalence, not binary attestation.
- External field, injection and diagnostics definitions:
  https://github.com/BLAST-WarpX/warpx/blob/ec1660d961696c865c87c26728b7e248b5454082/Docs/source/usage/parameters.rst
  SingleParticle uses gamma*beta for input u; reduced ParticleExtrema outputs SI
  momentum. Exported states use kg m/s, m, s and physical particle weights.
- New orbit fixture and independent Lorentz ODE are GPTWork numerical verification
  contributions directed by Dave Sheldon / Atlas Lattice. These are not measured
  field maps, material data or endorsed PRISM designs. No institutional endorsement.

No WarpX solver fork, patch or binary redistribution. Existing Stellar Forge
modules remain independent; no automatic model/evidence promotion.
