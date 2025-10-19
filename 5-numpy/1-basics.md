## 🧠 What is NumPy?

**NumPy** stands for **Numerical Python**.
It provides **fast**, **memory-efficient** tools for handling **large numerical data** — especially through its **n-dimensional array** object called `ndarray`.

It’s the backbone of libraries like **Pandas, Scikit-learn, TensorFlow, and Matplotlib**.

---

## ⚙️ Installation

```bash
pip install numpy
```

---

## 🧩 Importing NumPy

```python
import numpy as np
```

---

## 📦 1. NumPy Arrays

### Create a 1D array

```python
arr = np.array([1, 2, 3, 4, 5])
print(arr)
```

**Output:**

```
[1 2 3 4 5]
```

### Create a 2D array

```python
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
```

**Output:**

```
[[1 2 3]
 [4 5 6]]
```

### Array type and shape

```python
print(arr2.ndim)   # Number of dimensions
print(arr2.shape)  # (rows, columns)
print(arr2.dtype)  # Data type (e.g., int64, float64)
```

---

## 🔢 2. Creating Arrays Quickly

| Function              | Description            | Example                         |
| --------------------- | ---------------------- | ------------------------------- |
| `np.zeros()`          | Creates array of zeros | `np.zeros((2,3))`               |
| `np.ones()`           | Creates array of ones  | `np.ones((3,2))`                |
| `np.arange()`         | Range of values        | `np.arange(0,10,2)`             |
| `np.linspace()`       | Evenly spaced numbers  | `np.linspace(0,1,5)`            |
| `np.eye()`            | Identity matrix        | `np.eye(3)`                     |
| `np.random.rand()`    | Random floats (0–1)    | `np.random.rand(2,3)`           |
| `np.random.randint()` | Random integers        | `np.random.randint(1,10,(2,3))` |

---

## 🧮 3. Array Operations

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)   # [5 7 9]
print(a * b)   # [ 4 10 18]
print(a ** 2)  # [1 4 9]
print(np.mean(a))  # 2.0
```

👉 These operations happen **element-wise**, which makes NumPy **blazingly fast**.

---

## 🧠 4. Indexing & Slicing

```python
arr = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr[0, 1])     # 20
print(arr[:, 1])     # [20 50 80] -> all rows, 2nd column
print(arr[1:, :2])   # [[40 50],[70 80]]
```

---

## 📏 5. Reshaping and Flattening

```python
arr = np.arange(1, 7)
reshaped = arr.reshape(2, 3)
print(reshaped)
print(reshaped.flatten())
```

**Output:**

```
[[1 2 3]
 [4 5 6]]
[1 2 3 4 5 6]
```

---

## 🧰 6. Useful Functions

| Function                | Purpose             | Example        |
| ----------------------- | ------------------- | -------------- |
| `np.sum()`              | Sum of all elements | `np.sum(arr)`  |
| `np.mean()`             | Average             | `np.mean(arr)` |
| `np.std()`              | Standard deviation  | `np.std(arr)`  |
| `np.max()` / `np.min()` | Max / Min           | `np.max(arr)`  |
| `np.dot()`              | Dot product         | `np.dot(a, b)` |
| `np.sort()`             | Sort array          | `np.sort(arr)` |

---

## 📈 7. Example: Matrix Operations

```python
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print(A + B)        # Add matrices
print(A @ B)        # Matrix multiplication
print(np.linalg.inv(A))  # Inverse
```

---

## ⚡ 8. Why NumPy is Fast

NumPy uses **C under the hood**, performing operations on **contiguous memory blocks**, avoiding Python loops.
This can make NumPy **up to 50x faster** than plain Python lists!

---

## 🧩 Mini Exercise

```python
import numpy as np

arr = np.array([[2, 4, 6], [1, 3, 5], [7, 9, 11]])

# Try these:
print(np.mean(arr))
print(arr[1:, 1:])
print(arr.reshape(1, 9))
```
