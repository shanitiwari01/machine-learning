## 🎯 Lesson 1: Introduction to Model Evaluation and Metrics

### 🧠 Concept

Once you train a model (like a Decision Tree, KNN, etc.), you must **evaluate** how well it performs.
The goal is to measure:

* How **accurately** the model predicts unseen data.
* How well it **generalizes** (not just memorizes the training data).

We do this using **evaluation metrics**.

---

### ⚙️ Key Idea: Train-Test Split

Before evaluating, we divide our data:

* **Training set:** Used to train the model.
* **Testing set:** Used to measure performance.

Example:
If you have 1000 data points → 800 for training, 200 for testing.

---

### 🧮 Basic Metrics for Classification

1. **Accuracy:**
$$
   [
   \text{Accuracy} = \frac{\text{Correct Predictions}}{\text{Total Predictions}}
   ]
$$

   * Simple and intuitive.
   * But not reliable for **imbalanced data** (e.g., 95% “No” and 5% “Yes”).

2. **Precision:**
   Out of all predicted positives, how many were actually positive?
   $$
    [
    \text{Precision} = \frac{TP}{TP + FP}
    ]
    $$

3. **Recall (Sensitivity):**
   Out of all actual positives, how many did we correctly predict?
   $$
    [
    \text{Recall} = \frac{TP}{TP + FN}
    ]
    $$

4. **F1 Score:**
   Harmonic mean of Precision and Recall.
   $$
    [
    \text{F1} = 2 \times \frac{Precision \times Recall}{Precision + Recall}
    ]
    $$
   Good when you need a balance between precision and recall.

---

### 📊 For Regression Models

1. **Mean Absolute Error (MAE):**
   Average of absolute differences between predicted and actual values.
   $$
    [
    MAE = \frac{1}{n}\sum |y_i - \hat{y_i}|
    ]
    $$

2. **Mean Squared Error (MSE):**
   Squares the errors before averaging (penalizes large errors more).
   $$
    [
    MSE = \frac{1}{n}\sum (y_i - \hat{y_i})^2
    ]
    $$

3. **Root Mean Squared Error (RMSE):**
   Square root of MSE — keeps units consistent.
   $$
    [
    RMSE = \sqrt{MSE}
    ]
    $$

4. **R² (Coefficient of Determination):**
   Measures how well the model explains variance in the data (closer to 1 = better).

---

### ⚖️ Analogy

Think of model metrics like a **report card** for your ML model:

* Accuracy = overall grade
* Precision = how careful you are when calling something “positive”
* Recall = how many real positives you found
* F1 = your balanced performance score

---

### 💬 Socratic Questions

1. Why might *accuracy* be misleading in a dataset where 95% of the samples belong to one class?
2. If a doctor is diagnosing cancer, would you prefer **high recall** or **high precision**, and why?

---

### 🧩 Mini Exercise

Imagine this confusion matrix for a binary classification:

|                     | Predicted Positive | Predicted Negative |
| ------------------- | ------------------ | ------------------ |
| **Actual Positive** | 90                 | 10                 |
| **Actual Negative** | 20                 | 80                 |

Can you calculate **Accuracy**, **Precision**, and **Recall** for this model?
