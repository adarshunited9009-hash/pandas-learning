import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya", "Karan"],
    "Age": [20, 19, 21, 20, 22],
    "Marks": [85, 92, 78, 95, 88],
    "City": ["Indore", "Bhopal", "Delhi", "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

result3 = df[df["Age"] < 21]
result2 = df[(df["Marks"] > 80) & (df["Age"] > 19)]
result1 = df[(df["City"] == "Mumbai") | (df["City"] == "Pune")]
RESULT = df[df["Marks"].isin([85, 92, 95])]

print(RESULT)
print(result1)
print(result2)
print(result3)

# Output:
#     Name  Age  Marks    City
# 0   Aman   20     85  Indore
# 1   Riya   19     92  Bhopal
# 3  Priya   20     95  Mumbai
#     Name  Age  Marks    City
# 3  Priya   20     95  Mumbai
# 4  Karan   22     88    Pune
#     Name  Age  Marks    City
# 0   Aman   20     85  Indore
# 3  Priya   20     95  Mumbai
# 4  Karan   22     88    Pune
#     Name  Age  Marks    City
# 0   Aman   20     85  Indore
# 1   Riya   19     92  Bhopal
# 3  Priya   20     95  Mumbai
