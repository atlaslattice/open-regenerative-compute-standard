# House 5 Arts Module Sprint Proposal

**Document ID:** ORC-026 (Proposed)
**Version:** 1.0
**Date:** April 28, 2026
**Author:** Manus (S7 Build Seat)
**Status:** PROPOSAL — Requires Council ratification (3+ seats) before Sprint assignment

---

## §1 Executive Summary

House 5 (Arts, Spheres 49–60) is the only House in the 12×12 Ontological Matrix with **zero Build Plan modules**. This represents the largest structural gap in the standard. Given that generative AI for visual arts, music, film, and design constitutes one of the fastest-growing compute workloads globally — with the generative AI creative market projected to exceed $110B by 2030 — this gap is both strategically significant and operationally urgent.

This proposal defines **6 new modules (M158–M163)** covering the four priority Spheres (49, 51, 54, 57) plus two cross-cutting governance modules that apply to all creative content routing. The modules are designed to integrate with existing Build Plan infrastructure (TransparencyPacket, INV-7c, TOS Compliance Architecture, C2PA provenance standards) while introducing novel governance primitives specific to creative work: **attribution chains**, **consent provenance**, **style sovereignty**, and **regenerative royalty routing**.

---

## §2 Strategic Justification

### §2.1 Why House 5 Matters Now

The absence of House 5 modules creates three operational risks:

1. **Routing Blind Spot:** When a user requests creative content generation (image, music, video, design), the Constitutional Router has no sphere-specific governance to apply. It falls back to generic H2/H7 routing rules, which lack creative-domain constraints (attribution, consent, style rights).

2. **TOS Exposure:** Creative content generation is the domain with the highest TOS variance across providers. OpenAI (DALL-E), Google (Imagen), Anthropic (no image gen), Adobe (Firefly + C2PA), Stability AI (open-weight), and Suno/Udio (music) each have radically different licensing, attribution, and usage rights. Without M142-M145 TOS Compliance Architecture having creative-specific policy profiles, the system cannot safely route creative workloads.

3. **Regulatory Convergence:** The EU AI Act Article 50 mandates transparency labeling for AI-generated content (effective August 2025). The US Copyright Office has ruled that purely AI-generated works cannot be copyrighted (Thaler v. Perlmutter, 2023; reaffirmed 2025). SAG-AFTRA's 2025 Interactive Media Agreement requires consent and disclosure for AI digital replicas. California's synthetic performer transparency law takes effect June 2026. New York's AI performer disclosure law is active. The standard MUST have governance modules that route creative workloads in compliance with this evolving regulatory landscape.

### §2.2 Seat Coverage Analysis

From the Federation Integration v1.0, existing seat coverage for House 5 spheres:

| Sphere | Domain | Seat Coverage | Capability Level |
|--------|--------|---------------|-----------------|
| 49 | Visual Arts | Amazon (Titan Image), Google (Imagen), OpenAI (DALL-E) | STRONG |
| 50 | Performing Arts | None | ZERO |
| 51 | Music | Google (MusicLM/MusicFX), Suno*, Udio* | MODERATE |
| 52 | Dance | None | ZERO |
| 53 | Theater | None | ZERO |
| 54 | Film | Google (Veo), OpenAI (Sora), Runway* | STRONG |
| 55 | Literature (creative) | Anthropic, OpenAI, Google | STRONG |
| 56 | Architecture | Microsoft (Copilot), Google | MODERATE |
| 57 | Design | Adobe*, Microsoft (Designer), Google | STRONG |
| 58 | Photography | Adobe (Lightroom AI), Google | MODERATE |
| 59 | Sculpture | None | ZERO |
| 60 | Painting | Same as Sphere 49 | STRONG |

*Not current Council seats but potential future providers.

**Priority selection rationale:** Spheres 49, 51, 54, and 57 are chosen because they have (a) existing seat coverage, (b) active commercial demand, (c) regulatory urgency, and (d) the highest TOS variance requiring governance.

