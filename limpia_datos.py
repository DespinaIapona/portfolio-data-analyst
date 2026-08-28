import numpy as np
import pandas as pd

# Load the dataset
df = pd.read_csv('/Users/despoinaiapona/Downloads/archive/ecommerce_sales_data.csv')

# Check the dataset structure
print(df.head())
print(df.info())
print(df.isnull().sum())

# Cleaning the dataset
print(df.drop_duplicates())
print(df.dropna())

# Check for unique values 
print(df['Customer Gender'].unique())
print(df['Category'].unique())

# Check statistics of numerical columns
print(df['Customer Age'].describe())
print(df['Price'].describe())
print(df['Quantity'].describe())

# Check for negative values in numerical columns
print((df['Customer Age'] < 0).sum())
print((df['Price'] < 0).sum())
print((df['Quantity'] < 0).sum())

# Check the distribution of categorical variables
print(df['Customer Gender'].value_counts())
print(df['Category'].value_counts())