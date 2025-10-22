## 🧩 Python DSA — Hash Tables**

---

### 🧠 **Concept Overview**

A **Hash Table** is a data structure that stores data in **key–value** pairs for *fast access, insertion, and deletion.*

* Each key is **hashed** into an integer using a *hash function*.
* The hash value determines the *index (bucket)* where the value is stored.

In Python, the **`dict` (dictionary)** is the built-in implementation of a hash table.

---

### ⚙️ **How Hash Tables Work**

1. A key is passed through a **hash function**.
2. The function returns an **index** in an internal array.
3. The value is stored at that index.
4. When you query the key, the hash function finds the value in *O(1)* average time.

---

### 🧮 **Example: Dictionary as Hash Table**

```python
# Creating a hash table using dict
student_scores = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 88
}

# Accessing values
print(student_scores["Alice"])  # Output: 90

# Inserting
student_scores["David"] = 92

# Updating
student_scores["Bob"] = 89

# Deleting
del student_scores["Charlie"]

print(student_scores)
```

**Output:**

```
{'Alice': 90, 'Bob': 89, 'David': 92}
```

---

### 🔢 **Hash Function Example**

You can use Python’s built-in `hash()` to see how keys are hashed internally.

```python
print(hash("Alice"))
print(hash("Bob"))
```

⚠️ Hash values differ across sessions for security reasons.

---

### 🧩 **Handling Collisions**

When two keys map to the same index, a **collision** occurs.
Common solutions:

* **Chaining:** Store multiple items at the same index using a list.
* **Open Addressing:** Find the next free slot in the table.

**Example (Chaining Simulation):**

```python
hash_table = [[] for _ in range(10)]

def insert(table, key, value):
    index = hash(key) % len(table)
    for pair in table[index]:
        if pair[0] == key:
            pair[1] = value
            return
    table[index].append([key, value])

def get(table, key):
    index = hash(key) % len(table)
    for pair in table[index]:
        if pair[0] == key:
            return pair[1]
    return None

insert(hash_table, "apple", 10)
insert(hash_table, "banana", 20)
insert(hash_table, "grape", 30)

print(get(hash_table, "banana"))  # 20
print(hash_table)
```

---

### ⚡ **Time Complexity**

| Operation | Average Case | Worst Case |
| --------- | ------------ | ---------- |
| Insertion | O(1)         | O(n)       |
| Deletion  | O(1)         | O(n)       |
| Search    | O(1)         | O(n)       |

> Worst case happens only when many keys collide.

---

### 🔍 **When to Use Hash Tables**

* When fast *lookup/update/delete* is required.
* When you need *unique keys*.
* Perfect for caching, indexing, frequency counting, etc.

---

### 🧠 **Mini Quiz**

1. What is the average time complexity of lookup in a hash table?
2. How does Python internally implement dictionaries?
3. What happens when two keys have the same hash value?
4. What are two common techniques to resolve collisions?