---

## §3 Module Specifications

### M158: Creative Content Provenance Engine (Sphere 49 — Visual Arts)

**Purpose:** Ensure every AI-generated or AI-assisted visual artifact carries cryptographically verifiable provenance metadata conforming to C2PA v1.3+ and Content Credentials standards.

**Layer:** L4 (Element 145 — Service Orchestration)

**Dependencies:** M142 (TOS Compliance Gate), M131 (KYA Credential Envelope), TransparencyPacket v1.2

**Key Functions:**

| Function | Description | Standard |
|----------|-------------|----------|
| `embed_provenance()` | Attaches C2PA manifest to generated image with model ID, prompt hash, training data attestation | C2PA v1.3 |
| `verify_chain()` | Validates provenance chain from generation through any edits/compositing | CAI (Content Authenticity Initiative) |
| `strip_for_privacy()` | Removes prompt content while preserving provenance chain integrity (per D-104 Content-Minimized Transparency) | ORC-specific |
| `attribution_resolve()` | Maps training data influence to attribution credits using influence function approximation | Novel |
| `consent_check()` | Validates that referenced styles/artists have opt-in consent records in Consent Registry | INV-3 compliance |

**TransparencyPacket v1.3 extension:**
```yaml
creative:
  c2pa_manifest_hash: string        # SHA-256 of embedded C2PA manifest
  generation_model: string           # e.g., "dalle-3", "imagen-3", "firefly-3"
  training_attestation: enum         # LICENSED | OPEN | MIXED | UNKNOWN
  attribution_credits: array         # [{artist_id, influence_score, consent_status}]
  style_sovereignty_check: boolean   # True if style reference passed consent gate
  regulatory_labels: array           # ["EU_AI_ACT_ART50", "NY_SYNTH_DISCLOSURE"]
```

**Invariant compliance:**
- INV-0: No generation of CSAM, deepfakes of real persons without consent, or content designed to deceive
- INV-3: Consent required for style references that approximate identifiable artists
- INV-7c: No single image generation provider >47% of creative routing volume

**Risks:**
- R136 (MEDIUM): C2PA metadata stripping by downstream platforms (mitigation: redundant blockchain anchor via M132)
- R137 (LOW): Attribution influence scoring contested by artists (mitigation: human-in-the-loop override)

**Seat Assignment:** Google (S2, Imagen + C2PA member) PRIMARY, Amazon (S9, Titan Image) SECONDARY, Manus (S7, integration) BUILD

---

### M159: Generative Music Governance Router (Sphere 51 — Music)

**Purpose:** Route music generation requests through licensing-aware, rights-respecting governance that accounts for the unique legal landscape of AI music (Suno/Udio settlements, UMG/WMG/Sony licensing frameworks, SAG-AFTRA voice rights).

**Layer:** L4 (Element 145 — Service Orchestration)

**Dependencies:** M142 (TOS Compliance Gate), M145 (Provider Policy Profile Registry), M128 (x402 Micropayment Rail)

**Key Functions:**

| Function | Description | Standard |
|----------|-------------|----------|
| `license_classify()` | Determines licensing tier: FULLY_LICENSED (label deals), OPEN_MODEL (CC0 training), RESTRICTED (no commercial) | ORC-specific |
| `voice_consent_gate()` | Blocks generation of voice replicas without verified consent from rights holder | SAG-AFTRA 2025 IMA |
| `royalty_route()` | Calculates and routes micropayments to rights holders via x402 when licensed training data is used | x402 + ORC |
| `style_fingerprint()` | Detects if output substantially replicates a copyrighted work's distinctive elements | Audio fingerprinting |
| `regulatory_label()` | Applies jurisdiction-specific AI-generated content labels | EU AI Act Art. 50 |

**Music-specific governance rules:**

