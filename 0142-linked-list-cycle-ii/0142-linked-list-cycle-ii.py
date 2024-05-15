class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        # Check if there's a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # No cycle found
            return None

        # Reset slow to head and move both pointers one step at a time
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Return the node where the cycle begins
        return slow