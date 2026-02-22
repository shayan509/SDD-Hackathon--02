# Tasks: Todo Security Hardening

**Input**: Design documents from `C:\Users\icon\Desktop\SDD-Hackathon--02\specs\001-todo-security-hardening\`
**Prerequisites**: `plan.md` (required), `spec.md` (required), `research.md`, `data-model.md`, `contracts/openapi.yaml`, `quickstart.md`

**Tests**: Test execution tasks are included only where needed to validate independent story completion criteria.

**Organization**: Tasks are grouped by user story so each story can be implemented and validated independently.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: User story label (`[US1]`, `[US2]`, `[US3]`)
- Every task includes an exact file path

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Align dependencies and project configuration for secure auth + user-owned todos.

- [X] T001 Update backend security dependencies in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\backend\requirements.txt`
- [X] T002 [P] Add required secret/env placeholders in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\backend\.env.example`
- [X] T003 [P] Add frontend API/auth environment placeholders in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\frontend\.env.example`
- [X] T004 Document secure local setup for Windows in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\README.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core auth and ownership infrastructure that blocks all user stories until complete.

- [X] T005 Create canonical auth configuration loader with strict env validation in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\backend\auth_utils.py`
- [X] T006 [P] Add UserAccount + ownership-ready Todo schema definitions in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\backend\models\todo.py`
- [X] T007 [P] Implement DB session + SSL-required Neon connection wiring in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\backend\database\engine.py`
- [X] T008 Implement shared authenticated-user dependency and global auth error responses in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\backend\main.py`
- [X] T009 Wire token parsing helper for frontend requests in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\frontend\src\lib\auth.js`

**Checkpoint**: Foundational auth + schema work complete; user stories can proceed.

---

## Phase 3: User Story 1 - Secure Account Access (Priority: P1) MVP

**Goal**: Enable secure signup/login and block unauthenticated todo access.

**Independent Test**: Create a new account, login successfully, and confirm unauthenticated calls to `/todos` are denied.

### Implementation for User Story 1

- [X] T010 [US1] Implement signup endpoint behavior in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\backend\api\v1\endpoints\auth.py`
- [X] T011 [US1] Implement login endpoint behavior and token issuance in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\backend\api\v1\endpoints\auth.py`
- [X] T012 [P] [US1] Integrate auth routes and unauthorized handling in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\backend\main.py`
- [X] T013 [P] [US1] Build login/signup API helpers with token persistence in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\frontend\src\lib\api.ts`
- [X] T014 [US1] Implement login/signup session state flows in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\frontend\src\lib\auth.js`
- [X] T015 [US1] Apply Modern Night auth screen + guarded todo access behavior in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\frontend\src\components\TodoHeader.tsx`

**Checkpoint**: US1 fully functional and independently testable.

---

## Phase 4: User Story 2 - User-Owned Todo Isolation (Priority: P2)

**Goal**: Ensure each authenticated user can CRUD only their own todos.

**Independent Test**: With two accounts, verify each sees only own todos and cannot update/delete the other user's items.

### Implementation for User Story 2

- [X] T016 [US2] Add user-scoped todo query and mutation service logic in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\backend\services\service.py`
- [X] T017 [US2] Enforce owner filtering for list/create/update/delete endpoints in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\backend\api\v1\endpoints\todos.py`
- [X] T018 [P] [US2] Add cross-user access rejection behavior and status mapping in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\backend\main.py`
- [X] T019 [P] [US2] Update authenticated todo API client methods for owner-safe errors in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\frontend\src\lib\api.ts`
- [X] T020 [US2] Update todo list state handling for authenticated user data isolation in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\frontend\src\components\TodoList.tsx`
- [X] T021 [US2] Update todo create/toggle interactions for authenticated ownership context in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\frontend\src\components\TodoInput.tsx`

**Checkpoint**: US2 fully functional and independently testable.

---

## Phase 5: User Story 3 - Reliable Schema and Repository Hygiene (Priority: P3)

**Goal**: Ensure fresh deploy schema reliability, environment-only secrets, and cleanup of obsolete artifacts.

**Independent Test**: Run fresh schema initialization successfully and verify scoped obsolete Docker/phase-1 artifacts are removed.

### Implementation for User Story 3

- [X] T022 [US3] Implement startup schema initialization flow for fresh deploy in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\backend\main.py`
- [X] T023 [P] [US3] Add explicit schema migration/initialization command path in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\backend\migrate_db.py`
- [X] T024 [US3] Enforce fail-fast startup when required secrets are missing in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\backend\auth_utils.py`
- [X] T025 [US3] Remove obsolete Docker and phase-1 artifacts listed in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\README.md`
- [X] T026 [US3] Update deployment/setup notes for clean backend/frontend structure in `C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\DEPLOYMENT_GUIDE.md`

**Checkpoint**: US3 fully functional and independently testable.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final verification and consistency across all stories.

- [X] T027 [P] Validate API contract alignment against implemented endpoints in `C:\Users\icon\Desktop\SDD-Hackathon--02\specs\001-todo-security-hardening\contracts\openapi.yaml`
- [X] T028 Run end-to-end security acceptance checks from `C:\Users\icon\Desktop\SDD-Hackathon--02\specs\001-todo-security-hardening\quickstart.md`
- [X] T029 [P] Record implementation notes and residual risks in `C:\Users\icon\Desktop\SDD-Hackathon--02\specs\001-todo-security-hardening\plan.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: starts immediately.
- **Phase 2 (Foundational)**: depends on Phase 1 and blocks all user stories.
- **Phase 3 (US1)**: depends on Phase 2.
- **Phase 4 (US2)**: depends on Phase 2 and can begin after US1 auth contract is stable.
- **Phase 5 (US3)**: depends on Phase 2 and may run in parallel with US2.
- **Phase 6 (Polish)**: depends on completion of all selected user stories.

### User Story Dependency Graph

- `US1 -> US2`
- `US1 -> US3`
- `US2` and `US3` can run concurrently once `US1` auth surface is stable.

### Parallel Opportunities

- **Setup**: `T002` and `T003` can run in parallel.
- **Foundational**: `T006` and `T007` can run in parallel; `T009` can run while backend foundational tasks complete.
- **US1**: `T012` and `T013` can run in parallel after `T010`/`T011` start.
- **US2**: `T018` and `T019` can run in parallel after `T016`/`T017`.
- **US3**: `T023` can run in parallel with `T022` once schema approach is fixed.
- **Polish**: `T027` and `T029` can run in parallel before final validation `T028`.

---

## Parallel Example: User Story 1

- Run `T012` and `T013` together after backend auth endpoints (`T010`, `T011`) exist.

## Parallel Example: User Story 2

- Run `T018` and `T019` together after owner-scoped service and endpoint logic (`T016`, `T017`) is in place.

## Parallel Example: User Story 3

- Run `T023` in parallel with `T022` once startup initialization inputs are finalized.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1 and Phase 2.
2. Complete Phase 3 (US1).
3. Validate US1 independent test criteria before expanding scope.

### Incremental Delivery

1. Deliver US1 (secure account access).
2. Deliver US2 (user-owned todo isolation).
3. Deliver US3 (schema/deploy reliability and cleanup).
4. Complete Phase 6 polish and final acceptance checks.

### Validation Notes

- Every task follows required checklist format: checkbox, task ID, optional `[P]`, required `[US#]` for story tasks, and exact file path.
- Story phases are independently testable and mapped to priority order (P1 -> P2 -> P3).