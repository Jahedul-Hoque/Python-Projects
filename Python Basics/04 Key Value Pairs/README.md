<div align="center">

# 🏢 Employee Information Dictionary 📊

</div>

## 📖 Overview
This project demonstrates **dictionary operations in Python** for managing employee data. It covers **key-value retrieval, updating values, removing entries, looping through dictionary items, and handling missing keys with default values**.

## 🔑 Key Features
- **Dictionary Operations:** Retrieve, modify, add, and remove employee data.
- **Using `.get()` for default values** when keys do not exist.
- **Looping through dictionaries (`.items()`)** for structured output.
- **Dynamic key-value updates using `.update()`**.

## 💻 Code Breakdown
```python
# Employee information stored in a dictionary
employeeInfo = {
    'name': 'Shan',
    'Title': "CEO of Schonfeld",
    "Favourite Coding Languages": ["C++", "Python"],
    "Salary": 10000000
}

# Print entire dictionary
print(employeeInfo, "\n")

# Access specific dictionary keys
print(employeeInfo["name"], "is currently coding right now. \n")
print(employeeInfo["name"], "earns approximately $", employeeInfo["Salary"], "\n")

# Using .get() to handle missing keys
print(employeeInfo.get("Location", "Location not found"), "\n")

# Removing a key-value pair using .pop()
EmployeeName = employeeInfo.pop("name")
print("The employee's name that you've popped out of the dictionary is", EmployeeName, "\n")

# Updating dictionary with a new value
employeeInfo.update({"name": "Shan"})

# Dictionary length and keys
print("Number of keys in dictionary:", len(employeeInfo), "\n")
print(employeeInfo.keys(), "\n")

# Loop through dictionary and print key-value pairs
for key, value in employeeInfo.items():
    print(key, ":", value, "\n")
```

## 🔍 Explanation
1. **Retrieving Dictionary Values (`employeeInfo[key]`)**
   - Accesses employee name, title, and salary.

2. **Handling Missing Keys (`.get()`)**
   - Avoids key errors by providing a **default fallback value**.

3. **Modifying and Removing Data**
   - **`.pop("name")`** removes the employee's name from the dictionary.
   - **`.update({"name": "Shan"})`** re-adds the name.

4. **Looping Through Dictionary (`.items()`)**
   - Prints all key-value pairs dynamically.

## 🚀 Why Use Dictionaries?
✅ **Efficient key-value data storage** – Fast lookups and modifications.  
✅ **Dynamic and flexible** – Easily update or remove entries.  
✅ **Prevents key errors** – `.get()` ensures safe retrieval of missing values.  

## 🔥 Future Enhancements
- ✅ Store and retrieve **multiple employee records** dynamically.
- ✅ Integrate with **JSON storage for persistence**.
- ✅ Implement **sorting based on salary or experience**.

## 🎯 Summary
This **Python employee information project** explores **dictionary operations**, enabling **efficient retrieval, modification, and iteration** of structured employee data. The script showcases key-value handling for **real-world data processing**.

Happy Coding! 🚀🐍

