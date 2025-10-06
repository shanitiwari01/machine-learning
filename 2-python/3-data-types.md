## Python Data Types

### 📝 Explanation

In Python, **data types** define what kind of value a variable holds and what operations can be performed on it.

The **basic built-in data types** are:

1. **Numbers**

   * Integers (`int`): whole numbers → `x = 10`
   * Floating-point (`float`): decimal numbers → `pi = 3.14`
   * Complex (`complex`): numbers with real + imaginary part → `z = 2 + 3j`

2. **Text**

   * String (`str`): sequence of characters → `name = "Shani"`

3. **Boolean**

   * `True` or `False` → `is_active = True`

4. **Collections**

   * **List** (ordered, changeable) → `nums = [1, 2, 3]`
   * **Tuple** (ordered, unchangeable) → `point = (2, 3)`
   * **Set** (unordered, unique values) → `unique_nums = {1, 2, 3}`
   * **Dictionary** (key-value pairs) → `student = {"name": "Arjun", "age": 21}`

---

### 🌍 Analogy

Think of data types as **different containers in a kitchen**:

* A glass for water (float)
* A jar for sugar (int)
* A basket for fruits (list)
* A labeled box with key:content → (dictionary)

Each container is designed for a different kind of “stuff.”

---

### 📊 Example

```python
age = 25                 # int
price = 19.99            # float
name = "Shani"           # str
is_coder = True          # bool
colors = ["red", "blue"] # list
point = (3, 4)           # tuple
unique = {1, 2, 3}       # set
student = {"id": 101, "name": "Arjun"}  # dict
```

---

### ❓ Socratic Questions

1. If you need to store a list of student names, which data type would you choose?
2. Why might you use a dictionary instead of a list for student records?

---

### 🏋️‍♂️ Mini Exercise

Create variables with the following data types in Python:

* An integer age = 30
* A float salary = 55000.75
* A string city = "Mumbai"
* A list of 3 favorite fruits
* A dictionary with your name and profession

👉 Then `print()` each one.

