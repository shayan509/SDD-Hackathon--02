"use client";

import Link from 'next/link';
import { useRouter } from 'next/navigation';
import { FormEvent, useState } from 'react';
import { toast } from 'react-toastify';

import { signup } from '@/src/lib/api';

export default function SignupPage() {
  const router = useRouter();
  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setLoading(true);

    try {
      await signup(email.trim(), username.trim(), password);
      toast.success('Account created successfully! Please login.');
      router.replace('/login');
    } catch (err) {
      console.error(err);
      const errorMessage = err instanceof Error ? err.message : 'Signup failed. Please try again.';
      toast.error(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gradient-to-br from-zinc-950 via-zinc-900 to-zinc-950 text-zinc-100 flex items-center justify-center p-6">
      <div className="w-full max-w-md rounded-2xl border border-zinc-700/70 bg-zinc-900/80 shadow-2xl shadow-black/30 backdrop-blur-sm p-8">
        <h1 className="text-3xl font-semibold tracking-tight">Create account</h1>
        <p className="mt-2 text-sm text-zinc-400">Register to start managing your own todos.</p>

        <form className="mt-6 space-y-4" onSubmit={handleSubmit}>
          <div>
            <label className="block text-sm text-zinc-300 mb-1" htmlFor="email">Email</label>
            <input
              id="email"
              type="email"
              className="w-full rounded-lg border border-zinc-700 bg-zinc-950 px-3 py-2 outline-none focus:ring-2 focus:ring-emerald-500"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="you@example.com"
              required
            />
          </div>
          <div>
            <label className="block text-sm text-zinc-300 mb-1" htmlFor="username">Username</label>
            <input
              id="username"
              className="w-full rounded-lg border border-zinc-700 bg-zinc-950 px-3 py-2 outline-none focus:ring-2 focus:ring-emerald-500"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              placeholder="johndoe"
              required
              minLength={3}
            />
            <p className="text-xs text-zinc-500 mt-1">At least 3 characters</p>
          </div>
          <div>
            <label className="block text-sm text-zinc-300 mb-1" htmlFor="password">Password</label>
            <input
              id="password"
              type="password"
              className="w-full rounded-lg border border-zinc-700 bg-zinc-950 px-3 py-2 outline-none focus:ring-2 focus:ring-emerald-500"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="••••••••"
              required
              minLength={8}
            />
            <p className="text-xs text-zinc-500 mt-1">At least 8 characters</p>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full rounded-lg bg-emerald-500 px-4 py-2 font-medium text-zinc-950 hover:bg-emerald-400 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {loading ? 'Creating account...' : 'Sign up'}
          </button>
        </form>

        <p className="mt-6 text-sm text-zinc-400">
          Already have an account?{' '}
          <Link href="/login" className="text-emerald-400 hover:text-emerald-300">
            Login
          </Link>
        </p>
      </div>
    </main>
  );
}
