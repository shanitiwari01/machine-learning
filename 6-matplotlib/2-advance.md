## 🧩 ** Customization, Subplots, and Styling in Matplotlib**

---

### 🧠 **1️⃣ Customizing Colors, Lines, and Markers**

Matplotlib gives you complete control over how your plots look — color, style, shape, size, etc.

**Example:**

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(
    x, y,
    color='magenta',      # line color
    linestyle='--',       # solid(-), dashed(--), dotted(:)
    linewidth=2,          # line thickness
    marker='o',           # marker style
    markersize=8,         # marker size
    markerfacecolor='yellow'
)

plt.title("Prime Number Growth")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid(True)
plt.show()
```

🎨 You can use **named colors** (‘red’, ‘blue’, ‘green’) or hex codes (‘#FF5733’).

---

### 💬 **2️⃣ Adding Titles, Labels, and Legends**

Labels help your chart speak for itself.

```python
plt.plot(x, y, label="Prime Numbers", color='orange')
plt.title("Prime Numbers Over Time", fontsize=14, fontweight='bold')
plt.xlabel("Index", fontsize=12)
plt.ylabel("Prime Value", fontsize=12)
plt.legend(loc="upper left")
plt.show()
```

✅ Use `plt.legend()` to identify multiple datasets.

---

### 🧩 **3️⃣ Subplots — Multiple Charts in One Figure**

Sometimes, you need multiple related visualizations together.
You can use **`plt.subplot(rows, cols, position)`** or **`plt.subplots()`** (modern approach).

#### Example 1: `subplot()`

```python
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 16, 9, 4, 1]

plt.subplot(1, 2, 1)
plt.plot(x, y1, color='teal')
plt.title("Increasing")

plt.subplot(1, 2, 2)
plt.plot(x, y2, color='coral')
plt.title("Decreasing")

plt.tight_layout()
plt.show()
```

#### Example 2: `subplots()` (recommended)

```python
fig, axs = plt.subplots(2, 1, figsize=(6, 6))

axs[0].plot(x, y1, color='purple')
axs[0].set_title("Square Numbers")

axs[1].plot(x, y2, color='green')
axs[1].set_title("Reverse Pattern")

plt.tight_layout()
plt.show()
```

---

### 🧭 **4️⃣ Annotations — Highlight Key Points**

Annotations help direct attention to important data points.

```python
plt.plot(x, y1, color='orange')
plt.title("Annotation Example")

plt.annotate(
    "Peak Value",
    xy=(5, 25),
    xytext=(3, 20),
    arrowprops=dict(facecolor='black', shrink=0.05)
)

plt.show()
```

📍 You can use arrows, boxes, or highlights to point at specific values.

---

### 🌈 **5️⃣ Themes & Styles**

Matplotlib has built-in style themes for better aesthetics.

```python
import matplotlib.pyplot as plt
plt.style.use('ggplot')  # others: 'seaborn', 'fivethirtyeight', 'bmh', etc.
```

Try:

```python
print(plt.style.available)
```

to see all styles.

---

### 🧠 **6️⃣ Adding Grids and Axis Limits**

```python
plt.plot(x, y1)
plt.grid(True, linestyle=':', color='gray', alpha=0.7)
plt.xlim(0, 6)
plt.ylim(0, 30)
plt.show()
```

---

### 🧠 **Mini Quiz**

1. What function allows you to display multiple plots in one figure?
2. How can you make your plot background follow a predefined theme?
3. Which method adds a label for your plotted data?
4. What function adds an arrow to highlight data points?

---

### 🏋️‍♀️ **Mini Exercise**

Create **two subplots**:

* (1) A **line plot** showing population growth over 5 years
* (2) A **bar chart** showing birth rate by year

Add:

* Titles, axis labels, grid, and legend
* Use a custom style (like `'seaborn'`)
* Annotate the highest point on the line chart
