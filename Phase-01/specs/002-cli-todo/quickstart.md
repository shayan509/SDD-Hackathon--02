# Quickstart Guide: CLI Todo Application

## Prerequisites
- Python 3.9 or higher
- pip package manager

## Setup

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

### List all tasks
```bash
python main.py list
```

### Mark a task as completed
```bash
python main.py done [TASK_ID]
```

### Update a task name
```bash
python main.py update [TASK_ID] "New task description"
```

### Delete a task
```bash
python main.py delete [TASK_ID]
```

## Example Workflow

1. Add a task:
   ```bash
   python main.py add "Buy groceries"
   ```

2. View all tasks:
   ```bash
   python main.py list
   ```

3. Mark task as done (assuming the task ID is 1):
   ```bash
   python main.py done 1
   ```

## Windows PowerShell Command
```powershell
python main.py list
```

## Troubleshooting

- If you get a module not found error, ensure you've installed the requirements with `pip install -r requirements.txt`
- If database operations fail, check that you have write permissions in the application directory