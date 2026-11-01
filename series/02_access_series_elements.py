import pandas as pd

s = pd.Series(['maths', 'hindi', 'english', 'art', 'commerce', 'b',
               'accounts', 'physics', 'chemistry', 'biology', 'history', 'geography'])

print(s[2])
print(s[6])
print(s[0])
print(s[1])
print(s[8])

# Output:
# english
# accounts
# maths
# hindi
# chemistry
