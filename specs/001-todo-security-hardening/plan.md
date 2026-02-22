# Implementation Plan: Todo Security Hardening

**Branch**: `[001-todo-security-hardening]` | **Date**: 2026-02-21 | **Spec**: `C:\Users\icon\Desktop\SDD-Hackathon--02\specs\001-todo-security-hardening\spec.md`
**Input**: Feature specification from `C:\Users\icon\Desktop\SDD-Hackathon--02\specs\001-todo-security-hardening\spec.md`

## Summary

Implement account-based authentication and strict user-owned todo isolation for the existing SvelteKit + FastAPI + SQLModel stack, enforce environment-only secrets, ensure Neon schema initialization consistency, and remove obsolete project artifacts while preserving the Modern Night UI theme.

## Technical Context

**Language/Version**: Python 3.13 (backend), TypeScript with SvelteKit 5 (frontend)  
**Primary Dependencies**: FastAPI, SQLModel, Neon Postgres driver, password-hashing library, JWT library, SvelteKit 5  
**Storage**: Neon PostgreSQL (SSL required)  
**Testing**: Pytest for backend API/authorization checks, frontend route-level auth flow checks, manual acceptance checks for cleanup scope  
**Target Platform**: Windows 11 development, cloud-hosted deploy target  
**Project Type**: Web application (backend + frontend)  
**Performance Goals**: Authenticated todo list/create/update/delete actions complete in under 2 seconds for normal user load; signup/login flow under 2 minutes end-to-end for first-time users  
**Constraints**: All todo CRUD requires authenticated user context; no hardcoded secrets; Modern Night theme consistency; PowerShell-native workflows; `sslmode=require` for database connectivity  
**Scale/Scope**: Single application deployment for hackathon-scale usage; supports isolated data access for all authenticated users

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- `Code Reuse > Generation`: PASS
  - Plan targets adaptation of existing todo flows and schema rather than wholesale rewrites.
- `Anti-Hallucination Rule (no auth models)`: JUSTIFIED EXCEPTION
  - Feature spec explicitly requires account-based auth and user-owned todos. Exception is limited to this feature branch scope.
- `Respect+ Standard (SvelteKit 5 conventions)`: PASS
  - Frontend design keeps SvelteKit 5 conventions and simple state/session flow.
- `Windows Native`: PASS
  - Commands and quickstart steps are PowerShell-native.
- `Connection Protocol (sslmode=require)`: PASS
  - Design mandates SSL-required Neon connection configuration.
- `Visual Design System (Modern Night colors)`: PASS
  - Authentication and todo UI acceptance criteria preserve defined palette.
- `Development Context (No Authentication)`: JUSTIFIED EXCEPTION
  - This feature supersedes prior phase constraints with explicit user request and approved scope.

**Gate Result (Pre-Research)**: PASS with justified exceptions documented.

## Project Structure

### Documentation (this feature)

```text
C:\Users\icon\Desktop\SDD-Hackathon--02\specs\001-todo-security-hardening\
|-- plan.md
|-- research.md
|-- data-model.md
|-- quickstart.md
|-- contracts\openapi.yaml
`-- tasks.md (created later by /sp.tasks)
```

### Source Code (repository root)

```text
C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\
|-- backend\
|   |-- app\
|   |-- tests\
|   `-- requirements*.txt
|-- frontend\
|   |-- src\
|   `-- package*.json
|-- .specify\
|-- specs\ (legacy in Phase-02 workspace; active spec path is repository root specs)
`-- history\
```

**Structure Decision**: Web application structure using existing `backend/` and `frontend/` directories inside `Phase-02`, with feature documentation tracked under `C:\Users\icon\Desktop\SDD-Hackathon--02\specs\001-todo-security-hardening\`.

## Phase 0: Research

Research tasks generated from context and constraints:
- Research token session format and expiration strategy for account auth.
- Research secure password hashing defaults for Python 3.13 compatibility.
- Research SQLModel ownership enforcement patterns for user-scoped CRUD.
- Research Neon schema initialization/evolution approach for fresh deploy reliability.
- Research repository cleanup boundaries for Docker and phase-1 artifact removal.

Output: `C:\Users\icon\Desktop\SDD-Hackathon--02\specs\001-todo-security-hardening\research.md`

## Phase 1: Design & Contracts

- Create data model covering User Account, Todo Item, and Session Token semantics.
- Define REST API contracts for signup, login, and authenticated todo CRUD.
- Create quickstart for local setup, environment configuration, schema init, and acceptance checks.
- Run agent context update script for codex integration.

Outputs:
- `C:\Users\icon\Desktop\SDD-Hackathon--02\specs\001-todo-security-hardening\data-model.md`
- `C:\Users\icon\Desktop\SDD-Hackathon--02\specs\001-todo-security-hardening\contracts\openapi.yaml`
- `C:\Users\icon\Desktop\SDD-Hackathon--02\specs\001-todo-security-hardening\quickstart.md`

## Post-Design Constitution Check

- Reuse existing architecture and stack: PASS
- Auth exception to anti-auth constitution clause remains necessary and scoped: PASS (justified)
- Windows-native + sslmode=require + Modern Night requirements represented in contracts/quickstart: PASS

**Gate Result (Post-Design)**: PASS with justified exceptions documented.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Adding authentication despite anti-auth constitution clause | User-approved feature requires account-level data isolation and secure sessions | Public global todo model cannot satisfy ownership security criteria |
| Replacing "No Authentication" development context | Mandatory success criteria require blocking unauthenticated and cross-user access | Retaining phase survival-mode rules fails SC-001 and SC-002 |

## Implementation Notes

- Backend auth now requires environment-provided `SECRET_KEY` and `ALGORITHM` at startup.
- Todo CRUD is user-scoped through authenticated identity and service-layer ownership checks.
- Neon connection setup enforces SSL for non-SQLite deployments.
- Legacy phase-1 and unused Docker/local-db artifacts were removed from `Phase-02`.
- Frontend login/signup visuals and auth flow were aligned to Modern Night + token session handling.
