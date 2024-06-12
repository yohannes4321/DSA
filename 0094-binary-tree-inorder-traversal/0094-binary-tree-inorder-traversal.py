# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        list_t=[]
        def inorder(node:Optional[TreeNode]):
            if node:
                inorder(node.left)
                list_t.append(node.val)
                inorder(node.right)

        inorder(root)
        return list_t