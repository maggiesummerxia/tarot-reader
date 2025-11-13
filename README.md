# 🔮 Tarot Card Reader

A beautiful, full-stack tarot card reading application with Progressive Web App (PWA) support. Draw tarot cards with upright and reversed orientations.

[![Deploy to Cloud Run](https://img.shields.io/badge/Deploy%20to-Cloud%20Run-blue)](https://console.cloud.google.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-brightgreen)](https://www.docker.com/)
[![PWA](https://img.shields.io/badge/PWA-Enabled-orange)](https://web.dev/progressive-web-apps/)

## ✨ Features

- 🎴 Full 78-card tarot deck (22 Major Arcana + 56 Minor Arcana)
- 🔄 Upright and Reversed orientations
- 📱 Progressive Web App - Install on your phone!
- 🐳 Docker containerized
- ☁️ Deploy to Google Cloud Run
- 🎨 Beautiful gradient UI with animations
- ⚡ Fast and responsive
- 📡 Works offline (after first visit)

## 🚀 Quick Start

### Run Locally with Docker

```bash
docker-compose up -d
```

Open: http://localhost:5000

### Deploy to Google Cloud Run

```bash
gcloud run deploy tarot-reader \
  --source . \
  --platform managed \
  --region europe-west2 \
  --allow-unauthenticated \
  --port 5000
```

## 📁 Project Structure

```
tarot-reader/
├── static/                  # Static assets (PWA files, icons)
│   ├── icon-192.png
│   ├── icon-512.png
│   ├── manifest.json
│   └── service-worker.js
├── templates/               # HTML templates
│   └── index.html
├── docs/                    # Documentation
│   ├── README.md
│   ├── PWA_INSTALL_GUIDE.md
│   └── UPLOAD_CHECKLIST.md
├── scripts/                 # Utility scripts
│   ├── start.sh
│   ├── start.bat
│   └── deploy-pwa.sh
├── tarot_app.py            # Flask backend
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container configuration
└── docker-compose.yml      # Docker Compose config
```

## 🛠️ Tech Stack

- **Backend:** Python 3.11 + Flask
- **Frontend:** HTML5 + CSS3 + Vanilla JavaScript
- **Deployment:** Docker + Google Cloud Run
- **PWA:** Service Worker + Web Manifest

## 📱 Install as Mobile App

### Android (Chrome):
1. Visit the deployed URL in Chrome
2. Tap menu (⋮) → "Add to Home screen"
3. Tap "Add"

### iOS (Safari):
1. Visit the URL in Safari
2. Tap Share → "Add to Home Screen"
3. Tap "Add"

## 🔧 Development

### Prerequisites

- Python 3.11+
- Docker & Docker Compose
- Google Cloud SDK (for deployment)

### Local Setup

```bash
# Clone the repository
git clone https://github.com/maggiesummerxia/tarot-reader.git
cd tarot-reader

# Run with Docker
docker-compose up -d

# Or run with Python
pip install -r requirements.txt
python tarot_app.py
```

## 📚 Documentation

- [PWA Installation Guide](docs/PWA_INSTALL_GUIDE.md)
- [Upload Checklist](docs/UPLOAD_CHECKLIST.md)
- [Detailed README](docs/README.md)

## 🌐 API Endpoints

### `GET /`
Serves the web interface

### `POST /api/draw`
Draw tarot cards

**Request:**
```json
{
  "num_cards": 3
}
```

**Response:**
```json
{
  "cards": [
    {"card": "The Fool", "orientation": "Upright"},
    {"card": "Ace of Cups", "orientation": "Reversed"}
  ]
}
```

### `GET /api/deck-info`
Get deck information

## 💰 Cost

**Cloud Run Free Tier:**
- 2 million requests/month
- 360,000 GB-seconds memory
- 180,000 vCPU-seconds

For personal use: **$0/month** ✨

## 🤝 Contributing

Feel free to fork and submit PRs!

## 📄 License

MIT License - feel free to use for your own projects!

## 👤 Author

**Maggie Xia**
- GitHub: [@maggiesummerxia](https://github.com/maggiesummerxia)

---

Made with ✨ and 🔮
# CI/CD enabled
# Testing CI/CD with all permissions
# Add serviceUsageConsumer permission
