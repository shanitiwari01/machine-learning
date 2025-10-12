## 📘 Python File Handling

---

### 🧠 What is File Handling?

File handling allows Python programs to **interact with files** — reading data from them, writing data to them, or updating existing files.

Common use cases:

* Saving logs
* Storing user data
* Reading configuration files
* Writing reports or CSVs

---

### ⚙️ Basic File Operations in Python

| Mode  | Description                      |
| ----- | -------------------------------- |
| `'r'` | Read (default)                   |
| `'w'` | Write (overwrites file)          |
| `'a'` | Append (adds to file)            |
| `'x'` | Create new file, error if exists |
| `'b'` | Binary mode                      |
| `'t'` | Text mode (default)              |

---

### 🪶 1. Opening a File

```python
file = open("example.txt", "r")  # open file in read mode
content = file.read()
print(content)
file.close()  # always close file after use
```

---

### ✅ 2. The Better Way — Using `with` Statement

Using `with` automatically closes the file after execution (even if an error occurs).

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

No need to call `file.close()`.

---

### ✍️ 3. Writing to a File

```python
with open("notes.txt", "w") as file:
    file.write("Hello, Shani!\nWelcome to Python file handling.")
```

**Note:**

* `'w'` **overwrites** the file every time.
* Use `'a'` to **append** data instead.

```python
with open("notes.txt", "a") as file:
    file.write("\nThis line is appended.")
```

---

### 📖 4. Reading Lines One by One

```python
with open("notes.txt", "r") as file:
    for line in file:
        print(line.strip())
```

---

### 📜 5. Reading Files — Different Methods

| Method        | Description                 |
| ------------- | --------------------------- |
| `read()`      | Reads entire file           |
| `readline()`  | Reads one line              |
| `readlines()` | Reads all lines into a list |

Example:

```python
with open("notes.txt", "r") as file:
    lines = file.readlines()
    print(lines)
```

---

### 🧩 6. Handling File Errors (with try–except)

```python
try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
```

---

### 🌍 Analogy

Think of file handling like **opening a notebook**:

* `'r'` → You’re just *reading* it.
* `'w'` → You’re *erasing* everything and *rewriting*.
* `'a'` → You’re *adding notes* to the end.
* Always *close* it when done — or use `with` so Python closes it for you.

---

### 🧠 Socratic Questions

1. Why do you think we use `with open()` instead of `open()` and `close()` manually?
2. What would happen if you open a file in `'w'` mode that already exists?
3. What is the difference between `readline()` and `readlines()`?

---

### 🏋️ Mini Exercise

Write a Python script that:

1. Creates a file `student.txt`.
2. Writes three lines: your name, favorite language, and a motivational quote.
3. Reads back the file and prints all lines.
