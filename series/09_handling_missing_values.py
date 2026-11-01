import pandas as pd
import numpy as np

marks = pd.Series([78, np.nan, 89, 45, np.nan, 95, 67])

print(marks)
print(marks.isnull())
print(marks.isnull().sum())
print(marks.notnull())
print(marks.notnull().sum())
print(marks.dropna())
print(marks.fillna(0))

avg = marks.mean()
print("Average marks:", avg)
print(marks.fillna(avg))

# Output:
# 0    78.0
# 1     NaN
# 2    89.0
# 3    45.0
# 4     NaN
# 5    95.0
# 6    67.0
# dtype: float64
# 0    False
# 1     True
# 2    False
# 3    False
# 4     True
# 5    False
# 6    False
# dtype: bool
# 2
# 0     True
# 1    False
# 2     True
# 3     True
# 4    False
# 5     True
# 6     True
# dtype: bool
# 5
# 0    78.0
# 2    89.0
# 3    45.0
# 5    95.0
# 6    67.0
# dtype: float64
# 0    78.0
# 1     0.0
# 2    89.0
# 3    45.0
# 4     0.0
# 5    95.0
# 6    67.0
# dtype: float64
# Average marks: 74.8
# 0    78.0
# 1    74.8
# 2    89.0
# 3    45.0
# 4    74.8
# 5    95.0
# 6    67.0
# dtype: float64
