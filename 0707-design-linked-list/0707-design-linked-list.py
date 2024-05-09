class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        # Initialize an empty linked list with a dummy head node
        self.head = Node(None)

    def get(self, index: int) -> int:
        # Get the value of the index-th node in the linked list
        # If index is invalid, return -1
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        # Add a node of value 'val' before the first element of the linked list
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node

    def addAtTail(self, val: int) -> None:
        # Append a node of value 'val' as the last element of the linked list
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        # Add a node of value 'val' before the index-th node in the linked list
        # If index equals the length of the linked list, append the node to the end
        # If index is greater than the length, do not insert the node
        curr = self.head
        i = 0
        while curr:
            if i == index:
                new_node = Node(val)
                new_node.next = curr.next
                curr.next = new_node
                break
            curr = curr.next
            i += 1

    def deleteAtIndex(self, index: int) -> None:
        # Delete the index-th node in the linked list, if the index is valid
        curr = self.head
        i = 0
        while curr.next:
            if i == index:
                curr.next = curr.next.next
                break
            curr = curr.next
            i += 1
