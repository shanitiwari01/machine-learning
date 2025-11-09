# 🧠 Topic: Supervised Learning

---

## ⚙️ 1️⃣ What is Supervised Learning?

Supervised learning is a **machine learning approach** where the model learns from **labeled data** — that is, data that already has the correct answers (outputs).

You “supervise” the model by showing examples of inputs *and* their corresponding correct outputs.

💡 **Analogy:**
Think of a student learning math problems from a teacher.

* The teacher gives example problems (inputs) and solutions (outputs).
* The student (model) learns the pattern.
* Then the student is tested on new problems.

---

### 🧩 Example:

| Hours Studied | Exam Score |
| ------------- | ---------- |
| 1             | 20         |
| 2             | 40         |
| 3             | 60         |
| 4             | 80         |

Here:

* **Input (X):** Hours Studied
* **Output (Y):** Exam Score

The model learns the relationship between `X` and `Y`, so it can predict scores for unseen hours like 5 or 6.

---

## 🧮 2️⃣ Types of Supervised Learning

Supervised learning is divided into two main types:

| Type               | Output                   | Example                                     |
| ------------------ | ------------------------ | ------------------------------------------- |
| **Regression**     | Continuous numeric value | Predicting house prices, temperature, sales |
| **Classification** | Categorical label        | Spam/Not spam, Disease/No disease, Gender   |

---

### 🟢 **Regression Example (Predicting Numbers)**

Predicting **salary based on experience**:

```python
from sklearn.linear_model import LinearRegression
import pandas as pd

data = pd.DataFrame({
    'Experience': [1, 2, 3, 4, 5],
    'Salary': [25000, 35000, 45000, 55000, 65000]
})

X = data[['Experience']]
y = data['Salary']

model = LinearRegression()
model.fit(X, y)

pred = model.predict([[6]])
print(pred)  # Predict salary for 6 years of experience
```

---

### 🔵 **Classification Example (Predicting Categories)**

Predicting whether a student passes or fails based on study hours:

```python
from sklearn.linear_model import LogisticRegression

data = pd.DataFrame({
    'Hours': [1, 2, 3, 4, 5],
    'Pass': [0, 0, 0, 1, 1]
})

X = data[['Hours']]
y = data['Pass']

model = LogisticRegression()
model.fit(X, y)

pred = model.predict([[3.5]])
print(pred)
```

---

## 🔍 3️⃣ How Supervised Learning Works (The Pipeline)

1. **Collect labeled data**

   * Example: images of cats and dogs with correct labels.
2. **Split data into training & testing**

   * So the model can be evaluated on unseen data.
3. **Choose a model**

   * Example: Linear Regression, Decision Tree, SVM, etc.
4. **Train the model**

   * Model learns patterns in the training data.
5. **Predict on test data**

   * Apply learned rules to unseen examples.
6. **Evaluate performance**

   * Use metrics like accuracy, precision, recall, or RMSE.

---

## 📊 4️⃣ Common Algorithms in Supervised Learning

| Algorithm                    | Type           | Description                          |
| ---------------------------- | -------------- | ------------------------------------ |
| Linear Regression            | Regression     | Predicts continuous values           |
| Logistic Regression          | Classification | Predicts categorical outcomes        |
| Decision Trees               | Both           | Tree-based decision-making           |
| Random Forest                | Both           | Ensemble of multiple trees           |
| Support Vector Machine (SVM) | Both           | Finds the best separating boundary   |
| K-Nearest Neighbors (KNN)    | Both           | Predicts based on nearby data points |
| Naive Bayes                  | Classification | Based on probability                 |
| Gradient Boosting / XGBoost  | Both           | Advanced ensemble techniques         |

---

## 🎯 5️⃣ Evaluation Metrics

| Type               | Metrics                                                            |
| ------------------ | ------------------------------------------------------------------ |
| **Regression**     | Mean Squared Error (MSE), Root Mean Squared Error (RMSE), R² Score |
| **Classification** | Accuracy, Precision, Recall, F1-Score, Confusion Matrix            |

---

## 🧠 Socratic Questions

1. What is the main difference between regression and classification?
2. Why do we need labeled data in supervised learning?
3. Can a model trained for regression be used for classification? Why or why not?
4. What might happen if you train and test on the same data?

---

## 💪 Mini Exercise

Create a small dataset:

| Study Hours | Score |
| ----------- | ----- |
| 1           | 20    |
| 2           | 40    |
| 3           | 60    |
| 4           | 80    |
| 5           | 100   |

Tasks:

1. Use `LinearRegression` to train on this data.
2. Predict the score for 6 study hours.
3. Print the model’s slope (coefficient) and intercept.
4. Visualize it with a scatter plot and regression line (optional using `matplotlib`).
