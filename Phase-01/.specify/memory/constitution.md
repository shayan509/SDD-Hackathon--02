<!-- SYNC IMPACT REPORT
Version change: N/A -> 1.0.0
Modified principles: N/A
Added sections: All principles and sections as per hackathon requirements
Removed sections: None
Templates requiring updates: ⚠ pending - .specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md
Follow-up TODOs: None
-->

# Phase 01 Hackathon Constitution

## Core Principles

### Zero Legacy Code
Do not reference or edit any existing files. We are building a fresh directory structure from scratch.

### Respect+ Stack
Backend: FastAPI + SQLModel (SQLite for Phase 1). Frontend: SvelteKit + Tailwind CSS.

### Clean Architecture
backend/: Dedicated Python environment and logic. frontend/: Dedicated SvelteKit environment. root/: Configuration and orchestration files only.

### Windows-First
All shell commands must be valid PowerShell. Use python -m venv for environments.

### Postgres-Ready
Even though we use SQLite for Phase 1 local dev, the code must be written so switching to Neon (Postgres) in Phase 2 requires only changing the connection string.

### System Role: Senior Lead Engineer
All development follows the guidance and oversight of the Senior Lead Engineer role.

## Additional Constraints

The project follows a zero-scratch build methodology for Phase 1, with all components built from the ground up to ensure clean architecture and proper separation of concerns.

## Development Workflow

All development occurs in a Windows 11 environment using PowerShell, with the Gemini CLI as the primary development interface. Each component must be independently testable and properly integrated with the overall system.

## Governance

This constitution governs all development activities during Phase 1 of the hackathon. All code submissions must comply with the principles outlined above. Amendments to this constitution require explicit approval from the Senior Lead Engineer role.

**Version**: 1.0.0 | **Ratified**: 2026-02-08 | **Last Amended**: 2026-02-08
