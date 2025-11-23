# 🌟 Lesson 1: What is Unsupervised Learning?

### 🧠 Concept

Unsupervised Learning is a machine learning approach where the model learns **patterns, structure, or relationships** from **unlabeled data** — meaning **no output labels (Y)** are provided.

The algorithm must **find patterns on its own**.

---

### 💡 Real-World Analogy

Imagine entering a party where you don’t know anyone.
Without names or labels, you notice groups:

* People talking about tech
* People talking about fitness
* People talking about finance

You mentally **cluster** people based on their behavior — that's unsupervised learning.

---

## 🔍 What Can Unsupervised Learning Do?

### 1️⃣ **Clustering**

Grouping similar data points.
Examples:

* Customer segmentation
* Grouping similar articles
* Image compression

### 2️⃣ **Dimensionality Reduction**

Reducing the number of features while keeping important information.
Examples:

* PCA (Principal Component Analysis)
* t-SNE
  Used for:
* Visualization
* Noise reduction
* Speeding up ML models

### 3️⃣ **Association**

Finding “if-then” rules.
Examples:

* “People who buy bread also buy butter”
* Market basket analysis (Amazon, BigBasket, Flipkart)

### 4️⃣ **Anomaly Detection**

Finding unusual patterns.
Examples:

* Fraud detection
* System failure detection
* Detecting unusual user behavior

---

## 🧪 Example: Clustering

Let’s say we have shoppers:

| Age | Spending Score |
| --- | -------------- |
| 20  | 80             |
| 21  | 75             |
| 50  | 25             |
| 52  | 20             |

A clustering algorithm like **K-Means** might group:

* Young high-spenders = Group A
* Older low-spenders = Group B

Even without labels, the model finds hidden structure.

---

## 📌 Key Difference from Supervised Learning

| Supervised Learning               | Unsupervised Learning                       |
| --------------------------------- | ------------------------------------------- |
| Has labels (Y)                    | No labels                                   |
| Learns from correct answers       | Finds hidden patterns                       |
| Tasks: classification, regression | Tasks: clustering, dimensionality reduction |

---

## 🤖 Popular Unsupervised Algorithms

### **Clustering**

* K-Means
* Hierarchical Clustering
* DBSCAN

### **Dimensionality Reduction**

* PCA
* t-SNE
* UMAP

### **Association**

* Apriori Algorithm
* FP-Growth

---

## 🧠 Socratic Questions

1. Why do you think clustering is useful when you don’t have labels?
2. If you had 50 features in your dataset, why might dimensionality reduction help?
3. Why can’t accuracy be used as a metric in unsupervised learning?

---

## 🧩 Mini Exercise

Imagine this dataset:

| Height | Weight |
| ------ | ------ |
| 150    | 45     |
| 155    | 48     |
| 160    | 50     |
| 180    | 80     |
| 185    | 85     |

**Question:**
If you run K-Means with K=2, what two natural groups do you think it will form?
