## 🧩 Introduction to Pandas

### 🧠 Concept

**Pandas** (short for *Python Data Analysis Library*) provides **high-performance**, **easy-to-use** tools for working with **structured data** — like Excel sheets or SQL tables.

The two core data structures in Pandas are:

1. **Series** → A one-dimensional labeled array (like a single column).
2. **DataFrame** → A two-dimensional labeled data structure (like an Excel table or SQL table).

---

### 💡 Analogy

Imagine a **DataFrame** as an **Excel spreadsheet** in Python:

* **Rows** → Records
* **Columns** → Features
* **Index** → Row numbers (labels)

And a **Series** as a **single column** from that spreadsheet.

---

### ⚙️ Basic Example

```python
import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data)
print(df)
```

**Output:**

```
      Name  Age      City
0    Alice   25  New York
1      Bob   30    London
2  Charlie   35     Paris
```

---

### 🧭 Common Operations

| Operation       | Description                  | Example                  |
| --------------- | ---------------------------- | ------------------------ |
| `df.head()`     | View first 5 rows            | `df.head()`              |
| `df.tail()`     | View last 5 rows             | `df.tail()`              |
| `df.shape`      | Get number of rows & columns | `(rows, columns)`        |
| `df.info()`     | Get summary info about data  | Data types, nulls, etc   |
| `df.describe()` | Summary statistics           | Mean, std, min, max, etc |

---

### ❓ Socratic Questions

1. If you wanted to access a single column (say “Age”), what do you think the syntax would look like?
2. Why is Pandas more powerful than using lists or dictionaries for handling large data?

---

### 🏋️‍♀️ Mini Exercise

Create a Pandas DataFrame named `students` with columns:

* `Name`: [‘John’, ‘Emma’, ‘Raj’]
* `Marks`: [88, 92, 79]
  Then display the first two rows using `head()`.
