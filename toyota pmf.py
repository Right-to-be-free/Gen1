import numpy as np
import matplotlib.pyplot as plt

# Car sales data (December 2024) - Only model-specific
car_sales = {
    "Camry": 26811,
    "Corolla": 17720,
    "RAV4": 44296,
    "Tacoma": 22715,
    "Highlander": 76953,
    "Tundra": 14973,
    "4Runner": 121673
}

# Sorting cars by sales (most to least)
sorted_cars = sorted(car_sales.items(), key=lambda x: x[1], reverse=True)
car_names, sales_numbers = zip(*sorted_cars)

# Define a color map
cmap = plt.get_cmap('Paired')
colors = [cmap(i / len(sales_numbers)) for i in range(len(sales_numbers))]

# Plotting the pie chart
plt.figure(figsize=(10, 6))
plt.pie(sales_numbers, labels=car_names, autopct='%1.1f%%', colors=colors)
plt.title('Toyota Car Sales (December 2024)')
plt.show()

# Calculate total sales
total_sales = sum(car_sales.values())

# Calculate PMF (Probability Mass Function) for each car model
pmf = {car: sales / total_sales for car, sales in car_sales.items()}

# Print the PMF for each car model
for car, probability in pmf.items():
    print(f"The probability (PMF) of {car} is: {probability:.4f} or {probability*100:.2f}%")

# Example output (for reference, not part of the code):
# The probability (PMF) of Camry is: 0.0560 or 5.60%
# The probability (PMF) of Corolla is: 0.0370 or 3.70%
# The probability (PMF) of RAV4 is: 0.0926 or 9.26%
# The probability (PMF) of Tacoma is: 0.0475 or 4.75%
# The probability (PMF) of Highlander is: 0.1608 or 16.08%
# The probability (PMF) of Tundra is: 0.0313 or 3.13%
# The probability (PMF) of 4Runner is: 0.2542 or 25.42%

# Car sales data (December 2024) - Only model-specific
car_sales = {
    "Camry": 26811,
    "Corolla": 17720,
    "RAV4": 44296,
    "Tacoma": 22715,
    "Highlander": 76953,
    "Tundra": 14973,
    "4Runner": 121673
}

# Calculate total sales
total_sales = sum(car_sales.values())

# Calculate PMF (Probability Mass Function) for each car model
pmf = {car: sales / total_sales for car, sales in car_sales.items()}

# Sort the cars by sales in descending order (most to least)
sorted_cars = sorted(pmf.items(), key=lambda x: x[1], reverse=True)

# Calculate CFM (Cumulative Frequency Mass Function)
cfm = {}
cumulative_prob = 0

# Loop through sorted cars and calculate the cumulative probability
for car, probability in sorted_cars:
    cumulative_prob += probability
    cfm[car] = cumulative_prob

# Print the CFM for each car model
for car, cumulative_probability in cfm.items():
    print(f"The cumulative probability (CFM) up to {car} is: {cumulative_probability:.4f} or {cumulative_probability*100:.2f}%")

import matplotlib.pyplot as plt

# Car sales data (December 2024) - Only model-specific
car_sales = {
    "Camry": 26811,
    "Corolla": 17720,
    "RAV4": 44296,
    "Tacoma": 22715,
    "Highlander": 76953,
    "Tundra": 14973,
    "4Runner": 121673
}

# Calculate total sales
total_sales = sum(car_sales.values())

# Calculate PMF (Probability Mass Function) for each car model
pmf = {car: sales / total_sales for car, sales in car_sales.items()}

# Sort the cars by sales in descending order (most to least)
sorted_cars = sorted(pmf.items(), key=lambda x: x[1], reverse=True)
car_names, probabilities = zip(*sorted_cars)

# Plotting the "PDF" (PMF) as a bar chart
plt.figure(figsize=(10, 6))
plt.bar(car_names, probabilities, color='skyblue')
plt.xlabel('Car Models')
plt.ylabel('Probability (PMF)')
plt.title('Probability Mass Function (PMF) of Toyota Car Sales (December 2024)')
plt.xticks(rotation=45, ha='right')
plt.show()

