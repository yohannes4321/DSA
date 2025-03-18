# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root,nums):
       
            if root is None :
                return 0
            nums=nums*10 + root.val
            if root.left is None and root.right is None:
                return nums
                # this also the base case because if it is base case we gona return the sum 
            return helper(root.left,nums)+helper(root.right,nums)
        return helper(root,0)