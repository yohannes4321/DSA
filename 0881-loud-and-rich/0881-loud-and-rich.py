from collections import deque
from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        queue = deque()
        adj_list = [[] for _ in range(len(quiet))]
        indegree = [0] * len(quiet)
        
        for src, des in richer:
            adj_list[src].append(des)
            indegree[des] += 1
        
        for i in range(len(quiet)):
            if indegree[i] == 0:
                queue.append(i)
        
        answer = [i for i in range(len(quiet))]  # Initially, everyone thinks they are their own quietest
        
        while queue:
            node = queue.popleft()
            for neigh in adj_list[node]:
                if quiet[answer[node]] < quiet[answer[neigh]]:
                    answer[neigh] = answer[node]
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        
        return answer
