# Problem: Detonate the Maximum Bombs - https://leetcode.com/problems/detonate-the-maximum-bombs/description/

from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        #adj_list
        graph=defaultdict(list)
        n=len(bombs)
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                if (x1 - x2)**2 + (y1 - y2)**2 <= r1**2:
                    graph[i].append(j) 
        visted=set()
        max_el=0
        def dfs(val,visted,graph):
            visted.add(val)
            for neigh in graph[val]:
                if neigh not in visted:
                    dfs(neigh,visted,graph)
        for i in range(n):
            visted=set()
            dfs(i,visted,graph)
            max_el=max(max_el,len(visted))
        return max_el