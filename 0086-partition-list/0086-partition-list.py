class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create dummy nodes for the left and right partitions
        left_dummy = ListNode()
        right_dummy = ListNode()
        left_tail, right_tail = left_dummy, right_dummy

        # Traverse the original list
        while head:
            if head.val < x:
                left_tail.next = head
                left_tail = left_tail.next
            else:
                right_tail.next = head
                right_tail = right_tail.next
            head = head.next

        # Connect the left and right partitions
        left_tail.next = right_dummy.next
        right_tail.next = None

        return left_dummy.next