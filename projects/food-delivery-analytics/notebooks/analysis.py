import pandas as pd

# Load the food delivery dataset
df = pd.read_csv("../data/food_orders.csv")

# Get a quick look at the dataset
print(df.head())
print(df.describe())

# Find high-value orders
high_value_orders = df[df["item_total"] > 500]
print("Total number of high-value orders:", high_value_orders.shape[0])

# Find low-value orders
low_value_orders = df[df["item_total"] < 200]
print("Total number of low-value orders:", low_value_orders.shape[0])

# Count orders by city
city_count = df["city"].value_counts()
print("Number of orders from each city:")
print(city_count)

# Count orders by cuisine
cuisine_count = df["cuisine"].value_counts()
print("Number of orders for each cuisine:")
print(cuisine_count)

# Sort cities by order count, highest first
sorted_city = city_count.sort_values(ascending=False)
print("Cities sorted by number of orders:")
print(sorted_city)
