# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

from collections import deque
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        queue = deque()
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for src, des in prerequisites:
            adj_list[src].append(des)
            indegree[des] += 1
        
        reachable = [set() for _ in range(numCourses)]  # reachable[i] = set of courses i is prerequisite for
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for neigh in adj_list[node]:
                reachable[neigh] |= reachable[node]  # inherit prerequisites
                reachable[neigh].add(node)           # add direct prerequisite
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        
        ans = []
        for u, v in queries:
            ans.append(u in reachable[v])
        
        return ans
