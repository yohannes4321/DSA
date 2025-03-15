# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # breadth first search
        if root is None:
            return []
        queue=deque([root])
        all_element=[]
        while queue:
            max_element=float('-inf')
            for _  in range(len(queue)):
                top=queue.popleft()
                max_element=max(max_element,top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            all_element.append(max_element)
        return all_element