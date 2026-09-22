import json
import pandas as pd
import os

df = pd.read_csv("data/sales.csv")

# Create a new column of total price

df['Total'] = df['price'] * df['quantity']

os.makedirs('output', exist_ok=True)

df.to_json('output/sales_data.csv')