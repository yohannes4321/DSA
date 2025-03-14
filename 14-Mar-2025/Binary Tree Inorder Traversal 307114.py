# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, node: Optional[TreeNode]) -> List[int]:
        result=[]
        def func(node):
            if node==None:
                return None 
            func(node.left)
            result.append(node.val)
            func(node.right)
        func(node)
        return result
