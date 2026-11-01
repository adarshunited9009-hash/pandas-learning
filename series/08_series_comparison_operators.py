import pandas as pd

marks = pd.Series([76, 87, 89, 98, 77, 67])

print(marks > 70)
print(marks <= 70)
print(marks > 45)
print(marks <= 45)
print("failed :", marks <= 35)

# Output:
# 0    True
# 1    True
# 2    True
# 3    True
# 4    True
# 5   False
# dtype: bool
# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# 5     True
# dtype: bool
# 0    True
# 1    True
# 2    True
# 3    True
# 4    True
# 5    True
# dtype: bool
# 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# 5    False
# dtype: bool
# failed : 0    False
# 1    False
# 2    False
# 3    False
# 4    False
# 5    False
# dtype: bool
