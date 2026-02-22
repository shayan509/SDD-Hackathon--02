import React from 'react';

interface TodoHeaderProps {
  title?: string;
  todoCount?: number;
  completedCount?: number;
  onLogout?: () => void;
}

const TodoHeader: React.FC<TodoHeaderProps> = ({
  title = 'My Todo Wall',
  todoCount = 0,
  completedCount = 0,
  onLogout,
}) => {
  return (
    <header className="mb-8">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-4xl font-bold text-white mb-2">{title}</h1>
          <p className="text-zinc-400">A personal todo list for your account</p>
        </div>
        <div className="flex items-center gap-4">
          {todoCount > 0 && (
            <div className="text-right">
              <div className="text-3xl font-bold text-emerald-500">
                {completedCount}/{todoCount}
              </div>
              <div className="text-sm text-zinc-400">completed</div>
            </div>
          )}
          {onLogout && (
            <button
              type="button"
              onClick={onLogout}
              className="px-4 py-2 text-sm rounded-lg border border-emerald-700 bg-emerald-900/40 text-emerald-100 hover:bg-emerald-800/50 transition-colors"
            >
              Logout
            </button>
          )}
        </div>
      </div>
    </header>
  );
};

export default TodoHeader;
