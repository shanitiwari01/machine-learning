## 🧠 Python DSA — Lists & Arrays

---

### 🔹 1. What are Lists and Arrays?

Both **Lists** and **Arrays** are used to **store multiple items** in a single variable.

| Feature     | List                        | Array                                       |
| ----------- | --------------------------- | ------------------------------------------- |
| Data type   | Can hold *mixed* data types | Holds *same* data type                      |
| Flexibility | Very flexible, built-in     | More memory-efficient                       |
| Module      | Built-in (no import)        | Needs `array` or `numpy` module             |
| Use case    | General purpose             | Performance-critical or numerical computing |

---

### 🪶 Example — Python List

```python
numbers = [10, 20, 30, 40, 50]
print(numbers)
```

✅ Output:

```
[10, 20, 30, 40, 50]
```

A list can contain **integers, strings, or even other lists**:

```python
data = [10, "Python", 3.14, [1, 2, 3]]
```

---

### ⚙️ 2. List Operations (Core DSA Actions)

| Operation   | Description                   | Example               |
| ----------- | ----------------------------- | --------------------- |
| `append()`  | Add one element at end        | `nums.append(6)`      |
| `extend()`  | Add multiple elements         | `nums.extend([7,8])`  |
| `insert()`  | Add element at specific index | `nums.insert(1, 100)` |
| `remove()`  | Remove first match            | `nums.remove(10)`     |
| `pop()`     | Remove by index               | `nums.pop(2)`         |
| `sort()`    | Sort in ascending order       | `nums.sort()`         |
| `reverse()` | Reverse order                 | `nums.reverse()`      |
| `len()`     | Get length                    | `len(nums)`           |

---

### 💡 Example — Working with Lists

```python
nums = [1, 3, 5]
nums.append(7)
nums.extend([9, 11])
nums.insert(2, 4)
nums.pop(1)
print(nums)
```

✅ Output:

```
[1, 4, 5, 7, 9, 11]
```

---

### 🧩 3. List Comprehension (Pythonic Way)

Quick and powerful way to create lists:

```python
squares = [x**2 for x in range(1, 6)]
print(squares)
```

✅ Output:

```
[1, 4, 9, 16, 25]
```

---

### 🧱 4. 2D Lists (Matrix Representation)

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # 6
```

---

### 💾 5. Arrays (from the `array` module)

Lists are flexible, but **arrays** are more efficient for numeric data.
You need to import the `array` module:

```python
from array import array

arr = array('i', [1, 2, 3, 4, 5])
print(arr)
```

* `'i'` = type code for integer
* Other examples: `'f'` (float), `'d'` (double)

---

### ⚙️ 6. Common Array Operations

```python
arr.append(6)
arr.insert(2, 10)
arr.remove(3)
arr.pop()
print(arr.tolist())  # convert array to list
```

---

### ⚡ 7. Lists vs Arrays in DSA Context

| Feature           | Lists           | Arrays              |
| ----------------- | --------------- | ------------------- |
| Dynamic resizing  | ✅ Yes           | ⚠️ Limited          |
| Mixed data types  | ✅ Yes           | ❌ No                |
| Speed for numbers | ⚠️ Slower       | ✅ Faster            |
| Best for          | General storage | Numeric computation |

---

### 🧠 Socratic Questions

1. Why do you think Python allows both lists and arrays?
2. Which one would you prefer when handling millions of numeric values? Why?
3. How would you represent a 3x3 matrix in Python?

---

### 🧩 Mini Exercise

Create a program that:

1. Stores 5 numbers in a list.
2. Adds 2 more numbers.
3. Removes the smallest number.
4. Prints the **sum**, **average**, and **sorted list**.
