# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res=0
        def ave(node ):
            if not  node:
                return 0,0
            value_left,numl=ave(node.left )
            value_right,numr=ave(node.right )
            sum_value=value_left+value_right+node.val 
            number=numl+numr+1
            avg=sum_value//number
            if avg==node.val:
                nonlocal res
                res+=1
             
            return  sum_value,number
            
        ave(root )
        return res
          