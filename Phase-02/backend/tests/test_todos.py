import os
import sys
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from sqlmodel.pool import StaticPool

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from auth_utils import get_db_session
from main import app


test_engine = create_engine(
    'sqlite:///:memory:',
    connect_args={'check_same_thread': False},
    poolclass=StaticPool,
)


@pytest.fixture(name='session', autouse=True)
def session_fixture():
    SQLModel.metadata.create_all(test_engine)
    yield
    SQLModel.metadata.drop_all(test_engine)


def get_test_session():
    with Session(test_engine) as session:
        yield session


app.dependency_overrides[get_db_session] = get_test_session
client = TestClient(app)


def auth_headers() -> dict[str, str]:
    username = f'user-{uuid4().hex[:8]}'
    password = 'password123'

    signup_response = client.post('/api/auth/signup', json={'username': username, 'password': password})
    assert signup_response.status_code == 201

    login_response = client.post(
        '/api/auth/login',
        json={'username': username, 'password': password},
    )
    assert login_response.status_code == 200

    token = login_response.json()['access_token']
    return {'Authorization': f'Bearer {token}'}


def test_create_todo():
    headers = auth_headers()
    response = client.post('/api/todos/', json={'task': 'Test task'}, headers=headers)
    assert response.status_code == 201
    data = response.json()
    assert data['task'] == 'Test task'
    assert data['is_done'] is False


def test_unauthenticated_requests_rejected():
    response = client.get('/api/todos/')
    assert response.status_code == 401


def test_get_todos():
    headers = auth_headers()
    create_response = client.post('/api/todos/', json={'task': 'Test task for retrieval'}, headers=headers)
    assert create_response.status_code == 201

    response = client.get('/api/todos/', headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1


def test_update_todo_status():
    headers = auth_headers()
    create_response = client.post('/api/todos/', json={'task': 'Test task for update'}, headers=headers)
    assert create_response.status_code == 201
    todo_id = create_response.json()['id']

    response = client.patch(f'/api/todos/{todo_id}', json={'is_done': True}, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data['is_done'] is True


def test_delete_todo():
    headers = auth_headers()
    create_response = client.post('/api/todos/', json={'task': 'Test task for deletion'}, headers=headers)
    assert create_response.status_code == 201
    todo_id = create_response.json()['id']

    response = client.delete(f'/api/todos/{todo_id}', headers=headers)
    assert response.status_code == 204

    get_response = client.get('/api/todos/', headers=headers)
    todos = get_response.json()
    assert not any(todo['id'] == todo_id for todo in todos)


def test_cross_user_access_blocked():
    user_a_headers = auth_headers()
    user_b_headers = auth_headers()

    created = client.post('/api/todos/', json={'task': 'private todo'}, headers=user_a_headers)
    assert created.status_code == 201
    todo_id = created.json()['id']

    update_attempt = client.patch(
        f'/api/todos/{todo_id}',
        json={'is_done': True},
        headers=user_b_headers,
    )
    assert update_attempt.status_code == 403

    delete_attempt = client.delete(f'/api/todos/{todo_id}', headers=user_b_headers)
    assert delete_attempt.status_code == 403