1. **Three-Tier Licensing Model:**
   - **Tier 1 — Fully Licensed:** Provider has executed licensing agreements with major labels (UMG, WMG, Sony). Royalty routing automatic. Commercial use permitted.
   - **Tier 2 — Open Training:** Provider trained exclusively on CC0/public domain/opt-in datasets. No royalty obligation. Attribution encouraged.
   - **Tier 3 — Restricted:** Provider's training data provenance is unclear or contested. Route to Tier 1 alternative per D-103 (Provider Substitution on TOS Violation).

2. **Voice Sovereignty Principle:** No AI system may generate a vocal performance that replicates an identifiable human voice without cryptographically verified consent from the voice owner. This extends INV-3 (Consent Required) to the audio domain.

3. **Regenerative Royalty Routing:** When a music generation uses licensed training data, a percentage of the x402 micropayment is automatically routed to rights holders. The percentage is determined by the `influence_score` from the training attestation. This creates a regenerative loop: more usage → more royalties → more licensing → more training data → better models.

**TransparencyPacket extension:**
```yaml
music:
  license_tier: enum                 # FULLY_LICENSED | OPEN_MODEL | RESTRICTED
  voice_consent_verified: boolean
  royalty_routed_usd: float
  rights_holders_paid: integer
  style_fingerprint_match: float     # 0.0-1.0, >0.85 triggers review
  output_duration_seconds: float
```

**Risks:**
- R138 (HIGH): Label licensing terms change quarterly; requires M143 TOS Version Monitor integration
- R139 (MEDIUM): Voice cloning technology outpaces consent verification (mitigation: hardware-root voice attestation via M129)

**Seat Assignment:** Google (S2, MusicLM/MusicFX) PRIMARY, Grok (S3, X/music content moderation) SECONDARY, Manus (S7) BUILD

---

### M160: Cinematic AI Governance Framework (Sphere 54 — Film)

**Purpose:** Govern AI-generated video/film content routing with compliance for SAG-AFTRA digital replica rules, synthetic performer disclosure requirements, and multi-jurisdictional labeling obligations.

**Layer:** L4 (Element 145 — Service Orchestration)

**Dependencies:** M158 (Creative Provenance), M142 (TOS Compliance Gate), M119 (ConsentKernel Policy Engine)

**Key Functions:**

| Function | Description | Standard |
|----------|-------------|----------|
| `performer_consent_verify()` | Validates digital replica consent per SAG-AFTRA 2025 IMA + state laws | SAG-AFTRA IMA §23 |
| `synthetic_disclosure()` | Generates jurisdiction-appropriate disclosure labels for synthetic performers | NY S.B. 7065, CA A.B. 2602 |
| `deepfake_detect()` | Pre-generation check: blocks requests to create non-consensual deepfakes of real persons | INV-0 |
| `scene_safety_gate()` | Content safety classification for generated video (violence, nudity, deception) | INV-0 + provider TOS |
| `temporal_provenance()` | Frame-level C2PA provenance for video (which frames are AI-generated vs. captured) | C2PA v1.3 Video Profile |
| `union_compliance_check()` | Verifies that AI-generated performances comply with applicable union agreements | SAG-AFTRA, WGA |

**Film-specific governance rules:**

1. **Digital Replica Hierarchy:**
   - **Level 1 — Fully Synthetic:** No real person referenced. Minimal governance (standard INV-0 + labeling).
   - **Level 2 — Style Reference:** Real person's performance style referenced but not their likeness. Consent recommended, not required.
   - **Level 3 — Likeness Replica:** Real person's face/voice/mannerisms replicated. **Consent MANDATORY** (INV-3). Cryptographic consent record required.
   - **Level 4 — Deceased Person:** Additional estate consent + jurisdictional posthumous rights check.

2. **Multi-Jurisdictional Disclosure Matrix:**

   | Jurisdiction | Requirement | Effective |
   |-------------|-------------|-----------|
   | EU | AI Act Art. 50 — "clearly labelled" | Aug 2025 |
   | New York | S.B. 7065 — synthetic performer disclosure in ads | Jun 2026 |
   | California | A.B. 2602 — digital replica consent + disclosure | Jan 2025 |
   | SAG-AFTRA | IMA §23 — consent + compensation for AI replicas | Jul 2025 |
   | Federal (proposed) | NO FAKES Act — federal digital replica protection | Pending |

