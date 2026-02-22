# Data Model: Todo Security Hardening

## Entity: UserAccount
- Purpose: Represents an authenticated person who owns todo records.
- Fields:
  - id (UUID, required, immutable)
  - username (string, required, unique, normalized)
  - password_hash (string, required)
  - created_at (timestamp, required)
  - updated_at (timestamp, required)
- Validation Rules:
  - username must be unique and non-empty.
  - password_hash must never store plaintext credentials.
- Relationships:
  - One UserAccount owns many TodoItem records.

## Entity: TodoItem
- Purpose: Represents a user task managed in authenticated context.
- Fields:
  - id (integer or UUID, required, immutable)
  - user_id (foreign key to UserAccount.id, required)
  - task (string, required, non-empty)
  - is_done (boolean, required, default false)
  - created_at (timestamp, required)
  - updated_at (timestamp, required)
- Validation Rules:
  - task cannot be empty.
  - user_id must reference an existing UserAccount.
- Relationships:
  - Many TodoItem records belong to one UserAccount.

## Entity: SessionToken
- Purpose: Represents an authenticated session credential issued at login.
- Fields:
  - subject_user_id (UUID, required)
  - issued_at (timestamp, required)
  - expires_at (timestamp, required)
  - signature (derived from server secret, required)
- Validation Rules:
  - token must be signed with configured environment secret.
  - expired tokens are rejected.

## State Transitions

### UserAccount
- Registered -> Active (after successful signup)
- Active -> Authenticated Session Issued (after successful login)

### TodoItem
- Created (is_done=false) -> Completed (is_done=true)
- Completed -> Reopened (is_done=false)
- Created/Completed -> Deleted (terminal)

## Authorization Invariants
- Every todo query is filtered by authenticated user identity.
- Every todo mutation verifies ownership before update/delete.
- Unauthenticated callers cannot access TodoItem operations.