# Production Deployment Guide 🚀

## Overview

Your app is now production-ready with:
- ✅ Email-based authentication
- ✅ JWT tokens with expiration
- ✅ User-scoped todos
- ✅ Toast notifications
- ✅ CORS configured for production

## Deployment URLs

**Frontend (Vercel):** https://sdd-hackathon-02-p1.vercel.app
**Backend (Render):** https://sdd-hackathon-02-p2-backend.onrender.com

---

## 🔧 Backend Deployment (Render)

### Environment Variables to Add/Update

Go to your Render dashboard → Your service → Environment

#### ✅ Existing Variables (Keep These)
```
DATABASE_URL=postgresql://neondb_owner:npg_MTgFKa9zL2ju@ep-rough-bird-aiacc6wu-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
```

#### 🆕 NEW Variables to Add (Required for Authentication)
```
SECRET_KEY=5b93c0f1cbc109e284d4a922fc3b5cb73b97f561150e55668690ce1db72a8f96
ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60
```

#### 🔄 Update This Variable
```
CORS_ORIGINS=http://localhost:3000,https://sdd-hackathon-02-p1.vercel.app
```

#### ⚠️ Optional (Use with Caution)
```
RESET_DB_ON_START=false
```
**Note:** Set to `true` ONLY if you want to clear all data on next deployment. Set back to `false` immediately after.

### Complete Backend Environment Variables

Copy and paste these into Render:

```
DATABASE_URL=postgresql://neondb_owner:npg_MTgFKa9zL2ju@ep-rough-bird-aiacc6wu-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
SECRET_KEY=5b93c0f1cbc109e284d4a922fc3b5cb73b97f561150e55668690ce1db72a8f96
ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60
CORS_ORIGINS=http://localhost:3000,https://sdd-hackathon-02-p1.vercel.app
RESET_DB_ON_START=false
```

### What Each Variable Does

| Variable | Purpose | Required |
|----------|---------|----------|
| `DATABASE_URL` | Neon PostgreSQL connection | ✅ Yes |
| `SECRET_KEY` | JWT token signing key | ✅ Yes (NEW!) |
| `ALGORITHM` | JWT algorithm (HS256) | ✅ Yes (NEW!) |
| `JWT_EXPIRE_MINUTES` | Token expiration time | ✅ Yes (NEW!) |
| `CORS_ORIGINS` | Allowed frontend URLs | ✅ Yes |
| `RESET_DB_ON_START` | Clear DB on startup | ⚠️ Optional |

---

## 🎨 Frontend Deployment (Vercel)

### Environment Variables to Add/Update

Go to your Vercel dashboard → Your project → Settings → Environment Variables

#### 🔄 Update This Variable

**Variable Name:**
```
NEXT_PUBLIC_API_BASE_URL
```

**Value:**
```
https://sdd-hackathon-02-p2-backend.onrender.com
```

**Important:** Make sure there's NO trailing slash!

### Complete Frontend Environment Variables

You only need ONE variable:

```
NEXT_PUBLIC_API_BASE_URL=https://sdd-hackathon-02-p2-backend.onrender.com
```

---

## 📋 Step-by-Step Deployment

### Backend (Render)

1. **Go to Render Dashboard**
   - Navigate to: https://dashboard.render.com
   - Select your backend service

2. **Update Environment Variables**
   - Click "Environment" in the left sidebar
   - Add these NEW variables:
     - `SECRET_KEY` = `5b93c0f1cbc109e284d4a922fc3b5cb73b97f561150e55668690ce1db72a8f96`
     - `ALGORITHM` = `HS256`
     - `JWT_EXPIRE_MINUTES` = `60`
   - Update existing:
     - `CORS_ORIGINS` = `http://localhost:3000,https://sdd-hackathon-02-p1.vercel.app`

3. **Save and Deploy**
   - Click "Save Changes"
   - Render will automatically redeploy
   - Wait for deployment to complete (~2-5 minutes)

4. **Verify Deployment**
   - Visit: https://sdd-hackathon-02-p2-backend.onrender.com/docs
   - You should see the FastAPI documentation
   - Check for `/api/auth/signup` and `/api/auth/login` endpoints

### Frontend (Vercel)

1. **Go to Vercel Dashboard**
   - Navigate to: https://vercel.com/dashboard
   - Select your project

