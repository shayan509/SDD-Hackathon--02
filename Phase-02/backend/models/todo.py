from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class TodoItem(SQLModel, table=True):
    """
    TodoItem model representing a single todo item in the public list.
    
    Attributes:
        id (int): Unique identifier for the todo item (primary key, auto-generated)
        task (str): The title/name of the todo item (required, max 200 chars)
        description (str): Detailed description of the todo item (optional, max 1000 chars)
        is_done (bool): Completion status of the todo item (default False)
        created_at (datetime): Timestamp when the todo was created
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    task: str = Field(max_length=200, min_length=1)  # Task title must be 1-200 characters
    description: Optional[str] = Field(default="", max_length=1000)  # Optional description
    is_done: bool = Field(default=False)  # Default to not done
    created_at: datetime = Field(default_factory=datetime.utcnow)  # Auto-set creation time