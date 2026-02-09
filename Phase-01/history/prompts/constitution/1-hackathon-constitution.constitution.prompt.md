---
id: 1
title: Hackathon Constitution
stage: constitution
date_iso: 2026-02-08
surface: agent
model: Qwen Code
feature: none
branch: main
user: icon
command: /sp.constitution
labels: ["constitution", "hackathon", "setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - ".specify/memory/constitution.md"
tests_yaml: []
---

# Hackathon Constitution Creation

## User Input

```
/sp.constitution [SYSTEM ROLE]: Senior Lead Engineer. [CONTEXT]: Absolute Zero-Scratch Build for Phase 1 Hackathon. [ENVIRONMENT]: Windows 11 (PowerShell) using Gemini CLI.

[PHASE 01 CONSTITUTION]:

Zero Legacy Code: Do not reference or edit any existing files. We are building a fresh directory structure from scratch.

Respect+ Stack:

Backend: FastAPI + SQLModel (SQLite for Phase 1).

Frontend: SvelteKit + Tailwind CSS.

Clean Architecture:

backend/: Dedicated Python environment and logic.

frontend/: Dedicated SvelteKit environment.

root/: Configuration and orchestration files only.

Windows-First: All shell commands must be valid PowerShell. Use python -m venv for environments.

Postgres-Ready: Even though we use SQLite for Phase 1 local dev, the code must be written so switching to Neon (Postgres) in Phase 2 requires only changing the connection string.

Confirm that you are ready to generate a brand new project structure from zero.
```

## Response Summary

Created a new project constitution for Phase 1 Hackathon with the following core principles:
1. Zero Legacy Code - building fresh from scratch
2. Respect+ Stack - using FastAPI+SQLModel for backend and SvelteKit+Tailwind CSS for frontend
3. Clean Architecture - separating backend, frontend, and root configuration
4. Windows-First - using PowerShell commands and python -m venv
5. Postgres-Ready - code written to easily switch from SQLite to Postgres in Phase 2
6. System Role: Senior Lead Engineer - all development under senior oversight

The constitution includes additional constraints, development workflow, and governance sections specific to the hackathon requirements.

## Outcome

Successfully generated a new constitution file at `.specify/memory/constitution.md` with version 1.0.0, ratified on 2026-02-08, following all the specified requirements for the Phase 1 Hackathon.

## Evaluation

The constitution meets all requirements specified by the user, with clear principles that will guide the hackathon development process. The file contains all necessary sections and follows the proper format with an embedded sync impact report.