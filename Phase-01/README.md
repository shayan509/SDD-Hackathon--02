# CLI Todo Application

A feature-complete command-line tool for managing daily tasks. Built with Python, Typer, SQLModel, and Rich for a beautiful terminal experience.

## Features

- ✅ Add new tasks quickly from the command line
- 📋 View all tasks in a formatted table
- ✓ Mark tasks as completed
- ✏️ Update task descriptions
- 🗑️ Delete tasks
- 🎨 Beautiful terminal UI with colors and formatting
- 💾 Persistent SQLite database storage

## Prerequisites

- Python 3.9 or higher
- pip package manager

## Installation

1. Clone or download the project files

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Add a new task
```bash
python main.py add "Your task description here"
```

Example:
```bash
python main.py add "Buy groceries"
```

### List all tasks
```bash
python main.py list
```

This displays all tasks in a formatted table with:
- ID (in grey)
- Task description
- Status (Pending/Completed)
- Created timestamp (YYYY-MM-DD HH:MM)

### Mark a task as completed
```bash
python main.py done [TASK_ID]
```

Example:
```bash
python main.py done 1
```

### Update a task description
```bash
python main.py update [TASK_ID] "New task description"
```

Example:
```bash
python main.py update 1 "Buy groceries and cook dinner"
```

### Delete a task
```bash
python main.py delete [TASK_ID]
```

Example:
```bash
python main.py delete 1
```

## Example Workflow

```bash
# Add some tasks
python main.py add "Buy groceries"
python main.py add "Write documentation"
python main.py add "Review pull requests"

# View all tasks
python main.py list

# Mark a task as done
python main.py done 1

# Update a task
python main.py update 2 "Write comprehensive documentation"

# Delete a task
python main.py delete 3

# View updated list
python main.py list
```

## Windows PowerShell

All commands work the same in PowerShell:
```powershell
python main.py list
python main.py add "Task description"
```

## Technical Details

- **Language**: Python 3.9+
- **CLI Framework**: Typer
- **Database**: SQLite (with SQLModel ORM)
- **Terminal UI**: Rich
- **Storage**: Local SQLite database file (`todos.db`)

## Troubleshooting

### Module not found error
Ensure you've installed the requirements:
```bash
pip install -r requirements.txt
```

### Database operation fails
Check that you have write permissions in the application directory.

### Command not recognized
Make sure Python is installed and added to your PATH.

## Project Structure

```
.
├── main.py              # Main CLI application with all commands
├── models.py            # Todo data model using SQLModel
├── database.py          # Database engine and session management
├── requirements.txt     # Python dependencies
├── README.md            # This file
└── todos.db             # SQLite database (created automatically)
```

## Performance

All commands execute in under 2 seconds, even with up to 1000 tasks.

## License

This project was created as part of the SDD-Hackathon-02.

## Author

Shayan
