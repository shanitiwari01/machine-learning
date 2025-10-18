## 🧩 Pandas Series & Indexing

### 🧠 Concept

A **Series** is a **one-dimensional labeled array** in Pandas.
Think of it like a **single column in an Excel sheet**, or a **list with labels**.

You can create a Series from a list, NumPy array, or dictionary.

---

### ⚙️ Example 1: Creating a Series

```python
import pandas as pd

# Create a Series from a list
numbers = pd.Series([10, 20, 30, 40, 50])
print(numbers)
```

**Output:**

```
0    10
1    20
2    30
3    40
4    50
dtype: int64
```

Here:

* **Left column (0–4)** → Index labels
* **Right column (10–50)** → Data values

---

### ⚙️ Example 2: Custom Index

```python
marks = pd.Series([85, 90, 88], index=['Alice', 'Bob', 'Charlie'])
print(marks)
```

**Output:**

```
Alice      85
Bob        90
Charlie    88
dtype: int64
```

Now you can access data by **label** instead of position.

---

### 🔍 Accessing Data

| Operation                     | Description        | Example  | Output |
| ----------------------------- | ------------------ | -------- | ------ |
| `marks['Bob']`                | Access by label    | `90`     |        |
| `marks[1]`                    | Access by position | `90`     |        |
| `marks[['Alice', 'Charlie']]` | Access multiple    | `85, 88` |        |
| `marks.mean()`                | Get average value  | `87.67`  |        |

---

### 🧭 Indexing in DataFrames

You can access specific rows/columns using:

| Syntax               | Description                | Example      |
| -------------------- | -------------------------- | ------------ |
| `df['column_name']`  | Select column              | `df['Age']`  |
| `df.loc[row_label]`  | Access row by label        | `df.loc[1]`  |
| `df.iloc[row_index]` | Access row by index number | `df.iloc[1]` |

---

### 🌍 Analogy

Think of `.loc[]` as looking up **names in a phonebook** (labels),
and `.iloc[]` as looking up **entries by position** (numbers on a list).

---

### ❓ Socratic Questions

1. What’s the difference between `.loc[]` and `.iloc[]` in Pandas?
2. Why do you think Pandas allows both label-based and index-based selection?

---

### 💪 Mini Exercise

Create a Series named `temperatures` with values `[30, 32, 35, 33]`
and custom index labels `['Mon', 'Tue', 'Wed', 'Thu']`.

Then:

* Access the temperature for Wednesday using both **label** and **position**.
