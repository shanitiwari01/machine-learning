## 🧠 Python Exception Handling

---

### 💡 What is an Exception?

An **exception** is an *error* that occurs **during program execution**, disrupting the normal flow of code.

Example 👇

```python
print(10 / 0)
```

🔴 This will throw:

```
ZeroDivisionError: division by zero
```

Without handling, the program **crashes** right here.

---

### 🧯 What is Exception Handling?

**Exception Handling** lets you manage these unexpected errors gracefully — instead of crashing, your program can respond intelligently.

---

### 🧩 Syntax

```python
try:
    # Code that may raise an exception
except ExceptionType:
    # Code to handle that exception
else:
    # Executes if no exception occurs
finally:
    # Always executes (cleanup)
```

---

### 🔍 Example 1 — Simple Handling

```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

✅ Output:

```
Cannot divide by zero!
```

The program doesn’t crash — it *recovers* gracefully.

---

### 🔍 Example 2 — Multiple Exceptions

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("You can’t divide by zero!")
```

---

### 🔍 Example 3 — Using `else` and `finally`

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error occurred.")
else:
    print("Division successful:", result)
finally:
    print("Program finished.")
```

**Output:**

```
Division successful: 5.0  
Program finished.
```

---

### ⚙️ Example 4 — Catching All Exceptions

```python
try:
    x = int("hello")
except Exception as e:
    print("Error:", e)
```

Output:

```
Error: invalid literal for int() with base 10: 'hello'
```

The `Exception` class catches *any* error — and printing `e` shows what went wrong.

---

### 🧩 Example 5 — Raising Your Own Exceptions

You can use `raise` to create intentional exceptions.

```python
age = -5
if age < 0:
    raise ValueError("Age cannot be negative!")
```

Output:

```
ValueError: Age cannot be negative!
```

---

### 🌍 Analogy

Think of **try–except** like a **seatbelt in a car**:

* It doesn’t prevent accidents (errors) from happening,
* but it protects your program (and user) from a crash. 🚗💥

---

### 🧠 Socratic Questions

1. Why is it better to handle exceptions instead of letting the program crash?
2. What’s the difference between `except ValueError` and `except Exception as e`?
3. Why might we use `finally` even if no exception occurs?

---

### 🏋️ Mini Exercise

Write a program that:

* Takes two numbers as input
* Tries to divide them
* Catches `ZeroDivisionError` and `ValueError`
* Prints “Division successful” when no errors occur
* Always prints “Execution complete” at the end
