import pandas as pd

marks = pd.Series([85, 90, 78, 92, 88], index=["riya", "priya", "palak", "sam", "sia"])

print(marks["riya"])
print(marks["priya"])
print(marks)

# Output:
# 85
# 90
# riya     85
# priya    90
# palak    78
# sam      92
# sia      88
# dtype: int64
