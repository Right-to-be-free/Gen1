from math import comb  # Importing comb function to calculate combinations

# Given data
n = 5       # Number of coin tosses
p = 0.5     # Probability of getting heads (since it's a fair coin)

# (a) Probability of exactly 2 heads
k1 = 2  # Number of heads
prob_2_heads = comb(n, k1) * (p ** k1) * ((1 - p) ** (n - k1))

# (b) Probability of at least 4 heads (4 or 5 heads)
k2 = 4  # Number of heads for at least 4 heads
prob_4_heads = comb(n, k2) * (p ** k2) * ((1 - p) ** (n - k2))

k3 = 5  # Number of heads for exactly 5 heads
prob_5_heads = comb(n, k3) * (p ** k3) * ((1 - p) ** (n - k3))

# Total probability for at least 4 heads
prob_at_least_4_heads = prob_4_heads + prob_5_heads

# Printing results
print("Probability of exactly 2 heads:", prob_2_heads)
print("Probability of at least 4 heads:", prob_at_least_4_heads)
