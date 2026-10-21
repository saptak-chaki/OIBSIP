import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Simulating Retail Sales Dataset
np.random.seed(42)
n_rows = 200
data = {
    'Date': pd.date_range(start='2026-01-01', periods=n_rows, freq='D'),
    'Category': np.random.choice(['Electronics', 'Clothing', 'Home Appliances', 'Groceries'], n_rows),
    'Unit_Price': np.random.uniform(20, 1000, n_rows),
    'Quantity': np.random.randint(1, 10, n_rows),
    'Customer_Rating': np.random.randint(1, 6, n_rows)
}

df = pd.DataFrame(data)
df['Total_Revenue'] = df['Unit_Price'] * df['Quantity']

print("--- 1. Dataset Head ---")
print(df.head(), "\n")

print("--- 2. Dataset Summary Statistics ---")
print(df.describe(), "\n")

# 3. Category-wise Total Revenue
category_revenue = df.groupby('Category')['Total_Revenue'].sum().reset_index()
print("--- 3. Total Revenue by Category ---")
print(category_revenue, "\n")

# 4. Visualization
plt.figure(figsize=(9, 5))
sns.barplot(x='Category', y='Total_Revenue', data=category_revenue, palette='mako')
plt.title('Total Revenue Generation by Product Category', fontsize=12, fontweight='bold')
plt.xlabel('Product Category', fontsize=10)
plt.ylabel('Total Revenue ($)', fontsize=10)
plt.show()