# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node,left_path,right_path):
            if not node:
                return True
            if not(left_path<node.val<right_path):
                return False
            return (valid(node.left,left_path,node.val) and
                   valid(node.right,node.val,right_path))
            
        return valid(root, float('-inf'),float('inf')  )  
            
 
    
    