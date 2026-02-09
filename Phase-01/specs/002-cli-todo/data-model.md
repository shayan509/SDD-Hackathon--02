# Data Model: CLI Todo Application

## Entity: Todo

**Description**: Represents a single task in the user's todo list

**Fields**:
- `id` (Integer): Primary key, auto-generated unique identifier for each task
- `task` (String): The text description of the task (required)
- `is_done` (Boolean): Flag indicating whether the task is completed (default: False)
- `created_at` (DateTime): Timestamp when the task was created (auto-generated)

**Validation Rules**:
- `task` field must not be empty or consist only of whitespace
- `id` must be unique across all records
- `created_at` is automatically set when record is created

**State Transitions**:
- `is_done` transitions from `False` to `True` when task is marked as completed
- Once `is_done` is `True`, it can remain `True` or be changed back to `False`

**Relationships**: 
- No relationships with other entities in this simple model

## Database Schema

```sql
CREATE TABLE todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    is_done BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## Indexes
- Primary key index on `id` (automatically created)
- Potential index on `is_done` for filtering completed tasks (to be evaluated based on usage patterns)