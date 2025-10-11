## 📘 Python Tuples

A **tuple** in Python is an **ordered, immutable** collection of items.
It’s written using **parentheses `( )`** instead of square brackets.

```python
fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3, 4)
mixed = ("AI", 42, True, 3.14)
```

---

### ✅ Key Properties

1. **Ordered** → elements have a defined position (index-based).
2. **Immutable** → cannot be changed (no adding, removing, or modifying elements after creation).
3. **Allow duplicates** → repeated values are fine.
4. **Can hold mixed data types** (like lists).

---

### 🧩 Example

```python
person = ("Shani", 27, "Engineer")
print(person[0])    # Shani
print(person[-1])   # Engineer
```

You can **slice** tuples, just like lists:

```python
print(person[0:2])  # ('Shani', 27)
```

---

### 🔒 Immutability Example

```python
colors = ("red", "blue", "green")
# colors[1] = "yellow"  ❌  # Error: 'tuple' object does not support item assignment
```

You can’t modify tuples directly — that’s what makes them **safe** and **reliable** for fixed data.

---

### 🧰 Tuple Methods

Tuples have fewer methods than lists because they can’t be changed.

| Method     | Description                     | Example                      |
| ---------- | ------------------------------- | ---------------------------- |
| `count(x)` | Counts how many times x appears | `(1,2,2,3).count(2)` → `2`   |
| `index(x)` | Returns the index of x          | `(10,20,30).index(20)` → `1` |

You can also use `len()` to get tuple length:

```python
len(("AI", "ML", "Data"))
```

---

### 🔄 Tuple Packing and Unpacking

```python
# Packing
student = ("Shani", 90, "A")

# Unpacking
name, marks, grade = student
print(name)   # Shani
print(marks)  # 90
```

---

### 🔍 Real-World Example

Tuples are often used for **fixed data** or when you want to ensure data can’t be changed.

Example:

```python
location = (28.6139, 77.2090)  # Coordinates of Delhi
print("Latitude:", location[0])
print("Longitude:", location[1])
```

Tuples are great for storing coordinates, database records, or configuration constants.

---

### 🔎 Analogy

Think of a **tuple like a sealed box** 📦 —
once packed, you can read what’s inside, but you can’t change the contents.

A **list** is like an **open shopping bag** 🛍️ — you can add or remove items anytime.

---

### 🤔 Socratic Questions

1. What would happen if you try to modify an element inside a tuple?
2. How can you access elements from a tuple?
3. Why might you prefer a tuple over a list in certain situations?

---

### 📝 Mini Exercise

Create a tuple called `student` with values:
`("Shani", "AI Engineer", 2025)`

1. Print the job title.
2. Try changing the year to 2026 (observe what happens).
3. Unpack the tuple into three variables and print them separately.
