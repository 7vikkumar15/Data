import pandas as pd

# Sample Data
data = {
    "Name": ["Rahul", "Aman", "Priya", "Sneha", "Riya"],
    "Age": [15, 16, 15, 14, 16],
    "Marks": [85, 90, 78, 88, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Display first 3 rows
print("\nFirst 3 Rows:")
print(df.head(3))

# Display column names
print("\nColumn Names:")
print(df.columns)

# Add new column
df["Grade"] = ["A", "A+", "B", "A", "A+"]

print("\nData After Adding Grade Column:")
print(df)

# Filter students with marks greater than 80
print("\nStudents with Marks > 80:")
print(df[df["Marks"] > 80])

# Average Marks
print("\nAverage Marks:")
print(df["Marks"].mean())