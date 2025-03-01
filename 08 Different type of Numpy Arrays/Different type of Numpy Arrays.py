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
RepeatArray = np.repeat(f,3, axis=1)
print(RepeatArray, "\n")