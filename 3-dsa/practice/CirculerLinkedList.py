class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        newNode = Node(data)
        # print(newNode.data, end="Added")
        if self.head == None:
            self.head = newNode
            self.head.next = self.head
            self.head.prev = self.head
        else:
            # lastNode = self.head.prev # Get Last Node
            self.head.prev.next = newNode # Last Next should new node
            newNode.prev = self.head.prev # New node prev should last node
            newNode.next = self.head # New Node next should first node
            self.head.prev = newNode # Now new node became last
    
    def display(self):
        temp = self.head
        while True:
            print(temp.data, end=" => ")
            temp = temp.next
            if temp == self.head:
                break
    
    def delete(self, data):
        currentNode = self.head
        while currentNode.data != data:
            currentNode = currentNode.next
        currentNode.prev.next = currentNode.next
        currentNode.next.prev = currentNode.prev


linkedList = LinkedList()

linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
linkedList.append(4)
linkedList.append(5)

linkedList.delete(2)
linkedList.delete(5)


linkedList.display()

