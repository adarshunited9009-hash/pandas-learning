import pandas as pd

data = {
    "Name": ["Aman", "Riya", "Rahul", "Priya", "Karan"],
    "Age": [20, 19, 21, 20, 22],
    "Marks": [85, 92, 78, 95, 88]
}

df = pd.DataFrame(data)

print(df)
print(df.sort_values(by="Marks"))
print(df.sort_values(by=["Marks", "Age"]))
print(df.sort_values(by="Marks", ascending=False))

# Output:
#     Name  Age  Marks
# 0   Aman   20     85
# 1   Riya   19     92
# 2  Rahul   21     78
# 3  Priya   20     95
# 4  Karan   22     88
#     Name  Age  Marks
# 2  Rahul   21     78
# 0   Aman   20     85
# 4  Karan   22     88
# 1   Riya   19     92
# 3  Priya   20     95
#     Name  Age  Marks
# 2  Rahul   21     78
# 0   Aman   20     85
# 4  Karan   22     88
# 1   Riya   19     92
# 3  Priya   20     95
#     Name  Age  Marks
# 3  Priya   20     95
# 1   Riya   19     92
# 4  Karan   22     88
# 0   Aman   20     85
# 2  Rahul   21     78
