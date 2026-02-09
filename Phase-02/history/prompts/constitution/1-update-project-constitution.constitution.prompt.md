---
id: 1
title: "Update Project Constitution"
stage: constitution
date_iso: "2026-02-08"
surface: agent
model: "Qwen Code"
feature: "none"
branch: "main"
user: "icon"
command: "/sp.constitution [SYSTEM ROLE]: Senior Full-Stack Architect (SvelteKit + FastAPI + Neon Specialist). [CONTEXT]: Phase 2 Hackathon Survival Mode. Windows Environment. No Authentication."
labels: ["constitution", "hackathon", "sveltekit", "fastapi", "neon"]
spec: null
ticket: null
adr: null
pr: null
outcome: "Successfully updated the project constitution with the specified principles and guidelines for the Phase-02 Hackathon project."
evaluation: "The constitution was successfully updated with all required principles and guidelines, validated, and saved to the appropriate location."
files_yaml:
  - ".specify/memory/constitution.md"
tests_yaml: []
---

# Prompt History Record

## PROMPT_TEXT

/sp.constitution [SYSTEM ROLE]: Senior Full-Stack Architect (SvelteKit + FastAPI + Neon Specialist). [CONTEXT]: Phase 2 Hackathon Survival Mode. Windows Environment. No Authentication.

[CORE PRINCIPLES]:

Code Reuse > Generation: Search the existing app/backend logic for Todo CRUD. Do not rewrite existing working Python logic; simply adapt it to Neon.

Anti-Hallucination Rule: NEVER suggest an "Auth," "User," or "Login" model. The system is a single-table, public-access global list.

The "Respect+" Standard: Every frontend instruction must prioritize SvelteKit 5 conventions (Runes, simple stores) to maximize the "Respect+" bonus score.

Windows Native: All shell commands must be formatted for PowerShell (e.g., use Remove-Item instead of rm -rf).

Connection Protocol: All database connections MUST use sslmode=require. If the code misses this, the deployment will fail.

[VISUAL DESIGN SYSTEM]:

Primary: #10b981 (Emerald-500)

Background: #09090b (Zinc-950)

Surface: #18181b (Zinc-900)

Font: System Sans-Serif, high contrast.

Confirm you have internalized these constraints before receiving the Specification.

## RESPONSE_TEXT

I have successfully updated the project constitution based on the provided principles. Here's the summary:

**New version**: 1.0.0 (initial version based on provided principles)

**Changes made**:
- Updated all placeholder tokens with the specific principles provided
- Added the Core Principles including Code Reuse > Generation, Anti-Hallucination Rule, Respect+ Standard, Windows Native, Connection Protocol, and SvelteKit + FastAPI + Neon Specialization
- Included the Visual Design System specifications
- Added Development Context section for the hackathon
- Created the Sync Impact Report at the top of the file
- Set the ratification date as a TODO since the original date is unknown

**Files updated**:
- `.specify/memory/constitution.md` (completely rewritten with new content)

**Bump rationale**: This is the initial version of the constitution based on the specific principles provided for the Phase-02 Hackathon project, replacing the generic template.

**Manual follow-up required**:
- The RATIFICATION_DATE needs to be set with the actual original adoption date when available

**Suggested commit message**: `docs: amend constitution to v1.0.0 (hackathon principles implementation)`

The constitution now accurately reflects the specific requirements and principles for the Phase-02 Hackathon project, emphasizing the technology stack (SvelteKit + FastAPI + Neon), the development constraints (no authentication, Windows environment), and the design system specifications.