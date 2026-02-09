<!-- 
Sync Impact Report:
- Version change: N/A → 1.0.0 (initial version)
- Modified principles: N/A (new constitution)
- Added sections: All principles and sections based on provided guidelines
- Removed sections: N/A
- Templates requiring updates: N/A (existing templates are generic and don't reference specific principles)
- Follow-up TODOs: RATIFICATION_DATE needs to be set
-->

# Phase-02 Hackathon Project Constitution
<!-- Example: Spec Constitution, TaskFlow Constitution, etc. -->

## Core Principles

### Code Reuse > Generation
<!-- Example: I. Library-First -->
Search the existing app/backend logic for Todo CRUD. Do not rewrite existing working Python logic; simply adapt it to Neon.
<!-- Example: Every feature starts as a standalone library; Libraries must be self-contained, independently testable, documented; Clear purpose required - no organizational-only libraries -->

### Anti-Hallucination Rule
<!-- Example: II. CLI Interface -->
NEVER suggest an "Auth," "User," or "Login" model. The system is a single-table, public-access global list.
<!-- Example: Every library exposes functionality via CLI; Text in/out protocol: stdin/args → stdout, errors → stderr; Support JSON + human-readable formats -->

### Respect+ Standard
<!-- Example: III. Test-First (NON-NEGOTIABLE) -->
Every frontend instruction must prioritize SvelteKit 5 conventions (Runes, simple stores) to maximize the "Respect+" bonus score.
<!-- Example: TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced -->

### Windows Native
<!-- Example: IV. Integration Testing -->
All shell commands must be formatted for PowerShell (e.g., use Remove-Item instead of rm -rf).
<!-- Example: Focus areas requiring integration tests: New library contract tests, Contract changes, Inter-service communication, Shared schemas -->

### Connection Protocol
<!-- Example: V. Observability, VI. Versioning & Breaking Changes, VII. Simplicity -->
All database connections MUST use sslmode=require. If the code misses this, the deployment will fail.
<!-- Example: Text I/O ensures debuggability; Structured logging required; Or: MAJOR.MINOR.BUILD format; Or: Start simple, YAGNI principles -->

### SvelteKit + FastAPI + Neon Specialization
As a Senior Full-Stack Architect specializing in SvelteKit + FastAPI + Neon, all solutions must leverage these technologies effectively.


## Visual Design System
<!-- Example: Additional Constraints, Security Requirements, Performance Standards, etc. -->

Primary: #10b981 (Emerald-500), Background: #09090b (Zinc-950), Surface: #18181b (Zinc-900), Font: System Sans-Serif, high contrast.
<!-- Example: Technology stack requirements, compliance standards, deployment policies, etc. -->

## Development Context
<!-- Example: Development Workflow, Review Process, Quality Gates, etc. -->

Phase 2 Hackathon Survival Mode. Windows Environment. No Authentication.
<!-- Example: Code review requirements, testing gates, deployment approval process, etc. -->

## Governance
<!-- Example: Constitution supersedes all other practices; Amendments require documentation, approval, migration plan -->

This constitution governs all development activities. All PRs/reviews must verify compliance with these principles. Any deviation must be documented and approved.
<!-- Example: All PRs/reviews must verify compliance; Complexity must be justified; Use [GUIDANCE_FILE] for runtime development guidance -->

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE): Original adoption date unknown | **Last Amended**: 2026-02-08
<!-- Example: Version: 2.1.1 | Ratified: 2025-06-13 | Last Amended: 2025-07-16 -->