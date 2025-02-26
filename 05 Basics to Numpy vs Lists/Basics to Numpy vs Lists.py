import numpy as np

List_TradeValues = [123, 456, 789]
print(List_TradeValues)

# Requires you to use Int32 (4 bytes)
# Requires you to define Size and Reference Count
# REALLY big elements per list
# Data scattered across memory so it uses pointers

Numpy_TradeValues = np.array([564.31,400.34,349.53])
print (Numpy_TradeValues)

# Define smaller type such as the number 5 can be written as Int8:00000101
# Faster to read less bytes of memory
# Dont have to check the type of object
# Contingous Memory so better for cached memory
# Since data is continguous, Single Instruction Multiple Data (SIMD) performs multiple computations on 1 set of values

