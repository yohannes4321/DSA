# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count=0
        def helper(root):
            nonlocal count
            if root is None:
                return 0,0
            left_value=helper(root.left )
            right_value=helper(root.right )
            print("left_value",left_value)
            print("right_value",right_value)
            sum_value=left_value[0]+right_value[0]+root.val
            number_of_node=left_value[1]+right_value[1]+1
            if root.val==sum_value//number_of_node:
                count+=1
            return sum_value,number_of_node
        helper(root)
        
        return count 



