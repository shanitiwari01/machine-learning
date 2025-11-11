## 🧠 **Topic: Data Preprocessing**

---

### ⚙️ **1️⃣ What is Data Preprocessing?**

Data preprocessing is the **data-cleaning and transformation phase** that prepares raw data for analysis or model training.
In real-world scenarios, datasets often contain:

* Missing values ❌
* Duplicates 🔁
* Inconsistent formatting 🧩
* Unscaled numerical features ⚖️
* Categorical data (text) that ML models can’t handle directly 🔡

So preprocessing ensures the model can **learn efficiently and accurately**.

---

## 🧩 **2️⃣ Key Steps in Data Preprocessing**

Let’s go step-by-step.

---

### 🧹 **Step 1: Importing the Dataset**

```python
import pandas as pd

data = pd.read_csv('data.csv')
print(data.head())
```

---

### 🚫 **Step 2: Handling Missing Values**

**Option 1: Drop missing values**

```python
data.dropna(inplace=True)
```

**Option 2: Fill missing values**

```python
data['Age'].fillna(data['Age'].mean(), inplace=True)  # Mean imputation
data['City'].fillna('Unknown', inplace=True)           # Fill string columns
```

✅ Other strategies: `median`, `mode`, or predictive imputation (advanced).

---

### 🔁 **Step 3: Handling Duplicates**

```python
data.drop_duplicates(inplace=True)
```

This ensures no repeated entries affect the model’s learning.

---

### 🔤 **Step 4: Encoding Categorical Data**

Machine learning models work with numbers — not text.
So, you need to convert categorical columns into numeric form.

**Example Dataset:**

| Country | Gender | Salary |
| ------- | ------ | ------ |
| France  | Male   | 45000  |
| Spain   | Female | 54000  |
| Germany | Female | 61000  |

**Encoding:**

```python
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

# Label Encoding for binary columns
le = LabelEncoder()
data['Gender'] = le.fit_transform(data['Gender'])

# One-Hot Encoding for multi-class columns
ct = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), ['Country'])],
    remainder='passthrough'
)
data = ct.fit_transform(data)
```

Now "Country" becomes multiple binary columns — one for each country.

---

### 📏 **Step 5: Feature Scaling (Normalization / Standardization)**

Features like “Age” and “Salary” may have different ranges —
ML models (like KNN, SVM, Gradient Descent-based algorithms) need them on similar scales.

**Standardization (Z-score scaling):**

```python
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
data_scaled = sc.fit_transform(data)
```

Formula:
$$
[
z = \frac{x - \text{mean}}{\text{std}}
]
$$

**Normalization (Min-Max scaling):**

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
data_normalized = scaler.fit_transform(data)
```

Formula:
$$
[
x' = \frac{x - \text{min}}{\text{max} - \text{min}}
]
$$

---

### 🧠 **Step 6: Splitting the Dataset (Training & Testing)**

You need to split the data so you can test model performance on unseen data.

```python
from sklearn.model_selection import train_test_split

X = data.iloc[:, :-1].values   # features
y = data.iloc[:, -1].values    # target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

---

### 🧩 **Step 7: Outlier Detection and Removal (Optional)**

Outliers can bias your model.

**Using IQR (Interquartile Range):**

```python
Q1 = data['Salary'].quantile(0.25)
Q3 = data['Salary'].quantile(0.75)
IQR = Q3 - Q1

filtered_data = data[~((data['Salary'] < (Q1 - 1.5 * IQR)) | (data['Salary'] > (Q3 + 1.5 * IQR)))]
```

---

### 📊 **Step 8: Feature Engineering (Optional)**

You can create new features that might help the model —
for example:

* `BMI = Weight / (Height ** 2)`
* `Age_Group` from continuous `Age` values

---

### 🧠 **Mini Quiz**

1. What’s the difference between normalization and standardization?
2. Why do we perform encoding for categorical data?
3. What’s the use of splitting data into training and testing sets?
4. What function removes duplicate records in pandas?

---

### 🏋️‍♀️ **Mini Exercise**

Use the dataset below (create your own small CSV or DataFrame):

| Country | Age | Salary | Purchased |
| ------- | --- | ------ | --------- |
| France  | 44  | 72000  | No        |
| Spain   | 27  | 48000  | Yes       |
| Germany | 30  | NaN    | No        |
| Spain   | 38  | 61000  | No        |
| Germany | 40  | 67000  | Yes       |

Perform the following:

1. Fill missing salary with **mean**
2. Encode “Country” and “Purchased” columns
3. Split the dataset into **80/20 train-test**
4. Apply **StandardScaler** to the features
