# 🧠 Topic: K-Nearest Neighbors (KNN)

---

## ⚙️ 1️⃣ What is K-Nearest Neighbors?

KNN is a **supervised learning algorithm** that can perform both **classification** and **regression**.

Instead of building a mathematical model during training, it **stores all the training data** and makes predictions based on the **similarity (distance)** between new and existing points.

💡 **Think of it like this:**
You move into a new neighborhood and want to guess your likely income level. You look at your *K nearest neighbors* — if most of them earn high, your predicted income is likely high too.

---

## 🔍 2️⃣ How KNN Works (Step-by-Step)

Let’s say you want to predict whether a new student will **pass or fail** based on **study hours** and **sleep hours**.

1. **Choose a value for K** (e.g., 3)
2. **Calculate the distance** between the new student and all others in the dataset
   (usually Euclidean distance)
3. **Find the K nearest neighbors**
4. **Vote (classification)** → take the most common label among neighbors
   or
   **Average (regression)** → take the mean of neighbor values

---

### ✳️ Example Diagram (Conceptually)

Imagine points plotted on a 2D graph:

* 🔵 = Pass
* 🔴 = Fail

When you add a new point ❌, KNN looks at the 3 nearest points.
If 2 out of 3 are 🔵, the new point is predicted as “Pass.”

---

## 📏 3️⃣ Distance Metrics

The **distance metric** defines “closeness” between points.

| Distance Type         | Formula                                  | When to Use                   |   |           |   |                              |
| --------------------- | ---------------------------------------- | ----------------------------- | - | --------- | - | ---------------------------- |
| **Euclidean**         | ( \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2} ) | Default for numeric data      |   |           |   |                              |
| **Manhattan**         | (                                        | x_1 - x_2                     | + | y_1 - y_2 | ) | Grid-like or city-block data |
| **Minkowski**         | Generalization of both                   | Mixed data types              |   |           |   |                              |
| **Cosine Similarity** | Measures angle, not distance             | Text or high-dimensional data |   |           |   |                              |

---

## 🧮 4️⃣ Example: Classification with KNN

```python
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

# Dataset
data = pd.DataFrame({
    'Hours_Studied': [1, 2, 3, 4, 5, 6],
    'Sleep_Hours': [9, 8, 7, 6, 5, 4],
    'Pass': [0, 0, 0, 1, 1, 1]
})

X = data[['Hours_Studied', 'Sleep_Hours']]
y = data['Pass']

# Model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Predict for a new student
pred = model.predict([[3.5, 6]])
print(pred)  # Output: [1] → Predicted Pass
```

---

## 📊 5️⃣ Choosing the Right K

* If **K is too small** → Model becomes sensitive to noise (overfits)
* If **K is too large** → Model becomes too smooth (underfits)

✅ A common trick:
Use **odd K values** (like 3, 5, 7) to avoid ties in classification.

To choose the best K, use **cross-validation**.

---

## ⚡ 6️⃣ KNN for Regression

Instead of voting, KNN Regression averages the numeric values of the K nearest neighbors.

```python
from sklearn.neighbors import KNeighborsRegressor

model = KNeighborsRegressor(n_neighbors=3)
model.fit(X, y)
pred = model.predict([[3.5, 6]])
print(pred)
```

---

## ⚙️ 7️⃣ Data Scaling is Crucial ⚠️

Since KNN relies on distance, **features with large ranges dominate** the result.
So, always scale your data using StandardScaler or MinMaxScaler before applying KNN.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

---

## 🧠 Socratic Questions

1. Why does KNN not have a traditional “training” phase?
2. What might happen if one feature (like Salary) is much larger in scale than another (like Age)?
3. How would increasing K affect model accuracy and bias?
4. Why do we often use odd values for K?

---

## 💪 Mini Exercise

Create a small dataset:

| Study Hours | Sleep Hours | Pass |
| ----------- | ----------- | ---- |
| 1           | 9           | 0    |
| 2           | 8           | 0    |
| 3           | 7           | 0    |
| 4           | 6           | 1    |
| 5           | 5           | 1    |
| 6           | 4           | 1    |

Tasks:

1. Train a KNN classifier with `n_neighbors = 3`.
2. Predict for a new student who studied `3.5` hours and slept `6` hours.
3. Try changing K = 1, 3, 5 — observe how predictions change.
4. Apply `StandardScaler` and see if the result differs.

---

## 🧩 Bonus Insight

✅ **Pros**

* Simple, intuitive, no training time
* Works for both regression & classification
* Handles non-linear relationships

❌ **Cons**

* Slow for large datasets (since it checks all neighbors)
* Sensitive to irrelevant or unscaled features
* Doesn’t handle high dimensions well (curse of dimensionality)
