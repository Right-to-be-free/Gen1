def horse_race_pmf(horses, probabilities):
    """
    Returns a PMF for a horse race.

    :param horses: List of horse names or identifiers.
    :param probabilities: Corresponding list of probabilities for each horse winning.
    :return: Dictionary representing the PMF of the race.
    """
    if len(horses) != len(probabilities):
        raise ValueError("The number of horses must match the number of probabilities.")
    if not (0.99 <= sum(probabilities) <= 1.01):  # Allowing a small margin for floating-point precision
        raise ValueError("The sum of probabilities must be approximately 1.")
    return dict(zip(horses, probabilities))

# Example usage:
horses = ['Horse A', 'Horse B', 'Horse C', 'Horse D']
probabilities = [0.4, 0.3, 0.2, 0.1]  # Probabilities must sum to 1

pmf = horse_race_pmf(horses, probabilities)
print(pmf)

