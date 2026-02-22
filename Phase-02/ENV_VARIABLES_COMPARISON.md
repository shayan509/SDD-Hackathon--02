# Environment Variables: Old vs New 🔄

## What Changed?

Your old version was a **public todo wall** without authentication.
Your new version is a **private todo app** with email-based authentication.

---

## 🔴 Backend (Render) Changes

### Old Version (Public Todo Wall)
```
DATABASE_URL=postgresql://...
CORS_ORIGINS=http://localhost:3000,https://sdd-hackathon-02-p1.vercel.app
```

### New Version (Private Todo App)
```
DATABASE_URL=postgresql://...
SECRET_KEY=5b93c0f1cbc109e284d4a922fc3b5cb73b97f561150e55668690ce1db72a8f96  ← NEW!
ALGORITHM=HS256                                                              ← NEW!
JWT_EXPIRE_MINUTES=60                                                        ← NEW!
CORS_ORIGINS=http://localhost:3000,https://sdd-hackathon-02-p1.vercel.app
RESET_DB_ON_START=false                                                      ← NEW!
```

### What to Add to Render:
```
✅ Add: SECRET_KEY=5b93c0f1cbc109e284d4a922fc3b5cb73b97f561150e55668690ce1db72a8f96
✅ Add: ALGORITHM=HS256
✅ Add: JWT_EXPIRE_MINUTES=60
✅ Add: RESET_DB_ON_START=false
✅ Keep: DATABASE_URL (same as before)
✅ Keep: CORS_ORIGINS (same as before)
```

---

## 🟢 Frontend (Vercel) Changes

### Old Version (Public Todo Wall)
```
NEXT_PUBLIC_API_BASE_URL=https://sdd-hackathon-02-p2-backend.onrender.com
```

### New Version (Private Todo App)
```
NEXT_PUBLIC_API_BASE_URL=https://sdd-hackathon-02-p2-backend.onrender.com
```

### What to Add to Vercel:
```
✅ Keep: NEXT_PUBLIC_API_BASE_URL (same as before)
```

**No changes needed for frontend!** ✨

---

## 📊 Side-by-Side Comparison

| Variable | Old Version | New Version | Action |
|----------|-------------|-------------|--------|
| **Backend** |
| `DATABASE_URL` | ✅ Required | ✅ Required | Keep same |
| `SECRET_KEY` | ❌ Not needed | ✅ Required | **ADD THIS** |
| `ALGORITHM` | ❌ Not needed | ✅ Required | **ADD THIS** |
| `JWT_EXPIRE_MINUTES` | ❌ Not needed | ✅ Required | **ADD THIS** |
| `CORS_ORIGINS` | ✅ Required | ✅ Required | Keep same |
| `RESET_DB_ON_START` | ❌ Not needed | ⚠️ Optional | **ADD THIS** |
| **Frontend** |
| `NEXT_PUBLIC_API_BASE_URL` | ✅ Required | ✅ Required | Keep same |

---

## 🎯 Quick Action Items

### Render (Backend) - Add 3 Variables
1. Go to Render → Environment
2. Click "Add Environment Variable"
3. Add these:
   - Name: `SECRET_KEY`, Value: `5b93c0f1cbc109e284d4a922fc3b5cb73b97f561150e55668690ce1db72a8f96`
   - Name: `ALGORITHM`, Value: `HS256`
   - Name: `JWT_EXPIRE_MINUTES`, Value: `60`
4. Save Changes

### Vercel (Frontend) - No Changes Needed
✅ Your existing `NEXT_PUBLIC_API_BASE_URL` is correct!

---

## 🔍 Why These New Variables?

### SECRET_KEY
- **Purpose:** Signs JWT authentication tokens
- **Why needed:** Without it, users can't login/signup
- **Security:** Keep this secret! Never share publicly

### ALGORITHM
- **Purpose:** Specifies how JWT tokens are signed
- **Why needed:** Backend needs to know which algorithm to use
- **Value:** HS256 (HMAC with SHA-256)

### JWT_EXPIRE_MINUTES
- **Purpose:** How long tokens are valid
- **Why needed:** Security - tokens expire after 60 minutes
- **Value:** 60 (1 hour)

### RESET_DB_ON_START
- **Purpose:** Clear database on startup
- **Why needed:** Useful for testing, dangerous in production
- **Value:** false (never clear production data!)

---

## ⚠️ Important Notes

### Database Will Be Empty
Since you're adding authentication, the old public todos won't work with the new user-scoped system. The database structure changed:

**Old:** Todos without user ownership
**New:** Todos belong to specific users

**Recommendation:** Set `RESET_DB_ON_START=true` for ONE deployment to clear old data, then set it back to `false`.

### CORS Already Configured
Your CORS is already set up correctly! It allows:
- ✅ `http://localhost:3000` (local development)
- ✅ `https://sdd-hackathon-02-p1.vercel.app` (production)

No changes needed here.

---

## 📋 Copy-Paste Ready

### For Render (Backend)
```
SECRET_KEY=5b93c0f1cbc109e284d4a922fc3b5cb73b97f561150e55668690ce1db72a8f96
ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60
RESET_DB_ON_START=false
```

### For Vercel (Frontend)
```
No changes needed! ✅
```

---

## ✅ Verification Checklist

After adding variables:

**Backend:**
- [ ] SECRET_KEY added
- [ ] ALGORITHM added
- [ ] JWT_EXPIRE_MINUTES added
- [ ] RESET_DB_ON_START added
- [ ] Deployment successful
- [ ] Visit /docs endpoint - see auth endpoints

**Frontend:**
- [ ] NEXT_PUBLIC_API_BASE_URL still correct
- [ ] Deployment successful
- [ ] Can access login page
- [ ] Can create account

---

## 🎊 Summary

**What you need to add:**
- 3 new backend variables (SECRET_KEY, ALGORITHM, JWT_EXPIRE_MINUTES)
- 0 new frontend variables (already correct!)

**Total time:** ~5 minutes
**Difficulty:** Easy - just copy and paste!

Your production app will have full authentication after this! 🚀
