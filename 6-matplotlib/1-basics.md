## 🧩 **Topic: Matplotlib**

---

### 🧠 **1️⃣ Concept Overview**

**Matplotlib** is a powerful library for creating **static, interactive, and animated visualizations** in Python.
It’s often used with **NumPy** and **Pandas** to plot data quickly.

You can create:

* Line charts 📈
* Bar charts 📊
* Pie charts 🥧
* Histograms 📉
* Scatter plots 🌌

and much more.

---

### ⚙️ **Installation**

If you don’t have it yet:

```bash
pip install matplotlib
```

Then import:

```python
import matplotlib.pyplot as plt
```

---

### 💡 **Analogy**

Think of **Matplotlib** like a painter 🎨:

* The **canvas** = figure (`plt.figure()`)
* The **brush strokes** = plots (`plt.plot()`, `plt.bar()`, etc.)
* The **final painting** = chart (`plt.show()`)

---

### 🧮 **2️⃣ Basic Line Plot Example**

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()
```

🖼️ **Output:** A simple line graph showing a straight line (y = 2x).

---

### 🔧 **3️⃣ Adding Styles**

You can customize your plots easily:

```python
plt.plot(x, y, color='green', linestyle='--', marker='o')
plt.title("Styled Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid(True)
plt.show()
```

✅ **Markers**, **colors**, **line styles**, and **grids** make visuals more readable.

---

### 📊 **4️⃣ Bar Chart**

Perfect for comparing categories.

```python
subjects = ['Math', 'Science', 'History']
marks = [85, 90, 75]

plt.bar(subjects, marks, color='orange')
plt.title("Marks by Subject")
plt.ylabel("Scores")
plt.show()
```

---

### 🥧 **5️⃣ Pie Chart**

Great for showing proportions.

```python
labels = ['Apples', 'Bananas', 'Cherries']
sizes = [30, 45, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Fruit Distribution")
plt.show()
```

---

### ⚡ **6️⃣ Scatter Plot**

Used to show relationships between variables.

```python
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='purple')
plt.title("Scatter Plot Example")
plt.xlabel("Random X")
plt.ylabel("Random Y")
plt.show()
```

---

### 📈 **7️⃣ Histogram**

Shows data distribution.

```python
data = [12, 15, 13, 15, 16, 18, 19, 21, 21, 22, 23, 25, 28, 30]
plt.hist(data, bins=5, color='skyblue', edgecolor='black')
plt.title("Histogram Example")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()
```

---

### ⏫ **8️⃣ Subplots (Multiple Charts Together)**

```python
x = [1, 2, 3, 4, 5]
y1 = [2, 3, 4, 5, 6]
y2 = [5, 4, 3, 2, 1]

plt.subplot(1, 2, 1)
plt.plot(x, y1, color='red')
plt.title("Plot 1")

plt.subplot(1, 2, 2)
plt.plot(x, y2, color='blue')
plt.title("Plot 2")

plt.tight_layout()
plt.show()
```

🖼️ Displays two plots side by side.

---

### 🧠 **Mini Quiz**

1. What function displays the final chart on screen?
2. Which plot type is best for showing proportions?
3. How can you display multiple charts in one figure?
4. Which method is used for adding labels to axes?

---

### 🏋️‍♀️ **Mini Exercise**

Create a **bar chart** showing monthly expenses:

```python
Months = ['Jan', 'Feb', 'Mar', 'Apr']
Expenses = [2200, 2700, 2400, 3000]
```

Then:

* Add a title “Monthly Expenses”
* Label axes “Month” and “Expense ($)”
* Add different color for bars.
