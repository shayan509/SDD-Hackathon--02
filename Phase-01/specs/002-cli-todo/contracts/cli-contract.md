# API Contract: CLI Todo Application

## Command Interface Specifications

### Add Command
- **Command**: `python main.py add "task description"`
- **Parameters**: 
  - task (string, required): The description of the task to add
- **Response**: Success message confirming task addition with assigned ID
- **Error Conditions**: 
  - Empty task description
  - Database connection issues

### List Command
- **Command**: `python main.py list`
- **Parameters**: None
- **Response**: Rich table displaying all tasks with columns: ID, Task, Status, Created At
- **Error Conditions**: 
  - Database connection issues

### Done Command
- **Command**: `python main.py done [ID]`
- **Parameters**: 
  - ID (integer, required): The unique identifier of the task to mark as done
- **Response**: Success message confirming task status update
- **Error Conditions**: 
  - Invalid or non-existent task ID
  - Database connection issues

### Update Command
- **Command**: `python main.py update [ID] "new task description"`
- **Parameters**: 
  - ID (integer, required): The unique identifier of the task to update
  - new_task (string, required): The new description for the task
- **Response**: Success message confirming task update
- **Error Conditions**: 
  - Invalid or non-existent task ID
  - Empty new task description
  - Database connection issues

### Delete Command
- **Command**: `python main.py delete [ID]`
- **Parameters**: 
  - ID (integer, required): The unique identifier of the task to delete
- **Response**: Success message confirming task deletion
- **Error Conditions**: 
  - Invalid or non-existent task ID
  - Database connection issues

## Data Models

### Todo Entity
- **id** (integer): Unique identifier for the task
- **task** (string): The description of the task
- **is_done** (boolean): Completion status of the task
- **created_at** (datetime): Timestamp of when the task was created

## Error Handling

### Standard Error Format
- Error messages will be displayed in red text using Rich formatting
- Common error types include:
  - Invalid input parameters
  - Non-existent task IDs
  - Database connectivity issues
  - Permission errors

## UI/UX Specifications

### Color Scheme
- Success messages: Emerald Green
- IDs in tables: Zinc/Grey
- Error messages: Red
- Welcome panel: Default terminal colors

### Table Format (for list command)
- Columns: ID, Task, Status, Created At
- ID column: Zinc/Grey color
- Status column: Shows "Pending" or "Completed"
- Created At: Formatted as YYYY-MM-DD HH:MM