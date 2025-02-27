import numpy as np

a = np.array ([1,2,3])
b = np.array ([[9.0,8.0, 7.0], [6.0,5.0,4.0]])
print("a:", a, "\n","b:", b)
#makes 1d and 2d array and prints them both

adim = a.ndim
print("a has a dimension of", adim)
#a has a dimension of 1

bdim = b.ndim
print("b has a dimension of", bdim)
#b has a dimension of 2


ashape = a.shape
print("a has a shape of", ashape)
#ashape has a shape of 3 collumns + 1 invisible row

bshape = b.shape
print("a has a shape of", bshape)
#bshape has a shape of 3 collumns and 2 rows

print("a has a data type of ", a.dtype)
#64 bits or 8 bytes of an integer64 by default

print("b has a data type of ", b.dtype)
#64 bits or 8 bytes of a float64 by default
