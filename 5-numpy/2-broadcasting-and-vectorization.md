## 🧠 NumPy Broadcasting & Vectorization

### 🧩 1. What is Broadcasting?

**Broadcasting** is NumPy’s way of **applying arithmetic operations on arrays of different shapes**.

Normally, you can only add or multiply arrays of the same size.
But broadcasting lets NumPy “stretch” smaller arrays automatically to match the shape of larger ones — **without actually copying data**.

---

### 🧮 Example 1: Simple Broadcasting

```python
import numpy as np

arr = np.array([1, 2, 3])
print(arr + 10)
```

**Output:**

```
[11 12 13]
```

👉 NumPy added `10` to each element — it **broadcasted** the scalar (10) across the array.

---

### 🧮 Example 2: Row Broadcasting

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

add = np.array([10, 20, 30])

print(matrix + add)
```

**Output:**

```
[[11 22 33]
 [14 25 36]
 [17 28 39]]
```

✅ NumPy stretched `[10,20,30]` **vertically** to match the 3x3 matrix.

---

### 🧩 2. Broadcasting Rules

NumPy compares shapes **from right to left**:

| Case         | Array A | Array B | Result                              |
| ------------ | ------- | ------- | ----------------------------------- |
| Same shape   | (3, 3)  | (3, 3)  | Works                               |
| Compatible   | (3, 3)  | (1, 3)  | Works → B is stretched vertically   |
| Compatible   | (3, 1)  | (3, 3)  | Works → A is stretched horizontally |
| Incompatible | (3, 3)  | (2, 3)  | ❌ Error                             |

👉 **Rule**: Dimensions are compatible if they are **equal** or **one of them is 1**.

---

### ⚙️ Example 3: Column Broadcasting

```python
arr1 = np.array([[1], [2], [3]])   # Shape (3,1)
arr2 = np.array([10, 20, 30])      # Shape (3,)

print(arr1 + arr2)
```

**Output:**

```
[[11 21 31]
 [12 22 32]
 [13 23 33]]
```

👉 NumPy expands both arrays to shape `(3,3)` internally.

---

## ⚡ 3. Vectorization

**Vectorization** means performing operations **without explicit loops** —
by applying them directly on arrays.

This uses **low-level C operations** instead of Python loops, making it much faster.

---

### 🧮 Example: Without vs With Vectorization

```python
import numpy as np

# Without vectorization
nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums]

# With NumPy vectorization
arr = np.array(nums)
squares_np = arr ** 2
```

✅ Vectorized code is shorter, cleaner, and **~50x faster**.

---

## 🧠 Analogy

Think of broadcasting like **pouring tea** —
You can pour one teapot (scalar) into multiple cups (array elements) at once,
instead of filling each cup manually with a spoon (loop).

---

## 💡 Mini Exercise

Try this in Python:

```python
import numpy as np

matrix = np.array([[5, 10, 15], [20, 25, 30]])
vector = np.array([1, 2, 3])

print(matrix / vector)
```

1. Predict what will happen before running.
2. What is the shape of the result?

---

### 🧩 Socratic Questions

1. Why do you think NumPy’s broadcasting is faster than using Python loops?
2. What do you think happens if two arrays have incompatible shapes?
