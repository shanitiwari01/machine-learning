## 📘 Python Lists

A **list** in Python is an **ordered, mutable (changeable)** collection that can hold multiple items — even of **different data types**.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["AI", 42, True, 3.14]
```

Lists are written inside **square brackets `[ ]`**.

---

### ✅ Accessing List Elements

Lists are **indexed**, just like strings.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
print(fruits[-1])  # cherry (last element)
```

You can also **slice** lists:

```python
print(fruits[0:2])  # ['apple', 'banana']
print(fruits[1:])   # ['banana', 'cherry']
```

---

### 🧱 Modifying Lists

Lists are **mutable**, meaning you can change them after creation.

```python
fruits[1] = "mango"
print(fruits)  # ['apple', 'mango', 'cherry']
```

You can also **add** or **remove** elements:

```python
fruits.append("orange")        # Add to end
fruits.insert(1, "grape")      # Add at specific index
fruits.remove("apple")         # Remove by value
popped = fruits.pop()          # Remove last item
print(fruits)
```

---

### 🧰 Common List Methods

| Method         | Description                                      | Example              |
| -------------- | ------------------------------------------------ | -------------------- |
| `append()`     | Adds element to end                              | `nums.append(6)`     |
| `insert(i, x)` | Inserts at index `i`                             | `nums.insert(2, 10)` |
| `remove(x)`    | Removes first occurrence of x                    | `nums.remove(3)`     |
| `pop(i)`       | Removes item at index `i` (or last if not given) | `nums.pop()`         |
| `sort()`       | Sorts list                                       | `nums.sort()`        |
| `reverse()`    | Reverses list                                    | `nums.reverse()`     |
| `len()`        | Returns length                                   | `len(nums)`          |

---

### 🔁 Iterating Through a List

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

Output:

```
apple
banana
cherry
```

---

### 🔍 Real-World Example

You can use lists to store **student names**, **scores**, or **data fetched from APIs**.

```python
students = ["Shani", "Aarav", "Meera"]
scores = [85, 90, 78]
for i in range(len(students)):
    print(students[i], "scored", scores[i])
```

---

### 🔎 Analogy

Think of a **list** like a **shopping bag** —
you can add, remove, rearrange, or check items anytime.

Each item has its **position (index)** inside the bag.

---

### 🤔 Socratic Questions

1. What happens if you access an index that doesn’t exist in a list?
2. How is a list different from a string?
3. Can a list contain another list? What would that look like?

---

### 📝 Mini Exercise

Create a list of your 5 favorite movies:

1. Add one more movie to the list.
2. Remove the second movie.
3. Sort the list alphabetically.
4. Print the final list.
