import pandas as pd

dfk1 = {
    "Name": ["Aman", "Riya", "Rahul", "Aman"],
    "Age": [20, 19, 21, 20]
}

dfk2 = {
    "Name": ["Priya", "Karan"],
    "Age": [20, 22]
}

df1 = pd.DataFrame(dfk1)
df2 = pd.DataFrame(dfk2)

print(df1)
print(df2)

# Combine DataFrames row-wise
result = pd.concat([df1, df2], axis=0)
print(result)

# Combine DataFrames column-wise
result1 = pd.concat([df1, df2], axis=1)
print(result1)

# Reset the index after combining rows
result2 = pd.concat([df1, df2], ignore_index=True)
print(result2)

# Output:
#     Name  Age
# 0   Aman   20
# 1   Riya   19
# 2  Rahul   21
# 3   Aman   20
#     Name  Age
# 0  Priya   20
# 1  Karan   22
#     Name  Age
# 0   Aman   20
# 1   Riya   19
# 2  Rahul   21
# 3   Aman   20
# 0  Priya   20
# 1  Karan   22
#     Name   Age   Name   Age
# 0   Aman  20.0  Priya  20.0
# 1   Riya  19.0  Karan  22.0
# 2  Rahul  21.0    NaN   NaN
# 3   Aman  20.0    NaN   NaN
#     Name  Age
# 0   Aman   20
# 1   Riya   19
# 2  Rahul   21
# 3   Aman   20
# 4  Priya   20
# 5  Karan   22
