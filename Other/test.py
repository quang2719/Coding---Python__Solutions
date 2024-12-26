import numpy as np
a = np.array([1,2,3,4,5,6])
b = np.array([1,-1,-1,1,1,1])
print(sum(a*b))
b[2] = 1
print(sum(a*b))
print(len(a))
print(a.__len__)