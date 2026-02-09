"""
Database Configuration Module

This module handles all database-related operations including:
- Database engine creation and configuration
- Table creation and schema management
- Session management for database operations

The module uses SQLModel (built on SQLAlchemy) for ORM functionality
and supports both SQLite (default) and PostgreSQL databases.

Author: Shayan
Project: SDD-Hackathon-02 Phase-01
"""

from sqlmodel import create_engine, Session, SQLModel
from models import Todo
from typing import Generator
import os

# Database URL configuration
# Defaults to SQLite for local development, can be overridden with environment variable
# Example PostgreSQL URL: postgresql://user:password@localhost/dbname
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todos.db")

# Create database engine
# echo=False disables SQL query logging for cleaner output
engine = create_engine(DATABASE_URL, echo=False)


def create_db_and_tables():
    """
    Create database tables if they don't exist.
    
    This function uses SQLModel's metadata to create all defined tables
    in the database. It's idempotent - safe to call multiple times as it
    only creates tables that don't already exist.
    
    Tables created:
    - todo: Stores all todo items with id, task, is_done, and created_at fields
    """
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """
    Get a database session.
    
    This is a generator function that yields a database session and ensures
    proper cleanup after use. Should be used with context managers or next().
    
    Yields:
        Session: SQLModel database session for executing queries
        
    Example:
        with Session(engine) as session:
            # Perform database operations
            pass
    """
    with Session(engine) as session:
        yield session