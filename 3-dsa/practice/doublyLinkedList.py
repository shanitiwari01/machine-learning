class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, node):
        self.head = node
    
    def append(self, data):
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = Node(data)
        currentNode.next.prev = currentNode
    
    def display(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end="=>")
            currentNode = currentNode.next
    
    def delete(self, data):
        currentNode = self.head
        while currentNode.data != data:
            currentNode = currentNode.next
        currentNode.prev.next = currentNode.next
        currentNode.next.prev = currentNode.prev

linkedList = LinkedList(Node(1))
linkedList.append(2)
linkedList.append(3)
linkedList.append(4)
linkedList.append(5)

linkedList.display()

linkedList.delete(3)
linkedList.delete(2)

linkedList.display()
