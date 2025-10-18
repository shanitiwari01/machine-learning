## 🧩 Merging, Joining & Concatenating in Pandas

### 🧠 Concept

In real-world scenarios, data is often spread across multiple tables.
Pandas provides multiple ways to combine them:

1. **concat()** → Stack datasets vertically or horizontally
2. **merge()** → Combine on common columns (like SQL joins)
3. **join()** → Combine based on index

---

### ⚙️ Example 1: `concat()` — Stacking DataFrames

```python
import pandas as pd

data1 = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
data2 = {'Name': ['Charlie', 'David'], 'Age': [35, 40]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

combined = pd.concat([df1, df2])
print(combined)
```

**Output:**

```
      Name  Age
0    Alice   25
1      Bob   30
0  Charlie   35
1    David   40
```

✅ Use `ignore_index=True` to reset index.

---

### ⚙️ Example 2: `merge()` — SQL-style Joins

```python
employees = pd.DataFrame({
    'EmpID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

salaries = pd.DataFrame({
    'EmpID': [1, 2, 4],
    'Salary': [50000, 55000, 60000]
})

merged = pd.merge(employees, salaries, on='EmpID', how='inner')
print(merged)
```

**Output (INNER JOIN):**

```
   EmpID   Name  Salary
0      1  Alice   50000
1      2    Bob   55000
```

---

### 🧭 Types of Joins in Pandas

| Join Type | Description                    | Keeps                  |
| --------- | ------------------------------ | ---------------------- |
| `inner`   | Keeps only matching records    | Common values only     |
| `left`    | Keeps all from left DataFrame  | Matches + left extras  |
| `right`   | Keeps all from right DataFrame | Matches + right extras |
| `outer`   | Keeps all records              | Fills missing with NaN |

Example:

```python
pd.merge(employees, salaries, on='EmpID', how='outer')
```

**Output (OUTER JOIN):**

```
   EmpID     Name   Salary
0      1    Alice  50000.0
1      2      Bob  55000.0
2      3  Charlie      NaN
3      4      NaN  60000.0
```

---

### ⚙️ Example 3: `join()` — Index-based Merge

```python
df1 = pd.DataFrame({'A': [10, 20, 30]}, index=['x', 'y', 'z'])
df2 = pd.DataFrame({'B': [100, 200, 300]}, index=['x', 'y', 'a'])

joined = df1.join(df2, how='outer')
print(joined)
```

**Output:**

```
      A      B
x  10.0  100.0
y  20.0  200.0
z  30.0    NaN
a   NaN  300.0
```

---

### 🌍 Analogy

Think of these operations like **combining Excel sheets**:

* `concat()` → Pasting one sheet below another
* `merge()` → VLOOKUP based on a common column
* `join()` → Combining sheets based on row labels

---

### ❓ Socratic Questions

1. How is `merge()` different from `concat()`?
2. In what scenario would you prefer an `outer` join over an `inner` join?
3. Why might a join result in missing (NaN) values?

---

### 💪 Mini Exercise

Create two DataFrames:

1. `students` →

   | ID | Name |
   | -- | ---- |
   | 1  | John |
   | 2  | Emma |
   | 3  | Raj  |

2. `scores` →

   | ID | Marks |
   | -- | ----- |
   | 2  | 85    |
   | 3  | 90    |
   | 4  | 78    |

Now:

* Perform a **left join** using `merge()` to combine them.
* Observe which rows contain NaN and why.
