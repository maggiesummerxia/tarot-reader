# 📱 PWA Deployment & Installation Guide

Your Tarot Card Reader is now a Progressive Web App (PWA)! This means you can install it on your phone like a native app.

## 🚀 Deploy Updated PWA to Cloud Run

### From Cloud Shell:

```bash
# Navigate to your project
cd ~/tarot-reader

# Upload the new PWA files (if not already there):
# - manifest.json
# - service-worker.js
# - icon-192.png
# - icon-512.png
# - tarot_app.py (updated)
# - tarot_frontend.html (updated)

# Redeploy to Cloud Run
gcloud run deploy tarot-reader \
  --source . \
  --platform managed \
  --region europe-west2 \
  --allow-unauthenticated \
  --port 5000
```

Wait 2-3 minutes for deployment to complete.

---

## 📱 Install on Your Android Phone

### Step 1: Open in Chrome
1. Open **Chrome browser** on your Android phone
2. Go to: `https://tarot-reader-85429130230.europe-west2.run.app`

### Step 2: Install the App
You'll see one of these options:

**Option A: Install Banner**
- A banner will appear saying "Add Tarot Card Reader to Home screen"
- Tap **"Add"** or **"Install"**

**Option B: Manual Install**
1. Tap the **three-dot menu** (⋮) in Chrome
2. Tap **"Add to Home screen"** or **"Install app"**
3. Tap **"Add"** or **"Install"**

### Step 3: Use Like a Native App
- App icon appears on your home screen 🔮
- Opens in full-screen (no browser bars)
- Works offline (after first visit)
- Feels like a native app!

---

## 🍎 Install on iPhone (iOS)

### Using Safari:
1. Open **Safari** browser (not Chrome)
2. Go to: `https://tarot-reader-85429130230.europe-west2.run.app`
3. Tap the **Share button** (square with arrow)
4. Scroll down and tap **"Add to Home Screen"**
5. Tap **"Add"**

---

## 💻 Install on Desktop

### Chrome/Edge:
1. Visit your app URL
2. Look for the **install icon** (⊕) in the address bar
3. Click it and select **"Install"**

---

## ✨ PWA Features

Your app now has:
- ✅ **Installable** - Add to home screen like a real app
- ✅ **Offline support** - Works without internet (after first visit)
- ✅ **Full-screen mode** - No browser UI when opened
- ✅ **App icon** - Custom tarot-themed icon
- ✅ **Fast loading** - Cached for instant loading
- ✅ **Push notifications ready** - (can be added later)

---

## 🔧 Verify PWA Installation

### Check if PWA is working:
1. Open Chrome DevTools on desktop
2. Go to **Application** tab
3. Check **Manifest** - should show your app details
4. Check **Service Workers** - should show "activated and running"

### Test offline mode:
1. Install the app on your phone
2. Open it once (to cache files)
3. Turn on Airplane mode
4. Open the app - it should still work! ✨

---

## 📦 New Files Added

- `manifest.json` - PWA configuration (name, icons, theme)
- `service-worker.js` - Handles offline caching
- `icon-192.png` - App icon (192x192)
- `icon-512.png` - App icon (512x512)
- Updated `tarot_app.py` - Serves PWA files
- Updated `tarot_frontend.html` - Registers service worker

---

## 🎯 Quick Deploy Script

Copy-paste this into Cloud Shell to update everything:

```bash
cd ~/tarot-reader

# Make sure all files are present
ls -la

# Deploy
gcloud run deploy tarot-reader \
  --source . \
  --platform managed \
  --region europe-west2 \
  --allow-unauthenticated \
  --port 5000

# Get the URL
gcloud run services describe tarot-reader \
  --region europe-west2 \
  --format 'value(status.url)'
```

---

## 🐛 Troubleshooting

**"Add to Home Screen" doesn't appear:**
- Make sure you're using HTTPS (Cloud Run uses HTTPS by default)
- Try Chrome browser specifically
- Clear browser cache and reload

**App doesn't work offline:**
- Visit the app once while online (to cache files)
- Service worker needs time to activate (wait 10 seconds, reload)

**Icon doesn't show:**
- Icons should load automatically
- If not, check that icon files were deployed

---

## 🎉 You're Done!

You now have a fully functional PWA that:
- Runs on Google Cloud (europe-west2)
- Installs like a native app
- Works on Android, iOS, and Desktop
- Functions offline
- Costs $0/month (within free tier)

Enjoy your mystical tarot readings! 🔮✨
