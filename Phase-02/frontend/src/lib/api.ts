// API client functions for todo operations
const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000" || "https://sdd-hackathon-02-p2-backend.onrender.com";
import { getToken } from './auth';

export interface Todo {
  id: number;
  task: string;
  description?: string;
  is_done: boolean;
  created_at?: string;
  updated_at?: string;
}

const authFetch = async (url: string, options: RequestInit = {}) => {
  const token = getToken();
  const headers = new Headers(options.headers || {});
  if (token) {
    headers.set('Authorization', `Bearer ${token}`);
  }
  return fetch(url, { ...options, headers });
};

/**
 * Fetch all todo items from the API
 */
export const fetchTodos = async (): Promise<Todo[]> => {
  try {
    const response = await authFetch(`${API_BASE_URL}/api/todos/`);
    if (response.status === 401) {
      throw new Error("Unauthorized");
    }
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching todos:', error);
    throw error;
  }
};

/**
 * Create a new todo item via the API
 */
export const createTodo = async (task: string, description: string = ""): Promise<Todo> => {
  try {
    const response = await authFetch(`${API_BASE_URL}/api/todos/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ task, description, is_done: false }),
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error creating todo:', error);
    throw error;
  }
};

/**
 * Toggle the completion status of a todo item
 */
export const toggleTodoStatus = async (id: number, isDone: boolean): Promise<Todo> => {
  try {
    const response = await authFetch(`${API_BASE_URL}/api/todos/${id}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ is_done: !isDone }),
    });
    if (response.status === 403) {
      throw new Error("Forbidden");
    }
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error toggling todo status:', error);
    throw error;
  }
};

/**
 * Delete a todo item via the API
 */
export const deleteTodo = async (id: number): Promise<void> => {
  try {
    const response = await authFetch(`${API_BASE_URL}/api/todos/${id}`, {
      method: 'DELETE',
    });
    if (response.status === 403) {
      throw new Error("Forbidden");
    }
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
  } catch (error) {
    console.error('Error deleting todo:', error);
    throw error;
  }
};

export const login = async (email: string, password: string): Promise<string> => {
  const response = await fetch(`${API_BASE_URL}/api/auth/login`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email, password }),
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    const errorMessage = errorData.detail || 'Invalid email or password';
    throw new Error(errorMessage);
  }

  const data = await response.json();
  return data.access_token;
};

export const signup = async (email: string, username: string, password: string): Promise<void> => {
  const response = await fetch(`${API_BASE_URL}/api/auth/signup`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ email, username, password }),
  });

  if (!response.ok) {
    const data = await response.json().catch(() => ({}));
    throw new Error(data.detail || 'Signup failed');
  }
};
