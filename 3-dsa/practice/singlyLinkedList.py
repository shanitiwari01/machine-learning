class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head

    def teraverse(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data, end = " => ")
            currentNode = currentNode.next

    def findLowestValue(self):
        currentNode = self.head
        minValue = currentNode.data
        while currentNode:
            if currentNode.data <= minValue:
                minValue = currentNode.data
            currentNode = currentNode.next

        return minValue
    
    def append(self, data):
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next
        currentNode.next = Node(data)

    def delete(self, data):
        currentNode = self.head
        prevNode = None
        while currentNode.data != data:
            prevNode = currentNode
            currentNode = currentNode.next
        print("currentNode =>", currentNode.data)
        prevNode.next = currentNode.next


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

linkedList = LinkedList(node1)

linkedList.append(6)
linkedList.append(7)
linkedList.append(8)
linkedList.append(9)

# linkedList.teraverse()

linkedList.delete(6)

linkedList.teraverse()

print(linkedList.findLowestValue())