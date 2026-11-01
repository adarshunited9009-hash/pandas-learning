import pandas as pd

marks = pd.Series([85, 90, 78, 92, 88],
                  index=["riya", "priya", "palak", "sam", "siya"])

print(marks)
print(marks[["riya"]])
print(marks.loc["siya"])
print(marks.iloc[4])
print(marks.loc["sam"])

# Output:
# riya     85
# priya    90
# palak    78
# sam      92
# siya     88
# dtype: int64
# riya    85
# dtype: int64
# 88
# 88
# 92
