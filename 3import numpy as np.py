import numpy as np

# Define parameters for free throw shooting
n = 6  # Number of free throws
p = 0.75  # Probability of making a successful free throw

# Simulate the number of successful free throws
successful_free_throws = np.random.binomial(n, p)

# Print the result
print(f"Number of successful free throws: {successful_free_throws}")
