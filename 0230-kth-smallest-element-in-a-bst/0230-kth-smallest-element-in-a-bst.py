class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize an empty list to store the in-order traversal
        result = []
        
        def inorder(node):
            if not node:
                return
            # Traverse left subtree
            inorder(node.left)
            # Visit current node
            result.append(node.val)
            # Traverse right subtree
            inorder(node.right)
        
        # Perform in-order traversal
        inorder(root)
        # Return the k-th smallest element (1-indexed)
        return result[k - 1]