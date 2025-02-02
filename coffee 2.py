import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

fig, axs = plt.subplots(4, 2, figsize=(15, 20))

# 1. Probability Mass Function (PMF) - Number of Coffees Bought
coffees = np.array([1, 2, 3, 4])  # Possible coffee purchases
pmf_values = np.array([0.4, 0.3, 0.2, 0.1])  # Probabilities

axs[0, 0].bar(coffees, pmf_values, color='blue', alpha=0.7)
axs[0, 0].set_xlabel('Number of Coffees Bought')
axs[0, 0].set_ylabel('Probability')
axs[0, 0].set_title('PMF: Coffee Purchase Distribution')

# 2. Cumulative Distribution Function (CDF)
cdf_values = np.cumsum(pmf_values)
axs[0, 1].step(coffees, cdf_values, where='mid', color='red', label='CDF')
axs[0, 1].set_xlabel('Number of Coffees Bought')
axs[0, 1].set_ylabel('Cumulative Probability')
axs[0, 1].set_title('CDF: Coffee Purchase Distribution')
axs[0, 1].legend()

# 3. Normal Distribution - Coffee Prices
prices = np.random.normal(5, 1, 1000)  # Mean price $5, std dev $1
axs[1, 0].hist(prices, bins=30, color='green', alpha=0.7, density=True)
xmin, xmax = axs[1, 0].get_xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, 5, 1)
axs[1, 0].plot(x, p, 'k', linewidth=2)
axs[1, 0].set_xlabel('Price ($)')
axs[1, 0].set_ylabel('Density')
axs[1, 0].set_title('Normal Distribution: Coffee Prices')

# 4. Exponential Distribution - Time Between Customers
times = np.random.exponential(5, 1000)  # Mean time 5 minutes
axs[1, 1].hist(times, bins=30, color='purple', alpha=0.7, density=True)
xmin, xmax = axs[1, 1].get_xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.expon.pdf(x, scale=5)
axs[1, 1].plot(x, p, 'k', linewidth=2)
axs[1, 1].set_xlabel('Time (minutes)')
axs[1, 1].set_ylabel('Density')
axs[1, 1].set_title('Exponential Distribution: Time Between Customers')

# 5. Linear Regression - Revenue vs. Customers
customers = np.arange(1, 51)
revenue = 5 * customers + np.random.normal(0, 10, 50)
axs[2, 0].scatter(customers, revenue, color='orange', alpha=0.6)
slope, intercept, r_value, p_value, std_err = stats.linregress(customers, revenue)
axs[2, 0].plot(customers, slope * customers + intercept, color='black')
axs[2, 0].set_xlabel('Number of Customers')
axs[2, 0].set_ylabel('Revenue ($)')
axs[2, 0].set_title('Linear Regression: Revenue vs. Customers')

# 6. Correlation - Temperature vs Iced Coffee Sales
temperature = np.random.randint(60, 100, 50)  # Random temperatures (°F)
iced_coffee_sales = temperature * 0.8 + np.random.normal(0, 5, 50)  # Sales increase with temp
correlation_coefficient = np.corrcoef(temperature, iced_coffee_sales)[0, 1]
axs[2, 1].scatter(temperature, iced_coffee_sales, color='blue', alpha=0.6)
axs[2, 1].set_xlabel('Temperature (°F)')
axs[2, 1].set_ylabel('Iced Coffee Sales')
axs[2, 1].set_title(f'Correlation: Temperature vs. Iced Coffee Sales\nCorrelation Coefficient: {correlation_coefficient:.2f}')

# Adjust layout
plt.tight_layout()
plt.show()