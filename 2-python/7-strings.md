## Python Strings

A **string** in Python is simply a **sequence of characters** enclosed in quotes.
It can contain letters, numbers, symbols, and even spaces.

```python
name = "Shani"
greeting = 'Hello, World!'
```

Python lets you use **single (' ')**, **double (" ")**, or **triple quotes (''' ''' / """ """)** for multi-line text.

```python
note = """This is
a multi-line
string."""
```

---

### ✅ String Basics

1. **Accessing Characters** (Indexing)
   Each character has a **position (index)** starting from 0.

   ```python
   word = "Python"
   print(word[0])  # P
   print(word[-1]) # n
   ```

2. **Slicing Strings**
   Extract part of a string using `[start:end]` (end is excluded).

   ```python
   print(word[0:3])  # Pyt
   print(word[2:])   # thon
   print(word[:4])   # Pyth
   ```

3. **String Length**

   ```python
   print(len("Hello"))  # 5
   ```

4. **String Concatenation & Repetition**

   ```python
   print("AI" + " " + "Rocks")   # AI Rocks
   print("Hi! " * 3)             # Hi! Hi! Hi!
   ```

---

### 🧰 Useful String Methods

| Method      | Description             | Example                                    |
| ----------- | ----------------------- | ------------------------------------------ |
| `lower()`   | converts to lowercase   | `"HELLO".lower()` → `"hello"`              |
| `upper()`   | converts to uppercase   | `"hi".upper()` → `"HI"`                    |
| `strip()`   | removes spaces          | `"  hi  ".strip()` → `"hi"`                |
| `replace()` | replaces part of string | `"AI is cool".replace("cool", "powerful")` |
| `split()`   | splits string into list | `"a,b,c".split(",")` → `['a','b','c']`     |
| `join()`    | joins list into string  | `"-".join(['a','b'])` → `"a-b"`            |

---

### 🔍 Real-World Example

```python
username = " shani_tiwari "
clean_username = username.strip().lower()
print("Welcome,", clean_username)
```

Output:

```
Welcome, shani_tiwari
```

This is similar to cleaning user input before storing or comparing it.

---

### 🔎 Analogy

Think of a **string** like a **necklace** — each bead (character) is connected in a specific order.
You can **slice** the necklace, **replace** beads, or **count** them — but they always stay connected in a sequence.

---

### 🤔 Socratic Questions

1. What will `"Python"[1:4]` output?
2. Why do you think strings are *immutable* in Python (can’t be changed once created)?
3. What is the difference between `"hi" + "there"` and `"hi" * 3`?

---

### 📝 Mini Exercise

Write a short Python program that:

1. Takes a name as input.
2. Removes extra spaces.
3. Capitalizes the first letter.
4. Prints `"Hello, <Name>!"`
