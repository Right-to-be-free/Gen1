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
cmap = plt.cm.get_cmap('Paired', len(sales_numbers))
colors = [cmap(i) for i in range(len(sales_numbers))]

# Plotting the pie chart
plt.figure(figsize=(10, 6))
plt.pie(sales_numbers, labels=car_names, autopct='%1.1f%%', colors=colors)
plt.title('Top-Selling Toyota Models (December 2024)')
plt.show()
