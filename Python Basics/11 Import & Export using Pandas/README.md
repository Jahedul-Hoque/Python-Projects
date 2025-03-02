<div align="center">

# 📊 Pandas CSV & JSON File Operations 📂

</div>

## 📖 Overview
This project demonstrates how to **store and retrieve structured data using Pandas**, leveraging **CSV and JSON file formats**. It covers **creating, saving, and reading DataFrames** for efficient data management.

## 🔑 Key Features
- **Creating Pandas DataFrames (`pd.DataFrame()`).**
- **Exporting data to CSV (`to_csv()`).**
- **Exporting data to JSON (`to_json()`).**
- **Reading data from CSV and JSON files (`read_csv()`, `read_json()`).**

## 💻 Code Breakdown
```python
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
```

## 🔍 Explanation
1. **Creating a Pandas DataFrame (`pd.DataFrame()`)**
   - Stores **employee details** including names, titles, and salaries.

2. **Saving Data to CSV (`to_csv()`)**
   - Converts the DataFrame into a **comma-separated values (CSV) file**.

3. **Reading Data from CSV (`read_csv()`)**
   - Loads the **saved CSV file** back into a DataFrame.

4. **Saving Data to JSON (`to_json()`)**
   - Converts the DataFrame into a **JSON format file**.

5. **Reading Data from JSON (`read_json()`)**
   - Loads the **saved JSON file** back into a DataFrame.

## 🚀 Why Use CSV & JSON for Data Storage?
✅ **CSV is lightweight & human-readable** – Ideal for structured tabular data.  
✅ **JSON is flexible & widely used in APIs** – Supports **nested data** structures.  
✅ **Easy to store and retrieve** – Enables efficient **data persistence**.  
✅ **Essential for financial & business applications** – Used for storing employee records, trade data, and reports.  

## �� Future Enhanimport pandas as pd

df1 = pd.DataFrame({
"Employee Name": ["Jad", "Shan", "Jim", "Kevin"],
"Title": ["EUS Engineer", "Platforms Developer", "CEO", "Platforms Developer"],
"Salary": [40000, 150000, 1000000, 125000]

})

df1.to_csv("My_CSV_File", index=None)
# Creates CSV File

print(pd.read_csv("My_CSV_File"))
# Reads CSV File

df1.to_json("My_JSON_File", index=None)
# Creates JSON File

print(pd.read_json("My_JSON_File"))
# Reads JSON Filecements
- ✅ Implement **Excel file handling (`to_excel()`, `read_excel()`)**.
- ✅ Use **Pandas filtering & sorting** to enhance data retrieval.
- ✅ Integrate **real-world financial data processing** using APIs.

## 🎯 Summary
This **Pandas CSV & JSON project** introduces **data storage, retrieval, and file handling**. It enables efficient **data management for business applications, financial analysis, and reporting**.

Happy Coding! 🚀🐍
