import numpy as np

# arr1 = np.array([1, 2, 3,])
arr2 = np.array([[[1, 2],[3, 4]], [[5, 6], [7, 8]]])

# print("Tek boyut")

for x in np.nditer(arr2): print(x)
