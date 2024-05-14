# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length=0
        if not head:
            return None
        current =b=head
        while current:
            
            current=current.next
            length+=1
            
        
        index=k %length
        if index ==0:
            return head
        
        
        for i in range(length-index-1):
            b=b.next
        new_head=b.next
        b.next=None
        curr=new_head
        while curr.next:
            curr=curr.next
        curr.next=head
        return new_head
        
            
            