<div align="center">

# 📊 Pandas CSV & JSON File Operations 📂

</div>

## 📖 Overview
This project demonstrates how to **store, retrieve, and analyze structured data using Pandas**, leveraging **CSV and JSON file formats**. It covers **creating, saving, and reading DataFrames**, along with **basic data exploration techniques**.

## 🔑 Key Features
- **Creating Pandas DataFrames (`pd.DataFrame()`).**
- **Exporting data to CSV (`to_csv()`).**
- **Exporting data to JSON (`to_json()`).**
- **Reading data from CSV and JSON files (`read_csv()`, `read_json()`).**
- **Exploring datasets (`head()`, `tail()`, `sample()`, `describe()`, `max()`).**

## 💻 Code Breakdown
```python
import pandas as pd

# Creating a DataFrame with employee information
df1 = pd.DataFrame(
    {
        "Employee Name": [
            "Jad",
            "Shan",
            "Jim",
            "Kevin",
            "Dave",
            "Jack",
            "Dan",
        ],
        "Title": [
            "EUS Engineer",
            "Platforms Developer",
            "CEO",
            "Platforms Developer",
            "KDB Developer",
            "DevOps Engineer",
            "Senior EUS Engineer",
        ],
        "Salary": [40000, 150000, 1000000, 125000, 100000, 70000, 65000],
    }
)

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

6. **Exploring Data (`head()`, `tail()`, `sample()`, `describe()`, `max()`)**
   - `.head()` → Displays the **first 5 rows**.
   - `.tail()` → Displays the **last 5 rows**.
   - `.sample(n)` → Displays **random rows**.
   - `.describe()` → Shows **statistical summary** like **mean, min, max, and standard deviation**.
   - `.max()` → Retrieves the **highest salary** from the dataset.

## 🚀 Why Use Pandas for Data Analysis?
✅ **CSV is lightweight & human-readable** – Ideal for structured tabular data.  
✅ **JSON is flexible & widely used in APIs** – Supports **nested data** structures.  
✅ **Data exploration tools** – Quickly analyze trends, distributions, and statistics.  
✅ **Essential for financial & business applications** – Used for managing salaries, employee records, and reporting.  

## 🔥 Future Enhancements
- ✅ Implement **Excel file handling (`to_excel()`, `read_excel()`)**.
- ✅ Use **Pandas filtering & sorting** to enhance data retrieval.
- ✅ Integrate **real-world financial data processing** using APIs.

## 🎯 Summary
This **Pandas CSV & JSON project** introduces **data storage, retrieval, and basic data exploration techniques**. It enables efficient **data management for business applications, financial analysis, and reporting**.

Happy Coding! 🚀🐍
