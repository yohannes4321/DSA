# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        current=head
        res=[]
        # be wise the question asks the  next greater element so it is stack 
        stack=[]
        index=0 # but we donot know the length of linked list so we canot 
        while current:
            res.append(0)
            if not stack or current.val < stack[-1][0]:
                stack.append((current.val,index))
            else:
                while stack and stack[-1][0] < current.val:
                    res[stack[-1][1]]=current.val
                    stack.pop()
                stack.append((current.val,index))
            current=current.next
            index +=1
        return res
        
            