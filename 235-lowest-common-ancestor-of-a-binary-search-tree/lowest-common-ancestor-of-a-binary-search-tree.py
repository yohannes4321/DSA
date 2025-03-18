# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None 
        elif p.val > root.val and q.val > root.val:
            print("inside the elif frist ",root.val)
            return self.lowestCommonAncestor(root.right,p,q)
            print("inside the elif the second argument",root.val)
        elif  p.val < root.val and q.val < root.val:
            print("inside the elif frist ",root.val)
            return self.lowestCommonAncestor(root.left,p,q)
       
        else:
            return root  