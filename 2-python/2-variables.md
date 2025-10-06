## Python Variables

### 📝 Explanation

A **variable** in Python is like a **container** (or a labeled box) that stores data values.

* You create a variable by assigning a value using `=`.
* The variable name points to the value stored in memory.

Example:

```python
x = 10       # integer
name = "Shani"  # string
pi = 3.14    # float
```

* Here `x`, `name`, and `pi` are variables.

Python is **dynamically typed**, meaning you don’t need to declare the type — it’s inferred automatically.

---

### 🌍 Analogy

Think of a variable as a **jar with a label**:

* You can write “Sugar” on the jar and put sugar in it.
* Later, you can change the label to “Flour” and put flour in the same jar.

Similarly, in Python:

```python
x = 10
x = "Hello"  # x now stores a string instead of a number
```

---

### 📊 Example

```python
# Storing student details
student_name = "Arjun"
student_age = 21
is_enrolled = True

print(student_name, student_age, is_enrolled)
```

---

### ❓ Socratic Questions

1. Why do you think variable names should be meaningful (e.g., `student_age`) instead of just `a` or `x`?
2. What will happen if you do this in Python?

```python
count = 5
count = count + 2
print(count)
```

---

### 🏋️‍♂️ Mini Exercise

Write a Python snippet with three variables:

* your name
* your age
* your favorite programming language

👉 Print them in a single line like:

```
My name is Shani, I am 27 years old, and I love Python.
```