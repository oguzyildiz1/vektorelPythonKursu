import numpy as np

arr = np.array([1, 2, 3, 4])

# print(arr[0])
# print(arr[1])
# print(arr[2] + arr[3])


abc = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('1. Satırın 2. elemanı: ', abc[0 ,1])
print('2. Satırın 5. elemanı: ', abc[1, 4])

arr1 = np.arange(1,11)

tersi = arr1[::-1]

print(tersi)