# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        res=[]
        queue=deque([root])
        while queue:
            level=[]
            for _ in range(len(queue)):
                top=queue.popleft()
                print(top)
                level.append(top.val)
                print("level",level)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            level=list(reversed(level)) if len(res)%2 else level
            res.append(level)
            print(res)
        return res
