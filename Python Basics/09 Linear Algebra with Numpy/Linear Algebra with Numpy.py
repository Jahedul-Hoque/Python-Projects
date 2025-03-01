import numpy as np

a = np.ones((2,3))
print(a, "\n")
b = np.full((3,2), 5)
print(b, "\n")


print(np.matmul(a,b), "\n")
#multiplying matrices
#tally of (rows of Matrix "a" multiply collumns of matrix "b")
#(1*5 + 1*5 + 1*5) 
# inside each row and collumn of the resulting 2x2 matrix

c = np.identity(3)
print(np.linalg.det(c), "\n")
