## 📘 Python Functions

A **function** is a reusable block of code that performs a specific task.
You define it once and use it whenever needed — just like pressing a button that runs a pre-set action.

---

### ✅ Basic Syntax

```python
def function_name(parameters):
    # code block
    return result
```

Example:

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Shani"))
```

Output:

```
Hello, Shani!
```

---

### 🧠 Why Use Functions?

* **Avoid repetition** (Don’t Repeat Yourself principle)
* **Make code modular** and organized
* **Easier debugging & testing**
* **Encapsulate logic** — each function does *one job well*

---

### 🧩 Types of Functions

1. **Built-in Functions**
   Already available in Python — like `print()`, `len()`, `sum()`, `type()`.

2. **User-defined Functions**
   Created by you using `def`.

3. **Lambda (Anonymous) Functions**
   Small one-line functions using `lambda`.

   ```python
   square = lambda x: x * x
   print(square(5))  # 25
   ```

---

### 🔁 Parameters and Arguments

```python
def add(a, b):
    return a + b

print(add(5, 3))  # 8
```

You can also use **default parameters**:

```python
def greet(name="Guest"):
    print("Hello,", name)

greet()           # Hello, Guest
greet("Shani")    # Hello, Shani
```

---

### 🧰 Return Statement

`return` sends a result back to the caller.

```python
def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(result)  # 20
```

If you don’t use `return`, the function gives back `None` by default.

---

### ⚙️ Variable Scope

* **Local variable** → inside a function, temporary
* **Global variable** → defined outside, accessible everywhere

```python
x = 10  # global

def show():
    y = 5  # local
    print(x + y)

show()
```

---

### 🔍 Real-World Example

```python
def calculate_discount(price, discount=10):
    """Calculate final price after discount"""
    final_price = price - (price * discount / 100)
    return final_price

print(calculate_discount(1000))      # 900
print(calculate_discount(1000, 25))  # 750
```

---

### 🔎 Analogy

Think of a **function like a vending machine**:

* You input parameters (money + item code).
* The machine runs its internal process (function code).
* You get an output (your drink/snack — the return value).

---

### 🤔 Socratic Questions

1. What’s the difference between **parameters** and **arguments**?
2. What will happen if a function doesn’t include a `return` statement?
3. Why might you use default arguments in a function?

---

### 📝 Mini Exercise

Create a function `area_of_circle(radius)` that:

1. Takes `radius` as input.
2. Uses the formula `area = 3.14 * radius ** 2`.
3. Returns the area.
4. Call the function for radius `5` and print the result.
