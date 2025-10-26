from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        aggregatedNum = self.reverseNodeAndConvertToNum(l1) + self.reverseNodeAndConvertToNum(l2)
        
        head = tail = None
        for char in str(aggregatedNum)[::-1]:
            node = ListNode(int(char))
            if head is None:
                head = tail = node
            else:
                tail.next = node
                tail = node
        return head

    def reverseNodeAndConvertToNum(self, listNode: Optional[ListNode]) -> int:
        listNum = ''
        tempNode = listNode
        while tempNode:
            listNum += str(tempNode.val)
            tempNode = tempNode.next
        return int(listNum[::-1])

# Local test
def printList(node: Optional[ListNode]):
    while node:
        print(node.val, end=' ')
        node = node.next
    print()

listNode1 = ListNode(3, ListNode(4, ListNode(5)))
listNode2 = ListNode(3, ListNode(4, ListNode(5)))

solution = Solution()
result = solution.addTwoNumbers(listNode1, listNode2)
printList(result)
