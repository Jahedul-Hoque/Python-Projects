import numpy as np

# Creating a matrix of ones (2x3)
a = np.ones((2,3))
print(a, "\n")

# Creating a matrix filled with 5s (3x2)
b = np.full((3,2), 5)
print(b, "\n")

# Performing matrix multiplication
print(np.matmul(a, b), "\n")
# Explanation:
# - Matrix "a" (2x3) is multiplied by matrix "b" (3x2)
# - The result is a (2x2) matrix where each element is the sum of row-column multiplications.

# Creating an identity matrix (3x3) and calculating its determinant
c = np.identity(3)
print(np.linalg.det(c), "\n")
# The determinant of an identity matrix is always 1.