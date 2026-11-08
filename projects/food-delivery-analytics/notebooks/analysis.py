import pandas as pd

# Load the food delivery dataset
df = pd.read_csv("data/food_orders.csv")

# -------------------------
# 1. Explore the dataset
# -------------------------
print("First five orders:")
print(df.head())

print("\nDataset summary:")
print(df.describe())

print("\nDataset shape:", df.shape)
print("\nMissing values in each column:")
print(df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

# -------------------------
# 2. Order value analysis
# -------------------------
high_value_orders = df[df["item_total"] > 500]
low_value_orders = df[df["item_total"] < 200]

print("\nHigh-value orders:")
print(high_value_orders)
print("Total high-value orders:", high_value_orders.shape[0])

print("\nLow-value orders:")
print(low_value_orders)
print("Total low-value orders:", low_value_orders.shape[0])

print("Total food sales:", df["item_total"].sum())
print("Average order value:", df["item_total"].mean())

# -------------------------
# 3. City and cuisine analysis
# -------------------------
city_count = df["city"].value_counts()
cuisine_count = df["cuisine"].value_counts()

print("\nOrders by city:")
print(city_count.sort_values(ascending=False))

print("\nOrders by cuisine:")
print(cuisine_count)

city_analysis = df.groupby("city")["item_total"].agg(
    ["sum", "mean", "max", "min", "count"]
).sort_values("sum", ascending=False)

print("\nCity-wise sales analysis:")
print(city_analysis)

# -------------------------
# 4. Restaurant analysis
# -------------------------
restaurant_revenue = (
    df.groupby("restaurant")["item_total"]
    .sum()
    .sort_values(ascending=False)
)

restaurant_order_count = (
    df.groupby("restaurant")
    .size()
    .sort_values(ascending=False)
)

restaurant_delivery_time = (
    df[df["order_status"] == "Delivered"]
    .groupby("restaurant")["delivery_time"]
    .mean()
    .sort_values()
)

print("\nTop five restaurants by food sales:")
print(restaurant_revenue.head(5))

print("\nTop five restaurants by order count:")
print(restaurant_order_count.head(5))

print("\nFive fastest restaurants by average delivery time:")
print(restaurant_delivery_time.head(5))

# -------------------------
# 5. Cancellation analysis
# -------------------------
cancelled_orders = df[df["order_status"] == "Cancelled"]
delivered_orders = df[df["order_status"] == "Delivered"]

total_orders = df.shape[0]
cancelled_count = cancelled_orders.shape[0]
cancellation_rate = (cancelled_count / total_orders) * 100

print("\nTotal cancelled orders:", cancelled_count)
print("Cancellation rate: {:.2f}%".format(cancellation_rate))
print("\nOrder status counts:")
print(df["order_status"].value_counts())

city_cancellations = cancelled_orders.groupby("city").size()
city_total_orders = df.groupby("city").size()
city_cancellation_rate = (
    city_cancellations.div(city_total_orders).mul(100).fillna(0)
).sort_values(ascending=False)

print("\nCancelled orders by city:")
print(city_cancellations.sort_values(ascending=False))

print("\nCancellation rate by city:")
print(city_cancellation_rate)

# -------------------------
# 6. Payment method analysis
# -------------------------
payment_count = df["payment_method"].value_counts()
payment_percentage = (payment_count / total_orders) * 100

print("\nOrders by payment method:")
print(payment_count)

print("\nPayment method percentages:")
print(payment_percentage.round(2))

print("Most popular payment method:", payment_count.idxmax())

# -------------------------
# 7. Discount analysis
# -------------------------
discounted_orders = df[df["discount"] > 0]
non_discounted_orders = df[df["discount"] == 0]

print("\nAverage discounted order value:",
      round(discounted_orders["item_total"].mean(), 2))
print("Average non-discounted order value:",
      round(non_discounted_orders["item_total"].mean(), 2))
print("Total discounts given:", df["discount"].sum())

# This is the amount after subtracting the discount.
df["final_amount"] = df["item_total"] - df["discount"]

# -------------------------
# 8. Customer rating analysis
# -------------------------
restaurant_rating = (
    df.groupby("restaurant")["rating"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage customer rating:", df["rating"].mean())
print("Available ratings:", df["rating"].count())
print("Missing ratings:", df["rating"].isna().sum())
print("\nAverage rating by restaurant:")
print(restaurant_rating)

print("Highest-rated restaurant:", restaurant_rating.idxmax())
print("Lowest-rated restaurant:", restaurant_rating.idxmin())

# -------------------------
# 9. Delivery time analysis
# -------------------------
print("\nAverage delivery time:",
      delivered_orders["delivery_time"].mean())
print("Fastest delivery:",
      delivered_orders["delivery_time"].min())
print("Longest delivery:",
      delivered_orders["delivery_time"].max())

print("\nMissing delivery times by order status:")
print(
    df.groupby("order_status")["delivery_time"]
    .apply(lambda values: values.isna().sum())
)

# -------------------------
# 10. Overall business summary
# -------------------------
print("\nOverall business summary")
print("Total orders:", total_orders)
print("Delivered orders:", delivered_orders.shape[0])
print("Cancelled orders:", cancelled_count)
print("Total food sales:", round(df["item_total"].sum(), 2))
print("Average order value:", round(df["item_total"].mean(), 2))
print("Total discounts:", round(df["discount"].sum(), 2))
print("Total delivery fees:", round(df["delivery_fee"].sum(), 2))

# Note: item_total is food-item value before subtracting discounts.
# It should not be described as net revenue without checking the dataset definition.
