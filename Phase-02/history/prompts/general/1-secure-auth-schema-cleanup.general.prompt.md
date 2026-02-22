---
id: 1
title: "secure-auth-schema-cleanup"
stage: general
date_iso: "2026-02-20"
surface: agent
model: "GPT-5 Codex"
feature: "none"
branch: null
user: "icon"
command: "Secure auth, schema evolution & cleanup"
labels: ["general", "auth", "schema", "cleanup", "fastapi", "sveltekit"]
spec: null
ticket: null
adr: null
pr: null
outcome: "Updated backend models and auth utils for UUID users/JWT env config, added optional schema reset on startup, and refreshed backend .env.example."
evaluation: "No automated tests run."
files_yaml:
  - "backend/models/todo.py"
  - "backend/auth_utils.py"
  - "backend/main.py"
  - "backend/.env.example"
tests_yaml:
  - "not run"
---

## Prompt

[SPECIFICATION PROMPT: SECURE AUTH, SCHEMA EVOLUTION & SYSTEM CLEANUP][ROLE]: Senior Full-Stack Architect & Security Engineer.

[CONTEXT]:
Upgrading a Phase 2/3 Todo Application (SvelteKit + FastAPI + SQLModel + Neon) to a secure, professional state. The project runs on Windows 11 with Python 3.13.

[TECH SPECIFICATION: BACKEND]:

Dependencies: Update requirements.txt to include python-jose[cryptography], python-multipart, and passlib[bcrypt]>=1.7.4 (mandatory for Python 3.13 compatibility).

Models:

Define a User table (UUID primary key, unique username, hashed_password).

Add user_id: UUID as a ForeignKey to the Todo table.

Auth Logic:

Implement JWT utilities: verify_password, get_password_hash, and create_access_token.

Protected Routes: All /todo CRUD operations must use a get_current_user dependency to ensure users only access their own data.

Database Migration:

In main.py, include a one-time "reset" logic: SQLModel.metadata.drop_all(engine) followed by create_all(engine) to synchronize the Neon schema with the new relationships.

[TECH SPECIFICATION: FRONTEND]:

Auth Routing: Create SvelteKit routes for /login and /signup.

State Management: Use Svelte 5 Runes ($state) to manage the user session and save the JWT to localStorage.

API Integration: Implement a global fetch wrapper/interceptor that automatically injects the Authorization: Bearer <token> header into every request.

UI/UX: Strictly apply a "Modern Night" theme: Background #09090b, Primary Emerald #10b981, and high-contrast text.

[ENVIRONMENT & SECURITY SETUP]:

Strict No-Hardcode Policy: The code must fetch SECRET_KEY and ALGORITHM using os.getenv.

Env Generation: Provide a .env.example file and include a Python one-liner in the response that the user can run to generate a secure 32-byte hex SECRET_KEY.

[CLEANUP & OPTIMIZATION]:

Purge Useless Files: Identify and provide instructions/code to delete:

All unused Dockerfile, .dockerignore, and docker-compose.yml files.

Residual Phase 1 files (e.g., local .db or sqlite files).

Boilerplate SvelteKit/FastAPI files (unused counters, greeting routes).

Standardize: Ensure a clean directory structure: /backend and /frontend.

[ACTION]:

Generate updated models.py, a new auth_utils.py, and the modified main.py.

Provide the SvelteKit Auth store and /login page code.

List every file that should be deleted to achieve a "Lean" repository.

## Response snapshot

Updated backend auth/models/env handling for UUID users and env-based JWT config, added optional schema reset, and provided cleanup list plus SvelteKit auth/login snippets.

## Outcome

- Impact: Backend schema/auth config aligned with UUID users and env-only secrets; optional reset added; env example updated.
- Tests: Not run.
- Files: backend/models/todo.py, backend/auth_utils.py, backend/main.py, backend/.env.example
- Next prompts: None.
- Reflection: Frontend in repo is Next.js; provided SvelteKit snippets without modifying frontend files.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): Not run.
- Prompt variant (if applicable): N/A.
- Next experiment (smallest change to try): N/A.
