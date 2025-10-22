import numpy as np

dArr = np.eye(2,4,2, float)

print(dArr)
print(dArr.dtype)

intArr = dArr.astype(int)

print(intArr)
print(intArr.dtype)