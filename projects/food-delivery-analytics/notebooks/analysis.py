import pandas as pd

# Load the food delivery dataset
df = pd.read_csv("data/food_orders.csv")

# Get a quick look at the dataset
print(df.head())
print(df.describe())

# Find high-value and low-value orders
high_value_orders = df[df["item_total"] > 500]
print("Total number of high-value orders:", high_value_orders.shape[0])

low_value_orders = df[df["item_total"] < 200]
print("Total number of low-value orders:", low_value_orders.shape[0])

# Count orders by city and cuisine
city_count = df["city"].value_counts()
print("Number of orders from each city:")
print(city_count)

cuisine_count = df["cuisine"].value_counts()
print("Number of orders for each cuisine:")
print(cuisine_count)

# Sort cities by order count
sorted_city = city_count.sort_values(ascending=False)
print("Cities sorted by number of orders:")
print(sorted_city)

# Calculate total food sales and average order value by city
city_revenue = df.groupby("city")["item_total"].sum()
city_revenue_mean = df.groupby("city")["item_total"].mean()

print("Total food sales by city:")
print(city_revenue)

print("Average food order value by city:")
print(city_revenue_mean)

# Sort cities by total food sales
sorted_city_revenue = city_revenue.sort_values(ascending=False)
print("Cities sorted by total food sales:")
print(sorted_city_revenue)

# Calculate multiple statistics for each city
city_analysis = df.groupby("city")["item_total"].agg(
    ["sum", "mean", "max", "min", "count"]
)
print("City-wise sales summary:")
print(city_analysis)
