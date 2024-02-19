import numpy as np

# arr1 = np.array([1, 2, 3,])
arr2 = np.array([[[1, 2],[3, 4]]])
arr3 = np.array([[[5,6],[7,8]]])

# print("Tek boyut")

arr5 = np.concatenate((arr2, arr3))
print(arr5)

for x in np.nditer(arr5):
    print(x)
