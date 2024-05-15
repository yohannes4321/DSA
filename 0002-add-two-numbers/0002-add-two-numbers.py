# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1=l1
        t2=l2
        dummynode=ListNode(None,None)
        dummy=dummynode
        carry=0
        while t1 or t2 :# it continues if either come to end it will not stop if both is null
            sum_value=carry
            if t1:
                sum_value += t1.val
            if t2:
                sum_value+=t2.val
            new_node=ListNode(sum_value%10)
            carry=sum_value//10
            dummy.next=new_node
            dummy=new_node
            if t1:
                t1=t1.next
            if t2:
                t2=t2.next
        
        if carry:
            new_node=ListNode(carry,None)
            dummy.next=new_node
        return dummynode.next