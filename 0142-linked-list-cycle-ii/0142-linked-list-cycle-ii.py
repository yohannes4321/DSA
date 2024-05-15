class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        # Check if there's a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None
    
