# Implementation Tasks: CLI Todo Application

**Feature**: CLI Todo Application | **Branch**: `002-cli-todo` | **Date**: 2026-02-08
**Input**: spec.md, plan.md, data-model.md, contracts/, research.md, quickstart.md

## Implementation Strategy

Build the CLI Todo application incrementally, starting with the core functionality (User Story 1: Add New Task) to establish the foundation. Each user story will be implemented as a complete, independently testable increment. The application will be built with Python using Typer for CLI, SQLModel for data modeling, and Rich for terminal UI formatting.

**MVP Scope**: User Story 1 (Add New Task) with basic database functionality and minimal UI.

**Delivery Order**: 
1. Setup and foundational components
2. User Story 1 (Add Task) - P1 priority
3. User Story 2 (View Tasks) - P1 priority
4. User Story 3 (Mark as Done) - P2 priority
5. User Story 4 (Update/Delete Tasks) - P3 priority
6. Polish and cross-cutting concerns

## Phase 1: Setup

Initialize the project structure and install dependencies.

- [x] T001 Create project directory structure at root level
- [x] T002 Create requirements.txt with typer, sqlmodel, rich dependencies
- [x] T003 [P] Create models.py file with basic structure
- [x] T004 [P] Create database.py file with basic structure
- [x] T005 [P] Create main.py file with basic structure

## Phase 2: Foundational Components

Implement core components that all user stories depend on.

- [x] T006 Implement Todo model in models.py using SQLModel with id, task, is_done, created_at fields
- [x] T007 Implement database engine setup in database.py with SQLite connection
- [x] T008 Implement database initialization function in database.py to create tables
- [x] T009 Initialize Typer app in main.py with basic configuration
- [x] T010 Implement database session management in database.py

## Phase 3: User Story 1 - Add New Task (Priority: P1)

As a busy professional, I want to quickly add new tasks to my todo list from the command line so that I can capture ideas and responsibilities without leaving my terminal workflow.

**Independent Test**: Can be fully tested by running the add command with a sample task and verifying it appears in the list command output, delivering the core value of task capture.

**Acceptance Scenarios**:
1. Given user is at terminal prompt, When user runs `python main.py add "Buy groceries"`, Then the task "Buy groceries" is added to the database with pending status
2. Given user has added a task, When user runs the list command, Then the newly added task appears in the displayed table

- [x] T011 [US1] Implement add command in main.py that accepts task description as parameter
- [x] T012 [US1] Connect add command to database to persist new Todo with pending status
- [x] T013 [US1] Add validation to ensure task description is not empty in add command
- [x] T014 [US1] Add success message in emerald green when task is added successfully
- [x] T015 [US1] Test add functionality by running command and verifying task creation

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

As a user, I want to see all my tasks in a well-formatted table so that I can quickly assess my workload and prioritize my activities.

**Independent Test**: Can be fully tested by adding tasks and running the list command, delivering visibility into all tasks with their status.

**Acceptance Scenarios**:
1. Given user has multiple tasks in the database, When user runs `python main.py list`, Then all tasks are displayed in a rich table format with ID, Task, Status, and Created At columns

- [x] T016 [US2] Implement list command in main.py to retrieve all todos from database
- [x] T017 [US2] Create Rich table to display todos with ID, Task, Status, Created At columns
- [x] T018 [US2] Format ID column in zinc/grey color as specified in requirements
- [x] T019 [US2] Show "Pending" or "Completed" in Status column based on is_done field
- [x] T020 [US2] Format Created At column as YYYY-MM-DD HH:MM
- [x] T021 [US2] Test list functionality by adding tasks and verifying table display

## Phase 5: User Story 3 - Mark Task as Completed (Priority: P2)

As a user, I want to mark tasks as completed so that I can track my progress and focus on remaining items.

**Independent Test**: Can be fully tested by marking a task as done and verifying the status change in the list command output, delivering progress tracking capability.

**Acceptance Scenarios**:
1. Given user has a pending task with ID 1, When user runs `python main.py done 1`, Then the task status changes to completed and is reflected when viewing the list

- [x] T022 [US3] Implement done command in main.py that accepts task ID as parameter
- [x] T023 [US3] Add logic to find and update specific todo by ID to set is_done=True
- [x] T024 [US3] Add error handling for invalid/non-existent task IDs in done command
- [x] T025 [US3] Add success message in emerald green when task status is updated
- [x] T026 [US3] Test done functionality by marking task as done and verifying status in list

## Phase 6: User Story 4 - Update and Manage Tasks (Priority: P3)

As a user, I want to update, delete, and manage my tasks so that I can maintain an accurate and organized todo list.

**Independent Test**: Can be fully tested by performing update/delete operations and verifying changes in the list command output, delivering comprehensive task management.

**Acceptance Scenarios**:
1. Given user has a task with ID 1, When user runs `python main.py update 1 "Updated task name"`, Then the task name is changed in the database
2. Given user wants to remove a task, When user runs `python main.py delete 1`, Then the task is removed from the database

- [x] T027 [US4] Implement update command in main.py that accepts ID and new task description
- [x] T028 [US4] Add logic to find and update specific todo by ID with new task description
- [x] T029 [US4] Add validation to ensure new task description is not empty in update command
- [x] T030 [US4] Add error handling for invalid/non-existent task IDs in update command
- [x] T031 [US4] Add success message in emerald green when task is updated successfully
- [x] T032 [US4] Implement delete command in main.py that accepts task ID as parameter
- [x] T033 [US4] Add logic to find and remove specific todo by ID from database
- [x] T034 [US4] Add error handling for invalid/non-existent task IDs in delete command
- [x] T035 [US4] Add success message in emerald green when task is deleted successfully
- [x] T036 [US4] Test update functionality by updating task and verifying change in list
- [x] T037 [US4] Test delete functionality by deleting task and verifying removal from list

## Phase 7: Polish & Cross-Cutting Concerns

Implement error handling, UI enhancements, and final touches.

- [x] T038 Add welcome panel when the application starts using Rich
- [x] T039 Implement comprehensive error handling with informative messages in red
- [x] T040 Add validation for edge cases (empty task names, invalid IDs, etc.)
- [x] T041 Implement graceful handling of database connection issues
- [x] T042 Add README.md with usage instructions based on quickstart guide
- [x] T043 Test complete workflow: add, list, done, update, delete tasks
- [x] T044 Verify all commands execute within performance goals (<2 seconds)
- [x] T045 Perform final integration testing of all features

## Dependencies

User stories are designed to be as independent as possible, but there are some dependencies:
- US2 (List) depends on US1 (Add) to have data to display
- US3 (Done) and US4 (Update/Delete) depend on US1 (Add) to have tasks to operate on
- All stories depend on foundational components (database setup, models)

## Parallel Execution Opportunities

- T003-T005: Creating the basic files can happen in parallel
- T027-T032: Update and delete implementations can happen in parallel
- T036-T037: Testing for update and delete can happen in parallel