# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

        dummynode=ListNode(-1,None) # first let make the dummy node connect to theue null pointer
        tmp=dummynode
        t1=list1
        t2=list2
        while t1 and t2:
            if t1.val < t2.val:
                tmp.next=t1
                tmp=t1
                t1=t1.next
            else:
                tmp.next=t2
                tmp=t2
                t2=t2.next
        if t1:
            tmp.next=t1
        else:
            tmp.next=t2
        return dummynode.next