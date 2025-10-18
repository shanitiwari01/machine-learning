## 🧠 Queues

---

### 🔹 1. What is a Queue?

A **Queue** is a **linear data structure** that follows the rule:

> **FIFO (First In, First Out)**

✅ The element added **first** is removed **first** — just like people standing in a line at a movie ticket counter 🎟️.

---

### 🪶 Real-world Analogy

Imagine you’re in a **queue at Starbucks** ☕:

* The first person to join the line gets served first.
* The new person joins at the end of the line.

That’s how **Queue** works in programming.

---

### ⚙️ 2. Core Queue Operations

| Operation   | Description                   | Example           |
| ----------- | ----------------------------- | ----------------- |
| `enqueue()` | Add element to the rear       | `queue.append(x)` |
| `dequeue()` | Remove element from the front | `queue.pop(0)`    |
| `front()`   | Get first element             | `queue[0]`        |
| `rear()`    | Get last element              | `queue[-1]`       |
| `isEmpty()` | Check if queue is empty       | `len(queue) == 0` |

---

### 💻 3. Implementing Queue Using Python List

```python
queue = []

# Enqueue elements
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue:", queue)

# Dequeue
queue.pop(0)
print("After dequeue:", queue)
```

✅ Output:

```
Queue: ['A', 'B', 'C']
After dequeue: ['B', 'C']
```

⚠️ Note: Using `pop(0)` is **inefficient** for large queues — it takes O(n) time because it shifts all elements.

---

### ⚙️ 4. Efficient Queue — Using `collections.deque`

`deque` (double-ended queue) from `collections` is **fast and efficient** for queues.

```python
from collections import deque

queue = deque()

queue.append('A')
queue.append('B')
queue.append('C')

print("Queue:", queue)

queue.popleft()  # dequeue
print("After dequeue:", queue)
```

✅ Output:

```
Queue: deque(['A', 'B', 'C'])
After dequeue: deque(['B', 'C'])
```

---

### 🧱 5. Queue Implementation Using a Class

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return "Queue is empty"

    def front(self):
        return self.items[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Front:", q.front())
q.dequeue()
print("Queue size:", q.size())
```

✅ Output:

```
Front: 10
Queue size: 2
```

---

### 🧩 6. Variations of Queues

| Type                           | Description                                       |
| ------------------------------ | ------------------------------------------------- |
| **Simple Queue**               | Basic FIFO queue                                  |
| **Circular Queue**             | Last node connects back to first node             |
| **Priority Queue**             | Each element has a priority; highest served first |
| **Deque (Double-ended Queue)** | Insertion/removal at both ends                    |

---

### ⚙️ 7. Priority Queue Example

```python
import heapq  # built-in priority queue (min-heap)

queue = []
heapq.heappush(queue, (2, "Low priority"))
heapq.heappush(queue, (1, "High priority"))
heapq.heappush(queue, (3, "Very Low priority"))

while queue:
    print(heapq.heappop(queue))
```

✅ Output:

```
(1, 'High priority')
(2, 'Low priority')
(3, 'Very Low priority')
```

---

### 🌍 Real-world Use Cases

| Application              | Example                    |
| ------------------------ | -------------------------- |
| OS process scheduling    | FIFO task execution        |
| Print queue              | Documents printed in order |
| Messaging systems        | Kafka, RabbitMQ, AWS SQS   |
| Customer service systems | Serve customers in order   |

---

### 🧠 Socratic Questions

1. Why is FIFO important in real-world systems like task scheduling or messaging?
2. What happens if you try to dequeue from an empty queue?
3. When would you prefer a **deque** over a simple **list-based** queue?

---

### 🏋️ Mini Exercise

Write a program that:

1. Creates an empty queue
2. Enqueues 5 elements
3. Dequeues 2 elements
4. Prints the current **front element**, **remaining size**, and **queue items**
