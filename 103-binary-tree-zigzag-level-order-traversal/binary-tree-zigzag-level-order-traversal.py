# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #BFS
        if root==None:
            return []
        queue=deque([root])  
        general_list=[]
        index=0
        while queue:
            list_t=[] 
            for _ in range(len(queue)):
                node=queue.popleft()
                
                list_t.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            print("index",index)
            list_t=list(reversed(list_t)) if index % 2 !=0 else list_t
            index+=1
            print("list",list_t)
            general_list.append(list_t)
        return general_list

