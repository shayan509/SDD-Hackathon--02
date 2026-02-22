from uuid import UUID
from datetime import datetime, timezone

from fastapi import HTTPException
from sqlmodel import Session, select

from models.todo import TodoCreate, TodoItem, TodoUpdate


def get_all_todos_for_user(session: Session, user_id: UUID) -> list[TodoItem]:
    return session.exec(select(TodoItem).where(TodoItem.user_id == user_id)).all()


def create_todo_for_user(session: Session, payload: TodoCreate, user_id: UUID) -> TodoItem:
    task = payload.task.strip()
    if not task:
        raise HTTPException(status_code=400, detail="Task cannot be empty")

    todo = TodoItem(
        task=task,
        description=payload.description.strip() if payload.description else "",
        is_done=False,
        user_id=user_id,
    )
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo


def update_todo_for_user(
    session: Session,
    todo_id: int,
    payload: TodoUpdate,
    user_id: UUID,
) -> TodoItem:
    todo = session.get(TodoItem, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    if todo.user_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")

    if payload.is_done is not None:
        todo.is_done = payload.is_done
    todo.updated_at = datetime.now(timezone.utc)

    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo


def delete_todo_for_user(session: Session, todo_id: int, user_id: UUID) -> None:
    todo = session.get(TodoItem, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    if todo.user_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden")

    session.delete(todo)
    session.commit()
