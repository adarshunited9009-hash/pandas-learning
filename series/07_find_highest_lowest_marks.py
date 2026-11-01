import pandas as pd

marks = pd.Series([89, 67, 45, 90, 23],
                  index=["rahul", "john", "badie", "karlos", "country"])

print(marks.max())
print("topper :", marks.idxmax())
print(marks.min())
print("lowest :", marks.idxmin())

# Output:
# 90
# topper : karlos
# 23
# lowest : country
