## 📘 Python Operators

Operators in Python are **symbols or keywords** that tell Python to perform a specific operation on one or more values (called operands).

Think of them as the "verbs" of Python—they make numbers, variables, and data **do something**.

---

### ✅ Types of Python Operators

1. **Arithmetic Operators** → used for math
   `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `//` (floor division), `%` (modulus), `**` (power)

   Example:

   ```python
   print(10 + 3)   # 13
   print(10 / 3)   # 3.333...
   print(10 // 3)  # 3
   print(10 % 3)   # 1
   print(2 ** 3)   # 8
   ```

2. **Comparison (Relational) Operators** → compare values, return `True` or `False`
   `==`, `!=`, `>`, `<`, `>=`, `<=`

   Example:

   ```python
   print(5 > 3)   # True
   print(5 == 5)  # True
   print(5 != 2)  # True
   ```

3. **Logical Operators** → combine conditions
   `and`, `or`, `not`

   Example:

   ```python
   print(True and False)  # False
   print(True or False)   # True
   print(not True)        # False
   ```

4. **Assignment Operators** → assign values to variables
   `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`

   Example:

   ```python
   x = 5
   x += 3  # same as x = x + 3 → 8
   ```

5. **Bitwise Operators** → work at binary (bit) level
   `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), `>>` (right shift)

   Example:

   ```python
   print(5 & 3)   # 1  (binary 101 & 011 = 001)
   print(5 | 3)   # 7  (binary 101 | 011 = 111)
   ```

6. **Membership Operators** → check if a value is inside a collection
   `in`, `not in`

   Example:

   ```python
   nums = [1, 2, 3]
   print(2 in nums)      # True
   print(4 not in nums)  # True
   ```

7. **Identity Operators** → check if two objects point to the same memory location
   `is`, `is not`

   Example:

   ```python
   x = [1, 2]
   y = [1, 2]
   print(x == y)   # True (values are same)
   print(x is y)   # False (different objects in memory)
   ```

---

### 🔍 Analogy

Think of **operators like tools in a toolbox**:

* Arithmetic operators = basic tools (hammer, screwdriver).
* Comparison operators = ruler to compare sizes.
* Logical operators = decision-maker (yes/no).
* Bitwise operators = microscopic tools (work with binary).
* Membership & Identity = checking if something "belongs" or "is identical".

---

### 🤔 Socratic Questions

1. If `a = 10` and `b = 3`, what is the difference between `a / b` and `a // b`?
2. What will `not (5 > 3 and 2 < 1)` return?
3. If `x = [1,2,3]` and `y = [1,2,3]`, why is `x == y` True but `x is y` False?

---

### 📝 Mini Exercise

Write a small Python program that:

1. Takes two numbers, `a` and `b`.
2. Prints their sum, difference, product, and remainder.
3. Checks if `a` is greater than `b`.
4. Checks if `a` is in a list `[2, 4, 6, 8]`.
