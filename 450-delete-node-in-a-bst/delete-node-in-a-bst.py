# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #search 
        if not root:
            return None
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
            return root
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
            return root
        else:
            # delete
            if root.left is None  and root.right is None :
                return None
            elif root.right and root.left:
               right_value=self.successor(root,key)
               root.right = self.deleteNode(root.right,right_value) 
               root.val = right_value
               return root
            elif root.left:
                return root.left
            elif root.right:
                return root.right
                # left_value=self.predcessor(root,key)
                # deleteNode(root.left,key)
    def successor(self,root,key):
        root_right=root.right
        while root_right.left:
            root_right=root_right.left
        return root_right.val
    # def predcessor(self,root,key):
    #     root_left=root.left
    #     while root_left.right:
    #         root_left=root_left.right
    #     return root_left.val