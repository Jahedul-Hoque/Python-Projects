import numpy as np

newArray = np.array ([[[1,2],[3,4]],[[5,6],[7,8]]])

print(newArray)
print(newArray[1,0,1])
#[1,0,1] = [z,r,c]
# prints the second z index of the 1st row of the 2nd column

print(newArray[:,1,1])