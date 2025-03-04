import numpy as np

# Python List Trade Values
List_TradeValues = [123, 456, 789]
print(List_TradeValues)

# Characteristics of Python Lists:
# - Uses pointers due to scattered memory allocation.
# - Requires reference count and object type checking.
# - Supports different data types in a single list.

# NumPy Array Trade Values
Numpy_TradeValues = np.array([564.31, 400.34, 349.53])
print(Numpy_TradeValues)

# Characteristics of NumPy Arrays:
# - Uses contiguous memory allocation for efficiency.
# - Does not require object type checking (fixed dtype).
# - Optimized for vectorized operations and SIMD (Single Instruction Multiple Data).
# - Reduces memory overhead and improves cache performance.
