import random

# Define the possible numbers in European Roulette (0 to 36)
roulette_numbers = list(range(37))  # Generates [0, 1, 2, ..., 36]

# Randomly select the winning number
winning_number = random.choice(roulette_numbers)

# Print the result
print(f"The roulette ball landed on: {winning_number}")
