# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, node: Optional[TreeNode]) -> List[int]:
        result=[]
        def helper(node):
            if node==None:
                return None
            result.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(node)
        return result
                    