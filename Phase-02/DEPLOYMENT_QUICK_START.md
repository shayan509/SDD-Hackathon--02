# Quick Deployment Guide ⚡

## TL;DR - What You Need to Add

### 🔴 Render (Backend) - Add These 3 NEW Variables

```
SECRET_KEY=5b93c0f1cbc109e284d4a922fc3b5cb73b97f561150e55668690ce1db72a8f96
ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60
```

**And update this existing one:**
```
CORS_ORIGINS=http://localhost:3000,https://sdd-hackathon-02-p1.vercel.app
```

### 🟢 Vercel (Frontend) - Already Correct

```
NEXT_PUBLIC_API_BASE_URL=https://sdd-hackathon-02-p2-backend.onrender.com
```

---

## 🎯 5-Minute Deployment

### Step 1: Update Render (2 minutes)

1. Go to https://dashboard.render.com
2. Select your backend service
3. Click "Environment"
4. Add these 3 NEW variables:
   - `SECRET_KEY` → `5b93c0f1cbc109e284d4a922fc3b5cb73b97f561150e55668690ce1db72a8f96`
   - `ALGORITHM` → `HS256`
   - `JWT_EXPIRE_MINUTES` → `60`
5. Update `CORS_ORIGINS` → `http://localhost:3000,https://sdd-hackathon-02-p1.vercel.app`
6. Click "Save Changes"
7. Wait for auto-deploy

### Step 2: Verify Vercel (1 minute)

1. Go to https://vercel.com/dashboard
2. Select your project
3. Settings → Environment Variables
4. Verify `NEXT_PUBLIC_API_BASE_URL` = `https://sdd-hackathon-02-p2-backend.onrender.com`
5. If correct, you're done! If not, update it and redeploy.

### Step 3: Test (2 minutes)

1. Visit https://sdd-hackathon-02-p1.vercel.app
2. Click "Create one"
3. Signup with email, username, password
4. Login
5. Done! 🎉

---

## 📋 Complete Variable Lists

### Render Environment Variables (Copy-Paste Ready)

```
DATABASE_URL=postgresql://neondb_owner:npg_MTgFKa9zL2ju@ep-rough-bird-aiacc6wu-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
SECRET_KEY=5b93c0f1cbc109e284d4a922fc3b5cb73b97f561150e55668690ce1db72a8f96
ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60
CORS_ORIGINS=http://localhost:3000,https://sdd-hackathon-02-p1.vercel.app
RESET_DB_ON_START=false
```

### Vercel Environment Variables (Copy-Paste Ready)

```
NEXT_PUBLIC_API_BASE_URL=https://sdd-hackathon-02-p2-backend.onrender.com
```

---

## ⚠️ Important Notes

### What Changed from Old Version?

**Old Version (Public Todo Wall):**
- No authentication
- No email field
- No JWT tokens
- Public todos for everyone

**New Version (Private Todo App):**
- ✅ Email-based authentication
- ✅ JWT tokens (needs SECRET_KEY)
- ✅ User-scoped todos
- ✅ Toast notifications

### Why These New Variables?

| Variable | Why It's Needed |
|----------|----------------|
| `SECRET_KEY` | Signs JWT tokens for authentication |
| `ALGORITHM` | Specifies JWT signing algorithm |
| `JWT_EXPIRE_MINUTES` | Sets token expiration time |

Without these, authentication won't work!

---

## 🔍 How to Check If It's Working

### Backend Check
Visit: https://sdd-hackathon-02-p2-backend.onrender.com/docs

You should see:
- ✅ `/api/auth/signup` endpoint
- ✅ `/api/auth/login` endpoint
- ✅ `/api/todos/` endpoints (with lock icon = protected)

### Frontend Check
Visit: https://sdd-hackathon-02-p1.vercel.app

You should:
- ✅ Be redirected to login page
- ✅ See "Create one" link
- ✅ Be able to signup with email
- ✅ Be able to login
- ✅ See toast notifications

### CORS Check
Open browser console (F12) on frontend:
- ✅ No CORS errors
- ✅ API requests succeed

---

## 🐛 Common Issues

### "Missing SECRET_KEY" Error
**Fix:** Add the SECRET_KEY variable to Render

### CORS Error in Browser
**Fix:** Make sure CORS_ORIGINS includes your Vercel URL

### "Invalid email or password"
**Fix:** Database might be empty. Create a new account first.

### Frontend Can't Connect
**Fix:** Check NEXT_PUBLIC_API_BASE_URL is correct (no trailing slash!)

---

## ✅ Deployment Checklist

**Render (Backend):**
- [ ] Add SECRET_KEY
- [ ] Add ALGORITHM
- [ ] Add JWT_EXPIRE_MINUTES
- [ ] Update CORS_ORIGINS
- [ ] Save and wait for deploy

**Vercel (Frontend):**
- [ ] Verify NEXT_PUBLIC_API_BASE_URL
- [ ] Redeploy if needed

**Testing:**
- [ ] Visit frontend URL
- [ ] Create account
- [ ] Login
- [ ] Create todo
- [ ] All working!

---

## 🎊 That's It!

Your production app is now live with full authentication!

**Frontend:** https://sdd-hackathon-02-p1.vercel.app
**Backend:** https://sdd-hackathon-02-p2-backend.onrender.com
