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


if __name__ == "__main__":
    app()