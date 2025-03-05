<div align="center">

# 📊 Python NumPy Array Creation & Operations 📈

</div>

## 📖 Overview
This project demonstrates various **NumPy array creation methods and mathematical operations**. It covers **zero and one matrices, full matrices, random arrays, repetitions, slicing, and element-wise arithmetic operations**.

## 🔑 Key Features
- **Creating predefined arrays** (zeros, ones, full, random values).
- **Repeating and reshaping arrays** using `repeat()`.
- **Modifying arrays using slicing and indexing**.
- **Performing element-wise arithmetic operations**.

## 💻 Code Breakdown
```python
import numpy as np

# Creating arrays with predefined values
a = np.zeros((2, 3))
print(a, "\n")  # Matrix of zeros (2x3)

b = np.ones((4, 2, 3))
print(b, "\n")  # Matrix of ones (4x2x3)

c = np.full((2, 2, 2), 99)
print(c, "\n")  # Matrix filled with 99

# Generating random arrays
d = np.random.rand(4, 2)
print(d, "\n")  # Random values between 0-1 (4x2)

e = np.random.randint(7, size=(3, 3))
print(e, "\n")  # Random integers 0-6 (3x3)

# Repeating elements in an array
f = np.array([[1, 2, 3]])
repeat_array = np.repeat(f, 3, axis=0)
print(repeat_array, "\n")  # Repeats row-wise

repeat_array = np.repeat(f, 3, axis=1)
print(repeat_array, "\n")  # Repeats column-wise

# Creating a bordered matrix
array = np.ones((5, 5))
print(array, "\n")

zero = np.zeros((3, 3))
print(zero, "\n")
zero[1, 1] = 9
print(zero, "\n")

array[1:4, 1:4] = zero
print(array, "\n")

# Copying an array correctly
a = np.array([1, 2, 3])
b = a.copy()
b[0] = 100
print(a, "\n")  # a remains unchanged
print(b, "\n")  # b is modified independently

# Element-wise arithmetic operations
a = a + 2
print(a, "\n")

a = a * 2
print(a, "\n")

a = a - 2
print(a, "\n")

a = a / 2
print(a, "\n")

a = a + b
print(a, "\n")

```

## 🔍 Explanation
1. **Predefined Arrays (`zeros()`, `ones()`, `full()`)**
   - Creates matrices filled with **0s, 1s, or a specific value**.

2. **Random Arrays (`rand()`, `randint()`)**
   - Generates **random values or integers** within a range.

3. **Repeating and Slicing Arrays (`repeat()`, slicing)**
   - Repeats rows or columns dynamically.
   - Uses slicing (`Array[1:4, 1:4]`) to modify sections of an array.

4. **Copying Arrays (`copy()`)**
   - Prevents unintentional modifications by creating **independent copies**.

5. **Mathematical Operations**
   - Supports **element-wise addition, subtraction, multiplication, and division**.

## 🚀 Why Use NumPy Arrays?
✅ **Optimized for numerical operations** – Faster than Python lists.  
✅ **Memory-efficient storage** – Avoids unnecessary object overhead.  
✅ **Easy manipulation** – Supports reshaping, slicing, and broadcasting.  
✅ **Widely used in data science & machine learning** – Foundation for Pandas, TensorFlow, etc.  

## 🔥 Future Enhancements
- ✅ Implement **advanced broadcasting techniques** for efficient calculations.
- ✅ Compare **NumPy performance vs Python lists** using `timeit`.
- ✅ Utilize **matrix operations (`dot()`, `T`)** for financial modeling.

## 🎯 Summary
This **Python NumPy project** demonstrates key operations for creating and modifying arrays, performing mathematical operations, and handling memory efficiently. Mastering these techniques is essential for **data science, numerical computing, and financial analytics**.

Happy Coding! 🚀🐍
