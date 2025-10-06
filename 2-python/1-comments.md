## Python Comments

### 📝 Explanation

In Python, **comments** are lines in code that are **ignored by the interpreter**. They’re only for humans to read and understand the code.

Types of comments:

1. **Single-line comment** → starts with `#`

```python
# This is a single-line comment
x = 5  # You can also comment at the end of a line
```

2. **Multi-line comment / Docstring** → use triple quotes `'''` or `"""`

```python
"""
This is a multi-line comment
It is often used for documentation
"""
```

⚠️ Note: Triple quotes are actually strings, but if not assigned to a variable, they behave like comments.

---

### 🌍 Analogy

Think of comments like **sticky notes on your code**:

* They don’t change how the program runs.
* They just help people (including *future you*) understand the logic.

---

### 📊 Example

```python
# Calculate area of a rectangle
length = 10
width = 5

# Formula: area = length * width
area = length * width

print(area)  # Expected output: 50
```

---

### ❓ Socratic Questions

1. Why do you think comments are important even though they don’t affect the code?
2. What might happen in a big project if nobody used comments?

---

### 🏋️‍♂️ Mini Exercise

Write a short Python snippet to calculate the square of a number.
👉 Add comments explaining:

* what the program does
* what each step is doing
