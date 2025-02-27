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

# Creating 1D and 2D NumPy arrays
a = np.array([1, 2, 3])
b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print("a:", a, "\n", "b:", b, "\n")

# Retrieving array dimensions
adim = a.ndim
print("a has a dimension of", adim, "\n")

bdim = b.ndim
print("b has a dimension of", bdim, "\n")

# Retrieving array shapes
ashape = a.shape
print("a has a shape of", ashape, "\n")

bshape = b.shape
print("b has a shape of", bshape, "\n")

# Checking data types
dtype_a = a.dtype
print("a has a data type of", dtype_a, "\n")

dtype_b = b.dtype
print("b has a data type of", dtype_b, "\n")

# Memory usage
print("b uses", b.nbytes, "bytes of memory\n")

# Creating a new array and analyzing its elements
newArray = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("New Array:", newArray, "\n")
print("Number of elements in New Array:", newArray.size, "\n")

# Slicing an array segment
print(newArray[0, 1:4:1])  # Extracts elements 2, 3, and 4 from the first row

# Modifying an array element
newArray[1, 3] = 100
print(newArray)
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

