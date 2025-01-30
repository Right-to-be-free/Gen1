def probability_two_heads():
    """
    Calculates the probability of getting exactly two heads and one tail
    when flipping three fair coins.
    """
    total_outcomes = 2 ** 3  # Total possible outcomes (2^3 = 8)
    favorable_outcomes = 3    # Cases where we get exactly two heads and one tail
    probability = favorable_outcomes / total_outcomes
    return probability

# Example Usage
prob = probability_two_heads()
print(f"Probability of getting exactly two heads and one tail: {prob:.4f}")  # Output rounded to 4 decimal places
