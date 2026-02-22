# Login Troubleshooting Guide

## Issue: "Invalid username or password" Error

### Current Database Status
- **Total Users:** 1
- **Existing Username:** `shayan`

### Why This Error Occurs

The error happens when:
1. ❌ Username doesn't exist in the database
2. ❌ Password doesn't match the stored hash
3. ❌ Extra spaces in username (now fixed - we trim whitespace)

### Solutions

#### Option 1: Use Existing Account
If you created the "shayan" account:
- Username: `shayan`
- Password: (the password you used during signup)

#### Option 2: Create New Account
1. Go to http://localhost:3000/signup
2. Enter a new username (min 3 characters)
3. Enter a password (min 8 characters)
4. Click "Sign up"
5. You'll be redirected to login
6. Login with your new credentials

#### Option 3: Reset Database (Start Fresh)
If you forgot your password or want to start over:

1. Stop the backend server
2. Edit `backend/.env` and set:
   ```
   RESET_DB_ON_START=true
   ```
3. Restart the backend server (it will clear all users)
4. Edit `backend/.env` and set back to:
   ```
   RESET_DB_ON_START=false
   ```
5. Go to signup and create a new account

### Testing Your Credentials

To test if specific credentials work, run:

```bash
cd backend
python test_auth.py
```

This will show all users in the database.

### Common Mistakes

1. **Case Sensitivity:** Usernames are case-sensitive
   - "Shayan" ≠ "shayan"

2. **Spaces:** Extra spaces in username or password
   - " shayan " ≠ "shayan" (now fixed with trim)

3. **Wrong Password:** Make sure you're using the exact password from signup

4. **Account Doesn't Exist:** You must signup before login

### Improved Error Messages

I've updated the frontend to show more specific error messages from the backend. Now you'll see:
- "Invalid username or password" (from backend)
- Or any other specific error message

### Current Server Status

✅ Backend: http://localhost:8000
✅ Frontend: http://localhost:3000

### Next Steps

1. Try logging in with username: `shayan` and your password
2. If you don't remember the password, create a new account
3. If still having issues, check the backend logs for more details
