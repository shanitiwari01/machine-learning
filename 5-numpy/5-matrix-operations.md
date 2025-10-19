## 🧠  NumPy Linear Algebra (Matrix Operations)

Linear algebra is all about **vectors**, **matrices**, and **transformations** — and NumPy makes it incredibly easy.

All linear algebra functions live in the **`np.linalg`** module.

---

## 🧩 1. Matrix Creation

```python
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print(A)
print(B)
```

---

## ⚙️ 2. Matrix Addition, Subtraction, and Multiplication

```python
print(A + B)   # Element-wise addition
print(A - B)   # Element-wise subtraction
print(A * B)   # Element-wise multiplication
```

But for **true matrix multiplication** (like in math):

```python
print(A @ B)        # Using @ operator
print(np.dot(A, B)) # Same as above
```

✅ Output:

```
[[19 22]
 [43 50]]
```

---

## 🧮 3. Matrix Transpose

Swaps rows ↔ columns.

```python
print(A.T)
```

**Output:**

```
[[1 3]
 [2 4]]
```

---

## 📐 4. Determinant

The **determinant** tells you if a matrix is **invertible** or not.

```python
print(np.linalg.det(A))  # Output: -2.0
```

👉 If determinant = 0 → matrix is **singular (non-invertible)**

---

## 🔁 5. Inverse of a Matrix

The **inverse** of a matrix `A` is the matrix `A⁻¹` such that:

> `A * A⁻¹ = I` (Identity matrix)

```python
inv_A = np.linalg.inv(A)
print(inv_A)
```

**Output:**

```
[[-2.   1. ]
 [ 1.5 -0.5]]
```

---

## 🧩 6. Identity Matrix

```python
I = np.eye(3)
print(I)
```

**Output:**

```
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

---

## ⚡ 7. Solving Linear Equations

Suppose:

```
2x + y = 5  
x + 3y = 8
```

You can represent it as:

```
A = [[2, 1],
     [1, 3]]
b = [5, 8]
```

Now solve for `[x, y]`:

```python
A = np.array([[2, 1], [1, 3]])
b = np.array([5, 8])
solution = np.linalg.solve(A, b)
print(solution)
```

**Output:**

```
[1.4 2.2]
```

✅ So `x = 1.4`, `y = 2.2`

---

## 📊 8. Eigenvalues & Eigenvectors (Bonus)

These are critical in **PCA (Principal Component Analysis)** and ML.

```python
values, vectors = np.linalg.eig(A)
print("Eigenvalues:", values)
print("Eigenvectors:\n", vectors)
```

---

## 🧠 Analogy

Think of:

* **Matrix multiplication** → Applying filters or transformations
* **Transpose** → Flipping your data view
* **Inverse** → Undoing a transformation
* **Determinant** → Checking if a transformation “squashes” space (0 → flat)

---

## 💪 Mini Exercise

Try this in Python:

```python
import numpy as np

M = np.array([[4, 2],
              [3, 1]])

# 1. Find determinant
# 2. Find inverse
# 3. Verify A @ A_inv ≈ Identity
```

---

### 💭 Socratic Questions

1. What does it mean if a matrix’s determinant is **zero**?
2. Why might machine learning algorithms need matrix inverses or dot products?