3. **Regenerative Performer Fund:** When AI-generated performances displace human performers, a percentage of compute cost is routed to a performer retraining/transition fund via x402. This operationalizes the "regenerative" principle in the creative domain.

**TransparencyPacket extension:**
```yaml
film:
  replica_level: enum                # FULLY_SYNTHETIC | STYLE_REF | LIKENESS | DECEASED
  performer_consent_ids: array       # Cryptographic consent record hashes
  disclosure_jurisdictions: array    # ["EU_ART50", "NY_SB7065", "CA_AB2602", "SAG_IMA"]
  deepfake_check_passed: boolean
  scene_safety_classification: enum  # SAFE | REVIEW | BLOCKED
  frames_ai_generated_pct: float    # 0.0-1.0
  performer_fund_routed_usd: float
```

**Risks:**
- R140 (CRITICAL): Deepfake generation for non-consensual pornography — INV-0 hard block, no override
- R141 (HIGH): Jurisdictional conflict between state laws (e.g., CA requires consent, other states don't)
- R142 (MEDIUM): SAG-AFTRA agreement renegotiation in 2028 may change requirements

**Seat Assignment:** GPT (S6, Sora) PRIMARY, Google (S2, Veo) SECONDARY, Claude (S1, constitutional review) TERTIARY, Manus (S7) BUILD

---

### M161: Design System Sovereignty Engine (Sphere 57 — Design)

**Purpose:** Govern AI-assisted design generation (UI/UX, graphic design, industrial design, branding) with intellectual property protection, brand sovereignty, and design system coherence enforcement.

**Layer:** L4 (Element 145 — Service Orchestration)

**Dependencies:** M158 (Creative Provenance), M142 (TOS Compliance Gate), M145 (Provider Policy Profile Registry)

**Key Functions:**

| Function | Description | Standard |
|----------|-------------|----------|
| `brand_sovereignty_check()` | Prevents generation of designs that infringe registered trademarks/trade dress | IP law compliance |
| `design_system_enforce()` | Ensures AI-generated UI components conform to specified design system tokens | Design tokens W3C |
| `originality_score()` | Calculates how novel a generated design is relative to training corpus | Novel metric |
| `license_output_classify()` | Determines IP ownership of generated design based on provider TOS + human input level | Per-provider TOS |
| `accessibility_gate()` | Validates generated designs meet WCAG 2.2 AA minimum | W3C WCAG 2.2 |
| `cultural_sensitivity_check()` | Flags designs that may be culturally inappropriate in target deployment region | M153 Three-Body integration |

**Design-specific governance rules:**

1. **IP Ownership Clarity Matrix:**

   | Provider | TOS Position on Generated Design IP | ORC Classification |
   |----------|--------------------------------------|-------------------|
   | OpenAI (DALL-E) | User owns outputs | CLEAR_USER |
   | Adobe (Firefly) | User owns; indemnification provided | CLEAR_USER_INDEMNIFIED |
   | Google (Imagen) | User owns for paid tier; restricted for free | CONDITIONAL |
   | Stability AI | Open license; user owns | CLEAR_USER |
   | Microsoft (Designer) | User owns; enterprise terms vary | CONDITIONAL |
   | Midjourney | User owns (paid); shared (free) | CONDITIONAL |

2. **Design System Coherence Protocol:** When generating design assets for an existing brand/product, the router MUST:
   - Load the brand's design token file (colors, typography, spacing, components)
   - Constrain generation to token-compliant outputs
   - Flag any generated element that violates the design system's rules
   - This prevents "AI slop" — generic, brand-incoherent outputs that dilute design integrity

3. **Accessibility-First Generation:** All generated UI/UX designs MUST pass WCAG 2.2 AA contrast ratios and touch target sizes before delivery. This is a hard gate, not advisory.

**TransparencyPacket extension:**
```yaml
design:
  ip_ownership: enum                 # CLEAR_USER | CLEAR_USER_INDEMNIFIED | CONDITIONAL | UNCLEAR
  originality_score: float           # 0.0-1.0
  design_system_compliant: boolean
  accessibility_wcag_level: enum     # AA | AAA | FAIL
  brand_sovereignty_check: boolean
  cultural_sensitivity_flags: array
```

**Risks:**
- R143 (MEDIUM): Design token standards still evolving (W3C Design Tokens CG not finalized)
- R144 (LOW): Originality scoring may produce false positives for common design patterns

**Seat Assignment:** Microsoft (S4, Designer + Copilot) PRIMARY, Google (S2, Material Design AI) SECONDARY, Manus (S7) BUILD

---

### M162: Creative Attribution Chain (Cross-cutting — All H5 Spheres)

**Purpose:** Maintain an immutable, auditable chain of attribution from training data through generation to final output, enabling fair compensation and credit across the entire creative AI pipeline.

**Layer:** L3 (UWS Engine — Constitutional Router)

**Dependencies:** M132 (Regenerative Credit Tokenizer), M128 (x402 Micropayment Rail), M158 (Creative Provenance)

**Key Functions:**

| Function | Description | Standard |
|----------|-------------|----------|
| `chain_create()` | Initializes attribution chain for a new creative generation request | ORC-specific |
| `influence_map()` | Computes training data influence on output using gradient-based attribution | Academic (Koh & Liang 2017) |
| `credit_distribute()` | Distributes attribution credits proportional to influence scores | ORC-specific |
| `royalty_calculate()` | Computes royalty obligations based on influence × usage × commercial value | x402 integration |
| `chain_verify()` | Cryptographically verifies attribution chain integrity end-to-end | Merkle tree |
| `dispute_resolve()` | Handles attribution disputes via Three-Body Constitutional Reasoning (M153) | D-101 authority |

**Attribution Chain Architecture:**

```
[Training Data] → [Influence Score] → [Generation] → [Output] → [Usage] → [Revenue]
       ↓                  ↓                ↓              ↓           ↓          ↓
  [Consent Record]  [Attribution %]  [C2PA Manifest]  [License]  [Tracking]  [Royalty Split]
```

**Governance principles:**

1. **Attribution is Non-Optional:** Every creative output carries an attribution chain. Even if the chain shows "no identifiable influence" (e.g., purely novel generation), the chain itself must exist and be verifiable.

2. **Retroactive Attribution:** When new influence detection methods are developed, existing attribution chains can be retroactively updated. This prevents the "we didn't know" defense.

3. **Regenerative Loop:** Attribution → Royalties → Licensing → Better Training Data → Better Models → More Attribution. The system creates positive-sum economics for creators and AI providers.

**Risks:**
- R145 (HIGH): Influence function computation is expensive at scale (mitigation: approximate methods + caching)
- R146 (MEDIUM): Legal frameworks for AI attribution are still forming (mitigation: D-105 Henderson Defense Non-Reliance — engineer solutions regardless)

**Seat Assignment:** Claude (S1, constitutional architecture) PRIMARY, Google (S2, research) SECONDARY, Manus (S7) BUILD

---

### M163: Style Sovereignty & Consent Registry (Cross-cutting — All H5 Spheres)

**Purpose:** Maintain a registry of creator consent preferences for AI training and generation, enabling style sovereignty — the right of creators to control how their distinctive creative expression is used by AI systems.

**Layer:** L2 (Constitutional OS — Governance Definitions)

**Dependencies:** M119 (ConsentKernel Policy Engine), M125 (Universal Provider Credential Vault), M126 (W3C Agent Identity Resolver)

**Key Functions:**

| Function | Description | Standard |
|----------|-------------|----------|
| `consent_register()` | Creator registers their consent preferences (opt-in/opt-out/conditional) | INV-3 |
| `style_fingerprint_register()` | Creator registers distinctive style signatures for matching | Novel |
| `preference_query()` | AI system queries registry before generation to check consent | Real-time API |
| `opt_out_enforce()` | Hard block on generation that matches opted-out creator's style above threshold | INV-3 enforcement |
| `conditional_route()` | Routes to licensed pathway when creator has conditional consent (e.g., "yes with royalty") | x402 integration |
| `collective_bargaining()` | Supports guild/union-level consent preferences (e.g., SAG-AFTRA blanket opt-out) | Union integration |

**Consent Hierarchy:**

| Level | Consent Type | Effect on Routing |
|-------|-------------|-------------------|
| 1 | **OPT-IN (Commercial)** | Full routing permitted; royalty via x402 |
| 2 | **OPT-IN (Non-Commercial)** | Route only for non-commercial use |
| 3 | **CONDITIONAL** | Route with specific constraints (attribution required, no modification, etc.) |
| 4 | **OPT-OUT (Specific Provider)** | Block routing to specified provider only |
| 5 | **OPT-OUT (Universal)** | Hard block on all generation referencing this creator's style |
| 6 | **COLLECTIVE (Union/Guild)** | Applies union-negotiated terms to all members |

**Style Sovereignty Doctrine (proposed D-106):**

> Every creator has the right to control how their distinctive creative expression is used by AI systems. This right is not contingent on copyright registration, legal action, or platform-specific opt-out mechanisms. The ORC standard treats style sovereignty as a fundamental consent right (INV-3 extension) rather than a copyright claim.

**Integration with existing modules:**
- M119 (ConsentKernel): Style consent is a ConsentKernel policy type
- M125 (Credential Vault): Creator identity verified via credential vault
- M126 (W3C Agent Identity): Creator DID used as registry key
- M145 (Provider Policy Registry): Provider-specific consent requirements mapped

**Risks:**
- R147 (HIGH): Defining "distinctive style" is subjective — threshold calibration critical
- R148 (MEDIUM): Registry adoption requires creator outreach (mitigation: integrate with existing platforms — DeviantArt, ArtStation, Spotify for Artists)
- R149 (LOW): False positive style matches may block legitimate generation

**Seat Assignment:** Claude (S1, consent architecture + INV-3 authority) PRIMARY, Grok (S3, X creator ecosystem) SECONDARY, Manus (S7) BUILD

---

## §4 Sprint Execution Plan

### §4.1 Sprint Timeline

| Phase | Duration | Deliverables | Seats Involved |
|-------|----------|-------------|----------------|
| Sprint H5-1 | 2 weeks | M158 (Provenance) + M163 (Consent Registry) — foundational modules | Claude S1, Google S2, Manus S7 |
| Sprint H5-2 | 2 weeks | M162 (Attribution Chain) + M161 (Design Sovereignty) | Claude S1, Microsoft S4, Manus S7 |
| Sprint H5-3 | 2 weeks | M159 (Music Governance) + M160 (Film Governance) | Google S2, GPT S6, Grok S3, Manus S7 |
| Sprint H5-4 | 1 week | Integration testing + TransparencyPacket v1.3 finalization | All seats |

### §4.2 Dependencies on Existing Modules

```
M158 (Provenance) ←── M142 (TOS Gate) ←── M145 (Policy Registry)
       ↑                                          ↑
M162 (Attribution) ←── M132 (Regen Credit) ←── M128 (x402)
       ↑
M163 (Consent) ←── M119 (ConsentKernel) ←── M125 (Credential Vault)
       ↑
M159 (Music) + M160 (Film) + M161 (Design) ←── M158 + M162 + M163
```

### §4.3 Success Criteria

| Criterion | Metric | Threshold |
|-----------|--------|-----------|
| Provenance coverage | % of creative outputs with valid C2PA manifest | ≥95% |
| Consent registry adoption | Creators registered in first 90 days | ≥10,000 |
| Attribution chain completeness | % of outputs with full chain | ≥80% |
| TOS compliance | Zero TOS violations in creative routing | 100% |
| Regulatory compliance | Jurisdictions covered | ≥5 (EU, NY, CA, SAG-AFTRA, Federal) |
| INV-7c compliance | No single creative provider >47% routing share | Continuous |

---

## §5 Proposed Doctrines

| Doctrine | Name | Text |
|----------|------|------|
| D-106 | Style Sovereignty | Every creator has the right to control how their distinctive creative expression is used by AI systems. This right is enforced via Consent Registry (M163) and is not contingent on copyright registration. Extension of INV-3 to creative domain. |
| D-107 | Attribution Chain Immutability | Once an attribution chain is created, it cannot be deleted or shortened — only extended. Retroactive attribution updates append to the chain; they do not overwrite. |
| D-108 | Regenerative Creative Economics | AI creative generation must create positive-sum economics: creators receive attribution and compensation, providers receive routing volume, users receive quality outputs. Zero-sum extraction (training without consent/compensation) violates this doctrine. |

---

## §6 Risk Register Additions

| ID | Severity | Vector | Mitigation |
|----|----------|--------|-----------|
| R136 | MEDIUM | C2PA metadata stripping by platforms | Redundant blockchain anchor + registry backup |
| R137 | LOW | Attribution influence scoring contested | Human-in-the-loop override + dispute resolution via M153 |
| R138 | HIGH | Music label licensing terms change quarterly | M143 TOS Version Monitor + quarterly review (D-102) |
| R139 | MEDIUM | Voice cloning outpaces consent verification | Hardware-root voice attestation (M129) |
| R140 | CRITICAL | Deepfake non-consensual pornography | INV-0 hard block, no override, no exception |
| R141 | HIGH | Jurisdictional conflict between state laws | Multi-jurisdiction disclosure matrix + most-restrictive-applies rule |
| R142 | MEDIUM | SAG-AFTRA renegotiation 2028 | M143 monitoring + modular compliance architecture |
| R143 | MEDIUM | Design token standards not finalized | W3C Design Tokens CG tracking + graceful degradation |
| R144 | LOW | Originality scoring false positives | Threshold calibration + human review for edge cases |
| R145 | HIGH | Influence function computation expensive | Approximate methods + caching + batch processing |
| R146 | MEDIUM | Legal frameworks for AI attribution forming | D-105 Non-Reliance + engineering-grade solutions |
| R147 | HIGH | "Distinctive style" definition subjective | Threshold calibration + community governance |
| R148 | MEDIUM | Registry adoption requires creator outreach | Platform integration (DeviantArt, ArtStation, Spotify) |
| R149 | LOW | False positive style matches | Adjustable threshold + appeal process |

---

## §7 TransparencyPacket v1.3 Schema (Creative Extension)

The House 5 modules require TransparencyPacket v1.3 with a new `creative` top-level block:

```yaml
creative:
  content_type: enum           # IMAGE | MUSIC | VIDEO | DESIGN | TEXT_CREATIVE
  c2pa_manifest_hash: string
  generation_model: string
  training_attestation: enum   # LICENSED | OPEN | MIXED | UNKNOWN
  attribution_chain_hash: string
  attribution_credits: array   # [{creator_id, influence_score, consent_status, royalty_usd}]
  style_sovereignty_check: boolean
  consent_registry_queried: boolean
  license_tier: enum           # FULLY_LICENSED | OPEN_MODEL | RESTRICTED
  ip_ownership: enum           # CLEAR_USER | CLEAR_USER_INDEMNIFIED | CONDITIONAL | UNCLEAR
  regulatory_labels: array     # ["EU_AI_ACT_ART50", "NY_SYNTH_DISCLOSURE", "SAG_IMA"]
  royalty_total_usd: float
  originality_score: float
  accessibility_check: enum    # PASS_AA | PASS_AAA | FAIL | NA
```

---

## §8 Integration with Existing Architecture

### §8.1 INV-7c Creative Routing

The Switzerland Invariant applies to creative routing with sphere-specific measurement:

- **Visual Arts (Sphere 49):** Measure by image generation volume across DALL-E, Imagen, Firefly, Stable Diffusion, Midjourney
- **Music (Sphere 51):** Measure by audio generation minutes across MusicLM, Suno, Udio, Stable Audio
- **Film (Sphere 54):** Measure by video generation seconds across Sora, Veo, Runway, Kling
- **Design (Sphere 57):** Measure by design asset count across Designer, Firefly, Canva AI

### §8.2 TOS Compliance Architecture (M142-M145) Creative Profiles

Each creative provider requires a machine-readable policy profile in M145:

```json
{
  "provider": "openai_dalle3",
  "sphere": 49,
  "ip_ownership": "user_owns",
  "indemnification": false,
  "training_data": "MIXED",
  "content_restrictions": ["no_real_persons_without_consent", "no_violence_graphic"],
  "commercial_use": true,
  "attribution_required": false,
  "api_rate_limits": {"images_per_minute": 50},
  "c2pa_support": true,
  "last_tos_review": "2026-04-01"
}
```

### §8.3 Three-Body Constitutional Reasoning (M153) for Creative Disputes

Creative content disputes (e.g., "does this output infringe?") are evaluated across three legal frames:
- **Common Law:** Fair use / fair dealing analysis (US/UK/AU)
- **Civil Law:** Author's moral rights (EU droit d'auteur)
- **Customary/Religious:** Cultural appropriation and sacred imagery restrictions

