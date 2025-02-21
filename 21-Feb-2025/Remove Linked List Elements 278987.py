# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummynode=ListNode()
        dummynode.next=head
        current =dummynode

        while current and current.next:
            if current.next.val !=val:
                current=current.next
            else:
                # current =current.next
                current.next=current.next.next# traversal
        return dummynode.next