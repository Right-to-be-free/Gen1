import math

def normal_pdf(x, mu=0, sigma=1):
    """
    Computes the Probability Density Function (PDF) for a normal distribution.

    :param x: The value at which to evaluate the PDF.
    :param mu: Mean of the normal distribution (default is 0).
    :param sigma: Standard deviation of the normal distribution (default is 1).
    :return: Probability density at x.
    """
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = math.exp(-((x - mu) ** 2) / (2 * sigma ** 2))
    return coefficient * exponent

# Example usage:
print(normal_pdf(0))  # Output: 0.3989 (PDF of standard normal at x = 0)
print(normal_pdf(1, mu=0, sigma=1))  # Output: 0.2419
print(normal_pdf(2, mu=0, sigma=2))  # Output: 0.1209
