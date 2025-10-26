## 🧩 **Topic: Trees**

---

### 🧠 **Concept Overview**

A **Tree** is a **hierarchical data structure** that consists of **nodes** connected by **edges**.
Unlike arrays, linked lists, or hash tables — trees are *non-linear*, meaning data is stored in a branching structure.

---

### 🌱 **Terminology**

| Term       | Meaning                                           |
| ---------- | ------------------------------------------------- |
| **Root**   | The topmost node of the tree                      |
| **Parent** | A node that has child nodes                       |
| **Child**  | A node that descends from another node            |
| **Leaf**   | A node with no children                           |
| **Edge**   | Connection between two nodes                      |
| **Depth**  | Distance from the root node                       |
| **Height** | The number of edges on the longest path to a leaf |

---

### 💡 **Analogy**

Think of a **family tree**:

* You are a **node**.
* Your **parents** and **children** form edges.
* The **oldest ancestor** is the root.
* The **youngest generation** are the leaves.

---

### 🧮 **Tree Example**

Let’s visualize this:

```
        A
       / \
      B   C
     / \   \
    D   E   F
```

Here:

* `A` → Root
* `B, C` → Children of A
* `D, E, F` → Leaves

---

### ⚙️ **Python Implementation (Basic Tree Node)**

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return str(self.value)


# Create nodes
root = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')

# Build tree structure
root.add_child(b)
root.add_child(c)
b.add_child(d)
b.add_child(e)
c.add_child(f)
```

---

### 🔍 **Tree Traversals**

Tree traversal means visiting all nodes in a specific order.

#### 1️⃣ **Depth-First Search (DFS)**

Explore as far as possible along one branch before backtracking.

* **Preorder:** Root → Left → Right
* **Inorder:** Left → Root → Right
* **Postorder:** Left → Right → Root

Example (Recursive DFS):

```python
def dfs(node):
    print(node.value)
    for child in node.children:
        dfs(child)

dfs(root)
```

#### 2️⃣ **Breadth-First Search (BFS)**

Visit nodes level by level using a queue.

```python
from collections import deque

def bfs(node):
    queue = deque([node])
    while queue:
        current = queue.popleft()
        print(current.value)
        for child in current.children:
            queue.append(child)

bfs(root)
```

---

### ⚡ **Time Complexity**

| Operation | Average Case              |
| --------- | ------------------------- |
| Traversal | O(n)                      |
| Search    | O(n)                      |
| Insertion | O(1) (if reference known) |
| Deletion  | O(n)                      |

---

### 🧠 **Mini Quiz**

1. What is the difference between **DFS** and **BFS**?
2. Which traversal method uses a **queue**?
3. What is the **root** and **leaf** in a tree?
4. What is the **height** of a tree?

---

### 🏋️‍♀️ **Mini Exercise**

Create a tree that represents this structure:

```
         School
       /    |    \
   Admin  Teachers Students
                 /     \
              Alice   Bob
```

Then, perform a **DFS traversal** to print all node values.
