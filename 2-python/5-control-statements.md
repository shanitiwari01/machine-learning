## 📘 Python Control Statements

Control statements in Python help you **change the flow of execution** inside loops (`for`, `while`).
They act like *traffic signals* — deciding whether to continue, skip, or stop the loop.

---

### ✅ Types of Control Statements

1. **break** → **exits** the loop completely.

   ```python
   for i in range(1, 6):
       if i == 3:
           break
       print(i)
   # Output: 1, 2
   ```

   🔎 Analogy: Imagine leaving a movie theater in the middle of the film (you stop completely).

---

2. **continue** → **skips** the current iteration and moves to the next one.

   ```python
   for i in range(1, 6):
       if i == 3:
           continue
       print(i)
   # Output: 1, 2, 4, 5
   ```

   🔎 Analogy: You skip a song in a playlist but keep listening to the rest.

---

3. **pass** → does nothing; it’s a **placeholder** to avoid errors.

   ```python
   for i in range(1, 6):
       if i == 3:
           pass
       print(i)
   # Output: 1, 2, 3, 4, 5
   ```

   🔎 Analogy: A blank page in a book — it doesn’t add info but keeps the flow intact.

---

### 🔍 Real-World Example

Imagine a teacher taking attendance:

* If a student is present → mark ✅.
* If absent → **continue** (skip to next student).
* If a fire alarm rings → **break** (stop attendance immediately).
* If unsure about a student → **pass** (do nothing for now).

---

### 🤔 Socratic Questions

1. What will happen if you use `break` inside a loop?
2. If you want to **skip printing odd numbers** but keep the loop running, which control statement would you use?
3. Why might you use `pass` inside an unfinished function?

---

### 📝 Mini Exercise

Write a Python loop from 1 to 10 that:

1. Skips printing the number **5**.
2. Stops completely when it reaches **8**.
3. For all other numbers, just prints them.
