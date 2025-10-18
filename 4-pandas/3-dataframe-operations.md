## 🧩 DataFrame Operations

### 🧠 Concept

A **DataFrame** is a 2D labeled data structure — like an **Excel table** — with rows and columns.
Now that you know how to create and index data, it’s time to manipulate it like a pro. 💪

---

### ⚙️ Example: Sample DataFrame

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'Tokyo']
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
3    David   40     Tokyo
```

---

### ➕ Add Columns

You can add a column by **assigning** a new Series or list:

```python
df['Salary'] = [50000, 60000, 70000, 80000]
```

Now `df` will have a new column **Salary**.

---

### ➕ Add Rows

You can use `.loc[]` to add a new row:

```python
df.loc[4] = ['Eve', 28, 'Berlin', 55000]
```

---

### ❌ Remove Columns or Rows

```python
# Remove a column
df = df.drop('City', axis=1)

# Remove a row
df = df.drop(2, axis=0)
```

(`axis=1` → column, `axis=0` → row)

---

### 🔍 Filter Data

```python
# Filter rows where Age > 30
filtered = df[df['Age'] > 30]
print(filtered)
```

**Output:**

```
    Name  Age  Salary
2  Charlie   35  70000
3    David   40  80000
```

---

### ⚙️ Common Operations

| Operation               | Description           | Example                             |
| ----------------------- | --------------------- | ----------------------------------- |
| `df.columns`            | Get column names      | `['Name', 'Age', 'City', 'Salary']` |
| `df.shape`              | Get size (rows, cols) | `(4, 4)`                            |
| `df.sort_values('Age')` | Sort by column        | Ascending order                     |
| `df['Age'].mean()`      | Column average        | `32.5`                              |

---

### 🌍 Analogy

Think of a DataFrame as a **Google Sheet**:

* Adding columns = inserting new fields.
* Filtering = applying a filter button.
* Dropping rows = deleting entries.

---

### ❓ Socratic Questions

1. If you want to remove multiple columns (`Age`, `City`), how can you modify `df.drop()` to do that?
2. Why do you think `axis=0` means “row” and `axis=1` means “column”?

---

### 💪 Mini Exercise

Create a DataFrame named `students` with:

| Name | Marks | Subject |
| ---- | ----- | ------- |
| Raj  | 85    | Math    |
| Emma | 92    | Science |
| John | 78    | English |

Now:

1. Add a column `Grade` with values `['B', 'A', 'C']`.
2. Filter students with Marks > 80.
3. Remove the `Subject` column.
