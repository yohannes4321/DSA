from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #we gona use breadth first search
        if not root:
            return []
        list_t=[]
        queue=deque([root])
        while queue:
            level=[]
            n=len(queue)
            for i in range(n):
                node=queue.popleft()
                level.append(node.val)
                if node.left:

                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            list_t.append(level[-1])
        return list_t