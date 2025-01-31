import random

# Define the deck of 52 playing cards
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Create a full deck by combining ranks and suits
deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]

# Shuffle the deck
random.shuffle(deck)

# Deal a hand of 5 cards
hand = deck[:5]

# Print the shuffled deck and dealt hand
print("Shuffled Deck (first 5 cards shown):", deck[:5])
print("Dealt Hand:", hand)
