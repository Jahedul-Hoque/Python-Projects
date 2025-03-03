import pandas as pd

# Creating a DataFrame with employee information
df1 = pd.DataFrame({
    "Employee Name": ["Jad", "Shan", "Jim", "Kevin", "Dave", "Jack", "Dan"],
    "Title": ["EUS Engineer", "Platforms Developer", "CEO", "Platforms Developer", "KDB Developer", "DevOps Engineer", "Senior EUS Engineer"],
    "Salary": [40000, 150000, 1000000, 125000, 100000, 70000, 65000]
})

# Save DataFrame to a CSV file
df1.to_csv("My_CSV_File", index=None)

# Read and print CSV file
print(pd.read_csv("My_CSV_File"), "\n")

# Save DataFrame to a JSON file
df1.to_json("My_JSON_File", index=None)

# Read and print JSON file
print(pd.read_json("My_JSON_File"), "\n")

# Displaying the first 5 rows
print(df1.head(), "\n")

# Displaying the last 5 rows
print(df1.tail(), "\n")

# Displaying 2 random rows
print(df1.sample(2), "\n")

# Displaying statistical summary of numerical columns
print(df1.describe(), "\n")

# Printing the maximum salary
print(df1["Salary"].max())