import matplotlib as mp
import pandas as pd

# Creating a DataFrame with employee information
df1 = pd.DataFrame({
    "Employee Name": ["Jad", "Shan", "Jim", "Kevin", "Dave", "Jack", "Dan","Sanjay", "Tilly", "Metin", "George"],
    "Title": ["EUS Engineer", "Platforms Developer", "CEO", "Platforms Developer", "KDB Developer", "DevOps Engineer", "Senior EUS Engineer", "Facilities Manager", "Workplace Support", "Software Engineer", "Senior Software Engineer"],
    "Salary": [40000, 150000, 1000000, 125000, 100000, 70000, 65000, 45000, 35000, 100000, 120000]
})

print(df1)