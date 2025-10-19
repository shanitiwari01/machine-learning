## 🧠 NumPy Indexing & Slicing (Advanced)

NumPy gives you three main ways to access array data:

1. **Basic Indexing / Slicing**
2. **Boolean Indexing**
3. **Fancy Indexing**

Let’s go through them step-by-step 👇

---

## 🧩 1. Basic Indexing & Slicing

Similar to Python lists, but works in **multiple dimensions**.

### Example 1: 1D Array

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr[1:4])     # [20 30 40]
print(arr[-2:])     # [40 50]
```

---

### Example 2: 2D Array

```python
arr2d = np.array([[10, 20, 30],
                  [40, 50, 60],
                  [70, 80, 90]])

print(arr2d[0, 2])     # 30 (row 0, col 2)
print(arr2d[:, 1])     # [20 50 80] (all rows, col 1)
print(arr2d[1:, :2])   # [[40 50], [70 80]]
```

**Remember:**
`:` → “all elements” in that axis.

---

## 🧠 2. Boolean Indexing

Use **conditions** to filter data — just like queries in SQL.

```python
arr = np.array([5, 10, 15, 20, 25])
print(arr[arr > 10])
```

**Output:**

```
[15 20 25]
```

You can even combine conditions:

```python
print(arr[(arr > 10) & (arr < 25)])
# [15 20]
```

✅ Super useful for **filtering datasets** in Pandas too.

---

## 🧮 3. Fancy Indexing

Fancy indexing lets you access **specific elements or rows/columns** using lists or arrays of indices.

### Example 1: Selecting Multiple Rows

```python
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print(arr[[0, 2]])   # Select 1st and 3rd rows
```

### Example 2: Selecting Specific Elements

```python
print(arr[[0, 1, 2], [2, 0, 1]])
```

**Explanation:**

* From (0,2): 30
* From (1,0): 40
* From (2,1): 80

**Output:** `[30 40 80]`

---

## 🔍 4. Modifying Array Elements

You can assign values directly:

```python
arr = np.array([10, 20, 30, 40])
arr[2:4] = [300, 400]
print(arr)
```

**Output:**

```
[10 20 300 400]
```

---

## ⚡ 5. Copy vs View

This is **critical** in NumPy.

* **View** → changes affect the original array
* **Copy** → changes do *not* affect the original array

```python
arr = np.array([1, 2, 3, 4])
view = arr[1:3]
copy = arr[1:3].copy()

view[0] = 99
print(arr)   # [1 99 3 4]  -> changed

copy[0] = 55
print(arr)   # [1 99 3 4]  -> unchanged
```

---

## 🧭 Analogy

Think of:

* **View** → Like sharing a Google Sheet (changes reflect everywhere)
* **Copy** → Like downloading a file locally (original stays safe)

---

## 💪 Mini Exercise

Try this code:

```python
import numpy as np

data = np.array([[10, 15, 20],
                 [25, 30, 35],
                 [40, 45, 50]])

# 1. Extract the second column
# 2. Extract all elements > 25
# 3. Select rows 0 and 2
# 4. Change the middle element (30) to 300
```

---

### 💭 Socratic Questions

1. Why might you prefer to use *views* instead of *copies* in large datasets?
2. What happens if you slice using negative indices like `arr[-2:]`?
