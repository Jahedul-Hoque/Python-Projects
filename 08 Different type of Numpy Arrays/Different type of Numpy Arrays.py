import numpy as np

# Creating arrays with predefined values
a = np.zeros((2,3))
print(a, "\n")  # Matrix of zeros (2x3)

b = np.ones((4,2,3))
print(b, "\n")  # Matrix of ones (4x2x3)

c = np.full((2,2,2), 99)
print(c, "\n")  # Matrix filled with 99

# Generating random arrays
d = np.random.rand(4,2)
print(d, "\n")  # Random values between 0-1 (4x2)

e = np.random.randint(7, size=(3,3))
print(e, "\n")  # Random integers 0-6 (3x3)

# Repeating elements in an array
f = np.array([[1,2,3]])
RepeatArray = np.repeat(f, 3, axis=0)
print(RepeatArray, "\n")  # Repeats row-wise

RepeatArray = np.repeat(f, 3, axis=1)
print(RepeatArray, "\n")  # Repeats column-wise

# Creating a bordered matrix
Array = np.ones((5,5))
print(Array, "\n")

zero = np.zeros((3,3))
print(zero, "\n")
zero[1,1] = 9
print(zero, "\n")

Array[1:4, 1:4] = zero
print(Array, "\n")

# Copying an array correctly
a = np.array([1,2,3])
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