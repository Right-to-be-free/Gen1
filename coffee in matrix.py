import numpy as np

# Daily sales vector for Espresso, Latte, and Cappuccino
daily_sales = np.array([40, 35, 25])  # This is a vector in a 3-dimensional vector space

# Prices vector for Espresso, Latte, and Cappuccino
prices = np.array([3, 4, 5])  # Another vector in the same vector space

# Vector Property: Dot Product to calculate daily revenue
daily_revenue = np.dot(daily_sales, prices)
print(f"Daily Revenue (Dot Product of Sales and Prices vectors): ${daily_revenue}")

# Bias: Fixed daily operational cost (e.g., rent, utilities)
bias = 50  # Let's say you have a fixed cost of $50 per day

# Revenue after subtracting the bias (fixed cost)
net_daily_revenue = daily_revenue - bias
print(f"Net Daily Revenue (after fixed costs): ${net_daily_revenue}")

# Weekly sales matrix (same sales every day)
weekly_sales = np.tile(daily_sales, (7, 1))  # Repeating the daily sales vector for 7 days forms a matrix

# Total weekly sales per coffee type using scalar multiplication
total_weekly_sales = 7 * daily_sales  # Scaling the daily sales vector by 7
print(f"Total Weekly Sales (Espresso, Latte, Cappuccino): {total_weekly_sales}")

# Total weekly revenue considering bias (fixed cost per day)
weekly_revenue = (daily_revenue - bias) * 7
print(f"Net Weekly Revenue (after fixed costs): ${weekly_revenue}")

# Eigenvector Concept:
# Imagine the sales pattern changes but stays proportional (e.g., marketing boosts all sales by the same factor)
# An eigenvector represents a direction in which the data scales without changing its structure.

# Let's assume a growth factor (eigenvalue) due to marketing
growth_factor = 1.2  # 20% increase in sales

# New sales vector after applying the growth factor (eigenvalue)
new_sales = daily_sales * growth_factor
print(f"New Sales Vector after 20% growth (Eigenvector scaling): {new_sales}")

# New daily revenue after growth
new_daily_revenue = np.dot(new_sales, prices)
print(f"New Daily Revenue after 20% growth: ${new_daily_revenue}")

# Associative Property of Addition: (A + B) + C = A + (B + C)
# Example: Adding sales from three different days
sales_day1 = np.array([40, 35, 25])
sales_day2 = np.array([42, 33, 25])
sales_day3 = np.array([38, 36, 26])

# Grouping doesn't affect the total
total_sales_grouped1 = (sales_day1 + sales_day2) + sales_day3
total_sales_grouped2 = sales_day1 + (sales_day2 + sales_day3)
print(f"Associative Property Check: {np.array_equal(total_sales_grouped1, total_sales_grouped2)}")

# Commutative Property of Addition: A + B = B + A
# Example: Swapping the order of adding two days' sales
commutative_check = np.array_equal(sales_day1 + sales_day2, sales_day2 + sales_day1)
print(f"Commutative Property Check: {commutative_check}")

bias = 50
net_daily_revenue = daily_revenue - bias

growth_factor = 1.2
new_sales = daily_sales * growth_factor
