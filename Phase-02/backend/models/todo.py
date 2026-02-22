from datetime import datetime, timezone
from typing import Optional
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    email: str = Field(index=True, unique=True)
    username: str = Field(index=True)
    hashed_password: str


class TodoItemBase(SQLModel):
    task: str = Field(max_length=200, min_length=1)
    description: str = Field(default="", max_length=1000)


class TodoItem(TodoItemBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    is_done: bool = Field(default=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    user_id: UUID = Field(foreign_key="user.id", index=True)


class TodoCreate(TodoItemBase):
    pass


class TodoUpdate(SQLModel):
    is_done: Optional[bool] = None
