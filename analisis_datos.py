import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from a CSV file
df = pd.read_csv('/Users/despoinaiapona/Downloads/archive/ecommerce_sales_data.csv')

# Analizing the total sales by product category
sales_by_category = df.groupby('Category')['Total Sales'].sum().sort_values(ascending=False)
print("Total Sales by Product Category:")
print(sales_by_category)

# Total sales by customer gender
sales_by_gender = df.groupby('Customer Gender')['Total Sales'].sum().sort_values(ascending=False)
print("\nTotal Sales by Customer Gender:")
print(sales_by_gender)

# Price average by product category
average_price_by_category = df.groupby('Category')['Price'].mean().sort_values(ascending=False)
print("\nAverage Price by Product Category:")
print(average_price_by_category)

# Visualizing the total sales by product category
plt.figure(figsize=(12, 6))
sales_by_category.plot(kind='pie', color='skyblue', autopct='%1.1f%%', startangle=140)
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.savefig('/Users/despoinaiapona/Downloads/archive/total_sales_by_category.png')
plt.show()

# Visualizing the total sales by customer gender
plt.figure(figsize=(8, 6))
sales_by_gender.plot(kind='bar', color='lightgreen')
plt.title('Total Sales by Customer Gender')
plt.xlabel('Customer Gender')
plt.ylabel('Total Sales')
plt.savefig('/Users/despoinaiapona/Downloads/archive/total_sales_by_gender.png')
plt.show()

# Visualizing the average price by product category
plt.figure(figsize=(12, 6))
average_price_by_category.plot(kind='line', color='salmon')
plt.title('Average Price by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Average Price')
plt.savefig('/Users/despoinaiapona/Downloads/archive/average_price_by_category.png')
plt.show()