import pandas as pd

data = {
    "Name": ["aman", "riya", "rahul", "priya", "karan"],
    "Age": [20, 19, 21, 20, 21],
    "marks": [85, 92, 78, 95, 88],
    "subject": ["python", "maths", "python", "ai", "oops"]
}

df = pd.DataFrame(data)

print(df)
print(df.columns)
print(df.shape)
print(df.head(3))
print(df.tail(2))
print(df.info())

# Output:
#     Name  Age  marks  subject
# 0   aman   20     85   python
# 1   riya   19     92    maths
# 2  rahul   21     78   python
# 3  priya   20     95       ai
# 4  karan   21     88     oops
# Index(['Name', 'Age', 'marks', 'subject'], dtype='object')
# (5, 4)
#     Name  Age  marks subject
# 0   aman   20     85  python
# 1   riya   19     92   maths
# 2  rahul   21     78  python
#     Name  Age  marks subject
# 3  priya   20     95      ai
# 4  karan   21     88    oops
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 4 columns):
#  #   Column   Non-Null Count  Dtype
# ---  ------   --------------  -----
#  0   Name     5 non-null      object
#  1   Age      5 non-null      int64
#  2   marks    5 non-null      int64
#  3   subject  5 non-null      object
# dtypes: int64(2), object(2)
# memory usage: 292.0+ bytes
# None
