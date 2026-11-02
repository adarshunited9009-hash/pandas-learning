import pandas as pd

# Read student data from a CSV file
df = pd.read_csv("student.csv")
print(df)

# Select students who scored more than 85 marks
result = df[df["Marks"] > 85]
print(result)

# Save the filtered data into a new CSV file
result.to_csv("filtered_data.csv", index=False)
print("Filtered data saved successfully")

# Output depends on the contents of student.csv.
