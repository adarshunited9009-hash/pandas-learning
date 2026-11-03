import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya", "Karan"],
    "Marks": [85, 92, 45, 95, 60],
    "Age": [20, 19, 21, 20, 22]
}

df = pd.DataFrame(data)

# Convert names to uppercase
upp = df["Name"].map(str.upper)
print(upp)

# Add 6 marks to each student's marks
add = df["Marks"].apply(lambda x: x + 6)
print(add)

# Create a result column based on marks
df["result"] = df["Marks"].apply(
    lambda x: "pass" if x > 80 else "fail"
)
print(df)

# Assign a category based on marks
df["category"] = df["Marks"].map({
    85: "A",
    92: "A+",
    45: "C",
    95: "A+",
    60: "B"
})
print(df)

# Create an age group column
df["Age_group"] = df["Age"].apply(
    lambda x: "teenager" if x < 20 else "adult"
)
print(df)

# Output:
# 0     AMAN
# 1     RIYA
# 2    RAHUL
# 3    PRIYA
# 4    KARAN
# Name: Name, dtype: object
# 0    91
# 1    98
# 2    51
# 3    101
# 4    66
# Name: Marks, dtype: int64
#     Name  Marks  Age result
# 0   Aman     85   20   pass
# 1   Riya     92   19   pass
# 2  Rahul     45   21   fail
# 3  Priya     95   20   pass
# 4  Karan     60   22   fail
#     Name  Marks  Age result category
# 0   Aman     85   20   pass        A
# 1   Riya     92   19   pass       A+
# 2  Rahul     45   21   fail        C
# 3  Priya     95   20   pass       A+
# 4  Karan     60   22   fail        B
#     Name  Marks  Age result category Age_group
# 0   Aman     85   20   pass        A     adult
# 1   Riya     92   19   pass       A+  teenager
# 2  Rahul     45   21   fail        C     adult
# 3  Priya     95   20   pass       A+     adult
# 4  Karan     60   22   fail        B     adult
