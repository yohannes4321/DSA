# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #this idea is mind blowing i canot think but 
    # the secret is we gona have two pointers slow and fast 
    # 2 steps from  the last element means we will make right pointer 2 + fast and slow start from the beggineing
    #when the finsh the fast go to last element the slow come in the one node before the deleting element
        dumy_node=ListNode(None,head)
        fast=slow=dumy_node
        for i in range(n):
            fast=fast.next
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dumy_node.next
