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

newArray = np.array(
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
print("New Array:", newArray, "\n")
print("Number of elements in New Array:", newArray.size, "\n")
print(newArray[0, 1:4:1])
# print the 0th vectored row (1,2,3,4,5) and then start from the 1st index until the 4th index(5) and step by 1 which is 4.
# that should be 2,3,4

newArray[1, 3] = 100
print(newArray)
# should print the 4th element of the second row as 100
