## 🧠 NumPy Mathematical & Statistical Functions

Let’s explore the most important ones step by step 👇

---

## 🧩 1. Basic Mathematical Functions

These work **element-wise** (on every element in the array).

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(np.add(arr, 5))     # Add 5 to each element → [6 7 8 9 10]
print(np.subtract(arr, 2))# Subtract 2 → [-1 0 1 2 3]
print(np.multiply(arr, 3))# Multiply by 3 → [3 6 9 12 15]
print(np.divide(arr, 2))  # Divide by 2 → [0.5 1.  1.5 2.  2.5]
print(np.power(arr, 2))   # Square each element → [1 4 9 16 25]
```

All these are **vectorized**, so they are lightning fast 🚀.

---

## 📏 2. Aggregation Functions

Used to **summarize** data.

```python
arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print(np.sum(arr))        # 210
print(np.mean(arr))       # 35.0
print(np.max(arr))        # 60
print(np.min(arr))        # 10
print(np.std(arr))        # 17.078 (standard deviation)
print(np.var(arr))        # 292.0  (variance)
```

👉 You can also apply them **along an axis**:

```python
print(np.sum(arr, axis=0))  # column-wise sum → [50 70 90]
print(np.sum(arr, axis=1))  # row-wise sum → [60 150]
```

---

## 🧮 3. Statistical Functions

These are crucial in data science and ML:

| Function          | Meaning                      | Example                  |
| ----------------- | ---------------------------- | ------------------------ |
| `np.mean()`       | Average value                | `np.mean(arr)`           |
| `np.median()`     | Middle value                 | `np.median(arr)`         |
| `np.std()`        | Standard deviation           | `np.std(arr)`            |
| `np.var()`        | Variance                     | `np.var(arr)`            |
| `np.percentile()` | nth percentile               | `np.percentile(arr, 75)` |
| `np.corrcoef()`   | Correlation between datasets | `np.corrcoef(a, b)`      |

---

### Example: Correlation Coefficient

```python
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

print(np.corrcoef(x, y))
```

**Output:**

```
[[1. 1.]
 [1. 1.]]
```

✅ 1 means **perfect positive correlation** (as `x` increases, `y` increases proportionally).

---

## ⚙️ 4. Rounding & Other Utilities

| Function     | Description    | Example                       |
| ------------ | -------------- | ----------------------------- |
| `np.round()` | Round values   | `np.round(3.567, 2)` → `3.57` |
| `np.floor()` | Round down     | `np.floor(3.7)` → `3`         |
| `np.ceil()`  | Round up       | `np.ceil(3.2)` → `4`          |
| `np.abs()`   | Absolute value | `np.abs(-5)` → `5`            |

---

## 🧠 5. Axis Concept (Very Important)

Axis defines **the direction** along which operations happen:

```
Array:
[[1, 2, 3],
 [4, 5, 6]]

axis=0 → down columns
axis=1 → across rows
```

```python
np.sum(arr, axis=0)  # [5 7 9]
np.sum(arr, axis=1)  # [6 15]
```

---

## 🧩 Analogy

Think of `axis` like **the direction of a spreadsheet formula**:

* `axis=0` = column-wise (down)
* `axis=1` = row-wise (across)

---

## 💪 Mini Exercise

Try this in Python:

```python
import numpy as np

data = np.array([[2, 4, 6],
                 [1, 3, 5],
                 [7, 9, 11]])

# 1. Find mean of all elements
# 2. Find variance row-wise
# 3. Find correlation coefficient between first and last columns
```

---

### 💭 Socratic Questions

1. Why do you think standard deviation is important when analyzing datasets?
2. What could a correlation value of `-1` or `0` tell you about two variables?
