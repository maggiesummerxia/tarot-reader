#!/bin/bash

echo "🔮 Tarot Card Reader - Quick Start"
echo "=================================="
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed!"
    echo "Please install Docker Desktop from: https://www.docker.com/products/docker-desktop/"
    exit 1
fi

# Check if docker-compose is available
if command -v docker-compose &> /dev/null; then
    COMPOSE_CMD="docker-compose"
elif docker compose version &> /dev/null; then
    COMPOSE_CMD="docker compose"
else
    echo "❌ Docker Compose is not available!"
    echo "Please make sure Docker Desktop is installed and running."
    exit 1
fi

echo "✅ Docker found!"
echo ""
echo "Starting Tarot Card Reader..."
echo ""

# Start the container
$COMPOSE_CMD up -d

if [ $? -eq 0 ]; then
    echo ""
    echo "✨ Success! The Tarot Card Reader is now running!"
    echo ""
    echo "🌐 Open your browser to: http://localhost:5000"
    echo ""
    echo "📝 Useful commands:"
    echo "  View logs:    $COMPOSE_CMD logs -f"
    echo "  Stop app:     $COMPOSE_CMD down"
    echo "  Restart app:  $COMPOSE_CMD restart"
    echo ""
else
    echo ""
    echo "❌ Failed to start the container."
    echo "Try running: $COMPOSE_CMD logs"
    exit 1
fi
