list = [num for num in range(1, 1000000)]

for index, num in enumerate(list):
    list[index] = num * 10

print(list)

# import numpy as np
# arr = np.array([num for num in range(1, 1000000)])

# arr = arr * 10

# print(arr)