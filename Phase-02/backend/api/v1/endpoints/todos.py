from typing import Annotated, List

from fastapi import APIRouter, Depends
from sqlmodel import Session

from auth_utils import get_current_user, get_db_session
from models.todo import TodoCreate, TodoItem, TodoUpdate, User
from services.service import (
    create_todo_for_user,
    delete_todo_for_user,
    get_all_todos_for_user,
    update_todo_for_user,
)

router = APIRouter(prefix="/todos", tags=["todos"])

@router.get("/", response_model=List[TodoItem])
def get_todos(
    session: Annotated[Session, Depends(get_db_session)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    return get_all_todos_for_user(session, current_user.id)

@router.post("/", response_model=TodoItem, status_code=201)
def create_todo(
    todo: TodoCreate,
    session: Annotated[Session, Depends(get_db_session)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    return create_todo_for_user(session, todo, current_user.id)

@router.patch("/{todo_id}", response_model=TodoItem)
def update_todo_status(
    todo_id: int,
    todo_update: TodoUpdate,
    session: Annotated[Session, Depends(get_db_session)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    return update_todo_for_user(session, todo_id, todo_update, current_user.id)

@router.delete("/{todo_id}", status_code=204)
def delete_todo(
    todo_id: int,
    session: Annotated[Session, Depends(get_db_session)],
    current_user: Annotated[User, Depends(get_current_user)],
):
    delete_todo_for_user(session, todo_id, current_user.id)
    return None
