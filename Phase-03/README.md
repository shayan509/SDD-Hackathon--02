# Public Todo MVP

A public todo list application with a FastAPI backend connected to Neon Postgres database and a Next.js frontend. The application allows users to create, view, toggle completion status, and delete todo items in a shared public list.

## Features

- Create new todo items
- View all todo items in a public list
- Toggle completion status of todo items
- Delete todo items
- Responsive design with dark theme

## Tech Stack

- Backend: FastAPI, SQLModel, Neon Postgres
- Frontend: Next.js 14, TypeScript, Tailwind CSS
- Database: Neon Postgres with SSL connection

## Setup

1. Clone the repository
2. Navigate to the backend directory and install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
3. Set up environment variables in a `.env` file:
   ```
   DATABASE_URL=postgresql://username:password@ep-xxxxxx.us-east-1.aws.neon.tech/dbname?sslmode=require
   ```
4. Navigate to the frontend directory and install dependencies:
   ```bash
   cd frontend
   npm install
   ```
5. Run the backend:
   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
   ```
6. Run the frontend:
   ```bash
   cd frontend
   npm run dev
   ```

## API Endpoints

- `GET /api/todos` - Get all todo items
- `POST /api/todos` - Create a new todo item
- `PATCH /api/todos/{id}` - Update a todo item (toggle status)
- `DELETE /api/todos/{id}` - Delete a todo item

## Visual Design

- Primary Color: #10b981 (Emerald-500)
- Background: #09090b (Zinc-950)
- Surface: #18181b (Zinc-900)
- Font: System Sans-Serif