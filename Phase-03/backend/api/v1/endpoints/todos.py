from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from models.todo import TodoItem
from database.engine import engine
from typing import List
import logging

router = APIRouter(prefix="/todos", tags=["todos"])

def get_session():
    try:
        with Session(engine) as session:
            yield session
    except Exception as e:
        logging.error(f"Database connection error: {e}")
        raise HTTPException(status_code=503, detail="Database service unavailable")

@router.get("/", response_model=List[TodoItem])
def get_todos(session: Session = Depends(get_session)):
    """Get all todo items from the public list."""
    try:
        from sqlmodel import select
        todos = session.exec(select(TodoItem)).all()
        return todos
    except Exception as e:
        logging.error(f"Error fetching todos: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/", response_model=TodoItem, status_code=201)
def create_todo(todo: TodoItem, session: Session = Depends(get_session)):
    """Create a new todo item in the public list."""
    try:
        # Validate that the task is not empty
        if not todo.task.strip():
            raise HTTPException(status_code=400, detail="Task cannot be empty")
        
        # Create the new todo item
        db_todo = TodoItem(
            task=todo.task,
            description=todo.description or "",
            is_done=todo.is_done
        )
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        return db_todo
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Error creating todo: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.patch("/{todo_id}", response_model=TodoItem)
def update_todo_status(todo_id: int, todo_update: dict, session: Session = Depends(get_session)):
    """Toggle the completion status of a todo item."""
    try:
        db_todo = session.get(TodoItem, todo_id)
        if not db_todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        
        # Only update the is_done field if provided
        if 'is_done' in todo_update:
            db_todo.is_done = todo_update['is_done']
        
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        return db_todo
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Error updating todo: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.delete("/{todo_id}", status_code=204)
def delete_todo(todo_id: int, session: Session = Depends(get_session)):
    """Delete a todo item from the public list."""
    try:
        db_todo = session.get(TodoItem, todo_id)
        if not db_todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        
        session.delete(db_todo)
        session.commit()
        return None
    except HTTPException:
        raise
    except Exception as e:
        logging.error(f"Error deleting todo: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")