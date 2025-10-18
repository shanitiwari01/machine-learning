## 🧩 Data Cleaning & Handling Missing Data

### 🧠 Concept

Real-world datasets are **messy** — missing values, typos, inconsistent formats, or irrelevant columns.
Before any analysis or machine learning, you need to **clean the data**.

Pandas provides a rich set of tools for this.

---

### ⚙️ Example DataFrame

```python
import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [25, np.nan, 35, 40, 29],
    'City': ['New York', 'London', None, 'Tokyo', 'Berlin']
}

df = pd.DataFrame(data)
print(df)
```

**Output:**

```
      Name   Age      City
0    Alice  25.0  New York
1      Bob   NaN    London
2  Charlie  35.0      None
3    David  40.0     Tokyo
4     None  29.0    Berlin
```

---

### 🧹 Detect Missing Values

```python
df.isnull()
df.isnull().sum()   # Count missing values per column
```

**Output:**

```
Name    1
Age     1
City    1
dtype: int64
```

---

### 🧩 Handle Missing Data

#### 1. Drop Missing Values

Remove rows with any missing value:

```python
df_clean = df.dropna()
```

#### 2. Fill Missing Values

Replace missing data with a default value or mean:

```python
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['City'].fillna('Unknown', inplace=True)
df['Name'].fillna('NoName', inplace=True)
```

Now your DataFrame is clean!

---

### 🧰 Other Useful Cleaning Functions

| Function                           | Description          | Example                  |
| ---------------------------------- | -------------------- | ------------------------ |
| `df.duplicated()`                  | Check duplicate rows | Returns boolean mask     |
| `df.drop_duplicates()`             | Remove duplicates    | Removes repeated entries |
| `df.rename(columns={'Old':'New'})` | Rename columns       | Change column names      |
| `df.replace('?', np.nan)`          | Replace wrong values | Replace invalid data     |
| `df['col'].astype(int)`            | Convert data type    | Change column datatype   |

---

### 🌍 Analogy

Think of this as **cleaning your kitchen before cooking** —
you can’t prepare a great dish (analysis/model) until your ingredients (data) are clean, consistent, and ready.

---

### ❓ Socratic Questions

1. When would you prefer using `.fillna()` instead of `.dropna()`?
2. Why might dropping rows with missing values sometimes lead to biased results?

---

### 💪 Mini Exercise

Create a DataFrame named `sales` with:

| Product | Price | Quantity |
| ------- | ----- | -------- |
| Pen     | 10    | 5        |
| Pencil  | NaN   | 8        |
| Eraser  | 5     | NaN      |
| Ruler   | NaN   | 10       |

Now:

1. Replace missing `Price` with the **mean** of available prices.
2. Replace missing `Quantity` with **0**.
3. Print the cleaned DataFrame.
