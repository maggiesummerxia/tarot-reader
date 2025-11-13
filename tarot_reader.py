#!/usr/bin/env python3
"""
Tarot Card Drawing Program
Draws any number of cards from a full 78-card tarot deck
Includes upright and reversed orientations
"""

import random
from typing import List, Tuple

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

def draw_cards(num_cards: int) -> List[Tuple[str, str]]:
    """
    Draw a specified number of cards from the deck.
    Returns list of tuples: (card_name, orientation)
    """
    if num_cards < 1:
        print("Please draw at least 1 card!")
        return []
    
    if num_cards > 78:
        print("Cannot draw more than 78 cards!")
        return []
    
    deck = create_deck()
    random.shuffle(deck)
    
    drawn_cards = []
    for i in range(num_cards):
        card = deck[i]
        orientation = random.choice(["Upright", "Reversed"])
        drawn_cards.append((card, orientation))
    
    return drawn_cards

def display_cards(cards: List[Tuple[str, str]]) -> None:
    """Display the drawn cards in a nice format."""
    print("\n" + "="*60)
    print(f"✨ YOUR TAROT READING - {len(cards)} CARD{'S' if len(cards) > 1 else ''} ✨")
    print("="*60 + "\n")
    
    for i, (card, orientation) in enumerate(cards, 1):
        symbol = "↑" if orientation == "Upright" else "↓"
        print(f"Card {i}: {card}")
        print(f"        {symbol} {orientation}")
        print()

def main():
    """Main program loop."""
    print("🔮 Welcome to the Tarot Card Reader 🔮")
    print("="*60)
    print("The deck contains 78 cards:")
    print("  • 22 Major Arcana")
    print("  • 56 Minor Arcana (Wands, Cups, Swords, Pentacles)")
    print("="*60)
    
    while True:
        try:
            num = input("\nHow many cards would you like to draw? (1-78, or 'q' to quit): ").strip()
            
            if num.lower() in ['q', 'quit', 'exit']:
                print("\n✨ Thank you for using the Tarot Card Reader! ✨")
                break
            
            num_cards = int(num)
            cards = draw_cards(num_cards)
            
            if cards:
                display_cards(cards)
                
                # Ask if they want to draw again
                again = input("Draw again? (y/n): ").strip().lower()
                if again not in ['y', 'yes']:
                    print("\n✨ Thank you for using the Tarot Card Reader! ✨")
                    break
                    
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")
        except KeyboardInterrupt:
            print("\n\n✨ Thank you for using the Tarot Card Reader! ✨")
            break

if __name__ == "__main__":
    main()