2. **Update Environment Variables**
   - Go to Settings → Environment Variables
   - Find `NEXT_PUBLIC_API_BASE_URL`
   - Update value to: `https://sdd-hackathon-02-p2-backend.onrender.com`
   - Make sure it applies to: Production, Preview, and Development

3. **Redeploy**
   - Go to Deployments tab
   - Click "..." on the latest deployment
   - Click "Redeploy"
   - OR: Push a new commit to trigger deployment

4. **Verify Deployment**
   - Visit: https://sdd-hackathon-02-p1.vercel.app
   - You should be redirected to login page
   - Try creating an account

---

## 🔒 Security Notes

### SECRET_KEY
- This is used to sign JWT tokens
- Keep it secret and secure
- Never commit to git
- Current key is randomly generated and secure

### CORS_ORIGINS
- Only allows requests from specified domains
- Prevents unauthorized access
- Currently allows:
  - `http://localhost:3000` (local development)
  - `https://sdd-hackathon-02-p1.vercel.app` (production frontend)

---

## 🧪 Testing Production Deployment

### 1. Test Backend API
```bash
# Test signup endpoint
curl -X POST https://sdd-hackathon-02-p2-backend.onrender.com/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","username":"testuser","password":"password123"}'

# Should return: {"id":"...","email":"test@example.com","username":"testuser"}
```

### 2. Test Frontend
1. Visit: https://sdd-hackathon-02-p1.vercel.app
2. Click "Create one" to signup
3. Enter email, username, password
4. Should see success toast
5. Login with credentials
6. Should access dashboard

### 3. Test CORS
- Open browser console on frontend
- Check for CORS errors
- Should see no errors if configured correctly

---

## 🐛 Troubleshooting

### Backend Issues

**Problem:** "Missing SECRET_KEY or ALGORITHM"
- **Solution:** Add the new environment variables to Render

**Problem:** CORS errors in browser
- **Solution:** Check `CORS_ORIGINS` includes your Vercel URL

**Problem:** Database connection errors
- **Solution:** Verify `DATABASE_URL` is correct

### Frontend Issues

**Problem:** "Failed to fetch" errors
- **Solution:** Check `NEXT_PUBLIC_API_BASE_URL` is correct

**Problem:** Login/Signup not working
- **Solution:** Verify backend is deployed and running

**Problem:** Toast notifications not showing
- **Solution:** Clear browser cache and reload

---

## 📊 Deployment Checklist

### Before Deploying

- [ ] All code committed to git
- [ ] Environment variables documented
- [ ] Database backup (if needed)
- [ ] Test locally one more time

### Backend Deployment

- [ ] Add `SECRET_KEY` to Render
- [ ] Add `ALGORITHM` to Render
- [ ] Add `JWT_EXPIRE_MINUTES` to Render
- [ ] Update `CORS_ORIGINS` to Render
- [ ] Save and wait for deployment
- [ ] Test API endpoints

### Frontend Deployment

- [ ] Update `NEXT_PUBLIC_API_BASE_URL` in Vercel
- [ ] Redeploy frontend
- [ ] Test signup flow
- [ ] Test login flow
- [ ] Test todo operations

### Post-Deployment

- [ ] Create test account
- [ ] Test all features
- [ ] Check browser console for errors
- [ ] Verify toast notifications work
- [ ] Test on mobile device

---

## 🎉 Success Criteria

Your deployment is successful when:

✅ Backend API responds at `/docs`
✅ Frontend loads without errors
✅ Can create new account
✅ Can login with email/password
✅ Can create/edit/delete todos
✅ Toast notifications appear
✅ No CORS errors in console
✅ Logout works correctly

---

## 📞 Quick Reference

### Backend Environment Variables (6 total)
```
DATABASE_URL=<your-neon-db-url>
SECRET_KEY=5b93c0f1cbc109e284d4a922fc3b5cb73b97f561150e55668690ce1db72a8f96
ALGORITHM=HS256
JWT_EXPIRE_MINUTES=60
CORS_ORIGINS=http://localhost:3000,https://sdd-hackathon-02-p1.vercel.app
RESET_DB_ON_START=false
```

### Frontend Environment Variables (1 total)
```
NEXT_PUBLIC_API_BASE_URL=https://sdd-hackathon-02-p2-backend.onrender.com
```

---

## 🚀 Ready to Deploy!

Follow the steps above and your production app will be live with full authentication!
