class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Initialize pointers
        slow = fast = head

        # Move pointers
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        while slow:
            front = slow.next
            slow.next = prev
            prev = slow
            slow = front

        # Compare first half with reversed second half
        left, right = head, prev
        while left and right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True