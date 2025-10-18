## 🧩 Linked Lists

### 🧠 Concept

A **Linked List** is a **linear data structure** where elements (called **nodes**) are connected using **pointers** (or references).

Each **node** has two parts:

1. **Data** — stores the actual value.
2. **Next** — stores the address/reference to the next node in the list.

Unlike arrays or lists, linked lists **don’t store data in contiguous memory locations** — instead, each node points to the next one.

---

### 🪢 Analogy

Imagine a **treasure hunt** —
Each clue (node) tells you **what the next clue is** (the pointer).
You can’t jump directly to the 5th clue — you must follow the chain from the first clue to reach it.
That’s how a linked list works.

---

### ⚙️ Types of Linked Lists

1. **Singly Linked List** → Each node points to the *next* node only.
2. **Doubly Linked List** → Each node points to *next* and *previous* nodes.
3. **Circular Linked List** → The *last node* points back to the *first* node, forming a loop.

---

### 🧑‍💻 Example: Singly Linked List Implementation in Python

```python
# Define a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define the Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
```

**Output:**

```
10 -> 20 -> 30 -> None
```

---

### ❓ Socratic Questions

1. Why can’t we access the middle element of a linked list directly (like we do in arrays)?
2. What happens if we delete the *first node* in a singly linked list?
3. Which type of linked list allows backward traversal?

---

### 💪 Mini Exercise

Implement a method `delete(value)` in the above `LinkedList` class to delete a node with a specific value.
