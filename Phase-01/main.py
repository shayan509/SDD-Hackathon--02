"""
CLI Todo Application - Main Entry Point

This module provides a command-line interface for managing daily tasks.
It uses Typer for CLI framework, Rich for beautiful terminal output,
and SQLModel for database operations.

Features:
- Add new tasks to the database
- Rich terminal UI with colors and formatting
- SQLite database for persistent storage

Author: Shayan
Project: SDD-Hackathon-02 Phase-01
"""

import typer
from typing import Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.style import Style
from contextlib import contextmanager
from database import get_session, create_db_and_tables
from models import Todo

# Initialize Typer app - main CLI application instance
app = typer.Typer()

# Initialize Rich console - for beautiful terminal output
console = Console()


@contextmanager
def get_db_session():
    """
    Context manager for database sessions.
    
    Provides a safe way to handle database sessions with automatic
    cleanup and error handling. Ensures sessions are properly closed
    even if an exception occurs.
    
    Yields:
        Session: SQLModel database session
        
    Raises:
        Exception: Re-raises any exception after rolling back the transaction
    """
    try:
        session_gen = get_session()
        session = next(session_gen)
        yield session
    except Exception as e:
        # Rollback any pending changes if an error occurs
        session.rollback()
        raise e
    finally:
        # Always close the session to free resources
        session.close()


@app.callback()
def callback():
    """
    CLI tool for managing daily tasks.
    
    This callback runs before any command is executed. It displays
    a welcome message and ensures the database tables are created.
    """
    # Display welcome panel when the app starts
    console.print(
        Panel(
            "Welcome to CLI Todo App!",
            style="bold blue",
            border_style="bright_blue"
        )
    )
    # Initialize database tables if they don't exist
    create_db_and_tables()


@app.command()
def add(task_description: str):
    """
    Add a new task to the database.
    
    Creates a new todo item with the provided description and saves it
    to the SQLite database. Validates input and provides user feedback.
    
    Args:
        task_description (str): The description of the task to add
        
    Example:
        $ python main.py add "Buy groceries"
        ✓ Task 'Buy groceries' added successfully with ID: 1
    """
    # Validate that task description is not empty
    if not task_description.strip():
        console.print("[red]Error: Task description cannot be empty.[/red]")
        return
    
    with get_db_session() as session:
        # Create a new Todo object with the sanitized task description
        todo = Todo(task=task_description.strip())
        
        # Add the todo to the database and commit the transaction
        session.add(todo)
        session.commit()
        # Refresh to get the auto-generated ID from the database
        session.refresh(todo)
        
        # Display success message in emerald green with checkmark
        console.print(f"[green]✓ Task '{todo.task}' added successfully with ID: {todo.id}[/green]")


@app.command()
def list():
    """
    List all tasks in a formatted table.
    
    Retrieves all todos from the database and displays them in a Rich table
    with columns for ID, Task, Status, and Created At. The table provides
    a clear overview of all tasks and their current status.
    
    Example:
        $ python main.py list
        ┌────┬─────────────────┬───────────┬──────────────────┐
        │ ID │ Task            │ Status    │ Created At       │
        ├────┼─────────────────┼───────────┼──────────────────┤
        │ 1  │ Buy groceries   │ Pending   │ 2026-02-10 14:30 │
        └────┴─────────────────┴───────────┴──────────────────┘
    """
    with get_db_session() as session:
        # Retrieve all todos from the database
        from sqlmodel import select
        todos = session.exec(select(Todo)).all()
        
        # Check if there are any tasks
        if not todos:
            console.print("[yellow]No tasks found. Add a task using 'python main.py add \"task description\"'[/yellow]")
            return
        
        # Create a Rich table with specified columns
        table = Table(show_header=True, header_style="bold cyan")
        table.add_column("ID", style="dim", justify="right")  # Zinc/grey color using "dim"
        table.add_column("Task", style="white")
        table.add_column("Status", justify="center")
        table.add_column("Created At", style="white")
        
        # Add rows to the table
        for todo in todos:
            # Determine status text based on is_done field
            status = "Completed" if todo.is_done else "Pending"
            status_style = "green" if todo.is_done else "yellow"
            
            # Format created_at as YYYY-MM-DD HH:MM
            created_at_str = todo.created_at.strftime("%Y-%m-%d %H:%M")
            
            # Add row with styled status
            table.add_row(
                str(todo.id),
                todo.task,
                f"[{status_style}]{status}[/{status_style}]",
                created_at_str
            )
        
        # Display the table
        console.print(table)


@app.command()
def done(task_id: int):
    """
    Mark a task as completed.
    
    Updates the specified task's status to completed in the database.
    Provides feedback on success or if the task ID is invalid.
    
    Args:
        task_id (int): The ID of the task to mark as done
        
    Example:
        $ python main.py done 1
        ✓ Task marked as completed!
    """
    with get_db_session() as session:
        # Find the todo by ID
        from sqlmodel import select
        todo = session.exec(select(Todo).where(Todo.id == task_id)).first()
        
        # Check if todo exists
        if not todo:
            console.print(f"[red]Error: Task with ID {task_id} not found.[/red]")
            return
        
        # Update the is_done status
        todo.is_done = True
        session.add(todo)
        session.commit()
        
        # Display success message in emerald green
        console.print(f"[green]✓ Task '{todo.task}' marked as completed![/green]")


@app.command()
def update(task_id: int, new_task: str):
    """
    Update a task's description.
    
    Changes the description of an existing task in the database.
    Validates input and provides feedback on success or errors.
    
    Args:
        task_id (int): The ID of the task to update
        new_task (str): The new description for the task
        
    Example:
        $ python main.py update 1 "Buy groceries and cook dinner"
        ✓ Task updated successfully!
    """
    # Validate that new task description is not empty
    if not new_task.strip():
        console.print("[red]Error: Task description cannot be empty.[/red]")
        return
    
    with get_db_session() as session:
        # Find the todo by ID
        from sqlmodel import select
        todo = session.exec(select(Todo).where(Todo.id == task_id)).first()
        
        # Check if todo exists
        if not todo:
            console.print(f"[red]Error: Task with ID {task_id} not found.[/red]")
            return
        
        # Update the task description
        todo.task = new_task.strip()
        session.add(todo)
        session.commit()
        
        # Display success message in emerald green
        console.print(f"[green]✓ Task updated successfully![/green]")


@app.command()
def delete(task_id: int):
    """
    Delete a task from the database.
    
    Permanently removes the specified task from the database.
    Provides feedback on success or if the task ID is invalid.
    
    Args:
        task_id (int): The ID of the task to delete
        
    Example:
        $ python main.py delete 1
        ✓ Task deleted successfully!
    """
    with get_db_session() as session:
        # Find the todo by ID
        from sqlmodel import select
        todo = session.exec(select(Todo).where(Todo.id == task_id)).first()
        
        # Check if todo exists
        if not todo:
            console.print(f"[red]Error: Task with ID {task_id} not found.[/red]")
            return
        
        # Delete the todo
        session.delete(todo)
        session.commit()
        
        # Display success message in emerald green
        console.print(f"[green]✓ Task deleted successfully![/green]")


if __name__ == "__main__":
    app()