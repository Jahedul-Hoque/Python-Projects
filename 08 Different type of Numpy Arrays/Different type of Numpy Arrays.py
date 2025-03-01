import numpy as np

a= np.zeros((2,3))
print(a, "\n")
#matrix of 0 with 2x3

b = np.ones((4,2,3))
print(b, "\n")
#matrix of 99 with 4x2x3

c= np.full((2,2,2), 99)
print(c, "\n")
#matrix of 99

d = np.random.rand(4,2)
print(d, "\n")
#matrix of random numbers from 0-1 of 4x2

e = np.random.randint(7, size =(3,3))
print(e, "\n")
#printing a matrix with integers 0-7 of 3x3

f = np.array([[1,2,3]])
RepeatArray = np.repeat(f,3, axis=0)
print(RepeatArray, "\n")
#repeatArray is equal to "f" array x3 times
#axis is 0 so array should be in 3 lines

RepeatArray = np.repeat(f,3, axis=1)
print(RepeatArray, "\n")
#axis is 1 so all values should be in the same line

Array = np.ones((5, 5))
print(Array, "\n")
zero = np.zeros((3,3))
print (zero, "\n")
zero[1,1] = 9
print (zero, "\n")

Array[1:4, 1:4] = zero
print(Array, "\n")


a = np.array([1,2,3])
b = a.copy()
b[0] = 100
print(a, "\n")
print(b, "\n")
#copies the values of a to b 
#b DOESNT become a pointer to the same location as a

a = a+2
print(a, "\n")

a = a*2
print(a, "\n")

a = a-2
print(a, "\n")

a = a/2
print(a, "\n")

a = a+b
print(a, "\n")