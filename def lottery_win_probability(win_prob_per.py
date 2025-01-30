def lottery_win_probability(win_prob_per_ticket, num_tickets):
    """
    Calculates the probability of winning at least once in a lottery game.

    :param win_prob_per_ticket: Probability of winning with one ticket (e.g., 0.02 for 2 out of 100)
    :param num_tickets: Number of tickets purchased
    :return: Probability of winning at least once
    """
    lose_prob_per_ticket = 1 - win_prob_per_ticket
    lose_all_prob = lose_prob_per_ticket ** num_tickets
    win_at_least_one_prob = 1 - lose_all_prob
    return win_at_least_one_prob

# Example Usage
win_probability = lottery_win_probability(0.02, 10)
print(f"Probability of winning at least once: {win_probability:.4f}")  # Output rounded to 4 decimal places

