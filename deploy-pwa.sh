#!/bin/bash
# Quick script to update PWA files in Cloud Shell

echo "🔮 Updating Tarot Reader with PWA support..."
echo ""

# Check if we're in the right directory
if [ ! -f "tarot_app.py" ]; then
    echo "❌ Error: tarot_app.py not found. Are you in the tarot-reader directory?"
    exit 1
fi

echo "📦 Files in current directory:"
ls -la

echo ""
echo "🚀 Deploying to Cloud Run..."
gcloud run deploy tarot-reader \
  --source . \
  --platform managed \
  --region europe-west2 \
  --allow-unauthenticated \
  --port 5000

if [ $? -eq 0 ]; then
    echo ""
    echo "✨ Deployment successful!"
    echo ""
    echo "📱 Your PWA is ready!"
    echo ""
    echo "🌐 URL: https://tarot-reader-85429130230.europe-west2.run.app"
    echo ""
    echo "📋 Next steps:"
    echo "  1. Open the URL in Chrome on your phone"
    echo "  2. Tap the menu (⋮) and select 'Add to Home screen'"
    echo "  3. Enjoy your tarot app!"
    echo ""
else
    echo ""
    echo "❌ Deployment failed. Check the errors above."
fi
