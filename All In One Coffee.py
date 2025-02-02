import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# 1. Probability Mass Function (PMF) - Number of Coffees Bought
coffees = np.array([1, 2, 3, 4])  # Possible coffee purchases
pmf_values = np.array([0.4, 0.3, 0.2, 0.1])  # Probabilities

plt.bar(coffees, pmf_values, color='blue', alpha=0.7)
plt.xlabel('Number of Coffees Bought')
plt.ylabel('Probability')
plt.title('PMF: Coffee Purchase Distribution')
plt.show()

# 2. Cumulative Distribution Function (CDF)
cdf_values = np.cumsum(pmf_values)
plt.step(coffees, cdf_values, where='mid', color='red', label='CDF')
plt.xlabel('Number of Coffees Bought')
plt.ylabel('Cumulative Probability')
plt.title('CDF: Coffee Purchase Distribution')
plt.legend()
plt.show()

# 3. Probability Density Function (PDF) - Time Spent in Shop (Normal Distribution)
mu, sigma = 30, 5  # Mean and standard deviation
time_spent = np.linspace(10, 50, 100)
pdf_values = stats.norm.pdf(time_spent, mu, sigma)

plt.plot(time_spent, pdf_values, color='green')
plt.xlabel('Time Spent in Shop (minutes)')
plt.ylabel('Density')
plt.title('PDF: Time Spent in Coffee Shop')
plt.show()

# 4. Bernoulli Distribution - Buying a Pastry (Yes/No)
p = 0.6  # Probability of buying a pastry
bernoulli_samples = np.random.binomial(1, p, 1000)  # Simulating 1000 customers

plt.hist(bernoulli_samples, bins=[-0.5, 0.5, 1.5], density=True, color='purple', alpha=0.7, rwidth=0.8)
plt.xticks([0, 1], ['No Pastry', 'Bought Pastry'])
plt.ylabel('Probability')
plt.title('Bernoulli Distribution: Pastry Purchase')
plt.show()

# 5. Binomial Distribution - Number of Pastry Buyers in 10 Customers
n, p = 10, 0.6
binomial_x = np.arange(0, 11)
binomial_pmf = stats.binom.pmf(binomial_x, n, p)

plt.bar(binomial_x, binomial_pmf, color='orange', alpha=0.7)
plt.xlabel('Number of Customers Buying Pastry')
plt.ylabel('Probability')
plt.title('Binomial Distribution: Pastry Buyers (n=10)')
plt.show()

# 6. Normal Distribution - Daily Revenue
mu_revenue, sigma_revenue = 500, 50
daily_revenue = np.linspace(350, 650, 100)
daily_pdf = stats.norm.pdf(daily_revenue, mu_revenue, sigma_revenue)

plt.plot(daily_revenue, daily_pdf, color='brown')
plt.xlabel('Daily Revenue ($)')
plt.ylabel('Density')
plt.title('Normal Distribution: Daily Revenue')
plt.show()

# 7. Linear Equation - Revenue Prediction
customers = np.arange(0, 100, 1)  # Number of customers from 0 to 100
revenue = 5 * customers + 50

plt.plot(customers, revenue, color='black')
plt.xlabel('Number of Customers')
plt.ylabel('Revenue ($)')
plt.title('Linear Equation: Revenue vs. Customers')
plt.show()

# 8. Correlation - Temperature vs Iced Coffee Sales
temperature = np.random.randint(60, 100, 50)  # Random temperatures (°F)
iced_coffee_sales = temperature * 0.8 + np.random.normal(0, 5, 50)  # Sales increase with temp

correlation_coefficient = np.corrcoef(temperature, iced_coffee_sales)[0, 1]
print(f'Correlation coefficient between temperature and iced coffee sales: {correlation_coefficient:.2f}')

plt.scatter(temperature, iced_coffee_sales, color='blue', alpha=0.6)
plt.xlabel('Temperature (°F)')
plt.ylabel('Iced Coffee Sales')
plt.title('Correlation: Temperature vs. Iced Coffee Sales')
plt.show()
