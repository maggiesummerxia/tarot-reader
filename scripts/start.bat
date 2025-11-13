@echo off
echo 🔮 Tarot Card Reader - Quick Start
echo ==================================
echo.

REM Check if Docker is installed
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker is not installed!
    echo Please install Docker Desktop from: https://www.docker.com/products/docker-desktop/
    pause
    exit /b 1
)

echo ✅ Docker found!
echo.
echo Starting Tarot Card Reader...
echo.

REM Try docker-compose first, then docker compose
docker-compose version >nul 2>&1
if %errorlevel% equ 0 (
    docker-compose up -d
) else (
    docker compose up -d
)

if %errorlevel% equ 0 (
    echo.
    echo ✨ Success! The Tarot Card Reader is now running!
    echo.
    echo 🌐 Open your browser to: http://localhost:5000
    echo.
    echo 📝 Useful commands:
    echo   View logs:    docker-compose logs -f
    echo   Stop app:     docker-compose down
    echo   Restart app:  docker-compose restart
    echo.
) else (
    echo.
    echo ❌ Failed to start the container.
    echo Try running: docker-compose logs
    pause
    exit /b 1
)

pause
