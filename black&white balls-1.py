def find_black_balls(num_white, ratio):
    """
    Finds the number of black balls in a box.

    :param num_white: Number of white balls
    :param ratio: Ratio of black ball probability to white ball probability
    :return: Number of black balls
    """
    num_black = (ratio * num_white)  # Using the formula derived above
    return int(num_black)

# Example Usage
num_white_balls = 30
ratio_black_to_white_prob = 2 / 5

black_balls = find_black_balls(num_white_balls, ratio_black_to_white_prob)
print(f"Number of black balls: {black_balls}")
