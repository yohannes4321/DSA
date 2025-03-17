# Problem: Maximum Depth of Binary Tree - https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_el=0
        def helper(root):
            if root is None:
                return 0
            
            leftt=helper(root.left)
            rightt=helper(root.right)
            return 1+ max(leftt,rightt)
        return helper(root)
