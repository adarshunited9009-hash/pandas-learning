import pandas as pd

data = {
    "name": ["Aman", "Riya", "Rahul", "Aman", "Riya"],
    "age": [20, 18, 21, 20, 18],
    "marks": [85, 92, 78, 85, 92],
    "city": ["Delhi", "Mumbai", "Bangalore", "Delhi", "Mumbai"]
}

df = pd.DataFrame(data)
print(df)

# Display duplicate rows
print("\nDuplicated data are:")
print(df[df.duplicated()])

# Count duplicate rows
print("\nNumber of duplicated rows:")
print(df.duplicated().sum())

# Remove duplicate rows
print("\nUnique data are:")
dp = df.drop_duplicates()
print(dp)

# Save unique rows to a CSV file
dp.to_csv("unique_data.csv", index=False)
print("\nUnique data saved successfully in CSV file.")

# Output:
#     name  age  marks       city
# 0   Aman   20     85      Delhi
# 1   Riya   18     92     Mumbai
# 2  Rahul   21     78  Bangalore
# 3   Aman   20     85      Delhi
# 4   Riya   18     92     Mumbai
#
# Duplicated data are:
#    name  age  marks    city
# 3  Aman   20     85   Delhi
# 4  Riya   18     92  Mumbai
#
# Number of duplicated rows:
# 2
#
# Unique data are:
#     name  age  marks       city
# 0   Aman   20     85      Delhi
# 1   Riya   18     92     Mumbai
# 2  Rahul   21     78  Bangalore
#
# Unique data saved successfully in CSV file.
