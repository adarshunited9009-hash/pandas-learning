import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya", "Karan"],
    "City": ["Indore", "Bhopal", "Indore", "Bhopal", "Indore"],
    "Marks": [85, 92, 78, 95, 88]
}

df = pd.DataFrame(data)

print(df)

# Group students by city
result = df.groupby("City")

# Calculate statistics for Marks in each city
print(result["Marks"].mean())
print(result["Marks"].sum())
print(result["Marks"].max())
print(result["Marks"].min())
print(result["Marks"].count())

# Find average marks by city and sort from highest to lowest
result1 = df.groupby("City")["Marks"].mean()
print(result1.sort_values(ascending=False))

# Output:
#     Name     City  Marks
# 0   Aman   Indore     85
# 1   Riya   Bhopal     92
# 2  Rahul   Indore     78
# 3  Priya   Bhopal     95
# 4  Karan   Indore     88
#
# City
# Bhopal    93.500000
# Indore    83.666667
# Name: Marks, dtype: float64
# City
# Bhopal    187
# Indore    251
# Name: Marks, dtype: int64
# City
# Bhopal    95
# Indore    88
# Name: Marks, dtype: int64
# City
# Bhopal    92
# Indore    78
# Name: Marks, dtype: int64
# City
# Bhopal    2
# Indore    3
# Name: Marks, dtype: int64
# City
# Bhopal    93.500000
# Indore    83.666667
# Name: Marks, dtype: float64
