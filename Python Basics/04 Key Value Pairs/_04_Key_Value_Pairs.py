employee_info = {
    "name": "Shan",
    "Title": "CEO of Schonfeld",
    "Favourite Coding Languages": ["C++", "Python"],
    "Salary": 10000000,
}

print(employee_info, "\n")

print(employee_info["name"], "is currently coding right now. \n")

print(
    employee_info["name"], "earns approximately $", employee_info["Salary"], "\n"
)
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
