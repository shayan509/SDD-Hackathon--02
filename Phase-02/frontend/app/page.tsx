"use client";

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { toast } from 'react-toastify';
import TodoHeader from '@/src/components/TodoHeader';
import TodoInput from '@/src/components/TodoInput';
import TodoList from '@/src/components/TodoList';
import { fetchTodos } from '@/src/lib/api';
import { clearToken, isAuthenticated } from '@/src/lib/auth';

type Todo = {
  id: number;
  task: string;
  description?: string;
  is_done: boolean;
  created_at?: string;
};

export default function Home() {
  const router = useRouter();
  const [todos, setTodos] = useState<Todo[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    if (!isAuthenticated()) {
      router.replace('/login');
      return;
    }
    loadTodos();
  }, [router]);

  const loadTodos = async () => {
    try {
      setIsLoading(true);
      const data = await fetchTodos();
      setTodos(data);
    } catch (error) {
      console.error('Error loading todos:', error);
      toast.error('Failed to load todos. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleAddTodo = async (newTodo: Todo) => {
    setTodos(prevTodos => [...prevTodos, newTodo]);
    toast.success('Todo added successfully!');
  };

  const handleUpdateTodos = (updatedTodos: Todo[]) => {
    setTodos(updatedTodos);
  };

  const handleLogout = () => {
    clearToken();
    toast.info('Logged out successfully');
    router.replace('/login');
  };

  const completedCount = todos.filter(todo => todo.is_done).length;

  return (
    <div className="min-h-screen bg-gradient-to-br from-zinc-950 via-zinc-900 to-zinc-950 text-white">
      <div className="container mx-auto px-4 py-8 max-w-4xl">
        <TodoHeader 
          title="My Todo Wall" 
          todoCount={todos.length}
          completedCount={completedCount}
          onLogout={handleLogout}
        />
        
        <div className="bg-zinc-900/50 backdrop-blur-sm rounded-2xl shadow-2xl border border-zinc-800 p-6">
          <TodoInput onAddTodo={handleAddTodo} />
          
          {isLoading ? (
            <div className="text-center py-12">
              <div className="inline-block animate-spin rounded-full h-12 w-12 border-4 border-zinc-700 border-t-emerald-500"></div>
              <p className="mt-4 text-zinc-400">Loading todos...</p>
            </div>
          ) : (
            <TodoList todos={todos} onUpdateTodos={handleUpdateTodos} />
          )}
        </div>

        {/* Footer */}
        <div className="mt-8 text-center text-zinc-500 text-sm">
          <p>Built with Next.js, FastAPI, and Neon PostgreSQL</p>
        </div>
      </div>
    </div>
  );
}
