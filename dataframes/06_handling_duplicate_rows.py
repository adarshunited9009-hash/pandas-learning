import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Aman"],
    "Age": [20, 19, 21, 20],
    "Marks": [85, 92, 78, 85]
}

df = pd.DataFrame(data)

print(df)

# Check for duplicate rows
print(df.duplicated())

# Count the duplicate rows
print(df.duplicated().sum())

# Remove duplicate rows
print(df.drop_duplicates())

# Output:
#     Name  Age  Marks
# 0   Aman   20     85
# 1   Riya   19     92
# 2  Rahul   21     78
# 3   Aman   20     85
# 0    False
# 1    False
# 2    False
# 3     True
# dtype: bool
# 1
#     Name  Age  Marks
# 0   Aman   20     85
# 1   Riya   19     92
# 2  Rahul   21     78
