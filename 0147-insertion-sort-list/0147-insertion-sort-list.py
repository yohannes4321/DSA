# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummynode=ListNode(None,head)
        prev,curr=head,head.next
        while curr:
            if curr.val >= prev.val:
                prev,curr=curr,curr.next
                continue
            # it is single linke d so comes to the front
            temp=dummynode
            while curr and curr.val >=temp.next.val:
                temp=temp.next
            prev.next=curr.next
            curr.next=temp.next
            temp.next=curr
            curr=prev.next
        return dummynode.next
                