import numpy as np

# Creating a 3D NumPy array
new_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(new_array)

# Accessing a specific element using 3D indexing
print(new_array[1, 0, 1])
# Index breakdown: [z, r, c] → [1, 0, 1]
# Retrieves the second (z=1) matrix, first row (r=0), second column (c=1)
# Output: 6

# Slicing across the first axis (z-axis)
print(new_array[:, 1, 1])
# Selects all elements along the z-axis (:),
# 2nd row (index 1), and 2nd column (index 1)
# Output: [4, 8]
