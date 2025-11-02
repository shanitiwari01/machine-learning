# ⚙️ Topic: **Advanced Feature Scaling & Normalization**

---

## 🧩 1️⃣ Why Scaling Matters

Many ML algorithms (especially distance- or gradient-based ones like KNN, SVM, and Linear Regression) **assume all features are on the same scale**.

📊 Example:

* Feature A = “Age” (range 20–70)
* Feature B = “Salary” (range 30,000–300,000)

Without scaling, the model gives too much importance to “Salary,” simply because it has a larger numeric range.

---

## ⚖️ 2️⃣ Recap: Standardization vs Normalization

| Technique           | Formula                                     | Range          | Use Case                                 |
| ------------------- | ------------------------------------------- | -------------- | ---------------------------------------- |
| **Standardization** | ( z = \frac{x - \mu}{\sigma} )              | No fixed range | Data with normal (Gaussian) distribution |
| **Normalization**   | ( x' = \frac{x - min(x)}{max(x) - min(x)} ) | [0, 1]         | Data with unknown or skewed distribution |

---

## 🧠 3️⃣ Advanced Scaling Techniques

### 🔹 **(1) RobustScaler**

* Uses **median** and **IQR** (Interquartile Range)
* Best for **datasets with outliers**
* Less sensitive to extreme values

```python
from sklearn.preprocessing import RobustScaler
import pandas as pd

data = pd.DataFrame({
    'Salary': [30000, 50000, 70000, 120000, 1000000]
})

scaler = RobustScaler()
data_scaled = scaler.fit_transform(data)

print(data_scaled)
```

💡 Real-world use: Salary, transaction amounts, or house prices — where a few values can be huge outliers.

---

### 🔹 **(2) QuantileTransformer**

* Transforms features to **follow a uniform or normal distribution**
* Great for **highly skewed data**

```python
from sklearn.preprocessing import QuantileTransformer

qt = QuantileTransformer(output_distribution='normal')
data_qt = qt.fit_transform(data)
```

💡 This ensures that even non-Gaussian data can work well with algorithms that assume normality (like Linear Regression).

---

### 🔹 **(3) PowerTransformer (Box-Cox / Yeo-Johnson)**

* Used to make data **more Gaussian-like**
* Handles **both positive and negative values**
* Stabilizes variance and reduces skewness

```python
from sklearn.preprocessing import PowerTransformer

pt = PowerTransformer(method='yeo-johnson')
data_pt = pt.fit_transform(data)
```

💡 Best when you want smooth, symmetric data for regression models.

---

### 🔹 **(4) MaxAbsScaler**

* Scales data by dividing by the **maximum absolute value**
* Keeps **sign information** (negative values remain negative)
* Ideal for **sparse datasets** (like TF-IDF vectors)

```python
from sklearn.preprocessing import MaxAbsScaler

scaler = MaxAbsScaler()
data_maxabs = scaler.fit_transform(data)
```

---

### 🔹 **(5) Unit Vector Transformation (L2 Normalization)**

* Converts each row (data point) into a **unit vector**
* Common in **text or cosine similarity-based models**

```python
from sklearn.preprocessing import Normalizer

from sklearn.preprocessing import Normalizer
scaler = Normalizer(norm='l2')
data_norm = scaler.fit_transform(data)
```

---

## ⚙️ 4️⃣ When to Use Which Scaler

| Data Situation          | Best Scaler                            |
| ----------------------- | -------------------------------------- |
| Gaussian distribution   | StandardScaler                         |
| Many outliers           | RobustScaler                           |
| Highly skewed data      | QuantileTransformer / PowerTransformer |
| Sparse data             | MaxAbsScaler                           |
| Similarity-based models | Normalizer                             |

---

## 🧠 Socratic Questions

1. Why might RobustScaler work better than StandardScaler when outliers are present?
2. What’s the difference between QuantileTransformer and PowerTransformer?
3. In what situation would you use a Normalizer instead of a StandardScaler?
4. If your data has both negative and positive values, which scaler might you avoid?

---

## 💪 Mini Exercise

Create the following DataFrame:

| Age | Salary | Experience |
| --- | ------ | ---------- |
| 22  | 30000  | 1          |
| 28  | 50000  | 4          |
| 35  | 75000  | 8          |
| 45  | 120000 | 15         |
| 60  | 800000 | 35         |

Perform:

1. Standard scaling using `StandardScaler`
2. Robust scaling using `RobustScaler`
3. Quantile transformation to normal distribution
4. Compare the outputs — what difference do you observe?

---

## 🧩 Bonus Tip

In production pipelines, **fit the scaler only on training data**, and then **transform both train & test**:

```python
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

This prevents *data leakage* from test data into the training process.
