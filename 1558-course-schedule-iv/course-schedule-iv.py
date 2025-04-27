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
        
        reachable=[set() for _ in range(numCourses)] # reachable[i] = set of courses i is prerequisite for
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for neigh in adj_list[node]:
                reachable[neigh] |= reachable[node]
                reachable[neigh].add(node)
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        
        ans = []
      
        for u, v in queries:
            ans.append(True if u in reachable[v] else False)
        
        return ans
