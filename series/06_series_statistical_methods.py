import pandas as pd

marks = pd.Series([76, 87, 89, 98, 77, 67])

print(marks.mean())
print(marks.sum())
print(marks.max())
print(marks.min())
print(marks.count())

# Output:
# 82.33333333333333
# 494
# 98
# 67
# 6
