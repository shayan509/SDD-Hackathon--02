# Deployment Guide

## Required Environment Variables

### Backend

- `DATABASE_URL` (Neon Postgres URL with `sslmode=require`)
- `SECRET_KEY` (strong random secret)
- `ALGORITHM` (example: `HS256`)
- `JWT_EXPIRE_MINUTES` (example: `60`)
- `CORS_ORIGINS` (comma-separated allowed frontend origins)
- `RESET_DB_ON_START` (`false` in production)

### Frontend

- `NEXT_PUBLIC_API_BASE_URL` (public backend URL)

## Fresh Deploy Schema Initialization

- Startup runs `SQLModel.metadata.create_all(...)`.
- Optional one-time reset is available with `RESET_DB_ON_START=true` for non-production environments.
- Manual schema init command:
  - `python migrate_db.py`
  - Optional reset: `python migrate_db.py --reset`

## Production Security Checklist

- Do not hardcode database credentials or JWT secrets.
- Keep `RESET_DB_ON_START=false` in production.
- Restrict `CORS_ORIGINS` to known frontend domains only.
- Verify authentication is required for all todo CRUD endpoints.
- Verify users cannot access other users' todo records.
