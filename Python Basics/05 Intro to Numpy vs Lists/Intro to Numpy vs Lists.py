import numpy as np

# Python List Trade Values
list_trade_values = [123, 456, 789]
print(list_trade_values)

# Characteristics of Python Lists:
# - Uses pointers due to scattered memory allocation.
# - Requires reference count and object type checking.
# - Supports different data types in a single list.

# NumPy Array Trade Values
numpy_trade_values = np.array([564.31, 400.34, 349.53])
print(numpy_trade_values)

# Characteristics of NumPy Arrays:
# - Uses contiguous memory allocation for efficiency.
# - Does not require object type checking (fixed dtype).
# - Optimized for vectorized operations and SIMD (Single Instruction Multiple Data).
# - Reduces memory overhead and improves cache performance.
