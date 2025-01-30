def cmf(values, probabilities, x):
    """
    Computes the Cumulative Mass Function (CMF) / CDF for a discrete random variable.
    
    :param values: List of possible values of the random variable (must be sorted in ascending order).
    :param probabilities: Corresponding probabilities for each value.
    :param x: The value for which CMF is to be computed.
    :return: Cumulative probability up to x.
    """
    cumulative_probability = 0
    for v, p in zip(values, probabilities):
        if v <= x:
            cumulative_probability += p
        else:
            break
    return cumulative_probability

# Example usage:
values = [1, 2, 3, 4, 5, 6]  # Outcomes of a fair die
probabilities = [1/6] * 6  # Equal probability for each outcome

print(cmf(values, probabilities, 3))  # Output: 0.5 (1/6 + 1/6 + 1/6)
print(cmf(values, probabilities, 6))  # Output: 1.0 (Sum of all probabilities)
print(cmf(values, probabilities, 0))  # Output: 0 (Since 0 is not in values)

