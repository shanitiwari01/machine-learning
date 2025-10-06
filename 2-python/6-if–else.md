## 📘 Python if–else

Python’s `if`, `elif`, and `else` statements let your program **make decisions** based on conditions.
They’re like **traffic lights**—deciding whether to stop, go, or wait depending on the signal.

---

### ✅ Syntax

```python
if condition:
    # code block (executes if condition is True)
elif another_condition:
    # code block (executes if first condition is False, but this one is True)
else:
    # code block (executes if none of the above are True)
```

---

### 🔍 Example 1: Simple `if`

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

Output:

```
x is greater than 5
```

---

### 🔍 Example 2: `if...else`

```python
x = 3
if x % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

Output:

```
Odd number
```

---

### 🔍 Example 3: `if...elif...else`

```python
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")
```

Output:

```
Grade: B
```

---

### 🔎 Analogy

Think of **ordering food** at a restaurant:

* If the dish is available → you get it (`if`).
* Else if it’s not available but another option is → you get that (`elif`).
* Else → you don’t eat (`else`).

---

### 🤔 Socratic Questions

1. If `x = 0`, what will the following print?

   ```python
   if x > 0:
       print("Positive")
   elif x == 0:
       print("Zero")
   else:
       print("Negative")
   ```
2. Why do you think indentation is important in Python’s if–else statements?
3. Can you write a simple condition that checks whether a number is divisible by both 2 and 3?

---

### 📝 Mini Exercise

Write a program that:

* Takes a number `n`.
* If `n` is positive, print `"Positive"`.
* If `n` is negative, print `"Negative"`.
* If `n` is zero, print `"Zero"`.
