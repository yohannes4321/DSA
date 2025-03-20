# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr_sum=0
        def helper(root):
            nonlocal curr_sum
            # the base case 
            if root is None:
                return 
            helper(root.right)
            #right is finished 

            temp=root.val
            root.val+=curr_sum
            curr_sum+=temp
        

            helper(root.left)
        helper(root)
        return root
           

        return helper(root)
        