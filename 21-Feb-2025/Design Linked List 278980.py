# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class MyLinkedList:
    class Node:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        newnode = self.Node(val)
        newnode.next = self.head
        self.head = newnode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newnode = self.Node(val)
        if self.size == 0:
            self.head = newnode
        else:
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newnode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return  # No return value needed for addAtIndex

        if index == 0:
            self.addAtHead(val)  # Reuse addAtHead method
        elif index == self.size:
            self.addAtTail(val)  # Reuse addAtTail method
        else:
            newnode = self.Node(val)
            current = self.head
            for _ in range(index - 1):  # Find the node just before the insertion point
                current = current.next
            newnode.next = current.next
            current.next = newnode
            self.size += 1  # Increment size after successful insertion

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return  # No return value needed for deleteAtIndex

        if index == 0:
            self.head = self.head.next  # Remove the head node
        else:
            current = self.head
            for _ in range(index - 1):  # Find the node just before the one to delete
                current = current.next
            current.next = current.next.next  # Skip over the deleted node
        self.size -= 1  # Decrement size after successful deletion
