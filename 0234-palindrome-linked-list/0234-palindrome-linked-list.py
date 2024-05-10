# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
    
        if not head or not head.next:
            return True
        while fast and fast.next: # the head.next.next for the even length linkedlist
            slow=slow.next
            fast=fast.next.next

        # reverse from the secound half
        prev=None

        while slow:
            front=slow.next
            slow.next=prev
            prev=slow
            slow=front
            # the last element is prev becuse the slow is None that is why the loop ends

        left,right=head,prev
        while left and right :
            if left.val != right.val:
                return False
            left=left.next
            right=right.next
        return True
