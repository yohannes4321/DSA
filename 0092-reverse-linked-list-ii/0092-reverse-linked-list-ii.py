# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummynode=ListNode(None,head)
        prenode=dummynode
        currentnode=head
        for i in range(left-1):
            prenode=prenode.next
            currentnode=currentnode.next
        saveprenode=prenode
        savecurrent=currentnode
        prev=None
        for i in range(right-left+1):
            frontnode=currentnode.next
            currentnode.next=prev
            prev=currentnode
            currentnode=frontnode
        saveprenode.next=prev
        savecurrent.next=currentnode
        return dummynode.next
            
        