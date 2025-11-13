# 🔮 Tarot Card Reader - Full Stack Version

A beautiful tarot card reading application with a Python Flask backend and HTML/JavaScript frontend.

## 📁 Files Included

- `tarot_app.py` - Flask backend API server
- `tarot_frontend.html` - Frontend web interface
- `requirements.txt` - Python dependencies
- `Dockerfile` - Docker container configuration
- `docker-compose.yml` - Docker Compose configuration
- `.dockerignore` - Docker ignore file

## 🐳 Setup with Docker (RECOMMENDED)

**No Python installation needed! Just Docker.**

### Prerequisites
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### Quick Start

1. **Navigate to the project folder:**
```bash
cd /path/to/tarot-reader
```

2. **Start the app with Docker Compose:**
```bash
docker-compose up -d
```

3. **Open your browser:**
```
http://localhost:5000
```

4. **To stop the app:**
```bash
docker-compose down
```

### Docker Commands Cheat Sheet

```bash
# Start the app (builds image first time)
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the app
docker-compose down

# Rebuild after code changes
docker-compose up -d --build

# Check if container is running
docker ps
```

---

## 🐍 Setup without Docker (Alternative)

If you prefer to run it directly with Python:

### Step 1: Install Python Dependencies

Open your terminal/command prompt and navigate to the folder with these files, then run:

```bash
pip install -r requirements.txt
```

### Step 2: Start the Backend Server

Run the Flask server:

```bash
python tarot_app.py
```

### Step 3: Open the Frontend

With the server running, open your web browser and go to:

```
http://localhost:5000
```

The page will automatically check the connection status:
- 🟢 **Green** = Connected and ready
- 🔴 **Red** = Server not running
- 🔄 **Yellow** = Drawing cards

## 🎴 How to Use

1. Enter the number of cards you want to draw (1-78)
2. Click "✨ Draw Cards ✨"
3. Your cards will appear with their orientations (↑ Upright or ↓ Reversed)
4. Click "Clear Reading" to start over

## 📡 API Endpoints

The backend provides these endpoints:

### `GET /`
Serves the frontend HTML interface

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
    {"card": "Ace of Cups", "orientation": "Reversed"},
    {"card": "Queen of Swords", "orientation": "Upright"}
  ]
}
```

### `GET /api/deck-info`
Get information about the deck

**Response:**
```json
{
  "total_cards": 78,
  "major_arcana": 22,
  "minor_arcana": 56,
  "suits": ["Wands", "Cups", "Swords", "Pentacles"]
}
```

## 🛠️ Troubleshooting

### Docker Issues

**"docker-compose: command not found":**
- Make sure Docker Desktop is installed and running
- On some systems, use `docker compose` (without hyphen) instead of `docker-compose`

**Port 5000 already in use:**
- Stop other services using port 5000
- Or edit `docker-compose.yml` and change `"5000:5000"` to `"5001:5000"` (then access on port 5001)

**Container won't start:**
- Check logs: `docker-compose logs`
- Rebuild: `docker-compose up -d --build`

### Non-Docker Issues

**"Backend not connected" error:**
- Make sure you ran `python tarot_app.py` and the server is running
- Check that nothing else is using port 5000
- Try accessing http://localhost:5000 directly

**"Module not found" error:**
- Run `pip install -r requirements.txt` again
- Make sure you're in the correct directory

**Port already in use:**
- Close any other programs using port 5000
- Or edit `tarot_app.py` and change `port=5000` to another number (like 5001)

## 🎨 Features

- ✅ Full 78-card tarot deck (22 Major Arcana + 56 Minor Arcana)
- ✅ Upright and Reversed orientations
- ✅ Beautiful gradient design with animations
- ✅ Real-time connection status
- ✅ Error handling and validation
- ✅ Responsive design for all screen sizes
- ✅ RESTful API backend

## 🔧 Customization

You can easily customize:
- **Colors:** Edit the CSS gradient in `tarot_frontend.html`
- **Port:** Change `port=5000` in `tarot_app.py`
- **Card meanings:** Add a card meanings database to the backend

Enjoy your tarot readings! 🌟
