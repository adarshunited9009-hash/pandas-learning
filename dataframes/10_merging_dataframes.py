import pandas as pd

df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Aman", "Riya", "Rahul"]
})

df2 = pd.DataFrame({
    "ID": [2, 3, 4],
    "Marks": [92, 78, 95]
})

# Inner Join: keep IDs present in both DataFrames
print("INNER JOIN")
print(pd.merge(df1, df2, on="ID", how="inner"))

# Left Join: keep all IDs from df1
print("\nLEFT JOIN")
print(pd.merge(df1, df2, on="ID", how="left"))

# Right Join: keep all IDs from df2
print("\nRIGHT JOIN")
print(pd.merge(df1, df2, on="ID", how="right"))

# Outer Join: keep all IDs from both DataFrames
print("\nOUTER JOIN")
print(pd.merge(df1, df2, on="ID", how="outer"))

# Output:
# INNER JOIN
#    ID   Name  Marks
# 0   2   Riya     92
# 1   3  Rahul     78
#
# LEFT JOIN
#    ID   Name  Marks
# 0   1   Aman    NaN
# 1   2   Riya   92.0
# 2   3  Rahul   78.0
#
# RIGHT JOIN
#    ID   Name  Marks
# 0   2   Riya     92
# 1   3  Rahul     78
# 2   4    NaN     95
#
# OUTER JOIN
#    ID   Name  Marks
# 0   1   Aman    NaN
# 1   2   Riya   92.0
# 2   3  Rahul   78.0
# 3   4    NaN   95.0
