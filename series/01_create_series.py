import pandas as pd

s = [1, 1, 2, 3, 4, 5, 4, 4, 4, 5, 6, 68]

result = pd.Series(s)
print(result)

# Output:
# 0      1
# 1      1
# 2      2
# 3      3
# 4      4
# 5      5
# 6      4
# 7      4
# 8      4
# 9      5
# 10     6
# 11    68
# dtype: int64
