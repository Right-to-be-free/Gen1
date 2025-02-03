import numpy as np

# Daily coffee sales: Espresso = 40, Latte = 35, Cappuccino = 25
daily_sales = np.array([40, 35, 25])

# Prices per coffee: Espresso = $3, Latte = $4, Cappuccino = $5
prices = np.array([3, 4, 5])

# Calculate total daily revenue by multiplying sales with prices
daily_revenue = np.dot(daily_sales, prices)
print(f"Total money made in a day: ${daily_revenue}")

# Bias: Fixed daily costs like rent, utilities, etc.
bias = 50  # $50 fixed cost every day

# Net revenue after subtracting fixed costs
net_daily_revenue = daily_revenue - bias
print(f"Money left after covering fixed costs: ${net_daily_revenue}")

# Weekly sales: same sales every day, repeated for 7 days
weekly_sales = np.tile(daily_sales, (7, 1))  # Creates a 7-day sales record

# Total coffees sold in a week per type (Espresso, Latte, Cappuccino)
total_weekly_sales = 7 * daily_sales
print(f"Coffees sold in a week: Espresso = {total_weekly_sales[0]}, Latte = {total_weekly_sales[1]}, Cappuccino = {total_weekly_sales[2]}")

# Total weekly revenue after subtracting fixed costs for each day
weekly_revenue = (daily_revenue - bias) * 7
print(f"Total money made in a week after fixed costs: ${weekly_revenue}")

# Eigenvector: Sales grow by 20% but proportions remain the same
growth_factor = 1.2  # 20% increase in sales

# New sales numbers after growth
new_sales = daily_sales * growth_factor
print(f"Sales after 20% growth: Espresso = {new_sales[0]}, Latte = {new_sales[1]}, Cappuccino = {new_sales[2]}")

# New daily revenue after sales growth
new_daily_revenue = np.dot(new_sales, prices)
print(f"Money made in a day after 20% sales growth: ${new_daily_revenue}")

# Checking associative property: grouping sales differently gives the same total
sales_day1 = np.array([40, 35, 25])
sales_day2 = np.array([42, 33, 25])
sales_day3 = np.array([38, 36, 26])

total_sales_grouped1 = (sales_day1 + sales_day2) + sales_day3
total_sales_grouped2 = sales_day1 + (sales_day2 + sales_day3)
print(f"Does grouping sales differently give the same total? {np.array_equal(total_sales_grouped1, total_sales_grouped2)}")

# Checking commutative property: adding sales in any order gives the same total
commutative_check = np.array_equal(sales_day1 + sales_day2, sales_day2 + sales_day1)
print(f"Does adding sales in any order give the same total? {commutative_check}")
