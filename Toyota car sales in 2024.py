import numpy as np
import matplotlib.pyplot as plt

monthly_sales = [
    209953, 172909, 37044, 17720, 70, 579, 35, 810, 5211, 26811, 
    51236, 1458, 175, 5005, 158, 72, 6868, 58104, 1854, 44296, 
    7448, 2794, 1315, 3252, 8429, 60, 2105, 5399, 76953, 7032, 
    22715, 14973, 37688, 121673, 948, 8120, 397, 13027, 3462, 
    3468, 754, 30176, 151849
]

# Selecting the top 10 highest-selling vehicles
top_10_indices = np.argsort(monthly_sales)[-10:]  
top_10_sales = [monthly_sales[i] for i in top_10_indices]
top_10_labels = [f'Toyota {i+1}' for i in top_10_indices]  

# Plotting the pie chart
plt.figure(figsize=(10, 6))
plt.pie(top_10_sales, labels=top_10_labels, autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Top 10 Best-Selling Vehicles (December 2024)')
plt.show()