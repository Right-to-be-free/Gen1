import numpy as np
import matplotlib.pyplot as plt

# Car sales data (December 2024)
car_sales = {
    "Toyota TMNA": 209953,
    "Toyota Division": 172909,
    "Lexus Division": 37044,
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

# Plotting the pie chart
plt.figure(figsize=(10, 6))
plt.pie(sales_numbers, labels=car_names, autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Top 10 Best-Selling Cars (December 2024)')
plt.show()
