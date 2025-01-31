import numpy as np

# Define parameters
n = 100  # Number of bulbs checked
p = 0.02  # Probability of a defective bulb

# Simulate one trial (checking 100 bulbs)
num_defective = np.random.binomial(n, p)

# Print the result
print(f"Number of defective bulbs in 100 checked: {num_defective}")
