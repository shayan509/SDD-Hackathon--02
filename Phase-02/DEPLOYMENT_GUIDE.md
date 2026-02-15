# Deployment Guide

This guide explains how to properly configure environment variables for local development and production deployment.

## Architecture

- **Frontend**: Next.js deployed on Vercel
  - Production URL: https://sdd-hackathon-02-p1.vercel.app
- **Backend**: FastAPI deployed on Render
  - Production URL: https://sdd-hackathon-02-p2-backend.onrender.com
- **Database**: Neon PostgreSQL (serverless)

## Local Development Setup

### Backend (FastAPI)

1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Create/verify `.env` file:
   ```env
   DATABASE_URL=postgresql://neondb_owner:npg_MTgFKa9zL2ju@ep-rough-bird-aiacc6wu-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
   CORS_ORIGINS=http://localhost:3000,https://sdd-hackathon-02-p1.vercel.app
   ```

3. Install dependencies and run:
   ```bash
   pip install -r requirements.txt
   uvicorn main:app --reload --port 8000
   ```

4. Backend will be available at: http://localhost:8000

### Frontend (Next.js)

1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Create/verify `.env.local` file:
   ```env
   NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
   ```

3. Install dependencies and run:
   ```bash
   npm install
   npm run dev
   ```

4. Frontend will be available at: http://localhost:3000

## Production Deployment

### Backend on Render

1. Go to your Render dashboard
2. Select your FastAPI service
3. Navigate to "Environment" section
4. Add the following environment variables:

   ```
   DATABASE_URL=postgresql://neondb_owner:npg_MTgFKa9zL2ju@ep-rough-bird-aiacc6wu-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
   CORS_ORIGINS=http://localhost:3000,https://sdd-hackathon-02-p1.vercel.app
   ```

5. Save and redeploy

### Frontend on Vercel

1. Go to your Vercel dashboard
2. Select your Next.js project
3. Navigate to "Settings" → "Environment Variables"
4. Add the following environment variable:

   ```
   NEXT_PUBLIC_API_BASE_URL=https://sdd-hackathon-02-p2-backend.onrender.com
   ```

5. Redeploy your application

## API Endpoints

All API endpoints are prefixed with `/api`:

- `GET /api/todos/` - Get all todos
- `POST /api/todos/` - Create a new todo
- `PATCH /api/todos/{id}` - Update todo status
- `DELETE /api/todos/{id}` - Delete a todo

## CORS Configuration

The backend is configured to accept requests from:
- `http://localhost:3000` (local development)
- `https://sdd-hackathon-02-p1.vercel.app` (production frontend)

To add more origins, update the `CORS_ORIGINS` environment variable with comma-separated URLs.

## Troubleshooting

### Frontend can't connect to backend

1. Check that `NEXT_PUBLIC_API_BASE_URL` is set correctly
2. Verify the backend URL is accessible
3. Check browser console for CORS errors

### CORS errors

1. Verify frontend URL is in backend's `CORS_ORIGINS`
2. Ensure no trailing slashes in URLs
3. Check that environment variables are loaded correctly

### Database connection issues

1. Verify `DATABASE_URL` is correct
2. Check Neon database is active
3. Ensure connection string includes `sslmode=require`

## Environment Variables Summary

### Backend (.env)
- `DATABASE_URL` - PostgreSQL connection string
- `CORS_ORIGINS` - Comma-separated list of allowed origins

### Frontend (.env.local for dev, Vercel settings for prod)
- `NEXT_PUBLIC_API_BASE_URL` - Backend API URL

## Notes

- Never commit `.env` or `.env.local` files to git
- Use `.env.example` files as templates
- Environment variables starting with `NEXT_PUBLIC_` are exposed to the browser
- Backend environment variables are server-side only
