import React from 'react';

interface TodoHeaderProps {
  title?: string;
  todoCount?: number;
  completedCount?: number;
}

const TodoHeader: React.FC<TodoHeaderProps> = ({ 
  title = "Public Wall", 
  todoCount = 0,
  completedCount = 0 
}) => {
  return (
    <header className="mb-8">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-4xl font-bold text-white mb-2 flex items-center gap-3">
            <span className="text-5xl">📋</span>
            {title}
          </h1>
          <p className="text-zinc-400">A shared public todo list for everyone</p>
        </div>
        {todoCount > 0 && (
          <div className="text-right">
            <div className="text-3xl font-bold text-emerald-500">
              {completedCount}/{todoCount}
            </div>
            <div className="text-sm text-zinc-400">completed</div>
          </div>
        )}
      </div>
    </header>
  );
};

export default TodoHeader;