## 🧩  Data Analysis & Aggregation (groupby, sort, describe)

### 🧠 Concept

Data analysis is about **finding patterns and insights** — like averages, totals, or trends — across different groups or conditions.
Pandas gives us several powerful functions like:

* `groupby()`
* `describe()`
* `sort_values()`
* `agg()`
  to make this easy and intuitive.

---

### ⚙️ Example DataFrame

```python
import pandas as pd

data = {
    'Department': ['Sales', 'Sales', 'HR', 'HR', 'IT', 'IT'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Salary': [50000, 55000, 48000, 52000, 60000, 62000],
    'Experience': [2, 3, 4, 5, 3, 4]
}

df = pd.DataFrame(data)
print(df)
```

**Output:**

```
  Department Employee  Salary  Experience
0      Sales    Alice   50000           2
1      Sales      Bob   55000           3
2         HR  Charlie   48000           4
3         HR    David   52000           5
4         IT      Eve   60000           3
5         IT     Frank  62000           4
```

---

### 📊 `describe()` — Quick Statistics Summary

```python
df.describe()
```

Gives you:

* Count, Mean, Std, Min, Max, and Quartiles for numeric columns.

---

### 🧮 `groupby()` — Group and Aggregate Data

You can group data based on a column (like `Department`) and apply functions like `mean()`, `sum()`, or `count()`.

```python
dept_summary = df.groupby('Department')['Salary'].mean()
print(dept_summary)
```

**Output:**

```
Department
HR       50000.0
IT       61000.0
Sales    52500.0
Name: Salary, dtype: float64
```

💡 You can also aggregate multiple columns:

```python
df.groupby('Department').agg({'Salary':'mean', 'Experience':'max'})
```

---

### 🧭 Sorting Data

Sort by a column value:

```python
df.sort_values(by='Salary', ascending=False)
```

**Output:**

```
  Department Employee  Salary  Experience
5         IT     Frank   62000           4
4         IT       Eve   60000           3
1      Sales       Bob   55000           3
3         HR     David   52000           5
0      Sales     Alice   50000           2
2         HR   Charlie   48000           4
```

---

### 🧰 Common Aggregation Functions

| Function   | Meaning            |
| ---------- | ------------------ |
| `mean()`   | Average            |
| `sum()`    | Total              |
| `count()`  | Number of entries  |
| `max()`    | Maximum value      |
| `min()`    | Minimum value      |
| `median()` | Middle value       |
| `std()`    | Standard deviation |

---

### 🌍 Analogy

Think of `groupby()` like **pivot tables in Excel** —
you’re summarizing large data into meaningful small insights.

---

### ❓ Socratic Questions

1. What’s the difference between `.mean()` and `.agg({'col': 'mean'})`?
2. Why might grouping by multiple columns (like `Department` and `Experience`) be useful?
3. If your dataset had missing salary values, how would that affect `.mean()`?

---

### 💪 Mini Exercise

Create a DataFrame named `sales` with:

| Region | Salesperson | Sales |
| ------ | ----------- | ----- |
| East   | John        | 200   |
| West   | Emma        | 250   |
| East   | Raj         | 300   |
| West   | Alice       | 150   |

Now:

1. Find total sales per region using `groupby()`.
2. Sort the results by total sales (descending).
3. Print only the top-performing region.
