def conditional_probability(p_A_and_B, p_B):
    """
    Calculates the conditional probability P(A|B).

    :param p_A_and_B: Probability of both events A and B occurring (P(A ∩ B))
    :param p_B: Probability of event B occurring (P(B))
    :return: Conditional probability P(A|B)
    """
    if p_B == 0:
        return "Undefined (P(B) cannot be 0)"
    
    p_A_given_B = p_A_and_B / p_B
    return p_A_given_B

# Example Usage
p_A_and_B = 0.2  # Probability of both A and B occurring
p_B = 0.5        # Probability of event B occurring

prob = conditional_probability(p_A_and_B, p_B)
print(f"Conditional Probability P(A|B): {prob:.4f}")  # Output rounded to 4 decimal places
