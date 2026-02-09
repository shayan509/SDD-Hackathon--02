// API client functions for todo operations
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface Todo {
  id: number;
  task: string;
  description?: string;
  is_done: boolean;
  created_at?: string;
  updated_at?: string;
}

/**
 * Fetch all todo items from the API
 */
export const fetchTodos = async (): Promise<Todo[]> => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/todos/`);
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
    const response = await fetch(`${API_BASE_URL}/api/todos/`, {
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
    const response = await fetch(`${API_BASE_URL}/api/todos/${id}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ is_done: !isDone }),
    });
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
    const response = await fetch(`${API_BASE_URL}/api/todos/${id}`, {
      method: 'DELETE',
    });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
  } catch (error) {
    console.error('Error deleting todo:', error);
    throw error;
  }
};
