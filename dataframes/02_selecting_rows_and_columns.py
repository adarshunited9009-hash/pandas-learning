import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya", "Karan"],
    "Age": [20, 19, 21, 20, 22],
    "Marks": [85, 92, 78, 95, 88],
    "City": ["Indore", "Bhopal", "Delhi", "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

print(df)
print(df["Marks"])
print(df[["Name", "City"]])
print(df.loc[0:2])
print(df.iloc[3:5])
print(df.loc[0:2, ["Name", "Marks"]])

# Output:
#     Name  Age  Marks    City
# 0   Aman   20     85  Indore
# 1   Riya   19     92  Bhopal
# 2  Rahul   21     78   Delhi
# 3  Priya   20     95  Mumbai
# 4  Karan   22     88    Pune
# 0    85
# 1    92
# 2    78
# 3    95
# 4    88
# Name: Marks, dtype: int64
#     Name    City
# 0   Aman  Indore
# 1   Riya  Bhopal
# 2  Rahul   Delhi
# 3  Priya  Mumbai
# 4  Karan    Pune
#     Name  Age  Marks    City
# 0   Aman   20     85  Indore
# 1   Riya   19     92  Bhopal
# 2  Rahul   21     78   Delhi
#     Name  Age  Marks    City
# 3  Priya   20     95  Mumbai
# 4  Karan   22     88    Pune
#     Name  Marks
# 0   Aman     85
# 1   Riya     92
# 2  Rahul     78
