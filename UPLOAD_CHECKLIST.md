# 📋 Cloud Shell Upload Checklist

## Files to Upload to Cloud Shell

Upload these files to your `~/tarot-reader` directory in Cloud Shell:

### ✅ Backend & Config Files
- [ ] `tarot_app.py` (UPDATED - now serves PWA files)
- [ ] `requirements.txt`
- [ ] `Dockerfile`
- [ ] `docker-compose.yml`
- [ ] `.dockerignore`

### ✅ Frontend Files
- [ ] `tarot_frontend.html` (UPDATED - now has PWA support)

### ✅ PWA Files (NEW!)
- [ ] `manifest.json` - PWA configuration
- [ ] `service-worker.js` - Offline support
- [ ] `icon-192.png` - App icon (small)
- [ ] `icon-512.png` - App icon (large)

### ✅ Optional
- [ ] `deploy-pwa.sh` - Quick deploy script
- [ ] `PWA_INSTALL_GUIDE.md` - Installation guide
- [ ] `README.md` - Documentation

---

## 🚀 Upload Methods

### Method 1: Upload via Cloud Shell UI (EASIEST)

1. Open Cloud Shell: https://console.cloud.google.com
2. Click the **three-dot menu** (⋮) in Cloud Shell
3. Click **"Upload"**
4. Select all files above
5. They'll be uploaded to your home directory

### Method 2: Upload via GitHub (if you pushed to GitHub)

```bash
cd ~
git clone https://github.com/maggiesummerxia/tarot-reader.git
cd tarot-reader
```

### Method 3: Use Cloud Shell Editor

1. In Cloud Shell, click **"Open Editor"** button
2. Create files manually and paste content
3. Save each file

---

## 📦 Verify Files

After uploading, run this in Cloud Shell:

```bash
cd ~/tarot-reader
ls -la
```

You should see all the files listed above.

---

## 🚀 Deploy

Once all files are uploaded:

```bash
cd ~/tarot-reader
bash deploy-pwa.sh
```

Or manually:

```bash
gcloud run deploy tarot-reader \
  --source . \
  --platform managed \
  --region europe-west2 \
  --allow-unauthenticated \
  --port 5000
```

---

## 🎯 Quick Start (All-in-One)

If you have all files in a local folder, zip them first:

1. **On your Mac:** Right-click folder → "Compress"
2. **In Cloud Shell:** Upload the zip file
3. **Unzip in Cloud Shell:**
   ```bash
   cd ~
   unzip tarot-reader.zip
   cd tarot-reader
   bash deploy-pwa.sh
   ```

Done! 🎉
