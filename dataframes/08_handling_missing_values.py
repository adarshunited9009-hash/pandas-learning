import pandas as pd
import numpy as np

data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya", "Karan"],
    "Age": [20, 19, np.nan, 20, 22],
    "Marks": [85, np.nan, 78, 95, np.nan]
}

df = pd.DataFrame(data)

print(df)

# Check which values are missing
missing_value = df.isnull()
print(missing_value)

# Count missing values in each column
print("\nNumber of missing values:", df.isnull().sum())

# Replace missing marks with 0
df["Marks"] = df["Marks"].fillna(0)
print(df)

# Replace missing ages with the mean age
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df)

# Output:
#      Name   Age  Marks
# 0    Aman  20.0   85.0
# 1    Riya  19.0    NaN
# 2   Rahul   NaN   78.0
# 3   Priya  20.0   95.0
# 4   Karan  22.0    NaN
#
#     Name    Age  Marks
# 0  False  False  False
# 1  False  False   True
# 2  False   True  False
# 3  False  False  False
# 4  False  False   True
#
# Number of missing values: Name     0
# Age      1
# Marks    2
# dtype: int64
#
#      Name   Age  Marks
# 0    Aman  20.0   85.0
# 1    Riya  19.0    0.0
# 2   Rahul   NaN   78.0
# 3   Priya  20.0   95.0
# 4   Karan  22.0    0.0
#
#      Name    Age  Marks
# 0    Aman  20.00   85.0
# 1    Riya  19.00    0.0
# 2   Rahul  20.25   78.0
# 3   Priya  20.00   95.0
# 4   Karan  22.00    0.0
