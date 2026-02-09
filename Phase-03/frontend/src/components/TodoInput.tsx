import React, { useState } from 'react';
import { createTodo } from '../lib/api';

interface TodoInputProps {
  onAddTodo: (todo: any) => void;
}

const TodoInput: React.FC<TodoInputProps> = ({ onAddTodo }) => {
  const [inputValue, setInputValue] = useState('');
  const [description, setDescription] = useState('');
  const [isExpanded, setIsExpanded] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (inputValue.trim() === '') {
      alert('Task title cannot be empty');
      return;
    }

    try {
      setIsLoading(true);
      const newTodo = await createTodo(inputValue, description);
      onAddTodo(newTodo);
      setInputValue('');
      setDescription('');
      setIsExpanded(false);
    } catch (error) {
      console.error('Error creating todo:', error);
      alert('Failed to create todo');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="mb-6">
      <form onSubmit={handleSubmit} className="space-y-3">
        <div className="flex gap-2">
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            placeholder="What needs to be done?"
            className="flex-grow px-4 py-3 border-2 border-zinc-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent bg-zinc-800 text-white placeholder-zinc-500 transition-all"
            maxLength={200}
            disabled={isLoading}
          />
          <button
            type="button"
            onClick={() => setIsExpanded(!isExpanded)}
            className="px-4 py-3 bg-zinc-700 text-white rounded-lg hover:bg-zinc-600 focus:outline-none focus:ring-2 focus:ring-zinc-500 transition-all"
            disabled={isLoading}
          >
            {isExpanded ? '−' : '+'}
          </button>
          <button
            type="submit"
            disabled={isLoading}
            className="px-6 py-3 bg-emerald-500 text-white rounded-lg hover:bg-emerald-600 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2 focus:ring-offset-zinc-900 transition-all disabled:opacity-50 disabled:cursor-not-allowed font-medium"
          >
            {isLoading ? 'Adding...' : 'Add'}
          </button>
        </div>
        
        {isExpanded && (
          <div className="animate-fadeIn">
            <textarea
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              placeholder="Add a description (optional)..."
              className="w-full px-4 py-3 border-2 border-zinc-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent bg-zinc-800 text-white placeholder-zinc-500 resize-none transition-all"
              rows={3}
              maxLength={1000}
              disabled={isLoading}
            />
            <div className="text-xs text-zinc-500 mt-1 text-right">
              {description.length}/1000 characters
            </div>
          </div>
        )}
      </form>
    </div>
  );
};

export default TodoInput;