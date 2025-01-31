# Define parameters for online shopping clicks
import numpy as np


n = 20  # Number of visitors
p = 0.05  # Probability of a visitor clicking on the ad

# Simulate the number of clicks on the ad
clicks = np.random.binomial(n, p)

# Print the result
print(f"Number of clicks on the ad: {clicks}")
