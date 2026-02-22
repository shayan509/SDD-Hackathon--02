# Quickstart: Todo Security Hardening

## 1. Prerequisites
- Windows 11
- Python 3.13
- Node.js LTS
- Neon database URL with SSL enabled

## 2. Configure Environment
1. Backend environment:
   - Set database connection string in backend environment file.
   - Set token signing secret and algorithm via environment variables.
   - Ensure no hardcoded secrets remain in code.
2. Frontend environment:
   - Configure API base URL to backend.

## 3. Install Dependencies
```powershell
cd C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\backend
pip install -r requirements.txt
cd C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\frontend
npm install
```

## 4. Start Services
```powershell
cd C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\backend
uvicorn main:app --reload
cd C:\Users\icon\Desktop\SDD-Hackathon--02\Phase-02\frontend
npm run dev
```

## 5. Validate Security Criteria
1. Signup and login succeed for a new user.
2. Unauthenticated call to todo endpoints returns authorization failure.
3. User A cannot read/update/delete User B todo items.
4. Fresh environment can initialize required user and todo schema.

## 6. Validate Maintainability Criteria
1. Confirm only active `backend/` and `frontend/` app paths are used.
2. Confirm obsolete Docker and phase-1 boilerplate artifacts are removed from scoped cleanup list.
3. Confirm Modern Night theme is preserved in authentication and todo screens.