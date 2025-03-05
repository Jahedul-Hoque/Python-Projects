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
employee_info = {
    "name": "Shan",
    "Title": "CEO of Schonfeld",
    "Favourite Coding Languages": ["C++", "Python"],
    "Salary": 10000000,
}

print(employee_info, "\n")

print(employee_info["name"], "is currently coding right now. \n")

print(employee_info["name"], "earns approximately $", employee_info["Salary"], "\n")
# prints key of employee_info name and salary

print(employee_info.get("Location", "Location not found"), "\n")
# setting default values

employee_name = employee_info.pop("name")
print(
    "The employees name that you've popped out of the dictionary is",
    employee_name,
    "\n",
)

employee_info.update({"name": "Shan"})

print("Number of keys in dictionary:", len(employee_info), "\n")

print(employee_info.keys(), "\n")

print()
print()

for key, value in employee_info.items():
    print(key, ":", value, "\n")
    # loops through array and outputs key and value

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

