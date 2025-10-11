## 📘 Python Dictionary

A **dictionary** in Python is an **unordered**, **mutable**, and **indexed** collection of data stored as **key–value pairs**.

Syntax:

```python
my_dict = {
    "name": "Shani",
    "age": 27,
    "role": "Engineer"
}
```

Here:

* `"name"`, `"age"`, `"role"` are **keys**
* `"Shani"`, `27`, `"Engineer"` are **values**

---

### ✅ Accessing Dictionary Values

You can access values by their **key**:

```python
print(my_dict["name"])       # Shani
print(my_dict.get("role"))   # Engineer
```

If a key doesn’t exist:

```python
print(my_dict.get("salary", "Not found"))  # Safe way (avoids error)
```

---

### 🧱 Adding, Updating, and Deleting Items

```python
# Add new key-value
my_dict["city"] = "Mumbai"

# Update existing value
my_dict["age"] = 28

# Remove an item
my_dict.pop("role")

print(my_dict)
```

Output:

```
{'name': 'Shani', 'age': 28, 'city': 'Mumbai'}
```

---

### 🧰 Useful Dictionary Methods

| Method     | Description                 | Example                                |
| ---------- | --------------------------- | -------------------------------------- |
| `keys()`   | Returns all keys            | `my_dict.keys()`                       |
| `values()` | Returns all values          | `my_dict.values()`                     |
| `items()`  | Returns all key–value pairs | `my_dict.items()`                      |
| `update()` | Adds another dictionary     | `my_dict.update({"country": "India"})` |
| `pop(key)` | Removes specific key        | `my_dict.pop("age")`                   |
| `clear()`  | Removes all items           | `my_dict.clear()`                      |

---

### 🔁 Iterating Through a Dictionary

```python
for key, value in my_dict.items():
    print(key, ":", value)
```

Output:

```
name : Shani
age : 27
role : Engineer
```

---

### 🔍 Real-World Example

Think of a dictionary as a **mini database record**:

```python
student = {
    "name": "Shani",
    "marks": [85, 90, 88],
    "average": sum([85, 90, 88]) / 3
}
print("Average Marks:", student["average"])
```

---

### 🔎 Analogy

A **list** is like a shelf with numbered boxes 🧺 (index-based).
A **dictionary** is like a **locker room** with labeled lockers 🔐 —
you don’t care about order, you just look up by name (key).

---

### 🤔 Socratic Questions

1. What will happen if you access a key that doesn’t exist in the dictionary using `my_dict["key"]`?
2. How is a dictionary different from a list in terms of data access?
3. Can you use a list as a dictionary key? Why or why not?

---

### 📝 Mini Exercise

Create a dictionary `car` with:

```python
{
  "brand": "Tesla",
  "model": "Model 3",
  "year": 2024
}
```

Now:

1. Add a new key `"color": "Red"`
2. Update `"year"` to `2025`
3. Remove the `"model"` key
4. Print all remaining key–value pairs
