import numpy as np

print(np.__version__)

arr = [1,2,3,4,5]
print(arr)

arr1 = np.array([1,2,3,4,5])
print(arr1)

arr2 = np.array((1,2,3))
print(arr2)

print(type(arr1))

print(arr2.dtype)

arr3 = np.array([1.2, 3, 4])
print(arr3.dtype)