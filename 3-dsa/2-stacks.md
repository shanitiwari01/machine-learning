## 🧠 Python DSA — Stacks

---

### 🔹 1. What is a Stack?

A **Stack** is a **linear data structure** that follows the rule:

> **LIFO (Last In, First Out)**

👉 The last element added to the stack is the first one to be removed.

---

### 🪜 Real-world Analogy

Think of a **stack of plates** 🍽️:

* You add plates on top (push).
* You remove the top plate first (pop).
* You can only access the top plate directly.

---

### 🔧 2. Core Stack Operations

| Operation   | Description               | Example           |
| ----------- | ------------------------- | ----------------- |
| `push()`    | Add an element to the top | `stack.append(x)` |
| `pop()`     | Remove the top element    | `stack.pop()`     |
| `peek()`    | View the top element      | `stack[-1]`       |
| `isEmpty()` | Check if stack is empty   | `len(stack) == 0` |

---

### 💻 3. Implementing Stack Using Python List

```python
stack = []

# Push elements
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack:", stack)

# Pop element
stack.pop()
print("After pop:", stack)

# Peek top
print("Top element:", stack[-1])
```

✅ Output:

```
Stack: [10, 20, 30]
After pop: [10, 20]
Top element: 20
```

---

### ⚙️ 4. Stack Using `collections.deque`

`deque` (double-ended queue) is more efficient for stack operations.

```python
from collections import deque

stack = deque()

stack.append('A')
stack.append('B')
stack.append('C')

print("Stack:", stack)

stack.pop()
print("After pop:", stack)
```

---

### 🧩 5. Stack Class Implementation

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage
s = Stack()
s.push(5)
s.push(10)
print("Top:", s.peek())
s.pop()
print("Stack size:", s.size())
```

✅ Output:

```
Top: 10
Stack size: 1
```

---

### 🧠 6. Where Stacks Are Used in Real Life

| Application           | Description                               |
| --------------------- | ----------------------------------------- |
| Browser history       | Back/forward navigation                   |
| Undo feature          | In text editors                           |
| Recursion             | Function call stack                       |
| Expression evaluation | Balancing parentheses, postfix evaluation |
| DFS                   | Depth-first search in graphs              |

---

### 💬 Example — Checking Balanced Parentheses

```python
def is_balanced(expr):
    stack = []
    for char in expr:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or \
               (char == ")" and stack[-1] != "(") or \
               (char == "]" and stack[-1] != "[") or \
               (char == "}" and stack[-1] != "{"):
                return False
            stack.pop()
    return not stack

print(is_balanced("{[()]}"))   # ✅ True
print(is_balanced("{[(])}"))   # ❌ False
```

---

### 🧠 Socratic Questions

1. Why is LIFO ordering useful in recursion or function calls?
2. What would happen if you try to pop from an empty stack?
3. Can you simulate a stack using only two queues? (Hint: think logically)

---

### 🏋️ Mini Exercise

Write a Python program that:

1. Pushes 5 elements into a stack
2. Removes the top 2 elements
3. Prints the current top element and the full stack
