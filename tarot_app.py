#!/usr/bin/env python3
"""
Tarot Card Reader - Flask Backend API
Provides endpoints for drawing tarot cards
"""

from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import random
from typing import List, Dict

app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')
CORS(app)  # Enable CORS for frontend communication

# Major Arcana (22 cards)
MAJOR_ARCANA = [
    "0 - The Fool",
    "I - The Magician",
    "II - The High Priestess",
    "III - The Empress",
    "IV - The Emperor",
    "V - The Hierophant",
    "VI - The Lovers",
    "VII - The Chariot",
    "VIII - Strength",
    "IX - The Hermit",
    "X - Wheel of Fortune",
    "XI - Justice",
    "XII - The Hanged Man",
    "XIII - Death",
    "XIV - Temperance",
    "XV - The Devil",
    "XVI - The Tower",
    "XVII - The Star",
    "XVIII - The Moon",
    "XIX - The Sun",
    "XX - Judgement",
    "XXI - The World"
]

# Minor Arcana (56 cards - 4 suits × 14 cards each)
SUITS = ["Wands", "Cups", "Swords", "Pentacles"]
RANKS = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", 
         "Nine", "Ten", "Page", "Knight", "Queen", "King"]

def create_deck() -> List[str]:
    """Create a full 78-card tarot deck."""
    deck = MAJOR_ARCANA.copy()
    
    # Add all Minor Arcana cards
    for suit in SUITS:
        for rank in RANKS:
            deck.append(f"{rank} of {suit}")
    
    return deck

@app.route('/')
def index():
    """Serve the frontend HTML."""
    return render_template('index.html')

@app.route('/api/draw', methods=['POST'])
def draw_cards():
    """
    Draw cards from the tarot deck.
    Expects JSON: {"num_cards": <number>}
    Returns JSON: {"cards": [{"card": "card name", "orientation": "Upright/Reversed"}]}
    """
    try:
        data = request.get_json()
        num_cards = data.get('num_cards', 1)
        
        # Validate input
        if not isinstance(num_cards, int):
            return jsonify({"error": "num_cards must be an integer"}), 400
        
        if num_cards < 1 or num_cards > 78:
            return jsonify({"error": "num_cards must be between 1 and 78"}), 400
        
        # Create and shuffle deck
        deck = create_deck()
        random.shuffle(deck)
        
        # Draw cards
        drawn_cards = []
        for i in range(num_cards):
            card = deck[i]
            orientation = random.choice(["Upright", "Reversed"])
            drawn_cards.append({
                "card": card,
                "orientation": orientation
            })
        
        return jsonify({"cards": drawn_cards})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/deck-info', methods=['GET'])
def deck_info():
    """Get information about the deck."""
    return jsonify({
        "total_cards": 78,
        "major_arcana": len(MAJOR_ARCANA),
        "minor_arcana": len(SUITS) * len(RANKS),
        "suits": SUITS
    })

if __name__ == '__main__':
    print("🔮 Starting Tarot Card Reader Server...")
    print("📍 Open your browser to: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=5000)
