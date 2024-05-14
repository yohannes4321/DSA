class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        # Calculate the length of the linked list
        length = 0
        current = head
        while current:
            current = current.next
            length += 1

        # Handle the case where no rotation is needed
        index = k % length
        if index == 0:
            return head

        # Find the new head after rotation
        b = head
        for i in range(length - index - 1):
            b = b.next

        new_head = b.next
        b.next = None

        # Connect the last element to the original head
        current = new_head
        while current.next:
            current = current.next
        current.next = head

        return new_head