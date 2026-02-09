# Quickstart Guide: Public Todo MVP

## Prerequisites

- Python 3.11+
- Node.js 18+
- Poetry (for Python dependency management) or pip
- Access to a Neon Postgres database instance
- PowerShell (for Windows-specific commands)

## Setup Instructions

### 1. Clone and Navigate to Project

```powershell
git clone <repository-url>
cd <project-directory>
git checkout 001-public-todo-mvp
```

### 2. Backend Setup

#### Install Python Dependencies

```powershell
cd backend
pip install -r requirements.txt
# OR if using poetry
poetry install
```

#### Set Up Environment Variables

Create a `.env` file in the project root with your Neon database URL:

```env
DATABASE_URL=postgresql://username:password@ep-xxxxxx.us-east-1.aws.neon.tech/dbname?sslmode=require
```

### 3. Frontend Setup

```powershell
cd frontend
npm install
# OR
pnpm install
```

### 4. Run the Application

#### Backend (FastAPI)

```powershell
cd backend
uvicorn main:app --reload --port 8000
```

#### Frontend (SvelteKit)

```powershell
cd frontend
npm run dev
# OR
pnpm run dev
```

The application will be accessible at `http://localhost:5173`.

## Development Commands

### Backend Commands

```powershell
# Run tests
cd backend
pytest

# Format code
black .

# Lint code
flake8 .
```

### Frontend Commands

```powershell
# Build for production
cd frontend
npm run build

# Preview production build
npm run preview

# Run tests
npm run test
```

## File Cleanup (Windows)

If you need to clean up build artifacts and dependencies:

```powershell
# From project root
Remove-Item -Recurse -Force .next, node_modules, .svelte-kit, test.db
```

## Troubleshooting

1. **SSL Connection Issues**: Ensure your database connection string includes `sslmode=require`
2. **Port Conflicts**: Change ports in configuration if 8000 or 5173 are in use
3. **Dependency Issues**: Clean install by removing node_modules and reinstalling