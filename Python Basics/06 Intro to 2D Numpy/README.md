<div align="center">

# 📊 Python NumPy Array Operations 📈

</div>

## 📖 Overview
This project demonstrates how to create, manipulate, and analyze **NumPy arrays** in Python. It covers **array dimensions, shapes, data types, slicing, and memory usage** for efficient numerical computations.

## 🔑 Key Features
- **Creating 1D and 2D NumPy arrays**
- **Retrieving dimensions (`ndim`) and shapes (`shape`)**
- **Checking data types (`dtype`) and memory usage (`nbytes`)**
- **Slicing and modifying array elements**

## 💻 Code Breakdown
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print("a:", a, "\n", "b:", b, "\n")
# makes 1d and 2d array and prints them both

adim = a.ndim
print("a has a dimension of", adim, "\n")
# a has a dimension of 1

bdim = b.ndim
print("b has a dimension of", bdim, "\n")
# b has a dimension of 2


ashape = a.shape
print("a has a shape of", ashape, "\n")
# ashape has a shape of 3 collumns + 1 invisible row

bshape = b.shape
print("b has a shape of", bshape, "\n")
# bshape has a shape of 3 collumns and 2 rows

print("a has a data type of ", a.dtype, "\n")
# 64 bits or 8 bytes of an integer64 by default

print("b has a data type of ", b.dtype, "\n")
# 64 bits or 8 bytes of a float64 by default

print(b.nbytes, "\n")
# this prints out number of bytes (6 elements * 8 = 48 bytes)

new_array = np.array(
    [
        [
            1,
            2,
            3,
            4,
            5,
        ],
        [6, 7, 8, 9, 10],
    ],
    "\n",
)
print("New Array:", new_array, "\n")
print("Number of elements in New Array:", new_array.size, "\n")
print(new_array[0, 1:4:1])
# print the 0th vectored row (1,2,3,4,5) and then start from the 
# .. 1st index until the 4th index(5) and step by 1 which is 4.
# that should be 2,3,4

new_array[1, 3] = 100
print(new_array)
# should print the 4th element of the second row as 100

```

## 🔍 Explanation
1. **Array Creation (`np.array()`)**
   - Defines both **1D and 2D arrays**.

2. **Array Properties (`ndim`, `shape`, `dtype`)**
   - Retrieves **number of dimensions** and **shape** of the arrays.
   - Checks **data type** to determine memory efficiency.

3. **Memory Usage (`nbytes`)**
   - Computes memory consumption by multiplying **element count by element size**.

4. **Array Slicing (`[row, start:end:step]`)**
   - Extracts elements efficiently without loops.

5. **Modifying Elements (`array[row, col] = value`)**
   - Updates individual elements dynamically.

## 🚀 Why Use NumPy Arrays?
✅ **Faster numerical operations** – Uses contiguous memory and vectorized computations.  
✅ **Lower memory overhead** – Avoids Python object overhead present in lists.  
✅ **Efficient slicing and element-wise operations** – No need for explicit loops.  
✅ **Scalable for large datasets** – Optimized for machine learning and financial analytics.  

## 🔥 Future Enhancements
- ✅ Implement **NumPy arithmetic operations** on arrays.
- ✅ Compare **array broadcasting vs traditional loops** for performance. 
- ✅ Use **NumPy functions (`sum()`, `mean()`, `std()`)** for financial calculations.

## 🎯 Summary
This **Python NumPy project** covers **array creation, dimensions, slicing, and memory analysis** for high-performance numerical computing. The structured data handling in NumPy makes it a powerful tool for **financial modeling, machine learning, and scientific computing**.

Happy Coding! 🚀🐍

