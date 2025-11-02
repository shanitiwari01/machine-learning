## 🧠 1️⃣ What is Data Transformation?

**Data Transformation** means converting data from one form to another — making it *more useful* for analysis or training.
It often involves scaling, encoding, binning, or mathematical transformations.

---

### ⚙️ Common Types of Transformations:

#### **1. Log Transformation**

Used to reduce **skewness** (when data has extreme values).

```python
import numpy as np
data['Salary_Log'] = np.log(data['Salary'])
```

📈 Example: If most salaries are small but a few are extremely high, log-transform helps “compress” large values.

---

#### **2. Binning / Discretization**

Convert continuous data into categorical bins.

```python
bins = [0, 20, 40, 60, 100]
labels = ['Teen', 'Young Adult', 'Adult', 'Senior']
data['Age_Group'] = pd.cut(data['Age'], bins=bins, labels=labels)
```

🎯 Use Case: Converting continuous ages into meaningful groups.

---

#### **3. Polynomial Features**

Adds interaction terms between features — useful for models that capture **non-linear relationships**.

```python
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2, include_bias=False)
poly_features = poly.fit_transform(data[['Age', 'Salary']])
```

Now the dataset includes:

* Age², Salary², and (Age × Salary)

---

#### **4. Power Transformation (Box-Cox / Yeo-Johnson)**

Used to stabilize variance and make data more Gaussian-like.

```python
from sklearn.preprocessing import PowerTransformer

pt = PowerTransformer(method='yeo-johnson')
data[['Salary', 'Age']] = pt.fit_transform(data[['Salary', 'Age']])
```

---

#### **5. Encoding Ordinal Features**

When categories have *natural order* (e.g., Low < Medium < High).

```python
from sklearn.preprocessing import OrdinalEncoder

encoder = OrdinalEncoder(categories=[['Low', 'Medium', 'High']])
data['Priority'] = encoder.fit_transform(data[['Priority']])
```

---

## ⚡ 2️⃣ Feature Engineering

Now comes the creative part — designing **new meaningful features** that reveal hidden patterns in the data.

---

### 🔹 **Feature Combination**

You can combine features to create new relationships.

```python
data['Experience_to_Age'] = data['Experience'] / data['Age']
```

💡 Example: A higher ratio could mean early career advancement.

---

### 🔹 **Date-Time Features**

```python
data['Joining_Date'] = pd.to_datetime(data['Joining_Date'])
data['Join_Year'] = data['Joining_Date'].dt.year
data['Join_Month'] = data['Joining_Date'].dt.month
```

🎯 Extracting time-based features improves time-series or trend-based predictions.

---

### 🔹 **Text-Based Feature Engineering**

```python
data['Text_Length'] = data['Description'].apply(len)
data['Word_Count'] = data['Description'].apply(lambda x: len(x.split()))
```

Helps when analyzing customer reviews, resumes, or logs.

---

### 🔹 **Interaction Features**

```python
data['Salary_per_Experience'] = data['Salary'] / data['Experience']
```

Captures relationships that aren’t obvious individually.

---

## 🧮 3️⃣ Feature Selection (Filtering the Best Ones)

Too many features can lead to **overfitting** or **dimensionality problems**.

Common methods:

* **Correlation analysis**
* **Variance Threshold**
* **Feature importance** from models

```python
from sklearn.feature_selection import VarianceThreshold

selector = VarianceThreshold(threshold=0.01)
reduced_data = selector.fit_transform(data)
```

---

## 🧠 Socratic Questions

1. Why might we use a log transformation on salary data?
2. What’s the difference between one-hot encoding and ordinal encoding?
3. Why is feature engineering often called an “art” in machine learning?
4. How can polynomial features help non-linear models?

---

## 💪 Mini Exercise

Create a DataFrame with the following columns:

| Age | Salary | Experience | Priority | Joining_Date |
| --- | ------ | ---------- | -------- | ------------ |
| 22  | 30000  | 1          | Low      | 2020-06-10   |
| 28  | 50000  | 4          | Medium   | 2018-09-12   |
| 35  | 75000  | 8          | High     | 2015-02-03   |
| 45  | 120000 | 15         | High     | 2010-10-11   |

Perform:

1. Log-transform Salary
2. Create `Age_Group` bins
3. Encode `Priority` using OrdinalEncoder
4. Add a new feature `Experience_to_Age`
5. Extract `Join_Year` and `Join_Month`
