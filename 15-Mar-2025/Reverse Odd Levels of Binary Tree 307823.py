# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
       
        index=0
        queue=deque([root])
        
        while queue:
            if index % 2 !=0:
                print("index",index)
                left=0
                right=len(queue)-1
                while left<right:
                        print(len(queue))
                        print("index",left,right)
                        queue[left].val,queue[right].val=queue[right].val,queue[left].val
                        left+=1
                        right-=1
            for _ in range(len(queue)):
                top=queue.popleft()
              
                 
                if top.left:
                    
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            index+=1
        return root

                 
                     
            
       


                    

            