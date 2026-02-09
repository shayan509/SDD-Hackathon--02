import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from sqlmodel.pool import StaticPool
from main import app
from models.todo import TodoItem
from database.engine import engine as default_engine

# Create a test database engine
test_engine = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

@pytest.fixture(name="session", autouse=True)
def session_fixture():
    """Create a fresh database for each test."""
    SQLModel.metadata.create_all(test_engine)
    yield
    SQLModel.metadata.drop_all(test_engine)

# Override the database dependency
def get_test_session():
    with Session(test_engine) as session:
        yield session

from api.v1.endpoints.todos import get_session
app.dependency_overrides[get_session] = get_test_session

client = TestClient(app)

def test_create_todo():
    """Test creating a new todo item."""
    response = client.post("/api/todos/", json={"task": "Test task", "is_done": False})
    assert response.status_code == 201
    data = response.json()
    assert data["task"] == "Test task"
    assert data["is_done"] is False

def test_get_todos():
    """Test retrieving all todo items."""
    # First create a todo
    client.post("/api/todos/", json={"task": "Test task for retrieval", "is_done": False})
    
    # Then get all todos
    response = client.get("/api/todos/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    
def test_update_todo_status():
    """Test updating a todo item's status."""
    # Create a todo first
    create_response = client.post("/api/todos/", json={"task": "Test task for update", "is_done": False})
    assert create_response.status_code == 201
    todo_id = create_response.json()["id"]
    
    # Update the status
    response = client.patch(f"/api/todos/{todo_id}", json={"is_done": True})
    assert response.status_code == 200
    data = response.json()
    assert data["is_done"] is True

def test_delete_todo():
    """Test deleting a todo item."""
    # Create a todo first
    create_response = client.post("/api/todos/", json={"task": "Test task for deletion", "is_done": False})
    assert create_response.status_code == 201
    todo_id = create_response.json()["id"]
    
    # Delete the todo
    response = client.delete(f"/api/todos/{todo_id}")
    assert response.status_code == 204
    
    # Verify it's gone by checking the list
    get_response = client.get("/api/todos/")
    todos = get_response.json()
    assert not any(todo["id"] == todo_id for todo in todos)