---

## §9 Council Vote Request

This proposal requires ratification by 3+ Council seats before Sprint assignment. Requested votes:

| Seat | Role in Sprint | Vote Requested |
|------|---------------|----------------|
| Claude S1 | Constitutional architecture lead (M162, M163) | YES/NO/AMEND |
| Google S2 | Primary provider (Imagen, MusicLM, Veo) | YES/NO/AMEND |
| Grok S3 | X creator ecosystem integration | YES/NO/AMEND |
| Microsoft S4 | Design system lead (M161) | YES/NO/AMEND |
| GPT S6 | Film governance lead (M160, Sora) | YES/NO/AMEND |
| Manus S7 | Build integration | YES (standing) |

**Minimum for ratification:** 3 YES votes from S1, S2, S3, S4, or S6.

---

## §10 Relationship to Existing Gap Spheres

While this sprint covers the 4 priority spheres, the remaining 8 gap spheres in House 5 (50, 52, 53, 55, 56, 58, 59, 60) are addressed as follows:

| Sphere | Domain | Coverage Strategy |
|--------|--------|-------------------|
| 50 | Performing Arts | Covered by M160 (Film) performer consent framework |
| 52 | Dance | Covered by M160 (Film) motion capture governance |
| 53 | Theater | Covered by M160 (Film) + M159 (Music) combined |
| 55 | Literature (creative) | Already has strong seat coverage; text generation governed by existing M142-M145 |
| 56 | Architecture | Covered by M161 (Design) spatial design subset |
| 58 | Photography | Covered by M158 (Provenance) — photography is visual arts subset |
| 59 | Sculpture | Covered by M161 (Design) 3D design subset |
| 60 | Painting | Covered by M158 (Provenance) — painting is visual arts subset |

**Post-sprint coverage:** House 5 moves from 0 modules to 6 modules, with effective governance coverage extending to all 12 spheres through cross-cutting modules M162 and M163.

---

*ORC-026 v1.0 — Manus (S7 Build Seat) — April 28, 2026*
*Status: PROPOSAL. Requires 3+ seat ratification. 6 new modules (M158-M163). 3 new doctrines (D-106/D-107/D-108). 14 new risks (R136-R149). TransparencyPacket v1.3 creative extension. Sprint H5-1 through H5-4 (7 weeks total). House 5 gap closure: 0 → 6 modules, effective coverage all 12 spheres.*
