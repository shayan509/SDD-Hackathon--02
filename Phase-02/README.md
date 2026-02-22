# Secure Todo App (Phase-02)

Todo application with account authentication, user-owned data isolation, and Neon-backed persistence.

## Stack

- Backend: FastAPI + SQLModel + Neon Postgres
- Frontend: Next.js + React + Tailwind
- Runtime: Windows 11 development

## Core Security Guarantees

- All `/api/todos/*` endpoints require authentication.
- Users can only read/update/delete their own todo items.
- Passwords are stored hashed, never plaintext.
- JWT secrets and DB credentials are environment-only.
- Neon connection requires SSL.

## Local Setup (PowerShell)

1. Backend:
   - `cd backend`
   - `pip install -r requirements.txt`
   - Copy `.env.example` to `.env` and set values (`DATABASE_URL`, `SECRET_KEY`, `ALGORITHM`).
   - `uvicorn main:app --reload --port 8000`
2. Frontend:
   - `cd frontend`
   - `npm install`
   - Copy `.env.example` to `.env.local` and set `NEXT_PUBLIC_API_BASE_URL=http://localhost:8000`
   - `npm run dev`

## API Endpoints

- `POST /api/auth/signup`
- `POST /api/auth/login`
- `GET /api/todos/`
- `POST /api/todos/`
- `PATCH /api/todos/{id}`
- `DELETE /api/todos/{id}`

## Cleanup Scope

Obsolete artifacts targeted for removal in this feature:

- Legacy local DB files (`backend/test.db`, `backend/todo.db`)
- Root `docker-compose.yml` and phase-1 boilerplate files that are not used by active backend/frontend runtime
