import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 11, 2, 10, 9])

filter1 = np.array([41, 42, 43, 44])
x = [True, False, True, False]

newarr = filter1[x]
print(newarr)



