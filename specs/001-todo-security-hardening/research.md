# Phase 0 Research: Todo Security Hardening

## Decision 1: Session Model
- Decision: Use signed, time-bound bearer tokens for authenticated sessions, with short access lifetime and forced re-login after expiry.
- Rationale: Meets requirement for token-based sessions and enables stateless API authorization checks.
- Alternatives considered: Server-side session store (more operational state), long-lived non-expiring tokens (higher compromise risk).

## Decision 2: Password Security
- Decision: Use adaptive one-way password hashing with per-password salt and constant-time verification.
- Rationale: Satisfies secure password handling and prevents plaintext/password-replay storage risks.
- Alternatives considered: Unsalted hashes (insufficient), reversible encryption (violates least exposure).

## Decision 3: Ownership Enforcement
- Decision: Enforce ownership at query and mutation boundaries by binding every todo operation to authenticated user identity.
- Rationale: Directly satisfies user isolation criteria and prevents horizontal privilege escalation.
- Alternatives considered: Client-side filtering only (bypassable), shared global todo table without owner checks (violates requirements).

## Decision 4: Schema Initialization and Evolution
- Decision: Maintain explicit startup schema initialization path for fresh environments and versioned evolution steps for non-fresh environments.
- Rationale: Ensures deploy consistency while supporting controlled future schema changes in Neon.
- Alternatives considered: Manual ad-hoc schema creation (error-prone), implicit runtime schema assumptions (unreliable on fresh deploys).

## Decision 5: Secret Management
- Decision: Require all cryptographic/session secrets via environment variables and fail startup when missing.
- Rationale: Prevents hardcoded key leakage and enforces deploy-time secret hygiene.
- Alternatives considered: Default fallback hardcoded secrets (unsafe), optional secret loading with weak defaults (compliance risk).

## Decision 6: Repository Cleanup Scope
- Decision: Remove unused Docker and phase-1 boilerplate artifacts that are not required by active backend/frontend runtime.
- Rationale: Improves maintainability and reduces confusion around supported deployment paths.
- Alternatives considered: Keep all historical files (maintenance noise), partial cleanup without inventory (inconsistent results).

## Clarification Resolution Summary
- All prior unknowns are resolved by the above decisions.
- No remaining `NEEDS CLARIFICATION` items.