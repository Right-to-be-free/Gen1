import numpy as np

# Define parameters
n = 10  # Number of tosses
p = 0.5  # Probability of getting heads

# Simulate 1 trial of tossing a coin 10 times
num_heads = np.random.binomial(n, p)

# Print the result
print(f"Number of heads in 10 tosses: {num_heads}")

trials = 1000  # Number of experiments
results = np.random.binomial(n, p, trials)

# Print first 10 results as an example
print(f"First 10 simulations: {results[:10]}")
