## 📈 Lesson 2: Visual Evaluation — Confusion Matrix, ROC Curve, and AUC

### 🧠 Concept: Confusion Matrix

A **Confusion Matrix** helps you *visualize* how many predictions were correct or incorrect across different classes.

It’s a 2×2 table for binary classification:

|                     | **Predicted Positive** | **Predicted Negative** |
| ------------------- | ---------------------- | ---------------------- |
| **Actual Positive** | True Positive (TP)     | False Negative (FN)    |
| **Actual Negative** | False Positive (FP)    | True Negative (TN)     |

---

### ⚙️ Example

Suppose a model predicts whether emails are spam or not:

|                     | Predicted Spam | Predicted Not Spam |
| ------------------- | -------------- | ------------------ |
| **Actual Spam**     | 90 (TP)        | 10 (FN)            |
| **Actual Not Spam** | 20 (FP)        | 80 (TN)            |

From this table:

* **Accuracy** = (TP + TN) / Total = (90 + 80) / 200 = 85%
* **Precision** = TP / (TP + FP) = 90 / (90 + 20) = 81.8%
* **Recall** = TP / (TP + FN) = 90 / (90 + 10) = 90%

---

### 🪞 Analogy

Think of this like a **doctor’s diagnostic test**:

* **True Positive (TP):** Sick and correctly diagnosed sick.
* **False Negative (FN):** Sick but diagnosed healthy — dangerous miss.
* **False Positive (FP):** Healthy but diagnosed sick — unnecessary alarm.
* **True Negative (TN):** Healthy and diagnosed healthy.

---

### 🧩 ROC Curve (Receiver Operating Characteristic)

ROC Curve shows the trade-off between **True Positive Rate (Recall)** and **False Positive Rate**.

* **X-axis:** False Positive Rate (FPR) = FP / (FP + TN)
* **Y-axis:** True Positive Rate (TPR) = TP / (TP + FN)

Each point on the curve represents a **different threshold** for classification probability.

**Good Model:** Curve rises quickly toward top-left.
**Bad Model:** Curve stays close to the diagonal (random guessing).

---

### 💠 AUC (Area Under the Curve)

* A single number summarizing the ROC Curve.
* **AUC = 1.0** → Perfect model.
* **AUC = 0.5** → Random model.
* **AUC < 0.5** → Worse than random.

---

### 🧠 Socratic Questions

1. If your model has high recall but low precision, what does that tell you about its behavior?
2. Why might we prefer AUC instead of accuracy when comparing two models?

---

### 🏋️ Mini Exercise

Suppose two models have the following:

* **Model A:** AUC = 0.93
* **Model B:** Accuracy = 95%, AUC = 0.60

Which model would you *actually* trust more — and why?
