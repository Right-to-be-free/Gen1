def balloon_probability(num_black, num_white, num_yellow):
    """
    Calculates the probability of drawing a black balloon from a bag.

    :param num_black: Number of black balloons
    :param num_white: Number of white balloons
    :param num_yellow: Number of yellow balloons
    :return: Probability of selecting a black balloon
    """
    total_balloons = num_black + num_white + num_yellow
    prob_black = num_black / total_balloons
    return prob_black

# Example Usage
probability_black = balloon_probability(10, 47, 5)
print(f"Probability of selecting a black balloon: {probability_black:.4f}")  # Output rounded to 4 decimal places
