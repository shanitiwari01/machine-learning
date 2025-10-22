import numpy as np

oneD = np.array([1,2,3])
print(oneD)
print(oneD.shape)
print(oneD.dtype)
print(oneD.ndim)


twoD = np.array([[3,2,5],[2,35,6]])
print(twoD)
print(twoD.shape)
print(twoD.dtype)
print(twoD.ndim)

threeD = np.array([
    [[1,2,4],[2,35,6],[23,13,55]],
    [[1,2,5],[2,23,5],[23,13,55]],
    [[1,2,5],[2,23,5],[23,13,55]],
    [[1,2,5],[2,23,5],[23,13,55]],
])
print(threeD)
print(threeD.shape)
print(threeD.dtype)
print(threeD.ndim)