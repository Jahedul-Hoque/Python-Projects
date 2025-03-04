employeeInfo = {
    "name": "Shan",
    "Title": "CEO of Schonfeld",
    "Favourite Coding Languages": ["C++", "Python"],
    "Salary": 10000000,
}

print(employeeInfo, "\n")

print(employeeInfo["name"], "is currently coding right now. \n")

print(
    employeeInfo["name"], "earns approximately $", employeeInfo["Salary"], "\n"
)
# prints key of employeeInfo name and salary

print(employeeInfo.get("Location", "Location not found"), "\n")
# setting default values

EmployeeName = employeeInfo.pop("name")
print(
    "The employees name that you've popped out of the dictionary is",
    EmployeeName,
    "\n",
)

employeeInfo.update({"name": "Shan"})

print("Number of keys in dictionary:", len(employeeInfo), "\n")

print(employeeInfo.keys(), "\n")

print()
print()

for key, value in employeeInfo.items():
    print(key, ":", value, "\n")
    # loops through array and outputs key and value
