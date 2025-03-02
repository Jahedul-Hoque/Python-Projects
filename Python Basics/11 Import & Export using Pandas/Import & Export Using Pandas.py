import pandas as pd

# Creating a DataFrame with employee information
df1 = pd.DataFrame({
    "Employee Name": ["Jad", "Shan", "Jim", "Kevin"],
    "Title": ["EUS Engineer", "Platforms Developer", "CEO", "Platforms Developer"],
    "Salary": [40000, 150000, 1000000, 125000]
})

# Save DataFrame to a CSV file
df1.to_csv("My_CSV_File", index=None)

# Read and print CSV file
print(pd.read_csv("My_CSV_File"))

# Save DataFrame to a JSON file
df1.to_json("My_JSON_File", index=None)

# Read and print JSON file
print(pd.read_json("My_JSON_File"))