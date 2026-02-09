import React, { useState } from 'react';
import { toggleTodoStatus, deleteTodo } from '../lib/api';

interface Todo {
  id: number;
  task: string;
  description?: string;
  is_done: boolean;
  created_at?: string;
}

interface TodoListProps {
  todos: Todo[];
  onUpdateTodos: (todos: Todo[]) => void;
}

const TodoList: React.FC<TodoListProps> = ({ todos, onUpdateTodos }) => {
  const [expandedId, setExpandedId] = useState<number | null>(null);
  const [deletingId, setDeletingId] = useState<number | null>(null);

  const handleToggle = async (id: number, currentStatus: boolean) => {
    try {
      await toggleTodoStatus(id, currentStatus);
      const updatedTodos = todos.map(todo =>
        todo.id === id ? { ...todo, is_done: !todo.is_done } : todo
      );
      onUpdateTodos(updatedTodos);
    } catch (error) {
      console.error('Error toggling todo:', error);
      alert('Failed to update todo status');
    }
  };

  const handleDelete = async (id: number) => {
    if (!confirm('Are you sure you want to delete this todo?')) {
      return;
    }

    try {
      setDeletingId(id);
      await deleteTodo(id);
      const updatedTodos = todos.filter(todo => todo.id !== id);
      onUpdateTodos(updatedTodos);
    } catch (error) {
      console.error('Error deleting todo:', error);
      alert('Failed to delete todo');
    } finally {
      setDeletingId(null);
    }
  };

  const formatDate = (dateString?: string) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', { 
      month: 'short', 
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  if (todos.length === 0) {
    return (
      <div className="text-center py-12">
        <div className="text-6xl mb-4">📝</div>
        <p className="text-zinc-400 text-lg">No todos yet. Add one above to get started!</p>
      </div>
    );
  }

  return (
    <div className="space-y-3">
      {todos.map((todo) => (
        <div
          key={todo.id}
          className={`group rounded-xl border-2 transition-all duration-200 ${
            todo.is_done 
              ? 'bg-emerald-950/30 border-emerald-800/50' 
              : 'bg-zinc-800/50 border-zinc-700 hover:border-zinc-600'
          } ${deletingId === todo.id ? 'opacity-50' : ''}`}
        >
          <div className="p-4">
            <div className="flex items-start gap-3">
              {/* Checkbox */}
              <button
                onClick={() => handleToggle(todo.id, todo.is_done)}
                className="mt-1 flex-shrink-0"
                disabled={deletingId === todo.id}
              >
                <div className={`w-6 h-6 rounded-lg border-2 flex items-center justify-center transition-all ${
                  todo.is_done 
                    ? 'bg-emerald-500 border-emerald-500' 
                    : 'border-zinc-600 hover:border-emerald-500'
                }`}>
                  {todo.is_done && (
                    <svg className="w-4 h-4 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
                    </svg>
                  )}
                </div>
              </button>

              {/* Content */}
              <div className="flex-grow min-w-0">
                <div className="flex items-start justify-between gap-2">
                  <div className="flex-grow">
                    <h3 className={`text-lg font-medium transition-all ${
                      todo.is_done ? 'line-through text-zinc-500' : 'text-white'
                    }`}>
                      {todo.task}
                    </h3>
                    <div className="flex items-center gap-3 mt-1">
                      <span className="text-xs text-zinc-500 font-mono">
                        ID: {todo.id}
                      </span>
                      {todo.created_at && (
                        <span className="text-xs text-zinc-500">
                          {formatDate(todo.created_at)}
                        </span>
                      )}
                    </div>
                  </div>

                  {/* Actions */}
                  <div className="flex items-center gap-2 flex-shrink-0">
                    {todo.description && (
                      <button
                        onClick={() => setExpandedId(expandedId === todo.id ? null : todo.id)}
                        className="p-2 text-zinc-400 hover:text-white transition-colors"
                        title="Toggle description"
                      >
                        <svg className={`w-5 h-5 transition-transform ${expandedId === todo.id ? 'rotate-180' : ''}`} fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                        </svg>
                      </button>
                    )}
                    <button
                      onClick={() => handleDelete(todo.id)}
                      disabled={deletingId === todo.id}
                      className="p-2 text-zinc-400 hover:text-red-500 transition-colors disabled:opacity-50"
                      title="Delete todo"
                    >
                      {deletingId === todo.id ? (
                        <svg className="w-5 h-5 animate-spin" fill="none" viewBox="0 0 24 24">
                          <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                          <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                        </svg>
                      ) : (
                        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                        </svg>
                      )}
                    </button>
                  </div>
                </div>

                {/* Description */}
                {todo.description && expandedId === todo.id && (
                  <div className="mt-3 pt-3 border-t border-zinc-700">
                    <p className="text-sm text-zinc-300 whitespace-pre-wrap">
                      {todo.description}
                    </p>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
};

export default TodoList;